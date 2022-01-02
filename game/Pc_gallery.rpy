
####################################################################################################################################################
### Powerd by D.S.-sama ############################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

### The spacing between file slots.
define gui.slot_spacing_pc = 5
define gui.slot_spacing_pc_img = 5
define pc_gal_cousin = False
define pc_gal_aunt = False

define mom_pics_var_list= [ "spycammomshower",
    "spycammommbatebath",
    "mommbateonspycam",
    "ntr_club_pic_01",
    "mom_CreepShot_06"
    ]

define sidney_pics_var_list = [ "picturesofsidney",
    "spycamsidneyshower",
    "spycamsidneymbatebath",
    "sidneymbateonspycam" ]

define cousin_pics_var_list = [ "spycammandyshower",
    "spycammandymbatebath",
    "mandymbatespycam",
    "first_mandy_study_visit" ]

define aunt_pics_var_list = [ "first_lounge_clean",
    "first_bath_clean",
    "kitchen_boobs",
    "spycamauntshower",
    "spycamauntmbatebath",
    "auntmbatespycam" ]

init 1000 python:
    config.underlay.append(
        renpy.Keymap(
            n = lambda: renpy.run(
                If( pc_gal_aunt,
                    [ SetVariable("pc_gal_aunt", False) ],
                    [ SetVariable("pc_gal_aunt", True) ]
                    )
                )
            )
        )

    config.underlay.append(
        renpy.Keymap(
            m = lambda: renpy.run(
                If( pc_gal_cousin,
                    [ SetVariable("pc_gal_cousin", False) ],
                    [ SetVariable("pc_gal_cousin", True) ]
                    )
                )
            )
        )

####################################################################################################################################################
### Pc screen

init 2 screen desktopcompmap():

    add "bg Desktop_1"


    imagebutton idle "images/interface_images/pc_gallery_images/Pc_gal_Folder_icon_idle.png" hover_foreground "images/interface_images/pc_gallery_images/Pc_gal_Folder-Desktop-icon_hover.png" xpos 1034 ypos 170 focus_mask True action [ Hide("desktopcompmap"), Show("Pc_gallery") ]
    if progress >= 4:
        imagebutton idle "images/interface_images/pc_gallery_images/Ffox_idle.png" hover_foreground "images/interface_images/pc_gallery_images/Ffox_hover.png" xpos 1053 ypos 350 focus_mask True action [ Hide("desktopcompmap"), Jump("booble_search") ]
    imagebutton auto "images/interface_images/Pc_on_off_%s.png" xpos 1123 ypos 600 focus_mask True action [ Hide("desktopcompmap"), Hide("Cosplay_gallery"), Hide("Cosplay_outfits_gallery"), Jump("myroom") ]



screen Pc_gallery():

    add "bg DesktopFolder_1"

    fixed:

        ### The grid of file slots.
        vpgrid cols gui.file_slot_cols:
            mousewheel True
            arrowkeys True
            draggable True
            scrollbars "vertical"
            side_xalign 0.0
            ypos 438
            ymaximum 542
            style_prefix "slot"
            xalign 0.68
            yalign 0.48
            spacing gui.slot_spacing_pc

            for i in range(1 * 1):

                $ slot = i + 1

                if progress >= 3:
                    imagebutton:
                        idle "Pc_gal_Jacky_Folder-Desktop-icon_idle"
                        hover_foreground "images/interface_images/pc_gallery_images/Pc_gal_Folder_hover.png"
                        focus_mask True
                        action [ Hide("Pc_gallery"), Show("Pc_gallery_mom") ]
                else:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                if laurenprogress >= 2:
                    imagebutton:
                        idle "Pc_gal_Lauren_Folder-Desktop-icon_idle"
                        hover_foreground "images/interface_images/pc_gallery_images/Pc_gal_Folder_hover.png"
                        focus_mask True
                        action [ Hide("Pc_gallery"), Show("Pc_gallery_Lauren") ]
                else:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                if any( [ getattr(store, "{}".format(k), True) for k in sidney_pics_var_list ] ):#picturesofsidney:
                    imagebutton:
                        idle "Pc_gal_Sidney_Folder-Desktop-icon_idle"
                        hover_foreground "images/interface_images/pc_gallery_images/Pc_gal_Folder_hover.png"
                        focus_mask True
                        action [ Hide("Pc_gallery"), Show("Pc_gallery_Sidney") ]
                else:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                if any( [ getattr(store, "{}".format(k), True) for k in aunt_pics_var_list ] ):#pc_gal_aunt:
                    imagebutton:
                        idle "Pc_gal_Camille_Folder-Desktop-icon_idle"
                        hover_foreground "images/interface_images/pc_gallery_images/Pc_gal_Folder_hover.png"
                        focus_mask True
                        action [ Hide("Pc_gallery"), Show("Pc_gallery_aunt") ]
                else:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                if any( [ getattr(store, "{}".format(k), True) for k in cousin_pics_var_list ] ):#pc_gal_cousin:
                    imagebutton:
                        idle "Pc_gal_Mandy_Folder-Desktop-icon_idle"
                        hover_foreground "images/interface_images/pc_gallery_images/Pc_gal_Folder_hover.png"
                        focus_mask True
                        action [ Hide("Pc_gallery"), Show("Pc_gallery_cousin") ]
                else:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

    imagebutton auto "images/interface_images/close_button_%s.png" xpos 1129 ypos 25 focus_mask True action [ Hide("Pc_gallery"), Show("desktopcompmap") ]

