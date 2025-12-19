# mock_anthropic.py
# Fully compatible mock Anthropic client for running demo videos without API key.

import time
import random

class MockContent:
    def __init__(self, text=None, tool_name=None, tool_input=None, tool_id=None):
        self.type = "text" if tool_name is None else "tool_use"
        self.text = text
        self.name = tool_name
        self.input = tool_input
        self.id = tool_id

class MockResponse:
    def __init__(self, content):
        self.content = content
        self.stop_reason = "tool_use"

class MockMessages:
    async def create(self, **kwargs):
        time.sleep(0.3)  # simulate delay

        succeed = random.random() < 0.4

        if succeed:
            # Fake correct tool usage
            return MockResponse([
                MockContent(text="Cleaning dataset..."),
                MockContent(
                    tool_name="python_expression",
                    tool_input={"expression": "print(['cleaned', 'data'])"},
                    tool_id="tool1"
                ),
                MockContent(
                    tool_name="submit_answer",
                    tool_input={"answer": [
                        "i love this product!!!",
                        "pretty good overall",
                        "decent, could be better",
                        "excellent — highly recommend!"
                    ]},
                    tool_id="tool2"
                )
            ])
        else:
            # Fake failure
            return MockResponse([
                MockContent(text="Attempting cleaning..."),
                MockContent(
                    tool_name="submit_answer",
                    tool_input={"answer": []},
                    tool_id="tool_fail"
                )
            ])

class MockAnthropicClient:
    def __init__(self):
        # match real Anthropic API structure
        self.messages = MockMessages()
