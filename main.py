import streamlit as st
import webbrowser

st.set_page_config(page_title="Happy Birthday!", page_icon="🎂")

st.title("🎂 Happy Birthday! 🎉")
st.write(f"Hi bachhcaaa, happy birthdayy 🎊")

# Add a button to celebrate
if st.button("🎁 Click for a Surprise!"):
    st.balloons()
    st.write("🎶 *Happy Birthday to You!* 🎶")
    st.write("Click below for Surprise 2! 🎁")

url = "https://g5277.github.io/happy-birthday/"

if st.button("🎉 Click Here for Surprise 2!"):
    st.write(" PLEASE GO HERE https://g5277.github.io/happy-birthday/")

if st.button("🎆 Click Here for Surprise 3!"):
    url2 = " PLEASE VISIT https://docs.google.com/document/d/1AxY7qCmBSha9Ci4YQe4iKUse2mpUHBMuVzBPf43gZaY/edit?usp=drivesdk"
    st.write(url2)