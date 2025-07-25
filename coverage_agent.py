import os
from mistralai import Mistral

llm_api_key = os.environ["MISTRAL_API_KEY"]
llm_model = "mistral-small-latest"

llm_client = Mistral(api_key=llm_api_key)


def log(m):
    print("[LOG] " + m)


def ask_llm(spec, req_list):
    chat_response = llm_client.chat.complete(
        model=llm_model,
        messages=[
            {
                "role": "system",
                "content": "Given a specification of a system, and a list of atomic requirements, tell if that list of atomic requirements covers well that specification."
                           + " Answer COMPLETE is the specification is well covered."
                           + " Answer PARTIAL otherwise.",
            },
            {
                "role": "user",
                "content": "Specification: "
                           + spec
                           + "(end of the specification) List of requirements: "
                           + req_list
                           + "(end of list of requirements).",
            },
        ],
        max_tokens=2,
    )
    log(
        "I had an interaction with mistral. "
        + "I gave the following spec: "
        + spec
        + "I also gave the following requirements: "
        + req_list
        + " "
        + "Mistral gave me the following answer: "
        + chat_response.choices[0].message.content
    )
    return chat_response.choices[0].message.content.startswith("COMPLETE")


import agentspeak
from spade_bdi.bdi import BDIAgent


class CoverageBDIAgent(BDIAgent):
    def add_custom_actions(self, actions):
        @actions.add_function(
            ".examine",
            (
                    agentspeak.Literal,
                    agentspeak.Literal,
            ),
        )
        def _examine(s, r):
            return ask_llm(str(s), str(r))
