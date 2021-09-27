import os
from flask import Flask, jsonify, request
from transformers import pipeline

app = Flask(__name__)

model_path = "./model"

@app.route('/run')
def classify():
  # Your function
  # classify = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
  
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google Cloud
    # Run, a webserver process such as Gunicorn will serve the app.
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
