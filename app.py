import streamlit as st
import traceback

from scraper import process_url

st.title("Video Scraper")

url = st.text_input("Enter URL")

start_button = st.button("Start")

progress_container = st.empty()
status_container = st.empty()
result_container = st.empty()

if start_button and url:

    url = url.strip()

    status_container.empty()
    result_container.empty()

    progress = progress_container.progress(0)

    with st.spinner("Processing URL... Please wait. ⏳"):

        try:
            results = process_url(
                url,
                progress_callback=progress.progress,
            )

            progress_container.empty()

            status_container.success("Done!")

            with result_container.container():
                st.subheader("Results")
                st.code("\n".join(results))

        except Exception as e:
            progress_container.empty()
            status_container.error(str(e))

            # NEW: виводимо повний traceback помилки
            st.code(traceback.format_exc())