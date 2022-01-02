
####################################################################################################################################################
### Powerd by D.S.-sama ############################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

####################################################################################################################################################
### Inventory variable
####################################################################################################################################################
define see_imagemaps = False
####################################################################################################################################################
### Mod variable
####################################################################################################################################################
define persistent.mod_on = True
####################################################################################################################################################
### Mod variables

define gal_name_var = [ "mom",
    "Lauren",
    "Sidney",
    "Lauren",
    "auntie",
    "harem",
    "other_girls",
    "NTR",
    "Cosplay",
    "Mandy"
    ]


init 1:
    python:
#        my_dad = "Dad"
        def ItemCheatAlert():
            renpy.notify("You can't add any more!")

    $ day = ""

    $ mod_version = "0.1.2"
    $ game_version = "0.07"
    $ game_subversion = "_extended"
    $ game_versions_allowed_for_mod = [ str(game_version+game_subversion) ]
#    $ game_vtest = str(game_versions_allowed_for_mod) + "_supporter"
    $ devMod = False

    $ mod_show = False
    $ mod_dev = False
    $ mod_love = True
    $ label_see = False
    $ items_var = False
    $ events_var = False
    $ week_day_var = False

    $ logo_show = True

    $ close_stats_vars = [ "", "_Mom", "_Lauren", "_Sidney", "_Aunt", "_Cousin" ]
    $ list_girl_characters = [ "", "_Mom", "_Lauren", "_Sidney", "_Aunt", "_Cousin" ]

    $ stats_var = False #For girls stats
    $ stats_var_Mom = False
    $ stats_var_Lauren = False
    $ stats_var_Sidney = False
    $ stats_var_Aunt = False
    $ stats_var_Cousin = False

init 1000 python:
    #To be able to delete a file-------------
    import shutil
    import os
    import os.path
    import sys

    #to enable consoles-----------------------
    #config.developer = True
    config.console = True

    #to be able to advance/regress time-------
    config.underlay.append(
        renpy.Keymap(
            M = lambda: renpy.run(
                If(timeofdaycounter < 5,
                    [ Hide("ds"),
                        Hide("phone_interface"),
                        SetVariable("timeofdaycounter", timeofdaycounter + 1),
                        Jump("adv_rest_jump") ],
                    [ Hide("ds"),
                        Hide("phone_interface"),
                        Jump("adv_rest_jump") ]
                    )
                )
            )
        )

    config.underlay.append(
        renpy.Keymap(
            N = lambda: renpy.run(
                If((timeofdaycounter > 1) and (timeofdaycounter <= 5),
                    [ Hide("ds"),
                        Hide("phone_interface"),
                        SetVariable("timeofdaycounter", timeofdaycounter - 1),
                        Jump("adv_rest_jump") ],
                    [ Hide("ds"),
                        Hide("phone_interface"),
                        Jump("adv_rest_jump") ]
                    )
                )
            )
        )

    #to be able to reload---------------------
    config.underlay.append(
        renpy.Keymap(
            r = lambda: renpy.run(
                Function(renpy.reload_script
                    )
                )
            )
        )

    #label overrides--------------------------
#    if not persistent.patchFile_i_on:
#        config.label_overrides = {
#            k : "mod_{}".format(k)
#            for k in [
#                k for k in renpy.get_all_labels()
#                if renpy.has_label( "mod_{}".format(k) ) ] }

    #to be able to see_imagemaps--------------
    config.underlay.append(
        renpy.Keymap(
            I = lambda: renpy.run(
                If( see_imagemaps,
                    [ SetVariable("see_imagemaps", False) ],
                    [ SetVariable("see_imagemaps", True) ]
                    )
                )
            )
        )

####################################################################################################################################################
### For label callback

    return_label = ""

    def label_callback(name, abnormal):
        store.current_label = name

    config.label_callback = label_callback


    config.console = True

####################################################################################################################################################
### Callback label

screen lbl_see():
    frame:
        xalign 0.01 yalign 0.05
        vbox:
            text _("label name: [store.current_label]")
            textbutton _("iPatch: [persistent.patreonsafe]"):
                action If(persistent.patreonsafe,
                    [ SetField(persistent, "patreonsafe", False),
                        SetVariable("Mom", "Mom"),
                        SetVariable("mom", "mom"),
                        SetVariable("Dad", "Dad"),
                        SetVariable("dad", "dad"),
                        SetVariable("uncle", "uncle " + uncle_name),
                        SetVariable("Uncle", "Uncle " + uncle_name),
                        SetVariable("Auntie", "Aunt " + auntie_name_short),
                        SetVariable("auntie", "aunt " + auntie_name_short),
                        SetVariable("Auntie_2", "Aunt "),
                        SetVariable("auntie_2", "aunt ") ],
                    [ SetField(persistent, "patreonsafe", True),
                        SetVariable("Mom", mom_name),
                        SetVariable("mom", mom_name),
                        SetVariable("Dad", dad_name),
                        SetVariable("dad", dad_name),
                        SetVariable("uncle", uncle_name),
                        SetVariable("Uncle", uncle_name),
                        SetVariable("Auntie", auntie_name),
                        SetVariable("auntie", auntie_name),
                        SetVariable("Auntie_2", ""),
                        SetVariable("auntie_2", "") ])

####################################################################################################################################################
### Phone interface screen
####################################################################################################################################################

init 999 screen phone_interface():
    style_prefix "phoneint"

    add "MobileScreen.png"
    modal True


    key "ctrl_alt_K_z":
        action ToggleScreen("lbl_see")

    if persistent.patch_on:
        #my imagebuttons
        imagebutton xalign 0.579 yalign 0.0261:
            if not persistent.patreonsafe:
                idle ("images/interface_images/phone_screen_images/Led_idle.png")
                hover ("images/interface_images/phone_screen_images/Led_red_hover.png")
                action [ SetField(persistent, "patreonsafe", True),#SetField(persistent, "patch_enabled", False),
                    SetVariable("Mom", mom_name),
                    SetVariable("mom", mom_name),
                    SetVariable("Dad", dad_name),
                    SetVariable("dad", dad_name),
                    SetVariable("uncle", uncle_name),
                    SetVariable("Uncle", uncle_name),
                    SetVariable("Auntie", auntie_name),
                    SetVariable("auntie", auntie_name),
                    SetVariable("Auntie_2", ""),
                    SetVariable("auntie_2", "")
                     #Hide("phone_interface")
                    ]

            elif persistent.patreonsafe:
                idle ("images/interface_images/phone_screen_images/Led_idle.png")
                hover ("images/interface_images/phone_screen_images/Led_green_hover.png")
                action [ SetField(persistent, "patreonsafe", False),#SetField(persistent, "patch_enabled", True),
                    SetVariable("Mom", "Mom"),
                    SetVariable("mom", "mom"),
                    SetVariable("Dad", "Dad"),
                    SetVariable("dad", "dad"),
                    SetVariable("uncle", "uncle " + uncle_name),
                    SetVariable("Uncle", "Uncle " + uncle_name),
                    SetVariable("Auntie", "Aunt " + auntie_name_short),
                    SetVariable("auntie", "aunt " + auntie_name_short),
                    SetVariable("Auntie_2", "Aunt "),
                    SetVariable("auntie_2", "aunt ")
                     #Hide("phone_interface")
                    ]

    add "time_of_day" xpos .384 ypos .08

    add "day_of_week" xpos .443 ypos .43

    if persistent.mod_on:
        imagebutton at inv_eff:
            idle "images/interface_images/phone_screen_images/DSenterMod_idle.png"
            if any([config.version != "{}_supporter".format(k) for k in game_versions_allowed_for_mod]):
            #if config.version != game_version_allowed_for_mod:
                action [ Hide("phone_interface"),
                    Jump("version_test")]
            else:
                action [ Hide("phone_interface"),
                    Show("ds")]
            xalign 0.59
            yalign 0.13


    imagebutton auto "images/interface_images/phone_screen_images/Stats_%s.png":
        action [ Hide("phone_interface"),
            Show("stats_screen") ]
        xalign 0.42
        yalign 0.78

    imagebutton auto "images/interface_images/phone_screen_images/Progress_%s.png":
        action [ Hide("phone_interface"),
            Show("event_screen") ]
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
                    action [ SetVariable("timeofdaycounter", 2),
                        Hide("phone_interface"),
                        Jump("memes_time_skip") ]
            elif timeofdaycounter == 2:
                action [ SetVariable("timeofdaycounter", 3),
                    Hide("phone_interface"),
                    Jump("memes_time_skip") ]
            elif timeofdaycounter == 3:
                action [ SetVariable("timeofdaycounter", 4),
                    Hide("phone_interface"),
                    Jump("memes_time_skip") ]
            elif timeofdaycounter == 4:
                if not any([screen_on == "{}".format(k) for k in school_screens_all]):
                    if daycounter == 6:
                        action ui.callsinnewcontext ("mafia_warning")
                    else:
                        action [ SetVariable("timeofdaycounter", 5),
                            Hide("phone_interface"),
                            Jump("memes_time_skip") ]
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
        action [ Hide("phone_interface"), Show("phone_gallery") ]
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

    if see_imagemaps:
        text _("[screen_on]"):
            xalign 0.1
            yalign 0.1


