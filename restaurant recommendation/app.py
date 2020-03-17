from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model1.pkl', 'rb'))
print(model)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
        s=request.form['country']
        l0=[]
        l1=[]
        l2=[]
        l3=[]
        l4=[]
        for i in model:
            if i[1]==0:
               l0.append(i[0])
            elif i[1]==1:
               l1.append(i[0])
            elif i[1]==2:
               l2.append(i[0])
            elif i[1]==3:
               l3.append(i[0])
            else:
               l4.append(i[0])
        your_list=[]
        c=""
        if s in l0:
           your_list=l0
           c="cluster1"
        elif s in l1:
           your_list=l1
           c="cluster2"
        elif s in l2:
           your_list=l2
           c="cluster3"
        elif s in l3:
           your_list=l3
           c="cluster4"
        else:
           your_list=l4
           c="cluster5"
        return render_template('index.html', your_list= your_list,c=c)
if __name__ == "__main__":
    app.run(debug=False)# -*- coding: utf-8 -*-

