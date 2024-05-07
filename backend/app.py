from flask import Flask,request
from models.Prediction import Prediction
# from flask_cors import CORS

app = Flask(__name__)

# enable CORS
# CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/prediction",methods=['POST'])
def predict():
   try:
      
      content_type = request.headers.get('Content-Type')
      if content_type == 'application/json':
         json = request.json
         prediction = Prediction(
            json['marca'],
            json['inches'],
            json['cpu'],
            json['ram'],
            json['gpu'],
            json['so'],
            json['ssd']
         )
         return {"status":200,"value": str(prediction.do_prediction())}
      
      return {"status":500,"value":'content type Error'}
   
   except KeyError:
      return {"status":500,"value":'Missing parameter'}
   except:
      return {"status":500,"value":'Error'}
      
if __name__ == '__main__':
    app.run()