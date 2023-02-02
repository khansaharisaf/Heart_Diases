import numpy as np
import streamlit as st
import pickle

# load save model
model = pickle.load(open('heart_predic.pkl', 'rb'))

# judul web (header)
st.title('Prediksi Penyakit Jantung')

# membagi atribut kedalam 3 kolom, biar gausah ada 13 kolom kebawah
#col1, col2, col3 = st.columns(3)

#with col1:
age = st.number_input('Umur')
#with col2:
sex = st.number_input('Jenis Kelamin')
#with col3:
cp = st.number_input('Jenis Nyeri Dada')
#with col1:
trestbps = st.number_input('Tekanan_Darah')
#with col2:
chol = st.number_input('Nilai Kolesterol')
#with col3:
fbs = st.number_input('Gula Darah')
#with col1:
restecg = st.number_input('Hasil Elektrokardiografi')
#with col2:
thalach = st.number_input('Detak Jantung Maksimum')
#with col3:
exang = st.number_input('Induksi Angina')
#with col1:
oldpeak = st.number_input('ST Depression')
#with col2:
slope = st.number_input('Slope')
#with col3:
ca = st.number_input('Nilai Pembuluh Darah')
#with col1:
thal = st.number_input('Nilai Thal')

#code for prediction
heart_diagnosis = ''

#membuat tombol prediksi
if st.button('Prediksi Penyakit Jantung'):
    heart_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if(heart_prediction[0]==1):
        heart_diagnosis = 'Pasien Terkena Penyakit Jantung'
    else:
        heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'
st.success(heart_diagnosis)