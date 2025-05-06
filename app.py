import streamlit as st
import time
from collections import Counter

st.set_page_config(page_title="Mini Apps Hub", layout="centered")

# ---------------- Title Animation ----------------
def animated_title(title, delay=0.15):
    st.markdown(f"<h1 style='text-align: center; color: #6c63ff;'>{title}</h1>", unsafe_allow_html=True)
    time.sleep(delay)

# ---------------- Anagram Checker ----------------
def anagram_checker():
    animated_title("🔁 Anagram Checker")
    s1 = st.text_input("Enter the first word or sentence:")
    s2 = st.text_input("Enter the second word or sentence:")

    def clean_string(s):
        return ''.join(s.lower().split())

    if st.button("Check Anagram"):
        cleaned_s1 = clean_string(s1)
        cleaned_s2 = clean_string(s2)
        if Counter(cleaned_s1) == Counter(cleaned_s2):
            st.success("🎉 They are anagrams!")
        else:
            st.error("❌ Not anagrams")

# ---------------- Palindrome Checker ----------------
def palindrome_checker():
    animated_title("🔍 Palindrome Checker")
    user_input = st.text_input("Enter a sentence or word:")

    if st.button("Check Palindrome"):
        cleaned = ''.join(user_input.lower().split())
        if cleaned == cleaned[::-1]:
            st.success("✅ It's a palindrome!")
        else:
            st.error("❌ Not a palindrome.")

# ---------------- Sliding Window Visualizer ----------------
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

# ---------------- Sidebar Navigation ----------------
st.sidebar.title("🚀 Navigation")
option = st.sidebar.selectbox(
    "Choose an App:",
    ("Sliding Window Visualizer", "Palindrome Checker", "Anagram Checker")
)

# ---------------- Run selected section ----------------
if option == "Sliding Window Visualizer":
    sliding_window_visualizer()
elif option == "Palindrome Checker":
    palindrome_checker()
else:
    anagram_checker()

# ---------------- Footer ----------------
st.markdown("---")
st.markdown("<h6 style='text-align: center;'>#DasariSriRanjani</h6>", unsafe_allow_html=True)
