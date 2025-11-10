from ollama import chat, ChatResponse

messages = []

def ask(message):
    messages.append({'role': 'user', 'content': f'{message}/no_think', 'format': 'json'})
    response: ChatResponse = chat(model='hf.co/Qwen/Qwen3-1.7B-GGUF:latest', messages=[*messages], stream=True)
    # This stores ther response
    qwen_response = ""
    for line in response:
        chunk = line.message.content.replace("<think>", '').replace("</think>", '').replace("\n", "").replace("/nothink", "")
        qwen_response+= chunk
        # This one prints it
        print(chunk, end='', flush=True)
    messages.append({'role': "assistant", 'content': qwen_response, 'format': 'json'})
    print(messages)

ask('Very explain why the sky is blue')
ask('Relate that to my eyes')