def on_gesture_screen_down():
    global bericht
    # Wanneer het scherm naar beneden is, wordt de zin gereset
    # Bovenstaande lijnen zorgen ervooor dat de Y waarde veranderd wordt.
    bericht = ""
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_button_pressed_a():
    global aantal_geklikt
    # Verandert X met 1 naar rechts wanneer er op A geklikt wordt.
    if cursor.get(LedSpriteProperty.X) == 4 and cursor.get(LedSpriteProperty.Y) != 4:
        cursor.change(LedSpriteProperty.X, -4)
        cursor.change(LedSpriteProperty.Y, 1)
    elif cursor.get(LedSpriteProperty.X) == 4 and cursor.get(LedSpriteProperty.Y) == 4:
        cursor.change(LedSpriteProperty.Y, -4)
        cursor.change(LedSpriteProperty.X, -4)
        aantal_geklikt = -1
    else:
        cursor.change(LedSpriteProperty.X, 1)
    aantal_geklikt += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global aantal_geklikt
    # Wanneer er geshud wordt, wordt de cursor gereset.
    cursor.change(LedSpriteProperty.X, -4)
    cursor.change(LedSpriteProperty.Y, -4)
    aantal_geklikt = 0
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global bericht, cursor, aantal_geklikt
    # Krijg de optie om bericht te verzenden of verzenden te annuleren
    cursor.delete()
    basic.show_string(bericht)
    while True:
        if input.button_is_pressed(Button.A):
            radio.send_string(bericht)
            bericht = ""
            break
        elif input.button_is_pressed(Button.B):
            break
    basic.pause(500)
    bericht = bericht.slice(0, -1)
    cursor = game.create_sprite(0, 0)
    cursor.change(LedSpriteProperty.X, -4)
    aantal_geklikt = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    # Toon bericht als er een binnenkomt.
    if len(receivedString) < 50 and len(receivedString) != 0:
        basic.show_string(receivedString, 300)
    elif len(receivedString) == 0:
        pass
    else:
        basic.show_icon(IconNames.NO, 5000)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global letters, bericht
    # Maak het bericht
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
    bericht = "" + bericht + letters[aantal_geklikt]
input.on_button_pressed(Button.B, on_button_pressed_b)

letters: List[str] = []
aantal_geklikt = 0
cursor: game.LedSprite = None
bericht = ""
radio.set_group(5)
cursor = game.create_sprite(0, 0)