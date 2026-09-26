# GenAI Levers — which knob for which symptom, without retraining

Covers exam guide skills 1.3.1 (prompt engineering), 1.3.2 (tokens and context
window), 1.3.3 (RAG vs fine-tuning). Seeded from Q51 on 2026-09-26, the one miss on
that attempt reached by reasoning rather than skimming, which makes it the one real
misconception: "more context means fewer missing details."

---

## Symptom → cause → lever

| Symptom in the stem | Cause | Lever |
|---|---|---|
| Works on small inputs, loses details on large ones | Input exceeds the **context window**; the model is already dropping or under-weighting content | Send less, chosen by relevance (curate, chunk, retrieve) |
| Output stops before the structure is complete | **Max output tokens** too low | Raise the response length |
| Same request, inconsistent or random outputs | **Temperature / top-p** too high | Lower them |
| Output bland, repetitive, identical when variety is wanted | Temperature / top-p too low | Raise them |
| Model states things that are wrong or outdated about the company | Facts were never in training | **RAG** (retrieval at request time) |
| Model knows the facts but the style, format, or domain tone is off | Behavior, not knowledge | **Fine-tuning** |
| Output ignores instructions or format | Prompt structure | Prompt engineering: role, examples, explicit format, constraints |

## The three things people get backwards

1. **Adding more input to fix missing details.** Once the window is full, more input
   means more dropped. "Include the full history and every document" is the one
   option that makes the symptom worse. The correct move selects by relevance, which
   is what retrieval does at the mechanism level.
2. **Sampling parameters for capacity symptoms.** Temperature and top-p change *which*
   tokens are chosen. They never change how much fits in or how much comes out. Any
   option offering them for a truncation or missing-detail symptom is a distractor.
3. **Fine-tuning for missing facts.** Fine-tuning shapes behavior. It is a poor and
   expensive way to inject knowledge that changes. RAG is the knowledge lever.

## Diagnostic phrases

- "performs consistently for smaller ... for larger ... missing" → context window
- "ends before all required sections" · "cut off" · "incomplete" → output tokens
- "without retraining the foundation model" → the answer is in the prompt, the input,
  or inference parameters; model adaptation options are out
- "varies between runs" → temperature / top-p
- "doesn't know our products / policies" → RAG
- "knows the answer but not in our format / voice" → fine-tuning

---

## Quick-recall cheat card

- Fails as input grows → **context window.** Send less, by relevance.
- Stops mid-structure → **max output tokens.** Raise it.
- Random or bland → **temperature / top-p.** Down or up.
- Missing facts → **RAG.** Wrong style → **fine-tuning.**
- Temperature never fixes capacity. More context never fixes overflow.
