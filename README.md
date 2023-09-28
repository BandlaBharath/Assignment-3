# Assignment-3
English to Hindi Translator

# English to Hindi Translator with Exclusions

I developed this app using Python's Tkinter and the `googletrans` Google Translate API. Its aim is to translate English text into Hindi. Just input the English text, and the app will produce the Hindi translation for you. Also, you can choose to remove particular words or phrases from the translation.

## Prerequisites

Before running this application, make sure you have the following prerequisites installed:

- Python (Python 3.6 or higher)
- Tkinter library for GUI
- Google Translate API (`googletrans`) library

You can install the required libraries using pip:

#pip install tkinter googletrans==4.0.0-rc1



--> How to Use the Application:

1. Run the Application: Run the Python script provided in your terminal or code editor to start the application.

#python your_script.py

2. Application Interface: The GUI window will appear, featuring the     following components:

-Input Text Area: Enter the English text you want to translate in this text area.
-Translate Button: Click this button to initiate the translation process.
-Output Text Area: The translated text in Hindi will be displayed in this area.

3. Translation Process:

-The application splits the input text into sentences based on periods (".") and then further divides each sentence into words.
-For each word, it checks if the word exists in the "exclusions" list. If it's in the list, the word is kept as-is and not translated.
-If the word is not in the exclusions list, it is translated from English to Hindi using the Google Translate API.
-Finally, the translated sentences are combined, and the translated text is displayed in the output text area.

4. Exclusions List: You can customize the list of words, phrases, or objects to exclude from translation by modifying the "exclusions" list in the script. This is useful for preserving specific terms that shouldn't be translated.



--> Customization:

-To add more words or phrases to the "exclusions" list, simply extend the list with the items you want to exclude.
-You can customize the appearance and layout of the GUI, such as changing the window title, widget sizes, fonts, or colors.



--> Limitations:

-The translation quality relies on the Google Translate API, which may not always provide perfect translations, especially for complex or context-dependent sentences.
-The application splits sentences based on periods (".") and doesn't consider other punctuation marks or context.
-Translation might not always be accurate, especially for specialized terms or idiomatic expressions.



--> Disclaimer:

-This application relies on a free online translation service, and its usage might be subject to rate limiting or service availability. Ensure you use it responsibly and respect the terms of service of the translation API provider.
