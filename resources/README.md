# Resources

Inventory for the **AWS Certified AI Business Strategist (AIB-C01)** prep. Same shape
as the AIP-C01 repo's `resources/README.md`: confirmed facts first, then what exists on
Skill Builder, then bank economics.

Existing contents:

- `../ExamGuide.md` — markdown extraction of the official exam guide root page
  (domain pages, in-scope and technologies pages are linked, not inlined — see below)
- `Additional_Study_Resources.md` — curated external materials, mapped to domain and
  task, with a verdict on each

All facts below fetched **2026-09-25** unless noted. Skill Builder is behind login, so
its inventory is confirmed only where marked.

---

## Official exam guide pages worth reading in full

The exam guide root is in `../ExamGuide.md`, but the pages it links are the actual
contract for what can appear. Read all six end to end.

- [Exam guide root](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01/ai-business-strategist-01.html)
- [Domain 1 — AI Fundamentals and Literacy](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01/ai-business-strategist-01-domain1.html)
- [Domain 2 — AI Strategy and Business Value Creation](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01/ai-business-strategist-01-domain2.html)
- [Domain 3 — AI Governance and Responsible AI Leadership](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01/ai-business-strategist-01-domain3.html)
- [Domain 4 — Business Readiness, Leadership, and AI Transformation](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01/ai-business-strategist-01-domain4.html)
- [Technologies and concepts that might appear](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01/aib-01-technologies-concepts.html)
- [In-scope AWS services and features](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01/aib-01-in-scope-services.html)
- [Out-of-scope AWS services and features](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01/aib-01-out-of-scope-services.html)

The in-scope list is short: Amazon Bedrock, Amazon SageMaker AI, Amazon Quick, AWS CAF,
the shared responsibility model, AWS pricing structures, Cost Explorer, Marketplace,
Pricing Calculator. Everything else is "practical context, not the subject being
tested" (AWS launch blog, quoted below).

## Confirmed exam facts

| | |
|---|---|
| Exam code | AIB-C01 |
| Category | Business (first AWS cert in this category) |
| Status | **Beta.** Registration opened 2026-09-01. Delivery begins **2026-09-29**. |
| Beta window | Beta exams generally run 1–3 months. Candidates who earn the cert **by 2027-02-15** receive the Early Adopter badge, and third-party coverage puts standard-exam GA at that date. AWS has not published the beta close date itself. |
| Beta price | **$50 USD** (standard: $100) |
| Beta format | **85 questions, 170 minutes** (cert page) |
| Standard format | **130 minutes** per the exam guide; question count not published. Beta forms carry extra unscored items, which is why the two numbers differ. |
| Question types | Multiple choice, multiple response (guide lists only these two) |
| Passing score | 700 / 1000 scaled. Compensatory — pass overall, not per domain. |
| Results | Within 5 business days, beta included (Certification FAQs + Before Testing policy) |
| **Beta retake rule** | **One attempt only.** A beta fail cannot be retaken until the standard exam is GA (Before Testing policy). |
| Validity | 3 years; passing beta earns the full credential |
| Prerequisites | None. No coding, no hands-on AWS, no prior cert. 6 months alongside AI initiatives recommended. |

**Planning implication of the one-attempt rule:** there is no 14-day retake cushion
during beta. A miss on the $50 beta means waiting for the $100 standard exam in
Feb 2027. That makes the fresh-bank discipline below matter more than it did for
AIP-C01, not less.

**Unknown:** raw-to-scaled mapping for 700. AWS does not publish it. With a
compensatory model and unscored beta items, treat ~80% raw as the comfortable margin.

## Domain weights

| Domain | Title | Weight |
|---|---|---|
| 1 | AI Fundamentals and Literacy | 24% |
| 2 | AI Strategy and Business Value Creation | **28%** |
| 3 | AI Governance and Responsible AI Leadership | 24% |
| 4 | Business Readiness, Leadership, and AI Transformation | 24% |

Flat distribution apart from Domain 2. Task-level: 3 + 3 + 3 + 4 = 13 tasks, 50 skill
statements total. On an 85-question form that is roughly 1.7 questions per skill
statement, so per-skill feedback from any single attempt is noise. Domain-level is the
finest grain worth acting on.

---

## Skill Builder inventory

Confirmed from the public cert page and launch blog. Item-level detail (lengths,
free/paid tier) is behind login — **fill in from the enrolled plan.**

### Exam Prep Plan — [link](https://skillbuilder.aws/category/exam-prep/ai-business-strategist-business-AIB-C01)

