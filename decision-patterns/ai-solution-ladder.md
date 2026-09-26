# AI Solution Ladder — rules, chatbot, RAG assistant, agent

Covers exam guide skills 1.2.1 (rules vs AI), 1.2.2 (agents vs other AI), 2.1.4 (when
AI is not appropriate). Two mirror-image misses on 2026-09-26 (Q13 chose AI when rules
were right; Q65 chose rules when an agent was right) showed the boundary was fuzzy in
both directions.

---

## The ladder

The stem tells you which rung by what the system must **do**, never by how much data
exists or how many transactions there are.

| Rung | What the system must do | Tell in the stem | AWS context |
|---|---|---|---|
| **Rules / workflow** | Follow a decision path that can be fully written in advance | Thresholds, fixed outcomes, named exceptions, "consistently", "established rules" | Step Functions-style state machine; no ML |
| **Chatbot** | Answer from general knowledge | "answer common questions", no company data named | FM via Bedrock |
| **RAG assistant** | Answer grounded in company data; change nothing | "answer", "summarize", "explain", "connected to records/policies" | Bedrock Knowledge Bases |
| **Agent with tools** | Take actions in external systems, choosing the next action from the result of the last | "choose the next step", "depending on the case", "based on the result of a previous action", a list of *actions* (process, issue, create, escalate) | Bedrock Agents / AgentCore; tools, orchestration |

## Two one-question tests

**Rules vs AI:** *Can the output be fully written as rules from what the stem gives
you?* Yes → rules. The Responsible AI Lens itself excludes use cases solvable by
expert systems. "No, use rules" is the AWS-canonical answer, not a trick, and the
guide lists the skill twice.

**Workflow vs agent:** *Can every path be enumerated before the first request
arrives?* Yes → workflow. No, because step N depends on what step N-1 returned →
agent.

## What does NOT move a problem up the ladder

Data volume. Years of history. Transaction rate. "At scale." Structured or numeric
data. These are enablers of ML and appear in stems as bait (Q13). Only the *nature of
the decision* moves the rung: pattern inference, prediction, unstructured input,
judgment that varies case by case, or actions whose sequence is discovered at runtime.

## What does NOT make something an agent

Being grounded in documents. Being conversational. Having access to order records.
An assistant that reads and answers is a RAG assistant. An agent **acts** on external
systems and decides what to do next from what it just did (Q65). Skill 1.2.2 names
the capabilities: autonomy, tool use, agent-to-agent communication, orchestration.

---

## Quick-recall cheat card

- Stem states the logic → **rules.** Volume and history are bait.
- Stem says answer / summarize / explain over company data → **RAG assistant.**
- Stem says choose next step / depends on the result / lists actions → **agent.**
- Rules vs AI: can it be written as rules from the stem? Workflow vs agent: can every
  path be enumerated in advance?
- Agents act. Assistants answer.
