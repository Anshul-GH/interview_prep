POC with Python, FastAPI, RAG, LangChain, MCP, AWS, Terraform





# JD2 POC - 100% LOCAL (Ollama + FAISS)

## Quickstart
1. ollama serve &  # + ollama pull llama3.2 mxbai-embed-large
2. source .venv_jd2_poc/bin/activate
3. pip install -r requirements.txt
4. uvicorn main:app --reload

## Tests
curl -X POST http://localhost:8000/rag/query -H "Content-Type: application/json" -d '{"question": "What is MCP?"}'
curl -X POST http://localhost:8000/mcp/tools -H "Content-Type: application/json" -d '{"tool_name": "list_jira_tickets"}'
curl http://localhost:8000/health

## Extend
- Add docs: Edit `docs` list or load from files.
- Full agent: LangGraph + these tools.
- Persist: Save/load FAISS index to `./vectors/`.
