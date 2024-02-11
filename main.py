import streamlit as st

letter = '''
Hi babi love mahal irog kalandian ko! Feb 6, 2024, marks six years and nine months since we embarked on this incredible journey together. Thank you for filling the past 81 months with so much love and laughter. I'm grateful for every one of the 352 weeks and 3 days we've shared, and for the 2,467 days of pure joy and happiness you've brought into my life.

Being with you feels like snuggling up in a cozy blanket, wrapped in happiness, peace, and love. Every moment with you is like a sprinkle of magic, and I'll hold onto these memories forever.

Life can get crazy, but you're my anchor, my source of strength. Your love and support keep me going through thick and thin, and I can't thank you enough for that.

As we reflect on our journey together, I find myself longing for more adventures with you by my side. Will you be my Valentine, my partner in crime? Let's create even more beautiful memories together and continue this incredible journey of love.
'''

def get_result(user_name, password, response):
    if user_name == 'ramlovejade' and password == 'iloveyoulove06':
        return letter

def main():
    st.title("💙")

    # Text input
    with st.form(key='my_form'):
        user_name = st.text_input("Enter username", "")
        st.write('hint: "madlovejear"')
        password = st.text_input("Enter password", "", type="password")
        submitted = st.form_submit_button("Submit")

        if submitted:
            if user_name.lower() == 'ramlovejade' and password.lower() == 'iloveyoulove06':
                response = st.text_input("(yes/no)", "").lower()

                if response == 'yes':
                    st.markdown("## I'll see you on Feb 14! 💙")
                elif response == 'no':
                    st.markdown('## you mean yes? -_-')
                elif response == 'luh':
                    st.markdown('## luh i love you')

                result = get_result(user_name.lower(), password.lower(), response)
                st.markdown("## From adi 🌻")
                st.write(result)
                st.write("From your adi")
            else:
                st.markdown('## Wrong credentials your not my babi')



if __name__ == "__main__":
    main()
