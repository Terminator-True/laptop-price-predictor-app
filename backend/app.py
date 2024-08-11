from flask import Flask,request, jsonify
from models.Prediction import Prediction
from flask_cors import CORS
import json

app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/prediction",methods=['POST'])
def predict():
   try:
      
      # content_type = request.headers.get('Content-Type')
      # if content_type == 'application/json':
      data = json.loads(request.data)
      print(data)
      prediction = Prediction(
         data['marca'],
         data['inches'],
         data['cpu'],
         data['ram'],
         data['gpu'],
         data['so'],
         data['ssd']
      )
      return jsonify({"status":200,"value": str(prediction.do_prediction())})
      
      return jsonify({"status":500,"value":'content type Error'})
   
   except KeyError:
      return jsonify({"status":500,"value":'Missing parameter'})
   except Exception as e:
      return jsonify({"status":500,"value":e})
      
if __name__ == '__main__':
   app.run()