| Item | Status | Notes |
|---|---|---|
| Exam Prep Overview | ✅ done | |
| Exam prep course content (~15 hours, all knowledge checks) | ✅ done 2026-09 | "Generally crushing it" — no miss capture was taken. See Additional_Study_Resources.md for how to recover signal from this. |
| **Official Practice Question Set** | ✅ done, **90%** before the course | Cert page lists it. Standard AWS size is 20 questions, so 90% ≈ 18/20. Small sample; a 2-question swing is 10 points. |
| Practice Question Meeting Simulator | ? | Listed on the cert page. New format for this exam. Unknown whether taken. |
| Official Practice Exam | **not available during beta** | Cert page says so explicitly. There is no full-length AWS-authored measurement until standard GA. |
| Exam Prep Summary | ? | |

### AI Business Strategist Learning Plan — [link](https://skillbuilder.aws/learning-plan/TSP9R1XQ6P/aws-ai-business-strategist-learning-plan/BDE88AHVZN)

13 digital courses, ~14h 30m, mapped to the four domains. The launch blog frames this
as first-exposure content ("if you're new to the material, start here"). If the
15-hour exam prep already covered this ground, **do not re-watch.** Refinement-mode
anti-pattern #2.

### Adjacent free Skill Builder content (not AIB-branded)

| Course | Length | Relevance |
|---|---|---|
| Generative AI for Executives | 13 min | Domain 2 framing. Trivial. |
| Generative AI Learning Plan for Decision Makers (Art of the Possible → Planning a GenAI Project → Building a GenAI-Ready Organization) | 3h 17m | Domains 2 and 4. Predates the cert; likely source material for parts of the AIB courses. Low marginal value after the exam prep. |
| Introduction to Responsible AI | short | Domain 3. Almost certainly subsumed. |

---

## Bank economics

Fresh, full-length, blueprint-weighted question banks are the scarce resource, and the
one-attempt beta rule makes each one more valuable.

| Bank | Size | Status | Use |
|---|---|---|---|
| AWS Official Practice Question Set | ~20 Q | **Spent** (90%) | Retakes reshuffle identical items. Not a measurement. |
| AWS Official Practice Exam | — | **Does not exist during beta** | — |
| Skill Builder course knowledge checks | many small sets | Spent, no miss capture | Signal recoverable only by re-visiting the *missed* checks, not re-doing all of them |
| Tutorials Dojo AIB-C01 Practice Exams | 100+ Q, 4 modes | Unspent, $4.99 (sale from $14.99) | **Best available measurement.** Established shop, per-question rationale, section-based mode maps to domains. |
| Whizlabs AIB-C01 | free sampler + paid set | Unspent, details behind JS | Second fresh bank; free tier first. |
| Udemy practice sets (several) | 275–390 Q claimed | Unspent, unvetted | Third tier. See caveats in Additional_Study_Resources.md. |
| Bespoke drill exam (`../practice-exams/`) | to build | — | Repeatable reps once misses exist to cluster on |

### The uncomfortable fact about every third-party bank right now

**Nobody has sat this exam.** Delivery starts 2026-09-29. Every third-party question
set on the market was written from the exam guide alone, with zero post-exam
calibration, and there are no community post-mortems (Reddit, re:Post, dev.to) to
check them against. The DEA-C01 and AIP-C01 banks had months of candidate feedback
baked in; these have none.

Consequences:

- Use third-party banks to **surface misses for the loop**, not to predict a score.
- Expect some fraction of rationales to be wrong. Verify any rationale that
  contradicts an AWS primary source before writing it into a decision pattern.
- Prefer the two shops with a track record (Tutorials Dojo, Whizlabs) over
  unknown-provenance question mills, which for a new exam are the most likely to be
  LLM-generated straight from the guide.

---

## Sources

- [Cert page](https://aws.amazon.com/certification/certified-ai-business-strategist/) — beta dates, price, 85 Q / 170 min, prep resource list
- [Launch blog, AWS Training and Certification](https://aws.amazon.com/blogs/training-and-certification/introducing-aws-certified-ai-business-strategist-built-for-the-people-who-scale-ai/) — "AWS services appear as practical context, but they are not the subject being tested"
- [Before Testing policy](https://aws.amazon.com/certification/policies/before-testing/) — beta one-attempt rule, results timing, full credential on pass
- [Certification FAQs](https://aws.amazon.com/certification/faqs/) — beta results within 5 business days
