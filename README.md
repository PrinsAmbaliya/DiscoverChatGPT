# DiscoverChatGPT 

A Discord bot powered by **Groq LLMs** that can chat, remember simple facts, and respond when mentioned in a server.

> **Security Notice**: Never commit API keys, tokens, or secrets to GitHub. This project uses environment variables for safety.

---

##  Features

* Responds when mentioned in Discord
* `ping` → `pong`
* Remembers simple key–value data using `remember <key> <value>`
* Answers math / expressions with `what is <expression>`
* Uses **Groq (LLaMA 3.1)** for AI chat responses

---

##  Example Commands

```text
@Bot remember city London
@Bot what is city
@Bot what is 2 + 2
@Bot tell me a joke
```

---

##  Project Structure

```
DiscoverChatGPT/
│── main.py
│── requirements.txt
│── .gitignore
│── .env        # NOT committed
│── README.md
```

---

##  Requirements

* Python 3.10+
* Discord Bot Token
* Groq API Key

Install dependencies:

```bash
pip install -r requirements.txt
```

---

##  Environment Variables

Create a `.env` file in the project root:

```env
DISCORD_TOKEN=your_discord_bot_token
GROQ_API_KEY=your_groq_api_key
```

Make sure `.env` is listed in `.gitignore`.

---

##  Running the Bot

```bash
python main.py
```

If successful, you will see:

```text
Logged on as <bot-name>
```

---

##  Security Best Practices

*  Never hardcode tokens in source files
*  Never push `.env` files to GitHub
*  Rotate tokens immediately if leaked
*  Use GitHub Push Protection

---

##  Notes

* Memory is stored **in RAM only** (resets on restart)
* Discord message limit handled (2000 chars)

---

##  License

This project is for **educational purposes**. Use responsibly.

---

##  Author

Prins Ambaliya

GitHub: PrinsAmbaliya

LinkedIn: https://www.linkedin.com/in/prins-ambaliya-bb7546367
