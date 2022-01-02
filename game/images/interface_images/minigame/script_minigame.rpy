image Bar_b = "images/interface_images/minigame/Bar_body.webp"
image Bar_s = "images/interface_images/minigame/Bar_slider.webp"

init:
    python:
        bar_start_org = 400
        bar_start = bar_start_org
        bar_stop = 850
#        bar_complete = False

    #to test ------------------------------------------
        config.underlay.append(
            renpy.Keymap(
                T = lambda: renpy.run(
                    [ Show("test_minigame"),
                        SetVariable("bar_start", bar_start_org) ]
                    )
                )
            )
        
    transform bar_move(bar_start):
        xpos bar_start 
        ypos 650
#        linear 10 xpos 800
        
screen test_minigame():
    modal True
    
    default bar_complete = False
    
    add "Bar_b" xpos 400 ypos 650
    add "Bar_s" at bar_move(bar_start)
    
    vbox:
        xalign 0.5
        yalign 0.01
        frame:
            style "text_frame"
            text "{size=+6}[bar_start]{/size}"
    
    if bar_start >= bar_stop:
        $ bar_complete = True
    elif bar_start <= bar_start_org:
        $ bar_complete = False
    
    timer 0.02 repeat True action [ If( bar_start <= bar_stop - 5 and not bar_complete,
        SetVariable("bar_start", bar_start + 5),
        If(bar_start >= bar_start_org + 5 and bar_complete,
            SetVariable("bar_start", bar_start -5))) ]
    
#    timer 0.025 repeat True action [ If( bar_start >= 850,
#        SetVariable("bar_complete", False),
#        If( bar_start <= 400,
#            SetVariable("bar_complete", True))),
#        If( bar_start <= 845 and not bar_complete,
#            SetVariable("bar_start", bar_start + 5),
#            If(bar_start >= 405 and bar_complete,
#                SetVariable("bar_start", bar_start -5))) ]

    imagebutton:
        xpos 570
        ypos 530
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        action [ If( bar_start >= 565 and bar_start <= 680,
            [ Hide("test_minigame"), 
                Show("test_minigame_win") ],
            [ Hide("test_minigame"),
                Show("test_minigame_lose") ] ) ]

#            NullAction()

screen test_minigame_win():
    default win_timer_2 = ("#%06x" % renpy.random.randint(0, 0xFFFFFF)) #"#34f500"
    
    timer 0.5 repeat True:
        action [SetScreenVariable('win_timer_2', ("#%06x" % renpy.random.randint(0, 0xFFFFFF)))]

    key "hide_windows" action NullAction()
    text str(_("YOU WON!!!")) style "text_win_lose" color win_timer_2 at win_animation
    
    timer 3.0 action [ Hide("test_minigame_win"),
        Jump("map_location") ]
    
screen test_minigame_lose():
    
    key "hide_windows" action NullAction()
    text _("You lose!") style "text_win_lose" 
    
    timer 3.0 action [ Hide("test_minigame_lose"),
        Jump("map_location") ]
