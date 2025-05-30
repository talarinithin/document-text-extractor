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

*Add Tesseract and Poppler executables to your system PATH!*

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
Copy
Edit
pip install flask flask-cors pytesseract pillow pdf2image
Update paths in app.py:

python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
POPPLER_PATH = r'C:\Program Files\poppler\poppler-24.08.0\Library\bin'
Run backend server:

bash
Copy
Edit
python app.py
Frontend (React + Vite) ⚛️
Navigate to frontend folder:

bash
Copy
Edit
cd frontend/my-react-app
Install dependencies:

bash
Copy
Edit
npm install
Run frontend dev server:

bash
Copy
Edit
npm run dev
🎉 Usage
Open your browser at http://localhost:5173

Choose a file with Upload File button

Click Upload File (local upload)

Click Extract Text to extract text from file

View extracted text below

🐙 How to Push to GitHub (Step by Step)
Create a new GitHub repository

Initialize local git repo (if not already):

bash
Copy
Edit
cd your-project-folder
git init
Add remote origin:

bash
Copy
Edit
git remote add origin https://github.com/talarinithin/document-text-extractor.git
Add all files and commit:

bash
Copy
Edit
git add .
git commit -m "Initial commit: Add frontend & backend code"
Push to GitHub:

bash
Copy
Edit
git branch -M main
git push -u origin main
❤️ Thank you for using Document Text Extractor!
If you found this helpful, please ⭐️ the repo on GitHub!

Made with ❤️ by Talari Nithin
