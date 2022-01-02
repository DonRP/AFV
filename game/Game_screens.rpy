
####################################################################################################################################################
### Variables

define show_map = False
define persistent.click_nav = False

init:
    transform week_day_zoom: # too lazy to make another version of each item, we just use ATL to make hovered items super bright
        zoom 0.5 xanchor 0.5 yanchor 0.5

    transform day_time_zoom: # too lazy to make another version of each item, we just use ATL to make hovered items super bright
        zoom 0.3 xanchor 0.5 yanchor 0.5

    python:
        #to show map ------------------------------------------
        config.underlay.append(
            renpy.Keymap(
                x = lambda: renpy.run(
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        If(show_map,
                            [ SetVariable("show_map", False), Hide("nav_house") ],
                            [ SetVariable("show_map", True), Show("nav_house") ]
                            ),
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            If(show_map,
                                [ SetVariable("show_map", False), Hide("nav_school") ],
                                [ SetVariable("show_map", True), Show("nav_school") ]
                                )
                            )
                        )
                    )
                )
            )


####################################################################################################################################################
### Style

style nav_style:
    size 35
    color "#E60000"
#    hover_color "#1DDB16"
    outlines [(3, "#000", 0,0)]
    font "images/interface_images/nav_buttons/Apple Casual Regular.ttf"

####################################################################################################################################################
### House navigation screen

screen nav_house():

    imagebutton xalign 0.25 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_House_RyansRoom_idle.png")
        hover ("images/interface_images/nav_buttons/Button_House_RyansRoom_hover.png")
        if any([screen_on == "{}".format(k) for k in ryan_screens]):
            action NullAction()
        else:
            action [ SetVariable("show_map", False), Hide("nav_house"), Jump("myroom") ]
    text _(" My\nRoom") xalign 0.26 yalign 0.89 style "nav_style"

    imagebutton xalign 0.37 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_House_FamilyRoom_idle.png")
        hover ("images/interface_images/nav_buttons/Button_House_FamilyRoom_hover.png")
        if any([screen_on == "{}".format(k) for k in lounge_screens]):
            action NullAction()
        else:
            action [ SetVariable("show_map", False), Hide("nav_house"), Jump("lounge") ]
    text _("Lounge") xalign 0.37 yalign 0.87 style "nav_style"

    imagebutton xalign 0.49 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_House_Bathroom_idle.png")
        hover ("images/interface_images/nav_buttons/Button_House_Bathroom_hover.png")
        if any([screen_on == "{}".format(k) for k in bath_screens]):
            action NullAction()
        else:
            action [ SetVariable("show_map", False), Hide("nav_house"), Jump("bath") ]
    text _("Bath") xalign 0.49 yalign 0.87 style "nav_style"

    imagebutton xalign 0.61 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_House_Kitchen_idle.png")
        hover ("images/interface_images/nav_buttons/Button_House_Kitchen_hover.png")
        if any([screen_on == "{}".format(k) for k in kitchen_screens]):
            action NullAction()
        else:
            action [ SetVariable("show_map", False), Hide("nav_house"), Jump("kitchen") ]
    text _("Kitchen") xalign 0.61 yalign 0.87 style "nav_style"

    imagebutton xalign 0.73 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_House_MomsRoom_idle.png")
        hover ("images/interface_images/nav_buttons/Button_House_MomsRoom_hover.png")
        if any([screen_on == "{}".format(k) for k in mom_screens]):
            action NullAction()
        else:
            action [ SetVariable("show_map", False), Hide("nav_house"), Jump("momroom") ]
    text _("Mom") xalign 0.723 yalign 0.87 style "nav_style"

    imagebutton xalign 0.85 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_House_LaurenRoom_idle.png")
        hover ("images/interface_images/nav_buttons/Button_House_LaurenRoom_hover.png")
        if any([screen_on == "{}".format(k) for k in lauren_screens]):
            action NullAction()
        else:
            action [ SetVariable("show_map", False), Hide("nav_house"), Jump("laurenroom") ]
    text _("Lauren") xalign 0.845 yalign 0.87 style "nav_style"

    imagebutton xalign 0.97 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_Map_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Map_hover.png")
        action [ SetVariable("show_map", False), Hide("nav_house"), Jump("citymap") ]
    text _("City") xalign 0.945 yalign 0.87 style "nav_style"


####################################################################################################################################################
### House navigation screen

