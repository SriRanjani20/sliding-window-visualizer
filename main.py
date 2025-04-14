import streamlit as st

st.title("🪟 Sliding Window Visualizer")

user_input = st.text_input("Enter a string or space-separated numbers:")
k = st.number_input("Window size:", min_value=1, step=1)

def is_numeric_input(text):
    try:
        _ = list(map(int, text.strip().split()))
        return True
    except ValueError:
        return False

if user_input and k:
    if is_numeric_input(user_input):
        # Numeric Array Mode
        try:
            arr = list(map(int, user_input.strip().split()))
            if k > len(arr):
                st.error("Window size is larger than the number of elements.")
            else:
                st.subheader("🔢 Numeric Sliding Windows (with sum):")
                for i in range(len(arr) - k + 1):
                    window = arr[i:i+k]
                    win_sum = sum(window)
                    st.text(f"Window [{i}:{i+k}] → {window}, Sum = {win_sum}")
        except ValueError:
            st.error("Invalid numeric input.")
    else:
        # String Mode
        if k > len(user_input):
            st.error("Window size is larger than string length.")
        else:
            st.subheader("🔤 String Sliding Windows:")
            for i in range(len(user_input) - k + 1):
                window = user_input[i:i+k]
                st.text(f"Window [{i}:{i+k}] → \"{window}\"")
