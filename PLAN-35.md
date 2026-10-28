# Getting to 35

Working notes, 28 Oct 2026. Companion to the site changes shipped the same day.

---

## 0. What 25 October told us

**Nobody came.** One phone conversation since, another booked. That is the whole pipeline.

This is the most useful thing that has happened, because it rules out the wrong diagnosis. Everything in §4 below assumed the problem was conversion — getting people from interest to deposit. It isn't. A free, well-designed, well-flyered public talk drew zero. **The problem is distribution: there is no list, and a cold public talk has no mechanism to fill a room.**

Three structural reasons it was always going to be a hard room to fill, worth naming so the next one doesn't inherit them:

- **No list to invite.** Flyers and a share image reach people who already follow you. A school eleven months from opening has nobody to follow it yet.
- **Sunday at 3:00** competes with every travel-sports schedule on the North Shore. 11 November at 7:00 pm is a materially better slot.
- **Nothing to act on.** No address, no price, no deadline. A parent who was interested still had no reason to move *that* week. 11 November fixes this: a number, and seats that open the same night.

### What it changes

**Do not run another empty-room event.** 11 November has fourteen days and the same list problem. Two moves, both this week:

1. **Paid is no longer optional.** Organic posts to a new page reach approximately nobody; the nine-card series running 28 Oct – 11 Nov is a drumbeat with no drum. Put $400–600 behind it, geo-fenced to Miller Place, Rocky Point, Mount Sinai, Sound Beach, Shoreham and Port Jefferson, targeted at parents of 10–14 year olds. The survey page already carries the pixel hook and the `?a=h` / `?a=p` track tags — **set `SOUNDLINE_PIXEL_ID` before the first dollar is spent**, or the spend teaches you nothing. (Also move the last social card off 11 Nov; it should land the morning of, not the evening of.)
2. **Borrow rooms instead of booking them.** The library's own event calendar and newsletter (Adam's relationship), the five town Facebook groups, Gina's dance families, the PTA bulletins. One named ask each, this week.

**And reframe the night itself.** Six families around a table is a *good* evening and a better conversion environment than sixty in rows. Plan the 11th for six, not sixty, and it cannot fail twice.

The one-day gap between the room and the number is an asset, not an accident: it gives everyone who comes on the 11th a reason to leave contact details at the door, and it gives you a second touch on the 12th that is news rather than a nudge. Collect names in the room; send the number the next morning.

### Where the leverage actually is right now

One phone call converted into a second conversation. That is a 100% hit rate on the only channel being worked, against 0% on events. **Twenty conversations before 14 January will beat three information nights.** Events are for generating conversations; they are not the product. Until there is a list, the funnel in §4 runs on the phone — structure, questions and the close are in `CALL-GUIDE.md`.

The §4 benchmarks stay as written — they are what the funnel looks like *once there is traffic*. Treat them as the model to fill, not as a forecast.

---

## 1. Why the generic playbook mostly doesn't apply

The standard "increase private school enrollment" advice assumes an operating school. Three of its four pillars are void here:

| Standard lever | Status at Soundline |
|---|---|
| Activate current families / referral credits | **Void.** Zero current families. Becomes the best channel around 15 December, once there are ten founding families to ask. |
| Shadow days | **Void.** No school to shadow, no building to shadow in. Needs a substitute (§4.3). |
| RaiseRight gift-card tuition credit | **Void.** A loyalty mechanic for enrolled families. Not a pre-launch tool. |
| Google Business Profile | **Half-void.** Can't verify an address that isn't leased. Worth claiming the day the lease signs, not before. |
| Lower the cost barrier | **This one is real — and bigger than the advice knew.** See §2. |

Also wrong for New York specifically: there is no state voucher, no ESA, no state tuition tax credit. Marketing "school choice funding" in NY the way a Florida or Arizona school would is a dead end.

---

## 2. The lever that is actually live: the federal scholarship

This is the single most important fact in the file, and it is three weeks old.

