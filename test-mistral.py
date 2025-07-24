import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
# model = "mistral-large-latest" # paid
model = "mistral-small-latest"  # free

client = Mistral(api_key=api_key)


def build_messages_for_coverage(spec_descr, req_list):
    return [
        {
            "role": "system",
            "content": "Given a specification of a system, and a list of atomic requirements, tell if that list of atomic requirements covers well that specification."
                       + " Answer COMPLETE is the specification is well covered."
                       + " Answer PARTIAL otherwise.",
        },
        {
            "role": "user",
            "content": "Specification: "
                       + spec_descr
                       + "(end of the specification) List of requirements: "
                       + req_list
                       + "(end of list of requirements).",
        },
    ]


chat_response = client.chat.complete(
    model=model,
    messages=build_messages_for_coverage(
        "A software that compares two words.", "* It takes two words as parameters."
    ),
    max_tokens=2,
)
print("[" + chat_response.choices[0].message.content + "]")
