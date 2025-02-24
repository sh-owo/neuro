from ollama import chat
from typing import Optional

def chat_mainlm(query : Optional[str] = None) -> str:
    MODEL_NAME = "llama3.2"

    stream = chat(
        model=MODEL_NAME,
        messages=[{'role': 'user', 'content': query}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        # return chunk['message']['content']