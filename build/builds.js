/* The Saturday builds. One list, read by /build/ on the site and by the two flyers in
   print/, so a date is changed in exactly one place. Past dates drop off the page by
   themselves. `place` is what families see; "with your confirmation" until a room is booked.
   Dates are ISO so the page can compare them; `end` marks a multi-day run. */
var BUILDS = [
  { date: '2026-11-21', title: 'Instrument lab', time: '10:00 to 11:30', place: 'Address with your confirmation',
    note: 'Build an instrument that plays, out of things that were going to be thrown away. Then explain to the grown-ups why it works.' },
  { date: '2026-12-05', title: 'The Quest', time: '10:00 to 11:30', place: 'Port Jefferson, Dickens Festival weekend',
    note: 'A problem with a lock on it. Teams, clues, one way out, and you have to show your working.' },
  { date: '2026-12-12', title: 'Build, then the parents’ half hour', time: '10:00 to 12:00', place: 'Address with your confirmation',
    note: 'The December information session happens in the last half hour, in a room already full. We say where the school will be, or exactly what happens if we can’t yet.' },
  { date: '2026-12-19', title: 'World percussion: the Showcase', time: '10:00 to 11:30', place: 'Address with your confirmation',
    note: 'The whole room builds one piece together and plays it. This is what Friday looks like at Soundline.' },
  { date: '2026-12-29', end: '2026-12-31', title: 'Winter Quest, three mornings', time: '9:15 to 12:30 each day', place: 'Address with your confirmation',
    note: 'Three days, one build, and on the 31st at 11:45 you defend it in front of your parents. The hours are the Collaborative’s hours, on purpose.' },
  { date: '2027-01-09', title: 'Bring a friend', time: '10:00 to 11:30', place: 'Address with your confirmation',
    note: 'Everyone who has come before brings one person whose kid they’d want in the room with theirs. The last build before founding seats are allocated.' }
];
