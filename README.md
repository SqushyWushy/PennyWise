PennyWise API 🪙

🚀 About

The PennyWise API is a Python Flask-based application designed to provide financial advice by breaking down your paycheck into the 50/30/20 rule:
	•	50% for necessities
	•	30% for discretionary spending
	•	20% for savings.

Additionally, the API calculates projected savings with a 5% annual interest rate and offers motivational financial quotes to inspire better money management.

🛠 Features
	•	Paycheck Breakdown: Calculates how to allocate your paycheck using the 50/30/20 rule.
	•	Savings Projection: Projects your potential savings growth with a 5% annual interest rate.
	•	Motivational Quotes: Delivers random financial wisdom to encourage smart spending habits.

🧑‍💻 How to Use

1. Clone the Repository

git clone https://github.com/SqushyWushy/PennyWise.git
cd PennyWise

2. Install Dependencies

Make sure you have Python installed. Then, install Flask:

pip install flask

3. Run the Application

Start the Flask server:

python pennywise_api.py

The app will run on http://127.0.0.1:5000.

📡 API Endpoints

POST /advise

Get financial advice based on your paycheck.

Request
	•	URL: http://127.0.0.1:5000/advise
	•	Method: POST
	•	Body (JSON):

{
    "paycheck": 2500
}



Response
	•	Status: 200 OK
	•	Example:

{
    "paycheck": "$2500.00",
    "advice": {
        "necessities": "$1250.00 (50%)",
        "discretionary": "$750.00 (30%)",
        "savings": "$500.00 (20%)"
    },
    "savings_projection": "Save $500.00/paycheck, and you'll have approximately $13291.86 in 1 year (5% annual interest).",
    "note": "Stick to the 50/30/20 rule to build a balanced and sustainable financial future."
}

GET /motivate

Get a random financial motivational quote.

Request
	•	URL: http://127.0.0.1:5000/motivate
	•	Method: GET

Response
	•	Status: 200 OK
	•	Example:

{
    "quote": "Beware of little expenses. A small leak will sink a great ship. - Benjamin Franklin"
}

🔍 How It Works
	1.	Users send their paycheck amount to the /advise endpoint.
	2.	The API breaks the paycheck into the 50/30/20 categories and calculates a savings projection.
	3.	Users can also retrieve a random motivational quote from the /motivate endpoint.

📚 Learning Goals

This project was built to:
	•	Learn and practice Python and Flask for building REST APIs.
	•	Implement financial calculations and JSON data validation.
	•	Deliver meaningful financial insights in a fun, interactive way.

🛠 Future Improvements
	•	Add support for custom savings rates and custom financial rules.
	•	Integrate a frontend interface for ease of use.
	•	Implement multi-user accounts and saving tracking.

🔗 Useful Links
	•	Flask Documentation - https://flask.palletsprojects.com/
	•	Postman - https://www.postman.com/
	•	GitHub - https://github.com/SqushyWushy/PennyWise

📩 Contact

Created by Hector Gonzalez
Feel free to reach out for collaboration or questions at jhgonzalez.tx@gmail.com!