from spellchecker import SpellChecker

spell = SpellChecker()

def correct_spelling(text):
    corrected = spell.candidates(text)
    if corrected is not None :
        corrected.add(text)
    return corrected