- Last year's federal tax law created a scholarship tax credit that begins **1 January 2027** — the same tax year as the September Soundline opens.
- A taxpayer gives to a non-profit scholarship granting organization (SGO) and takes a **dollar-for-dollar federal credit, up to $1,700 per person.** The SGO pays tuition scholarships to families.
- Eligibility runs to **300% of area median gross income.** Nassau–Suffolk AMI for a family of four is roughly $164,000, so the ceiling lands near half a million dollars. In Miller Place this is not a low-income program. It is nearly everyone.
- **Hochul announced on 9 October that New York will opt in.** New York is not yet on the IRS participating list — the state's election must be filed by 1 January, and the state's approved-SGO list is due to the IRS by **15 February 2027.**

Two consequences, and the second is the one with a deadline on it.

**It solves the price objection without discounting.** You never have to compete on sticker price again if a third of your families are arriving with scholarship money. This is what the pasted plan was reaching for and got wrong for NY.

**It is also a fundraising instrument that costs the donor nothing.** Up to $1,700 per taxpayer, dollar for dollar, out of their federal tax bill instead of their pocket. Forty neighbours is $68,000. A hundred is $170,000 — a real scholarship fund, raised from people who are not out a cent. No school in this market is making that pitch yet.

**Critical path — this is the most time-sensitive item in the entire plan, ahead of any marketing:**

> An SGO must be a 501(c)(3) serving at least 10 students across different schools, spending 90%+ of income on scholarships. Soundline cannot be its own SGO. **You need a named SGO partner, with Soundline on their eligible-schools list, before New York files its list on 15 February.** Miss that window and your founding families lose the entire 2027 scholarship year — the exact year you are selling them right now.
>
> Target: SGO partner identified by **1 December**, relationship signed by **15 January.** Start with the Catholic diocesan and independent-school networks already organising in NY; they will be forming SGOs this quarter and will want schools on the list.

Shipped today: `cost.html` — the full explanation, carefully hedged (New York has announced, not filed), plus the donor ask.

---

## 3. The number problem: 35 does not fit the school you are selling

The site says, in three places, **eight to ten in a grade.** Three grades is 24–30 seats. 35 is above your own published cap.

Two honest ways to resolve it, and only one of them is good:

**A. 30 full-time + 5–8 Collaborative. ← recommended.** Keeps the promise exactly as written, and the Collaborative is where the flex belongs: homeschool families come three days, so a Collaborative student does not consume a full seat or break a seminar table. It also happens to be the fastest-converting segment you have (§4.2).

**B. Raise to 11–12 per grade.** Gets you to 35 full-time and breaks the most-repeated sentence on the site. Every family who enrolled on "eight to ten" notices in September.

Pick A deliberately now, or you will arrive at B by accident in June. Shipped today: `collaborative.html`, which until this morning existed only as one card on `day.html` and one line in the FAQ — no page, no CTA, no search surface, for what should be a quarter of your enrollment.

---

## 4. The funnel, backwards from 35

Pre-launch conversion, with a building and a published price:

```
    35 enrolled September 2027
 ÷  0.85  melt between deposit and first day
 =  41 deposits
 ÷  0.33  families who attend an event and deposit (warm, founder-led: 33%; cold: 20%)
 =  125 families through an information night or a Saturday build
 ÷  0.40  survey respondents who show up to something
 =  310 completed surveys
```

**So the real target is not 35 students. It is ~310 surveys and ~125 families in a room, by 14 January.** Those are the numbers to put on a wall.

Catchment check: grades 6–8 within about twenty minutes — Miller Place ~530, Rocky Point ~620, Mount Sinai ~500, Shoreham-Wading River ~400, Port Jefferson ~250, Comsewogue ~800, Three Village ~1,300 — call it **4,400 students**, plus several hundred Suffolk homeschoolers in the band. 310 surveys is ~7% of that. Cold channels will not produce 7%. Institutions that already hold those families will.

### 4.1 Lead with the scholarship, not with the school

"Come hear about my new school" does not get you booked. **"A free session on the new federal scholarship that starts in January and what it means for Long Island families"** gets you booked at libraries, PTAs, church halls and chambers of commerce across Brookhaven between now and February — because it is genuinely useful news that nobody is covering yet, and you are the person in the room who knows it.

Soundline is the second half of every one of those talks. Target twelve bookings before 15 February.

### 4.2 The Collaborative is the fastest path to bodies

Homeschool families are already out of the system. No "leave my district" leap, no spring-decision calendar, and the site now offers them **enrollment by the term rather than the year** — which is the single thing that makes a first-year school signable for a cautious family.

Suffolk homeschool co-ops, Facebook groups and the library programs they already use. Target 8–10 of the 35, closing faster than the full-time cohort.

### 4.3 Kid-first events, not parent-first

You cannot run a shadow day. You can run the thing a shadow day is actually for: **a 90-minute Saturday build.** Adam already designs and runs exactly this format — instrument labs, escape rooms, world percussion — for libraries across Long Island. It is a proven, bookable, zero-new-work asset sitting in your own staff list.

Kids make something. Parents collect them for the last fifteen minutes and see their own child lit up. Children sell middle schools to parents far more reliably than tours do. Run one in November, December and January; a library room is free and it is already Adam's relationship.

### 4.4 The institutions that already hold your families

Gina has taught North Shore dance to this exact age group for thirty-five years. That is hundreds of families who know her name — the closest thing to a current-parent referral network a pre-launch school can have, and it is sitting unused in your About page.

Build the named list — dance studios, travel sports clubs, scouts, martial arts, private music teachers, library youth programs — and make one specific ask of each. Not "please share": a flyer on a counter and a named date.

### 4.5 Paid, last and small

$300–600/month across town Facebook groups, once `cost.html` exists to retarget against. Paid is the cheapest lever to turn on and the most expensive per enrolled student. It confirms demand; it does not create it.

---

## 5. The two things that actually gate 35

**The building.** *"We announce the building the day the lease is signed."* No parent pays a deposit on a school with no address, however good the packet is. **If the lease is not signed by 12 December, 35 is not reachable for September 2027** — and the right move is to say so in January, open at 18–22 plus the Collaborative, and keep the founding promise intact. That decision is far cheaper in January than in May.

**Measurement.** The site had no analytics of any kind. You could not have known which page, flyer or QR produced a survey. Wired today, dormant until you create the Plausible site and set one line in `site.js`.

---

## 6. Dates that are not yours to move

| Date | What |
|---|---|
| **this week** | Pixel ID set, paid campaign live, six borrowed-audience asks made. Without these the 11th is another empty room. |
| **11 Nov, 7:00 pm** | Information night, Port Jefferson Free Library. Confirmed. |
| **12 Nov** | Tuition published, founding enrollment opens. Deposit mechanism must be live — amount, refundability, payment rail. People in the room on the 11th get the number first. |
| **1 Dec** | SGO partner identified. |
| **12 Dec** | Information night. Building named, or contingency announced. |
| **1 Jan** | New York's IRS election due. Watch for it; announce it the day it lands. |
| **14 Jan** | Last information night before seats are allocated. |
| **15 Feb** | **New York's SGO list due to the IRS. Hard external deadline.** |
| **1 Apr** | Families' district busing requests due. Send pre-filled forms by 1 March. |
| **1 Jun** | IEP service requests due to the host district. |

---

## 7. Open questions, in priority order

1. ~~How many came on 25 October?~~ **Answered: nobody.** See §0 — it changes the diagnosis, not the destination.
2. ~~Nov 12 venue and time.~~ **Answered: Wednesday 11 November, 7:00 pm, Port Jefferson Free Library**, library confirmed open. Tuition and registration follow on the 12th, so the packet's date stands. Both live across the site.
3. **How many surveys are in, and what do they say?** Now the single most important unknown. Ten real responses would change the channel mix more than anything else in this file.
4. **35 = 30 + Collaborative, or a raised cap?** §3.
5. **Lease status.** §5.
6. **Deposit: how much, refundable, and on what rail?** Needed before 11 November.
7. **How many of the twenty calls are booked?** §0 and `CALL-GUIDE.md`. The phone is the live channel; everything else is still potential.
