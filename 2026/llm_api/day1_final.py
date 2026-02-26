# day1_final.py - Complete Day 1
import requests
import json
import time

def ollama_chat(prompt, model="tinyllama", system="You are a helpful assistant.", temp=0.7):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        "stream": False,  # Single JSON response
        "options": {"temperature": temp, "num_predict": 200}
    }
    
    resp = requests.post(url, json=payload, timeout=180)
    if resp.status_code == 200:
        return resp.json()['message']['content']
    else:
        print(f"Error {resp.status_code}: {resp.text}")
        return None

# Your 5 Day 1 experiments
experiments = [
    "Explain Python generators in 3 sentences.",
    "Write a haiku about APIs.",
    "List 3 Python design patterns with brief examples.",
    "Compare async/await vs threading in Python.",
    "Debug this: def factorial(n): return n * factorial(n-1)"
]

print("=== DAY 1: LLM API EXPERIMENTS ===\n")
results = []
for i, prompt in enumerate(experiments, 1):
    print(f"Prompt {i}: {prompt[:60]}...")
    response = ollama_chat(prompt)
    if response:
        print(f"✅ Response: {response[:150]}...")
        results.append((prompt, response))
    print("-" * 50)
    time.sleep(2)  # Polite pause

# Auto-save log
with open("prompts_log.md", "w") as f:
    f.write("# Day 1 Prompts Log\n\n")
    f.write("| # | Prompt | Response Preview |\n")
    f.write("|---|--------|------------------|\n")
    for i, (p, r) in enumerate(results, 1):
        f.write(f"| {i} | {p[:50]}... | {r[:100]}... |\n")

print(f"\n✅ Day 1 COMPLETE! Check prompts_log.md ({len(results)} experiments logged)")
print("Git commit: git add . && git commit -m 'Day 1: Ollama tinyllama chat experiments'")
