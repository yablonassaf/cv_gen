#streamlit run first_app.py
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd


st.title('Welcome the Harvard Resume Generator')
st.text("")
st.text("")


df = pd.DataFrame({
  'first column': ["Technology", "Banking", "Consulting", "Healthcare"],
  'second column': [10, 20, 30, 40]
})


option = st.selectbox(
    'In which industry do you work?',
     df['first column'])

'You selected: ', option

import time
st.text("")
st.text("")
st.text("")
st.text("")

'Generating resume...'
st.text("")

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Loading please hold {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and your resume is done!'