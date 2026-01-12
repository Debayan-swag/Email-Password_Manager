# 🔐 Master Key Password Manager (Python)

A terminal-based password manager built using Python.  
This project focuses on improving Python skills by working with randomness, file handling, encryption, and terminal control.

> ⚠️ This project is for learning purposes only. Not intended for real-world security use.

---

## 📌 Features

- Random **Master Key** generation
- Master key visible for **5 seconds only**
- Uses **Fernet symmetric encryption**
- Stores credentials locally
- View or change stored credentials
- Custom exception for invalid master key
- Terminal auto-clear for better UX

---

## 🧠 Project Structure
``` bash
├── master_key.py
├── main.py
├── Master.key
├── fernet.key
├── DETAILS.txt
└── README.md
```
---

---

## 🚀 How It Works

1. A random master key is generated
2. The key is displayed for 5 seconds
3. User must enter the master key to:
   - Set credentials
   - View credentials
   - Change credentials
4. Credentials are stored in `DETAILS.txt`
5. Invalid access raises a custom exception

---

## ▶️ How to Run

### Install dependencies
```bash
pip install cryptography
```
### 🔎 Run the program
``` bash
python main.py
```