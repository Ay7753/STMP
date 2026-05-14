# SMTP Email Automation Project

An SMTP-based Email Automation System built using Python.  
This project enables secure and automated email sending functionality using SMTP services.

---

## 🚀 Features

- Automated Email Sending
- Secure SMTP Configuration
- Real-time Email Delivery
- API-based Backend Integration
- Dynamic Email Handling

---

## 🛠 Tech Stack

- Python
- FastAPI
- SMTP
- Email Automation
- Uvicorn

---

## 📂 Project Structure

```bash
STMP/
│── api/
│   └── main.py
│── services/
│   └── email_service.py
│── pyproject.toml
│── config.toml
│── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Ay7753/STMP.git
```

Move into the project folder:

```bash
cd STMP
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn api.main:app --reload
```

---

## 📧 SMTP Configuration

Create a `.env` file and add:

```env
EMAIL=your_email@gmail.com
PASSWORD=your_app_password
```

---

## ▶️ API Endpoint

Example endpoint:

```bash
POST /send-email
```

---

## 📌 Learning Outcomes

- SMTP Integration
- Email Automation
- Backend API Development
- FastAPI Basics
- Secure Credential Handling

---

## 👨‍💻 Author

Ayush Kumar

GitHub: https://github.com/Ay7753
