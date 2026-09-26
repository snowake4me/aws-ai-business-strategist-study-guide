# Additional Study Resources — AIB-C01

Curated 2026-09-25 for a candidate already at 90% on the Official Practice Question Set
with the full Skill Builder exam prep complete. That is **refinement mode**, and the
anti-patterns from `STUDY-PROCESS.md` in the DEA-C01 and AIP-C01 repos apply in full:
no more video courses, no re-reading notes, no practice questions without miss capture,
no time on topics already at 90%+.

So this list is not "more content." It is three things:

1. **Fresh measurement banks** — to surface misses so the loop has something to chew on
2. **Primary sources** — the AWS documents whose vocabulary the scenario questions key
   on, to settle a discriminator when a miss reveals one
3. **Framework vocabulary** — the specific named lists (phases, dimensions, tiers) where
   a plausible near-synonym is the designed distractor

Every item carries a verdict. Skip anything marked *skip*.

---

## 1. Measurement banks — in the order to spend them

The Official Practice Exam does not exist during beta, the 20-question Official
Practice Question Set is spent, and no one has sat the real exam yet (delivery starts
2026-09-29). So every bank below is uncalibrated against the real thing. Use them to
find misses, not to forecast a score. See `README.md` in this folder for the full bank
economics.

| Order | Bank | What it is | Verdict |
|---|---|---|---|
| 1 | [Tutorials Dojo — AIB-C01 Practice Exams](https://portal.tutorialsdojo.com/product/aws-certified-ai-business-strategist-aib-c01-practice-exams/) | 100+ original questions; Timed, Review, **Section-Based** (per domain), and Final randomized modes; rationale plus reference link on every question; bonus flashcards; 1-year access. $4.99 on sale (list $14.99). | **Buy. Take one timed full pass cold first**, then use Section-Based mode on whichever domain the pass says is weakest. TD's rationales cite AWS docs, which makes them checkable. |
| 2 | [Whizlabs — AIB-C01](https://www.whizlabs.com/aws-certified-ai-business-strategist/) | Their blog says a free practice test is up and the paid set pairs every question with "why each distractor is wrong and what business principle it violates." Question counts and price are behind a JS page and could not be verified. | **Free tier first.** Buy the paid set only if the TD pass leaves an open cluster that needs more reps. Whizlabs question quality has historically been a notch below TD; treat rationales as claims to verify. |
| 3 | Udemy practice sets — [Maruchin Tech "AIB Exam Prep Course" (beta edition)](https://www.udemy.com/course/aws-ai-business-strategist-aib-en/) · [Exam Questions Course](https://www.udemy.com/course/aws-certified-ai-business-strategist-exam-questions-course/) · [Practice Sets](https://www.udemy.com/course/aws-certified-ai-business-strategist-aib-c01-practice-sets/) · [Exam Practice](https://www.udemy.com/course/aws-certified-ai-business-strategist-exam-practice/) | Several appeared within weeks of the announcement. The Maruchin Tech one is the only author with a public track record (12x AWS certified, 100k+ Udemy students) and is explicitly labeled a beta edition. Udemy blocks unauthenticated fetches, so ratings and counts are unverified. | **Third tier, and only the Maruchin set.** Skip the video portion entirely (anti-pattern #2). Wait for a coupon; the author issues them monthly per his dev.to post. |
| — | Preporato (390+ Q), CertSafari (346 Q), CloudForAll (340 Q), impodays, K21 Academy, NetCom articles | Unknown-provenance sites that stood up AIB-C01 pages within days of the announcement with suspiciously large question counts for an exam nobody has taken. | **Skip.** For a brand-new exam these are the most likely to be LLM-generated from the guide with unreviewed answer keys. A wrong rationale absorbed into a decision pattern costs more than the bank saves. |
| — | ExamTopics, Reddit r/AWSCertifications, AWS re:Post | Community dumps and post-mortems. | **Nothing exists yet.** Re-check re:Post and r/AWSCertifications in mid-October once the first beta sitters report back. Ignore ExamTopics regardless. |
| — | [YouTube "AIB-C01 Practice Exam" video](https://www.youtube.com/watch?v=zABvgbDQLhM) | Read-aloud question set. | Skip. No confidence tagging, no section breakdown, unknown author. |
| — | Pluralsight / A Cloud Guru, LinkedIn Learning, Coursera | The reserved-measurement source on DEA-C01 and AIP-C01. | **Nothing published for AIB-C01 as of today.** Check again in November; Pluralsight typically lags new AWS exams by a quarter. |

### Recovering signal from the 15 hours already spent

The Skill Builder knowledge checks were done without miss capture. Do not redo them
all. Instead, open the course, go to each module's knowledge check, and **list only the
items marked incorrect or that you remember hesitating on** as paraphrased descriptors
in `misses/`. Skill Builder keeps knowledge-check state per module. That is a free
first miss set to cluster before spending the TD bank.

---

## 2. Primary sources mapped to the exam guide

The exam guide's technologies page names the frameworks it draws from. These are the
documents. Each row says which skill statements it feeds and what to actually read.
Nothing here is a cover-to-cover assignment; open the section when a miss points at it.

### Domain 1 — AI Fundamentals and Literacy (24%)

| Source | Feeds | What to read | Verdict |
|---|---|---|---|
| [ISO/IEC 42001:2023 overview (ISO)](https://www.iso.org/standard/42001) and a [plain-English comparison of 42001 vs NIST AI RMF vs EU AI Act](https://www.eccouncil.org/cybersecurity-exchange/responsible-ai-governance/eu-ai-act-nist-ai-rmf-and-iso-iec-42001-a-plain-english-comparison/) | 1.1.6 (also 3.2.4) | Enough to hold the discriminator: **42001 = certifiable AI *management system* standard for the organization; 23053 = framework describing an ML-based AI *system* and its lifecycle.** Org-level shell vs system-level lifecycle. | One sitting. Flashcard. |
| [ISO/IEC 23053 glossary summary](https://sgsystemsglobal.com/glossary/iso-iec-23053-ai-system-lifecycle-framework/) | 1.1.6 | Same discriminator from the other side. | Flashcard only. |
| [AWS Generative AI Security Scoping Matrix](https://aws.amazon.com/ai/security/generative-ai-scoping-matrix/) | 1.2.4 (shadow AI, tool classification), 3.2.3, 3.3 | The five scopes: consumer app → enterprise app → pre-trained models → fine-tuned models → self-trained models, and how ownership and control shift across them. This is AWS's canonical "classify the AI tool" model and likely the frame behind approved / blocked / under-evaluation questions. | **Read in full (short).** |
| [Agentic AI Security Scoping Matrix](https://aws.amazon.com/ai/security/agentic-ai-scoping-matrix/) | 1.2.2 (agent capabilities: autonomy, tool use, agent-to-agent, orchestration) | Skim the four architectural scopes. Gives the business-level vocabulary for "what makes an agent an agent." | Skim once. |
| [Well-Architected Generative AI Lens — Cost Optimization](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gencost01.html) | 1.3.2 (tokens, context windows), 2.2.5 | GENCOST01 (right-size model selection) and [GENCOST02](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gencost02.html) (pricing model: provisioned / on-demand / hosted / batch). Token economics at the business level. | Read the two question pages, not the whole lens. |

### Domain 2 — AI Strategy and Business Value Creation (28%)

The heaviest domain and, per Whizlabs and the Maruchin Tech post, where the exam most
often separates "the technically optimal answer" from "the defensible business
decision." Every source here is about money, prioritization, or build-buy-partner.

| Source | Feeds | What to read | Verdict |
|---|---|---|---|
| [AWS Cloud Value Framework — Business Value on AWS](https://aws.amazon.com/executive-insights/content/business-value-on-aws) ([PDF](https://pages.awscloud.com/rs/112-TZM-766/images/Business%20Value%20on%20AWS%20EN.pdf)) | 2.2.1, 2.2.3 | The **five value pillars: cost savings (TCO), staff productivity, operational resilience, business agility, sustainability.** This is AWS's ROI vocabulary. When a stem asks for a "comprehensive" ROI framework, the distractors will be single-pillar answers. | **Read.** Two pages. |
| [AWS Cloud Economics](https://aws.amazon.com/economics) and the [Cloud Economics ebook](https://d1.awsstatic.com/executive-insights/en_US/awscloudeconomicsebook.pdf) | 2.2.2 (baselines), 2.2.3 | Business case construction, baseline-before-migrate. Skim for the baseline and TCO framing only. | Skim. |
| [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) | 2.2.5, "AWS AI pricing structures" | Do **not** memorize numbers. Learn the **modes**: On-Demand, Batch (50% off), Provisioned Throughput (hourly, 1- or 6-month commit), Priority / Flex / Reserved tiers, prompt caching, model customization, Guardrails per text unit, Knowledge Bases per GB and per query. The business question is always "which mode fits this traffic shape and commitment appetite." | One careful read of the mode list. |
| [Amazon Quick — QuickSight evolves to Quick Suite (AWS BI blog)](https://aws.amazon.com/blogs/business-intelligence/reimagine-business-intelligence-amazon-quicksight-evolves-to-amazon-quick-suite/) | "Amazon Quick at a strategic level", pricing structures | Quick is **seat-based**: Reader, Reader Pro, Author, Author Pro tiers plus a monthly infrastructure fee for Pro / Q&A users. Components: Quick Sight (BI), Research, Flows, Automate, Index, Spaces, Chat. It absorbed Amazon Q Business (closed to new customers 2026-07-31). Named "Quick Suite" at launch Oct 2025, now just "Amazon Quick." | **Read.** This is the newest in-scope service and the one the Skill Builder course is most likely to have described under an older name. |
| [AWS Marketplace](https://aws.amazon.com/marketplace) · [Pricing Calculator](https://calculator.aws/) · [Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) | 2.1.2 (build-buy-partner), 2.2.5 | Know the role, not the UI: Marketplace = evaluate *buy* and *partner* options with consolidated billing; Pricing Calculator = *forecast* before commit; Cost Explorer = *observe* after the fact. Calculator vs Explorer (plan vs report) is a likely one-keyword swap. | Flashcard. |
| [Prescriptive Guidance — Best practices for enterprise generative AI adoption and scaling](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html) | 2.1.3, 2.1.5, 4.4.3 | Model selection pattern the exam will reward: **prove the use case on a top-tier model, then systematically evaluate smaller models against benchmarks for production cost.** Plus AI CoE and model governance committee. | **Read in full.** One page. |
| [Executive's Guide to Agentic AI (AWS Executive Insights)](https://aws.amazon.com/executive-insights/content/an-executives-guide-to-agentic-ai/) and [Navigating the GenAI Landscape: Blueprint for CEOs and CIOs](https://aws.amazon.com/blogs/enterprise-strategy/navigating-the-generative-ai-landscape-a-strategic-blueprint-for-ceos-and-cios/) | 2.3.x (competitive advantage, business model transformation, investment levels) | AWS's own framing of "business impact over technology, cross-functional teams, right use case, parallel pilots, measure real outcomes." Domain 2.3 has the fewest concrete anchors in the guide; this is where AWS says what it thinks. | Skim both once. |

### Domain 3 — AI Governance and Responsible AI Leadership (24%)

| Source | Feeds | What to read | Verdict |
|---|---|---|---|
| [AWS Responsible AI — core dimensions](https://aws.amazon.com/ai/responsible-ai/) | 3.1.1, 3.1.2 | The **eight dimensions as AWS lists them on the marketing page**: fairness, explainability, privacy and security, safety, controllability, veracity and robustness, governance, transparency. Each has a one-line AWS definition. Questions that ask "which dimension is at stake" test whether you can tell controllability from transparency, or veracity from robustness. | **Read. Flashcard all eight with the AWS definitions verbatim.** |
| [Well-Architected Responsible AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/responsible-ai-lens.html) (published 2025-11-19) | 3.1.3 (governance by design), 3.1.4, 3.3.x | Named in the exam guide's recommended-knowledge list. The lens splits the dimensions into **ten** (privacy and security separate; veracity and robustness separate) and organizes best practices into **eight focus areas aligned to the ML lifecycle.** Read the landing page and the [design principles](https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/design-principles.html). Skip the per-question best-practice pages unless a miss points there. | Landing page + design principles. Note the 8-vs-10 split (see section 3). |
| [Responsible Use of AI guide](https://aws.amazon.com/ai/responsible-ai/resources/) and [AI Service Cards](https://aws.amazon.com/blogs/machine-learning/introducing-aws-ai-service-cards-a-new-resource-to-enhance-transparency-and-advance-responsible-ai/) | 3.1, 3.3.3 | Service Cards = AWS's transparency artifact (intended use, limitations, design choices). Know what one *is* and which dimension it serves (transparency). | Skim the Service Cards intro. |
| [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) plus [Bedrock security, privacy and responsible AI](https://aws.amazon.com/bedrock/security-privacy-responsible-ai/) | 3.2.3, "shared responsibility model for AI workloads" | The AI-specific additions on top of the classic model: AWS runs the service and does not use customer prompts or completions to train models, does not share them with model providers; the customer owns IAM, data classification, regulatory compliance of the use case, prompt-injection defenses, and output review. | Read the Bedrock page. |
| [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) and [SC Media explainer: NIST AI RMF vs EU AI Act risk classification](https://www.scworld.com/tech-explainer/ai-risk-classification-nist-ai-rmf-and-eu-ai-act-for-security-practitioners) | 3.2.4 (risk classification frameworks), 3.2.2 | **NIST AI RMF: Govern, Map, Measure, Manage** (voluntary, US). **EU AI Act: unacceptable, high, limited, minimal risk** (binding, tiered obligations). The exam guide says "risk classification frameworks" without naming one; these two are the ones every vendor bank will use. | One sitting, then flashcards for the two lists. |
| [Prescriptive Guidance — AI CoE and model governance committee](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html) and [Establishing an AI/ML CoE (AWS ML blog)](https://aws.amazon.com/blogs/machine-learning/establishing-an-ai-ml-center-of-excellence/) | 3.2.1, 4.4.3 | Cross-functional representation (IT, business, security, legal, compliance, GenAI SMEs), clear accountability, committee reviews model usage requests. | Already covered under Domain 2; same page. |

### Domain 4 — Business Readiness, Leadership, and AI Transformation (24%)

| Source | Feeds | What to read | Verdict |
|---|---|---|---|
| [Prescriptive Guidance — Generative AI maturity model](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-maturity-model/introduction.html) | **4.1.2, 4.4.1, 4.4.2, 4.4.5** | Four levels: **Envision → Experiment → Launch → Scale.** Skill 4.4.1 uses exactly these four words, so this document is the source. Each level has criteria plus activities across six pillars (business, people, governance, platform, security, operations) and a "transformation strategy to reach the next level." Level 1 names cross-functional squads as the seed of a later CoE; Level 3 introduces the RACI matrix and human-in-the-loop; Level 4 is reusable components and self-service. | **Read all four level pages.** This is the single highest-value document on the list for Domain 4. |
| [AWS CAF for AI, ML, and Generative AI (CAF-AI)](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/aws-caf-for-ai.html) | 4.1.1, 4.1.3, 4.2.x, "AWS CAF" | The **six perspectives: Business, People, Governance, Platform, Security, Operations**, each with foundational capabilities, and the AI-specific additions (for example ML fluency under People; responsible use under Governance; data architecture and data engineering under Platform). Read [Your AI/ML transformation journey](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/your-aiml-transformation-journey.html) and [Foundational AI/ML capabilities](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/foundational-aiml-capabilities.html). Marked "historical reference" by AWS but still the document the guide names. | **Read those two sections.** Skip the per-perspective deep dives unless a miss lands there. |
| [AWS CAF overview — Your cloud transformation journey](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/your-cloud-transformation-journey.html) | 4.4.1 (as a distractor source) | The *general* CAF phases are **Envision → Align → Launch → Scale.** Not the same list as the GenAI maturity model. See section 3. | Read the one page so the two lists stop blurring. |
| [Prescriptive Guidance — Transform the ADM operating model with generative AI: action areas](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-transform-adm-operating-model-gen-ai/recommendations.html) | 4.3.x (workforce, change management, role transition) | AWS's recommendations on org structure and skills when AI enters application development. Useful for 4.3.6 (transitioning human roles to oversight). | Skim. |
| [AWS Executive Insights — Generative AI/ML](https://aws.amazon.com/executive-insights/generative-ai-ml/) and [The State of Generative AI for executives](https://aws.amazon.com/executive-insights/content/state-of-generative-ai-for-executives/) | 4.3.1, 4.3.4 (sponsorship, culture) | Executive-audience framing of sponsorship, skilling, and culture. Low density; the guide's Domain 4 language comes from here. | Skim one. |

---

## 3. Framework vocabulary — the designed-distractor lists

Scenario exams on named frameworks reliably plant a near-synonym from an adjacent
framework as a distractor. These are the pairs most likely to be swapped on AIB-C01.
Every one belongs in `flashcards/deck.md`.

| Distinction | The lists | Why it will be swapped |
|---|---|---|
| **GenAI maturity model levels** vs **CAF transformation phases** | Maturity model: **Envision, Experiment, Launch, Scale.** CAF: **Envision, Align, Launch, Scale.** | Three of four words match. Skill 4.4.1 says "envision, experiment, launch, scale" — so "Align" in an option is the tell for the wrong framework. |
| **Responsible AI dimensions: 8 or 10** | AWS site (8): fairness, explainability, privacy *and* security, safety, controllability, veracity *and* robustness, governance, transparency. RAI Lens (10): the same set with privacy / security and veracity / robustness split. The exam guide's own list (3.1.1): fairness, explainability, privacy, safety, transparency, robustness. | Any answer built around "which dimension" depends on the definitions, not the count. Learn the AWS one-liners: controllability = monitor and *steer*; transparency = stakeholders make *informed choices*; veracity = *factually correct*; robustness = correct under *unexpected inputs*. |
| **ISO/IEC 42001** vs **ISO/IEC 23053** | 42001 = certifiable AI *management system* (organization-level, auditable). 23053 = framework for describing an ML-based AI *system* and its lifecycle. | Both start with "ISO/IEC," both are "AI frameworks." Organization vs system is the axis. |
| **NIST AI RMF functions** vs **EU AI Act tiers** | NIST: Govern, Map, Measure, Manage (voluntary). EU: unacceptable, high, limited, minimal (binding, obligations scale with tier). | "Risk classification" in a stem points to the EU tiers; "risk management functions" points to NIST. |
| **CAF perspectives** vs **maturity-model pillars** | Both: Business, People, Governance, Platform, Security, Operations. | Same six words in both. This one is *not* a trap; it is a freebie. |
| **AWS pricing structures** | Consumption-based (tokens: **Bedrock**), instance-based (compute hours: **SageMaker AI** endpoints and training), seat-based (per user per month: **Amazon Quick**). | The exam guide names these three structures and exactly these three services. Mapping each service to its dominant structure is almost certainly a question. |
| **Bedrock inference modes** | On-Demand · Batch (async, 50% off) · Provisioned Throughput (hourly, committed) · Priority / Flex / Reserved tiers · prompt caching. | Stems describe a traffic shape ("bursty and unpredictable" / "steady and latency-sensitive" / "overnight, not time-critical") and ask for the mode. |
| **Pricing Calculator** vs **Cost Explorer** | Calculator forecasts *before* spend. Explorer analyzes *after* spend. Both are in scope. | One-keyword swap. |
| **Cloud Value Framework pillars** | Cost savings (TCO), staff productivity, operational resilience, business agility, sustainability. | A "comprehensive ROI framework" (2.2.3) that omits intangibles is the distractor. |
| **GenAI Security Scoping Matrix scopes** | 1 consumer app · 2 enterprise app · 3 pre-trained models · 4 fine-tuned models · 5 self-trained models. | Shadow AI (1.2.4) questions will describe an employee using a scope-1 tool and ask what governance applies. |
| **Rule-based automation vs AI** (1.2.1, 2.1.4) | Deterministic, stable rules, full explainability required, small data → rules. Pattern recognition, unstructured input, tolerance for probabilistic output → AI. | The RAI Lens itself says its guidance "is not appropriate for AI use cases that can be solved without machine learning, for example, by using expert systems." Expect "AI is not the answer" to be a correct option more than once. |

---

## 4. What not to spend time on

| Resource | Why skip |
|---|---|
| Re-watching the AWS AI Business Strategist Learning Plan (13 courses, 14.5 h) or the exam prep course | Refinement-mode anti-pattern #2. The knowledge checks were already strong. Recover the *missed* checks only (section 1). |
| AIF-C01 (AI Practitioner) practice banks | Different exam. AIF tests service and technique recall; AIB tests business judgment with services as context. Responsible AI overlaps in vocabulary but not in question shape. Do not import misses across. |
| AIP-C01 (GenAI Developer Pro) materials from the sibling repo | RAG, agents, Guardrails, evaluation on Bedrock are all on AIB's **out-of-scope** list as implementation topics. Useful only as background for "when do you need this," which the AIB course already covered. |
| Any Bedrock, SageMaker, or Quick *hands-on* lab | The guide says no hands-on is required and lists configuring or deploying services as out of scope. Labs were the right tool for DEA-C01 and AIP-C01 knowledge gaps; here a "lab" is reading a pricing page or a maturity-model level and writing the decision rule. |
| Vendor blog "exam overview" articles (K21 Academy, NetCom, Whizlabs blog beyond the free test link) | Restate the exam guide. Zero new information. |
| Generic ISO 42001 implementation guides (Apptega, ISMS.online, OneTrust) | Compliance-vendor depth aimed at auditors. The exam wants the one-line discriminator only. |

---

## 5. Re-check dates

| When | What |
|---|---|
| **2026-10-15** | Search r/AWSCertifications and AWS re:Post for first-sitter reports. First real signal on which domains the beta form actually stresses. Until then, every claim about "what the exam emphasizes" is inference from the guide. |
| **2026-11-01** | Pluralsight / A Cloud Guru catalog for an AIB-C01 course or practice exam. If one lands, it becomes the reserved measurement, as on prior preps. |
| **2027-02-15** | Standard exam GA. Official Practice Exam should appear on Skill Builder around then. Only relevant if the beta attempt is missed. |

---

## Sources consulted (2026-09-25)

Official: [cert page](https://aws.amazon.com/certification/certified-ai-business-strategist/) · [exam guide](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01/ai-business-strategist-01.html) and its [domain 1](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01/ai-business-strategist-01-domain1.html), [domain 2](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01/ai-business-strategist-01-domain2.html), [domain 3](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01/ai-business-strategist-01-domain3.html), [domain 4](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01/ai-business-strategist-01-domain4.html), [technologies](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01/aib-01-technologies-concepts.html), [in-scope services](https://docs.aws.amazon.com/aws-certification/latest/ai-business-strategist-01/aib-01-in-scope-services.html) pages · [launch blog](https://aws.amazon.com/blogs/training-and-certification/introducing-aws-certified-ai-business-strategist-built-for-the-people-who-scale-ai/) · [Before Testing policy](https://aws.amazon.com/certification/policies/before-testing/) · [Certification FAQs](https://aws.amazon.com/certification/faqs/) · [Skill Builder exam prep plan](https://skillbuilder.aws/category/exam-prep/ai-business-strategist-business-AIB-C01) · [AIB Learning Plan](https://skillbuilder.aws/learning-plan/TSP9R1XQ6P/aws-ai-business-strategist-learning-plan/BDE88AHVZN)

Third-party: [Tutorials Dojo announcement](https://tutorialsdojo.com/introducing-new-aws-certified-ai-business-strategist-aib-c01-certification/) and [product page](https://portal.tutorialsdojo.com/product/aws-certified-ai-business-strategist-aib-c01-practice-exams/) · [Whizlabs exam overview](https://www.whizlabs.com/blog/aib-c01-exam-overview/) · [Maruchin Tech on dev.to](https://dev.to/maruchin_tech_555/aws-certified-ai-business-strategist-aib-c01-who-is-this-new-exam-for-4cm4) · [AWS Builder Center: Who it's for and how to prepare](https://builder.aws.com/content/3ImE9lJ2iYY80czblITDg2h3jAr/aws-certified-ai-business-strategist-who-its-for-and-how-to-prepare) and [Come prepare with me — Domain 1](https://builder.aws.com/content/3J1qzcSSAuUxQnoawisqjaj4rCP/come-prepare-with-me-for-aws-certified-ai-business-strategist-domain-1-ai-fundamentals-and-literacy) (both JS-rendered; not fetched, listed for manual reading)

Primary AWS documents are linked inline in section 2.
