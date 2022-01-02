
####################################################################################################################################################
### Powerd by D.S.-sama ############################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

####################################################################################################################################################
### Styles

style phone_gallery_text_style:
    size 20
    #bold True
    color "#888888" #00589E # E60000
    hover_color "#c184ff"
    outlines [(3, "#000", 0,0)]

####################################################################################################################################################
### Main phone gallery screen

screen phone_gallery():

#    if persistent.patreonsafe:
#        $ Mom = mom_name
#        $ mom = mom_name
#        $ Dad = dad_name
#        $ dad = dad_name
#        $ uncle = uncle_name
#        $ Uncle = uncle_name
#        $ Auntie = auntie_name
#        $ auntie = auntie_name
#        $ Auntie_2 = ""
#        $ auntie_2 = ""
#    else:
#        $ Mom = "Mom"
#        $ mom = "mom"
#        $ Dad = "Dad"
#        $ dad = "dad"
#        $ uncle = "uncle " + uncle_name
#        $ Uncle = "Uncle " + uncle_name
#        $ Auntie = "Aunt " + auntie_name_short
#        $ auntie = "aunt " + auntie_name_short
#        $ Auntie_2 = "Aunt "
#        $ auntie_2 = "aunt "

    style_prefix "phone_gall"

    add "MobileScreen.png"
    modal True

    frame xalign .495 yalign .297:# at truecenter:
        background None
        has vbox

        text _("{image=images/interface_images/phone_screen_images/images_phone.png} Photo Gallery") style "phone_gallery_text_style" size 25 at center

        side ("c"):
            area (1,0,315,510)
            viewport id "stats_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:

                    text _("") size 10

                    if progress >= 3:
                        textbutton _("{image=images/interface_images/phone_screen_images/folder_phone_small.png} Mom's pictures"):
                            text_style ("phone_gallery_text_style")
                            action [ Hide("phone_gallery"), Show("phone_gallery_mom") ]

                    if laurenprogress >= 2:
                        textbutton _("{image=images/interface_images/phone_screen_images/folder_phone_small.png} Lauren's pictures"):
                            text_style ("phone_gallery_text_style")
                            action [ Hide("phone_gallery"), Show("phone_gallery_Lauren") ]

                    if any( [ getattr(store, "{}".format(k), True) for k in sidney_pics_var_list ] ):
                        textbutton _("{image=images/interface_images/phone_screen_images/folder_phone_small.png} Sidney's pictures"):
                            text_style ("phone_gallery_text_style")
                            action [ Hide("phone_gallery"), Show("phone_gallery_Sidney") ]

                    if any( [ getattr(store, "{}".format(k), True) for k in aunt_pics_var_list ] ):
                        textbutton _(If(persistent.patreonsafe,
                            "{image=images/interface_images/phone_screen_images/folder_phone_small.png} Aunt Camille's pictures",
                            "{image=images/interface_images/phone_screen_images/folder_phone_small.png} Aunt Camille's pictures")):
                            text_style ("phone_gallery_text_style")
                            action [ Hide("phone_gallery"), Show("phone_gallery_Aunt") ]

                    if any( [ getattr(store, "{}".format(k), True) for k in cousin_pics_var_list ] ):
                        textbutton _(If(persistent.patreonsafe,
                            "{image=images/interface_images/phone_screen_images/folder_phone_small.png} Cousin Mandy's pictures",
                            "{image=images/interface_images/phone_screen_images/folder_phone_small.png} Cousin Mandy's pictures")):
                            text_style ("phone_gallery_text_style")
                            action [ Hide("phone_gallery"), Show("phone_gallery_Mandy") ]


            #vbar value YScrollValue("stats_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG


    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("phone_gallery"), Show("phone_interface") ]
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
### Mom's phone gallery screen

screen phone_gallery_mom():

#    if persistent.patreonsafe:
#        $ Mom = mom_name
#        $ mom = mom_name
#        $ Dad = dad_name
#        $ dad = dad_name
#        $ uncle = uncle_name
#        $ Uncle = uncle_name
#        $ Auntie = auntie_name
#        $ auntie = auntie_name
#        $ Auntie_2 = ""
#        $ auntie_2 = ""
#    else:
#        $ Mom = "Mom"
#        $ mom = "mom"
#        $ Dad = "Dad"
#        $ dad = "dad"
#        $ uncle = "uncle " + uncle_name
#        $ Uncle = "Uncle " + uncle_name
#        $ Auntie = "Aunt " + auntie_name_short
#        $ auntie = "aunt " + auntie_name_short
#        $ Auntie_2 = "Aunt "
#        $ auntie_2 = "aunt "

    style_prefix "phone_gall"

    add "MobileScreen.png"
    modal True

    frame xalign .495 yalign .297:# at truecenter:
        background None
        has vbox

        text _("{image=images/interface_images/phone_screen_images/folder_phone_small.png} Mom's pictures") style "phone_gallery_text_style" at center

        side ("c"):
            area (1,0,315,510)
            viewport id "stats_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:

                    text _("") size 10

                    if progress >= 3:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Mom's club pic 01"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_mom_1")

                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Mom's club pic 02"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_mom_2")

                    if ntr_club_pic_01:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Mom's club pic 03 (NTR)"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_mom_6")

                    if spycammomshower:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Mom's shower spy pic 01"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_mom_3")

                    if spycammommbatebath:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Mom's shower spy pic 02"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_mom_4")

                    if mommbateonspycam:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Mom's room spy pic 01"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_mom_5")

                    if not ntrcontent:
                        if ntr_club_pic_01:
                            textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} \"NTR\" Mom's pole dance pic 01"):
                                text_size 18
                                text_style ("phone_gallery_text_style")
                                action ui.callsinnewcontext("label_gal_creepshot_mom_6")

                    if mom_CreepShot_06:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Mom's ass in the basement"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_mom_7")

            #vbar value YScrollValue("stats_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG


    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("phone_gallery_mom"), Show("phone_gallery") ]
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
### Lauren's phone gallery screen