####################################################################################################################################################
### Define D.S.-sama character

define DS = Character("D.S.-sama", color="#1DDB16")

####################################################################################################################################################
### Styles

style ds_mod_style:
    bold True
    color "#00589E" # E60000
    hover_color "#c184ff"
    outlines [(3, "#000", 0,0)]

style ds_mod_style_red:
    bold True
    color "#E60000" # E60000
    hover_color "#c184ff"
    outlines [(3, "#000", 0,0)]

style ds_mod_style_nfo:
    bold True
    color "#1DDB16"
    hover_color "#c184ff"
    outlines [(3, "#000", 0,0)]

style ds_mod_style_close_button:
    size 25
    #bold True
    color "#00589E" # E60000
    hover_color "#E60000"
    outlines [(3, "#000", 0,0)]

style ds_mod_style_image_button:
    size 20
    #bold True
    color "#888888" #00589E # E60000
    hover_color "#c184ff"
    outlines [(3, "#000", 0,0)]

style ds_mod_style_important_button:
    size 25
    #bold True
    color "#E60000" # E60000
    hover_color "#04e5f9"
    outlines [(3, "#000", 0,0)]

####################################################################################################################################################
### Main mod screen
####################################################################################################################################################

screen ds():
    #style_prefix "stats"

    add "MobileScreen.png"
    modal True

    if persistent.patch_on:
        #my imagebuttons
        imagebutton xalign 0.579 yalign 0.0261:
            if not persistent.patreonsafe:
                idle ("images/interface_images/phone_screen_images/Led_idle.png")
                hover ("images/interface_images/phone_screen_images/Led_red_hover.png")
                action [ SetField(persistent, "patreonsafe", True),#SetField(persistent, "patch_enabled", False),
                    SetVariable("Mom", mom_name),
                    SetVariable("mom", mom_name),
                    SetVariable("Dad", dad_name),
                    SetVariable("dad", dad_name),
                    SetVariable("uncle", uncle_name),
                    SetVariable("Uncle", uncle_name),
                    SetVariable("Auntie", auntie_name),
                    SetVariable("auntie", auntie_name),
                    SetVariable("Auntie_2", ""),
                    SetVariable("auntie_2", "")
                     #Hide("phone_interface")
                    ]

            elif persistent.patreonsafe:
                idle ("images/interface_images/phone_screen_images/Led_idle.png")
                hover ("images/interface_images/phone_screen_images/Led_green_hover.png")
                action [ SetField(persistent, "patreonsafe", False),#SetField(persistent, "patch_enabled", True),
                    SetVariable("Mom", "Mom"),
                    SetVariable("mom", "mom"),
                    SetVariable("Dad", "Dad"),
                    SetVariable("dad", "dad"),
                    SetVariable("uncle", "uncle " + uncle_name),
                    SetVariable("Uncle", "Uncle " + uncle_name),
                    SetVariable("Auntie", "Aunt " + auntie_name_short),
                    SetVariable("auntie", "aunt " + auntie_name_short),
                    SetVariable("Auntie_2", "Aunt "),
                    SetVariable("auntie_2", "aunt ")
                     #Hide("phone_interface")
                    ]

    frame xalign 0.500 yalign 0.275:# at truecenter:
        background  "Mobile_event_Screen.png"
        has vbox

        textbutton _("Mod Info!") at center:
            text_style ("ds_mod_style_image_button")
            action ui.callsinnewcontext ("ds_mod_info")

        side ("c"):
            area (1,0,315,510)
            viewport id "ds_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:

                    #text _("") size 20

                    #text _("{color=#00589E}mod_incest--------------------------------------{/color}") outlines [(1.1, "#000000", 0, 0)]

                    #if not patreonsafe:
                    #    textbutton _("mod_incest: {color=#1DDB16}ON{/color}"):
                    #        text_style ("ds_mod_style_image_button")
                    #        action Hide("ds"), SetVariable("mod_show", False), SetField(persistent, "patreonsafe", True), Function(renpy.call, label="incest_mod")#, Function(renpy.reload_script) #SetVariable("patreonsafe", True)

                    #elif patreonsafe:
                    #    textbutton _("mod_incest: {color=#E60000}OFF{/color}"):
                    #        text_style ("ds_mod_style_image_button")
                    #        action Hide("ds"), SetVariable("mod_show", False), SetField(persistent, "patreonsafe", False), Function(renpy.call, label="incest_mod")# ui.callsinnewcontext ("mod_incest")#, Function(renpy.reload_script) #SetVariable("patreonsafe", False)

                    #if patch_on:
                    #    textbutton _("mod_incest: {color=#E60000}OFF{/color}"):
                    #        text_style ("ds_mod_style_image_button")
                    #        action ui.callsinnewcontext ("delete_files")

                    #if not patch_on:
                    #    textbutton _("mod_incest: {color=#1DDB16}ON{/color}"):
                    #        text_style ("ds_mod_style_image_button")
                    #        action ui.callsinnewcontext ("create_file")

                    #text _("") size 20

                    #text _("{color=#00589E}Hide_mod_logo----------------------------{/color}") outlines [(1.1, "#000000", 0, 0)]

                    #if logo_show == True:
                    #    textbutton _("Mod logo: {color=#1DDB16}ON{/color}"):# at center:
                    #        text_style ("ds_mod_style_image_button")
                    #        action [ SetVariable("logo_show", False) ]
                    #else:
                    #    textbutton _("Mod logo: {color=#E60000}OFF{/color}"):# at center:
                    #        text_style ("ds_mod_style_image_button")
                    #        action [ SetVariable("logo_show", True) ]

                    #text _("") size 9

                    text _("{color=#00589E}Name_changes------------------{/color}")

                    textbutton _("Change your name. \n{color=#1DDB16}(Current name is: [ryan]){/color}"):
                        text_style ("ds_mod_style_image_button")
                        action ui.callsinnewcontext ("ds_change_name_Ryan")

                    text _("") size 8

                    textbutton _(If( persistent.patreonsafe,
                        "Change Jacky's name. \n{color=#1DDB16}(Current name is: [mom_name]){/color}",
                        "Change Mom's name. \n{color=#1DDB16}(Current name is: [mom_name]){/color}")):
                        text_style ("ds_mod_style_image_button")
                        action ui.callsinnewcontext ("ds_change_name_mom")

                    text _("") size 8
                    text _("{color=#00589E}Points_and_items--------------{/color}") #outlines [(1.1, "#000000", 0, 0)]

                    textbutton _("{color=#1DDB16}Add{/color}/{color=#E60000}Remove{/color} items"):
                        text_style ("ds_mod_style_image_button")
                        if items_var == False and any( [ getattr(store, "stats_var{}".format(k), True) for k in close_stats_vars ] ):
                            action [ Hide("change_stats"),
                                [ Hide("change_stats{}".format(k)) for k in close_stats_vars ],
                                Show("items_mod"), SetVariable("stats_var", False),
                                [ SetVariable("stats_var{}".format(k), False) for k in close_stats_vars ],
                                SetVariable("items_var", True) ]
                        elif items_var == False and events_var == True:
                            action [ Hide("events_mod"),
                                Show("items_mod"),
                                SetVariable("events_var", False),
                                SetVariable("items_var", True) ]
                        elif items_var == False and  week_day_var == True:
                            action [ Hide("week_day"),
                                Show("items_mod"),
                                SetVariable("week_day_var", False),
                                SetVariable("items_var", True) ]
                        elif items_var == False and  stats_var == True:
                            action [ Hide("change_stats"),
                                Show("items_mod"),
                                SetVariable("stats_var", False),
                                SetVariable("items_var", True) ]
                        elif items_var == False:
                            action [ Show("items_mod"),
                                SetVariable("items_var", True) ]
                        elif items_var == True:
                            action [ Hide("items_mod"),
                                SetVariable("items_var", False) ]

                    textbutton _("Change girls stats"):
                        text_style ("ds_mod_style_image_button")
                        if stats_var == False and items_var == True:
                            action [ Hide("items_mod"),
                                Show("change_stats"),
                                SetVariable("items_var", False),
                                SetVariable("stats_var", True) ]
                        elif stats_var == False and events_var == True:
                            action [ Hide("events_mod"),
                                Show("change_stats"),
                                SetVariable("events_var", False),
                                SetVariable("stats_var", True) ]
                        elif stats_var == False and  week_day_var == True:
                            action [ Hide("week_day"),
                                Show("change_stats"),
                                SetVariable("week_day_var", False),
                                SetVariable("stats_var", True) ]
                        elif stats_var == False:
                            action [ Show("change_stats"),
                                SetVariable("stats_var", True) ]
                        elif any( [ getattr(store, "stats_var{}".format(k), True) for k in close_stats_vars ] ):
                            action [ [ SetVariable("stats_var{}".format(k), False) for k in close_stats_vars ],
                            [ Hide("change_stats{}".format(k)) for k in close_stats_vars ] ]
                        elif stats_var == True:
                            action [ Hide("change_stats"),
                                SetVariable("stats_var", False) ]

