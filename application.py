from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

def load_model():
    with open("count_vectorizer.pkl", "rb") as vec_file:
        vectorizer = pickle.load(vec_file)
    with open("basic_classifier.pkl", "rb") as clf_file:
        classifier = pickle.load(clf_file)
    return vectorizer, classifier

vectorizer, classifier = load_model()


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')

    # Vectorize the text using the preloaded vectorizer
    transformed_text = vectorizer.transform([text])

    # Use the classifier to make a prediction
    prediction = classifier.predict(transformed_text)[0]

    # Map the string output to integer
    label_map = {'FAKE': 1, 'REAL': 0}
    int_prediction = label_map.get(prediction, -1) 

    # Return the result as JSON
    return jsonify({'prediction': int_prediction})

if __name__ == '__main__':
    app.run(debug=True)
