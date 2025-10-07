# Prompt Playbook v1

## Objective
Capture empirical observations comparing prompt variants and model behaviors. Use this as a living artifact you will refine in future weeks.

## How to Use This File
1. After each script run, append rows to the Results Table.
2. Tag failure modes (see legend) so patterns emerge quickly.
3. Summarize insights after completing stretch assignments.

## Scoring Rubric (1–5)
| Score | Instruction Adherence | Reasoning Depth | Style / Persona | Format Fidelity |
|-------|-----------------------|-----------------|-----------------|-----------------|
| 1 | Misses key directives | Single sentence | Ignores persona | Broken / ignores |
| 3 | Mostly follows | Some steps implicit | Partial persona | Minor drift |
| 5 | Precise & complete | Clear multi-step chain | Fully consistent | Exact, parsable |

## Failure Mode Tags
hallucination, verbosity, shallow, drift (format), persona-loss, json-break, constraint-fail

## Results Table (Populate During Lab)
| Prompt Pattern | Example Used | Model | Adherence (1–5) | Reasoning (1–5) | Style (1–5) | Format (1–5) | Failure Modes | Notes | Reuse? (Y/N) |
|----------------|--------------|-------|------------------|-----------------|-------------|--------------|---------------|-------|--------------|
Simple|Explain photosynthesis|Llama3|5|5|5|5|None|clear definition, very comprehensive|-
Simple|Explain photosynthesis|Mistral|3|5|5|3|Missing Information|less comprenhensive than Llama3, missing some info|-
Role|Explain photosynthesis as a Science Teacher|Llama3|5|5|5|5|None|explanation is simple and accurate and follows the teacher persona|-
Role|Explain photosynthesis as a Science Teacher|Mistral|3|5|3|3|Inconsistency| very technical |-
Chain-of-Thought|Explain photosynthesis step-by-step, from inputs to outputs|Llama3|5|5|5|5|None|-|-
Chain-of-Thought|Explain photosynthesis step-by-step, from inputs to outputs|Mistral|1|1|1|1|Incomplete response, repetition| looper with a broken response|-

## Model Summary (After Initial Pass)
| Capability | Best Model(s) | Evidence Snippet | Notes |
|------------|---------------|------------------|-------|
| Explanatory Clarity | Llama3 Gemini| | |
| Chain-of-Thought | Llama3 Gemini | | successfully addapated to every prompt pattern |
| JSON Adherence | All of them | | All of them performed well with the right instructions |
| Persona Control | Gemini  |I have recently had occasion to examine a curious new contrivance, styled by some as "Google Glass," which purports to augment the human faculties of sight and information acquisition. | |
| Instruction Strictness | Gemini Llama3| Into the immense wood, the traveler stepped. A canopy of dense boughs blocked the sky, letting slivers filter through the gloom.| All of them performed welll with the negative prompt |

## Insight Log
Record notable surprises, regressions, or improvements.
- Day 1:

Mistral model on the Chain-of-Thought prompt. It didn't just provide a weak answer; it entered a repetitive loop, broke its formatting, and introduced significant errors. This reveals a critical instability when faced with structured reasoning tasks

- Day 2:
- Day 3:

---

### 1. Role Prompting

*   **Best Practice:**
    *   Clearly define the persona or role you want the AI to adopt. This helps to set the context, tone, and level of detail in the response.
*   **Example:**
    *   Instead of "Explain black holes," use "You are an astrophysicist. Explain the concept of a black hole to a curious 10-year-old."

---

### 2. Few-Shot Learning

*   **Best Practice:**
    *   Provide a few examples of the desired input and output format. This is especially useful for tasks like classification, summarization, or code generation.
*   **Example:**
    *   When asking for a summary, provide one or two examples of a text and its corresponding summary before providing the text you want to be summarized.

---

### 3. Chain-of-Thought (CoT)

*   **Best Practice:**
    *   Encourage the model to "think step by step" or to "show its work." This is particularly effective for complex reasoning tasks, such as math problems or logic puzzles.
*   **Example:**
    *   Append "Let's think step by step" to your prompt when you need the model to reason through a problem.

---

### 4. Anti-Patterns to Avoid
## Reflection (End of Week)
Answer briefly:
1. Which two prompt patterns yielded the largest delta between models?

Answer:
The two prompt patterns with the largest performance difference between models were Role and Chain-of-Thought. the Role prompt showed a significant gap in adherence, the Chain-of-Thought prompt resulted in a complete model failure for Mistral, which produced a repetitive, factually incorrect, and unusable response

2. Which failure mode was most frequent? Root cause?

Answer:
The most significant failure mode was Mistral's Incomplete Response / Repetition, seen in the Chain-of-Thought prompt. leads to an output loop and factual hallucination.

3. Default model choice for: explanation / reasoning / structure.

Answer:
Explanation: Llama3, for its comprehensive and accurate responses.
Reasoning: Llama3, executed the step-by-step task.
Structure: Llama3, for consistently providing well-formatted and structured outputs.

4. Open questions heading into Week 2.
*   **Ambiguity:**
    *   Avoid vague or open-ended questions. Be as specific as possible.
*   **Leading Questions:**
    *   Don't phrase your prompt in a way that suggests a desired answer.
*   **Overly Complex Prompts:**
    *   Break down complex tasks into smaller, more manageable prompts.

---
