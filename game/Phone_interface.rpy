define see_imagemaps = False

define close_casino_screens = [ "casinomap",
    "casinosidneymap",
    ### BlackJack ###
    "betBlackJack",
    ### BlackJack ###
    "startRoulette"
    ]

define close_phone_screens = [ "phone_interface",
    ### Event screens ###
    "event_screen",
    ### Gallery screens ###
    "phone_gallery",
    "phone_gallery_mom",
    "phone_gallery_Lauren",
    "phone_gallery_Sidney",
    "phone_gallery_Mandy",
    "phone_gallery_Aunt",
    ### Games screens ###
    "phone_games",
    ### Stats screens ###
    "stats_screen",
    "stats_screen_boys",
    ### Mod screens ###
    "ds",
    "items_mod",
    "week_day",
    "change_stats",
    "change_stats_Mom",
    "change_stats_Lauren",
    "change_stats_Sidney",
    "change_stats_Aunt",
    "change_stats_Cousin" ]

define screen_on = ""

define ryan_screens = [ "ryanmap",
    "ryanmapnight",
    "ryanwithsidneymap" ]

define lounge_screens = [ "loungemap",
    "loungemapnight",
    "sidneyloungemorningmap",
    "sidneyloungenightmap",
    "momcleanloungemap",
    "momcleanloungemap02",
    "momcleanloungemap03",
    "laurenponietvmap" ]

define bath_screens = [ "bathmap",
    "bathdoormap",
    "bathdoornightmap" ]#, "bathdoornightmap"

define kitchen_screens = [ "kitchenmap",
    "kitchenmapnight",
    "kitchenmapsleep",
    "sidneykitchenmap" ]

define mom_screens = [ "momsmap",
    "momsmapnight",
    "momdoormap",
    "momdoornightmap",
    "momsleepingnightmap" ]

define lauren_screens = [ "laurenmap",
    "laurenmapnight",
    "laurennightemptymap",
    "laurendoormap",
    "laurendoornightmap",
    "laurenmapsleepin",
    "sidneylaurennightmap",
    "sidneysleepinmap",
    "sidneylaurensleepingmap" ]

define city_screens = [ "citymapmap",
    "citymapmapnight" ]

define school_screens_all = [ "schoolhallmap",
    "classmap",
    "ntrclassmap",
    "schoolbathmap",
    "girlslockermap",
    "newclassmap",
    "newschoolhallmap",
    "newschoolbathmap",
    "newgirlslockermap",
    "asseffecthallmap",
    "badschoolhallmap",
    "bulbhallmap",
    "dragonhallmap",
    "goodhallmap",
    "matthallmap",
    "dresscodehallmap",
    "dresscodeclassmap",
    "campaignmap",
    "nocheerclassmap" ]

define school_screens = [ "schoolhallmap",
    "newschoolhallmap",
    "asseffecthallmap",
    "badschoolhallmap",
    "bulbhallmap",
    "dragonhallmap",
    "goodhallmap",
    "matthallmap",
    "campaignmap",
    "dresscodehallmap" ]

define class_screens = [ "classmap",
    "ntrclassmap",
    "newclassmap",
    "dresscodeclassmap",
    "nocheerclassmap" ]

define schoolbath_screens = [ "schoolbathmap",
    "newschoolbathmap" ]

define girlslocker_screens = [ "girlslockermap",
    "newgirlslockermap" ]

define campaign_screens = [ "campaignmap" ]

define nav_home_location = ryan_screens + lounge_screens + bath_screens + kitchen_screens + mom_screens + lauren_screens
define nav_school_location = school_screens_all

define nav_home_location_screens = [ "nav_house" ]
define nav_school_location_screens = [ "nav_school",
    "nav_new_school" ]

define all_screens = nav_home_location + nav_school_location

style inventory_label:
    xalign 0.2

style slot:
    background Frame("square", 0,0)
    minimum(80,80)
    maximum(80,80)
    xalign 0.5

style green_ntr:
    color "#1DDB16"
    hover_color "#E60000"
    outlines [(3, "#000", 0,0)]

style red_ntr:
    color "#E60000"
    hover_color "#1DDB16"
    outlines [(3, "#000", 0,0)]

