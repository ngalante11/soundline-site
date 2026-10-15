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
