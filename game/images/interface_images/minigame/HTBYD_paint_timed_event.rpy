image Bar_b = "images/interface_images/minigame/Bar_body.webp"
image Bar_s = "images/interface_images/minigame/Bar_slider.webp"
image poster_button_idle = im.Scale("images/interface_images/minigame/event_poster_build_icon.png", 100, 100)
image poster_button_hover = im.Scale("images/interface_images/minigame/event_poster_build_icon_hover.png", 100, 100)
image bg HTBYD_start_game = "images/interface_images/minigame/HTBYD/PaintPoster06.webp"
image bg HTBYD_game_img_1 = "images/interface_images/minigame/HTBYD/PaintPoster07.webp"
image bg HTBYD_game_img_2 = "images/interface_images/minigame/HTBYD/PaintPoster08.webp"
image bg HTBYD_game_win = "images/interface_images/minigame/HTBYD/PaintPoster09.webp"
image bg HTBYD_game_lose = "images/interface_images/minigame/HTBYD/PaintPoster10.webp"

init:
    python:
        bar_start_org = 400
        bar_start = bar_start_org
        bar_stop = 850
        HTBYD_game_1_win = 0
        HTBYD_game_2_win = 0
        HTBYD_timer = 0

    transform bar_move(bar_start):
        xpos bar_start
        ypos 650
#        linear 10 xpos 800

screen HTBYD_timed_event_1():
    modal True

    default bar_complete = False

############ INSURANCES ############

    key "game_menu" action NullAction()
    key "hide_windows" action NullAction()

############ BACKGROUND ############

    if HTBYD_game_1_win == 0:
        add "bg HTBYD_game_img_1"
    elif HTBYD_game_1_win == 1:
        add "bg HTBYD_game_img_2"

############ TIMER ############

    if HTBYD_timer >0.1:
        timer 0.1 action [ If( HTBYD_timer > 0.1,
            SetVariable("HTBYD_timer", HTBYD_timer - 0.1),
            [ Function(renpy.block_rollback),
                SetVariable("HTBYD_game_1_win", 2),
                Hide("HTBYD_timed_event_1"),
                Jump("HTBYD_game_end_lbl") ] ) ] repeat True

    if HTBYD_timer > 3:
        vbox  xalign 0.54 yalign 0.014 spacing 20:
            frame:
                style "text_frame"
                text str("{size=+20}Time:{color=#00ff00} [HTBYD_timer]{/color}{/size}")

    if HTBYD_timer < 3 and HTBYD_timer > 0.1:
        timer 1.9 action [Play ("memory_game_m", "music/card_lose.wav")]
        vbox  xalign 0.54 yalign 0.014 spacing 20:
            frame:
                style "text_frame"
                text str("{size=+20}Time:{color=#00ff00} [HTBYD_timer]{/color}{/size}") at timer_animation

    elif HTBYD_timer < 0.1:
        timer 0.1 action [ Function(renpy.block_rollback),
            SetVariable("HTBYD_game_1_win", 2),
            Hide("HTBYD_timed_event_1"),
            Jump("HTBYD_game_end_lbl") ]
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

    if HTBYD_game_1_win == 0:
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
            [ If(HTBYD_game_1_win == 0,
                SetVariable("HTBYD_game_1_win", 1),
                [ If(HTBYD_game_1_win == 1,
                    SetVariable("HTBYD_game_2_win", 1))]),
                Hide("HTBYD_timed_event_1"),
                Jump("HTBYD_game_end_lbl") ],
            [ If(HTBYD_game_1_win == 0 and HTBYD_game_1_win != 2,
                SetVariable("HTBYD_game_1_win", 2),
                [ If(HTBYD_game_1_win == 1,
                    SetVariable("HTBYD_game_2_win", 2))]),
                Hide("HTBYD_timed_event_1"),
                Jump("HTBYD_game_end_lbl") ] ) ]

label HTBYD_game_start_lbl:
    scene bg HTBYD_start_game
    with fade
    if not first_poster:
        MS "That's the picture of Lauren you're going to use?"
        R "Yeah, do you like it?"
        MS "I'm... It's... Well..."
        MS "Is Lauren ok with this?"
        R "It was mostly her idea."
        RT "{i}With a lot of coaxing.{/i}"
        MST "{i}Oh my God!... That will get the attention of all the students for sure.  These kids are bringing their \"A game\"{/i}"
        MST "{i}It's also useful to know that [ryan] and Lauren are anything but prudes.{/i}"
        MS "Lauren looks a lot like the girl in that movie \"How to Breed your Dragon.\", only with much fewer... clothes on... What's her name?... Assturd?"
        R "Yeah, that's exactly right."
        MS "Ok, good.  So you want the poster to reflect that with a proper background, and a proper slogan... So take a second to think about it."
        R "...."
        R "Ok... I think I've got an idea."
        MS "Ok... Just let your creativity flow."
    else:
        MS "You still want to use that particular picture?"
        R "Yeah, why not?"
        MS "No reason."
        MST "{i}Unless you've got something even sexier.{/i}"
        MST "{i}I'm not even into women, but I can appreciate a beautiful young ass.{/i}"
        MS "Now, remember your theme."
        MS "Think of a good slogan..."
        MS "And let your creativity flow."
        R "Ok... I think I'm ready."
    $ bar_start = bar_start_org
    $ HTBYD_game_1_win = 0
    $ HTBYD_game_2_win = 0
    $ HTBYD_timer = 8
    call screen HTBYD_timed_event_1

label HTBYD_game_end_lbl:
    if HTBYD_game_1_win == 1 and HTBYD_game_2_win == 1:
        scene bg HTBYD_game_win
        with dissolve
        $ renpy.pause ()
        MS "Wow... That's really good."
        MST "{i}The slogan is a bit provocative, but it definitely goes with the flavor of the picture.{/i}"
        R "Yeah... I just did exactly what you said..."
        R "You're such a good art teacher!"
        MS "Ohhh... That's so sweet!"
        MS "Now, is that it, or did you say you need to design another poster?"
        R "I've got one more."
        MS "Ok, let's set it up."
        $ htbyd_poster = 1
        scene bg SleepBlack
        with fade
        jump ASS_Affect_game_start_lbl
    elif HTBYD_game_1_win == 1 and HTBYD_game_2_win == 0:
        scene bg HTBYD_game_img_2
        with dissolve
        MS "The background is looking nice, now bring it home with a creative slogan."
        R "Alright... I've got this."
        $ bar_start = bar_start_org
        $ HTBYD_timer = 6
        call screen HTBYD_timed_event_1
    elif HTBYD_game_1_win == 2 or HTBYD_game_2_win == 2:
        scene bg HTBYD_game_lose
        with dissolve
        MS "Oh... That's... Hmmm..."
        R "Well... That didn't end up the way I planned."
        R "But, I think nobody will really care since they will just be paying attention to the picture of Lauren."
        MS "Hmmm... Well, you may be right."
        MS "Now, is that it, or did you say you need to design another poster?"
        R "I've got one more."
        MS "Ok, let's set it up."
        $ poster_failed += 1
        $ htbyd_poster = 2
        scene bg SleepBlack
        with fade
        jump ASS_Affect_game_start_lbl
