#Sequencer coded by Nathan Blades.
from microbit import *
import music

h_pos = 0 #Tracks selection cursor position
h_pos2 = 0 #Tracks playback position
display.set_pixel(h_pos, 3, 5) #Sets cursor default position
music.set_tempo() #Sets the song tempo to 120bpm.
#Put 'bpm=' and a number in the brackets to set a different tempo.

#Put your music lists in here!
MusicA=["g4:1", "a#", "g", "f", "d#"]
MusicB=["d#4:1", "r", "d#", "g#", "g#"]
MusicC=["f4:1", "g#", "g", "g:2", "d#"]


#Tilt controls for selector
while True:
    switch_on = display.get_pixel(h_pos, 3) #Check current LED brightness of 'cursor' row
    if switch_on != 5: #If LED isn't lit as 'cursor'
        display.set_pixel(h_pos, 3, 5) #Set LED to 'cursor' brightness.
    sleep(100)
    # Check tilt.
    reading = accelerometer.get_x()
    # If big tilt to the right...
    if reading > 300 and h_pos < 4:
        display.set_pixel(h_pos, 3, 0) #Turn LED off
        h_pos += 1 #Move position right

    # If big tilt to the left...
    elif reading < -300 and h_pos > 0:
        display.set_pixel(h_pos, 3, 0)
        h_pos -= 1 #Move position left

    #Change an LED's 'phrase' with the A button!
    if button_a.is_pressed():
        switch_on = display.get_pixel(h_pos, 2) #Check LED brightness above 'cursor' LED
        if switch_on == 0: #If LED is off...
            display.set_pixel(h_pos, 2, 9) #Set LED to 9
            sleep(100)
        elif switch_on == 9: #If LED is at 9...
            display.set_pixel(h_pos, 2, 5) #Set LED to 5.
            sleep(100)
        elif switch_on == 5: #If LED is at 5...
            display.set_pixel(h_pos, 2, 0) #Set LED to 0.
            sleep(100)

    # Playback your mix with the B button!
    # Each LED in Row 2 is checked in turn. Plays a different phrase depending on LED brightness.
    if button_b.is_pressed():
        h_pos2 = 0
        while h_pos2 <= 4: #For each of the LEDs in row 1...
            display.set_pixel(h_pos2, 1, 9)
            playback = display.get_pixel(h_pos2, 2) #Check current LED brightness in row 2.
            if playback == 0: #If the LED is off, play...
                music.play(MusicA)
                display.set_pixel(h_pos2, 1, 0) #Turn off Playback LED
                h_pos2 += 1 #Move Playback LED.
            if playback == 9: #If LED is at Brightness 9, play...
                music.play(MusicB)
                display.set_pixel(h_pos2, 1, 0) #Turn off Playback LED
                h_pos2 += 1 #Move Playback LED.
            if playback == 5: #If LED is at Brightness 5, play...
                music.play(MusicC)
                display.set_pixel(h_pos2, 1, 0) #Turn off Playback LED
                h_pos2 += 1 #Move Playback LED.
