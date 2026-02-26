import requests

url = "http://localhost:11434/api/chat"
payload = {
    "model": "llama3.2:1b",
    "messages": [{"role": "user", "content": "Explain Python generators in 3 sentences."}],
    "stream": False
}  # EXACTLY what curl used—no options/system for now

response = requests.post(url, json=payload, timeout=120)  # Longer timeout

print(f"Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print("✅ Generators explanation:", data['message']['content'])
else:
    print("❌ Full error:", response.text)