#                    if not renpy.loadable("D.S.Mod_v0.1d_AFamilyVenture-0.01b-pc/Gallery_mod/Gallery_AFV_v0.2.rpyc"):
#                        if renpy.loadable("D.S.Mod_v0.1d_AFamilyVenture-0.01b-pc/Event_Sceens.rpyc"):
#                            textbutton _("Events"):
#                                text_style ("ds_mod_style_image_button")
#                                if events_var == False and any( [ getattr(store, "stats_var{}".format(k), True) for k in close_stats_vars ] ):
#                                    action [ Hide("change_stats"),
#                                    [ Hide("change_stats{}".format(k)) for k in close_stats_vars ],
#                                    Show("events_mod"), SetVariable("stats_var", False),
#                                    [ SetVariable("stats_var{}".format(k), False) for k in close_stats_vars ],
#                                    SetVariable("events_var", True) ]
#                                elif events_var == False and  week_day_var == True:
#                                    action [ Hide("week_day"),
#                                        Show("events_mod"),
#                                        SetVariable("week_day_var", False),
#                                        SetVariable("events_var", True) ]
#                                elif events_var == False and  items_var == True:
#                                    action [ Hide("items_mod"),
#                                        Show("events_mod"),
#                                        SetVariable("items_var", False),
#                                        SetVariable("events_var", True) ]
#                                elif events_var == False and  stats_var == True:
#                                    action [ Hide("change_stats"),
#                                        Show("events_mod"),
#                                        SetVariable("stats_var", False),
#                                        SetVariable("events_var", True) ]
#                                elif events_var == False:
#                                    action [ Show("events_mod"),
#                                        SetVariable("events_var", True) ]
#                                elif events_var == True:
#                                    action [ Hide("events_mod"),
#                                        SetVariable("events_var", False) ]

#                    if renpy.loadable("D.S.Mod_v0.1d_AFamilyVenture-0.01b-pc/Gallery_mod/Gallery_AFV_v0.2.rpyc"):
#                         textbutton _("Gallery"):
#                            text_style ("ds_mod_style_image_button")
#                            action ShowMenu("gallery")

                    text _("") size 8

                    text _("{color=#00589E}Time:[timeofdaycounter]-----------------------------{/color}") #outlines [(1.1, "#000000", 0, 0)]

                    textbutton _(" Press to jump to the right\n                   time!"):
                        text_style ("ds_mod_style_image_button")
                        action [ Hide("ds"),
                            Hide("phone_interface"),
                            Jump("adv_rest_jump") ]

                    textbutton _("Advance Time"):
                        text_style ("ds_mod_style_image_button")
                        if timeofdaycounter < 5:
                            action SetVariable("timeofdaycounter", timeofdaycounter + 1)
#                            action [ SetVariable("timeofdaycounter", timeofdaycounter + 1),
#                                Hide("ds"),
#                                Hide("phone_interface"),
#                                Jump("adv_rest_jump") ]
                        elif timeofdaycounter == 5:
                            action NullAction()
#                            action [ Hide("ds"),  #NullAction()
#                                Hide("phone_interface"),
#                                Jump("adv_rest_jump") ]


                    textbutton _("Regress Time"):
                        text_style ("ds_mod_style_image_button")
                        if (timeofdaycounter > 1) and (timeofdaycounter <= 5):
                            action SetVariable("timeofdaycounter", timeofdaycounter - 1)
#                            action [ SetVariable("timeofdaycounter", timeofdaycounter - 1),
#                                Hide("ds"),
#                                Hide("phone_interface"),
#                                Jump("adv_rest_jump") ]
                        elif timeofdaycounter == 1:
                            action NullAction()
#                            action [ Hide("ds"),  #NullAction()
#                                Hide("phone_interface"),
#                                Jump("adv_rest_jump") ]

                    textbutton _("Set week day"):
                        text_style ("ds_mod_style_image_button")
                        if week_day_var == False and items_var == True:
                            action [ Hide("items_mod"),
                                Show("week_day"),
                                SetVariable("items_var", False),
                                SetVariable("week_day_var", True) ]
                        elif week_day_var == False and events_var == True:
                            action [ Hide("events_mod"),
                                Show("week_day"),
                                SetVariable("events_var", False),
                                SetVariable("week_day_var", True) ]
                        elif week_day_var == False and any( [ getattr(store, "stats_var{}".format(k), True) for k in list_girl_characters ] ):
                            action [ [ Hide("change_stats{}".format(k)) for k in list_girl_characters ],
                                Show("week_day"),
                                [ SetVariable("stats_var{}".format(k), False) for k in list_girl_characters ],
                                SetVariable("week_day_var", True) ]
                        elif week_day_var == False:
                            action [ Show("week_day"),
                                SetVariable("week_day_var", True) ]
                        elif week_day_var == True:
                            action [ Hide("week_day"),
                                SetVariable("week_day_var", False) ]

                    text _("") size 8

                    text _("{color=#00589E}Money:[money]----------------------{/color}") #outlines [(1.1, "#000000", 0, 0)]

                    textbutton _("Add $1000"):
                        text_style ("ds_mod_style_image_button")
                        action SetVariable("money", money + 1000)

                    textbutton _("Remove $1000"):
                        text_style ("ds_mod_style_image_button")
                        if (money >= 1000):
                            action SetVariable("money", money - 1000)
                        elif money < 1000:
                            action SetVariable("money", 0)
                        elif money == 0:
                            action NullAction()

                    textbutton _("Input money"):
                        text_style ("ds_mod_style_image_button")
                        action ui.callsinnewcontext ("input_money")

                    text _("{color=#00589E}Gallery unlocker-----------------{/color}") #outlines [(1.1, "#000000", 0, 0)]

                    textbutton _(If( any( [ getattr( persistent, "gal_{}_{}".format(k, i) , True) for i in range(1, 10) for k in gal_name_var ] ),
                        "Lock Gallery",
                        "Unlock Gallery")):
                        text_style ("ds_mod_style_image_button")
                        if any( [ getattr( persistent, "gal_{}_{}".format(k, i) , True) for i in range(1, 10) for k in gal_name_var ] ):
                            action [ SetField( persistent, "gal_{}_{}".format(k, i) , False) for i in range(1, 10) for k in gal_name_var ]
                        else:
                            action [ SetField( persistent, "gal_{}_{}".format(k, i) , True) for i in range(1, 10) for k in gal_name_var ]

                    #text _("") size 10

            #vbar value YScrollValue("ds_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG

    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("ds"),
            Show("phone_interface") ]
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

####################################################################################################################################################
### Items screen

