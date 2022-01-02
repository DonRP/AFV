
####################################################################################################################################################
### Patreon Gallery
####################################################################################################################################################
### Powerd by D.S.-sama ############################################################################################################################
####################################################################################################################################################
####################################################################################################################################################


####################################################################################################################################################
### Mod variable
####################################################################################################################################################
define persistent.patreon_gal_screens_on = True
####################################################################################################################################################

####################################################################################################################################################
### Patreon Gallery $5

screen gallery_patreon_5():
    tag menu

    use game_menu(_("                          Supporter's gallery"), scroll="page"):

        fixed:

            ### The grid of file slots.
            vpgrid cols gui.file_slot_cols:
                mousewheel True
                arrowkeys True
                draggable True
                scrollbars "vertical"
                side_xalign 0.0
                ypos 270
                ymaximum 1000
                style_prefix "slot"
                xalign 0.45
                yalign 0.5
                spacing gui.slot_spacing

                for i in range(1 * 1):

                    $ slot = i + 1

                    imagebutton:
                            idle "patreon_KittyPark01_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_patreon_KittyPark01")

                    imagebutton:
                            idle "patreon_Bondage_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_patreon_Bondage")

                    imagebutton:
                            idle "patreon_LockerRoomBonus_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_patreon_LockerRoomBonus")

                    imagebutton:
                            idle "patreon_Easter01_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_patreon_Easter01")

                    imagebutton:
                            idle "patreon_Easter02_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_patreon_Easter02")

                    imagebutton:
                            idle "patreon_M_DayKitchen_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_patreon_M_DayKitchen")

                    imagebutton:
                            idle "patreon_TrickorTreat_01_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_patreon_TrickorTreat_01")

                    imagebutton:
                            idle "patreon_SidneyXmas_01_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_patreon_SidneyXmas_01")

                    imagebutton:
                            idle "patreon_VDay_01_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_patreon_VDay_01")

                    imagebutton:
                            idle "patreon_LaurenWP_01_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_patreon_LaurenWP_01")

                    imagebutton:
                            idle "patreon_LaurenWP_02_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_patreon_LaurenWP_02")

                    imagebutton:
                            idle "patreon_CheerCarWash_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_patreon_CheerCarWash")

                    imagebutton:
                            idle "patreon_SwimMeet_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_patreon_SwimMeet")

                    imagebutton:
                            idle "patreon_WombRaider_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_patreon_WombRaider")

                    imagebutton:
                            idle "images/interface_images/gallery_images/label_gal_no_bg.png"
                            action NullAction()

    imagebutton auto "images/interface_images/Button_backgal_%s.png" xpos 600 ypos 660 focus_mask True action ShowMenu("gallery8")

    if patreon_level == "$10":
        imagebutton auto "images/interface_images/Button_nextgal_%s.png" xpos 848 ypos 660 focus_mask True action ShowMenu("gallery_patreon_10")
    else:
        imagebutton auto "images/interface_images/Button_nextgal_%s.png" xpos 848 ypos 660 focus_mask True action ShowMenu("gallery_commissions")

####################################################################################################################################################
### Patreon Gallery $10

screen gallery_patreon_10():
    tag menu

    use game_menu(_("                               Supporter's gallery $10"), scroll="page"):

        fixed:

            ### The grid of file slots.
            vpgrid cols gui.file_slot_cols:
                mousewheel True
                arrowkeys True
                draggable True
                scrollbars "vertical"
                side_xalign 0.0
                ypos 270
                ymaximum 1000
                style_prefix "slot"
                xalign 0.45
                yalign 0.5
                spacing gui.slot_spacing

                for i in range(1 * 1):

                    $ slot = i + 1

                    imagebutton:
                            idle "patreon_KittyPark01_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_patreon_KittyPark01")

                    imagebutton:
                            idle "images/interface_images/gallery_images/label_gal_no_bg.png"
                            action NullAction()

                    imagebutton:
                            idle "images/interface_images/gallery_images/label_gal_no_bg.png"
                            action NullAction()

                    imagebutton:
                            idle "images/interface_images/gallery_images/label_gal_no_bg.png"
                            action NullAction()

                    imagebutton:
                            idle "images/interface_images/gallery_images/label_gal_no_bg.png"
                            action NullAction()

                    imagebutton:
                            idle "images/interface_images/gallery_images/label_gal_no_bg.png"
                            action NullAction()

                    imagebutton:
                            idle "images/interface_images/gallery_images/label_gal_no_bg.png"
                            action NullAction()

                    imagebutton:
                            idle "images/interface_images/gallery_images/label_gal_no_bg.png"
                            action NullAction()

                    imagebutton:
                            idle "images/interface_images/gallery_images/label_gal_no_bg.png"
                            action NullAction()

    imagebutton auto "images/interface_images/Button_backgal_%s.png" xpos 600 ypos 660 focus_mask True action ShowMenu("gallery_patreon_5")

    imagebutton auto "images/interface_images/Button_nextgal_%s.png" xpos 848 ypos 660 focus_mask True action ShowMenu("gallery_commissions")

####################################################################################################################################################
### Patreon Gallery Commissioned

screen gallery_commissions():
    tag menu

    use game_menu(_("            Patreon/Subscribestar Commissions"), scroll="page"):

        fixed:

            ### The grid of file slots.
            vpgrid cols gui.file_slot_cols:
                mousewheel True
                arrowkeys True
                draggable True
                scrollbars "vertical"
                side_xalign 0.0
                ypos 270
                ymaximum 1000
                style_prefix "slot"
                xalign 0.45
                yalign 0.5
                spacing gui.slot_spacing

                for i in range(1 * 1):

                    $ slot = i + 1

                    imagebutton:
                            idle "commissions_N7_01_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_commissions_N7_01")

                    imagebutton:
                            idle "commissions_Frayed80_01_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_commissions_Frayed80_01")

                    imagebutton:
                            idle "commissions_FrayedCommish_0_04_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_commissions_Frayed80_02")

                    imagebutton:
                            idle "commissions_StreetWalkers_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_commissions_StreetWalkers")

                    imagebutton:
                            idle "commissions_StrenifComish_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_commissions_StrenifComish")

                    imagebutton:
                            idle "commissions_UrqyComish_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_commissions_UrqyComish")

                    imagebutton:
                            idle "commissions_Jtf1357_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_commissions_Jtf1357")

                    imagebutton:
                            idle "commissions_TarakisComish_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_commissions_TarakisComish")

                    imagebutton:
                            idle "commissions_ElthaunComish_small"
                            idle_foreground "gallery_idle"
                            action ui.callsinnewcontext("label_gal_commissions_ElthaunComish")

    if patreon_level != "$10":
        imagebutton auto "images/interface_images/Button_backgal_%s.png" xpos 600 ypos 660 focus_mask True action ShowMenu("gallery_patreon_5")
    else:
        imagebutton auto "images/interface_images/Button_backgal_%s.png" xpos 600 ypos 660 focus_mask True action ShowMenu("gallery_patreon_10")

    imagebutton auto "images/interface_images/Button_nextgal_%s.png" xpos 848 ypos 660 focus_mask True action ShowMenu("gallery")
