from microbit import *
import music

def show_image(image):
    display.show(image)
    sleep(50)

def show_centre_pixel():
    display.set_pixel(2, 2, 9)
    sleep(50)

def animate_heart():
    show_image(Image.HEART)
    show_image(Image.HEART_SMALL)
    show_centre_pixel()
    display.clear()
    sleep(50)
    show_centre_pixel()
    show_image(Image.HEART_SMALL)
    show_image(Image.HEART)
    sleep(50)

music_list = ['DADADADUM',
              'ENTERTAINER',
              'PRELUDE',
              'ODE',
              'NYAN',
              'RINGTONE',
              'FUNK',
              'BLUES',
              'BIRTHDAY',
              'WEDDING',
              'FUNERAL',
              'PUNCHLINE',
              'PYTHON',
              'BADDY',
              'CHASE',
              'BA_DING',
              'WAWAWAWAA',
              'JUMP_UP',
              'JUMP_DOWN',
              'POWER_UP',
              'POWER_DOWN']

music_index = 0

while True:
    animate_heart()
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll("BYE!")
        sleep(1000)
        display.clear()
        break
    elif button_a.is_pressed():
        if music_index > 0:
            music_index -= 1
            display.scroll(music_list[music_index])
            music.play(eval('music.' + music_list[music_index]))
        else:
            display.scroll(music_list[0])
            music.play(eval('music.' + music_list[0]))
    elif button_b.is_pressed():
        if music_index < len(music_list):
            music_index += 1
            display.scroll(music_list[music_index])
            music.play(eval('music.' + music_list[music_index]))
        else:
            display.scroll(music_list[music_index])
            music.play(eval('music.' + music_list[len(music_list) - 1]))
