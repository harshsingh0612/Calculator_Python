import streamlit as st

def calculator():
    st.title("Calculator")
    
    # Get user inputs
    number1 = st.number_input("Enter the first number:")
    operation = st.selectbox("Select an operation", ["+", "-", "*", "/"])
    number2 = st.number_input("Enter the second number:")
    
    # Perform calculation based on operation selected
    result = 0
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        if number2 == 0:
            st.error("Error: Division by zero!")
        else:
            result = number1 / number2
    
    # Display the result
    st.write(f"Result: {number1} {operation} {number2} = {result}")

if __name__ == "__main__":
    calculator()