import streamlit as st
import pickle
import numpy as np
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
    st.markdown("this is for entertainment only")

    st.markdown(html_temp, unsafe_allow_html=True)
    
    M = st.text_input("male age","")
    F = st.text_input("female age","")
    MY = st.text_input("years of marriage","")
    CN = st.text_input("number of child 1st or 2nd","")
    
    zero_html="""  
      <div style="background-color:#71F50A;padding:30px >
       <h1 style="color:white;text-align:center;"> its a girl</h1>
       &#x1F467; 
       </div>
    """
    one_html="""  
      <div style="background-color:#0AF5E6;padding:30px >
       <h1 style="color:white;text-align:center;"> its a boy</h1>
       &#128102;
       </div>
    """
   
    
    if st.button("Predict"):
        output=predict_baby(M,F,MY,CN)
       
        
        if output == 0:
            st.title( "GIRL")
            st.markdown(zero_html,unsafe_allow_html=True)
        else:
            st.title( "BOY")
            st.markdown(one_html,unsafe_allow_html=True)

       
if __name__=='__main__':
  
    main()