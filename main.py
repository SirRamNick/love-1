import streamlit as st


letter = '''
    Hi babi love mahal baby ko! Feb 6, 2024, marks six years and nine months since we embarked on this incredible journey together. Thank you for filling the past 81 months with so much love and laughter. I'm grateful for every one of the 352 weeks and 3 days we've shared, and for the 2,467 days of pure joy and happiness you've brought into my life

Being with you feels like snuggling up in a cozy blanket, wrapped in happiness, peace, and love. Every moment with you is like a sprinkle of magic, and I'll hold onto these memories forever.

Life can get crazy, but you're my anchor, my source of strength. Your love and support keep me going through thick and thin, and I can't thank you enough for that.

As we reflect on our journey together, I find myself longing for more adventures with you by my side. Will you be my Valentine, my partner in crime? Let's create even more beautiful memories together and continue this incredible journey of love.
'''


def get_result(user_name, password):
    if user_name == 'ramlovejade' and password == 'iloveyoulove06':
        st.empty()
        return letter


def main():
    st.title("💙")
    
    # Text input
    with st.form(key='my_form'):
        user_name = st.text_input("Enter something", "")
        password = st.text_input("Enter something", "", type="password")
        submitted = st.form_submit_button("Submit")
        if submitted:
            result1 = get_result(user_name, password)
            st.markdown("## From adi 🌻")
            st.write(result1)
            st.write("From your adi")

if __name__ == "__main__":
    main()
