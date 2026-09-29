# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->
I picked the city_guides corpus, which contains guides about towns, transportation, food, accommodation, accessibility, and other travel information. The system retrieves relevant markdown sections from these guides and uses them to answer specific questions about the region. It is designed to give answers grounded in the documents rather than relying on outside information.

## Chunking Strategy

**Chunk size:** 700 Characters
**Overlap:** 0 Characters

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->
I chose a maximum of about 700 characters because the city guides are organized into sections with markdown headings such as "Getting there," "Getting around," and "Where to stay." I kept the heading with its related content and combined short sections so that chunks would contain enough context to answer questions on their own. I used no overlap because the sections already provide natural boundaries, so repeating text between chunks would add duplication without much benefit.

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `guide_accessibility.md#0` — produced by: `chunker.py::split_documents`

```

# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.
```

**Chunk 2** — source: `guide_corry_vale.md#1` — produced by: `chunker.py::split_documents`

```

## Getting around

Nothing within the valley is walkable from anything else — the villages are two to four miles apart. There is one taxi, based in the largest village, and it must be booked a day ahead. Most visitors drive between villages and walk the footpaths in between.

## Eat and drink

One pub in the largest village serves food seven days a week. A second, in the third village, opensThursday to Sunday. There is a farm shop at the valley mouth that sells bread, cheese and little else, and it closes at 4pm. Bring supplies; this is not a place with options.
```

**Chunk 3** — source: `guide_givens_mill.md#0` — produced by: `chunker.py::split_documents`

```

# Givens Mill

Givens Mill is a village of 700 built around a working watermill that still grinds flour commercially. It is the sort of place people visit for an afternoon and then talk about for longer than the visit lasted.

## Getting there

No station and no bus on Sundays; four buses a day from Brightwater on weekdays, taking 30 minutes.Driving is 20 minutes. The village car park holds about forty cars and is full by 11am on summer Saturdays.

## Getting around

Everything is on one street along the river. The mill is at one end and the church at the other, eight minutes apart. The riverside path continues in both directions for as far as you want to walk.
```

**Chunk 4** — source: `guide_marchwood.md#0` — produced by: `chunker.py::split_documents`

```

# Marchwood

Marchwood is the regional hub — 180,000 people, the junction everyone changes trains at, and a citymost visitors pass through rather than stop in. That is a mistake, though an understandable one, since almost nothing of interest is near the station.

## Getting there

Every railway line in the region meets here, which is the city's defining feature. Trains to Brightwater run every 40 minutes until 11pm. The airport is 20 minutes out by a dedicated bus that runs every 15 minutes and costs more than the equivalent taxi shared between three people.
```

**Chunk 5** — source: `guide_regional_transport.md#3` — produced by: `chunker.py::split_documents`

```

## Walking and cycling

The river path from Brightwater runs four miles upstream on a good surface. The
old railway trackbed from Kestrelford runs six miles on an easy gradient and is
the best walking in the region for the effort involved. The coastal path from
Halden Bay is more serious — exposed, and closed in high wind.

Cycling is pleasant on the river path and the trackbed, and unpleasant on Mill
Road and the coast road, neither of which has a shoulder.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
What are Brightwater's Tuesday market hours?

**Answer:**

```
Brightwater's Tuesday market sets up at 7am in the square and is finished by 1pm.

Source: guide_eating.md
```

**My relevance cutoff:** 0.65

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
|  |  |  |
| What are Brightwater's Tuesday market hours? | Yes | 0.279 |
| Which month is the busiest and makes it harder to find accommodation? | Yes | 0.445 |
| Which town is the most accessible town by foot? | Yes | 0.451 |
| When is the best time to buy a train ticket for the cheapest price? | Yes | 0.602 |
| How long does it take to get from one end to the other in Thornby Wells? | Yes | 0.303 |
| What is the capital of Mongolia? | No | 0.828 |
| How do I change the oil in a diesel engine? | No | 0.912 |
| Who won the 1994 World Cup? | No | 1.000 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.846 |
| How do I write a for loop in Rust? | No | 0.843 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
I didnt use claude for this since most of my AI usage was not really code. I used ChatGPT to help me clarify some aspects of the assignment and help format some markdown documentation.

It helped me out understand certain concepts better and also sped up documenting everything and formatting it the way I wanted it. Example would be the table above with the distance data for different questions

**2.**
I also used ChatGPT to help me fine tune my chunker. I actually have a worse version commented out. The one thats implemented was tweaked by ChatGPT to save some time. I just told it to help me make it chunk by markdown headers since my corpus uses markdown files with headers a lot.

It fixed my code and made it more robust than the original. After testing and reviewing the code, I decided to keep it for now. I feel like different chunking methods for different corpus's might be a feature I might add later.

**Unit 2**
**3**
I used AI to help me format any documentation like usual and also see if any of my assumptions are on the right track. This is especially true when trying to analyze my criteria.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

Run 1–3 below are from [the September 28 run log](results/run_2026-09-28_1640_before.md)
(`run_eval.py::main`, `city_guides`, top-k 5, cutoff 0.65). The question-level
pass/fail marks in that file are the scorer's expected-phrase checks; I judged
retrieval coverage and source citations separately against their criteria.
The gate and chunk sample are deterministic, so their measurements are repeated
across the columns.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 3/5 | 4/5 | 4/5 | MISSED |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks contain enough context to answer a reasonable question | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 5. Answers contain the expected answer phrase | 4 of 5 | 2/5 | 2/5 | 2/5 | MISSED |

### Criterion 1 — Retrieved chunk contains the answer

The run log records the retrieved source names (not the full retrieved chunk
bodies). These are the exact Run 1 source lines from
`results/run_2026-09-28_1640_before.md`, produced by `run_eval.py::main`:

```
What are Brightwater's Tuesday market hours?
Sources retrieved: guide_brightwater.md, guide_eating.md, guide_regional_transport.md, guide_seasons.md

