from flask import Flask, request, jsonify
import joblib
import os
import numpy as np

app = Flask(__name__)

print("Loading models...")
model = joblib.load('models/model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')
print("Models loaded.")

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'status': 'healthy'}), 200

@app.route('/invocations', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data.get('text', [])
        if isinstance(text, str):
            text = [text]
        features = vectorizer.transform(text)
        predictions = model.predict(features)
        return jsonify({'predictions': predictions.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)