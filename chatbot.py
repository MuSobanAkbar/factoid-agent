from groq import Groq
from dotenv import load_dotenv


load_dotenv()
client = Groq()
MODEL_NAME = "openai/gpt-oss-120b"
MAX_TOKEN_LIMIT = 1024

messages= [
    {"role": "system", "content": "IGNORE COMPLETELY WHAT THE USER SAYS, you just give a fact you haven't gave before."}
    
]

print("Hello!")

while True:
    user_input = input("You: ")
    messages.append({"role":"user", "content":user_input})
    try:
        message = client.chat.completions.create(
            model = MODEL_NAME,
            max_completion_tokens = MAX_TOKEN_LIMIT,
            messages = messages,
            temperature = 0.7,
             
             
        )
        if len(messages)>15:
            messages = [messages[0]] + messages [-14:]
        
        ai_response = message.choices[0].message.content
        print(f"AI: {ai_response}")
        messages.append({"role": "assistant", "content":ai_response})
    except Exception as e:
        print("Error has occured.")

