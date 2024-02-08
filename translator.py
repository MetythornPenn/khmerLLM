from deep_translator import GoogleTranslator

def translate_to_english(text):
    # Translate text to English
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    return translated

def translate_to_khmer(text):
    # Translate text to Khmer
    translated = GoogleTranslator(source='auto', target='km').translate(text)
    return translated

# Example usage:
eng_txt = "Yeah, I plan to apply for the Chevening Scholarship, but I want to gain 3 or more years of work experience before applying."
khm_txt = "រក្សាវាឡើង អ្នកពិតជាអស្ចារ្យមែន"

# english_translation = translate_to_english(khm_txt)
# khmer_translation = translate_to_khmer(eng_txt)

# print("English Translation:", english_translation)
# print("Khmer Translation:", khmer_translation)