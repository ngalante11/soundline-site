# Paid campaign — the 11 November room

Written 28 Oct 2026. Thirteen days of running time. Budget $500.
Goal: fill Port Jefferson Free Library on Wednesday 11 November at 7:00 pm.

---

## Set-up decisions that matter more than the copy

**Optimise for Landing Page Views, not Leads.** The pixel has no history and $500 over thirteen days will not produce the ~50 conversions a week Meta needs to leave the learning phase. Optimising for Leads on a cold pixel spends the budget teaching the algorithm nothing. Track the Lead event, don't optimise to it — you are building the pool for January, when you will have history and a reason to optimise properly.

**One campaign, three ad sets, Traffic objective.** Not Advantage+ Shopping, not Leads. Plain Traffic → website → Landing Page Views.

**Every link carries its track tag**, so the Lead event tells you which audience actually moved:

| Ad set | Link |
|---|---|
| Public-school parents | `soundlineschool.com/rsvp/?a=p` |
| Homeschool | `soundlineschool.com/rsvp/?a=h` |
| Retargeting | `soundlineschool.com/rsvp/?a=p` |

`/rsvp/` preserves the query string on the hand-off, so the tag survives to the survey page. **Set `SOUNDLINE_PIXEL_ID` in `survey/index.html` before the first dollar goes out** or none of this reports.

**Geography.** A 10-mile radius around Miller Place, or name the towns: Miller Place, Sound Beach, Rocky Point, Mount Sinai, Shoreham, Wading River, Port Jefferson, Port Jefferson Station, Setauket, East Setauket, Stony Brook, Coram, Selden, Centereach, Ridge, Middle Island. Set it to **people living in this location**, not "recently in."