screen items_mod():
    #style_prefix "stats"

    add "MobileScreen.png"
    modal True

    frame xalign 0.510 yalign 0.3:# at truecenter:
        background  "Mobile_event_Screen.png"
        has vbox

        text _("{color=#E60000}Add/Remove items{/color}") outlines [(1.1, "#000000", 0, 0)] at center

        textbutton _(If(spycaminmomroom,
            "{size=18}Spy cam in [mom]'s room is: \n                   {color=#1DDB16}Set{/color}{/size}",
            "{size=18}Spy cam in [mom]'s room is: \n                {color=#E60000}Not set{/color}{/size}")):
            text_style ("ds_mod_style_image_button")
            action [ If(progress >= 6,
                [ If(spycaminmomroom,
                    [ SetVariable("spycaminmomroom", False) ],
                    [ SetVariable("spycaminmomroom", True) ]) ],
                [ ui.callsinnewcontext("info_spy_cams") ]) ]

        textbutton _(If(spycaminlaurenroom,
            "{size=18}Spy cam in Lauren's room is: \n                   {color=#1DDB16}Set{/color}{/size}",
            "{size=18}Spy cam in Lauren's room is: \n               {color=#E60000}Not set{/color}{/size}")):
            text_style ("ds_mod_style_image_button")
            action [ If((progress >= 6 and sidneyfingerlaurenprogress > 4),
                [ If(spycaminlaurenroom,
                    [ SetVariable("spycaminlaurenroom", False) ],
                    [ SetVariable("spycaminlaurenroom", True) ]) ],
                [ ui.callsinnewcontext("info_spy_cams") ]) ]

        textbutton _(If(spycaminbath,
            "{size=18}Spy cam in bathroom is: \n                   {color=#1DDB16}Set{/color}{/size}",
            "{size=18}Spy cam in bathroom room is: \n               {color=#E60000}Not set{/color}{/size}")):
            text_style ("ds_mod_style_image_button")
            action [ If(progress >= 6,
                [ If(spycaminbath,
                    [ SetVariable("spycaminbath", False) ],
                    [ SetVariable("spycaminbath", True) ]) ],
                [ ui.callsinnewcontext("info_spy_cams") ]) ]

        text _("{color=#000000}-------------------------------------{/color}") #at center

        side ("c"):
            area (1,0,315,300)
            viewport id "items_mod_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:
                    text _("{{color=#E60000}}Chocolate Bar: {0}{{/color}}".format(inventory.inv_amount(chocolate))) outlines [(1.1, "#000000", 0, 0)] size 25 at center


                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(chocolate) < 10:
                            action Function(inventory.add, chocolate, 10-inventory.inv_amount(chocolate))#SetField(inventory, "add", "chocolate")#NullAction()#Function(renpy.run(inventory.add(chocolate)))
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, chocolate)

                    text _("")

                    text _("{{color=#E60000}}Hardalong Gift Card: {0}{{/color}}".format(inventory.inv_amount(giftcard))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(giftcard) < 10:
                            action Function(inventory.add, giftcard, 10-inventory.inv_amount(giftcard))
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, giftcard)

                    text _("")

                    text _("{{color=#E60000}}Flowers: {0}{{/color}}".format(inventory.inv_amount(flowers))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(flowers) < 10:
                            action Function(inventory.add, flowers, 10-inventory.inv_amount(flowers))
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, flowers)

                    text _("")

                    text _("{{color=#E60000}}Melatonin: {0}{{/color}}".format(inventory.inv_amount(melatonin))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(melatonin) < 1:
                            action Function(inventory.add, melatonin)
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, melatonin)

                    textbutton _(If(tookmelatonin,
                        "Remove from tea!",
                        "Spike the tea!")) at center:
                        text_style ("ds_mod_style_image_button")
                        action If(tookmelatonin,
                            SetVariable("tookmelatonin", False),
                            SetVariable("tookmelatonin", True))

                    text _("")

                    text _("{{color=#E60000}}Spycams: {0}{{/color}}".format(inventory.inv_amount(spycam))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(spycam) < 3:
                            action Function(inventory.add, spycam)
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, spycam)

                    text _("")

                    text _("{{color=#E60000}}Ball Gag: {0}{{/color}}".format(inventory.inv_amount(ball_gag))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(ball_gag) < 1:
                            action Function(inventory.add, ball_gag)
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, ball_gag)

                    text _("")

                    text _("{{color=#E60000}}Perry Hotter Book 1: {0}{{/color}}".format(inventory.inv_amount(ph_book1))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(ph_book1) < 1:
                            action Function(inventory.add, ph_book1)
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, ph_book1)

                    text _("")

                    text _("{{color=#E60000}}Perry Hotter Book 2: {0}{{/color}}".format(inventory.inv_amount(ph_book2))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(ph_book2) < 1:
                            action Function(inventory.add, ph_book2)
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, ph_book2)

                    text _("")

                    text _("{{color=#E60000}}Perry Hotter Book 3: {0}{{/color}}".format(inventory.inv_amount(ph_book3))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(ph_book3) < 1:
                            action Function(inventory.add, ph_book3)
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, ph_book3)

                    text _("")

                    text _("{{color=#E60000}}DSLR Camera: {0}{{/color}}".format(inventory.inv_amount(camera))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(camera) < 1:
                            action Function(inventory.add, camera)
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, camera)

                    text _("")

                    text _("{{color=#E60000}}Green screen: {0}{{/color}}".format(inventory.inv_amount(green_screen))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(green_screen) < 1:
                            action Function(inventory.add, green_screen)
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, green_screen)

                    text _("")

                    text _("{{color=#E60000}}Pro lights: {0}{{/color}}".format(inventory.inv_amount(pro_lights))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(pro_lights) < 1:
                            action Function(inventory.add, pro_lights)
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, pro_lights)

                    text _("")

                    text _("{{color=#E60000}}[Mom]'s new bikini: {0}{{/color}}".format(inventory.inv_amount(jacky_bikini_01))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(jacky_bikini_01) < 1:
                            action Function(inventory.add, jacky_bikini_01)
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, jacky_bikini_01)

                    text _("")

                    text _("{{color=#E60000}}DSLR Lenses: {0}{{/color}}".format(inventory.inv_amount(camera_accessories_1))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(camera_accessories_1) < 1:
                            action Function(inventory.add, camera_accessories_1)
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, camera_accessories_1)

                    text _("")

                    text _("{{color=#E60000}}DSLR Eyepiece: {0}{{/color}}".format(inventory.inv_amount(camera_accessories_2))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(camera_accessories_2) < 1:
                            action Function(inventory.add, camera_accessories_2)
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, camera_accessories_2)

                    text _("")

                    text _("{{color=#E60000}}DSLR Hand Grip: {0}{{/color}}".format(inventory.inv_amount(camera_accessories_3))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(camera_accessories_3) < 1:
                            action Function(inventory.add, camera_accessories_3)
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, camera_accessories_3)

                    text _("")

                    text _("{{color=#E60000}}DSLR Ring Flash: {0}{{/color}}".format(inventory.inv_amount(camera_accessories_4))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(camera_accessories_4) < 1:
                            action Function(inventory.add, camera_accessories_4)
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, camera_accessories_4)

                    text _("")

                    text _("{{color=#E60000}}DSLR Camera Tripod: {0}{{/color}}".format(inventory.inv_amount(camera_accessories_5))) outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    textbutton _("Add!") at center:
                        text_style ("ds_mod_style_image_button")
                        if inventory.inv_amount(camera_accessories_5) < 1:
                            action Function(inventory.add, camera_accessories_5)
                        else:
                            action ItemCheatAlert

                    textbutton _("Remove!") at center:
                        text_style ("ds_mod_style_image_button")
                        action Function(inventory.drop, camera_accessories_5)

                    text _("")

            #vbar value YScrollValue("items_mod_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG

    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("items_mod"),
            Show("ds") ]
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

####################################################################################################################################################
### Set day of the week screen

screen week_day():
    #style_prefix "stats"

    add "MobileScreen.png"
    modal True

    frame xalign 0.500 yalign 0.297:# at truecenter:
        background  "Mobile_event_Screen.png"
        has vbox

        side ("c"):
            area (1,0,315,510)
            viewport id "week_day_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:

                    if daycounter == 1:
                            $ day = "Monday"
                    elif daycounter == 2:
                            $ day = "Tuesday"
                    elif daycounter == 3:
                            $ day = "Wednesday"
                    elif daycounter == 4:
                            $ day = "Thursday"
                    elif daycounter == 5:
                            $ day = "Friday"
                    elif daycounter == 6:
                            $ day = "Saturday"
                    else:
                            $ day = "Sunday"

                    text _("{color=#E60000}Day of the week:{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 xpos 0.15
                    text _("{color=#E60000}[day]{/color}") outlines [(1.1, "#4118fa", 0, 0)]size 23 xpos 0.38


                    text _("{color=#000000}------------------------------------------{/color}") size 20 at center

                    textbutton _("Monday!") at center:
                        text_style ("ds_mod_style_image_button")
                        if daycounter != 1:
                            action SetVariable("daycounter", 1)
                        elif daycounter == 1:
                            action NullAction()

                    text _("") size 8

                    textbutton _("Tuesday!") at center:
                        text_style ("ds_mod_style_image_button")
                        if daycounter != 2:
                            action SetVariable("daycounter", 2)
                        elif daycounter == 2:
                            action NullAction()

                    text _("") size 8

                    textbutton _("Wednesday!") at center:
                        text_style ("ds_mod_style_image_button")
                        if daycounter != 3:
                            action SetVariable("daycounter", 3)
                        elif daycounter == 3:
                            action NullAction()

                    text _("") size 8

                    textbutton _("Thursday!") at center:
                        text_style ("ds_mod_style_image_button")
                        if daycounter != 4:
                            action SetVariable("daycounter", 4)
                        elif daycounter == 4:
                            action NullAction()

                    text _("") size 8

                    textbutton _("Friday!") at center:
                        text_style ("ds_mod_style_image_button")
                        if daycounter != 5:
                            action SetVariable("daycounter", 5)
                        elif daycounter == 5:
                            action NullAction()


                    text _("") size 8

                    textbutton _("Saturday!") at center:
                        text_style ("ds_mod_style_image_button")
                        if daycounter != 6:
                            action SetVariable("daycounter", 6)
                        elif daycounter == 6:
                            action NullAction()

                    text _("") size 8

                    textbutton _("Sunday!") at center:
                        text_style ("ds_mod_style_image_button")
                        if daycounter != 7:
                            action SetVariable("daycounter", 7)
                        elif daycounter == 7:
                            action NullAction()

                    #text _("") size 8


            #vbar value YScrollValue("week_day_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG

    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("week_day"),
            Show("ds") ]
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

####################################################################################################################################################
### Change girls stats screen

