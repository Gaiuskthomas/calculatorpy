
📱 Glassmorphism Calculator
A sleek, modern web-based calculator built with Python (Flask) and Custom CSS. This project demonstrates the "Glassmorphism" design trend using backdrop-filter and real-time backend calculation logic.

🚀 Live Demo
You can view the live application here: [calculatorpy.onrender.com]

✨ Features
Modern UI: Frosted glass effect with soft shadows and rounded corners.

Responsive Design: Works on both desktop and mobile browsers.

Flask Backend: Math logic is processed securely on the server side.

Error Handling: Prevents crashes from invalid math operations (like dividing by zero).

🛠️ Tech Stack
Backend: Python 3, Flask

Frontend: HTML5, CSS3 (Flexbox & Glassmorphism)

Deployment: Render, Gunicorn

Version Control: Git & GitHub

📂 Project Structure
Plaintext
calculatorpy/
├── app.py           # Flask application logic
├── requirements.txt # Project dependencies
├── static/          # CSS and assets
└── templates/       # HTML files
⚙️ Local Setup
If you want to run this project on your own machine:

Clone the repository:

Bash
git clone https://github.com/Gaiuskthomas/calculatorpy.git
cd calculatorpy
Create a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Run the app:

Bash
python app.py
