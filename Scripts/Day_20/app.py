from flask import Flask, request, jsonify
import joblib
import pandas as pd
app = Flask(__name__)
# 1. Load the pre-trained pipeline
model = joblib.load('production_model.pkl')
@app.route('/predict', methods=['POST'])
@app.route('/')
def home():
    return "Helloooo API is running!"
def predict():
 # 2. Get data from the POST request
 data = request.get_json()
# 3. Convert JSON to DataFrame
 query_df = pd.DataFrame([data])

 # 4. Predict using the pipeline (it will scale the data automatically!)
 prediction = model.predict(query_df)

 # 5. Return result as JSON
 return jsonify({'prediction': list(prediction)})
if __name__ == '__main__':
 app.run(port=5000, debug=True)

