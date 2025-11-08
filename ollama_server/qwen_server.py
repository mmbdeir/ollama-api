import requests, json

r = requests.post("http://localhost:11434/api/generate", json={
    "model": "hf.co/Qwen/Qwen3-1.7B-GGUF:latest",
    "prompt": "Write a small paragraph on dolphins./no_think",
    "stream": True
}, stream=True)

for line in r.iter_lines():
    if line:
        try:
          res = json.loads(line).get("response")
          if res:
             print(res, end='', flush=True)
        except json.JSONDecodeError:
           continue