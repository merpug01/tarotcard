import random
from tarot_card import tarot_card 
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():

    user_input = request.form['user_input']
    user_input_lower = user_input.lower()
    

    random_number = random.randint(0, 77)
    random_card = tarot_card[random_number]
    

    response = {"card": random_card['card'], "image": random_card.get('image', 'CardBacks.jpg')}  # Default fallback for image
    if user_input_lower == 'general advice':
        response["message"] = random_card['Advice']
    elif user_input_lower == 'love':
        response["message"] = random_card['Love']
    elif user_input_lower == 'career':
        response["message"] = random_card['Career']
    elif user_input_lower == 'yes or no':
        response["message"] = random_card['Yes/No']
    else:
        response["message"] = "Invalid input. Please enter 'general advice', 'love', 'career', or 'yes or no'."
    
    return jsonify(response)
    

if __name__ == '__main__':
    app.run(debug=True)