screen nav_school():

    imagebutton xalign 0.25 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_School_Hallway_idle.png")
        hover ("images/interface_images/nav_buttons/Button_School_Hallway_hover.png")
        if any([screen_on == "{}".format(k) for k in school_screens]):
            action NullAction()
        else:
            action [ SetVariable("show_map", False), Hide("nav_school"), Jump("school") ]
    text _("Hallway") xalign 0.25 yalign 0.87 style "nav_style"

    imagebutton xalign 0.4 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_School_Classroom_idle.png")
        hover ("images/interface_images/nav_buttons/Button_School_Classroom_hover.png")
        if any([screen_on == "{}".format(k) for k in class_screens]):
            action NullAction()
        else:
            action [ SetVariable("show_map", False), Hide("nav_school"), Jump("classroom") ]
    text _("Class") xalign 0.405 yalign 0.87 style "nav_style"

    imagebutton xalign 0.55 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_School_BathoomBoys_idle.png")
        hover ("images/interface_images/nav_buttons/Button_School_BathoomBoys_hover.png")
        if any([screen_on == "{}".format(k) for k in schoolbath_screens]):
            action NullAction()
        else:
            action [ SetVariable("show_map", False), Hide("nav_school"), Jump("schoolbathroom") ]
    text _("Bathroom") xalign 0.55 yalign 0.87 style "nav_style"

    imagebutton xalign 0.7 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_School_BathroomGirls_idle.png")
        hover ("images/interface_images/nav_buttons/Button_School_BathroomGirls_hover.png")
        if any([screen_on == "{}".format(k) for k in girlslocker_screens]):
            action NullAction()
        else:
            action [ SetVariable("show_map", False), Hide("nav_school"), Jump("girlslockers") ]
    text _("{size=29} {/size}Girls\nLocker\n{size=25} {/size}Room") xalign 0.695 yalign 0.92 style "nav_style"

    imagebutton xalign 0.85 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_Map_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Map_hover.png")
        action [ SetVariable("show_map", False), Hide("nav_school"), Jump("citymap") ]
    text _("City") xalign 0.835 yalign 0.87 style "nav_style"

####################################################################################################################################################
### House navigation screen

screen nav_new_school():

    imagebutton xalign 0.25 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_School_Hallway_idle.png")
        hover ("images/interface_images/nav_buttons/Button_School_Hallway_hover.png")
        if any([screen_on == "{}".format(k) for k in school_screens]):
            action NullAction()
        else:
            action [ SetVariable("show_map", False), Hide("nav_new_school"), Jump("school") ]
    text _("Hallway") xalign 0.25 yalign 0.87 style "nav_style"

    imagebutton xalign 0.385 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_School_Classroom_idle.png")
        hover ("images/interface_images/nav_buttons/Button_School_Classroom_hover.png")
        if any([screen_on == "{}".format(k) for k in class_screens]):
            action NullAction()
        else:
            action [ SetVariable("show_map", False), Hide("nav_new_school"), Jump("new_classroom") ]
    text _("Class") xalign 0.39 yalign 0.87 style "nav_style"

    imagebutton xalign 0.52 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_School_BathoomBoys_idle.png")
        hover ("images/interface_images/nav_buttons/Button_School_BathoomBoys_hover.png")
        if any([screen_on == "{}".format(k) for k in schoolbath_screens]):
            action NullAction()
        else:
            action [ SetVariable("show_map", False), Hide("nav_new_school"), Jump("newschoolbathroom") ]
    text _("Bathroom") xalign 0.52 yalign 0.87 style "nav_style"

    imagebutton xalign 0.655 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_School_BathroomGirls_idle.png")
        hover ("images/interface_images/nav_buttons/Button_School_BathroomGirls_hover.png")
        if any([screen_on == "{}".format(k) for k in girlslocker_screens]):
            action NullAction()
        else:
            action [ SetVariable("show_map", False), Hide("nav_new_school"), Jump("newgirlslockers") ]
    text _("{size=29} {/size}Girls\nLocker\n{size=25} {/size}Room") xalign 0.655 yalign 0.92 style "nav_style"

    imagebutton xalign 0.79 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_School_Campaign_HQ_idle.png")
        hover ("images/interface_images/nav_buttons/Button_School_Campaign_HQ_hover.png")
        if any([screen_on == "{}".format(k) for k in campaign_screens]):
            action NullAction()
        else:
            action [ SetVariable("show_map", False), Hide("nav_new_school"), Jump("campaign_headquarters") ]
    text _("Campaign\n   HQ") xalign 0.795 yalign 0.9 style "nav_style"

    imagebutton xalign 0.925 yalign 0.93:
        idle ("images/interface_images/nav_buttons/Button_Map_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Map_hover.png")
        action [ SetVariable("show_map", False), Hide("nav_new_school"), Jump("citymap") ]
    text _("City") xalign 0.905 yalign 0.87 style "nav_style"

