import argparse
import asyncio

import spade

from dotenv import load_dotenv

import os

from coverage_agent import CoverageBDIAgent

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


async def main(server, password):
    a = CoverageBDIAgent(f"bdiagent@{server}", password, "coverage_agent.asl")
    print_state(a)
    add(a, "spec", "A function to compare two words.")
    add(a, "req", "* The fonction should take two parameters.")
    await start(a)

    await asyncio.sleep(1)
    print_state(a)
    await start(a)

    await asyncio.sleep(2)
    await start(a)
    print_state(a)

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
