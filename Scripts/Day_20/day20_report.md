## Technical Summary

Today, I transitioned from building ML models to deploying them as a production-ready service.

I created an end-to-end Pipeline using sklearn.pipeline.Pipeline, which combines StandardScaler and RandomForestRegressor. This ensures that any incoming data is processed consistently before prediction, eliminating the risk of data leakage.

I then serialized the trained pipeline using joblib, saving it as a .pkl file. This file acts as the "brain" of the application.

To make the model usable in real-world scenarios, I built a Flask API with a /predict endpoint that accepts JSON input, processes it through the pipeline, and returns predictions in real-time.

Finally, I tested the API using a separate Python script that sends POST requests and successfully receives predictions.

## The "Bug" Log

While testing the API, I encountered a ConnectionRefusedError, which occurred because the Flask server was not running when the test script was executed.

I resolved this by ensuring the correct execution order:

Train and save the model
Start the Flask server (app.py)
Run the test script (test_api.py) in a separate terminal

I also encountered a 404 Not Found error in the browser. This was due to accessing the root (/) endpoint, which was not defined. I fixed this by adding a simple home route to confirm the API is running.

## Conceptual Reflection

Saving a complete Pipeline instead of separate scaler and model objects ensures consistency in preprocessing and prediction.

If we saved them separately, there is a risk of:

forgetting to scale input data
applying incorrect transformations
introducing data mismatch errors

By bundling everything into one pipeline, we guarantee that the exact same transformations used during training are applied during inference, making the system reliable and production-ready.

## Key Takeaways
Machine learning models must be deployed to be useful in real-world applications.
Pipelines ensure consistent preprocessing and prevent data leakage.
Serialization (using joblib) allows models to be reused without retraining.
Flask APIs enable real-time interaction with ML models via HTTP requests.
Proper execution flow is critical when working with APIs (server must run before requests).
POST requests are required for sending structured data like JSON to ML models.