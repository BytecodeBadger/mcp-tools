from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
msg = "what is the meaning of life?"
resp = client.chat.completions.create(
    model="llama3.2:1b-instruct-q4_K_S",
    messages=[{"role": "user", "content": msg}],
)
print(resp.choices[0].message.content)