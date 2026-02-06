# 🌍 Multi-Agent AI Travel Planner

A professional-grade Travel Planning application built with **LangGraph** and **Ollama (Mistral)**. This project demonstrates advanced AI engineering concepts like state machines, persistent SQLite memory, and multi-agent orchestration.

## 🚀 Key Features
- **Multi-Agent Orchestration**: Specialized agents for flights, accommodation, and presentation.
- **Persistent Memory**: Uses `SqliteSaver` to remember user history across sessions.
- **Local LLM**: Privacy-focused execution using **Mistral** via Ollama.
- **Automated Reporting**: Generates downloadable PDF itineraries.

## 🛠 Tech Stack
- **Framework**: LangChain & LangGraph
- **Brain**: Mistral (Local via Ollama)
- **UI**: Gradio
- **Storage**: SQLite
- **Tools**: DuckDuckGo Search API

## 📂 Installation
1. Install [Ollama](https://ollama.ai/) and run `ollama pull mistral`.
2. Clone this repo.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run the app: `python main.py`.

## 🧠 Architecture
The system uses a **Directed Acyclic Graph (DAG)** where state is passed between nodes. Each node represents a specific AI agent specialized in one task.
<img width="1855" height="842" alt="scrrenshot Travel Planner" src="https://github.com/user-attachments/assets/245e1b7a-4bc5-493e-9d09-44dce9f50cad" />