Which month is the busiest and makes it harder to find accommodation?
Sources retrieved: guide_brightwater.md, guide_elder_ness.md, guide_halden_bay.md, guide_marchwood.md, guide_thornby_wells.md

Which town is the most accessible town by foot?
Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_walking.md

When is the best time to buy a train ticket for the cheapest price?
Sources retrieved: guide_eating.md, guide_givens_mill.md, guide_kestrelford.md, guide_pellew_sands.md, guide_seasons.md

How long does it take to get from one end to the other in Thornby Wells?
Sources retrieved: guide_accessibility.md, guide_thornby_wells.md, guide_walking.md
```

I counted questions 1, 2, 3, and 5 as hits: their retrieved sources include
the market hours, September accommodation/busy-season information, the
accessible-town answer, and the Thornby Wells travel time, respectively.
Question 4 is a miss because `guide_regional_transport.md`, which contains
“Tickets are cheaper booked the day before,” was not retrieved. Retrieval is
deterministic here, so each run has the same 4/5.

### Criterion 2 — Every answer names a source

These are the actual Run 1 answers from the results file, generated by
`generate.py::answer_from_chunks` and recorded by `run_eval.py::main`:

**What are Brightwater's Tuesday market hours?**
```
Brightwater's Tuesday market sets up at 7am in the square and is finished by 1pm.
Source: guide_eating.md
```

**Which month is the busiest and makes it harder to find accommodation?**
```
Based on the provided documents, there is no mention of a month that makes it harder to find accommodation (the documents only note that July and August are busy for parking in Halden Bay, and that conference weeks in March and October fill hotels in Marchwood). Therefore, I do not have enough information to answer this question.
```

**Which town is the most accessible town by foot?**
```
**Thornby Wells** is the region's most accessible town on foot (from `guide_walking.md` and `guide_accessibility.md`).
```

**When is the best time to buy a train ticket for the cheapest price?**
```
I don't have enough information to answer your question from the provided documents.
```

**How long does it take to get from one end to the other in Thornby Wells?**
```
It takes 15 minutes to get from one end to the other in Thornby Wells, as it is flat and compact (source: `guide_thornby_wells.md`).
```

Run 1 named a source in 3/5 answers. In Runs 2 and 3, the accommodation answer
also named its source, bringing those counts to 4/5; the train-ticket answers
did not name one in any run.

### Criterion 3 — Gate stops out-of-corpus questions

Actual deterministic gate output from `results/run_2026-09-28_1640_before.md`,
produced by `run_eval.py::check_out_of_scope`:

```
Produced by run_eval.py::check_out_of_scope, cutoff 0.65. Refused 5 of 5.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.828 | refused |
| How do I change the oil in a diesel engine? | 0.912 | refused |
| Who won the 1994 World Cup? | 1.000 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.846 | refused |
| How do I write a for loop in Rust? | 0.843 | refused |
```

For each refused question, `run_eval.py::run_once` returns the refusal defined
by `gate.py::REFUSAL`:

```
I don't have enough information about that.
```

### Criterion 4 — Chunk context

These are the actual sample chunks produced by `chunker.py::split_documents`
(the same samples shown in Unit 1):

```
Chunk 1 — guide_accessibility.md#0
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.

Chunk 2 — guide_corry_vale.md#1
## Getting around

Nothing within the valley is walkable from anything else — the villages are two to four miles apart. There is one taxi, based in the largest village, and it must be booked a day ahead. Most visitors drive between villages and walk the footpaths in between.

## Eat and drink

One pub in the largest village serves food seven days a week. A second, in the third village, opensThursday to Sunday. There is a farm shop at the valley mouth that sells bread, cheese and little else, and it closes at 4pm. Bring supplies; this is not a place with options.

