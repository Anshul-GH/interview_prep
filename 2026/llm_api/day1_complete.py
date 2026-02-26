import requests
import json
import time

def chat(prompt, system=None, temp=0.7, max_tokens=150):
    payload = {
        "model": "llama3.2:1b",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    if system:
        payload["messages"].insert(0, {"role": "system", "content": system})
    payload["options"] = {"temperature": temp, "num_predict": max_tokens}
    
    response = requests.post("http://localhost:11434/api/chat", json=payload, timeout=180)
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        return data['message']['content']
    else:
        print("Raw error:", response.text)
        return None

# Day 1: 5–10 prompt experiments
prompts = [
    "Explain Python generators in 3 sentences.",
    "Write a haiku about APIs. (creative)",
    "List 3 benefits of async Python.",
    "Debug: def fib(n): return n if n < 2 else fib(n-1) + fib(n-2)",
    "Compare lists vs tuples in Python."
]

print("=== Day 1 LLM Experiments ===\n")
for i, prompt in enumerate(prompts, 1):
    print(f"\n--- Prompt {i} ---")
    resp = chat(prompt)
    if resp:
        print(resp[:200] + "..." if len(resp) > 200 else resp)
    time.sleep(1)  # Rate limit politeness

print("\n✅ Day 1 complete! Log these to prompts_log.md")
