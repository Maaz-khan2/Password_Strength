import re
import streamlit as st

# page styling
st.set_page_config(page_title='Password Strength Checker' , page_icon='🔑' , layout='centered')

# custom css
st.markdown(
  """
  <style>
    .main{text-align:center;}
    .stTextInput{width: 30vh , }
  </style>
  """ , unsafe_allow_html=True
)

# page title and description

st.title('🔐Password Strength Generator')
st.write('Enter your Password belo to check the secuirty level.')


# Function password
def check_password_strength(Password):
    score = 0,
    feedback = []

    if len(Password) >= 8:
        score += 1 
    else:
        feedback.append('Password Must be 8 Character')     

    
    if re.search(r'[A-Z]' , Password) and re.search(r'[a-z]' , Password):
        score += 1
    else:
        feedback.append('❌Password should include **both uper case [A-Z] and lower case[a-z]**.')



    if re.search(r'/d' , Password): 
        score += 1
    else:
        feedback.append('❌Password should include **at least onr number[0-9]**.')    


    if re.search(r'[!@#$%^&*]' , Password):
        score += 1    
    else:
        feedback.append('❌Password should include **at least one speacial character(!@#$%^&*)**.')    


    #  display password strength
    
    if score == 5:
       st.success('**Strong password**your password is secure')
    elif score == 4:
        st.info('**Strong password**your password is secure')   
    else:
        st.error('❌**Week Password** Follow the suggestion below to strength it.') 

    #  feedback
     
    if feedback:
        with st.expander('Improve your password'):   
             for item in feedback:
                 st.write(item)

Password = st.text_input('Enter your Password' , type='password' , help='Ensure your Password is strong')


# check password
if st.button('Check Password'):
   if Password:
         check_password_strength(Password)
   else:
       st.warning('Please Enter a Password first!')     
