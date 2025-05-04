from flask import Flask,request,render_template
import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline


application=Flask(__name__)
app=application

#Route for home page

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=="GET":
        return render_template("home.html")
    else:
      data=CustomData(
          age=request.form.get('age'),
          sex=request.form.get('sex'),
          chest_pain_type=request.form.get('chest_pain_type'),
          resting_bp_s=request.form.get('resting_bp_s'),
          cholesterol=request.form.get('cholesterol'),
          fasting_blood_sugar=request.form.get('fasting_blood_sugar'),
          resting_ecg=request.form.get('resting_ecg'),
          max_heart_rate=request.form.get('max_heart_rate'),
          exercise_angina=request.form.get('exercise_angina'),
          oldpeak=request.form.get('oldpeak'),
          ST_slope=request.form.get('ST_slope'),
      )
      pred_df=data.get_data_as_data_frame()
      print(pred_df)

      predict_pipeline=PredictPipeline()
      results=predict_pipeline.predict(pred_df)
      return render_template('home.html',results=results[0])
    
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)