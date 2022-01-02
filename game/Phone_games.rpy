
####################################################################################################################################################
### Powerd by D.S.-sama ############################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

####################################################################################################################################################
### Styles

style phone_games_text_style:
    size 20
    #bold True
    color "#888888" #00589E # E60000
    hover_color "#c184ff"
    outlines [(3, "#000", 0,0)]

####################################################################################################################################################
### Main phone gallery screen

screen phone_games():

    style_prefix "phone_games"

    add "MobileScreen.png"
    modal True

    frame xalign .495 yalign .13:# at truecenter:
        background None
        has vbox

        text _("{image=images/interface_images/phone_screen_images/Games_small.webp} Games") style "phone_games_text_style" size 25 at center

        text _("") size 50

        hbox:
            xalign .1
            imagebutton at inv_eff:
                idle "images/interface_images/Memory_game/Brain_games.webp"
#                hovered Show("displayTextScreen", displayText = "Braine games!")
                action [ Play("sound", "music/mouse_click.mp3"),
                    Hide("{}".format(k) for k in all_screens),
                    Hide("phone_games"),
                    Hide("displayTextScreen"),
                    Jump("memory_game_label") ]
#                unhovered Hide("displayTextScreen")

        hbox:
            xalign .1
            text ""

#        hbox:
#            xalign 5
#            imagebutton at inv_eff:
#                idle "images/interface_images/blackjack/bj_icon.png"
##                hovered Show("displayTextScreen", displayText = "Braine games!")
#                action [ Play("sound", "music/mouse_click.mp3"),
#                    Hide("{}".format(k) for k in all_screens),
#                    Hide("phone_games"),
#                    Hide("displayTextScreen"),
#                    Show("betBlackJack", transition=Dissolve(1.0)) ]
##                unhovered Hide("displayTextScreen")

#            imagebutton at inv_eff:
#                idle "rouletteIcon"
##                hovered Show("displayTextScreen", displayText = "Braine games!")
#                action [ Play("sound", "music/mouse_click.mp3"),
#                    Hide("{}".format(k) for k in all_screens),
#                    Hide("phone_games"),
#                    Hide("displayTextScreen"),
#                    Show("startRoulette", transition=Dissolve(1.0)) ]
##                unhovered Hide("displayTextScreen")

    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("phone_games"), Show("phone_interface") ]
        xalign 0.495
        yalign 0.91

    imagebutton:
        xalign 0.6345
        yalign 0.15
        idle "phoneExitIdle"
        hover "phoneExitHover"
        if persistent.mod_on:
            action [ [ Hide("{}".format(k)) for k in close_phone_screens ],
                [ SetVariable("stats_var{}".format(k), False) for k in list_girl_characters ],
                SetVariable("items_var", False),
                SetVariable("week_day_var", False) ]
        else:
            action [ Hide("{}".format(k)) for k in close_phone_screens ]
