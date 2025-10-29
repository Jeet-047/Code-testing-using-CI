import streamlit as st

# StreamLit UI
st.title("Power Calculator")
st.write("Enter a number to calculate it's square, cube, and fifth power")

# Get user input
user_input = st.number_input("Enter an integer",min_value=1, step=1, placeholder="write a positive integer")

# Calculate results
square = user_input ** 2
cube = user_input ** 3
fifth_power = user_input ** 5

# Display outputs
st.write(f"The square of {user_input} is -> {square}")
st.write(f"The cube of {user_input} is -> {cube}")
st.write(f"The fifth power of {user_input} is -> {fifth_power}")