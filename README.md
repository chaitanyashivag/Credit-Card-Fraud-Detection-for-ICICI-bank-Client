# Credit Card Fraud Detection Using Machine Learning & Python

For Testing Purposes, a main dataset from Kaggle is downloaded and all the features are PCA transformed for confidentiality purposes.

# Objective 

To developed a machine learning model using Logistic Regression, Decision Trees, Random Forests, Support Vector Machines, XGBoost Classifier to predict whether a credit card transaction
is fraudulent or not.

# Prerequisites

Install following packages:

pip install numpy
pip install pandas
pip install sklearn
pip install keras
pip install seaborn

# Model Building

Following 5 models are built : 

1. Decision Tree
2. Random Forest
3. Support Vector Machine
4. Logistic Regression
5. XG Boost classifier

We will be trying different machine learning models one by one. Defining models are much easier. A single line of code can define our model. And, in the same way, a single line of code can fit the model on our data.

We can also tune these models by selecting different optimized parameters. But, if the accuracy is better even with less parameter tuning then — no need to make it complex.

# Deploying the model 

We are using streamlit for deploying our best model i.e XG Boost Classifier as it is showing maximum accuracy. We are exporting the model through pickle format

# Conclusion
We arrived at a 99.95% accuracy in our credit card fraud detection and successfully deployed it through streamlit so as to use it in realtime
