import streamlit as st
import pickle
import numpy as np
import sklearn
model=pickle.load(open('logmodel.pkl','rb')) 

def predict_baby(M,F,MY,CN):
    input=np.array([[M,F,MY,CN]]).astype(np.float64)
    prediction=model.predict(input)
    #pred='{0:.{1}f}'.format(prediction[0][0], 2)
    pred = float(np.asarray(prediction))
    #st.write(prediction)
    #st.write(pred)
    act_pre = int(pred)
    #st.write(act_pre)
    return act_pre
    


def main():
    st.title("BABY'S GENDER PREDICTION")

    html_temp = """ <p>&copy; sharad ingle</p> """
    #st.markdown("")

    st.markdown(html_temp, unsafe_allow_html=True)
    
    M = st.slider("male age", min_value=18 , max_value=45, value=21 )
    F = st.slider("female age", min_value=18 , max_value=45, value=21 )
    MY = st.slider("years of marriage", min_value=0 , max_value=15, value=0 )
    CN = st.radio("number of child",["1","2","3"], index=0 )
    
   
    if st.checkbox("you accept this is for entertainment only", value = False):
        st.write("Thank you for your consideration")
        if st.button("Predict"):
            output=predict_baby(M,F,MY,CN)
       
        
            if output == 0:
                st.title( "GIRL :girl:")
                st.balloons()
            else:
                st.title( "BOY :boy:")
                st.balloons()

       
if __name__=='__main__':
  
    main()
