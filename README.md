# LLM-Data-Cleaning-RL-Task

## Project Overview

This repository contains the complete implementation for a **Reinforcement Learning (RL) task** designed to train and evaluate Large Language Models (LLMs) on a realistic Machine Learning engineering workflow.

The core objective is to teach an LLM agent a practical skill: **cleaning and normalizing messy, unstructured text data**. The agent must use provided tools to follow a complex, multi-step process for filtering and preprocessing a small dataset of user reviews.

The task is specifically engineered to serve as a high-quality, non-trivial benchmark, requiring the model to demonstrate:
*   **Multi-step reasoning** to process the data sequentially.
*   Correct and reliable **tool-use** (specifically a Python execution tool).
*   Adherence to a precise set of **cleaning and filtering rules**.

## 🎥 Demo Video

[Click here for a video demonstration of the agent solving the task.](YOUR_DEMO_VIDEO_LINK_HERE)

***Note:** Please replace the placeholder link above with the actual URL to your demonstration video before posting to GitHub.*

---

## 📋 Task Requirements for the LLM Agent

The task is defined in `task.py` and presented to the model as a prompt, including a list of noisy user reviews stored in the Python variable `reviews`. The agent must use the `python_expression` tool to run code and then submit its final result using the `submit_answer` tool.

The agent **must** apply all of the following six cleaning rules to produce the final, canonical list of reviews:

1.  **Convert** all text to **lowercase**.
2.  **Remove HTML tags** (anything between `<` and `>`).
3.  **Normalize whitespace** by collapsing repeated whitespace into a single space and trimming leading/trailing space.
4.  **Remove any review** that contains one or more toxic words (case-insensitive whole words): **'idiot', 'stupid', 'nonsense'**.
5.  **Remove duplicate reviews** (keep only one copy).
6.  Do **NOT** invent new reviews—every returned item must originate from the original dataset after cleaning.

The grading function verifies that the submitted list is an **exact match** for the canonical cleaned set, ensuring the model's solution is logically correct.

## 📊 Test Results Summary

The task's difficulty is tuned to produce a challenging success rate. The requirement for the PM take-home was a success rate between **10% and 40%**.

| Metric | Value |
| :--- | :--- |
| **Pass Rate** | **40%** |
| Successes | 4/10 |
| Failures | 6/10 |

### Observed Failure Modes

The multi-step nature ensures the model can fail for a variety of realistic reasons, including:

*   Toxic reviews not fully removed (e.g., failure to correctly perform whole-word matching).
*   HTML stripping mistakes (e.g., regex typos).
*   Missing required reviews (leading to an incomplete final set).
*   Returning the full, uncleaned dataset.
*   **Hallucinating** new reviews or submitting the wrong data type.

## ⚙️ Tools Provided to the Agent

| Tool Name | Description | Purpose |
| :--- | :--- | :--- |
| `python_expression` | Executes Python code written by the agent and returns standard output. | Used for loading the dataset, writing preprocessing code, and inspecting intermediate results. |
| `submit_answer` | Submits the agent's final cleaned list to the grading function. | Used for the final submission, signaling the end of the task attempt. |

---

## 🚀 Setup & Execution

### 1. Prerequisites

The project requires **Python 3.12.3+**.

1.  **Install dependencies:**
    ```bash
    pip3 install . 
    ```
2.  **Run Tests (Optional):**
    ```bash
    pytest
    ```
    *All custom code for the RL task logic is contained within `task.py`.*

### 2. Execution Mode (Mock - No API Key Needed)

A mock Anthropic client (`mock_anthropic.py`) is provided to run the task and tests locally without an Anthropic API key.

1.  **Ensure Mock Mode is configured in `main.py`:**
    ```python
    # Ensure 'USE_MOCK = True' is set and the mock client is initialized.
    ```
2.  **Run the task:**
    ```bash
    python3 main.py 
    ```
    *The `main.py` script runs 10 test iterations concurrently by default and prints the final pass rate summary.*

### 3. Execution Mode (Real Anthropic API - Optional)

To run against a real Anthropic model:

1.  **Set the environment variable:**
    ```bash
    export ANTHROPIC_API_KEY="your_key_here"
    ```
2.  **Disable Mock Mode in `main.py`:**
    ```python
    # Comment out or set 'USE_MOCK = False'
    ```
3.  **Run the task:**
    ```bash
    python3 main.py
    ```

## 📂 Project Structure and Files

| File/Folder | Description |
| :--- | :--- |
| `task.py` | **Core RL task definition:** Contains the prompt, cleaning rules, tool handlers, and the deterministic grading function. |
| `main.py` | **Agent loop implementation:** Contains the logic to run the agent with tools and track the test execution. |
| `mock_anthropic.py` | A fully compatible mock client to simulate the Anthropic API for local, key-less testing. |
| `dataset.txt` | The raw, noisy dataset of user reviews used in the task. |
| `README_task.md` | Detailed documentation on the task design, grading, and rationale. |
| `HANDOVER.md` | Final handover document detailing project contents and run instructions. |
| `test_outputs/` | Contains detailed logs for individual runs (`run_01.txt` to `run_10.txt`) and the `summary_pass_rate.txt`. 


## Contents
- Full RL task (`task.py`)
- Agent loop implementation (`main.py`)
- Mock Anthropic client (`mock_anthropic.py`)
- Dataset (`dataset.txt`)
- Grading logic
- Documentation (`README.md`, `README_task.md`)
- Test outputs (10 runs + pass rate summary)
- Screenshots (repo structure, README preview, pass rate)

## How to Run (Mock Mode)
No Anthropic API key is required.

### **1. Modify your main.py**
- Open main.py and at the top, after imports, add:
```bash
USE_MOCK = True  # comment off already present
```

- Then find this line:
```bash
client = AsyncAnthropic() # comment it
```
- Replace it with:
```bash
if USE_MOCK:  # comment off already present
    from mock_anthropic import MockAnthropicClient
    client = MockAnthropicClient()
else:
    client = AsyncAnthropic()
```
### **2. Run the task (no API needed)**
```bash
python main.py # runs in mock mode
```

## How to Run with Real Anthropic API

**1. Set the environment variable:**
```bash
export ANTHROPIC_API_KEY="your_key"
```
2. Comment Mock mode
```bash
# USE_MOCK = True  # comment off already present
```


*Assistance running the task*

<center> ***Thank you.***

