/* Survey goes through soundlineschool.com/survey (redirect page in the repo) — change the form there, not here. Every "Take the survey" link carries class="survey". */
var SURVEY_URL = "https://soundlineschool.com/survey/";
(function(){
  var links = document.querySelectorAll('a.survey');
  for (var i = 0; i < links.length; i++) {
    if (SURVEY_URL) { links[i].href = SURVEY_URL; }
    links[i].target = '_blank'; links[i].rel = 'noopener';
  }
})();
