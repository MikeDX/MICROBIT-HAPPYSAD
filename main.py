def clearface():
    global happy, sad
    happy = 0
    sad = 0

def on_button_pressed_a():
    global happy
    if happy == 1:
        basic.show_icon(IconNames.ASLEEP)
        clearface()
    else:
        basic.show_icon(IconNames.HAPPY)
        happy = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global sad
    if sad == 1:
        basic.show_icon(IconNames.ASLEEP)
        clearface()
    else:
        basic.show_icon(IconNames.SAD)
        sad = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

sad = 0
happy = 0
basic.show_icon(IconNames.ASLEEP)
happy = 0
sad = 0

def on_forever():
    pass
basic.forever(on_forever)
