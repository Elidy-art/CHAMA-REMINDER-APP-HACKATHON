# Chama Payment Reminder Bot  

This is a simple web app that helps Chama groups (community savings groups) to:  
✅ Track members’ contributions  
✅ Record payments  
✅ Send mock payment reminders  

---

## 💡 Problem Solved  

Chamas often struggle to monitor payments and remind members to contribute on time. This bot provides an easy, digital solution — with clear tracking of due amounts, paid amounts, and pending balances.  

---

## ⚙ Tech Stack  

- **Python 3**  
- **Flask** (for the backend web server)  
- **SQLite** (for local database storage)  
- **Bootstrap 5** (for clean, responsive UI)  

---

## 🚀 Features  

- Add members with name, phone number, and contribution due amount  
- Display all members in a table (with paid vs pending status)  
- Record partial or full payments  
- Simulate sending reminders (mock output shown on screen + terminal)  
- Stylish UI with Bootstrap — clean tables, badges, color-coded rows  

---

## 🌐 Demo Video  

🎥 [Click here to watch the demo](https://drive.google.com/file/d/1b0ynU1yLegU7UOmEVnOcWCtbis5-4umM/view?usp=drive_link)  

---

## 📂 Project Structure  

chama-reminder-bot/
│
├── app.py # Main Flask app
├── chama.db # SQLite database (auto-generated on first run)
├── templates/
│ ├── index.html # Homepage with member table + actions
│ └── add_member.html # Add member form
└── venv/ (optional) # Virtual environment (not included in GitHub)

## ⚡ How to Run Locally  

1️⃣ Clone the repo  
git clone https://github.com/yourusername/chama-reminder-bot.git
cd chama-reminder-bot


2️⃣ Create virtual environment  
python -m venv venv

3️⃣ Activate it  
- **Windows:**  

4️⃣ Install Flask  
pip install Flask

5️⃣ Run the app  
python app.py

6️⃣ Open in browser:  
http://127.0.0.1:5000/



---

## 🌟 Future Improvements  

- Real SMS/WhatsApp integration (e.g. Twilio, Africa's Talking)  
- PDF reports for Chama records  
- M-Pesa payment integration  
- Authentication for admin access  

---

## ❤️ Credits  

Built by Elidy Muriithi for Hackathon 2025.  

---

## 💌 License  

This project is open for educational and demo purposes.  



