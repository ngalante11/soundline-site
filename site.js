/* Survey goes through soundlineschool.com/survey (redirect page in the repo) — change the form there, not here. Every "Take the survey" link carries class="survey". */
var SURVEY_URL = "https://soundlineschool.com/survey/";
(function(){
  var links = document.querySelectorAll('a.survey');
  for (var i = 0; i < links.length; i++) {
    if (SURVEY_URL) { links[i].href = SURVEY_URL; }
    links[i].target = '_blank'; links[i].rel = 'noopener';
  }
})();

/* rev. 11: the sticky survey bar steps aside while any other survey button is on screen,
   so a phone never shows two yellow pills at once. Without IntersectionObserver the bar simply stays. */
(function(){
  var bar = document.querySelector('.sticky-cta'); if (!bar || !('IntersectionObserver' in window)) return;
  var others = Array.prototype.filter.call(document.querySelectorAll('a.survey'), function(a){ return !bar.contains(a); });
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

/* The three things worth counting on a pre-enrollment site: who starts the survey, who
   takes the packet, and who writes to us. Tagged here rather than in the markup so the
   pages stay clean and a new page gets it for free. */
(function(){
  function goal(name, props){
    if (!ANALYTICS_DOMAIN || !window.plausible) return;
    window.plausible(name, props ? {props: props} : undefined);
  }
  function page(){ return location.pathname.replace(/index\.html$/, '') || '/'; }
  document.addEventListener('click', function(e){
    var a = e.target && e.target.closest ? e.target.closest('a') : null;
    if (!a || !a.getAttribute) return;
    var href = a.getAttribute('href') || '';
    if (a.classList.contains('survey') || /\/survey\/?$/.test(href))      goal('Survey start', {from: page()});
    else if (/\.pdf($|\?)/.test(href))                                     goal('Packet download', {from: page()});
    else if (/^mailto:/.test(href))                                        goal('Email us', {from: page()});
  }, true);
})();
