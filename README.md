# experiments-spade-bdi

## Installation tips

The latest versions of some packages break spade (see https://github.com/javipalanca/spade/issues/127). So use those
ones instead (overridden by requirements.txt):

```
spade==4.0.3
pyjabber==0.2.4
slixmpp==1.9.1
```

## Configuration

Add in your environment (shell or .env file) two variables to set the address of the chat server (see below) and the
password of your agent on the chat server (see below).

```
XMPP_ADDR=...
AGENT_PASSWD=...
```

You should also give as an environment variaple you API key for the target LLM (currently Mistral) :

```
MISTRAL_API_KEY=...
```

## Run tips

Reminder (from Spade): launch the chat server before running the agent with run spade (see prepare.sh)

Tip : On the first connexion of an agent to the chat server, the user is created and the password is set.
