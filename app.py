import pickle
from flask import Flask,request,jsonify
with open("models/best_model.pkl","rb") as f:
    model=pickle.load(f)

app=Flask(__name__)
@app.route("/predict",methods=["POST"])
def predict():
    features=request.get_json()
    if features is None:
        return jsonify({"error":"no input data"}),400
    try:
           preds=model.predict(features)
           return jsonify({"predictions":preds.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


