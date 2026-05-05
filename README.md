# BCS601-4MW23CS119 – Cloud Visitor Counter

## Project Title
Cloud Visitor Counter Application

## Description
This project is developed as part of Cloud Computing Lab (BCS601).
It is a simple web-based application that counts the number of visitors accessing the webpage.
The visit count is stored in a SQLite database and updated dynamically whenever the page is refreshed.

## Technologies Used
- Python
- Flask Framework
- SQLite Database
- GitHub
- Render Cloud Platform

## Deployment URL
https://bcs601-4mw23cs119.onrender.com

## How It Works
1. When a user visits the webpage, the application connects to the SQLite database.
2. The visit count is incremented by 1.
3. The updated count is displayed on the webpage.

## Project Structure
bcs601_4mw23cs119/
│
├── app.py
├── requirements.txt
├── visitors.db
├── templates/
│   └── index.html
└── README.md

## Steps to Run Locally

1. Clone the repository:
   git clone https://github.com/reynol-31/bcs601_4mw23cs119.git

2. Navigate to project folder:
   cd bcs601_4mw23cs119

3. Install dependencies:
   pip install -r requirements.txt

4. Run the application:
   python app.py

5. Open browser:
   http://127.0.0.1:5000