####################################################################################################################################################
### Image maps

init 1 screen housemap():
    imagemap:
        ground "ImageMapHouse.webp"
        hover "SafeImageMapHouseHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

        hotspot (1131,19,103,106) action [ ToggleScreen("phone_interface") ]
        hotspot (22,12,110,118) action [ ToggleScreen("inventory_screen") ]
        hotspot(119,166,223,221) action [ Hide("housemap"), Jump("momroom") ]
        hotspot (360,144,300,336) action [ Hide("housemap"), Jump("lounge") ]
        hotspot (1018,160,258,212) action [ Hide("housemap"), Jump("citymap") ]
        hotspot (932,389,296,305) action [ Hide("housemap"), Jump("kitchen") ]
        hotspot (642,166,234,160) action [ Hide("housemap"), Jump("bath") ]
        hotspot (330,480,311,214) action [ Hide("housemap"), Jump("myroom") ]
        hotspot(9,480,345,223) action [ Hide("housemap"), Jump("laurenroom") ]

init 1 screen ryanmap():
    imagemap:
        ground "ImageMapRyanRoom.webp"
        hover "ImageMapRyanRoomHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom: #205
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom: #263
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (309, 327, 533, 208) clicked Jump("bed")
        hotspot (1097, 303, 67, 41) clicked Jump("computer")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]
        
    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()
            
    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
    #        focus_mask True
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion") ]
                ]
        
