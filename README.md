# SnapBill - Smart Receipt Scanner & Bill Splitter

SnapBill is a Django-based application that makes splitting bills from receipts effortless. Simply snap a photo of your receipt, and SnapBill will automatically read the items and prices using OCR (Optical Character Recognition), then help you split the bill among friends.

## Core Features

- 📸 **Smart Receipt Scanning**: Take a photo or upload a receipt image
- 🔍 **Automatic OCR**: Extract text, items, and prices using pytesseract
- 💰 **Smart Bill Splitting**: Split bills equally or by specific items
- 📱 **Mobile-Friendly**: Works great on both desktop and mobile devices

## Tech Stack

- **Backend**: Django 5.0.2
- **OCR Engine**: pytesseract
- **Image Processing**: Pillow (PIL)
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Bootstrap 5

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ByteWizard750/SnapBill.git
cd SnapBill
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Tesseract OCR:
- macOS: `brew install tesseract`
- Ubuntu: `sudo apt-get install tesseract-ocr`
- Windows: Download installer from GitHub

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000` in your browser

## How It Works

1. **Snap**: Take a photo of your receipt or upload an image
2. **Scan**: SnapBill automatically reads the text using OCR
3. **Parse**: The system identifies items and their prices
4. **Split**: Choose how to split the bill:
   - Split equally among all people
   - Split by specific items
   - Custom split with different amounts

## Project Structure

- `snapbill/` - Main Django project
- `receipts/` - Receipt processing app
  - `ocr.py` - OCR and text processing
  - `parser.py` - Receipt parsing logic
  - `splitter.py` - Bill splitting algorithms
- `static/` - Static files (CSS, JS, images)
- `templates/` - HTML templates

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- Rohan (ByteWizard750)

## Acknowledgments

- Tesseract OCR
- Django Documentation
- Bootstrap Documentation 