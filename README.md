# 🤖 LangChain - Chat with Search (Wikipedia + Arxiv + DuckDuckGo)

An interactive **AI-powered search assistant** built using **LangChain**, **Groq LLMs**, and **Streamlit**. This tool allows users to ask questions and get real-time responses pulled from:
- 🧠 Wikipedia  
- 📚 Arxiv (research papers)  
- 🌐 DuckDuckGo (web search)

---

## 🎥 Demo Video

👉 [Watch Demo on Google Drive](https://drive.google.com/file/d/13O07_ogovTOHM3jm_JCvm8Z-6fhmAMZJ/view)

---

## 🖼️ Screenshot

![App Screenshot](https://drive.google.com/uc?export=view&id=1ecOkOmGd-e1gI905UEvIC2CUhHTZ292h)

---

## 🧠 How It Works

1. The user types a query into the chat.
2. The app uses **LangChain agents** to:
   - Search relevant sources using Arxiv, Wikipedia, and DuckDuckGo.
   - Retrieve and summarize content using a **Groq-hosted LLM** (`Llama3-8b-8192`).
3. Results are streamed back with **thought-action-observation** style reasoning via `StreamlitCallbackHandler`.

---

## 🛠️ Tech Stack

| Component            | Tool / Library                          |
|----------------------|------------------------------------------|
| UI Framework         | Streamlit                                |
| LLM Backend          | Groq (`Llama3-8b-8192`)                  |
| Retrieval Wrappers   | LangChain Community (Arxiv, Wikipedia)   |
| Web Search           | DuckDuckGo via `duckduckgo-search`       |
| LangChain Orchestration | Agents + Tools + Memory               |
| Environment Config   | python-dotenv                            |

---

## 📁 Folder Structure

```

langchain-chat-search/
├── app.py               # Main Streamlit app
├── .env                 # Environment file (HF\_TOKEN)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

````

---

## 🧪 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/langchain-chat-search.git
cd langchain-chat-search
````

### 2. Create virtual environment

```bash
python -m venv venv
# Activate the environment:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add environment variables

Create a `.env` file:

```env
HF_TOKEN="your_huggingface_token"
```

You'll input the **Groq API Key** directly in the app sidebar during runtime.

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🧰 Requirements

`requirements.txt`:

```
langchain
python-dotenv
langchain-community
bs4
langchain-text-splitters
sentence_transformers
langchain_huggingface
faiss-cpu
beautifulsoup4
langchain_groq
langchain_core
arxiv
wikipedia
streamlit
duckduckgo-search
```

---

## ✨ Features

* 🔍 Real-time multi-source search (Wikipedia, Arxiv, DuckDuckGo)
* 💬 Chat interface with session memory
* 🧠 LLM-backed reasoning and summarization
* 🔁 Streams live responses with intermediate steps (`Thought → Action → Observation`)

---

## 📚 Use Cases

* Academic research assistant
* General-purpose conversational search
* AI-powered learning companion
* PDF + Web knowledge combo agents (extensible)

---

## 🔐 API Keys Required

* 🧠 [Groq API Key](https://console.groq.com/)
* 🔤 [HuggingFace Token](https://huggingface.co/settings/tokens)

---

## 🧑‍💻 Author

> Built with ❤️ by \[Shivam Gupta]
> GitHub: [@Shivam-Gyan](https://github.com/Shivam-Gyan/Search_Agent)
> LinkedIn: [@shivam-gupta19](https://www.linkedin.com/in/shivam-gupta19/)

---