init 1 screen ryanmapnight():
    imagemap:
        ground "MyRoomNight.webp"
        hover "SafeImageMapMyRoomNightHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (309, 327, 533, 208) clicked Jump("bed")
        hotspot (1097, 303, 67, 41) clicked Jump("computer")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()
    
    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen loungemap():
    imagemap:
        ground "ImageMapLounge.webp"
        hover "SafeImageMapLoungeHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("myroom")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (391, 181, 160, 92) clicked Jump("tv")
        hotspot (924, 93, 201, 161) clicked Jump("familypic")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen loungemapnight():
    imagemap:
        ground "ImageMapLoungeNight.webp"
        hover "SafeImageMapLoungeNightHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("myroom")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (391, 181, 160, 92) clicked Jump("tv")
        hotspot (924, 93, 201, 161) clicked Jump("familypic")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen sidneyloungemorningmap():
    imagemap:
        ground "ImageMapSidneyLoungeMorning.webp"
        hover "SafeImageMapLoungeHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("myroom")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (924, 93, 201, 161) clicked Jump("familypic")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen sidneyloungenightmap():
    imagemap:
        ground "ImageMapSidneyLoungeNight.webp"
        hover "SafeImageMapLoungeNightHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("myroom")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (924, 93, 201, 161) clicked Jump("familypic")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen bathmap():
    imagemap:
        ground "bathroom01.webp"
        hover "SafeImageMapBathHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("myroom")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (741, 514, 163, 31) clicked Jump("toilet")
        hotspot (1002, 216, 72, 89) clicked Jump("shower")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen bathdoormap():
    imagemap:
        ground "BathroomDoor.webp"
        hover "BathroomDoor.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("myroom")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen bathdoornightmap():
    imagemap:
        ground "BathroomDoorNight.webp"
        hover "BathroomDoorNight.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("myroom")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("nav_house") ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("nav_school"),
                                Hide("nav_new_school")],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen kitchenmap():
    imagemap:
        ground "ImageMapKitchen.webp"
        hover "SafeImageMapKitchenHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("myroom")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (17, 277, 530, 170) clicked Jump("dishes")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen kitchenmapnight():
    imagemap:
        ground "ImageMapKitchenNight.webp"
        hover "SafeImageMapKitchenNightHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("myroom")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (17, 277, 530, 170) clicked Jump("dishes")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()
    
    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen kitchenmapsleep():
    imagemap:
        ground "ImageMapMomSleepKitchen.webp"
        hover "SafeImageMapKitchenHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("myroom")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (17, 277, 530, 170) clicked Jump("dishes")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen sidneykitchenmap():
    imagemap:
        ground "ImageMapSidneyInKitchen.webp"
        hover "SafeImageMapKitchenHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("myroom")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (17, 277, 530, 170) clicked Jump("dishes")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen momsmap():
    imagemap:
        ground "ImageMapMom.webp"
        hover "ImageMapMomHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("myroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (814, 447, 99, 36) clicked Jump("momnightstand")
        hotspot (976, 346, 202,33) clicked Jump("momdresser")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen momsmapnight():
    imagemap:
        ground "ImageMapMomNight.webp"
        hover "ImageMapMomNightHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("myroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (814, 447, 99, 36) clicked Jump("momnightstand")
        hotspot (976, 346, 202,33) clicked Jump("momdresser")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()
    
    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen momdoormap():
    imagemap:
        ground "MomDoor.webp"
        hover "MomDoor.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("myroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen momdoornightmap():
    imagemap:
        ground "MomDoorNight.webp"
        hover "MomDoorNight.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("myroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen momsleepingnightmap():
    imagemap:
        ground "MomInBedAtNight.webp"
        hover "ImageMapMomNightHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("myroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (814, 447, 99, 36) clicked Jump("momnightstand")
        hotspot (976, 346, 202,33) clicked Jump("momdresser")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen laurenmap():
    imagemap:
        ground "ImageMapLauren.webp"
        hover "SafeImageMapLaurenHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("myroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (684, 265, 22, 87) clicked Jump("laurendresser")
        hotspot (1035, 445, 244, 95) clicked Jump("laurenlaundry")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen laurenmapsleepin():
    imagemap:
        ground "LaurenSleepIn.webp"
        hover "SafeImageMapLaurenHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("myroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (684, 265, 22, 87) clicked Jump("laurendresser")
        hotspot (1035, 445, 244, 95) clicked Jump("laurenlaundry")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen laurenmapnight():
    imagemap:
        ground "NightLauren01.webp"
        hover "SafeImageMapLaurenNightEmptyHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("myroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (684, 265, 22, 87) clicked Jump("laurendresser")
        hotspot (1035, 445, 244, 95) clicked Jump("laurenlaundry")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen laurendoormap():
    imagemap:
        ground "LaurenDoor.webp"
        hover "LaurenDoor.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("myroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()
    
    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen laurendoornightmap():
    imagemap:
        ground "LaurenDoorNight.webp"
        hover "LaurenDoorNight.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("myroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen sidneylaurennightmap():
    imagemap:
        ground "ImageMapLaurenSidneyNight.webp"
        hover "SafeImageMapLaurenNightEmptyHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("myroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (684, 265, 22, 87) clicked Jump("laurendresser")
        hotspot (1035, 445, 244, 95) clicked Jump("laurenlaundry")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen sidneysleepinmap():
    imagemap:
        ground "ImageMapSidneySleepIn.webp"
        hover "SafeImageMapLaurenHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("myroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (684, 265, 22, 87) clicked Jump("laurendresser")
        hotspot (1035, 445, 244, 95) clicked Jump("laurenlaundry")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen sidneylaurensleepingmap():
    imagemap:
        ground "ImageMapLaurenSidneySleeping.webp"
        hover "SafeImageMapLaurenHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("myroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (684, 265, 22, 87) clicked Jump("laurendresser")
        hotspot (1035, 445, 244, 95) clicked Jump("laurenlaundry")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action Jump("myroom")

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen desktopcompmap():
    add "bg Desktop"

    imagebutton auto "/Pc_gal/Pc_gal_Folder_icon_%s.png" xpos 1034 ypos 170 focus_mask True action [ Hide("desktopcompmap"), Show("Pc_gallery") ]
    imagebutton auto "/Pc_gal/Pc_on_off_%s.png" xpos 1123 ypos 600 focus_mask True action [ Jump("myroom") ]

