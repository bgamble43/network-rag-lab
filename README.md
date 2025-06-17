# Network RAG Lab 📡

A starter for a Cisco‑focused RAG assistant in Python + LangChain + FAISS, containerized for EVE‑NG.

## 🚀 How to Use

1. Fork this repo on GitHub.
2. Clone it inside your EVE‑NG Docker host.
3. Build the image:
   ```bash
   docker build -t network-rag-lab .
   ```
4. Load image into EVE‑NG if needed (`docker save`/`docker load`).
5. Run the container:
   ```bash
   docker run -it network-rag-lab
   ```
6. Inside container:
   ```bash
   git clone https://github.com/YOUR_USERNAME/network-rag-lab.git
   cd network-rag-lab
   echo "OPENAI_API_KEY=sk-…" > .env
   python ask_routing.py "What AD for backup static routes?"
   ```

## ✍️ Customize

- Add more docs in `docs/`.
- Adjust chunk size or retrieval settings in `rag_engine.py`.
- Build out pipelines: Slack bot, Streamlit UI, CI tasks.

## 🔐 Notes
- `.env` is ignored by git. Add your key manually.
- For shared labs, consider using Vault or Docker Secrets.
