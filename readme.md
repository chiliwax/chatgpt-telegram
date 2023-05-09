# README

## Overview

This repository contains a Python script for running a Telegram bot powered by OpenAI's GPT-3.5 language model. The bot can be trained to converse on a wide range of topics and can be customized to suit various use cases.

## Prerequisites

Before you can run the bot, you'll need to have the following installed on your system:

- Docker
- Docker Compose

You'll need to sign up for the OpenAI API and obtain an API key. You can sign up for the API on the OpenAI website [here](https://platform.openai.com/account/api-keys).

You'll also need to create a Telegram bot and obtain an API key. You can follow the instructions on the Telegram website to create a bot and obtain its API key or follow the instruction bellow.

### Telegram - create bot

Create an account on telegram, download the app, and from that follow the bellow instruction :

- Go to Contacts tab
- find `@BotFather` and open a discution
- write `/newbot` in order to create your bot and follow the instruction on your screen. At the end of the process it should give you a link to your bot. Open it and write anything to keep a conversation in your Chats tab.
- At this step @botFather should give you the API KEY. keep it safe, you will need it later
- Go back to BotFather conversation
- write `/mybots`
- select the bot you just created
- choose `Edit Bot` following by `Edit Commands`
- add thooses commands :
  ```
  setagent - Define the prePrompt
  reset - Clean conversation history and set default prompt
  kill - Emergency kill app
  ```
- you should be good to go !

### Telegram - get discution ID

In order to get the discution ID (discution between you and your bot), You could make an API request :

```curl
curl --request GET \
  --url http://api.telegram.org/bot<YOUR-BOT-KEY>/getUpdates
```

it will return a json like that :

```json
{
	"ok": true,
	"result": [
		{
			"update_id": 9xxxxxxxx2,
			"message": {
				"message_id": 7,
				"from": {
					"id": ******,
					"is_bot": false,
					"first_name": "************",
					"last_name": "**********",
					"language_code": "en"
				},
				"chat": {
					"id": 5xxxxxxx9,  <-- YOUR CONVERSATION ID
					"first_name": "**********",
					"last_name": "**********",
					"type": "private"
				},
				"date": 1683223403,
				"text": "Fhf"
			}
		}
	]
}
```

Getting the conversation ID will allow us to make sure that only you could speak to your GPT BOT !

At this step you should have :

- An OpenAI API Key
- A token for your Telegram BOT
- The discution ID between you and the bot

## Installation

Clone this repository to your local machine:

```sh
git clone https://github.com/chiliwax/chatgpt-telegram
```

Navigate to the repository directory:

```sh
cd chatgpt-telegram
```

Create a .env file in the root directory and add the following environment variables:

```sh
#APIS KEY
GPT_API_KEY=<YOUR-API-KEY>
TELEGRAM_BOT_TOKEN=<YOUR-BOT-KEY>
TELEGRAM_AUTHAURIZE_CHANNEL=<YOUR-CHANNEL-ID>
#CONFIGURATION
GPT_MODEL=gpt-3.5-turbo # could be replace by gpt-4 (on waitlist now)
BOT_NAME=ChiliBot # whatever you want
DEFAULT_PROMPT="You are ${BOT_NAME}, a large language model based on ChatGPT that is trained by OpenAI (model: ${GPT_MODEL}). Answer as concisely as possible. Knowledge cutoff 2021-09" # could be what you want
```

Build the Docker image:

```sh
docker-compose build
```

## Usage

To start the bot, run the following command:

```sh
docker-compose up -d
```

This will start the bot as a Docker container in detached mode.

To stop the bot, run the following command:

```sh
docker-compose down
```

## Customization

You can customize the bot by modifying the main.py script. The script contains a number of functions that handle various Telegram commands and messages. You can modify these functions to change the behavior of the bot.

You can also customize the behavior of the OpenAI GPT-3.5 language model by modifying the GPT_MODEL and DEFAULT_PROMPT environment variables in the .env file. You can change the model to a different version of GPT-3 or a different language model altogether. You can also customize the default prompt that the bot uses when it starts a conversation.

## Troubleshooting

- You could experience some trouble to make your Telegram bot running. It could take some time (30min/1hour) to have it completely functionnal. (no worry in case of no responding at the beginning) :) 

## Links

GPT-4 waitlist : https://openai.com/waitlist/gpt-4-api


