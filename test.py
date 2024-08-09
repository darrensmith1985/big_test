import pandas as pd
import quickfix as fix
from xbbg import blp

import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)
