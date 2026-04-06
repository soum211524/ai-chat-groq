# AI Chat System:

A minimal AI-powered chat system built with **Groq API**, **LangChain**, and **FastAPI** — without using ChatGPT or OpenAI.

---

## 🚀 Tech Stack

| Layer | Technology |
|-------|-----------|
| LLM Inference | [Groq API](https://groq.com) (llama-3.3-70b-versatile) |
| AI Framework | LangChain (ConversationChain + Memory) |
| Backend | FastAPI (Python) |
| Frontend | Vanilla HTML, CSS, JavaScript |

---

## 📁 Project Structure

```
ai-chat-groq/
├── app.py          # FastAPI backend with Groq + LangChain
├── index.html      # Frontend chat UI
├── .env            # API keys (not committed)
├── .gitignore      # Ignores .env and cache files
└── README.md
```

---

## ⚙️ How It Works

1. User types a message in the browser
2. Frontend sends a `POST /chat` request to the FastAPI backend
3. LangChain's `ConversationChain` processes the message with memory
4. Groq API runs inference using the LLaMA 3.3 70B model
5. Response is returned and displayed in the chat UI

```
User → index.html → FastAPI (app.py) → LangChain → Groq API → LLaMA 3.3
```

---

## 🛠️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/soum211524/ai-chat-groq.git
cd ai-chat-groq
```

### 2. Install dependencies
```bash
pip install fastapi uvicorn langchain langchain-groq python-dotenv
```

### 3. Configure environment variables
Create a `.env` file in the root folder:
```
GROQ_API_KEY=your_groq_api_key_here
```
> Get your free API key at https://console.groq.com

### 4. Run the backend
```bash
python app.py
```
Server starts at `http://localhost:8000`

### 5. Open the frontend
Simply open `index.html` in your browser.

---

## 💬 Features

- Real-time AI chat interface
- Conversation memory (remembers previous messages)
- Fast inference via Groq (low latency)
- Clean minimal UI — no frameworks
- Secure API key handling via `.env`

---



---

## 📦 Dependencies

```
fastapi
uvicorn
langchain
langchain-groq
python-dotenv
```

---


GitHub: [@soum211524](https://github.com/soum211524)

---

> ⚠️ Never commit your `.env` file. The `.gitignore` already handles this.