screen change_stats():

    key "ctrl_alt_K_z":
        action ToggleVariable("devMod")

    if persistent.patreonsafe:
        $ Mom = mom_name
        $ mom = mom_name
        $ Dad = dad_name
        $ dad = dad_name
        $ uncle = uncle_name
        $ Uncle = uncle_name
        $ Auntie = auntie_name
        $ auntie = auntie_name
        $ Auntie_2 = ""
        $ auntie_2 = ""
    else:
        $ Mom = "Mom"
        $ mom = "mom"
        $ Dad = "Dad"
        $ dad = "dad"
        $ uncle = "uncle " + uncle_name
        $ Uncle = "Uncle " + uncle_name
        $ Auntie = "Aunt " + auntie_name_short
        $ auntie = "aunt " + auntie_name_short
        $ Auntie_2 = "Aunt "
        $ auntie_2 = "aunt "

    #style_prefix "stats"

    add "MobileScreen.png"
    modal True

    frame xalign 0.500 yalign 0.297:# at truecenter:
        background  "Mobile_event_Screen.png"
        has vbox

        text _("")

        text _("{color=#E60000}Change girls stats{/color}") outlines [(1.1, "#000000", 0, 0)] at center

        text _("{color=#000000}-------------------------------------{/color}") #at center

        textbutton _("Reset all girls anger lvl!") at center:
            text_style ("ds_mod_style_image_button")
            action [ SetVariable("momanger", 0),
                SetVariable("laurenanger", 0),
                SetVariable("sidneyanger", 0),
                SetVariable("auntanger", 0),
                SetVariable("cousinanger", 0),
                ui.callsinnewcontext ("ds_anger_reset_nfo")
                ]
        if devMod:
            textbutton _("Set all girls libido lvl to max!") at center:
                text_style ("ds_mod_style_image_button")
                action [ SetVariable("momlibido", 10),
                    SetVariable("laurenlibido", 10),
                    SetVariable("sidneylibido", 10),
#                    SetVariable("auntlibido", 10),
#                    SetVariable("cousinlibido", 10),
                    ui.callsinnewcontext ("ds_libido_2max_nfo")
                    ]
        text _("{color=#000000}-------------------------------------{/color}") #at center

        side ("c"):
            area (1,0,315,480)
            viewport id "change_stats_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:

                    text _("")

                    textbutton _("{image=iconM} [Mom]"):
                        text_style ("ds_mod_style_image_button")
                        if stats_var_Mom == False and any( [ getattr(store, "stats_var{}".format(k), True) for k in list_girl_characters if k != "_Mom" and k != "" ] ):
                            action [ [ Hide("change_stats{}".format(k)) for k in list_girl_characters if k != "_Mom" and k != "" ],
                                Show("change_stats_Mom"),
                                [ SetVariable("stats_var{}".format(k), False) for k in list_girl_characters if k != "_Mom" and k != "" ],
                                SetVariable("stats_var_Mom", True) ]
                        elif stats_var_Mom == False:
                            action [ Show("change_stats_Mom"),
                                SetVariable("stats_var_Mom", True) ]
                        elif stats_var_Mom == True:
                            action [ Hide("change_stats_Mom"),
                                SetVariable("stats_var_Mom", False) ]

                    text _("") size 10

                    textbutton _("{image=iconL} Lauren"):
                        text_style ("ds_mod_style_image_button")
                        if stats_var_Lauren == False and any( [ getattr(store, "stats_var{}".format(k), True) for k in list_girl_characters if k != "_Lauren" and k != "" ] ):
                            action [ [ Hide("change_stats{}".format(k)) for k in list_girl_characters if k != "_Lauren" and k != "" ],
                                Show("change_stats_Lauren"),
                                [ SetVariable("stats_var{}".format(k), False) for k in list_girl_characters if k != "_Lauren" and k != "" ],
                                SetVariable("stats_var_Lauren", True) ]
                        elif stats_var_Lauren == False:
                            action [ Show("change_stats_Lauren"),
                                SetVariable("stats_var_Lauren", True) ]
                        elif stats_var_Lauren == True:
                            action [ Hide("change_stats_Lauren"),
                                SetVariable("stats_var_Lauren", False) ]

                    text _("") size 10

                    textbutton _("{image=iconS} Sidney"):
                        text_style ("ds_mod_style_image_button")
                        if stats_var_Sidney == False and any( [ getattr(store, "stats_var{}".format(k), True) for k in list_girl_characters if k != "_Sidney" and k != "" ] ):
                            action [ [ Hide("change_stats{}".format(k)) for k in list_girl_characters if k != "_Sidney" and k != "" ],
                                Show("change_stats_Sidney"),
                                [ SetVariable("stats_var{}".format(k), False) for k in list_girl_characters if k != "_Sidney" and k != "" ],
                                SetVariable("stats_var_Sidney", True) ]
                        elif stats_var_Sidney == False:
                            action [ Show("change_stats_Sidney"),
                                SetVariable("stats_var_Sidney", True) ]
                        elif stats_var_Sidney == True:
                            action [ Hide("change_stats_Sidney"),
                                SetVariable("stats_var_Sidney", False) ]

                    text _("") size 10

                    textbutton _("{image=iconA} [Auntie]"):
                        text_style ("ds_mod_style_image_button")
                        if stats_var_Aunt == False and any( [ getattr(store, "stats_var{}".format(k), True) for k in list_girl_characters if k != "_Aunt" and k != "" ] ):
                            action [ [ Hide("change_stats{}".format(k)) for k in list_girl_characters if k != "_Aunt" and k != "" ],
                                Show("change_stats_Aunt"),
                                [ SetVariable("stats_var{}".format(k), False) for k in list_girl_characters if k != "_Aunt" and k != "" ],
                                SetVariable("stats_var_Aunt", True) ]
                        elif stats_var_Aunt == False:
                            action [ Show("change_stats_Aunt"),
                                SetVariable("stats_var_Aunt", True) ]
                        elif stats_var_Aunt == True:
                            action [ Hide("change_stats_Aunt"),
                                SetVariable("stats_var_Aunt", False) ]

                    text _("") size 10

                    textbutton _(If( persistent.patreonsafe,
                        "{image=iconC} Mandy",
                        "{image=iconC} Cousin Mandy")):
                        text_style ("ds_mod_style_image_button")
                        if stats_var_Cousin == False and any( [ getattr(store, "stats_var{}".format(k), True) for k in list_girl_characters if k != "_Cousin" and k != "" ] ):
                            action [ [ Hide("change_stats{}".format(k)) for k in list_girl_characters if k != "_Cousin" and k != "" ],
                                Show("change_stats_Cousin"),
                                [ SetVariable("stats_var{}".format(k), False) for k in list_girl_characters if k != "_Cousin" and k != "" ],
                                SetVariable("stats_var_Cousin", True) ]
                        elif stats_var_Cousin == False:
                            action [ Show("change_stats_Cousin"),
                                SetVariable("stats_var_Cousin", True) ]
                        elif stats_var_Cousin == True:
                            action [ Hide("change_stats_Cousin"),
                                SetVariable("stats_var_Cousin", False) ]

                    text _("") size 10

            #vbar value YScrollValue("change_stats_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG

    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("change_stats"),
            Show("ds") ]
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

####################################################################################################################################################
### Change stats for Mom

