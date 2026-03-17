# 🏫 School MCP Agent Admin: Local Agentic AI PoC

[![MCP](https://img.shields.io)](https://modelcontextprotocol.io)
[![Ollama](https://img.shields.io)](https://ollama.com)

**School MCP Agent Admin** is a privacy-first, local-first management system powered by the **Model Context Protocol (MCP)**. It allows school administrators to query student data and generate PDF reports using natural language, all running on a **local LLM**. A Local Agentic School Management System using Model Context Protocol (MCP), LangGraph, and Ollama. Feature-rich PoC with SQLite data, PDF reporting, and an AI-driven Streamlit interface.

## 🏗️ Architecture
- **Host:** Streamlit (Web UI)
- **Orchestrator:** LangGraph + LangChain
- **Client:** MCP Python SDK (Subprocess Transport)
- **Server:** FastMCP (Python)
- **LLM:** Ollama (Llama 3.1)
- **Backend:** SQLite

## 🚀 Getting Started

### 1. Prerequisites
- Install [Ollama](https://ollama.com) and run `ollama pull llama3.1`.
- Python 3.10+.

### 2. Installation
```bash
git clone https://github.com/NxtGenCodeBase/mcp-local-school-orchestrator.git
cd school-mcp-agent-admin
pip install -r requirements.txt

## Project structure

school-mcp-agent-admin/
├── .gitignore
├── README.md
├── requirements.txt
├── database.py       # Mock Backend Data Layer
├── server.py         # MCP Server (The Tools)
├── orchestrator.py   # MCP Client & LangGraph Logic
└── app.py            # Streamlit Host Interface

## How it works:

Host (Streamlit) receives your question: "Generate a report for me."
Host passes this to the Orchestrator (LangGraph/Ollama) to reason.
The Orchestrator tells the Client (ClientSession): "I need to run the generate_student_report tool."
The Client sends a JSON-RPC message over stdio to the Server (server.py).
Server executes the Python code, creates the PDF, and sends the path back to the Client. 

