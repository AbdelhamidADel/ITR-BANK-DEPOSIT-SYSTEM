import pickle

#--------------------------Encoders---------------------------------
#  contact_enc
with open('./Encoders/contact_enc.pkl', 'rb') as contact:
    contact_enc = pickle.load(contact)

#  default_enc
with open('./Encoders/default_enc.pkl', 'rb') as default:
    default_enc = pickle.load(default)
    
# deposit_enc
with open('./Encoders/deposit_enc.pkl', 'rb') as deposit:
    deposit_enc = pickle.load(deposit)

# education_enc
with open('./Encoders/education_enc.pkl', 'rb') as education:
    education_enc = pickle.load(education)

# housing_enc
with open('./Encoders/housing_enc.pkl', 'rb') as housing:
    housing_enc = pickle.load(housing)

# job_enc
with open('./Encoders/job_enc.pkl', 'rb') as job:
    job_enc = pickle.load(job)  

# loan_enc
with open('./Encoders/loan_enc.pkl', 'rb') as loan:
    loan_enc = pickle.load(loan)

# marital_enc
with open('./Encoders/marital_enc.pkl', 'rb') as marital:
    marital_enc = pickle.load(marital)

# month_enc
with open('./Encoders/month_enc.pkl', 'rb') as month:
    month_enc = pickle.load(month)
    
# poutcome_enc
with open('./Encoders/poutcome_enc.pkl', 'rb') as poutcome:
    poutcome_enc = pickle.load(poutcome)   


#--------------------------model---------------------------------
with open('./Classification Model/Class_Model.pkl', 'rb') as deposit:
    model = pickle.load(deposit)   