screen phone_interface():
    style_prefix "phoneint"

    add "MobileScreen.png"
    modal True

    add "time_of_day" xpos .384 ypos .08

    add "day_of_week" xpos .443 ypos .43

    if persistent.mod_on:
        imagebutton at inv_eff:
            idle "images/interface_images/phone_screen_images/DSenterMod_idle.png"
            action [ Hide("phone_interface"), Show("ds") ]
            xalign 0.59
            yalign 0.13

    imagebutton auto "images/interface_images/phone_screen_images/Stats_%s.png":
        action [ Hide("phone_interface"), Show("stats_screen") ]
        xalign 0.42
        yalign 0.78

    imagebutton auto "images/interface_images/phone_screen_images/Progress_%s.png":
        action [ Hide("phone_interface"), Show("event_screen") ]
        xalign 0.57
        yalign 0.80

    imagebutton at inv_eff:
        idle "images/interface_images/phone_screen_images/Games.webp"
        action [ Hide("phone_interface"),
            Hide("Points_screen_Sidney"),
            Show("phone_games") ]
        xalign 0.495
        yalign 0.75
        focus_mask True

    imagebutton auto "images/interface_images/Pc_on_off_%s.png":
        action Hide("phone_interface")
        xalign 0.497
        yalign 0.91

    imagebutton at inv_eff:
        idle "images/interface_images/phone_screen_images/time_skip.png"
        xalign 0.58
        yalign 0.87
        focus_mask True
        if progress >= 4:
            if timeofdaycounter == 1:
                if not any([screen_on == "{}".format(k) for k in school_screens_all]):
                    action [ SetVariable("timeofdaycounter", 2), Hide("phone_interface"), Jump("memes_time_skip") ]
            elif timeofdaycounter == 2:
                if start_of_campaign and not campaign_finished and daycounter == 1:
                    action ui.callsinnewcontext ("campaign_warning")
                else:
                    action [ SetVariable("timeofdaycounter", 3), Hide("phone_interface"), Jump("memes_time_skip") ]
            elif timeofdaycounter == 3:
                action [ SetVariable("timeofdaycounter", 4), Hide("phone_interface"), Jump("memes_time_skip") ]
            elif timeofdaycounter == 4:
                if not any([screen_on == "{}".format(k) for k in school_screens_all]):
                    if daycounter == 6:
                        action ui.callsinnewcontext ("mafia_warning")
                    else:
                        action [ SetVariable("timeofdaycounter", 5), Hide("phone_interface"), Jump("memes_time_skip") ]
                else:
                    action ui.callsinnewcontext ("school_warning")
            elif timeofdaycounter == 5:
                if not any([screen_on == "{}".format(k) for k in school_screens_all]):
                    action ui.callsinnewcontext ("night_warning")#NullAction()
                else:
                    action ui.callsinnewcontext ("school_warning")
        else:
            action NullAction()

    imagebutton at inv_eff:
        idle "images/interface_images/phone_screen_images/folder_phone.png"
        action [ Hide("phone_interface"),
            Show("phone_gallery") ]
        xalign 0.42
        yalign 0.875
        #action NullAction()


    textbutton _(If( ntrcontent,
        "NTR route",
        "Loyalty route")):
        xalign 0.42
        yalign 0.075
        if not ntrcontent:
            text_style "red_ntr"
            action [ SetVariable("ntrcontent", True),
                SetVariable("firstntrblowjob", True),
                SetField(persistent, "gal_NTR_1", True) ]
        else:
            text_style "green_ntr"
            action [ SetVariable("ntrcontent", False),
                SetVariable("firstntrblowjob", False),
                SetField(persistent, "gal_NTR_1", False) ]

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

label mafia_warning:
    RT "{i}I can't waste time right now, the DeCapos will be here any minute.{/i}"

    return

label night_warning:
    RT "{i}It's night, I should go to sleep.{/i}"

    return

label school_warning:
    RT "{i}Right now I'm at School, I must first go home to advance time.{/i}"

    return

label campaign_warning:
    RT "{i}I can't waist time. I need to go to school and see how Lauren is doing in the student body election poll.{/i}"

    return

