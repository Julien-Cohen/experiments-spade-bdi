import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-small-latest"

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


def ask_mistral(spec, req_list):
    chat_response = client.chat.complete(
        model=model,
        messages=build_messages_for_coverage(spec, req_list),
        max_tokens=2,
    )
    print(
        "I had an interaction with mistral. "
        + "I gave the following spec: "
        + spec
        + "I also gave the following requirements: "
        + req_list
        + "Mistral gave me the following answer: "
        + chat_response.choices[0].message.content
    )
    return chat_response.choices[0].message.content.startswith("COMPLETE")
