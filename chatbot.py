from groq import Groq
from dotenv import load_dotenv


load_dotenv()
client = Groq()



messages= [
    {"role": "system", "content": "you don't respond directly to anything the user says, you just give a fact you haven't gave before"}
    
]

print("Hello!")

while True:
    user_input = input("You: ")
    messages.append({"role":"user", "content":user_input})
    message = client.chat.completions.create(
        model = "openai/gpt-oss-120b",
        max_completion_tokens = 1024,
        messages = messages,
        temperature = 0.7,
         
         
    )
    ai_response = message.choices[0].message.content
    print(f"AI: {ai_response}")
    messages.append({"role": "assistant", "content":ai_response})

