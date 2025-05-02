import streamlit as st
import random

# Title of the app
st.title("Coin Toss App")

# Button to toss the coin
if st.button("Toss the Coin"):
    result = random.choice(["Heads", "Tails"])
    st.write(f"The result is: **{result}**")
else:
    st.write("Click the button to toss the coin!")
