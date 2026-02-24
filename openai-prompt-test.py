# from openai import OpenAI

# # Client automatically reads OPENAI_API_KEY from environment
# client = OpenAI()
# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a AiOps Engineer Assistance."},
#         {"role": "user", "content": "Explain How to start AiOps Journey for a DevOps Engineer."}
#     ]
# )
# print(response.choices[0].message.content)

###Basic Prompt####

from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Explain Docker in simple words"}
    ]
)
print(response.choices[0].message.content)

