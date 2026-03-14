# OCR Web App (Flask + Tesseract)

This is a simple OCR website built with **Flask** (Python) and **Tesseract OCR**.

## Prerequisites

- Python 3.12+ installed
- Tesseract OCR installed on your machine

### Install Tesseract (Windows)

1. Install from the UB Mannheim build:
   - https://github.com/UB-Mannheim/tesseract/wiki
2. After installing, open PowerShell and verify:

```powershell
tesseract --version
```

If `tesseract` is not recognized, add the install folder to your **PATH** (commonly `C:\Program Files\Tesseract-OCR\`) and restart PowerShell.

## Project Structure

```text
OCR/
  app.py
  requirements.txt
  templates/
    index.html
  static/
    style.css
```

## Setup (Windows PowerShell)

From the project folder:

```powershell
# Create virtual environment
python -m venv .venv

# Activate it
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

## Run

```powershell
python app.py
```

Then open this URL in your browser:

- http://127.0.0.1:5000/

## Notes

- If OCR accuracy is low for certain images (memes/comics), try higher-resolution images or adjust preprocessing / Tesseract settings in `app.py`.
- The browser may request `/favicon.ico` and show a 404 in the console; this is normal.
