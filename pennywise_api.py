from flask import Flask, request, jsonify
from collections import OrderedDict
import random

app = Flask(__name__)

# Custom JSON provider to handle OrderedDict
class CustomJSONProvider:
    def dumps(self, obj, **kwargs):
        if isinstance(obj, OrderedDict):
            obj = dict(obj)
        return jsonify(obj).data.decode("utf-8")

app.json_provider_class = CustomJSONProvider

# Motivational quotes
quotes = [
    "Don’t spend what’s left after saving, save what’s left after spending. - Warren Buffett",
    "It’s not your salary that makes you rich, it’s your spending habits. - Charles A. Jaffe",
    "Beware of little expenses. A small leak will sink a great ship. - Benjamin Franklin",
    "Do not save what is left after spending; spend what is left after saving. - Warren Buffett"
]

def calculate_savings_projection(biweekly_savings, annual_rate=0.05, years=1):
    """
    Calculate projected savings with compound interest for biweekly savings.
    """
    # Convert biweekly savings to monthly savings
    monthly_savings = biweekly_savings * 2.165  # Approximation for biweekly contribution
    months = years * 12
    monthly_rate = annual_rate / 12
    projection = monthly_savings * (((1 + monthly_rate) ** months) - 1) / monthly_rate
    return round(projection, 2)

@app.route('/advise', methods=['POST'])
def advise_paycheck():
    # Parse the paycheck amount from the request
    data = request.json
    if not data or "paycheck" not in data:
        return jsonify({"error": "Please provide a paycheck amount."}), 400

    paycheck = data["paycheck"]

    if not isinstance(paycheck, (int, float)) or paycheck <= 0:
        return jsonify({"error": "Paycheck must be a positive number."}), 400

    # Apply the 50/30/20 Rule
    necessities = paycheck * 0.50
    discretionary = paycheck * 0.30
    savings = paycheck * 0.20

    # Calculate savings projection for biweekly paychecks
    projected_savings = calculate_savings_projection(savings)

    # Build the response using OrderedDict for consistent order
    response = OrderedDict()
    response["paycheck"] = f"${paycheck:.2f}"
    response["advice"] = OrderedDict([
        ("necessities", f"${necessities:.2f} (50%)"),
        ("discretionary", f"${discretionary:.2f} (30%)"),
        ("savings", f"${savings:.2f} (20%)")
    ])
    response["savings_projection"] = f"Save ${savings:.2f}/paycheck, and you'll have approximately ${projected_savings} in 1 year (5% annual interest)."
    response["note"] = "Stick to the 50/30/20 rule to build a balanced and sustainable financial future."

    return jsonify(response), 200


@app.route('/motivate', methods=['GET'])
def get_motivation():
    # Return a random motivational quote
    quote = random.choice(quotes)
    return jsonify({"quote": quote}), 200


if __name__ == '__main__':
    app.run(debug=True)