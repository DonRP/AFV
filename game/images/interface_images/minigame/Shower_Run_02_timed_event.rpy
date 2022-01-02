image Bar_b = "images/interface_images/minigame/Bar_body.webp"
image Bar_s = "images/interface_images/minigame/Bar_slider.webp"
image poster_button_idle = im.Scale("images/interface_images/minigame/event_run_build_icon.png", 100, 100)
image poster_button_hover = im.Scale("images/interface_images/minigame/event_run_build_icon_hover.png", 100, 100)
image bg Shower_Run02_start_game = "images/ShowerRun07.webp"
image bg Shower_Run02_game_img_1 = "images/ShowerRun07.webp"
image bg Shower_Run02_game_img_2 = "images/ShowerRun08.webp"
image bg Shower_Run02_game_win = "images/ShowerRun11.webp"
image bg Shower_Run02_game_lose = "images/ShowerRun05.webp"

init:
    python:
        bar_start_org = 400
        bar_start = bar_start_org
        bar_stop = 850
        Shower_Run02_game_1_win = 0
        Shower_Run02_game_2_win = 0
        Shower_Run02_timer = 0

    transform bar_move(bar_start):
        xpos bar_start
        ypos 650
#        linear 10 xpos 800

screen Shower_Run02_timed_event_1():
    modal True

    default bar_complete = False

############ INSURANCES ############

    key "game_menu" action NullAction()
    key "hide_windows" action NullAction()

############ BACKGROUND ############

    if Shower_Run02_game_1_win == 0:
        add "bg Shower_Run02_game_img_1"
    elif Shower_Run02_game_1_win == 1:
        add "bg Shower_Run02_game_img_2"

############ TIMER ############

    if Shower_Run02_timer >0.1:
        timer 0.1 action [ If( Shower_Run02_timer > 0.1,
            SetVariable("Shower_Run02_timer", Shower_Run02_timer - 0.1),
            [ Function(renpy.block_rollback),
                SetVariable("Shower_Run02_game_1_win", 2),
                Hide("Shower_Run02_timed_event_1"),
                Jump("Shower_Run02_game_end_lbl") ] ) ] repeat True

    if Shower_Run02_timer > 3:
        vbox  xalign 0.54 yalign 0.014 spacing 20:
            frame:
                style "text_frame"
                text str("{size=+20}Time:{color=#00ff00} [Shower_Run02_timer]{/color}{/size}")

    if Shower_Run02_timer < 3 and Shower_Run02_timer > 0.1:
        timer 1.9 action [Play ("memory_game_m", "music/card_lose.wav")]
        vbox  xalign 0.54 yalign 0.014 spacing 20:
            frame:
                style "text_frame"
                text str("{size=+20}Time:{color=#00ff00} [Shower_Run02_timer]{/color}{/size}") at timer_animation

    elif Shower_Run02_timer < 0.1:
        timer 0.1 action [ Function(renpy.block_rollback),
            SetVariable("Shower_Run02_game_1_win", 2),
            Hide("Shower_Run02_timed_event_1"),
            Jump("Shower_Run02_game_end_lbl") ]
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

    if Shower_Run02_game_1_win == 0:
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
            [ If(Shower_Run02_game_1_win == 0,
                SetVariable("Shower_Run02_game_1_win", 1),
                [ If(Shower_Run02_game_1_win == 1,
                    SetVariable("Shower_Run02_game_2_win", 1))]),
                Hide("Shower_Run02_timed_event_1"),
                Jump("Shower_Run02_game_end_lbl") ],
            [ If(Shower_Run02_game_1_win == 0 and Shower_Run02_game_1_win != 2,
                SetVariable("Shower_Run02_game_1_win", 2),
                [ If(Shower_Run02_game_1_win == 1,
                    SetVariable("Shower_Run02_game_2_win", 2))]),
                Hide("Shower_Run02_timed_event_1"),
                Jump("Shower_Run02_game_end_lbl") ] ) ]

label Shower_Run02_game_start_lbl:
    scene bg Shower_Run02_start_game
    with dissolve
    if not first_shower_run02:
        RT "{i}Ok... Don't panic!... I've just got to sneak past them too.{/i}"
        RT "{i}And maybe sneak a peek of those fabulous tits as I go by.{/i}"
    else:
        RT "{i}I've got it this time.{/i}"
        RT "{i}At least I get to sneak another peek.{/i}"
    $ bar_start = bar_start_org
    $ Shower_Run02_game_1_win = 0
    $ Shower_Run02_game_2_win = 0
    $ Shower_Run02_timer = 8
    call screen Shower_Run02_timed_event_1

label Shower_Run02_game_end_lbl:
    if Shower_Run02_game_1_win == 1 and Shower_Run02_game_2_win == 1:
        scene bg Shower_Run02_game_win
        with dissolve
        $ renpy.pause ()
        if not first_shower_run02:
            RT "{i}I made it!{/i}"
            RT "{i}Damnit!... Not the swim team, too!{/i}"
            $ first_shower_run02 = True
        else:
            RT "{i}I made it!{/i}"
            RT "{i}Damnit!... The swim team again? I've got the worst luck!{/i}"
        jump Shower_Run03_game_start_lbl
    elif Shower_Run02_game_1_win == 1 and Shower_Run02_game_2_win == 0:
        scene bg Shower_Run02_game_img_2
        with dissolve
        RT "{i}Ok, just a little further and I can turn right.{/i}"
        $ bar_start = bar_start_org
        $ Shower_Run02_timer = 6
        call screen Shower_Run02_timed_event_1
    elif Shower_Run02_game_1_win == 2 or Shower_Run02_game_2_win == 2:
        $ renpy.block_rollback ()
        scene bg Shower_Run02_game_lose
        with dissolve
        R "Goddammit!"
        $ shower_fail_counter = 2
        jump bad_shower_caught
