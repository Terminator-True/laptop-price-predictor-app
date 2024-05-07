from flask import Flask
import models.Prediction
# from flask_cors import CORS

app = Flask(__name__)

# enable CORS
# CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/prediction",methods=['POST'])
def predict():
   pass



if __name__ == '__main__':
    app.run()