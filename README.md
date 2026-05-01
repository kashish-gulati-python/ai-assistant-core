# AI Assistant

A full-stack AI orchestration platform. This project serves as an intelligent backend for document RAG (Retrieval-Augmented Generation) and automated chat services.

## Project Structure
```text
ai-assistant/
├── backend/
│   ├── app/
│   │   ├── api/        # API Routes
│   │   ├── services/   # Business logic (LLM/RAG calls)
│   │   ├── models/     # Pydantic schemas
│   │   └── main.py     # Application entry point
│   └── requirements.txt
```

## Getting Started
### 1. Clone the repository:

```bash
git clone <your-repo-url>
cd ai-assistant
```

### 2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies:

```bash
pip install -r backend/requirements.txt
Run the application:
```

### 4. Run the application
```bash
uvicorn backend.app.main:app --reload
```

The API will be available at http://127.0.0.1:8000. Access the docs at http://127.0.0.1:8000/docs.
