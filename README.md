# SnapBill - Smart Receipt Management System

SnapBill is a modern web application built with Django that helps users manage their receipts digitally. Upload receipts, track expenses, split bills, and share receipts with others - all in one place!

## Features

- 📸 **Receipt Upload**: Upload receipt images and store them digitally
- 💰 **Bill Splitting**: Easily split bills among multiple people
- 🔍 **Receipt History**: View and manage all your receipts in one place
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- 🔗 **Receipt Sharing**: Share receipts with others via unique links
- 📊 **Item Tracking**: Track individual items and their prices
- 🔒 **User Authentication**: Secure login and signup system

## Tech Stack

- **Backend**: Django 5.0.2
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default)
- **Styling**: Bootstrap 5, Custom CSS
- **Icons**: Bootstrap Icons

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

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Visit `http://127.0.0.1:8000` in your browser

## Usage

1. **Sign Up/Login**: Create an account or log in to access your receipts
2. **Upload Receipt**: Use the upload button to add new receipts
3. **View Receipts**: Access your receipt history from the navigation menu
4. **Split Bills**: Select items and split the bill among multiple people
5. **Share Receipts**: Generate sharing links for any receipt
6. **Mark as Paid**: Track payment status for each receipt

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- Rohan (ByteWizard750)

## Acknowledgments

- Django Documentation
- Bootstrap Documentation
- All contributors and users of SnapBill 