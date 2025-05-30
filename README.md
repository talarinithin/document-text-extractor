# 📄 Document Text Extractor

Extract text from images, PDFs, or text files with ease!  
A simple, fast web app using **React** (frontend) + **Flask** (backend) + **Tesseract OCR** 🖼️📜

---

## 🚀 Features

- 📁 Upload images, PDFs, or text files  
- 🧾 Extract text using OCR (Tesseract) & PDF rendering  
- ⚡️ Responsive React UI with separate Upload & Extract buttons  
- 🔄 Smooth communication between frontend & backend  
- 🛡️ Error handling & loading indicators for better UX  

---

## 🛠️ Prerequisites

Make sure you have installed and configured:

- 🐍 Python 3.7+  
- 🟢 Node.js 16+  
- 📝 Tesseract OCR  
- 📄 Poppler (for PDF processing)  

_Add Tesseract and Poppler executables to your system PATH!_

---

## ⚙️ Setup Instructions

### Backend (Flask) 🐍

1. Create and activate virtual environment:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
Install dependencies:

bash
Copy code
pip install flask flask-cors pytesseract pillow pdf2image
Update paths in app.py:

python
Copy code
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
POPPLER_PATH = r'C:\Program Files\poppler\poppler-24.08.0\Library\bin'
Run backend server:

bash
Copy code
python app.py
Frontend (React + Vite) ⚛️
Navigate to frontend folder:

bash
Copy code
cd frontend/my-react-app
Install dependencies:

bash
Copy code
npm install
Run frontend dev server:

bash
Copy code
npm run dev
🎉 Usage
Open your browser at http://localhost:5173

Choose a file with Upload File button

Click Upload File (local upload)

Click Extract Text to extract text from file

View extracted text below

🐙 How to Push to GitHub (Step by Step)
Create a new GitHub repository:

Go to GitHub

Click New repository

Name it e.g. document-text-extractor

Choose Public or Private

Click Create repository

Initialize local git repo (if not already):

bash
Copy code
cd your-project-folder
git init
Add remote origin:

bash
Copy code
git remote add origin https://github.com/talarinithin/document-text-extractor.git
Add all files and commit:

bash
Copy code
git add .
git commit -m "Initial commit: Add frontend & backend code"
Push to GitHub:

bash
Copy code
git branch -M main
git push -u origin main
🎉 Your project is now on GitHub!

❤️ Thank you for using Document Text Extractor!
If you found this helpful, feel free to ⭐️ the repo on GitHub!

Made with ❤️ by Talari Nithin
