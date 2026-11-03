# Task 1 — Language Translation Tool

A Streamlit application that accepts text, lets the user choose source and target languages, and displays the translated result.

## Main features
- Source and target language selection
- Automatic source-language detection
- Translation result display
- Download translated text
- Basic input and error handling

## Run
From the main project folder:
```bash
streamlit run task1_translation/app.py
```

## Method
The interface is built with Streamlit. The `deep-translator` package sends the text to its Google Translate integration and returns the translated text. Internet access is required.