init 1 screen familyphotomap():
    imagemap:
        ground "ImageMapFamilyPhoto.webp"
        hover "ImageMapFamilyPhotoHover.webp"

        imagebutton xpos .03 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .09 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

        hotspot (255, 431, 210, 212) clicked If( in_family_photomap,
            [ ui.callsinnewcontext("sidney") ],
            [ Jump("sidney") ] )
        hotspot (496, 428, 192, 193) clicked If( in_family_photomap,
            [ ui.callsinnewcontext("ryan") ],
            [ Jump("ryan") ] )
        hotspot (804, 432, 192, 195) clicked If( in_family_photomap,
            [ ui.callsinnewcontext("lauren") ],
            [ Jump("lauren") ] )
        hotspot (435, 83, 149, 179) clicked If( in_family_photomap,
            [ ui.callsinnewcontext("dad") ],
            [ Jump("dad") ] )
        hotspot (719, 186, 161, 165) clicked If( in_family_photomap,
            [ ui.callsinnewcontext("mom") ],
            [ Jump("mom") ] )
        hotspot (1160, 27, 84, 78) clicked If( in_family_photomap,
            [ Hide("familyphotomap"),
            Show("event_screen"),
            SetVariable("in_family_photomap", False) ],
            [ Jump("backbutton") ] )

init 1 screen citymapmap():
    imagemap:
        ground "ImagemapMap.webp"
        hover "ImagemapMapHover.webp"

        hotspot (161, 38, 140, 99) clicked Jump("school")
        hotspot (148, 329, 113, 99) clicked Jump("myroom")
        hotspot (635, 88, 103, 100) clicked Jump("stripclub")
        hotspot (849,324,226,103) clicked Jump("warehouse")

init 1 screen citymapmapnight():
    imagemap:
        ground "ImagemapMapNight.webp"
        hover "ImagemapMapNightHover.webp"

        hotspot (161, 38, 140, 99) clicked Jump("school")
        hotspot (148, 329, 113, 99) clicked Jump("myroom")
        hotspot (635, 88, 103, 100) clicked Jump("stripclub")
        hotspot (849,324,226,103) clicked Jump("warehouse")

init 1 screen classmap():
    imagemap:
        ground "Classroom01.webp"
        hover "ImageMapClassHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("school")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("girlslockers")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen schoolhallmap():
    imagemap:
        ground "SchoolHallway01.webp"
        hover "ImageMapSchoolHallHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("classroom")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("girlslockers")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")
        hotspot (503, 206, 27, 229) clicked Jump("mylocker")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen schoolbathmap():
    imagemap:
        ground "SchoolBathroom01.webp"
        hover "ImageMapSchoolBathHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("school")
#        hotspot (457, 546, 134, 130) clicked Jump("classroom")
#        hotspot (662, 546, 128, 130) clicked Jump("girlslockers")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")
        hotspot (724, 173, 80, 224) clicked Jump("bathstall")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen girlslockermap():
    imagemap:
        ground "LockerRoom.webp"
        hover "ImageMapLockerRoomHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("school")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("classroom")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")
        hotspot (212, 52, 62, 237) clicked Jump("girllocker")

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            if timeofdaycounter == 1:
                idle "Morning.png"
            elif timeofdaycounter == 2:
                idle "LateMorning.png"
            elif timeofdaycounter == 3:
                idle "Afternoon.png"
            elif timeofdaycounter == 4:
                idle "Evening.png"
            else:
                idle "Night.png"
            action NullAction()

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen safewarningintromap():
    imagemap:
        ground "ImageMapWarningIntro.webp"
        hover "ImageMapWarningIntroHover.webp"

        #hotspot (96, 91, 14,12) clicked Jump("truegame")
        hotspot (552, 513, 175, 36) clicked [ Jump("truestart") ]#, SetField(persistent, "patreonsafe", True) ]#
        hotspot (576, 588, 130, 34) clicked Jump("endgame")

init 1 screen laurennightemptymap():
    imagemap:
        ground "ImageMapLaurenNightEmpty.webp"
        hover "SafeImageMapLaurenNightEmptyHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("myroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen ryanwithsidneymap():
    imagemap:
        ground "MyRoomNightWSidney.webp"
        hover "SafeImageMapRyanRoomWSidneyNightHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("lounge")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")
        hotspot (309, 327, 533, 208) clicked Jump("bed")
        hotspot (1097, 303, 67, 41) clicked Jump("computer")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen ntrclassmap():
    imagemap:
        ground "NewClassroom01.webp"
        hover "NewClassroom01.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("school")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("girlslockers")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen momcleanloungemap():
    imagemap:
        ground "ImageMapMomCleanLounge.webp"
        hover "ImageMapMomCleanLounge.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("myroom")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen momcleanloungemap02():
    imagemap:
        ground "ImageMapMomCleanLounge02.webp"
        hover "ImageMapMomCleanLounge02.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("myroom")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen momcleanloungemap03():
    imagemap:
        ground "ImageMapMomCleanLounge03.webp"
        hover "ImageMapMomCleanLounge03.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("myroom")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen laurenponietvmap():
    imagemap:
        ground "LaurenPonieTVMap.webp"
        hover "LaurenPonieTVMap.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 32, 75, 83) clicked ToggleScreen("inventory_screen")
