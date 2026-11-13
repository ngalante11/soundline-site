/* Where a visitor came from. Any link into the site can carry ?s=<source> (a flyer's QR code,
   a partner's newsletter, a town-group post), ?a=h or ?a=p (the two ad tracks) or ?r=<family>
   (the referral link you hand a founding family). The tags are remembered for the visit and
   carried onto /survey/, /rsvp/ and /talk/, so the pixel, the form and the pipeline sheet all
   name the same source. Nothing here identifies a person; it names a channel. */
var FORM_SOURCE_ENTRY = "";
/* ^ Add a short-answer question to the survey form, "How did you hear about us? (code)", open the
   form's prefilled-link tool once, and paste the question's id here (it looks like entry.1234567890).
   From then on every response carries its source and the sheet can count by channel. Empty means
   the form is left exactly as it is. */

var SOUNDLINE_SOURCE = (function () {
  var KEY = 'soundline.source';
  var tags = {};
  try { tags = JSON.parse(window.sessionStorage.getItem(KEY) || '{}') || {}; } catch (e) { tags = {}; }
  try {
    var q = new URLSearchParams(window.location.search);
    ['s', 'a', 'r'].forEach(function (k) {
      var v = (q.get(k) || '').trim().toLowerCase().replace(/[^a-z0-9_.-]/g, '').slice(0, 40);
      if (v) tags[k] = v;
    });
    window.sessionStorage.setItem(KEY, JSON.stringify(tags));
  } catch (e) {}

  function track() { return tags.a === 'h' ? 'homeschool' : tags.a === 'p' ? 'public-school' : 'unknown'; }
  function label() {
    if (tags.r) return 'referral:' + tags.r;
    if (tags.s) return tags.s;
    if (tags.a) return 'ad:' + track();
    return 'direct';
  }
  function query() {
    var p = new URLSearchParams();
    ['s', 'a', 'r'].forEach(function (k) { if (tags[k]) p.set(k, tags[k]); });
    return p.toString();
  }
  function carry(url) {
    var q = query(); if (!q) return url;
    return url + (url.indexOf('?') === -1 ? '?' : '&') + q;
  }
  /* The Google Form, with the source written into its code question when FORM_SOURCE_ENTRY is set. */
  function prefill(formUrl) {
    var entry = (typeof FORM_SOURCE_ENTRY === 'string' ? FORM_SOURCE_ENTRY : '').trim();
    if (!entry || label() === 'direct') return formUrl;
    return formUrl + (formUrl.indexOf('?') === -1 ? '?' : '&') + 'usp=pp_url&' + encodeURIComponent(entry) + '=' + encodeURIComponent(label());
  }
  return { tags: tags, track: track, label: label, carry: carry, prefill: prefill };
})();

/* Survey goes through soundlineschool.com/survey (redirect page in the repo) — change the form there, not here. Every "Take the survey" link carries class="survey". */
var SURVEY_URL = "https://soundlineschool.com/survey/";
(function(){
  var links = document.querySelectorAll('a.survey');
  for (var i = 0; i < links.length; i++) {
    if (SURVEY_URL) { links[i].href = SURVEY_URL; }
    links[i].href = SOUNDLINE_SOURCE.carry(links[i].href);
    links[i].target = '_blank'; links[i].rel = 'noopener';
  }
  /* The other two doors carry the tags too. */
  var doors = document.querySelectorAll('a[href]');
  for (var j = 0; j < doors.length; j++) {
    var h = doors[j].getAttribute('href') || '';
    if (/^(https:\/\/soundlineschool\.com)?\/(rsvp|talk|build)\/?(#.*)?$/.test(h)) doors[j].href = SOUNDLINE_SOURCE.carry(doors[j].href);
  }
})();

/* Nov 12: the one action is "Ask for a call" (a.btn.call, a mailto with the questions filled in).
   rev. 11: the sticky bar steps aside while any other action button is on screen,
   so a phone never shows two yellow pills at once. Without IntersectionObserver the bar simply stays. */
(function(){
  var bar = document.querySelector('.sticky-cta'); if (!bar || !('IntersectionObserver' in window)) return;
  var others = Array.prototype.filter.call(document.querySelectorAll('a.btn.call, a.btn.survey'), function(a){ return !bar.contains(a); });
  if (!others.length) return;
  var seen = new Set();
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){ if (e.isIntersecting) seen.add(e.target); else seen.delete(e.target); });
    bar.classList.toggle('off', seen.size > 0);
  }, {threshold: .6});
  others.forEach(function(a){ io.observe(a); });
})();

/* Measurement. Nothing loads and nothing is sent until ANALYTICS_DOMAIN is set below.
   Set it to "soundlineschool.com" after creating the site in Plausible (no cookie banner
   needed; no personal data leaves the page). Until then this block is a no-op, and the
   click tracking below simply does nothing. */
var ANALYTICS_DOMAIN = "";

(function(){
  if (!ANALYTICS_DOMAIN) return;
  var s = document.createElement('script');
  s.defer = true; s.setAttribute('data-domain', ANALYTICS_DOMAIN);
  s.src = 'https://plausible.io/js/script.outbound-links.tagged-events.js';
  document.head.appendChild(s);
  window.plausible = window.plausible || function(){ (window.plausible.q = window.plausible.q || []).push(arguments); };
})();

/* The four things worth counting on a pre-enrollment site: who starts the survey, who
   takes the packet, who writes to us, and who asks for a call. Tagged here rather than in
   the markup so the pages stay clean and a new page gets it for free. Every goal carries
   the source tag, so a flyer and a Facebook post can be told apart. */
(function(){
  function goal(name, props){
    if (!ANALYTICS_DOMAIN || !window.plausible) return;
    props = props || {}; props.source = SOUNDLINE_SOURCE.label();
    window.plausible(name, {props: props});
  }
  function page(){ return location.pathname.replace(/index\.html$/, '') || '/'; }
  document.addEventListener('click', function(e){
    var a = e.target && e.target.closest ? e.target.closest('a') : null;
    if (!a || !a.getAttribute) return;
    var href = a.getAttribute('href') || '';
    if (a.classList.contains('call'))                                      goal('Call request', {from: page()});
    else if (a.classList.contains('survey') || /\/survey\/?($|\?)/.test(href)) goal('Survey start', {from: page()});
    else if (/\/talk\/?($|\?)/.test(href))                                 goal('Call page', {from: page()});
    else if (/\.pdf($|\?)/.test(href))                                     goal('Packet download', {from: page()});
    else if (/^mailto:/.test(href))                                        goal('Email us', {from: page()});
    else if (/^tel:/.test(href))                                           goal('Call us', {from: page()});
  }, true);
})();
