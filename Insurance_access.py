import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


title = st.title("Insurance Access Dashboard")
df = pd.read_csv(".csv")







ch = st.checkbox('I understand this data')
if ch:
    st.write("Thanks for visiting Sainab's Admin Dashboard")