import streamlit as st
import google.generativeai as veddyAI
from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate

prompt_template = """Your job is to generate code accordingly and precisely for asked question if the question is incomplete then just reply by what do you want?"""

load_dotenv()
API_KEY = os.environ.get("KEY")
veddyAI.configure(api_key=API_KEY)

def main():
    st.set_page_config(
        page_title="Veddy AI - CHAT",
        layout="centered"
    )

    st.title(":violet[Veddy AI]")
    st.image('https://media.tenor.com/n53f5g-plM0AAAAi/emo.gif', width=120)
    st.header("The Code Bot")

    prompt = st.text_input("Ready For Action 🔥", placeholder="Question Here", key="prompt_input")

    if st.button("Generate Code", key="generate_button"):
        if prompt:
            model = "models/text-bison-001"
            response = veddyAI.generate_text(
                model=model,
                prompt=prompt + prompt_template,
                temperature=0.6,
                max_output_tokens=800
            )

            with st.expander("Response", expanded=True):
                st.markdown(response.result, unsafe_allow_html=True)
        else:
            st.warning("Please enter a prompt before generating text.")
        hide_st_style = """
                        <style>
                        # MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        </style>

                        """
        st.markdown(hide_st_style, unsafe_allow_html=True)

    # Custom Footer with Styling
    st.markdown(
        """
        <div style="position: fixed; bottom: 10px; right: 10px; background-color: #ff4b4b; padding: 10px; border-radius: 8px; color: white;">
            Thevk22
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
