# Final Handover – RL Task for LLM Training

This project contains a complete Reinforcement Learning task designed for LLM training and evaluation.

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

## Files Delivered

**Code files: main.py, task.py, test_task.py**

**Support: mock_anthropic.py**

**Dataset: dataset.txt**

**Docs: README.md, README_task.md, HANDOVER.md**

**Test results: test_outputs/**

**Summary: summary_pass_rate.txt**

## Support Window

**I will provide 3 days of post-handover support for:**
*Minor fixes*

*Clarifications*

*Assistance running the task*

<center> ***Thank you.***
