from ollama import chat, ChatResponse

messages = [
    {
        'role': 'user',
        'content': 'What did i ask you previously?/nothink',
        'format': 'json'
    },
]

def ask(message):
    messages.append({'role': 'user', 'content': message, 'format': 'json'})
    response: ChatResponse = chat(model='hf.co/Qwen/Qwen3-1.7B-GGUF:latest', messages=[*messages], stream=True)
    # This stores ther response
    qwen_response = ""
    for line in response:
        chunk = line.message.content.replace("<think>", '').replace("</think>", '').replace("\n", "")
        qwen_response+= chunk
        # This one prints it
        print(chunk, end='', flush=True)
    messages.append({'role': "assistant", 'content': response, qwen_response: 'json'})

ask('How are you')