import streamlit as st
import time

# Title animation
def animated_title(title, delay=0.15):
    st.markdown(f"<h1 style='text-align: center; color: #6c63ff;'>{title}</h1>", unsafe_allow_html=True)
    time.sleep(delay)

# Palindrome Checker
def palindrome_checker():
    animated_title("🔍 Palindrome Checker")
    user_input = st.text_input("Enter a sentence or word:")

    if st.button("Check Palindrome"):
        cleaned = ''.join(user_input.lower().split())
        if cleaned == cleaned[::-1]:
            st.success("✅ It's a palindrome!")
        else:
            st.error("❌ Not a palindrome.")

# Sliding Window Visualizer
def sliding_window_visualizer():
    animated_title("🪟 Sliding Window Visualizer")

    user_input = st.text_input("Enter a string or space-separated numbers:")
    k = st.number_input("Window size:", min_value=1, step=1)

    def is_numeric_input(text):
        try:
            list(map(int, text.strip().split()))
            return True
        except ValueError:
            return False

    if user_input and k:
        if is_numeric_input(user_input):
            arr = list(map(int, user_input.strip().split()))
            if k > len(arr):
                st.error("❗ Window size is larger than the number of elements.")
            else:
                st.subheader("🔢 Numeric Sliding Windows (Sum)")
                for i in range(len(arr) - k + 1):
                    window = arr[i:i+k]
                    win_sum = sum(window)
                    st.success(f"Window [{i}:{i+k}] → {window}, Sum = {win_sum}")
        else:
            if k > len(user_input):
                st.error("❗ Window size is larger than string length.")
            else:
                st.subheader("🔤 String Sliding Windows")
                for i in range(len(user_input) - k + 1):
                    window = user_input[i:i+k]
                    st.success(f"Window [{i}:{i+k}] → \"{window}\"")

# -----------------------------

# Sidebar navigation
st.sidebar.title("🚀 Navigation")
option = st.sidebar.selectbox(
    "Choose an App:",
    ("Sliding Window Visualizer", "Palindrome Checker")
)

# Main app
if option == "Sliding Window Visualizer":
    sliding_window_visualizer()
else:
    palindrome_checker()

# Footer
st.markdown("---")
st.markdown("<h6 style='text-align: center;'>#DasariSriRanjani</h6>", unsafe_allow_html=True)
