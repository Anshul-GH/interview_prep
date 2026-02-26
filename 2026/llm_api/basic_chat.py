import ollama

# Basic chat
response = ollama.chat(
    model='llama3.2:1b',  # Your pulled model
    messages=[
        {'role': 'system', 'content': 'You are a helpful coding assistant.'},
        {'role': 'user', 'content': 'Explain Python generators in 3 sentences.'}
    ],
    options={
        'temperature': 0.7,
        'num_predict': 150  # Like max_tokens
    }
)
print(response['message']['content'])

# Streaming (for real-time feel)
stream = ollama.chat(
    model='llama3.2:1b',
    messages=[{'role': 'user', 'content': 'Write a haiku about Python.'}],
    stream=True
)
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