#        hotspot (1117, 25, 124, 98) clicked ToggleScreen("phone_interface")
#        hotspot (75, 548, 136, 132) clicked Jump("myroom")
#        hotspot (283, 548, 136, 132) clicked Jump("bath")
#        hotspot (472, 548, 131, 128) clicked Jump("kitchen")
#        hotspot (662, 548, 129, 129) clicked Jump("momroom")
#        hotspot (850, 545, 132, 131) clicked Jump("laurenroom")
#        hotspot (1042, 548, 128, 128) clicked Jump("citymap")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]


##### Upd 3

init 1 screen pstudioemptymap():
    imagemap:
        ground "ImageMapPStudioEmpty.webp"
        hover "ImageMapPStudioEmptyHover.webp"

        imagebutton xpos .03 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .09 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#            imagebutton xalign .9635 yalign .04:
#                idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
#                hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
#                action [ ToggleScreen("phone_interface") ]

        hotspot (242, 419, 124, 240) clicked [ Jump("htbydshoot") ]
        hotspot (1182, 632, 93, 77) clicked [ Jump("warehousealso") ]

init 1 screen pstudiogscreenmap():
    imagemap:
        ground "ImageMapPStudioGScreen.webp"
        hover "ImageMapPStudioGScreenHover.webp"

        imagebutton xpos .03 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .09 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#            imagebutton xalign .9635 yalign .04:
#                idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
#                hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
#                action [ ToggleScreen("phone_interface") ]

        hotspot (242, 419, 124, 240) clicked [ Jump("htbydshoot") ]
        hotspot (1182, 632, 93, 77) clicked Jump("warehousealso")

init 1 screen pstudiolightsmap():
    imagemap:
        ground "ImageMapPStudioLights.webp"
        hover "ImageMapPStudioLightsHover.webp"

        imagebutton xpos .03 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .09 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#            imagebutton xalign .9635 yalign .04:
#                idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
#                hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
#                action [ ToggleScreen("phone_interface") ]

        hotspot (242, 419, 124, 240) clicked [ Jump("htbydshoot") ]
        hotspot (1182, 632, 93, 77) clicked Jump("warehousealso")

init 1 screen pstudiogscreenlightsmap():
    imagemap:
        ground "ImageMapPStudioGScreenLights.webp"
        hover "ImageMapPStudioGScreenLightsHover.webp"

        imagebutton xpos .03 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .09 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#            imagebutton xalign .9635 yalign .04:
#                idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
#                hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
#                action [ ToggleScreen("phone_interface") ]

        hotspot (242, 419, 124, 240) clicked [ Jump("htbydshoot") ]
        hotspot (1182, 632, 93, 77) clicked Jump("warehousealso")


##### Upd 6


init 1 screen pstudiohpmap():
    imagemap:
        ground "ImageMapPStudioHP.webp"
        hover "ImageMapPStudioHPHover.webp"

        imagebutton xpos .03 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .09 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#            imagebutton xalign .9635 yalign .04:
#                idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
#                hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
#                action [ ToggleScreen("phone_interface") ]

        hotspot (242, 419, 124, 240) clicked [ Jump("htbydshoot") ]
        hotspot (469, 400, 172, 311) clicked [ Jump("wrshoot") ]
        hotspot (712, 290, 138, 349) clicked [ Jump("ph_shoot") ]
        hotspot (1182, 632, 93, 77) clicked [ Jump("warehousealso") ]

### Casino

init 1 screen casinomap():
    imagemap:
        ground "ImageMapCasino.webp"
        hover "ImageMapCasinoHover.webp"

        imagebutton xpos .03 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .09 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

        hotspot (95, 184, 115, 100) clicked [ Hide("casinomap"), Show("betBlackJack")]
        hotspot (134, 346, 205, 255) clicked [ Hide("casinomap"), Show("startRoulette")]
        hotspot (452, 574, 247, 139) clicked [ Hide("casinomap"), Jump("casino_exit")]
        hotspot (998, 427, 270, 157) clicked [ Hide("casinomap"), Jump("nightclubbing")]

