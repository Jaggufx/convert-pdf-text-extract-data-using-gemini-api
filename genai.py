#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install google-generativeai


# In[2]:


pip install PyPDF2


# In[36]:


import google.generativeai as genai
import os
import pandas as pd
from PyPDF2 import PdfReader
import json


# In[83]:


genai.configure(api_key="AIzaSyBTtPfm20WiKRPqxbmCTeHkw5pGSTqjfjo")
model = genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config={"response_mime_type": "application/json"})
reader = PdfReader('resume.pdf')
no_of_pages = len(reader.pages)
for pg in range(0,no_of_pages):
    page = reader.pages[pg]
    text = page.extract_text()
    response = model.generate_content(f"find the name, college, email, phone number and skills in {text} give structured data in json format ")
    dt = response.text
    # print(type(dt))
dd = json.loads(dt)
# print(dd)
data = pd.DataFrame([dd])
data


# In[ ]:





# In[ ]:




