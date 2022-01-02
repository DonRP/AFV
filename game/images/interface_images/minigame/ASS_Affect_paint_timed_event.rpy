image Bar_b = "images/interface_images/minigame/Bar_body.webp"
image Bar_s = "images/interface_images/minigame/Bar_slider.webp"
image poster_button_idle = im.Scale("images/interface_images/minigame/event_poster_build_icon.png", 100, 100)
image poster_button_hover = im.Scale("images/interface_images/minigame/event_poster_build_icon_hover.png", 100, 100)
image bg ASS_Affect_start_game = "images/interface_images/minigame/ASS Affect/PaintPoster01.webp"
image bg ASS_Affect_game_img_1 = "images/interface_images/minigame/ASS Affect/PaintPoster02.webp"
image bg ASS_Affect_game_img_2 = "images/interface_images/minigame/ASS Affect/PaintPoster03.webp"
image bg ASS_Affect_game_win = "images/interface_images/minigame/ASS Affect/PaintPoster04.webp"
image bg ASS_Affect_game_lose = "images/interface_images/minigame/ASS Affect/PaintPoster05.webp"

init:
    python:
        bar_start_org = 400
        bar_start = bar_start_org
        bar_stop = 850
        ASS_Affect_game_1_win = 0
        ASS_Affect_game_2_win = 0
        ASS_Affect_timer = 0

    transform bar_move(bar_start):
        xpos bar_start
        ypos 650
#        linear 10 xpos 800

screen ASS_Affect_timed_event_1():
    modal True

    default bar_complete = False

############ INSURANCES ############

    key "game_menu" action NullAction()
    key "hide_windows" action NullAction()

############ BACKGROUND ############

    if ASS_Affect_game_1_win == 0:
        add "bg ASS_Affect_game_img_1"
    elif ASS_Affect_game_1_win == 1:
        add "bg ASS_Affect_game_img_2"

############ TIMER ############

    if ASS_Affect_timer >0.1:
        timer 0.1 action [ If( ASS_Affect_timer > 0.1,
            SetVariable("ASS_Affect_timer", ASS_Affect_timer - 0.1),
            [ Function(renpy.block_rollback),
                SetVariable("ASS_Affect_game_1_win", 2),
                Hide("ASS_Affect_timed_event_1"),
                Jump("ASS_Affect_game_end_lbl") ] ) ] repeat True

    if ASS_Affect_timer > 3:
        vbox  xalign 0.54 yalign 0.014 spacing 20:
            frame:
                style "text_frame"
                text str("{size=+20}Time:{color=#00ff00} [ASS_Affect_timer]{/color}{/size}")

    if ASS_Affect_timer < 3 and ASS_Affect_timer > 0.1:
        timer 1.9 action [Play ("memory_game_m", "music/card_lose.wav")]
        vbox  xalign 0.54 yalign 0.014 spacing 20:
            frame:
                style "text_frame"
                text str("{size=+20}Time:{color=#00ff00} [ASS_Affect_timer]{/color}{/size}") at timer_animation

    elif ASS_Affect_timer < 0.1:
        timer 0.1 action [ Function(renpy.block_rollback),
            SetVariable("ASS_Affect_game_1_win", 2),
            Hide("ASS_Affect_timed_event_1"),
            Jump("ASS_Affect_game_end_lbl") ]
        text str("{size=+20}{color=#f00}0{/color}{/size}") xalign 0.54 yalign 0.014

############ MOVING BAR ############

    add "Bar_b" xpos 400 ypos 650
    add "Bar_s" at bar_move(bar_start)

#    vbox:
#        xalign 0.5
#        yalign 0.01
#        frame:
#            style "text_frame"
#            text "{size=+6}[bar_start]{/size}"

    if bar_start >= bar_stop:
        $ bar_complete = True
    elif bar_start <= bar_start_org:
        $ bar_complete = False

    if ASS_Affect_game_1_win == 0:
        timer 0.02 repeat True action [ If( bar_start <= bar_stop - 10 and not bar_complete,
            SetVariable("bar_start", bar_start + 10),
            If(bar_start >= bar_start_org + 10 and bar_complete,
                SetVariable("bar_start", bar_start -10))) ]
    else:
        timer 0.02 repeat True action [ If( bar_start <= bar_stop - 15 and not bar_complete,
            SetVariable("bar_start", bar_start + 15),
            If(bar_start >= bar_start_org + 15 and bar_complete,
                SetVariable("bar_start", bar_start -15))) ]

############ BUTTON ############

    imagebutton:
        xpos 570
        ypos 530
        focus_mask True
        idle ("poster_button_idle")
        hover ("poster_button_hover")
        action [ If( bar_start >= 565 and bar_start <= 680,
            [ If(ASS_Affect_game_1_win == 0,
                SetVariable("ASS_Affect_game_1_win", 1),
                [ If(ASS_Affect_game_1_win == 1,
                    SetVariable("ASS_Affect_game_2_win", 1))]),
                Hide("ASS_Affect_timed_event_1"),
                Jump("ASS_Affect_game_end_lbl") ],
            [ If(ASS_Affect_game_1_win == 0 and ASS_Affect_game_1_win != 2,
                SetVariable("ASS_Affect_game_1_win", 2),
                [ If(ASS_Affect_game_1_win == 1,
                    SetVariable("ASS_Affect_game_2_win", 2))]),
                Hide("ASS_Affect_timed_event_1"),
                Jump("ASS_Affect_game_end_lbl") ] ) ]

label ASS_Affect_game_start_lbl:
    scene bg ASS_Affect_start_game
    with fade
    if not first_poster:
        MS "Oh... I see Lauren is in a similar pose for this picture too."
        MS "She is very photogenic from that angle."
        R "Yeah, what she lacks in the bra, she makes up for in the trunk."
        MS "Haha... [ryan]..."
        R "Oh, right... I shouldn't talk like that in school, sorry."
        MS "Uh huh... And who is Lauren supposed to be in this picture?"
        R "Well, she's supposed to be Penny Roberson from \"Missing in Space\", but she could pass for any number of sci-fi girls."
        MS "Ok, great... So remember, think of a theme, a background, and a slogan."
        R "...."
        R "Ok, I think I've got an idea."
    else:
        MS "Ok, let's see if you can do any better this time."
        MS "Now, remember your theme."
        MS "Think of a good slogan..."
        MS "And let your creativity flow."
        R "Ok... I think I'm ready."
    $ bar_start = bar_start_org
    $ ASS_Affect_game_1_win = 0
    $ ASS_Affect_game_2_win = 0
    $ ASS_Affect_timer = 8
    call screen ASS_Affect_timed_event_1

label ASS_Affect_game_end_lbl:
    if ASS_Affect_game_1_win == 1 and ASS_Affect_game_2_win == 1:
        scene bg ASS_Affect_game_win
        with dissolve
        $ renpy.pause ()
        if not first_me_poster:
            MS "It looks really good!"
            MS "What is \"Ass Affect\" referencing though?"
            R "It's a parody on the sci-fi video game \"Ass Effect\", but it's really effect with an \"e\"."
            MS "Oh... I think my nephew used to play that game."
            MS "That's a pretty clever play on words."
            $ first_me_poster = True
        else:
            MS "It looks really good!"
            MS "I'm not much for video games, but that poster makes me want to go try it."
            MS "Not to mention vote for Lauren, if I could."
        MS "Great job!"
        if htbyd_poster == 1:
            $ posters_good = True
            $ posters_complete = True
        if htbyd_poster == 2:
            $ posters_dragon = True
        $ htbyd_poster = 0
        jump finished_painting
    elif ASS_Affect_game_1_win == 1 and ASS_Affect_game_2_win == 0:
        scene bg ASS_Affect_game_img_2
        with dissolve
        MS "The background is looking nice, now bring it home with a creative slogan."
        R "Alright... I've got this."
        $ bar_start = bar_start_org
        $ ASS_Affect_timer = 6
        call screen ASS_Affect_timed_event_1
    elif ASS_Affect_game_1_win == 2 or ASS_Affect_game_2_win == 2:
        scene bg ASS_Affect_game_lose
        with dissolve
        MS "Oh... That's... Hmmm..."
        R "Well... That didn't end up the way I planned."
        R "But, I think nobody will really care since they will just be paying attention to the picture of Lauren."
        MS "Hmmm... Well, you may be right."
        $ poster_failed += 1
        if htbyd_poster == 1:
            $ posters_me = True
        if htbyd_poster == 2:
            $ posters_bad = True
        $ htbyd_poster = 0
        jump finished_painting
