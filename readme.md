# README
## Overview
This repository contains a Python script for running a Telegram bot powered by OpenAI's GPT-3.5 language model. The bot can be trained to converse on a wide range of topics and can be customized to suit various use cases.

## Prerequisites
Before you can run the bot, you'll need to have the following installed on your system:

- Docker
- Docker Compose

You'll also need to create a Telegram bot and obtain an API key. You can follow the instructions on the Telegram website to create a bot and obtain its API key.


Additionally, you'll need to sign up for the OpenAI GPT-3 API and obtain an API key. You can sign up for the API on the OpenAI website.


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
GPT_MODEL=gpt-3.5-turbo #could be replace by gpt-4
BOT_NAME=ChiliBot
DEFAULT_PROMPT="You are ${BOT_NAME}, a large language model based on ChatGPT that is trained by OpenAI (model: ${GPT_MODEL}). Answer as concisely as possible. Knowledge cutoff 2021-09"
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
