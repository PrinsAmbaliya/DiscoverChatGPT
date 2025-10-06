# DiscoverChatGPT

A Discord bot integrated with Groq AI to provide conversational responses and simple memory functionality. The bot responds to mentions, handles basic commands like `ping`, and supports storing and retrieving information using `remember` and `what is` commands.

## Features
- Responds to `ping` with `pong`.
- Stores key-value pairs with the `remember` command (e.g., `remember name John`).
- Retrieves stored values with the `what is` command (e.g., `what is name`).
- Answers general queries using Groq AI when mentioned (e.g., `@Bot What is AI?`).
- Splits long responses (>2000 characters) into multiple messages to comply with Discord's limits.

## Prerequisites
- Python 3.8 or higher
- A Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications)
- A Groq API key from [Groq Console](https://console.groq.com/keys)
- A Discord server where the bot is invited with permissions to read and send messages