screen phone_gallery_Lauren():
    style_prefix "phone_gall"

    add "MobileScreen.png"
    modal True

    frame xalign .495 yalign .297:# at truecenter:
        background None
        has vbox

        text _("{image=images/interface_images/phone_screen_images/folder_phone_small.png} Lauren's pictures") style "phone_gallery_text_style" at center

        side ("c"):
            area (1,0,315,510)
            viewport id "stats_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:

                    text _("") size 10

                    if laurenprogress >= 2:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Lauren's room spy pic 01"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_Lauren_1")

                    if laurenmbateonspycam:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Lauren's room spy pic 02"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_Lauren_4")

                    if spycamlaurenshower:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Lauren's shower spy pic 01"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_Lauren_2")

                    if spycamlaurenmbatebath:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Lauren's shower spy pic 02"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_Lauren_3")



            #vbar value YScrollValue("stats_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG


    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("phone_gallery_Lauren"), Show("phone_gallery") ]
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
### Sidney's phone gallery screen

screen phone_gallery_Sidney():
    style_prefix "phone_gall"

    add "MobileScreen.png"
    modal True

    frame xalign .495 yalign .297:# at truecenter:
        background None
        has vbox

        text _("{image=images/interface_images/phone_screen_images/folder_phone_small.png} Sidney's pictures") style "phone_gallery_text_style" at center

        side ("c"):
            area (1,0,315,510)
            viewport id "stats_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:

                    text _("") size 10

                    if picturesofsidney:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Sidney's room spy pic 01"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_Sidney_1")

                    if sidneymbateonspycam:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Sidney's room spy pic 02"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_Sidney_4")

                    if spycamsidneyshower:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Sidney's shower spy pic 02"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_Sidney_2")

                    if spycamsidneymbatebath:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Sidney's shower spy pic 03"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_Sidney_3")


            #vbar value YScrollValue("stats_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG


    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("phone_gallery_Sidney"), Show("phone_gallery") ]
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
### Cousin Mandy's phone gallery screen

screen phone_gallery_Mandy():
    style_prefix "phone_gall"

    add "MobileScreen.png"
    modal True

    frame xalign .495 yalign .297:# at truecenter:
        background None
        has vbox

        text _("{image=images/interface_images/phone_screen_images/folder_phone_small.png} Mandy's pictures") style "phone_gallery_text_style" at center

        side ("c"):
            area (1,0,315,510)
            viewport id "stats_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:

                    text _("") size 10

                    if spycammandyshower:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Mandy's shower spy pic 01"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_cousin_1")

                    if spycammandymbatebath:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Mandy's shower spy pic 02"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_cousin_2")

                    if mandymbatespycam:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Mandy's room spy pic 01"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_cousin_3")


                    if first_mandy_study_visit:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Mandy's room spy pic 02"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_cousin_4")

            #vbar value YScrollValue("stats_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG


    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("phone_gallery_Mandy"), Show("phone_gallery") ]
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
### Aunt's phone gallery screen

screen phone_gallery_Aunt():
    style_prefix "phone_gall"

    add "MobileScreen.png"
    modal True

    frame xalign .495 yalign .297:# at truecenter:
        background None
        has vbox

        text _("{image=images/interface_images/phone_screen_images/folder_phone_small.png} Camille's pictures") style "phone_gallery_text_style" at center

        side ("c"):
            area (1,0,315,510)
            viewport id "stats_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:

                    text _("") size 10

                    if first_lounge_clean:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Camille's pic 01"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_aunt_1")

                    if first_bath_clean:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Camille's pic 02"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_aunt_2")

                    if kitchen_boobs:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Camille's pic 03"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_aunt_3")

                    if spycamauntshower:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Camille's shower spy pic 04"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_aunt_4")

                    if spycamauntmbatebath:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Camille's shower spy pic 05"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_aunt_5")

                    if auntmbatespycam:
                        textbutton _("{image=images/interface_images/phone_screen_images/images_phone.png} Camille's room spy pic 06"):
                            text_size 18
                            text_style ("phone_gallery_text_style")
                            action ui.callsinnewcontext("label_gal_creepshot_aunt_6")

            #vbar value YScrollValue("stats_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG


    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("phone_gallery_Aunt"), Show("phone_gallery") ]
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