####################################################################################################################################################
### Pc screen Mom

screen Pc_gallery_mom():

    add "bg DesktopFolder_1"

    fixed:

        ### The grid of file slots.
        vpgrid cols gui.file_slot_cols:
            mousewheel True
            arrowkeys True
            draggable True
            scrollbars "vertical"
            side_xalign 0.0
            ypos 438
            ymaximum 542
            style_prefix "slot"
            xalign 0.68
            yalign 0.48
            spacing gui.slot_spacing_pc_img

            for i in range(1 * 1):

                $ slot = i + 1

                if progress >= 3:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_mom_CreepShot_01_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_mom_1")
                else:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()
#                else:
#                    imagebutton:
#                        idle "images/interface_images/gallery_images/locked_no_bg.png"
#                        action NullAction()

                if progress >= 3:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_mom_CreepShot_02_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_mom_2")
                else:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                if spycammomshower:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_mom_CreepShot_03_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_mom_3")
                elif any( [ getattr(store, "{}".format(k), False) for k in mom_pics_var_list if k != "spycammommbatebath" and k != "mommbateonspycam" and k != "ntr_club_pic_01" ] ):
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                if spycammommbatebath:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_mom_CreepShot_04_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_mom_4")
                elif any( [ getattr(store, "{}".format(k), False) for k in mom_pics_var_list if k != "spycammomshower" and k != "mommbateonspycam" and k != "ntr_club_pic_01" ] ):
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                if mommbateonspycam:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_mom_CreepShot_05_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_mom_5")
                elif any( [ getattr(store, "{}".format(k), False) for k in mom_pics_var_list ] ):
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                if mom_CreepShot_06:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_mom_CreepShot_06_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_mom_7")
                elif any( [ getattr(store, "{}".format(k), False) for k in mom_pics_var_list ] ):
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                if not ntrcontent:
                    if ntr_club_pic_01:
                        imagebutton:
                            idle "images/interface_images/pc_gallery_images/Pc_gal_mom_NTR_Club_idle.png"
                            idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_creepshot_mom_6")
                    elif any( [ getattr(store, "{}".format(k), False) for k in mom_pics_var_list ] ):
                        imagebutton:
                            idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                            action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

    imagebutton auto "images/interface_images/close_button_%s.png" xpos 1129 ypos 25 focus_mask True action [ Hide("Pc_gallery_mom"), Show("Pc_gallery") ]

    if progress >= 4:
        imagebutton auto "images/interface_images/pc_gallery_images/Fap_%s.png" xpos 0 ypos 550 focus_mask True action [ Hide("Pc_gallery_mom"), Jump("fap_mom") ]

####################################################################################################################################################
### Pc screen Lauren

screen Pc_gallery_Lauren():

    add "bg DesktopFolder_1"

    fixed:

        ### The grid of file slots.
        vpgrid cols gui.file_slot_cols:
            mousewheel True
            arrowkeys True
            draggable True
            scrollbars "vertical"
            side_xalign 0.0
            ypos 438
            ymaximum 542
            style_prefix "slot"
            xalign 0.68
            yalign 0.48
            spacing gui.slot_spacing_pc_img

            for i in range(1 * 1):

                $ slot = i + 1

                if laurenprogress >= 2:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_Lauren_CreepShot_01_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_Lauren_1")

                if spycamlaurenshower:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_Lauren_CreepShot_02_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_Lauren_2")

                if spycamlaurenmbatebath:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_Lauren_CreepShot_03_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_Lauren_3")

                if laurenmbateonspycam:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_Lauren_CreepShot_04_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_Lauren_4")

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

    imagebutton auto "images/interface_images/close_button_%s.png" xpos 1129 ypos 25 focus_mask True action [ Hide("Pc_gallery_Lauren"), Show("Pc_gallery") ]

    if progress >= 4:
        imagebutton auto "images/interface_images/pc_gallery_images/Fap_%s.png" xpos 0 ypos 550 focus_mask True action [ Hide("Pc_gallery_Lauren"), Jump("fap_lauren") ]

