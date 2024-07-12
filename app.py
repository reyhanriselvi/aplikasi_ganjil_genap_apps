import streamlit as st

number2 = st.number_input("Insert the second number")
if st.button('Check Type'):
    if number2 % 2 == 0:
        st.write(f"The number {number2} is even.")
    else:
        st.write(f"The number {number2} is odd.")


result = number1 * number2
if st.button('Check Result Type'):
    if result % 2 == 0:
        st.write(f"The result of {number1} * {number2} = {result} is even.")
    else:
        st.write(f"The result of {number1} * {number2} = {result} is odd.")