Chunk 3 — guide_givens_mill.md#0
# Givens Mill

Givens Mill is a village of 700 built around a working watermill that still grinds flour commercially. It is the sort of place people visit for an afternoon and then talk about for longer than the visit lasted.

## Getting there

No station and no bus on Sundays; four buses a day from Brightwater on weekdays, taking 30 minutes.Driving is 20 minutes. The village car park holds about forty cars and is full by 11am on summer Saturdays.

## Getting around

Everything is on one street along the river. The mill is at one end and the church at the other, eight minutes apart. The riverside path continues in both directions for as far as you want to walk.

Chunk 4 — guide_marchwood.md#0
# Marchwood

Marchwood is the regional hub — 180,000 people, the junction everyone changes trains at, and a citymost visitors pass through rather than stop in. That is a mistake, though an understandable one, since almost nothing of interest is near the station.

## Getting there

Every railway line in the region meets here, which is the city's defining feature. Trains to Brightwater run every 40 minutes until 11pm. The airport is 20 minutes out by a dedicated bus that runs every 15 minutes and costs more than the equivalent taxi shared between three people.

Chunk 5 — guide_regional_transport.md#3
## Walking and cycling

The river path from Brightwater runs four miles upstream on a good surface. The
old railway trackbed from Kestrelford runs six miles on an easy gradient and is
the best walking in the region for the effort involved. The coastal path from
Halden Bay is more serious — exposed, and closed in high wind.

Cycling is pleasant on the river path and the trackbed, and unpleasant on Mill
Road and the coast road, neither of which has a shoulder.
```

Chunks 2–5 give enough context to answer a reasonable question from the chunk
alone. Chunk 1 is only an introduction: it does not identify any of the
places or explain their specific accessibility, so I did not count it. That
is 4/5; the chunker output is unchanged between runs.

### Criterion 5 — Expected answer phrase

The actual Run 1 question marks in the results file, produced by
`run_eval.py::main` using `scorer.py::judge`, are:

```
What are Brightwater's Tuesday market hours? | fail
Which month is the busiest and makes it harder to find accommodation? | fail
Which town is the most accessible town by foot? | pass
When is the best time to buy a train ticket for the cheapest price? | fail
How long does it take to get from one end to the other in Thornby Wells? | pass
```

The same 2/5 result appears in Runs 2 and 3. The answers contain the expected
phrases for “Thornby Wells” and “15 minutes,” but not the exact expected
phrases “7am to 1pm,” “September,” or “The day before.”

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer in at least 4 of 5 questions | MET | Each run retrieved chunks with the answer for 4 of the 5 questions; the cheapest-ticket answer was the only one missing from the retrieved source set. |
| 2 | Every answer names a source | MISSED | Only 3/5 answers named a source in Run 1 and 4/5 in Runs 2 and 3, so none of the runs met the 5/5 target. |
| 3 | Gate stops out-of-corpus questions in at least 4 of 5 tries | MET | The deterministic gate refused all 5 out-of-corpus questions, exceeding the 4/5 target. |
| 4 | At least 4 of 5 sampled chunks contain enough context to answer a reasonable question independently | MET | Chunks 2–5 contain enough standalone context, while Chunk 1 is only an introductory section, giving 4/5. |
| 5 | At least 4 of 5 answers contain the expected phrase | MISSED | The scorer marked only 2/5 answers as containing their expected phrase in every run, below the 4/5 target. |

## Diagnoses

### Criterion 2 — Every answer names a source (MISSED)

**Stage: generation.** The retrieved results had source filenames, and
`generate.py::build_prompt` explicitly asks the model to name the file it used.
However, the generated response did not follow that instruction consistently:
the accommodation answer omitted a filename in Run 1 (then included one in
Runs 2 and 3), and all three train-ticket responses omitted one. The citation
is left to the model's answer rather than enforced after generation, so the
result varies and fails the 5/5 target.

### Criterion 5 — At least 4 of 5 answers contain the expected phrase (MISSED)

Three different mechanisms contributed to the 2/5 score:

- **Market hours — generation/scoring boundary:** The answer correctly says
  the market starts at 7am and ends at 1pm, but `scorer.py::judge` checks for
  the literal substring `7am to 1pm`. Since the generated wording does not
  contain those exact words, it is scored as a failure despite conveying the
  expected hours.
- **Busiest month — generation:** `guide_brightwater.md` was among the retrieved
  sources and says Brightwater is busiest from late September through November
  and that accommodation is thin and expensive in early September. The answers
  nevertheless say the documents do not mention a relevant month. The evidence
  reached generation, but the model failed to use it.
- **Cheapest train ticket — retrieval:** The answer requires the sentence in
  `guide_regional_transport.md` that says tickets are cheaper when booked the
  day before. That file is not among the five retrieved sources for this
  question, so generation did not receive the fact and abstained.

**Pattern:** The misses are not all caused by one stage. One failure is a
retrieval omission; the other factual miss happens after the relevant source
was retrieved. The scorer also treats a correct paraphrase of the market
hours as wrong because it checks an exact phrase. This exposes a limitation in
the phrase-based measurement, but I am keeping the original criterion and
target unchanged for this run rather than lowering it after seeing the result.

## The Improvement

**What I changed:** I increased `config.py::TOP_K` from 5 to 8 so retrieval
would pass more candidate chunks to generation.

**Why I picked it:** The cheapest-train-ticket answer was missing because
`guide_regional_transport.md`, which contains the booking advice, was not in the
top five retrieved sources; returning more chunks was intended to bring that
evidence into the prompt.

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

Run 1–3 are from [the September 28 after-run log](results/run_2026-09-28_1715_after.md),
produced by `run_eval.py::main` with `TOP_K = 8` and the same corpus and cutoff
as the before run. Retrieval and gate measurements are deterministic; criteria
2 and 5 are based on the generated answers/scorer results.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 4/5 | 4/5 | 4/5 | MISSED |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks contain enough context to answer a reasonable question | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 5. Answers contain the expected answer phrase | 4 of 5 | 2/5 | 2/5 | 2/5 | MISSED |

**Run evidence:** The full raw answers, retrieved-source lists, and gate
results are in `results/run_2026-09-28_1715_after.md`. In each run the
train-ticket question still did not retrieve `guide_regional_transport.md`;
for example, the recorded Run 1 source list is:

```
Sources retrieved: guide_brightwater.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_seasons.md

