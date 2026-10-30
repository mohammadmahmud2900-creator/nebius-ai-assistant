import os
from openai import OpenAI
client = OpenAI(base_url="https://api.studio.nebius.com/v1/", api_key=os.environ.get("NEBIUS_API_KEY"))
def ask_ai(q):
    r=client.chat.completions.create(model="meta-llama/Meta-Llama-3.1-70B-Instruct",messages=[{"role":"user","content":q}])
    return r.choices[0].message.content
print(ask_ai(input("Ask: "))
