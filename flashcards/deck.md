# Flashcard Deck — AIB-C01

For **one-keyword decisions** — misses you would have got instantly if you'd held the
rule. Seeded from the 2026-09-26 Tutorials Dojo attempt (6 misses) plus adjacent rules
from the same skill statements.

Format: **Q** → *A* · `source`

---

## Reading discipline (Theme 1)

**Before committing an answer, what must you be able to name for every rejected option?**
→ *The fact in the stem that eliminates it. If you can't, you're choosing on tone.* · `themes`

**Stem states a daily volume and a weekly peak. An option proposes testing a "small set of typical" items. Verdict?**
→ *Wrong. Small ≠ representative; typical ≠ peak. Scope-shrink distractor.* · `Q9`

**Stem places "thousands per day" and "years of records" after a fully stated policy. What are those phrases for?**
→ *Bait. Volume and history are enablers of ML, not needs for it.* · `Q13`

**Stem gives a retraining cadence ("every two months"). Any per-request option that touches the model is...?**
→ *Wrong by construction. Parameters change only in training.* · `Q18`

## Rules / RAG / agent boundary (Theme 2)

**Process already runs on one AI platform; moving to Bedrock. Pilot or load test?**
→ *Representative-volume test against the current baseline. Pilot is for new capabilities, not migrations.* · `Q9`, skill 2.1.5

**The stem spells out thresholds, fixed percentages, and a named exception. AI or rules?**
→ *Rules. Nothing is left to learn.* · `Q13`, skills 1.2.1 / 2.1.4

**One question that decides rules vs AI?**
→ *Can the output be fully written as rules from what the stem gives you?* · `Q13`

**Stem says "choose the next step, depending on the case, based on the result of a previous action," and lists actions on external systems. Solution?**
→ *AI agent with tools.* · `Q65`, skill 1.2.2

**One question that decides workflow vs agent?**
→ *Can every path be enumerated before the first request arrives? Yes → workflow. No → agent.* · `Q65`

**Assistant that answers questions grounded in company documents, changes no external state. Agent?**
→ *No. RAG assistant. Agents act.* · `Q65`

**The four rungs of the capability ladder, bottom to top?**
→ *Rules/workflow → chatbot → RAG assistant → agent with tools.* · `Q65`

## GenAI levers (Theme 3)

**App works on small inputs, loses details on large ones. Cause? Lever?**
→ *Input exceeds the context window. Send less, chosen by relevance.* · `Q51`, skill 1.3.2

**Generated report stops before all sections are written. Lever?**
→ *Raise maximum output tokens.* · `Q51`

**Does raising temperature or top-p change how much fits in or comes out?**
→ *No. They change which tokens are chosen, never capacity.* · `Q51`

**"Include the full history and every document" as a fix for missing details. Verdict?**
→ *Makes it worse once the window is full. The model is already dropping content.* · `Q51`

**Model lacks facts it was never trained on vs model has facts but wrong style or format. Levers?**
→ *RAG for missing facts. Fine-tuning for style, format, domain tone.* · skill 1.3.3

## Training vs inference

**Each morning the deployed model receives new data and returns a forecast. Which stage?**
→ *Inference. Nothing in the model changes.* · `Q18`, skill 1.1.1

**Where do model parameters change?**
→ *Training and retraining only.* · `Q18`

**"Uses each prediction as new training data." Verdict?**
→ *Wrong. A prediction is an output, not a training example, and updates need a separate training job.* · `Q18`

## Business-value KPIs

**Stem asks for KPIs capturing financial impact AND workforce efficiency. Which metric classes count?**
→ *Financial outcome, and labor-per-output or output-per-labor. Nothing else.* · `Q10`, skill 2.2.1

**"Percentage of alerts reviewed by technicians" — which class?**
→ *Adoption/activity. Leading indicator at best. Not value.* · `Q10`

**Precision, inference latency, system availability, percentage of equipment connected — which class?**
→ *Technical or deployment metrics. Not business value.* · `Q10`

**Four KPI classes?**
→ *Financial outcome · workforce/process efficiency · adoption/activity · technical/model quality. Only the first two answer "business value."* · `Q10`

## Migration and cost planning

**Two things every pre-cutover plan for an AI platform migration includes?**
→ *Cost estimate including the parallel-run period (Pricing Calculator), and a representative-volume test against the current baseline.* · `Q9`

**Pricing Calculator vs Cost Explorer?**
→ *Calculator forecasts before spend. Explorer analyzes after.* · in-scope services

**Consumption-based, instance-based, seat-based — which in-scope service is the canonical example of each?**
→ *Bedrock (tokens) · SageMaker AI (compute hours) · Amazon Quick (per user per month).* · exam guide pricing structures
