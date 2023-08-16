
ABCD_CODMORSE = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
  
}

def Texto_a_codigo_morse(text):
    return ' '.join(ABCD_CODMORSE.get(char, '') for char in text.upper())

def codMorse_a_texto(morse_code):
    cod_morse_reves = {valor: k for k, valor in ABCD_CODMORSE.items()}
    return ''.join(cod_morse_reves.get(code, '') for code in morse_code.split())

sc = input("que desea hacer: \n1. pasar de texto a codigo Morse \n2. Pasar de codigo Morse a texto\n")

if sc == '1':
    text = input("Ingrese el texto para pasar a codigo Morse: ")
    morse_code = Texto_a_codigo_morse(text)
    print("El codigo Morse es el siguiente :", morse_code)
elif sc == '2':
    morse_code = input("Ingrese el código Morse a pasar a Texto: ")
    text = codMorse_a_texto(morse_code)
    print("El texto es :", text)

  
