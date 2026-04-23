import streamlit as st
import random
st.title("🎲 Ready for Guess A Number Game?🎲")
st.write("Can you get it in first try?")

st.header ("You look brave" )
name = st.text_input("What's Your Name?") 
if name:
    st.success(f"Hello **{name}** you only have 4 trial before💣💥 *Byebye*")
if "number" not in st.session_state:
    st.session_state.number = random.randint(1,50)
    st.session_state.attempts = 0

user_value = st.number_input("Guess number (1-50)", min_value=1, max_value=50)

if st.button("Check"):
    st.session_state.attempts += 1

    if st.session_state.attempts > 4:
        st.error("💣 Game Over! No more tries")
        st.stop()

    if user_value == st.session_state.number:
        st.success("🎉 Correct! You win!🙌 See you next time")
    elif st.session_state.attempts >= 4:
        st.error(f"💣 Game Over! Number was {st.session_state.number}")
    elif user_value > st.session_state.number:
        st.warning("Too high!👏 Try again kiddo")
    else:
        st.warning("Too low!🤏 Oops")

    st.write(f"Attempts left: {4 - st.session_state.attempts}")
