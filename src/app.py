from pickle import load
import streamlit as st

model = load(open('src/random-forest-diabetes.pkl', 'rb'))

class_dict = {'0': 'You are not diabetic',
              '1': 'You are diabetic'}

st.title('Diabetes - Model prediction')
st.markdown("""Power by: [Ineta Keryte]()""")
st.divider()

val1 = st.slider('Pregnancies', min_value=1, max_value=17, step=1)
val2 = st.slider('Glucose', min_value=30, max_value=200, step=20)
val3 = st.slider('Blood Pressure', min_value=20, max_value=120, step=10)
val4 = st.slider('Skin Thickness', min_value=0, max_value=60, step=5)
val5 = st.slider('Insulin', min_value=0, max_value=1000, step=20)
val6 = st.slider('BMI', min_value=0, max_value=70, step=5)
val7 = st.slider('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, step=0.1)
val8 = st.slider('Age', min_value=0, max_value=90, step=1)

if st.button("Predict"):
    prediction = str(model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])[0])
    pred_class = class_dict[prediction]
    st.divider()
    st.write("Prediction:", pred_class)
    st.divider()
