# HNG Stage 0 – Profile Endpoint API

This repository contains my submission for the HNG Stage 0 backend task. It exposes a `/me` endpoint built with FastAPI that returns my profile details and a live cat fact from the Cat Facts API.

---

## 🚀 Overview

This API exposes a single endpoint `/me` which returns:

* My **email**, **full name**, and **backend stack**
* A **live cat fact** from `https://catfact.ninja/fact`
* A **dynamic UTC timestamp** in ISO 8601 format
* A **status** flag that is always `success`

---

## 📂 Project Structure

```
.
├── main.py          # FastAPI entrypoint
├── utils.py         # Helper for fetching cat facts
├── requirements.txt # Dependencies
```

---

## ✅ Features

* FastAPI-based lightweight backend
* Dynamic timestamp (updates every request)
* Live Cat Fact API integration
* Graceful fallback if external API fails
* Clean JSON response matching HNG spec

---

## 🌍 Deployment
Deployed to Railway at :
```
https://your-app.up.railway.app/me
```
---

## 📦 Installation & Setup

```bash
# Clone repo
git clone <your-repo-url>
cd <project-folder>

# Install dependencies
pip install -r requirements.txt

# Run locally
uvicorn main:app --reload
```

Access at → [http://localhost:8000/me](http://localhost:8000/me)

---

## 📡 API Response Example

```json
{
  "status": "success",
  "user": {
    "email": "example@example.com",
    "name": "John Doe",
    "stack": "C#, Python, Node.js"
  },
  "timestamp": "2025-10-15T12:34:56.789Z",
  "fact": "Cats sleep 70% of their lives."
}
```

---

## 🧪 Test It Quickly

Open in browser or use using the deployed url:

```bash
curl https://your-app.up.railway.app/me
```

---

## 🛠 Tech Stack

* **FastAPI** (Python)
* **httpx** — async external call
* **Uvicorn** — server

---

## 👨‍💻 Author

- **Fabian Muoghalu**
- Email: `fabbenco97@gmail.com`

---

## ✅ Checklist

* [ ] /me returns 200 OK
* [ ] Matches exact JSON format
* [ ] Timestamp is ISO 8601 & dynamic
* [ ] Cat fact fetched live
* [ ] Deployed and accessible publicly ✅

---