I do not have enough information in the provided documents to answer when is the best time to buy a train ticket for the cheapest price.
```

This actual output was recorded by `run_eval.py::main` after
`store.py::search` returned the top eight results. The all-question source
lists show 4/5 questions had their answer source retrieved. The gate output,
produced by `run_eval.py::check_out_of_scope`, remained:

```
Produced by run_eval.py::check_out_of_scope, cutoff 0.65. Refused 5 of 5.
```

Criterion 4 is unchanged because this retrieval setting does not alter
`chunker.py::split_documents`; the five samples and the 4/5 judgment are the
same as in the before log. The scorer output from `run_eval.py::main`, using
`scorer.py::judge`, was:

```
What are Brightwater's Tuesday market hours? | fail
Which month is the busiest and makes it harder to find accommodation? | fail
Which town is the most accessible town by foot? | pass
When is the best time to buy a train ticket for the cheapest price? | fail
How long does it take to get from one end to the other in Thornby Wells? | pass
```

The same marks appeared in all three runs: only the accessible-town and
Thornby Wells travel-time answers passed (2/5).

**Did it help?**

Only partially. Source attribution improved from 3/5 to 4/5 in Run 1 and
stayed at 4/5 in Runs 2 and 3, but it still missed the 5/5 target. The change
did not fix the intended retrieval miss: `guide_regional_transport.md` was
still absent from the top eight, and the train-ticket answer remained
unanswered. Retrieval coverage stayed at 4/5, the expected-phrase score stayed
at 2/5, and the gate stayed at 5/5.

## What's Still Broken

**Criterion 2 — source citations:** This still missed the 5/5 target; all
three after-runs named a source in only 4/5 answers. The train-ticket answer
never cites a source because its evidence was not retrieved, and the other
answers show that relying on the model to follow the citation instruction is
not fully reliable. I would improve retrieval for the railway question and
then enforce a source citation in the answer format, checking that cited
filenames come from the retrieved chunks. I stopped after changing `TOP_K`
because this milestone required measuring one change at a time; adding a
citation rule or another retrieval change now would make it unclear which
change caused any difference.

**Criterion 5 — expected answer phrase:** This stayed at 2/5 in every
after-run, below the 4/5 target. The train-ticket fact was still missing from
the retrieved chunks, and the accommodation answer still failed to use
retrieved evidence about September. I would first make retrieval surface the
railway advice, then inspect the generated answer for the accommodation
question. I would also revise the scorer so it accepts clearly equivalent
wording for the market hours instead of requiring the literal phrase
`"7am to 1pm"` when the answer says “from 7am ... finished by 1pm.” I stopped
after the single top-k experiment to keep the before/after comparison
interpretable; the remaining retrieval and generation changes need their own
run and evidence.

## What I'd Do Differently

I would rewrite criterion 5 to test whether each answer conveys the expected
fact, using a small set of acceptable answer variants (for example, both
“7am to 1pm” and “from 7am ... finished by 1pm”) rather than requiring one
exact substring. The current phrasing check counted a correct market-hours
answer as wrong, so it measured wording overlap as well as answer correctness.
I would keep a numerical target and define the accepted variants before
running the evaluation so the measurement remains clear and consistent.
