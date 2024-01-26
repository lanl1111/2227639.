def morse_translator(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..'
    }
    morse_translated = ''
    for word in text.upper().split():
        for char in word:
            morse_translated += morse_code_dict.get(char, '') + ' '
        morse_translated = morse_translated.strip() + ' / '
    
    return morse_translated.strip(' / ')

print(morse_translator("Hello World"))
