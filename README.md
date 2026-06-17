# 🎓 AI Tutor Lite v1

A backend-powered AI tutor chatbot where students ask questions and get intelligent responses — stored per user in PostgreSQL.

Built with **FastAPI**, **PostgreSQL**, **JWT authentication**, and **GEMINI LLM API**.

---

## ✨ Features

- 🔐 JWT-based user authentication (register, login, logout)
- 🤖 AI responses via GEMINI LLM API
- 🗄️ Per-user chat history stored in PostgreSQL
- ⚡ Fully async backend with SQLAlchemy + asyncpg
- 🔄 Database migrations with Alembic
- 🌐 Minimal HTML/CSS/JS frontend

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI (Python) |
| Database | PostgreSQL + SQLAlchemy (async) |
| Auth | JWT (python-jose) + bcrypt |
| LLM | GEMINI API |
| Migrations | Alembic |

---

## 📁 Project Structure

```
ai-tutor/
├── main.py               # App entry point, lifespan
├── database.py           # Async engine, session, Base
├── models/
│   ├── user.py           # User model
│   └── chats.py          # Chat history model
├── routers/
│   ├── auth.py           # Register, login routes
│   └── chat.py           # Chat + history routes
├── authMain.py           # JWT token logic, get_current_user_db
├── static/               # JS and CSS
│   ├── chat.js           
│   ├── auth.js
│   └── style.css
├── templates/              # HTML frontend
│   ├── chat.html           
│   ├── login.html
│   └── signup.html
├── alembic/              # DB migrations
├── .env                  # Environment variables (not committed)
└── requirements.txt
```

---

## ⚙️ Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/ai-tutor-lite-v1.git
cd ai-tutor-lite-v1
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Create `.env` file
```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost/aitutor
SECRET_KEY=your_secret_key_here
GEMINI_API_KEY=your_gemini_key_here
```

### 4. Run migrations
```bash
alembic upgrade head
```

### 5. Start the server
```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000` for the app or `http://127.0.0.1:8000/docs` for Swagger UI.

---

## 🔌 API Endpoints

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/auth/signup` | ❌ | Create new user |
| POST | `/auth/login` | ❌ | Login, get JWT token |
| POST | `/chat/chat` | ✅ | Ask AI a question |
| GET | `/chat/history` | ✅ | Load chat history |

---

## 📸 Application Preview

### Login Page

![Login Page](screenshots/login.png)

### Chat Interface

![Chat Page](screenshots/chat.png)

---

## 🏗️ Application Flow

```text
User Login
↓
JWT Token Issued
↓
User Sends Question
↓
Gemini Generates Response
↓
Chat Saved To PostgreSQL
↓
History Retrieved From Database

---

## 🚀 What's Next

## 🚀 Roadmap

- [x] JWT Authentication
- [x] Gemini Integration
- [x] Chat History
- [x] PostgreSQL Storage
- [ ] PDF Upload Support
- [ ] Vector Embeddings
- [ ] pgvector Integration
- [ ] RAG Pipeline
- [ ] Docker Deployment
- [ ] Cloud Deployment

---

## 👨‍💻 Author

**AKUMARTHI MARIYA RAJU** — BSc Mathematics (8.51 CGPA)
Passionate about AI integration in education.

[LinkedIn](https://www.linkedin.com/in/mariya-raju-akumarthi-687354417) · [GitHub](https://github.com/imLeo007/imLeo007)
