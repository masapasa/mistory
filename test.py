#%%
from mistralai.client import MistralClient
from mistralai.models.

# init the client but point it to TGI
client = MistralClient(api_key="-", endpoint="http://127.0.0.1:8080")
chat_response = client.chat(
    model="-",
    messages=[
      ChatMessage(role="user", content="What is the best French cheese?")
    ]
)

print(chat_response.choices[0].message.content)
#%%
# Synchronous Example
from mistralai import Mistral
import os

s = Mistral(
    api_key=os.getenv("MISTRAL_API_KEY", ""),
)

res = s.chat.complete(model="mistral-small-latest", messages=[
    {
        "content": "Who is the best French painter? Answer in one short sentence.",
        "role": "user",
    },
])

if res is not None:
    # handle response
    pass
# %%
res
# %%
res.choices[0].message.content
# %%
