import llm_chat




import agentspeak
from spade_bdi.bdi import BDIAgent


class CoverageBDIAgent(BDIAgent):
    """ An agent based on AgentSpeak behavior defined in coverage_agent.asl

    Two custom actions are also defined: .external_examine_coverage and .external_add_req
    Those actions rely on a dialogue with an LLM.
    """

    def __init__(self, id, password):
        super().__init__(id, password, "coverage_agent.asl")

    # this method is called by super class __init__(...)
    def add_custom_actions(self, actions):

        # first custom action
        @actions.add_function(
            ".external_examine_coverage",
            (
                agentspeak.Literal,
                agentspeak.Literal,
            ),
        )
        def _examine_coverage(s, r):
            return llm_chat.ask_llm_for_coverage(str(s), str(r))

        # second custom action
        @actions.add_function(
            ".external_add_req",
            (
                agentspeak.Literal,
                agentspeak.Literal,
            ),
        )
        def _add_req(s, r):
            return agentspeak.Literal(
                str(r) + " * " + llm_chat.ask_llm_for_completion(str(s), str(r))
            )
