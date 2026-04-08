import os
from flask import Flask, request, jsonify, send_from_directory
import stripe
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='.')

# Initialize Stripe
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

@app.route('/')
def index():
    return send_from_directory('.', 'checkout.html')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        data = request.get_json()
        price_in_cents = data.get('price', 700)  # Default to €7
        product_name = data.get('product_name', 'AI Prompt Engineering Cheat Sheet')
        
        origin = request.headers.get('Origin', 'http://localhost:5000')
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'eur',
                    'product_data': {
                        'name': product_name,
                    },
                    'unit_amount': price_in_cents,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=origin + '/success.html',
            cancel_url=origin + '/cancel.html',
        )
        
        return jsonify({'id': session.id})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/success.html')
def success():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Payment Successful</title>
    </head>
    <body>
        <h1>Thank you for your purchase!</h1>
        <p>Your AI Prompt Engineering Cheat Sheet is ready for download.</p>
        <p><a href="ai-prompt-cheatsheet" download>Download Cheat Sheet</a></p>
        <p><a href="ai-prompt-cheatsheet-sales.md">View Sales Page</a></p>
    </body>
    </html>
    '''

@app.route('/cancel.html')
def cancel():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Payment Cancelled</title>
    </head>
    <body>
        <h1>Payment Cancelled</h1>
        <p>You can try again anytime.</p>
        <a href="/">Back to Checkout</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)