####################################################################################################################################################
### Pc screen Sidney

init 1 screen Pc_gallery_Sidney():

    add "bg DesktopFolder_1"

    fixed:

        ### The grid of file slots.
        vpgrid cols gui.file_slot_cols:
            mousewheel True
            arrowkeys True
            draggable True
            scrollbars "vertical"
            side_xalign 0.0
            ypos 438
            ymaximum 542
            style_prefix "slot"
            xalign 0.68
            yalign 0.48
            spacing gui.slot_spacing_pc_img

            for i in range(1 * 1):

                $ slot = i + 1

                if picturesofsidney:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_Sidney_CreepShot_01_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_Sidney_1")

                if spycamsidneyshower:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_Sidney_CreepShot_02_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_Sidney_2")

                if spycamsidneymbatebath:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_Sidney_CreepShot_03_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_Sidney_3")

                if sidneymbateonspycam:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_Sidney_CreepShot_04_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_Sidney_4")

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

    imagebutton auto "images/interface_images/close_button_%s.png" xpos 1129 ypos 25 focus_mask True action [ Hide("Pc_gallery_Sidney"), Show("Pc_gallery") ]

    if picturesofsidney:
        imagebutton auto "images/interface_images/pc_gallery_images/Fap_%s.png" xpos 0 ypos 550 focus_mask True action [ Hide("Pc_gallery_Sidney"), Jump("fap_sidney") ]

####################################################################################################################################################
### Pc screen Aunt

init 1 screen Pc_gallery_aunt():

    add "bg DesktopFolder_1"

    fixed:

        ### The grid of file slots.
        vpgrid cols gui.file_slot_cols:
            mousewheel True
            arrowkeys True
            draggable True
            scrollbars "vertical"
            side_xalign 0.0
            ypos 438
            ymaximum 542
            style_prefix "slot"
            xalign 0.68
            yalign 0.48
            spacing gui.slot_spacing_pc_img

            for i in range(1 * 1):

                $ slot = i + 1

                if first_lounge_clean:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/pc_gal_Aunt_CreepShot_01_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_aunt_1")

                if first_bath_clean:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/pc_gal_Aunt_CreepShot_02_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_aunt_2")

                if kitchen_boobs:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/pc_gal_Aunt_CreepShot_03_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_aunt_3")

                if spycamauntshower:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/pc_gal_Aunt_CreepShot_04_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_aunt_4")

                if spycamauntmbatebath:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/pc_gal_Aunt_CreepShot_05_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_aunt_5")

                if auntmbatespycam:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/pc_gal_Aunt_CreepShot_06_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_aunt_6")

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

    imagebutton auto "images/interface_images/close_button_%s.png" xpos 1129 ypos 25 focus_mask True action [ Hide("Pc_gallery_aunt"), Show("Pc_gallery") ]

    if any( [ getattr(store, "{}".format(k), True) for k in aunt_pics_var_list ] ):
        imagebutton auto "images/interface_images/pc_gallery_images/Fap_%s.png" xpos 0 ypos 550 focus_mask True action [ Hide("Pc_gallery_aunt"), Jump("fap_aunt") ]

####################################################################################################################################################
### Pc screen Cousin

init 1 screen Pc_gallery_cousin():

    add "bg DesktopFolder_1"

    fixed:

        ### The grid of file slots.
        vpgrid cols gui.file_slot_cols:
            mousewheel True
            arrowkeys True
            draggable True
            scrollbars "vertical"
            side_xalign 0.0
            ypos 438
            ymaximum 542
            style_prefix "slot"
            xalign 0.68
            yalign 0.48
            spacing gui.slot_spacing_pc_img

            for i in range(1 * 1):

                $ slot = i + 1

                if spycammandyshower:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_cousin_CreepShot_01_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_cousin_1")

                if spycammandymbatebath:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_cousin_CreepShot_02_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_cousin_2")

                if mandymbatespycam:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_cousin_CreepShot_03_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_cousin_3")

                if first_mandy_study_visit:
                    imagebutton:
                        idle "images/interface_images/pc_gallery_images/Pc_gal_cousin_CreepShot_04_idle.png"
                        idle_foreground "images/interface_images/pc_gallery_images/Pc_gal_idle.png"
                        focus_mask True
                        action ui.callsinnewcontext("label_gal_creepshot_cousin_4")

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

                imagebutton:
                        idle "images/interface_images/pc_gallery_images/label_gal_no_bg.png"
                        action NullAction()

    imagebutton auto "images/interface_images/close_button_%s.png" xpos 1129 ypos 25 focus_mask True action [ Hide("Pc_gallery_cousin"), Show("Pc_gallery") ]

    if any( [ getattr(store, "{}".format(k), True) for k in cousin_pics_var_list ] ):
        imagebutton auto "images/interface_images/pc_gallery_images/Fap_%s.png" xpos 0 ypos 550 focus_mask True action [ Hide("Pc_gallery_cousin"), Jump("fap_cousin") ]

