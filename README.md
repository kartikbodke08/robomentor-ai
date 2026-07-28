# RoboMentor AI

### An AI-Powered Coding & Robotics Learning Assistant

RoboMentor AI is an AI-powered learning assistant that helps beginners understand programming, electronics, and robotics concepts through natural conversations.

The goal of this project was to build a complete AI application from scratch while learning how modern AI systems are designed. Instead of creating only an LLM interface, the project focuses on integrating a frontend, backend, database, and AI model into a single production-ready application.

This project represents Version 1 (MVP) of RoboMentor AI.

---

# Features

- AI-powered chatbot using Google's Gemini model
- Beginner-friendly explanations
- Multi-turn conversations
- Conversation history management
- Responsive chat interface
- FastAPI REST API backend
- React frontend
- SQLite database integration
- Clean modular project structure

---

# Tech Stack

## Frontend

- React
- Vite
- CSS

## Backend

- FastAPI
- Python
- SQLAlchemy
- Google Gemini API
- Python Dotenv

## Database

- SQLite

---

# Project Structure

```
RoboMentor_AI
│
├── backend
│   ├── app
│   │   ├── api
│   │   ├── core
│   │   ├── database
│   │   ├── models
│   │   ├── prompts
│   │   ├── routes
│   │   ├── schemas
│   │   ├── services
│   │   └── main.py
│   │
│   ├── .env
│   ├── pyproject.toml
│   └── README.md
│
├── frontend
│   ├── src
│   │   ├── assets
│   │   ├── components
│   │   ├── services
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# Architecture

```
                React Frontend
                      │
                      ▼
              FastAPI REST API
                      │
                      ▼
         Conversation Management
                      │
                      ▼
             Google Gemini API
                      │
                      ▼
               AI Generated Reply
                      │
                      ▼
             Response to Frontend
```

---

# How It Works

1. The user enters a question in the React application.
2. The frontend sends the request to the FastAPI backend.
3. The backend creates or retrieves the current conversation.
4. The user's prompt is forwarded to Google's Gemini model.
5. Gemini generates a response.
6. The conversation is stored in the database.
7. The response is returned to the frontend and displayed in the chat window.

---

# Getting Started

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/RoboMentor_AI.git

cd RoboMentor_AI
```

---

# Backend Setup

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -e .
```

Create a `.env` file inside the backend folder.

```env
GEMINI_API_KEY=YOUR_API_KEY
GEMINI_MODEL=gemini-3.6-flash
```

Run the backend

```bash
uvicorn app.main:app --reload
```

Backend will start on

```
http://127.0.0.1:8000
```

---

# Frontend Setup

Move into the frontend folder

```bash
cd frontend
```

Install dependencies

```bash
npm install
```

Run the development server

```bash
npm run dev
```

Frontend will start on

```
http://localhost:5173
```

---

# Current Version

## Version 1.0 (MVP)

### Completed

- AI Chat
- Gemini Integration
- Conversation Management
- React Frontend
- FastAPI Backend
- SQLite Database
- REST API Integration
- Responsive User Interface

---

# Testing

The MVP has been tested for the following scenarios:

- Normal conversation
- Multiple consecutive questions
- Page refresh
- Empty input
- Long prompts
- Backend restart
- Backend unavailable
- API error handling
- Frontend-backend communication

---

# Challenges Faced

Some of the key challenges while building this project were:

- Connecting the React frontend with the FastAPI backend.
- Managing conversation state across multiple requests.
- Debugging API communication issues.
- Configuring CORS correctly.
- Integrating Google's Gemini API.
- Structuring the project for scalability.

Working through these problems helped me understand how real-world AI applications are developed and debugged.

---

# What I Learned

This project helped me gain practical experience with:

- FastAPI
- React
- REST APIs
- SQLAlchemy
- Environment variable management
- AI model integration
- Prompt engineering
- Debugging frontend-backend communication
- Project architecture
- Git and GitHub workflow

---

# Future Improvements

Possible enhancements for future versions include:

- Retrieval-Augmented Generation (RAG)
- File upload support
- Voice interaction
- Authentication
- Streaming AI responses
- Better conversation memory
- Markdown rendering
- Code syntax highlighting

---

# About This Project

The primary objective of RoboMentor AI was to understand the complete lifecycle of building an AI-powered application—from designing the frontend and backend to integrating an LLM, managing conversations, and preparing the project for deployment.

Rather than focusing only on AI APIs, this project emphasizes full-stack AI application development.

---

# Author

**Kartik Bodke**

B.E. Artificial Intelligence & Data Science

PVG's College of Engineering and Technology, Pune

---

## If you found this project interesting, feel free to give it a ⭐ on GitHub.