import re
import warnings

import numpy as np
import pandas as pd
import pyttsx3
from flask import Flask, render_template, request
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, _tree

warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Add the code for symptom prediction and disease information here
    # Retrieve the user-entered symptoms from the form
    symptoms = request.form.get('symptoms')
    # Perform the necessary prediction and display the results

    return render_template('result.html', symptoms=symptoms, predicted_disease=predicted_disease)
