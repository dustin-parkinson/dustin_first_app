import streamlit as st
import numpy as np
import pandas as pd

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)