from ollama import chat

response= chat(model='hf.co/Qwen/Qwen3-1.7B-GGUF:latest', messages=[
  {
    'role': 'user',
    'content': 'What did i ask you previously?/nothink',
    'format': 'json'
  },
],
  stream=True
)

for line in response:
    print(line.message.content, end='', flush=True)