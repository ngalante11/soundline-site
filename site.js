/* Survey goes through soundlineschool.com/survey (redirect page in the repo) — change the form there, not here. Every "Take the survey" link carries class="survey". */
var SURVEY_URL = "https://soundlineschool.com/survey/";
(function(){
  var links = document.querySelectorAll('a.survey');
  for (var i = 0; i < links.length; i++) {
    if (SURVEY_URL) { links[i].href = SURVEY_URL; }
    links[i].target = '_blank'; links[i].rel = 'noopener';
  }
})();

/* rev. 10: the fathom rail — a depth map of the page. Ticks are sections; the lead is where you are. */
(function(){
  if (!window.matchMedia || !matchMedia('(min-width:66rem)').matches) return;
  var secs = document.querySelectorAll('[data-fathom]'); if (!secs.length) return;
  var rail = document.createElement('div'); rail.className = 'fathom'; rail.setAttribute('aria-hidden','true');
  var lead = document.createElement('div'); lead.className = 'lead';
  var fm = document.createElement('div'); fm.className = 'fm';
  rail.appendChild(lead); rail.appendChild(fm); document.body.appendChild(rail);
  var ticks = [];
  function layout(){
    var H = rail.clientHeight, docH = document.documentElement.scrollHeight - innerHeight; if (docH <= 0) docH = 1;
    rail.querySelectorAll('.tick').forEach(function(t){ t.remove(); }); ticks = [];
    secs.forEach(function(s){
      var y = s.getBoundingClientRect().top + scrollY; var p = Math.min(1, y / docH);
      var t = document.createElement('div'); t.className = 'tick'; t.style.top = (p * H) + 'px';
      var a = document.createElement('a'); a.href = '#' + (s.id || ''); a.textContent = s.getAttribute('data-fathom');
      a.addEventListener('click', function(e){ e.preventDefault(); s.scrollIntoView({behavior:'smooth'}); });
      t.appendChild(a); rail.appendChild(t); ticks.push({el:t, y:y});
    });
    move();
  }
  function move(){
    var docH = document.documentElement.scrollHeight - innerHeight; if (docH <= 0) docH = 1;
    var p = Math.min(1, scrollY / docH); lead.style.top = (p * rail.clientHeight) + 'px';
    fm.style.top = (p * rail.clientHeight) + 'px'; fm.textContent = (p * 10).toFixed(1) + ' fm';
    ticks.forEach(function(t){ t.el.classList.toggle('near', Math.abs(t.y - scrollY) < innerHeight * .5); });
  }
  addEventListener('scroll', move, {passive:true}); addEventListener('resize', layout); addEventListener('load', layout); layout();
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
