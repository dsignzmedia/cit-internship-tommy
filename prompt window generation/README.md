# 🪟 Smart Design Generator

The **Smart Design Generator** is a lightweight and intuitive web app that lets users generate door or window designs from plain text input. Simply describe the design — like "4-panel pvc french window with handle-2 and blue glass" — and get a visual preview instantly!

---

## 🚀 Features

- ✨ Text-to-design generator using natural language prompts
- 🧠 Keyword recognition for frame type, glass, handles, and panel count
- 📷 Real-time design image preview and download option
- 💬 Suggestions for inputs like `handle-1`, `2-panel` to guide users
- ⚡ Built with a fast Flask backend and Tailwind CSS frontend

---

## 🛠️ Tech Stack

- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Backend**: Python 3, Flask
- **Image Layering**: Pillow (PIL)
- **Deployment**: Localhost (ready for Render, Railway, etc.)

---

## 📂 Project Structure

prompt window generation/
├── app.py # Flask application entry
├── generator.py # Logic for image composition
├── requirements.txt
│
├── templates/
│ ├── index.html # Welcome page
│ └── generator.html # Main UI with input form
│
├── static/
│ ├── script.js # JS for interactivity
│ └── sample_design_images/
│     ├── frames/
│     ├── handles/
│     ├── glass/
│     └── panels/


## 🧪 Try Sample Prompts

- `2-panel wooden window with handle-1 and glass-2`
- `french window with handle-3 and 4-panel glass`
- `composite window with 3 panels, handle-2, and blue glass`

---

## ▶️ How to Run

python app.py