init 1 screen casinosidneymap():
    imagemap:
        ground "ImageMapCasinoWSidney.webp"
        hover "ImageMapCasinoWSidneyHover.webp"

        imagebutton xpos .03 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .09 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

        hotspot (95, 184, 115, 100) clicked [ Hide("casinosidneymap"), Show("betBlackJack")]
        hotspot (134, 346, 205, 255) clicked [ Hide("casinosidneymap"), Show("startRoulette")]
        hotspot (452, 574, 247, 139) clicked [ Hide("casinosidneymap"), Jump("casino_exit")]
        hotspot (998, 427, 270, 157) clicked [ Hide("casinosidneymap"), Jump("stripper_stage")]
        hotspot (785, 70, 149, 216) clicked [ Hide("casinosidneymap"), Jump("sid_working_club")]

init 1 screen newclassmap():
    imagemap:
        ground "LaurenEvents18.webp"
        hover "LaurenEvents18.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("school")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("girlslockers")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_new_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen dresscodeclassmap():
    imagemap:
        ground "AfterClassAfterDressCode.webp"
        hover "AfterClassAfterDressCode.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("school")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("girlslockers")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_new_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
            unhovered NullAction()
    
    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen nocheerclassmap():
    imagemap:
        ground "AfterClassNoCheerDressCode.webp"
        hover "AfterClassNoCheerDressCode.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("school")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("girlslockers")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_new_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen newschoolhallmap():
    imagemap:
        ground "SchoolHallway01.webp"
        hover "ImageMapSchoolHallHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("classroom")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("girlslockers")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")
        hotspot (503, 206, 27, 229) clicked Jump("mylocker")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_new_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen asseffecthallmap():
    imagemap:
        ground "SchoolHallLaurenAssEffect.webp"
        hover "ImageMapSchoolHallHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("classroom")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("girlslockers")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")
        hotspot (503, 206, 27, 229) clicked Jump("mylocker")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_new_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen badschoolhallmap():
    imagemap:
        ground "SchoolHallLaurenBad.webp"
        hover "ImageMapSchoolHallHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("classroom")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("girlslockers")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")
        hotspot (503, 206, 27, 229) clicked Jump("mylocker")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_new_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen bulbhallmap():
    imagemap:
        ground "SchoolHallLaurenBulb.webp"
        hover "ImageMapSchoolHallHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("classroom")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("girlslockers")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")
        hotspot (503, 206, 27, 229) clicked Jump("mylocker")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_new_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen dragonhallmap():
    imagemap:
        ground "SchoolHallLaurenDragon.webp"
        hover "ImageMapSchoolHallHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("classroom")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("girlslockers")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")
        hotspot (503, 206, 27, 229) clicked Jump("mylocker")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_new_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen goodhallmap():
    imagemap:
        ground "SchoolHallLaurenGood.webp"
        hover "ImageMapSchoolHallHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("classroom")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("girlslockers")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")
        hotspot (503, 206, 27, 229) clicked Jump("mylocker")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_new_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen matthallmap():
    imagemap:
        ground "SchoolHallMatt.webp"
        hover "ImageMapSchoolHallHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("classroom")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("girlslockers")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")
        hotspot (503, 206, 27, 229) clicked Jump("mylocker")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_new_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen dresscodehallmap():
    imagemap:
        ground "SchoolHallDressCode.webp"
        hover "ImageMapSchoolHallHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("classroom")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("girlslockers")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")
        hotspot (503, 206, 27, 229) clicked Jump("mylocker")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_new_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen newschoolbathmap():
    imagemap:
        ground "SchoolBathroom01.webp"
        hover "ImageMapSchoolBathHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("school")
