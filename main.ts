input.onGesture(Gesture.ScreenDown, function on_gesture_screen_down() {
    
    //  Wanneer het scherm naar beneden is, wordt de zin gereset
    //  Bovenstaande lijnen zorgen ervooor dat de Y waarde veranderd wordt.
    bericht = ""
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    //  Verandert X met 1 naar rechts wanneer er op A geklikt wordt.
    if (cursor.get(LedSpriteProperty.X) == 4 && cursor.get(LedSpriteProperty.Y) != 4) {
        cursor.change(LedSpriteProperty.X, -4)
        cursor.change(LedSpriteProperty.Y, 1)
    } else if (cursor.get(LedSpriteProperty.X) == 4 && cursor.get(LedSpriteProperty.Y) == 4) {
        cursor.change(LedSpriteProperty.Y, -4)
        cursor.change(LedSpriteProperty.X, -4)
        aantal_geklikt = -1
    } else {
        cursor.change(LedSpriteProperty.X, 1)
    }
    
    aantal_geklikt += 1
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    //  Wanneer er geshud wordt, wordt de cursor gereset.
    cursor.change(LedSpriteProperty.X, -4)
    cursor.change(LedSpriteProperty.Y, -4)
    aantal_geklikt = 0
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    //  Krijg de optie om bericht te verzenden of verzenden te annuleren
    cursor.delete()
    basic.showString(bericht)
    while (true) {
        if (input.buttonIsPressed(Button.A)) {
            radio.sendString(bericht)
            bericht = ""
            break
        } else if (input.buttonIsPressed(Button.B)) {
            break
        }
        
    }
    basic.pause(500)
    bericht = bericht.slice(0, -1)
    cursor = game.createSprite(0, 0)
    cursor.change(LedSpriteProperty.X, -4)
    aantal_geklikt = 0
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    //  Toon bericht als er een binnenkomt.
    if (receivedString.length < 50 && receivedString.length != 0) {
        basic.showString(receivedString, 300)
    } else if (receivedString.length == 0) {
        
    } else {
        basic.showIcon(IconNames.No, 5000)
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    //  Maak het bericht
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]
    bericht = "" + bericht + letters[aantal_geklikt]
})
let letters : string[] = []
let aantal_geklikt = 0
let cursor : game.LedSprite = null
let bericht = ""
radio.setGroup(5)
cursor = game.createSprite(0, 0)