label memes_time_skip:

    hide screen Points_screen_Sidney

    scene bg BlurryWhite

    if progress >= 4:
        $ memepage = renpy.random.randint(1, 28)

        if memepage == 1:

            show Memes01
            with fade
            $ renpy.pause ()

        elif memepage == 2:

            show Memes02
            with fade
            $ renpy.pause ()

        elif memepage == 3:

            show Memes03
            with fade
            $ renpy.pause ()

        elif memepage == 4:

            show Memes04
            with fade
            $ renpy.pause ()

        elif memepage == 5:

            show Memes05
            with fade
            $ renpy.pause ()

        elif memepage == 6:

            show Memes06
            with fade
            $ renpy.pause ()

        elif memepage == 7:

            show Memes07
            with fade
            $ renpy.pause ()

        elif memepage == 8:

            show Memes08
            with fade
            $ renpy.pause ()

        elif memepage == 9:

            show Memes09
            with fade
            $ renpy.pause ()

        elif memepage == 10:

            show Memes10
            with fade
            $ renpy.pause ()

        elif memepage == 11:

            show Memes11
            with fade
            $ renpy.pause ()

        elif memepage == 12:

            show Memes12
            with fade
            $ renpy.pause ()

        elif memepage == 13:

            show Meme13
            with fade
            $ renpy.pause ()

        elif memepage == 14:

            show Meme14
            with fade
            $ renpy.pause ()

        elif memepage == 15:

            show Meme15
            with fade
            $ renpy.pause ()

        elif memepage == 16:

            show Meme16
            with fade
            $ renpy.pause ()

        elif memepage == 17:

            show Meme17
            with fade
            $ renpy.pause ()

        elif memepage == 18:

            show Meme18
            with fade
            $ renpy.pause ()

        elif memepage == 19:

            show Meme19
            with fade
            $ renpy.pause ()

        elif memepage == 20:

            show Meme20
            with fade
            $ renpy.pause ()

        elif memepage == 21:

            show Meme21
            with fade
            $ renpy.pause ()

        elif memepage == 22:

            show Meme22
            with fade
            $ renpy.pause ()

        elif memepage == 23:

            show Meme23
            with fade
            $ renpy.pause ()

        elif memepage == 24:

            show Meme24
            with fade
            $ renpy.pause ()

        elif memepage == 25:

            show Meme25
            with fade
            $ renpy.pause ()

        elif memepage == 26:

            show Meme26
            with fade
            $ renpy.pause ()

        elif memepage == 27:

            show Meme27
            with fade
            $ renpy.pause ()

        else:

            show Meme28
            with fade
            $ renpy.pause ()

    if any([screen_on == "{}".format(k) for k in ryan_screens]): # ryan_screens
        jump myroom
    elif any([screen_on == "{}".format(k) for k in lounge_screens]): # lounge_screens
        jump lounge
    elif any([screen_on == "{}".format(k) for k in bath_screens]): # bath_screens
        jump bath
    elif any([screen_on == "{}".format(k) for k in kitchen_screens]): # kitchen_screens
        jump kitchen
    elif any([screen_on == "{}".format(k) for k in mom_screens]): # mom_screens
        jump momroom
    elif any([screen_on == "{}".format(k) for k in lauren_screens]): # lauren_screens
        jump laurenroom
    elif any([screen_on == "{}".format(k) for k in school_screens]): # school_screens
        if timeofdaycounter <= 3:
            jump school
        else:
            RT "{i}School has ended, I must return home.{/i}"
            jump myroom
    elif any([screen_on == "{}".format(k) for k in class_screens]): # class_screens
        if timeofdaycounter <= 3 and start_of_campaign:
            jump new_classroom
        elif timeofdaycounter <= 3:
            jump classroom
        else:
            RT "{i}School has ended, I must return home.{/i}"
            jump myroom
    elif any([screen_on == "{}".format(k) for k in schoolbath_screens]): # schoolbath_screens
        if timeofdaycounter <= 3:
            jump schoolbathroom
        else:
            RT "{i}School has ended, I must return home.{/i}"
            jump myroom
    elif any([screen_on == "{}".format(k) for k in girlslocker_screens]): # girlslocker_screens
        if timeofdaycounter <= 3:
            jump girlslockers
        else:
            RT "{i}School has ended, I must return home.{/i}"
            jump myroom
    elif any([screen_on == "{}".format(k) for k in city_screens]): # city_screens
        if timeofdaycounter <=4:
            $ screen_on = "citymapmap"
            call screen citymapmap
        else:
            $ screen_on = "citymapmapnight"
            call screen citymapmapnight
    elif any([screen_on == "{}".format(k) for k in campaign_screens]): # campaign_screens
        if timeofdaycounter <= 3:
            jump campaign_headquarters
        else:
            RT "{i}School has ended, I must return home.{/i}"
            jump myroom

    #return
