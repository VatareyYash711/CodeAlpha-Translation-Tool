import streamlit as st
import requests

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 Language Translation Tool")
st.write("Translate text between supported languages.")

LANGUAGES = {
    "Auto Detect": "autodetect",
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Punjabi": "pa",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Russian": "ru"
}

left, right = st.columns(2)

with left:
    source_name = st.selectbox(
        "Source language",
        list(LANGUAGES.keys()),
        index=1
    )

with right:
    target_name = st.selectbox(
        "Target language",
        [name for name in LANGUAGES if name != "Auto Detect"],
        index=2
    )

text = st.text_area(
    "Enter text to translate",
    height=160,
    placeholder="Type your text here..."
)

if st.button("Translate", type="primary", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some text.")

    elif source_name == target_name:
        st.info("Source and target languages are the same.")

    else:
        try:
            source = LANGUAGES[source_name]
            target = LANGUAGES[target_name]

            if source == "autodetect":
                st.warning(
                    "Please select the source language "
                    "instead of Auto Detect."
                )
            else:
                response = requests.get(
                    "https://api.mymemory.translated.net/get",
                    params={
                        "q": text.strip(),
                        "langpair": f"{source}|{target}"
                    },
                    timeout=20
                )

                response.raise_for_status()
                data = response.json()

                if data.get("responseStatus") == 200:
                    translated = data["responseData"]["translatedText"]

                    st.subheader("Translated text")
                    st.text_area(
                        "Result",
                        value=translated,
                        height=160
                    )

                    st.download_button(
                        "Download Translation",
                        data=translated,
                        file_name="translation.txt",
                        mime="text/plain"
                    )
                else:
                    st.error(
                        "Translation service could not process "
                        "your request. Please try again later."
                    )

        except requests.exceptions.Timeout:
            st.error("The request timed out. Please try again.")

        except requests.exceptions.RequestException:
            st.error(
                "Could not connect to the translation service. "
                "Check your internet connection."
            )

        except (KeyError, ValueError):
            st.error(
                "Unexpected response from the translation service."
            )

st.caption(
    "Educational project. An internet connection is required."
)