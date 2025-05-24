# SnapBill

A Django-based application for splitting bills from receipt images using OCR.

## Features

- Upload or take photos of receipts
- Extract text using OCR (pytesseract)
- Parse items and prices
- Split bills equally or by items
- Calculate final totals per person

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Tesseract OCR:
- macOS: `brew install tesseract`
- Ubuntu: `sudo apt-get install tesseract-ocr`
- Windows: Download installer from GitHub

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## Project Structure

- `snapbill/` - Main Django project
- `receipts/` - Receipt processing app
- `static/` - Static files (CSS, JS, images)
- `templates/` - HTML templates 