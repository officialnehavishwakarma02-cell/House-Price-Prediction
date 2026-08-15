import streamlit as st
import pickle
import pandas as pd
model=pickle.load(open("model2.pkl","rb"))
MSZoning=st.selectbox('enter MSZoning',('RL','RM','FV'))
Neighborhood=st.selectbox('enter Neighborhood',
    ('Veenker','CollgCr','Crawfor','NoRidge','Gilbert','NWAmes','Crawfor','Edwards'))
SaleCondition=st.selectbox('enter SaleCondition',('Normal','Abnorml'))
BldgType=st.selectbox("enter BldgType",('1Fam','Duplex','TwnhsE'))
BsmtQual=st.selectbox("enter BsmtQual",('TA','Gd'))
Foundation=st.selectbox("enter Foundation",('CBlock','PConc','BrkTil','Stone'))
GarageCond=st.selectbox("enter GarageCond",('TA','None'))
KitchenQual=st.selectbox("enter KitchenQual",('TA','Gd','Ex'))
HeatingQC=st.selectbox("enter HeatingQC",('EX','Gd','TA'))
ExterQual=st.selectbox("enter ExterQual",('TA','Gd','EX'))
RoofStyle=st.selectbox("enter RoofStyle",('Gable','Hip'))
RoofMatl=st.selectbox("enter RoofMatl",('CompShg','None'))
LotConfig=st.selectbox('enter LotConfig',('FR2','Inside','Corner'))
GarageFinish=st.selectbox("enter GarageFinish",('RFn','Unf','Fin','None'))
LotArea=st.number_input("enter LotArea",step=1)
GrLivArea=st.number_input("enter GrLivArea",step=1)
YearBuilt=st.number_input("enter YearBuilt",step=1)
OverallCond=st.number_input("enter OverallCond",step=1)
TotalBsmtSF=st.number_input("enter TotalBsmtSF",step=1)
BsmtFullBath=st.number_input("enter BsmtFullBath",step=1)
FullBath=st.number_input("enter FullBath",step=1)
HalfBath=st.number_input("enter HalfBath",step=1)
GarageArea=st.number_input("enter GarageArea",step=1)
TotRmsAbvGrd=st.number_input("enter TotRmsAbvGrd",step=1)
GarageCars=st.number_input("enter GarageCars",step=1)
SalePrice=st.number_input("enter SalePrice",step=1)
if st.button("predict_OverallQual"):
     features=features = pd.DataFrame([{
          'MSZoning':MSZoning,
          'Neighborhood':Neighborhood,
          'SaleCondition':SaleCondition,
          'BldgType':BldgType,
          'BsmtQual':BsmtQual,
          'Foundation':Foundation,
          'GarageCond':GarageCond,
          'KitchenQual':KitchenQual,
          'HeatingQC':HeatingQC,
          'ExterQual':ExterQual,
          'RoofStyle':RoofStyle,
          'RoofMatl':RoofMatl,
          'LotConfig':LotConfig,
          'GarageFinish':GarageFinish,
          'LotArea':LotArea,
          'GrLivArea':GrLivArea,
          'YearBuilt':YearBuilt,
          'OverallCond':OverallCond,
          'TotalBsmtSF':TotalBsmtSF,
          'BsmtFullBath':BsmtFullBath,
          'FullBath':FullBath,
          'HalfBath':HalfBath,
          'GarageArea':GarageArea,
          'TotRmsAbvGrd':TotRmsAbvGrd,
          'GarageCars':GarageCars,
          'SalePrice':SalePrice
     }])
     prediction=model.predict(features)
     st.success(f"predicted OverallQual:{prediction[0]}")

        
