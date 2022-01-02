style inventory_label:
    xalign 0.2

style slot:
    background Frame("square", 0,0)
    minimum (80,80)
    maximum (80,80)
    xalign 0.5

screen meme_screen():
    style_prefix "memescr"

    $ memepage = renpy.random.randint(1, 24)

    if memepage == 1:
        add "Meme01.png"
        $ timeofdaycounter += 1
    elif memepage == 2:
        add "Meme02.png"
        $ timeofdaycounter += 1
    elif memepage == 3:
        add "Meme03.png"
        $ timeofdaycounter += 1
    elif memepage == 4:
        add "Meme04.png"
        $ timeofdaycounter += 1
    elif memepage == 5:
        add "Meme05.webp"
        $ timeofdaycounter += 1
    elif memepage == 6:
        add "Meme06.webp"
        $ timeofdaycounter += 1
    elif memepage == 7:
        add "Meme07.webp"
        $ timeofdaycounter += 1
    elif memepage == 8:
        add "Meme08.webp"
        $ timeofdaycounter += 1
    elif memepage == 9:
        add "Meme09.webp"
        $ timeofdaycounter += 1
    elif memepage == 10:
        add "Meme10.webp"
        $ timeofdaycounter += 1
    elif memepage == 11:
        add "Meme11.webp"
        $ timeofdaycounter += 1
    elif memepage == 12:
        add "Meme12.webp"
        $ timeofdaycounter += 1
    elif memepage == 13:
        add "Meme13.webp"
        $ timeofdaycounter += 1
    elif memepage == 14:
        add "Meme14.webp"
        $ timeofdaycounter += 1
    elif memepage == 15:
        add "Meme15.webp"
        $ timeofdaycounter += 1
    elif memepage == 16:
        add "Meme16.webp"
        $ timeofdaycounter += 1
    elif memepage == 17:
        add "Meme17.webp"
        $ timeofdaycounter += 1
    elif memepage == 18:
        add "Meme18.webp"
        $ timeofdaycounter += 1
    elif memepage == 19:
        add "Meme19.webp"
        $ timeofdaycounter += 1
    elif memepage == 20:
        add "Meme20.webp"
        $ timeofdaycounter += 1
    elif memepage == 21:
        add "Meme21.webp"
        $ timeofdaycounter += 1
    elif memepage == 22:
        add "Meme22.webp"
        $ timeofdaycounter += 1
    elif memepage == 23:
        add "Meme23.webp"
        $ timeofdaycounter += 1
    elif memepage == 24:
        add "Meme24.webp"
        $ timeofdaycounter += 1
    elif memepage == 25:
        add "Meme25.webp"
        $ timeofdaycounter += 1
    elif memepage == 26:
        add "Meme26.webp"
        $ timeofdaycounter += 1
    elif memepage == 27:
        add "Meme27.webp"
        $ timeofdaycounter += 1
    else:
        add "Meme28.webp"
        $ timeofdaycounter += 1
    modal True

    textbutton "{color=#ff0000}Return{/color}":
        action Hide("meme_screen")
        xalign 0.5
        yalign 0.9
        text_size 30