screen change_stats_Mom():

    if persistent.patreonsafe:
        $ Mom = mom_name
        $ mom = mom_name
        $ Dad = dad_name
        $ dad = dad_name
        $ uncle = uncle_name
        $ Uncle = uncle_name
        $ Auntie = auntie_name
        $ auntie = auntie_name
        $ Auntie_2 = ""
        $ auntie_2 = ""
    else:
        $ Mom = "Mom"
        $ mom = "mom"
        $ Dad = "Dad"
        $ dad = "dad"
        $ uncle = "uncle " + uncle_name
        $ Uncle = "Uncle " + uncle_name
        $ Auntie = "Aunt " + auntie_name_short
        $ auntie = "aunt " + auntie_name_short
        $ Auntie_2 = "Aunt "
        $ auntie_2 = "aunt "

    #style_prefix "stats"

    add "MobileScreen.png"
    modal True

    frame xalign 0.500 yalign 0.290:# at truecenter:
        background  "Mobile_event_Screen.png"
        has vbox

        text _("")

        text _("{image=iconM} {color=#E60000}[Mom]{/color}") outlines [(1.1, "#000000", 0, 0)] at center

        text _("{color=#000000}-------------------------------------{/color}") #at center

        side ("c"):
            area (1,0,315,450)
            viewport id "change_stats_Mom_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:
                    text _("{color=#00589E}Respect:{/color} {color=#1DDB16}[momrespect]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase respect!") at center:
                        text_style ("ds_mod_style_image_button")
                        if momrespect >= 0 and momrespect < 10:
                            action SetVariable("momrespect", momrespect+1)
                        elif momrespect == 5:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease respect!") at center:
                        text_style ("ds_mod_style_image_button")
                        if momrespect > 1:
                            action SetVariable("momrespect", momrespect-1)
                        elif momrespect == 1:
                            action SetVariable("momrespect", 0)
                        elif momrespect == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Affection:{/color} {color=#1DDB16}[momaffection]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase affection!") at center:
                        text_style ("ds_mod_style_image_button")
                        if momaffection >= 0 and momaffection < 20:
                            action SetVariable("momaffection", momaffection+1)
                        elif momaffection == 100:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease affection!") at center:
                        text_style ("ds_mod_style_image_button")
                        if momaffection > 1:
                            action SetVariable("momaffection", momaffection-1)
                        elif momaffection == 1:
                            action SetVariable("momaffection", 0)
                        elif momaffection == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Libido:{/color} {color=#1DDB16}[momlibido]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase libido!") at center:
                        text_style ("ds_mod_style_image_button")
                        if momlibido >= 0 and momlibido < 10:
                            action SetVariable("momlibido", momlibido+1)
                        elif momlibido == 10:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease libido!") at center:
                        text_style ("ds_mod_style_image_button")
                        if momlibido > 1:
                            action SetVariable("momlibido", momlibido-1)
                        elif momlibido == 1:
                            action SetVariable("momlibido", 0)
                        elif momlibido == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Submission:{/color} {color=#1DDB16}[momsubmission]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase submission!") at center:
                        text_style ("ds_mod_style_image_button")
                        if momsubmission >= 0 and momsubmission < 100:
                            action SetVariable("momsubmission", momsubmission+1)
                        elif momsubmission == 100:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease submission!") at center:
                        text_style ("ds_mod_style_image_button")
                        if momsubmission > 1:
                            action SetVariable("momsubmission", momsubmission-1)
                        elif momsubmission == 1:
                            action SetVariable("momsubmission", 0)
                        elif momsubmission == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Anger:{/color} {color=#1DDB16}[momanger]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Reset anger!") at center:
                        text_style ("ds_mod_style_image_button")
                        action SetVariable("momanger", 0)

                    text _("") size 15

                    textbutton _("Increase anger!") at center:
                        text_style ("ds_mod_style_image_button")
                        if momanger >= 0 and momanger < 10:
                            action SetVariable("momanger", momanger+1)
                        elif momanger == 10:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease anger!") at center:
                        text_style ("ds_mod_style_image_button")
                        if momanger > 1:
                            action SetVariable("momanger", momanger-1)
                        elif momanger == 1:
                            action SetVariable("momanger", 0)
                        elif momanger == 0:
                            action NullAction()

                    text _("") size 15

            #vbar value YScrollValue("change_stats_Mom_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG

    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("change_stats_Mom"), Show("change_stats") ]
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

####################################################################################################################################################
### Change stats for Lauren

screen change_stats_Lauren():
    #style_prefix "stats"

    add "MobileScreen.png"
    modal True

    frame xalign 0.500 yalign 0.290:# at truecenter:
        background  "Mobile_event_Screen.png"
        has vbox

        text _("")

        text _("{image=iconL} {color=#E60000}Lauren{/color}") outlines [(1.1, "#000000", 0, 0)] at center

        text _("{color=#000000}-------------------------------------{/color}") #at center

        side ("c"):
            area (1,0,315,450)
            viewport id "change_stats_Lauren_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:
                    text _("{color=#00589E}Respect:{/color} {color=#1DDB16}[laurenrespect]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase respect!") at center:
                        text_style ("ds_mod_style_image_button")
                        if laurenrespect >= 0 and laurenrespect < 5:
                            action SetVariable("laurenrespect", laurenrespect+1)
                        elif laurenrespect == 5:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease respect!") at center:
                        text_style ("ds_mod_style_image_button")
                        if laurenrespect > 1:
                            action SetVariable("laurenrespect", laurenrespect-1)
                        elif laurenrespect == 1:
                            action SetVariable("laurenrespect", 0)
                        elif laurenrespect == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Affection:{/color} {color=#1DDB16}[laurenaffection]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase affection!") at center:
                        text_style ("ds_mod_style_image_button")
                        if laurenaffection >= 0 and laurenaffection < 20:
                            action SetVariable("laurenaffection", laurenaffection+1)
                        elif laurenaffection == 100:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease affection!") at center:
                        text_style ("ds_mod_style_image_button")
                        if laurenaffection > 1:
                            action SetVariable("laurenaffection", laurenaffection-1)
                        elif laurenaffection == 1:
                            action SetVariable("laurenaffection", 0)
                        elif laurenaffection == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Libido:{/color} {color=#1DDB16}[laurenlibido]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase libido!") at center:
                        text_style ("ds_mod_style_image_button")
                        if laurenlibido >= 0 and laurenlibido < 10:
                            action SetVariable("laurenlibido", laurenlibido+1)
                        elif laurenlibido == 10:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease libido!") at center:
                        text_style ("ds_mod_style_image_button")
                        if laurenlibido > 1:
                            action SetVariable("laurenlibido", laurenlibido-1)
                        elif laurenlibido == 1:
                            action SetVariable("laurenlibido", 0)
                        elif laurenlibido == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Submission:{/color} {color=#1DDB16}[laurensubmission]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase submission!") at center:
                        text_style ("ds_mod_style_image_button")
                        if laurensubmission >= 0 and laurensubmission < 100:
                            action SetVariable("laurensubmission", laurensubmission+1)
                        elif laurensubmission == 100:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease submission!") at center:
                        text_style ("ds_mod_style_image_button")
                        if laurensubmission > 1:
                            action SetVariable("laurensubmission", laurensubmission-1)
                        elif laurensubmission == 1:
                            action SetVariable("laurensubmission", 0)
                        elif laurensubmission == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Anger:{/color} {color=#1DDB16}[laurenanger]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Reset anger!") at center:
                        text_style ("ds_mod_style_image_button")
                        action SetVariable("laurenanger", 0)

                    text _("") size 15

                    textbutton _("Increase anger!") at center:
                        text_style ("ds_mod_style_image_button")
                        if laurenanger >= 0 and laurenanger < 10:
                            action SetVariable("laurenanger", laurenanger+1)
                        elif laurenanger == 10:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease anger!") at center:
                        text_style ("ds_mod_style_image_button")
                        if laurenanger > 1:
                            action SetVariable("laurenanger", laurenanger-1)
                        elif laurenanger == 1:
                            action SetVariable("laurenanger", 0)
                        elif laurenanger == 0:
                            action NullAction()

                    if start_of_campaign:
                        text _("") size 18

                        text _("{color=#00589E}School influence:{/color} {color=#1DDB16}[school_influence]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                        text _("") size 20

                        textbutton _("Increase influence!") at center:
                            text_style ("ds_mod_style_image_button")
                            if school_influence >= 0 and school_influence < 100:
                                action SetVariable("school_influence", school_influence+1)
                            elif school_influence == 100:
                                action NullAction()

                        text _("") size 15

                        textbutton _("Decrease influence!") at center:
                            text_style ("ds_mod_style_image_button")
                            if school_influence > 1:
                                action SetVariable("school_influence", school_influence-1)
                            elif school_influence == 1:
                                action SetVariable("school_influence", 0)
                            elif school_influence == 0:
                                action NullAction()

                    text _("") size 15

            #vbar value YScrollValue("change_stats_Lauren_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG

    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("change_stats_Lauren"), Show("change_stats") ]
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

####################################################################################################################################################
### Change stats for Sidney

screen change_stats_Sidney():
    #style_prefix "stats"

    add "MobileScreen.png"
    modal True

    frame xalign 0.500 yalign 0.290:# at truecenter:
        background  "Mobile_event_Screen.png"
        has vbox

        text _("")

        text _("{image=iconS} {color=#E60000}Sidney{/color}") outlines [(1.1, "#000000", 0, 0)] at center

        text _("{color=#000000}-------------------------------------{/color}") #at center

        side ("c"):
            area (1,0,315,450)
            viewport id "change_stats_Sidney_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:
                    text _("{color=#00589E}Respect:{/color} {color=#1DDB16}[sidneyrespect]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase respect!") at center:
                        text_style ("ds_mod_style_image_button")
                        if sidneyrespect >= 0 and sidneyrespect < 5:
                            action SetVariable("sidneyrespect", sidneyrespect+1)
                        elif sidneyrespect == 5:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease respect!") at center:
                        text_style ("ds_mod_style_image_button")
                        if sidneyrespect > 1:
                            action SetVariable("sidneyrespect", sidneyrespect-1)
                        elif sidneyrespect == 1:
                            action SetVariable("sidneyrespect", 0)
                        elif sidneyrespect == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Affection:{/color} {color=#1DDB16}[sidneyaffection]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase affection!") at center:
                        text_style ("ds_mod_style_image_button")
                        if sidneyaffection >= 0 and sidneyaffection < 20:
                            action SetVariable("sidneyaffection", sidneyaffection+1)
                        elif sidneyaffection == 100:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease affection!") at center:
                        text_style ("ds_mod_style_image_button")
                        if sidneyaffection > 1:
                            action SetVariable("sidneyaffection", sidneyaffection-1)
                        elif sidneyaffection == 1:
                            action SetVariable("sidneyaffection", 0)
                        elif sidneyaffection == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Libido:{/color} {color=#1DDB16}[sidneylibido]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase libido!") at center:
                        text_style ("ds_mod_style_image_button")
                        if sidneylibido >= 0 and sidneylibido < 10:
                            action SetVariable("sidneylibido", sidneylibido+1)
                        elif sidneylibido == 10:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease libido!") at center:
                        text_style ("ds_mod_style_image_button")
                        if sidneylibido > 1:
                            action SetVariable("sidneylibido", sidneylibido-1)
                        elif sidneylibido == 1:
                            action SetVariable("sidneylibido", 0)
                        elif sidneylibido == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Submission:{/color} {color=#1DDB16}[sidneysubmission]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase submission!") at center:
                        text_style ("ds_mod_style_image_button")
                        if sidneysubmission >= 0 and sidneysubmission < 100:
                            action SetVariable("sidneysubmission", sidneysubmission+1)
                        elif sidneysubmission == 100:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease submission!") at center:
                        text_style ("ds_mod_style_image_button")
                        if sidneysubmission > 1:
                            action SetVariable("sidneysubmission", sidneysubmission-1)
                        elif sidneysubmission == 1:
                            action SetVariable("sidneysubmission", 0)
                        elif sidneysubmission == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Anger:{/color} {color=#1DDB16}[sidneyanger]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Reset anger!") at center:
                        text_style ("ds_mod_style_image_button")
                        action SetVariable("sidneyanger", 0)

                    text _("") size 15

                    textbutton _("Increase anger!") at center:
                        text_style ("ds_mod_style_image_button")
                        if sidneyanger >= 0 and sidneyanger < 10:
                            action SetVariable("sidneyanger", sidneyanger+1)
                        elif sidneyanger == 10:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease anger!") at center:
                        text_style ("ds_mod_style_image_button")
                        if sidneyanger > 1:
                            action SetVariable("sidneyanger", sidneyanger-1)
                        elif sidneyanger == 1:
                            action SetVariable("sidneyanger", 0)
                        elif sidneyanger == 0:
                            action NullAction()

                    text _("") size 15

            #vbar value YScrollValue("change_stats_Sidney_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG

    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("change_stats_Sidney"), Show("change_stats") ]
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

####################################################################################################################################################
### Change stats for Aunt

screen change_stats_Aunt():
    #style_prefix "stats"

    if persistent.patreonsafe:
        $ Mom = mom_name
        $ mom = mom_name
        $ Dad = dad_name
        $ dad = dad_name
        $ uncle = uncle_name
        $ Uncle = uncle_name
        $ Auntie = auntie_name
        $ auntie = auntie_name
        $ Auntie_2 = ""
        $ auntie_2 = ""
    else:
        $ Mom = "Mom"
        $ mom = "mom"
        $ Dad = "Dad"
        $ dad = "dad"
        $ uncle = "uncle " + uncle_name
        $ Uncle = "Uncle " + uncle_name
        $ Auntie = "Aunt " + auntie_name_short
        $ auntie = "aunt " + auntie_name_short
        $ Auntie_2 = "Aunt "
        $ auntie_2 = "aunt "

    add "MobileScreen.png"
    modal True

    frame xalign 0.500 yalign 0.290:# at truecenter:
        background  "Mobile_event_Screen.png"
        has vbox

        text _("")

        text _("{image=iconA} {color=#E60000}[Auntie]{/color}") outlines [(1.1, "#000000", 0, 0)] at center

        text _("{color=#000000}-------------------------------------{/color}") #at center

        side ("c"):
            area (1,0,315,450)
            viewport id "change_stats_Aunt_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:
                    text _("{color=#00589E}Respect:{/color} {color=#1DDB16}[auntrespect]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase respect!") at center:
                        text_style ("ds_mod_style_image_button")
                        if auntrespect >= 0 and auntrespect < 5:
                            action SetVariable("auntrespect", auntrespect+1)
                        elif auntrespect == 5:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease respect!") at center:
                        text_style ("ds_mod_style_image_button")
                        if auntrespect > 1:
                            action SetVariable("auntrespect", auntrespect-1)
                        elif auntrespect == 1:
                            action SetVariable("auntrespect", 0)
                        elif auntrespect == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Affection:{/color} {color=#1DDB16}[auntaffection]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase affection!") at center:
                        text_style ("ds_mod_style_image_button")
                        if auntaffection >= 0 and auntaffection < 20:
                            action SetVariable("auntaffection", auntaffection+1)
                        elif auntaffection == 100:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease affection!") at center:
                        text_style ("ds_mod_style_image_button")
                        if auntaffection > 1:
                            action SetVariable("auntaffection", auntaffection-1)
                        elif auntaffection == 1:
                            action SetVariable("auntaffection", 0)
                        elif auntaffection == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Libido:{/color} {color=#1DDB16}[auntlibido]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase libido!") at center:
                        text_style ("ds_mod_style_image_button")
                        if auntlibido >= 0 and auntlibido < 10:
                            action SetVariable("auntlibido", auntlibido+1)
                        elif auntlibido == 10:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease libido!") at center:
                        text_style ("ds_mod_style_image_button")
                        if auntlibido > 1:
                            action SetVariable("auntlibido", auntlibido-1)
                        elif auntlibido == 1:
                            action SetVariable("auntlibido", 0)
                        elif auntlibido == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Submission:{/color} {color=#1DDB16}[auntsubmission]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase submission!") at center:
                        text_style ("ds_mod_style_image_button")
                        if auntsubmission >= 0 and auntsubmission < 100:
                            action SetVariable("auntsubmission", auntsubmission + 1)
                        elif auntsubmission == 100:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease submission!") at center:
                        text_style ("ds_mod_style_image_button")
                        if auntsubmission > 1:
                            action SetVariable("auntsubmission", auntsubmission-1)
                        elif auntsubmission == 1:
                            action SetVariable("auntsubmission", 0)
                        elif auntsubmission == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Anger:{/color} {color=#1DDB16}[auntanger]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Reset anger!") at center:
                        text_style ("ds_mod_style_image_button")
                        action SetVariable("auntanger", 0)

                    text _("") size 15

                    textbutton _("Increase anger!") at center:
                        text_style ("ds_mod_style_image_button")
                        if auntanger >= 0 and auntanger < 10:
                            action SetVariable("auntanger", auntanger+1)
                        elif auntanger == 10:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease anger!") at center:
                        text_style ("ds_mod_style_image_button")
                        if auntanger > 1:
                            action SetVariable("auntanger", auntanger-1)
                        elif auntanger == 1:
                            action SetVariable("auntanger", 0)
                        elif auntanger == 0:
                            action NullAction()

                    text _("") size 15

            #vbar value YScrollValue("change_stats_Aunt_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG

    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("change_stats_Aunt"), Show("change_stats") ]
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

####################################################################################################################################################
### Change stats for Cousin Mandy

screen change_stats_Cousin():
    #style_prefix "stats"

    add "MobileScreen.png"
    modal True

    frame xalign 0.500 yalign 0.290:# at truecenter:
        background  "Mobile_event_Screen.png"
        has vbox

        text _("")

        text _(If( persistent.patreonsafe,
                        "{image=iconC} {color=#E60000}Mandy{/color}",
                        "{image=iconC} {color=#E60000}Cousin Mandy{/color}")) outlines [(1.1, "#000000", 0, 0)] at center

        text _("{color=#000000}-------------------------------------{/color}") #at center

        side ("c"):
            area (1,0,315,450)
            viewport id "change_stats_Cousin_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:
                    text _("{color=#00589E}Respect:{/color} {color=#1DDB16}[cousinrespect]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase respect!") at center:
                        text_style ("ds_mod_style_image_button")
                        if cousinrespect >= 0 and cousinrespect < 5:
                            action SetVariable("cousinrespect", cousinrespect+1)
                        elif cousinrespect == 5:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease respect!") at center:
                        text_style ("ds_mod_style_image_button")
                        if cousinrespect > 1:
                            action SetVariable("cousinrespect", cousinrespect-1)
                        elif cousinrespect == 1:
                            action SetVariable("cousinrespect", 0)
                        elif cousinrespect == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Affection:{/color} {color=#1DDB16}[cousinaffection]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase affection!") at center:
                        text_style ("ds_mod_style_image_button")
                        if cousinaffection >= 0 and cousinaffection < 20:
                            action SetVariable("cousinaffection", cousinaffection+1)
                        elif cousinaffection == 100:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease affection!") at center:
                        text_style ("ds_mod_style_image_button")
                        if cousinaffection > 1:
                            action SetVariable("cousinaffection", cousinaffection-1)
                        elif cousinaffection == 1:
                            action SetVariable("cousinaffection", 0)
                        elif cousinaffection == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Libido:{/color} {color=#1DDB16}[cousinlibido]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase libido!") at center:
                        text_style ("ds_mod_style_image_button")
                        if cousinlibido >= 0 and cousinlibido < 10:
                            action SetVariable("cousinlibido", cousinlibido+1)
                        elif cousinlibido == 10:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease libido!") at center:
                        text_style ("ds_mod_style_image_button")
                        if cousinlibido > 1:
                            action SetVariable("cousinlibido", cousinlibido-1)
                        elif cousinlibido == 1:
                            action SetVariable("cousinlibido", 0)
                        elif cousinlibido == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Submission:{/color} {color=#1DDB16}[cousinsubmission]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Increase submission!") at center:
                        text_style ("ds_mod_style_image_button")
                        if cousinsubmission >= 0 and cousinsubmission < 100:
                            action SetVariable("cousinsubmission", cousinsubmission+1)
                        elif cousinsubmission == 100:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease submission!") at center:
                        text_style ("ds_mod_style_image_button")
                        if cousinsubmission > 1:
                            action SetVariable("cousinsubmission", cousinsubmission-1)
                        elif cousinsubmission == 1:
                            action SetVariable("cousinsubmission", 0)
                        elif cousinsubmission == 0:
                            action NullAction()

                    text _("") size 18

                    text _("{color=#00589E}Anger:{/color} {color=#1DDB16}[cousinanger]{/color}") outlines [(1.1, "#000000", 0, 0)] size 25 at center

                    text _("") size 20

                    textbutton _("Reset anger!") at center:
                        text_style ("ds_mod_style_image_button")
                        action SetVariable("cousinanger", 0)

                    text _("") size 15

                    textbutton _("Increase anger!") at center:
                        text_style ("ds_mod_style_image_button")
                        if cousinanger >= 0 and cousinanger < 10:
                            action SetVariable("cousinanger", cousinanger+1)
                        elif cousinanger == 10:
                            action NullAction()

                    text _("") size 15

                    textbutton _("Decrease anger!") at center:
                        text_style ("ds_mod_style_image_button")
                        if cousinanger > 1:
                            action SetVariable("cousinanger", cousinanger-1)
                        elif cousinanger == 1:
                            action SetVariable("cousinanger", 0)
                        elif cousinanger == 0:
                            action NullAction()

                    text _("") size 15

            #vbar value YScrollValue("change_stats_Cousin_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG

    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("change_stats_Cousin"), Show("change_stats") ]
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

####################################################################################################################################################
### Labels
####################################################################################################################################################

label input_money:
    $ addmoney = int(renpy.input("How much money to add?", allow="0123456789") or 0)
    $ money = money + addmoney
    DS "You added $[addmoney] and now have: $[money]."

    return

#label mod_truestart:
#    scene bg SleepBlack
#    $ renpy.pause (1.5, hard=True)
#    scene bg Intro01
#    with fade
#    $ renpy.pause (2.5, hard=True)
#    scene bg SleepBlack
#    with fade
#    $ renpy.pause (1.0, hard=True)
#    if persistent.patreonsafe:
#        scene bg SafeTitleWAttributions
#        with fade
#        $ renpy.pause (5.5, hard=True)
#    else:
#        scene bg TitleWAttributions
#        with fade
#        $ renpy.pause (5.5, hard=True)
#    scene bg SleepBlack
#    jump change_name_patreon

label change_name_patreon:
    menu change_names:
        "Do you want to change your name? Default name is: {color=#0000CC}Ryan{/color}"
        "Yes":
            python:
                ryan = renpy.input ("Change Your Name. Default name is: {color=#0000CC}Ryan{/color}")

                ryan = ryan.strip()

                upper_ryan = ryan.upper()

                if ryan == "":
                    ryan = "Ryan"

            "Okay, your new name is: ({color=#0000CC}[ryan]{/color})."

            jump skip_game

        "No":
            jump skip_game

label ds_change_name_mom:
    python:
        mom_name = renpy.input ("Change [Mom]'s Name. Default name is: {color=#0000CC}Jacky{/color}")

        mom_name = mom_name.strip()

        if persistent.patreonsafe:
            Mom = mom_name
            mom = mom_name
        else:
            pass

#        upper_ryan = ryan.upper()

        if mom_name == "":
            mom_name = "Jacky"


    DS "Okay, her new name is: ({color=#0000CC}[mom_name]{/color})."

    return

label ds_change_name_Ryan:
    python:
        ryan = renpy.input ("Change Your Name. Default name is: {color=#0000CC}Ryan{/color}")

        ryan = ryan.strip()

        upper_ryan = ryan.upper()

        if ryan == "":
            ryan = "Ryan"


    DS "Okay, your new name is: ({color=#0000CC}[ryan]{/color})."

    return

label ds_mod_info:
    DS "This mod(v[mod_version]) was made by {color=#00589E}D.S.-sama{/color} for {color=#E60000}WillTylor{/color} and his game, {color=#34f500}AFamilyVenture_v[game_version]{/color}. Have fun playing the game and let us know if you find any bugs."

    return

label ds_anger_reset_nfo:
    DS "You have reset the anger lvl for all girls!"

    return

label ds_libido_2max_nfo:
    DS "You have set the libido lvl to max for all girls!"

    return

label info_spy_cams:
    DS "To set up the spy cams in the rooms you must first have the \'progress >= 6\' (after the event when Sidney comes home) and as an extra condition to set the camera in Lauren's room you must have \'sidneyfingerlaurenprogress > 4'\ (Sidney must move out of her room)."

    return

label after_load_000003:

    # if _version < config.version:
    if any([config.version != "{}_supporter".format(k) for k in game_versions_allowed_for_mod]):
        jump version_test
    else:
        pass


    return

label version_test:

    python:

        if os.path.isdir(config.basedir + "/game/Patreon_$5_Gallery"):
            mypath1  = config.basedir + "/game/Patreon_$5_Gallery"
            mypath2  = config.basedir + "/game/Patreon_$5_Gallery/Patreon IMG's"
#            mypath3  = config.basedir + "/game/Patreon_$5_Gallery/Patreon IMG's/Buttons"
            exes_list = [ ".rpy", ".rpyc", ".png", ".webp" ]
#            mypaths = [ "game/Patreon_$5_Gallery", "game/Patreon_$5_Gallery/Patreon IMG's", "game/Patreon_$5_Gallery/Patreon IMG's/Buttons" ]
            filelist1 = [ f for f in os.listdir(mypath1) if any( [ f.endswith("{}".format(i))for i in exes_list ] ) ]
            filelist2 = [ f for f in os.listdir(mypath2) if any( [ f.endswith("{}".format(i))for i in exes_list ] ) ]
#            filelist3 = [ f for f in os.listdir(mypath3) if any( [ f.endswith("{}".format(i))for i in exes_list ] ) ]

#            for f in filelist3:
#                os.remove(os.path.join(mypath3, f))
            for f in filelist2:
                os.remove(os.path.join(mypath2, f))
            for f in filelist1:
                os.remove(os.path.join(mypath1, f))
            shutil.rmtree(config.basedir + "/game/Patreon_$5_Gallery")

        if os.path.isfile(config.basedir + "/game/Patreon_extra.rpa"):
            os.remove(config.basedir + "/game/Patreon_extra.rpa")

        if not persistent.modCaught_on: #renpy.loadable("DSMod_nfo.rpy"):
            f = open(config.basedir + "/game/DSMod_nfo.rpy","w+")
            code_mod_nfo = [ "define persistent.modCaught_on = True",
                    "\n",
                    "define DS = Character('D.S.-sama', color='#1DDB16')",
                    "\n",
                    "label version_test:",
                    " DS 'Nice try'",
                    " jump myroom",
                    "\n"
                    ]
            f.write("\n".join(code_mod_nfo))
            f.close()

    $ renpy.run( Function(renpy.reload_script) )

label adv_rest_jump:
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
            RT "{i}School has ended, I must return home{/i}"
            jump myroom
    elif any([screen_on == "{}".format(k) for k in class_screens]): # class_screens
        if timeofdaycounter <= 3 and start_of_campaign:
            jump new_classroom
        elif timeofdaycounter <= 3:
            jump classroom
        else:
            RT "{i}School has ended, I must return home{/i}"
            jump myroom
    elif any([screen_on == "{}".format(k) for k in schoolbath_screens]): # schoolbath_screens
        if timeofdaycounter <= 3:
            jump schoolbathroom
        else:
            RT "{i}School has ended, I must return home{/i}"
            jump myroom
    elif any([screen_on == "{}".format(k) for k in girlslocker_screens]): # girlslocker_screens
        if timeofdaycounter <= 3:
            jump girlslockers
        else:
            RT "{i}School has ended, I must return home{/i}"
            jump myroom
    elif any([screen_on == "{}".format(k) for k in city_screens]): # city_screens
        if timeofdaycounter <=4:
            $ screen_on = "citymapmap"
            call screen citymapmap
        else:
            $ screen_on = "citymapmapnight"
            call screen citymapmapnight

    return