####################################################################################################################################################
### Mom Creepshot Gallery labels

label label_gal_creepshot_mom_1:
    scene bg CreepShot01
    $ renpy.pause ()

    return

label label_gal_creepshot_mom_2:
    scene bg CreepShot02
    $ renpy.pause ()

    return

label label_gal_creepshot_mom_3:
    scene bg MomInShower03
    $ renpy.pause ()

    return

label label_gal_creepshot_mom_4:
    scene bg MomMastBateBath03
    $ renpy.pause ()

    return

label label_gal_creepshot_mom_5:
    scene bg SpyCamMomBedroom09
    $ renpy.pause ()

    return

label label_gal_creepshot_mom_6:
    scene bg NTRClub04
    $ renpy.pause ()

    return

label label_gal_creepshot_mom_7:
    scene bg HoneyDoList52
    $ renpy.pause ()

    return

####################################################################################################################################################
### Lauren Creepshot Gallery labels

label label_gal_creepshot_Lauren_1:
    scene bg LaurenNightPeek1
    $ renpy.pause ()

    return

label label_gal_creepshot_Lauren_2:
    scene bg LaurenInShower03
    $ renpy.pause ()

    return

label label_gal_creepshot_Lauren_3:
    scene bg LaurenMastBateBath03
    $ renpy.pause ()

    return

label label_gal_creepshot_Lauren_4:
    scene bg SpyCamLaurenBedroom06
    $ renpy.pause ()

    return

####################################################################################################################################################
### Sidney Creepshot Gallery labels

label label_gal_creepshot_Sidney_1:
    scene bg PeekSidneyDressingMobile
    $ renpy.pause ()

    return

label label_gal_creepshot_Sidney_2:
    scene bg SidneyInShower03
    $ renpy.pause ()

    return

label label_gal_creepshot_Sidney_3:
    scene bg SidneyMastBateBath03
    $ renpy.pause ()

    return

label label_gal_creepshot_Sidney_4:
    scene bg SpyCamSidneyBedroom04
    $ renpy.pause ()

    return

####################################################################################################################################################
### Aunt Creepshot Gallery labels

label label_gal_creepshot_aunt_1:
    scene bg AuntCreepShot01
    $ renpy.pause ()

    return

label label_gal_creepshot_aunt_2:
    scene bg AuntCreepShot02
    $ renpy.pause ()

    return

label label_gal_creepshot_aunt_3:
    scene bg AuntCreepShot03
    $ renpy.pause ()

    return

label label_gal_creepshot_aunt_4:
    scene bg AuntShower03
    $ renpy.pause ()

    return

label label_gal_creepshot_aunt_5:
    scene bg AuntMbateShower03
    $ renpy.pause ()

    return

label label_gal_creepshot_aunt_6:
    scene bg AuntMastBedroom03
    $ renpy.pause ()

    return

####################################################################################################################################################
### Cousin Creepshot Gallery labels

label label_gal_creepshot_cousin_1:
    scene bg MandyShower02
    $ renpy.pause ()

    return

label label_gal_creepshot_cousin_2:
    scene bg MandyMbateShowerVideo01F01
    $ renpy.pause ()

    return

label label_gal_creepshot_cousin_3:
    scene bg MandMastBedroom08
    $ renpy.pause ()

    return

label label_gal_creepshot_cousin_4:
    scene bg MandyStudy01
    $ renpy.pause ()

    return

####################################################################################################################################################
### Fap Mom labels

label fap_mom:
    if daycounter == 6:
        while timeofdaycounter == 4:
            scene bg Desktop_1
            RT "{i}I don't have time for that. The DeCapos will be here any minute.{/i}"
            call screen Pc_gallery_mom
        if daycounter == 6:
            scene bg MomsPictures01
            RT "{i}Someday I will have you for real!{/i}"
            jump fapmom
    elif timeofdaycounter == 5:
        scene bg Desktop_1
        RT "{i}Nah, I feel like something else right now.{/i}"
        call screen Pc_gallery_mom
    elif start_of_campaign and not campaign_finished and daycounter == 1 and timeofdaycounter == 2:
        scene bg Desktop_1
        RT "{i}I can't waist time. I need to go to school and see how Lauren is doing in the student body election poll.{/i}"
        call screen Pc_gallery_mom
    else:
        scene bg MomsPictures01
        RT "{i}Someday I will have you for real!{/i}"
        jump fapmom

    return

