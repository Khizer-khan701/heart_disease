import sys
import pandas as pd 
import numpy as np 
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass 

    def predict(self,features):
        try:
            model_path="artifacts\model.pkl"
            preprocessor_path="artifacts\preprocessor.pkl"
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(self, age, sex, chest_pain_type, resting_bp_s, cholesterol,
                 fasting_blood_sugar, resting_ecg, max_heart_rate,
                 exercise_angina, oldpeak, ST_slope):
        self.age = age
        self.sex = sex
        self.chest_pain_type = chest_pain_type
        self.resting_bp_s = resting_bp_s
        self.cholesterol = cholesterol
        self.fasting_blood_sugar = fasting_blood_sugar
        self.resting_ecg = resting_ecg
        self.max_heart_rate = max_heart_rate
        self.exercise_angina = exercise_angina
        self.oldpeak = oldpeak
        self.ST_slope = ST_slope
    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict={
            'age': [self.age],
            'sex': [self.sex],
            'chest pain type': [self.chest_pain_type],  # space here
            'resting bp s': [self.resting_bp_s],        # add space if needed
            'cholesterol': [self.cholesterol],
            'fasting blood sugar': [self.fasting_blood_sugar],
            'resting ecg': [self.resting_ecg],
            'max heart rate': [self.max_heart_rate],
            'exercise angina': [self.exercise_angina],
            'oldpeak': [self.oldpeak],
            'ST slope': [self.ST_slope]  # space here
        }

            return  pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomData(e,sys)