#        hotspot (457, 546, 134, 130) clicked Jump("classroom")
#        hotspot (662, 546, 128, 130) clicked Jump("girlslockers")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")
        hotspot (724, 173, 80, 224) clicked Jump("bathstall")

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_new_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen newgirlslockermap():
    imagemap:
        ground "LockerRoom.webp"
        hover "ImageMapLockerRoomHover.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("school")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("classroom")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")
        hotspot (212, 52, 62, 237) clicked Jump("girllocker")

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            if timeofdaycounter == 1:
                idle "Morning.png"
            elif timeofdaycounter == 2:
                idle "LateMorning.png"
            elif timeofdaycounter == 3:
                idle "Afternoon.png"
            elif timeofdaycounter == 4:
                idle "Evening.png"
            else:
                idle "Night.png"
            action NullAction()

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_new_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]

init 1 screen campaignmap():
    imagemap:
        ground "LaurenEvents79.webp"
        hover "LaurenEvents79.webp"

        imagebutton xpos .13 ypos .1 at week_day_zoom:
            idle "day_of_week"
            action NullAction()

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            idle "time_of_day"
            action NullAction()

#        hotspot (41, 30, 77, 87) clicked ToggleScreen("inventory_screen")
#        hotspot (1136, 26, 97, 96) clicked ToggleScreen("phone_interface")
#        hotspot (258, 547, 131, 129) clicked Jump("school")
#        hotspot (457, 546, 134, 130) clicked Jump("schoolbathroom")
#        hotspot (662, 546, 128, 130) clicked Jump("classroom")
#        hotspot (862, 546, 131, 130) clicked Jump("citymap")
#        hotspot (212, 52, 62, 237) clicked Jump("girllocker")

        imagebutton xpos .19 ypos .1 at day_time_zoom:
            if timeofdaycounter == 1:
                idle "Morning.png"
            elif timeofdaycounter == 2:
                idle "LateMorning.png"
            elif timeofdaycounter == 3:
                idle "Afternoon.png"
            elif timeofdaycounter == 4:
                idle "Evening.png"
            else:
                idle "Night.png"
            action NullAction()

    imagebutton:
        xalign 0.035
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Backpack_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Backpack_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("inventory_screen")
            ]

    imagebutton:
        xalign 0.9635
        yalign 0.04
        idle ("images/interface_images/nav_buttons/Phone_icon_idle.png")
        hover ("images/interface_images/nav_buttons/Phone_icon_hover.png")
        action [ If(show_map,
                [ SetVariable("show_map", False),
                    If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                        [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                        If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                            [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                            NullAction()
                            )
                        )
                    ],
                NullAction()
                ),
            ToggleScreen("phone_interface")
            ]

    if any([screen_on == "{}".format(k) for k in nav_home_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ If(show_map,
                [ SetVariable("show_map", False), Hide("nav_house") ],
                NullAction()),
                [ Hide("{}".format(k)) for k in nav_home_location ],
                Show("housemap") ]
    elif any([screen_on == "{}".format(k) for k in nav_school_location]):
        imagebutton xalign 0.005 yalign 0.93:
            idle ("images/interface_images/nav_buttons/Button_House_Map_idle.png")
            hover ("images/interface_images/nav_buttons/Button_House_Map_hover.png")
            action [ Hide("nav_new_school"), Jump("myroom") ]

    imagebutton:
        xalign 0.12
        yalign 0.93
        idle ("images/interface_images/nav_buttons/Button_Nav_hide_show_idle.png")
        hover ("images/interface_images/nav_buttons/Button_Nav_hide_show_hover.png")
        if persistent.click_nav:
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                action [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
        else:
            action NullAction()
            if any([screen_on == "{}".format(k) for k in nav_home_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_house") ]
            elif any([screen_on == "{}".format(k) for k in nav_school_location]):
                hovered [ ToggleVariable("show_map"), ToggleScreen("nav_new_school") ]
            unhovered NullAction()

    if progress >= 11:
        imagebutton:
            xalign 0.092
            yalign 0.8 #0.04
            idle ("images/interface_images/nav_buttons/PS_idle.png")
            hover ("images/interface_images/nav_buttons/PS_hover.png")
            action [ If(show_map,
                    [ SetVariable("show_map", False),
                        If(any([screen_on == "{}".format(k) for k in nav_home_location]),
                            [ Hide("{}".format(k)) for k in nav_home_location_screens ],
                            If(any([screen_on == "{}".format(k) for k in nav_school_location]),
                                [ Hide("{}".format(k)) for k in nav_school_location_screens ],
                                NullAction()
                                )
                            )
                        ],
                    NullAction()
                    ),
                [ [ Hide("{}".format(k)) for k in all_screens ],
                    Jump("warehous_studion")]
                ]