**Ages 30–55**, all genders. For the public-school set, add parent targeting (Meta's bracket names move around — look for preteens 09–12 and early teens 13–15) and then let Advantage+ audience expand from it. For homeschool, keep targeting manual; the interest is narrow and expansion will waste it.

**Placements: Advantage+ on.** At this budget, hand-picking placements starves delivery.

**One caution.** Keep the federal-scholarship angle out of the cold ads. It is the strongest thing you have, but an ad about a federal tax-credit programme can get pulled into Meta's social-issues review, and a thirteen-day campaign cannot survive a three-day appeal. Save it for retargeting, where the audience is small and a pause costs little — and if it gets flagged there, you have lost nothing.

---

## Budget

| Ad set | Daily | 13 days | Why |
|---|---|---|---|
| **A · Public-school parents** | $21 | $273 | The volume play. Four ads, let Meta pick. |
| **B · Homeschool** | $8 | $104 | Small audience, highest intent, cheapest conversion. |
| **C · Retargeting** | $4 | $52 | Thin until ~5 Nov. Worth it from the 4th. |
| **Reserve** | — | $71 | Spend from 8 Nov on whichever ad is winning. |

Start A and B on the 28th. Start C on 4 November, once there is a pool to retarget.

---

## Ad set A · Public-school parents

Run all four. Meta will settle on one or two within four days; kill anything under 0.8% CTR on day four and push its budget to the leader.

### A1 — Fine on paper
*Image: `img/hero-sound-1200.jpg`*

> Your kid might be doing fine on paper and quietly checked out.
>
> Middle school is three years. They go fast.
>
> Soundline opens in Miller Place in September 2027 — grades six through eight, eight to ten in a grade, and every adult in the building knows your child by name. Two hours of practice in the morning. Four hours of making.
>
> Come hear about it. Wednesday 11 November, 7:00 pm, Port Jefferson Free Library. Free, and you can ask anything.

**Headline:** A new middle school in Miller Place
**Description:** Information night · Wed 11 Nov · 7:00 pm
**Button:** Learn more

### A2 — Nobody waits
*Image: `img/social/02-oct30-s2.png` or a practice-table shot*

> Nobody moves on until they've got it. And nobody waits once they have.
>
> At Soundline, students are grouped by skill, not by age — a sixth grader and an eighth grader can work the same thing at the same table, and each moves on when it's theirs.
>
> Grades six through eight, opening September 2027 in Miller Place. Eight to ten in a grade.
>
> Information night: Wednesday 11 November, 7:00 pm, Port Jefferson Free Library.

**Headline:** Grouped by skill, not by age
**Description:** Free information night · Port Jefferson Library
**Button:** Learn more

### A3 — The screens one
*Image: hands-on / making shot, no screens visible*

> The only screen in the room all morning belongs to the teacher.
>
> Two hours of practice at a table with a guide. Four hours of making — seminar, lab, studio. AI is taught as a subject here, never used as a shortcut.
>
> Soundline. A new school for grades six through eight, opening September 2027 in Miller Place.
>
> Come and ask us anything: Wednesday 11 November, 7:00 pm, Port Jefferson Free Library.

**Headline:** Less screen time than you'd think
**Description:** Information night · Wed 11 Nov · 7:00 pm
**Button:** Learn more

### A4 — The number
*Image: `img/social/09-nov11-h1.png`*

> Eight to ten in a grade.
>
> Small enough that there's nowhere to hide. Big enough for a real seminar. One advisor who stays with your child for all three years.
>
> Soundline opens in Miller Place in September 2027, grades six through eight, and adds a grade a year through twelfth.
>
> Wednesday 11 November, 7:00 pm, Port Jefferson Free Library. Tuition is published the next morning — everyone in the room hears the number first.

**Headline:** Eight to ten in a grade
**Description:** Free and open to all · Wed 11 Nov
**Button:** Learn more

---

## Ad set B · Homeschool

Narrow targeting: homeschooling interest, plus Suffolk County co-op and curriculum interests. No Advantage+ expansion.

### B1 — Three days
*Image: studio or build shot*

> You keep teaching your child. We take Monday, Wednesday and Friday.
>
> The Soundline Collaborative is three days a week for homeschooling families on the North Shore — same guides, same rooms, same studio, same Friday build as the full-time students. Your child comes home with you the rest of the week.
>
> Your plan stays yours. **Enrolled by the term, not by the year.**
>
> Grades six through eight, opening September 2027 in Miller Place.

**Headline:** Three days a week, by the term
**Description:** For homeschooling families · Miller Place
**Button:** Learn more

### B2 — The paperwork
*Image: `img/social/03-nov01-ask.png` or a desk/document shot*

> The paperwork is the part we can actually take off you.
>
> New York wants an IHIP, four quarterly reports and an annual assessment. For the three days your child is with us, we hand you the course descriptions in syllabus form, dated hours and attendance logs by subject, and the work itself — defended, every six weeks.
>
> The Soundline Collaborative. Monday, Wednesday, Friday. Grades six through eight, Miller Place, September 2027.

**Headline:** Course descriptions that match the IHIP
**Description:** Three days a week · By the term
**Button:** Learn more

### B3 — Kitchen table *(swap in if B1 and B2 stall)*

> A seminar needs eight people who read the same thing and disagree. A lab needs equipment nobody buys for one child.
>
> That's what the three days are for.

---

## Ad set C · Retargeting — from 4 November

Audience: anyone who hit the site in the last 90 days, plus Facebook and Instagram page engagers. Exclude anyone who fired the Lead event.

### C1 — The date
*Image: `img/social/09-nov11-h1.png`*

> You looked at Soundline. Here's the date.
>
> Wednesday 11 November, 7:00 pm. Port Jefferson Free Library, 100 Thompson Street. Free, and you can ask anything — including about the money.
>
> Tuition is published the next morning, and founding enrollment opens with it. Everyone in the room on the 11th gets the number first.

**Headline:** Wednesday 11 November, 7:00 pm
**Description:** Port Jefferson Free Library · Free
**Button:** Learn more

### C2 — The scholarship *(site visitors who reached `cost.html`)*

Run this one only to the retargeting pool, per the caution above.

> There is a new scholarship for private school tuition starting in January, and most Long Island families qualify.
>
> It begins 1 January 2027 — the same school year Soundline opens. Eligibility runs to 300% of area median income, which around here is far higher than people assume.
>
> We've written up everything we know, including the parts that aren't settled yet.

**Headline:** What it costs, honestly
**Description:** Including the January scholarship
**Button:** Learn more
**Link:** `soundlineschool.com/cost.html`

---

## What to watch, and when

**Day 4 (31 Oct).** Kill any ad under 0.8% CTR. Do not touch anything else — edits reset learning.

**Day 7 (3 Nov).** Cost per landing page view should be under $1.50 in a radius this tight. Above $2.50 and the targeting is too broad, not the copy. Narrow the radius before you rewrite anything.

**Day 10 (6 Nov).** Move the reserve to the leading ad. Switch the two best ads' copy to lead with the date rather than the idea — by now the job is reminding, not persuading.

**Last 72 hours (8–11 Nov).** Everything points at the room. If fewer than fifteen people have said they are coming, stop trying to fill it and work the phone instead: six families around a table is a good evening, and `CALL-GUIDE.md` converts better than a room does anyway.

**One honest note on reporting.** The Lead event fires when someone taps *I've sent the survey* — a self-reported confirmation. Real submissions will run higher than Meta shows. Reconcile against the Google Form responses, not the pixel.
