# 🎁 AI Gift Idea Generator

An AI-powered web application that generates personalized gift suggestions based on a person's relationship with the recipient, age, budget, and interests.

## ✨ Features

- Generate personalized gift ideas using AI.
- Get suggestions based on relationship, age, budget, and interests.
- Explore gift recommendations for different occasions and preferences.
- Simple and user-friendly web interface.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Backend:** Flask
- **Frontend:** HTML and CSS
- **AI Integration:** Google Gemini API

## 📁 Project Structure

```text
AI-Gift-Idea-Generator/
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/suppi2006/ai-gift-idea-generator.git
cd ai-gift-idea-generator
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root and add your Gemini API key using the environment variable name expected by `app.py`.

**Security:** Never upload your `.env` file or API key to GitHub.

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

http://127.0.0.1:5000/

## 🎯 Project Objective

The goal of this project is to explore generative AI integration with Python and Flask to create a practical, personalized gift recommendation application.

## 👩‍💻 Author

Developed as a Python and AI learning project.
