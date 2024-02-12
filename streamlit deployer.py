
import pickle
import streamlit as st


pickle_in = open("G:\DS\Projects\dts.pkl","rb")
classifier=pickle.load(pickle_in)


def predict_fraudulency(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28):
     prediction=classifier.predict([[V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28]])
     print(prediction)
     return prediction





def main():
    st.title("Credit Card Fraudulency Predictor")
    V1 = st.text_input("V1","")
    V2 = st.text_input("V2","")
    V3 = st.text_input("V3","")
    V4 = st.text_input("V4","")
    V5 = st.text_input("V5","")
    V6 = st.text_input("V6","")
    V7 = st.text_input("V7","")
    V8 = st.text_input("V8","")
    V9 = st.text_input("V9","")
    V10 = st.text_input("V10","")
    V11 = st.text_input("V11","")
    V12 = st.text_input("V12","")
    V13 = st.text_input("V13","")
    V14 = st.text_input("V14","")
    V15 = st.text_input("V15","")
    V16 = st.text_input("V16","")
    V17 = st.text_input("V17","")
    V18 = st.text_input("V18","")
    V19 = st.text_input("V19","")
    V20 = st.text_input("V20","")
    V21 = st.text_input("V21","")
    V22 = st.text_input("V22","")
    V23 = st.text_input("V23","")
    V24 = st.text_input("V24","")
    V25 = st.text_input("V25","")
    V26 = st.text_input("V26","")
    V27 = st.text_input("V27","")
    V28 = st.text_input("V28","")
    result=""
    if st.button("Predict"):
        result=predict_fraudulency(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28)
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()