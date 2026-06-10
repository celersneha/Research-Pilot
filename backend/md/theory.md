# LCEL Breakdown

```python
prompt_value = prompt.invoke(data)
```

### Step 1: Create Prompt

- Fill the prompt template with input data.
- Converts variables into a formatted prompt for the LLM.

---

```python
response = llm.invoke(prompt_value)
```

### Step 2: Generate Response

- Send the formatted prompt to the LLM.
- The model processes the prompt and returns an AI response.

---

```python
final_output = parser.invoke(response)
```

### Step 3: Parse Output

- Extract and format the LLM response.
- Convert the response into a plain string or desired structure.

---

## Flow

```text
Input Data
    ↓
Prompt Template
    ↓
LLM
    ↓
Output Parser
    ↓
Final Result
```

## LCEL Equivalent

```python
chain = prompt | llm | StrOutputParser()
```

This performs the same three steps automatically:

```text
Input Data
    ↓
Prompt
    ↓
LLM
    ↓
Parser
    ↓
Final Output
```
