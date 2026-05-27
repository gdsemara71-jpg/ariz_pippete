from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name', '')
    email = data.get('email', '')
    message = data.get('message', '')
    # In production, send email or save to database
    print(f"New message from {name} ({email}): {message}")
    return jsonify({'success': True, 'message': 'Pesan berhasil dikirim!'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
