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

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PrinsAmbaliya/discoverchatgpt.git
   cd discoverchatgpt
2. **Install Dependencies**:
   Create a virtual environment (optional but recommended) and install the required packages:
   python -m venv venv
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
3. **Set Up Environment Variables**:
   Create a file named token.env in the project directory.
   Add your Discord bot token and Groq API key:
   ```bash
   DISCORD_TOKEN=your_discord_bot_token
   GROQ_API_KEY=your_groq_api_key
4. **Run the Bot**:
   ```bash
   python main.py

## Usage
- Ping Command: Send ping in a channel to get pong.
- Remember Command: Use remember <key> <value> to store data (e.g., remember name John).
- Query Stored Data: Use what is <key> to retrieve data (e.g., what is name returns John).
- AI Chat: Mention the bot with a question or message (e.g., @Bot Tell me about AI), and it will respond using Groq AI.

---

## Author
Prins Ambaliya

GitHub: PrinsAmbaliya

LinkedIn: https://www.linkedin.com/in/prins-ambaliya-bb7546367

