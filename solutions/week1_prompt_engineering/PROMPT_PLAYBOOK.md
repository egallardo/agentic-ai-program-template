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
- Week 1:

Mistral model on the Chain-of-Thought prompt. It didn't just provide a weak answer; it entered a repetitive loop, broke its formatting, and introduced significant errors. This reveals a critical instability when faced with structured reasoning tasks

- Week 2:
 
 Relying on the LLM to ignore the bad information is inefficient and unreliable

- Week 3:

Without a standard like MCP, AIs often try to call tools by just "guessing" how they work, which leads to errors or completely made-up answers. 

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
## Week 2 Section- context engineering

| Query | Mode (raw/RAG) | k | Retrieved IDs | Strengths | Weaknesses | Failure Modes | Notes | 
|-------|----------------|---|---------------|-----------|------------|---------------|-------|
What are the support hours?|RAG|2|faq7 faq5| Found the correct document faq7 and provided the right answer|One of the retrieved k is irrelevant| irrelevant|Right Answer
Can I pay with Bitcoin?|RAW|N/A|No context|Gave a general answer, indicating that bitcoi is one of the most widely accepted cryptocurrencies| wrong answer |no-hit, irrelevant| Review general information and concludes that bitcoin is accepted as a payment option |
|What-s the process for tracking my package?|RAG|4|faq2 faq9 faq4 faq1|Retrieves the exact document faq2|faq 4 is related but doesnt help answer the question about the process, faq9 and faq1 are irrelevant, adding noise|irrelevant| The system provides the correct answer


### Scoring (suggested 1–5 each)
| Dimension | Definition | 1 | 5 | Score | Notes
|-----------|------------|---|---|-------|------
| Grounding | Uses factual retrieved content | Hallucinates | Fully cites sources | 5 | Answer based of retrieved documents 
| Relevance | Stays on user ask | Tangential | Direct & focused | 5 | Answers direct and focused on the user question
| Completeness | Covers key facts | Missing core | Fully addresses | 5 | Answers fully address the user querys
| Brevity | Concise & purposeful | Verbose fluff | Tight answer | 5 | Answers are to the point, irrelevant noise ignored
| Traceability | Clear which docs | Unclear | Explicit ids | 5 | with the code modifications is easy to trace the source ids used for generation

Failure Mode Tags: `no-hit`, `irrelevant`, `partial`, `verbose`, `leakage`, `stale`.

## Reflection Prompts
- Where did additional context hurt answer quality?
A: Introduces irrelevant documents, the LLM do extra work to filter out the noise and increase the risk to provide incorrect answer
- Which failure mode appeared most often?
A: The Irrelevant failure, the system struggle to find relevant documents
- What is your next improvement priority & why?
A: provide more context to the LLM with a combination of questions and answers to help to get more reliable answers

## Insight Log
Record notable surprises, regressions, or improvements.

- Week 2:
 
 Relying on the LLM to ignore the bad information is inefficient and unreliable

- Week 3:

Without a standard like MCP, AIs often try to call tools by just "guessing" how they work, which leads to errors or completely made-up answers. 


## Week 3 Lab: Intro to Model Context Protocol (MCP)

## Evaluation & Logging

| Query | Intent Parsed | Tool? | Tool Latency ms | Success | Answer Quality (1–5) | Notes |
|-------|---------------|-------|-----------------|---------|----------------------|-------|
"what is the weather in El Salvador?"| get_weather | Yes | 0.8356571197509766 | Yes | 5 | Correctly parsed city and cited the data
"what is the weather?" | None | No |  0 | Yes | 5 | Correclty indentified city was missing in the request 
"what is the capital in El Salvador?"| None | No | 0 | Yes | 3 | Correctly identified no tool was needed, but was generic
"I need the weather in San Jose"| get_weather | Yes | 0.020742416381835938 | Yes | 5 | Correctly identified city and cited the data
"how hot is London?" | None | No | 0.0 | No | 1 | False Negative, Agent didnt undestand
"what is the time in EST?" | get_current_time | Yes	| 0.0171661376953125 | Yes | 5 |	Correctly identified city and cited the data
"Tell me the weather in London and the current time in UTC?" |	None |	No | 0.0 |	No | 1 | False Negative, Agent didnt undestand

Success Criteria:
- Tool invoked only when needed
- City parameter extracted correctly (≥3 test cities)
- Error handled (unknown city) without crash
- Answer cites tool data explicitly (e.g., “According to tool…”) 

---
## Reflection Prompts
- When did the tool invocation NOT improve answer quality?

Some queries were not asking weather information, it provided a generic error
Asking how hot was the weather caused a false negative, the agent didnt understand and provided a wrong anser

- Which failure mode appeared first? Root cause?

The False Negative, some of my queries didn't match the simple regex pattern

- Next production hardening step you’d prioritize?

Improve the rigid regex, the agent failed cause the limited weather pattern regex


## Insight Log
Record notable surprises, regressions, or improvements.


- Without a standard like MCP, AIs often try to call tools by just "guessing" how they work, which leads to errors or completely made-up answers.
- Adding the multi tool gives more power to the Agent to use external data and services

