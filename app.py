import streamlit as st
import pickle
import pandas as pd
import numpy as np
model=pickle.load(open("model.pkl","rb"))
st.title("salePrice Prediction")
GarageType=st.selectbox('enter GarageType',
   ( 'Attchd','Detchd'
))
Neighborhood=st.selectbox('enter Neighborhood',
    ('Veenker','CollgCr','Crawfor','NoRidge','Gilbert','NWAmes','Crawfor','Edwards'
))
MSZoning=st.selectbox('enter MSZoning',
    ('RL','RM','FV'
))
LotConfig=st.selectbox('enter LotConfig',
    ('FR2','Inside','Corner'
))
GarageQual=st.selectbox('enter GarageQual',
    ('TA','Fa','None'
    ))
YrSold=st.number_input("enter YrSold",step=1)
MoSold=st.number_input("enter MoSold",step=1)
YearBuilt=st.number_input("enter YearBuilt",step=1)
OverallQual=st.number_input("enter OverallQual",step=1)
GrLivArea=st.number_input("enter GrLivArea",step=1)
TotalBsmtSF=st.number_input("enter TotalBsmtSF",step=1)
BsmtFullBath=st.number_input("enter BsmtFullBath",step=1)
BsmtHalfBath=st.number_input("enter BsmtHalfBath",step=1)
YearRemodAdd=st.number_input("enter YearRemoAdd",step=1)
GarageArea=st.number_input("enter GarageArea",step=1)
if st.button("predict_price"):
    features=features = pd.DataFrame([{
    "YrSold": YrSold,
    "MoSold": MoSold,
    "YearBuilt": YearBuilt,
    "OverallQual": OverallQual,
    "GrLivArea": GrLivArea,
    "TotalBsmtSF": TotalBsmtSF,
    "BsmtHalfBath": BsmtHalfBath,
    "YearRemodAdd": YearRemodAdd,
    "GarageArea": GarageArea,
    "GarageType": GarageType,
    "Neighborhood": Neighborhood,
    "MSZoning": MSZoning,
    "LotConfig": LotConfig,
    "GarageQual": GarageQual,
    "BsmtFullBath": BsmtFullBath
}])
    prediction=model.predict(features)
    prediction=np.expm1(prediction)
    st.success(f"predicted sale price:{prediction[0]:,.2f}")
                             
