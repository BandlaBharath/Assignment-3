import tkinter as tk
from googletrans import Translator

# List of words/phrases/objects to exclude from translation
exclusions = ["apple", "car", "hello", "goodbye"]

def translate_text():
    text_to_translate = input_text.get("1.0", "end-1c")
    translator = Translator()

    # Split the text into sentences
    sentences = text_to_translate.split(".")
    translated_sentences = []

    for sentence in sentences:
        words = sentence.split()
        translated_words = []

        for word in words:
            # Check if the word is in the exclusions list
            if word.lower() in exclusions:
                translated_words.append(word)
            else:
                try:
                    translated_word = translator.translate(word, src='en', dest='hi').text
                    translated_words.append(translated_word)
                except Exception as e:
                    # Handle exceptions (e.g., if translation fails)
                    translated_words.append(word)

        translated_sentence = " ".join(translated_words)
        translated_sentences.append(translated_sentence)

    translated_text = ". ".join(translated_sentences)

    output_text.delete("1.0", "end")
    output_text.insert("1.0", translated_text)

# Create the main application window
app = tk.Tk()
app.title("English to Hindi Translator with Exclusions")

# Create input and output text widgets
input_text = tk.Text(app, height=5, width=40)
output_text = tk.Text(app, height=5, width=40)

# Create Translate button
translate_button = tk.Button(app, text="Translate", command=translate_text)

# Pack widgets
input_text.pack()
translate_button.pack()
output_text.pack()

# Start the GUI main loop
app.mainloop()
