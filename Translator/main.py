# Import the Translator class from the translate module
from translate import Translator

# Function to translate a given word to a specified language
def translate_words(word, language):
    # Initialize the translator with the target language
    translator = Translator(to_lang=language)
    
    try:
        # Attempt to translate the given word
        word_translation = translator.translate(word)
    except Exception as e:
        # Handle translation errors and print an error message
        print(f"Translation failed: {e}")
        word_translation = None

    # Return the translated word (or None if translation failed)
    return word_translation
    
# Main loop for user interaction
while True:
    # Get user input for an English word
    english_word = input("Enter an English word: ")
    
    # Check if the user wants to exit the loop
    if english_word == "xxx":
        break

    # Translate the English word to Hindi and Vietnamese
    hindi_translation = translate_words(english_word, "hi")
    vietnamese_translation = translate_words(english_word, "vi")

    # Print the original word and its translations
    print(f"English: {english_word}")
    print(f"Hindi: {hindi_translation}")
    print(f"Vietnamese: {vietnamese_translation}")

        
    