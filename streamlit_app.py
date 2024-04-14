import pandas as pd
import streamlit as st

# apply custom css if needed
# with open('assets/styles/style.css') as css:
#     st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

if __name__ == "__main__":
    st.title('🔨 Streamlit Template')
    st.markdown("""
        This app is only a template for a new Streamlit project. <br>

        ---
        """, unsafe_allow_html=True)

    st.balloons()

st.title('🔨 Streamlit Template')
st.write("hello")
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='latin1')  # replace 'latin1' with the correct encoding
    st.write(df)