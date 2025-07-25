import argparse
import asyncio

import spade

from spade_bdi.bdi import BDIAgent

from dotenv import load_dotenv

import os

import agentspeak
from ask_mistral import ask_mistral

load_dotenv()

tmp_addr = os.getenv("XMPP_ADDR")
chat_server_address = tmp_addr if tmp_addr else "0.0.0.0"

tmp_passwd = os.getenv("AGENT_PASSWD")
agent_password = tmp_passwd if tmp_passwd else ""


def print_state(a):
    print("CURRENT_BELIEFS:" + str(a.bdi.get_beliefs()))


def add(a, k, v):
    print("ADDING BELIEFS: " + k + "=" + v)
    a.bdi.set_belief(k, v)


def remove(a, k, v):
    print("REMOVING BELIEFS: " + k + "=" + v)
    a.bdi.remove_belief(k, v)


async def start(a):
    print("STARTING AGENT")
    await a.start()


class MyCustomBDIAgent(BDIAgent):
    def add_custom_actions(self, actions):
        @actions.add_function(
            ".examine",
            (
                    agentspeak.Literal,
                    agentspeak.Literal,
            ),
        )
        def _examine(s, r):
            return ask_mistral(str(s), str(r))

        @actions.add(".my_action", 1)
        def _my_action(agent, term, intention):
            arg = agentspeak.grounded(term.args[0], intention.scope)
            print(arg)
            yield


async def main(server, password):
    a = MyCustomBDIAgent(f"bdiagent@{server}", password, "coverage_manager.asl")
    print_state(a)
    add(a, "spec", "A function to compare two words.")
    add(a, "req", "* The fonction should take two parameters.")
    await start(a)

    await asyncio.sleep(1)

    print_state(a)

    await start(a)

    await a.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--server", help="XMPP Server")
    parser.add_argument("--password", help="Password")
    args = parser.parse_args()

    if args.server is None:
        server = chat_server_address
    else:
        server = args.server

    if args.password is None:
        passwd = agent_password
    else:
        passwd = args.password
    spade.run(main(server, passwd))
