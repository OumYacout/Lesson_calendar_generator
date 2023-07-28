# gpt3 professional email generator by Belghini - version July 2023
# to run : streamlit run streamlit_app.py

import os
import openai
import streamlit as st


# Connect to OpenAI GPT-3, fetch API key from Streamlit secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

#or enter the api key here
#openai.api_key = "........"

Model= "text-davinci-003"


def gen_lesson(nb_chapter, subject):

    response = openai.Completion.create(
        engine=Model,
        prompt=f"Write {nb_chapter} chapter lesson plan calendarfor the subject: {subject}.The markdown table should. The markdown table columns should be: Chapter, Lesson, Activity, Homework. Please organize each lesson in the table so that it looks like a calendar. ",
        temperature=0.8,
        max_tokens=4000,
        top_p=0.8,
        best_of=2,
        frequency_penalty=0.0,
        presence_penalty=0.0)

    return response.get("choices")[0]['text']


def main_gpt_calendar_lesson_generator():

    st.markdown('Generate Lesson Calendar related to a topic - powered by OpenAI using text-davinci-003 Model:sun_with_face:')
    st.write('\n')  # add spacing

    st.subheader('\nWhat is your Topic is about?\n')

    lesson_calendar_text = ""  # initialize columns variables
    col1, space, col2, space, col3 = st.columns([10, 0.5, 5, 0.5, 5])
    with col1:
        input_topic = st.text_input('Tape a topic')
    with col2:
        input_number = st.text_input('number of chapters')
    with col3:
        st.write("\n")
        st.write("\n")
        if st.button('Generate lesson calendar'):
            with st.spinner():
                lesson_calendar_text = gen_lesson(input_number, input_topic)
    if lesson_calendar_text != "":
        st.write('\n')  # add spacing
        with st.expander("Lesson Calendat Output", expanded=True):
            st.markdown(lesson_calendar_text)  #output the results


if __name__ == '__main__':
    main_gpt_calendar_lesson_generator()
