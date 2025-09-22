def on_received_number(receivedNumber):
    if receivedNumber == 0:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        music.play(music.tone_playable(262, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
    elif receivedNumber == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . # # # .
            . . . . .
            . . . . .
            """)
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    elif receivedNumber == 2:
        basic.show_string("M1")
        music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    elif receivedNumber == 3:
        basic.show_string("M2")
        music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    elif receivedNumber == 4:
        basic.show_string("M3")
        music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    basic.clear_screen()
radio.on_received_number(on_received_number)

def on_logo_long_pressed():
    radio.send_number(3)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_a():
    radio.send_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_free_fall():
    music.play(music.create_sound_expression(WaveShape.SINE,
            4999,
            2668,
            245,
            0,
            1001,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
input.on_gesture(Gesture.FREE_FALL, on_gesture_free_fall)

def on_button_pressed_ab():
    radio.send_number(4)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_number(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    radio.send_number(2)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_every_interval():
    basic.clear_screen()
loops.every_interval(5000, on_every_interval)