####################################################################################################################################################
### Fap Lauren labels

label fap_lauren:
    if daycounter == 6:
        while timeofdaycounter == 4:
            scene bg Desktop_1
            RT "{i}I don't have time for that. The DeCapos will be here any minute.{/i}"
            call screen Pc_gallery_Lauren
        if daycounter == 6:
            scene bg LaurensPictures01
            RT "{i}Soon I will have you for real!{/i}"
            jump faplauren
    elif timeofdaycounter == 5:
        scene bg Desktop_1
        RT "{i}Nah, I feel like something else right now.{/i}"
        call screen Pc_gallery_Lauren
    elif start_of_campaign and not campaign_finished and daycounter == 1 and timeofdaycounter == 2:
        scene bg Desktop_1
        RT "{i}I can't waist time. I need to go to school and see how Lauren is doing in the student body election poll.{/i}"
        call screen Pc_gallery_Lauren
    else:
        scene bg LaurensPictures01
        RT "{i}Soon I will have you for real!{/i}"
        jump faplauren

    return

####################################################################################################################################################
### Fap Sidney labels

label fap_sidney:
    if daycounter == 6:
        while timeofdaycounter == 4:
            scene bg Desktop_1
            RT "{i}I don't have time for that. The DeCapos will be here any minute.{/i}"
            call screen Pc_gallery_Sidney
        if daycounter == 6:
            scene bg SidneysPictures01
            RT "{i}Why are you so sexy?{/i}"
            jump fapsidney
    elif timeofdaycounter == 5:
        scene bg Desktop_1
        RT "{i}Nah, I feel like something else right now.{/i}"
        call screen Pc_gallery_Sidney
    elif start_of_campaign and not campaign_finished and daycounter == 1 and timeofdaycounter == 2:
        scene bg Desktop_1
        RT "{i}I can't waist time. I need to go to school and see how Lauren is doing in the student body election poll.{/i}"
        call screen Pc_gallery_Sidney
    else:
        scene bg SidneysPictures01
        RT "{i}Why are you so sexy?{/i}"
        jump fapsidney

    return

####################################################################################################################################################
### Fap Aunt labels

label fap_aunt:
    if daycounter == 6:
        while timeofdaycounter == 4:
            scene bg Desktop_1
            RT "{i}I don't have time for that. The DeCapos will be here any minute.{/i}"
            call screen Pc_gallery_Sidney
        if daycounter == 6:
            scene bg AuntPictures01
            RT "{i}Why are you so sexy?{/i}"
            jump fapaunt
    elif timeofdaycounter == 5:
        scene bg Desktop_1
        RT "{i}Nah, I feel like something else right now.{/i}"
        call screen Pc_gallery_aunt
    elif start_of_campaign and not campaign_finished and daycounter == 1 and timeofdaycounter == 2:
        scene bg Desktop_1
        RT "{i}I can't waist time. I need to go to school and see how Lauren is doing in the student body election poll.{/i}"
        call screen Pc_gallery_aunt
    else:
        scene bg AuntPictures01
        RT "{i}Why are you so sexy?{/i}"
        jump fapaunt

    return
###################################################################################################################################################
## Fap Cousin labels

label fap_cousin:
    if daycounter == 6:
        while timeofdaycounter == 4:
            scene bg Desktop_1
            RT "{i}I don't have time for that. The DeCapos will be here any minute.{/i}"
            call screen Pc_gallery_cousin
        if daycounter == 6:
            scene bg AuntPictures01
            RT "{i}Why are you so sexy?{/i}"
            jump fapmandy
    elif timeofdaycounter == 5:
        scene bg Desktop_1
        RT "{i}Nah, I feel like something else right now.{/i}"
        call screen Pc_gallery_cousin
    elif start_of_campaign and not campaign_finished and daycounter == 1 and timeofdaycounter == 2:
        scene bg Desktop_1
        RT "{i}I can't waist time. I need to go to school and see how Lauren is doing in the student body election poll.{/i}"
        call screen Pc_gallery_cousin
    else:
        scene bg MandysPictures01
        RT "{i}Why are you so sexy?{/i}"
        jump fapmandy

    return
