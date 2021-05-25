from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn
import datetime

from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index1.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        state= request.form['state']
        if(state=="West Bengal"):
            States=36;
        if(state=="Kerala"):
            States=17;
        if(state=="Punjab"):
            States=28;
        if(state=="Goa"):
            States=10;
        if(state=="Chhattisgarh"):
            States=7;
        if(state=="Chandigarh"):
            States=6;
        if(state=="Andhra Pradesh"):
            States=2;
        if(state=="Assam"):
            States=4;
        if(state=="Uttarakhand"):
            States=35;
        if(state=="Tamil Nadu"):
            States=31;
        if(state=="Haryana"):
            States=12;
        if(state=="Odisha"):
            States=26;
        if(state=="Karnataka"):
            States=16;
        if(state=="Uttar Pradesh"):
            States=34;
        if(state=="Jammu and Kashmir"):
            States=14;
        if(state=="Bihar"):
            States=5;
        if(state=="Madhya Pradesh"):
            States=20;
        if(state=="Nagaland"):
            States=25;
        if(state=="Maharashtra"):
            States=21;
        if(state=="Mizoram"):
            States=24;
        if(state=="Delhi"):
            States=9;
        if(state=="Rajasthan"):
            States=29;
        if(state=="Gujarat"):
            States=11;
        if(state=="Arunachal Pradesh"):
            States=3;
        if(state=="Dadar and Nagar Haveli and Daman and Diu"):
            States=8;
        if(state=="Himachal Pradesh"):
            States=13;
        if(state=="Jharkhand"):
            States=15;
        if(state=="Tripura"):
            States=33;
        if(state=="Ladakh"):
            States=18;
        if(state=="Manipur"):
            States=22;
        if(state=="Meghalaya"):
            States=22;
        if(state=="Andaman and Nicobar Islands"):
            States=1;
        if(state=="Puducherry"):
            States=27;
        if(state=="Telangana"):
            States=32;
        if(state=="Sikkim"):
            States=30;
        if(state==""):
            States=-1;
        Month=int(datetime.date.today().month)
        Year=int(datetime.date.today().year)
        DayOfWeek=int(datetime.date.today().weekday())
        Day=datetime.date.today().day
        DayOfYear=Month*30+Day
        try:
            TotalSamples=int(request.form['totalsamples'])
            prediction=model.predict([[States,TotalSamples,Year,Month,Day,DayOfWeek,DayOfYear]])
            output=int(round(prediction[0],2))+1;
        
            if States==-1:
                return render_template('index1.html',prediction_text="Please,select a state")
            if output>TotalSamples or output<0:
                return render_template('index1.html',prediction_text="Sorry, we can't predict this.")
            else:
                return render_template('index1.html',prediction_text="Total number of positive cases expected in {}: {}".format(state,output))
        except:
             return render_template('index1.html',prediction_text="Enter the total number of samples tested(without commas)")
    else:
        return render_template('index1.html')

if __name__=="__main__":
    app.run(debug=True)
