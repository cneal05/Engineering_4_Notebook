#type: ignore

import board
import digitalio
import time
led = digitalio.DigitalInOut(board.GP20)
led.direction = digitalio.Direction.OUTPUT

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier

# Dictionary representing the morse code chart
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}


while True:
    print("Enter Morse Code Message, or enter -q to quit:")
    message = input()
    if message == "-q":
        break
    else:
        final = ""
        for letter in message:
            letter = letter.upper()
            letter = MORSE_CODE[letter]
            final = f"{final + letter} "
        print(final)
        for character in message:
            if character == ".":
                led.value = True
                time.sleep(dot_time)
                led.value = False
            if character == "-":
                led.value = True
                time.sleep(dash_time)
                led.value = False
            if character == " ":
                led.value = True
                time.sleep(between_letters)
                led.value = False
            if character == "/":
                led.value = True
                time.sleep(between_words)
                led.value = False