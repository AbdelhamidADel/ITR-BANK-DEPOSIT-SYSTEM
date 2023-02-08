import streamlit as st
import numpy as np
from streamlit_lottie import st_lottie
import requests
import base64
from streamlit_option_menu import option_menu
from utils import *
import pickle
from PIL import Image


#------------------------configuration of page ----------------------------------
st.set_page_config(layout="centered",page_icon="favicon.ico",initial_sidebar_state="expanded",page_title="ITR-Bank System")

#------------------------SITE BACKGROUND-------------------
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('cover1.jpg')
#--------------------------SITE SIDBAR ICON--------------------------------- 
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_message = load_lottieurl(
    "https://assets5.lottiefiles.com/packages/lf20_gr9towjo.json"
)
with st.sidebar:
    st_lottie(lottie_message, height=140, width=None, key="message")
    st.markdown("<h1 style='text-align: center; color: white'>ITR-BANK DEPOSIT SYSTEM</h1>", unsafe_allow_html=True)


# ================================ NAVBAR ===========================
with st.sidebar:
    selected = option_menu(None, ["Home", 'Prediction',"Contact Us"], 
        icons=['house', 'gear','list-task'], menu_icon="cast", default_index=0,
        styles={
        "container": {"background-color": "#262730"},
        "icon": {"color": "gold", "font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#62657c"},
        "nav-link-selected": {"background-color": "#62657c"},
    }
)
st.markdown(
    f'''
        <style>
            .sidebar .sidebar-content {{
                width: 350px;
            }}
        </style>
    ''',
    unsafe_allow_html=True
)
footer_sidebar="""<div>
<p style='margin-top: 110px; text-align: center;' >Developed with ❤️ by <a style='color: gold;text-shadow: 2px 2px 4px black; text-align: center;' href="https://github.com/AbdelhamidADel" target="_blank">Abdelhamid Adel</a></p>
</div>
"""
st.sidebar.markdown(footer_sidebar,unsafe_allow_html=True)
# ---------------------------Home Page-----------------------------
if selected =='Home':
    page="""<style>
    body {color: #262730;
    text-shadow: 2px 2px 8px black;
    font-weight: bold;}
    </style>"""
    st.markdown(page,unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: gold;'>W  e  l  c  o  m  e<br/>to<br/>ITR-BANK DEPOSIT SYSTEM</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; color: gold;'>What is ITR-Bank Deposit System ?</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold;'>It is a system that was created to predict if a specific customer will deposit in the bank, by means of some data that is entered into a model that was developed using machine learning.</p>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; color: gold;'>What are Bank Deposits ?</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>Bank deposits are a savings product that customers can use to hold an amount of money at a bank for a specified length of time. In return, the financial institution will pay the customer the relevant amount of interest, based on how much they choose to deposit and for how long.Once the agreed term has elapsed, the bank will return the amount deposited plus the interest to have accrued over that period at the agreed rate.</p>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left; color: gold;'>What Kind of Needed Data to Use ITR-Bank Model ?</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>Age : Client Age </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>Job : Client Job </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>marital status : divorced, married, single, unknown </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>Education : primary, secondary, tertiary and unknown </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>Default : has credit in default? (no, yes) </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>Housing: has housing loan? (no, yes) </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>Loan: has Personal loan? (no, yes) </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>Balance: Balance of the individual </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>Contact: contact communication type (cellular, telephone) </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>Month: last contact month of year (jan, feb, mar, ..., nov, dec) </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>Day: last contact day of the month (1,2,3,....29,30) </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>Duration: last contact duration, in seconds </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>Campaign: number of contacts performed during this campaign and for this client </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>Pdays: number of days that passed by after the client was last contacted from a previous campaign </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>Previous: number of contacts performed before this campaign and for this client </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold; '>Poutcome: outcome of the previous marketing campaign (failure, nonexistent, success) </p>", unsafe_allow_html=True)


# ---------------------------Prediction Page-----------------------------
#age--balance--day--duration--campaign--pdays--previous--job_enc--marital_enc--education_enc--default_enc--housing_enc--loan_enc--contact_enc--month_enc--poutcome_enc
if selected =='Prediction':
     # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/pred_botton.css")

    page="""<style>
    body {color: #262730;
    text-shadow: 2px 2px 8px black;
    font-weight: bold;}
    </style>"""
    st.markdown(page,unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: gold;'>Prediction</h2>", unsafe_allow_html=True)
    try:
        # ---------------------------------user input---------------------------------------
        with st.form('Form2'):
            age=st.slider('Age', 1, 100)
            balance= st.number_input('Insert client balance')
            day=st.number_input('choose a day', min_value=1, max_value=31,step=1)
            duration= st.number_input('Insert duration in seconds')
            campaign=st.slider('campaign', 1, 100)
            pdays = st.text_input(label='pdays',value=0)
            Previous=st.slider('Previous', 0, 100)
            job=st.selectbox(
            'choose client job',
            ('admin', 'technician', 'services', 'management', 'retired',
        'blue-collar', 'unemployed', 'entrepreneur', 'housemaid',
        'unknown', 'self-employed', 'student'))
            marital=st.selectbox(
            'choose client marital status',
            ( 'married', 'single', 'divorced'))
            education=st.selectbox(
            'choose client Education',('primary', 'secondary', 'tertiary' , 'unknown'))
            default=st.selectbox('has credit in default?',('yes','no'))
            housing=st.selectbox('has housing loan?',('yes','no'))
            loan=st.selectbox('has Personal loan?',('yes','no'))
            contact=st.selectbox('contact communication type',('unknown', 'cellular', 'telephone'))
            months=st.selectbox('select a month',('jan', 'feb','mar', 'apr','may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'))
            poutcome=st.selectbox('outcome of the previous marketing campaign',('unknown', 'other', 'failure', 'success'))

        # ------------------------------------input processing-------------------------------------
            new_job=job_enc.transform([str(job)])[0]
            new_marital=marital_enc.transform([str(marital)])[0]
            new_education=education_enc.transform([str(education)])[0]
            new_default=default_enc.transform([str(default)])[0]
            new_housing=housing_enc.transform([str(housing)])[0]
            new_loan=loan_enc.transform([str(loan)])[0]
            new_contact=contact_enc.transform([str(contact)])[0]
            new_month=month_enc.transform([str(months)])[0]
            new_poutcome=poutcome_enc.transform([str(poutcome)])[0]

        # ------------------------------------prediction process-------------------------------------
            result=model.predict([[age,balance,int(day),duration,campaign,int(pdays),Previous,
                                new_job,new_marital,new_education,new_default,new_housing,
                        new_loan,new_contact,new_month,new_poutcome]])
            if st.form_submit_button('Predict'):            
                if result[0] == 0 :
                    st.error("The Client won't Deposit ❌")
                else:
                    st.success("The Client will Deposit ✅")
    except :
        st.button('Predict',disabled=True)
        st.error('Check From Your Inputs')
# ---------------------------Contact Page-----------------------------
if selected =='Contact Us':
    st.markdown("<h2 style='text-align: center; color: gold;'>Contact Us</h2>", unsafe_allow_html=True)
    st.header(":mailbox: Get In Touch With Me!")


    contact_form = """
    <form action="https://formspree.io/f/xnqynawb" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")

# ======================footer====================================

headers="""<style>
h2,h4{text-shadow: 2px 2px 8px black;
background-color: transparent;
text-decoration: underline;
</style>

"""
st.markdown(headers,unsafe_allow_html=True)
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
st.markdown(hide_st_style, unsafe_allow_html=True)
