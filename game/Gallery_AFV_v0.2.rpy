
####################################################################################################################################################
### Powerd by D.S.-sama ############################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

init 1000 python:

    config.underlay.append(
        renpy.Keymap(
            t = lambda: renpy.run(
                If( gal_test,
                    [ SetVariable("gal_test", False) ],
                    [ SetVariable("gal_test", True) ]
                    )
                )
            )
        )

####################################################################################################################################################
### Gallery buttons image definition
####################################################################################################################################################

image gal_mom_mod_01 = im.Scale("images/DrunkMomRoom01.webp", 300, 176) #Enter specific numbers <--
image gal_mom_mod_02 = im.Scale("images/FrontDoor03.webp", 300, 176) #Enter specific numbers <--

image gal_mom_01 = im.Scale("images/StripPeek001.webp", 300, 176) #Enter specific numbers <--
image gal_mom_02 = im.Scale("images/ClassroomStrip04.webp", 300, 176) #Enter specific numbers <--
image gal_mom_03 = im.Scale("images/MomMastBateBath01.webp", 300, 176) #Enter specific numbers <--
image gal_mom_04_safe = im.Scale("images/SpyCamMomBedroom04.webp", 300, 176) #Enter specific numbers <--
image gal_mom_05 = im.Scale("images/PoolBlue27.webp", 300, 176) #Enter specific numbers <--
image gal_mom_06 = im.Scale("images/MCaughtInOffice05.webp", 300, 176) #Enter specific numbers <--
image gal_mom_07 = im.Scale("images/HoneyDoList03.webp", 300, 176) #Enter specific numbers <--
image gal_mom_08 = im.Scale("images/Office16.webp", 300, 176) #Enter specific numbers <--
image gal_mom_09 = im.Scale("images/PHRead06.webp", 300, 176) #Enter specific numbers <--

image gal_auntie_01 = im.Scale("images/AuntVisit01.webp", 300, 176) #Enter specific numbers <--
image gal_auntie_02 = im.Scale("images/AuntMbateShower02.webp", 300, 176) #Enter specific numbers <--
image gal_auntie_03 = im.Scale("images/AuntMastBedroom03.webp", 300, 176) #Enter specific numbers <--

image gal_Lauren_01 = im.Scale("images/LaurenWakeMe1.webp", 300, 176) #Enter specific numbers <--
image gal_Lauren_02 = im.Scale("images/LaurenRemoteSearch06.webp", 300, 176) #Enter specific numbers <--
image gal_Lauren_03 = im.Scale("images/LaurenMastBateBath01.webp", 300, 176) #Enter specific numbers <--
image gal_Lauren_04 = im.Scale("images/SpyCamLaurenBedroom02.webp", 300, 176) #Enter specific numbers <--
image gal_Lauren_05 = im.Scale("images/DiazVisit03.webp", 300, 176) #Enter specific numbers <--
image gal_Lauren_06 = im.Scale("images/GOT52.webp", 300, 176) #Enter specific numbers <--
image gal_Lauren_07 = im.Scale("images/Assembly29.webp", 300, 176)
image gal_Lauren_08 = im.Scale("images/ShowerRun20.webp", 300, 176)

image gal_Sidney_01 = im.Scale("images/PeekSidneyDressing01.webp", 300, 176) #Enter specific numbers <--
image gal_Sidney_02 = im.Scale("images/SidneyMastBateBath01.webp", 300, 176) #Enter specific numbers <--
image gal_Sidney_03 = im.Scale("images/SpyCamSidneyBedroom02.webp", 300, 176) #Enter specific numbers <--
image gal_Sidney_04 = im.Scale("images/SleepWithSidney43.webp", 300, 176) #Enter specific numbers <--
image gal_Sidney_05 = im.Scale("images/SidneyRun74.webp", 300, 176) #Enter specific numbers <--
image gal_Sidney_06 = im.Scale("images/SidClub31.webp", 300, 176) #Enter specific numbers <--
image gal_Sidney_07 = im.Scale("images/SidSex11.webp", 300, 176) #Enter specific numbers <--
image gal_Sidney_08 = im.Scale("images/WRSex01.webp", 300, 176) #Enter specific numbers <--
image gal_Sidney_09 = im.Scale("images/RunSex05.webp", 300, 176) #Enter specific numbers <--
image gal_Sidney_10 = im.Scale("images/BRSex07.webp", 300, 176) #Enter specific numbers <--

image gal_harem_01 = im.Scale("images/SidneyLaurenSleeping01.webp", 300, 176) #Enter specific numbers <--
image gal_harem_02 = im.Scale("images/ChristmasEvent15.webp", 300, 176) #Enter specific numbers <--
image gal_harem_03 = im.Scale("images/Dare45.webp", 300, 176) #Enter specific numbers <--
image gal_harem_04 = im.Scale("images/DiazAgain09.webp", 300, 176) #Enter specific numbers <--
image gal_harem_05 = im.Scale("images/LaurenRewardVideo03F01.webp", 300, 176)

image gal_other_girls_01 = im.Scale("images/MeganInHall02.webp", 300, 176) #Enter specific numbers <--
image gal_other_girls_02 = im.Scale("images/MrsStonesClass20.webp", 300, 176)
image gal_other_girls_03 = im.Scale("images/ShowMegan06.webp", 300, 176)
image gal_other_girls_04 = im.Scale("images/ElectionHelp04.webp", 300, 176)

image gal_ntr_01 = im.Scale("images/SchoolBathBlow03.webp", 300, 176) #Enter specific numbers <--
image gal_ntr_02 = im.Scale("images/NTRClub06.webp", 300, 176) #Enter specific numbers <--
image gal_ntr_03 = im.Scale("images/SidneyRun15.webp", 300, 176) #Enter specific numbers <--
image gal_ntr_04 = im.Scale("images/Office03.webp", 300, 176) #Enter specific numbers <--
image gal_ntr_05 = im.Scale("images/HPCosplay11.webp", 300, 176) #Enter specific numbers <--
image gal_ntr_06 = im.Scale("images/Assembly15.webp", 300, 176)
image gal_ntr_07 = im.Scale("images/LaurenTrain13.webp", 300, 176)

image gal_cosplay_01 = im.Scale("images/CosplayIntro04.webp", 300, 176) #Enter specific numbers <--
image gal_cosplay_02 = im.Scale("images/HTBYD_F_00.webp", 300, 176) #Enter specific numbers <--
image gal_cosplay_03 = im.Scale("images/SidneyWRShoot18.webp", 300, 176) #Enter specific numbers <--
image gal_cosplay_04 = im.Scale("images/HPCosplay67.webp", 300, 176) #Enter specific numbers <--

image gal_Mandy_01 = im.Scale("images/MandyMbateShower02.webp", 300, 176) #Enter specific numbers <--
image gal_Mandy_02 = im.Scale("images/MandMastBedroom08.webp", 300, 176) #Enter specific numbers <--

####################################################################################################################################################
### Gallery test variable
####################################################################################################################################################

define gal_test = True

define gal_mod = False

define persistent.gal_mom_1 = False
define persistent.gal_mom_2 = False
define persistent.gal_mom_3 = False
define persistent.gal_mom_4 = False
define persistent.gal_mom_5 = False
define persistent.gal_mom_6 = False
define persistent.gal_mom_7 = False
define persistent.gal_mom_8 = False
define persistent.gal_mom_9 = False
define persistent.gal_mom_10 = False

define persistent.gal_Lauren_1 = False
define persistent.gal_Lauren_2 = False
define persistent.gal_Lauren_3 = False
define persistent.gal_Lauren_4 = False
define persistent.gal_Lauren_5 = False
define persistent.gal_Lauren_6 = False
define persistent.gal_Lauren_7 = False
define persistent.gal_Lauren_8 = False
define persistent.gal_Lauren_9 = False
define persistent.gal_Lauren_10 = False

define persistent.gal_Sidney_1 = False
define persistent.gal_Sidney_2 = False
define persistent.gal_Sidney_3 = False
define persistent.gal_Sidney_4 = False
define persistent.gal_Sidney_5 = False
define persistent.gal_Sidney_6 = False
define persistent.gal_Sidney_7 = False
define persistent.gal_Sidney_8 = False
define persistent.gal_Sidney_9 = False
define persistent.gal_Sidney_10 = False

define persistent.gal_harem_1 = False
define persistent.gal_harem_2 = False
define persistent.gal_harem_3 = False
define persistent.gal_harem_4 = False
define persistent.gal_harem_5 = False
define persistent.gal_harem_6 = False
define persistent.gal_harem_7 = False
define persistent.gal_harem_8 = False
define persistent.gal_harem_9 = False
define persistent.gal_harem_10 = False

define persistent.gal_auntie_1 = False
define persistent.gal_auntie_2 = False
define persistent.gal_auntie_3 = False
define persistent.gal_auntie_4 = False
define persistent.gal_auntie_5 = False
define persistent.gal_auntie_6 = False
define persistent.gal_auntie_7 = False
define persistent.gal_auntie_8 = False
define persistent.gal_auntie_9 = False
define persistent.gal_auntie_10 = False

define persistent.gal_other_girls_1 = False
define persistent.gal_other_girls_2 = False
define persistent.gal_other_girls_3 = False
define persistent.gal_other_girls_4 = False
define persistent.gal_other_girls_5 = False
define persistent.gal_other_girls_6 = False
define persistent.gal_other_girls_7 = False
define persistent.gal_other_girls_8 = False
define persistent.gal_other_girls_9 = False
define persistent.gal_other_girls_10 = False

define persistent.gal_NTR_1 = False
define persistent.gal_NTR_2 = False
define persistent.gal_NTR_3 = False
define persistent.gal_NTR_4 = False
define persistent.gal_NTR_5 = False
define persistent.gal_NTR_6 = False
define persistent.gal_NTR_7 = False
define persistent.gal_NTR_8 = False
define persistent.gal_NTR_9 = False
define persistent.gal_NTR_10 = False

define persistent.gal_Cosplay_1 = False
define persistent.gal_Cosplay_2 = False
define persistent.gal_Cosplay_3 = False
define persistent.gal_Cosplay_4 = False
define persistent.gal_Cosplay_5 = False
define persistent.gal_Cosplay_6 = False
define persistent.gal_Cosplay_7 = False
define persistent.gal_Cosplay_8 = False
define persistent.gal_Cosplay_9 = False
define persistent.gal_Cosplay_10 = False

define persistent.gal_Mandy_1 = False
define persistent.gal_Mandy_2 = False
define persistent.gal_Mandy_3 = False
define persistent.gal_Mandy_4 = False
define persistent.gal_Mandy_5 = False
define persistent.gal_Mandy_6 = False
define persistent.gal_Mandy_7 = False
define persistent.gal_Mandy_8 = False
define persistent.gal_Mandy_9 = False
define persistent.gal_Mandy_10 = False

### The spacing between file slots.
define gui.slot_spacing = 12

####################################################################################################################################################
### Gallery screens
####################################################################################################################################################

####################################################################################################################################################
### Gallery No. 1: Mom

screen gallery():
    tag menu

    if persistent.patreonsafe:
        $ Mom = "Mom"
        $ mom = "mom"
        $ mom_name = "Jacky"
        $ Dad = "Dad"
        $ dad = "dad"
        $ dad_name = "Tony"
        $ uncle = "Uncle Bobby"
    else:
        $ Mom = "Mom"
        $ mom = "mom"
        $ mom_name = "Jacky"
        $ Dad = "Dad"
        $ dad = "dad"
        $ dad_name = "Tony"
        $ uncle = "Uncle Bobby"

    use game_menu(_("Mom's gallery"), scroll="page"):

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

                    if gal_mod:
                        if gal_test:
                            imagebutton:
                                idle "gal_mom_mod_01"
                                idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                                focus_mask True
                                action ui.callsinnewcontext("label_gal_mom_drunk")
                        else:
                            imagebutton:
                                idle "images/interface_images/gallery_images/locked.png"
                                action NullAction()

                        if gal_test:
                            imagebutton:
                                idle "gal_mom_mod_02"
                                idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                                focus_mask True
                                action ui.callsinnewcontext("label_gal_mom_yes_to_money")
                        else:
                            imagebutton:
                                idle "images/interface_images/gallery_images/locked.png"
                                action NullAction()

                    if persistent.gal_mom_1:
                        imagebutton:
                            idle "gal_mom_01"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_mom_nightclubbing")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_mom_2:
                        imagebutton:
                            idle "gal_mom_02"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_mom_school_strip")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_mom_3:
                        imagebutton:
                            idle "gal_mom_03"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_mom_fingerselfbath")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_mom_4:
                        imagebutton:
                            if persistent.patch_on:
                                if persistent.patreonsafe:
                                    idle "gal_mom_04_safe"
                                else:
                                    idle "gal_mom_04"
                            else:
                                idle "gal_mom_04_safe"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_mom_spycamroomhorny")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_mom_5:
                        imagebutton:
                            idle "gal_mom_05"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_mom_weekend_pool_01")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_mom_6:
                        imagebutton:
                            idle "gal_mom_06"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_mom_office")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_mom_7:
                        imagebutton:
                            idle "gal_mom_07"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_mom_honey_do")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_mom_8:
                        imagebutton:
                            idle "gal_mom_08"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_mom_blackmailed")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_mom_9:
                        imagebutton:
                            idle "gal_mom_09"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_mom_ph_read")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    imagebutton:
                            idle "images/interface_images/gallery_images/label_gal_no_bg.png"
                            action NullAction()

    if persistent.patreon_gal_screens_on:
        imagebutton auto "images/interface_images/Button_backgal_%s.png" xpos 600 ypos 660 focus_mask True action ShowMenu("gallery_commissions")

    if not persistent.patreon_gal_screens_on:
        imagebutton auto "images/interface_images/Button_backgal_%s.png" xpos 600 ypos 660 focus_mask True action ShowMenu("gallery8")

    imagebutton auto "images/interface_images/Button_nextgal_%s.png" xpos 848 ypos 660 focus_mask True action ShowMenu("gallery2")

####################################################################################################################################################
### Gallery No. 2: Lauren

screen gallery2():
    tag menu

    use game_menu(_("Lauren's gallery"), scroll="page"):

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

                    if persistent.gal_Lauren_1:
                        imagebutton:
                            idle "gal_Lauren_01"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Lauren_wakeRyan")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Lauren_2:
                        imagebutton:
                            idle "gal_Lauren_02"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Lauren_RmtSearch")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Lauren_3:
                        imagebutton:
                            idle "gal_Lauren_03"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Lauren_fingerselfbath")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Lauren_4:
                        imagebutton:
                            idle "gal_Lauren_04"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Lauren_spycamroomhorny")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Lauren_5:
                        imagebutton:
                            idle "gal_Lauren_05"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Lauren_Diaz_01")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Lauren_6:
                        imagebutton:
                            idle "gal_Lauren_06"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Lauren_GOT")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Lauren_7:
                        imagebutton:
                            idle "gal_Lauren_07"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_election_win")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Lauren_8:
                        imagebutton:
                            idle "gal_Lauren_08"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_locker_room_run")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    imagebutton:
                            idle "images/interface_images/gallery_images/label_gal_no_bg.png"
                            action NullAction()

                    imagebutton:
                            idle "images/interface_images/gallery_images/label_gal_no_bg.png"
                            action NullAction()

    imagebutton auto "images/interface_images/Button_backgal_%s.png" xpos 600 ypos 660 focus_mask True action ShowMenu("gallery")

    imagebutton auto "images/interface_images/Button_nextgal_%s.png" xpos 848 ypos 660 focus_mask True action ShowMenu("gallery3")

####################################################################################################################################################
### Gallery No. 3: Sidney

screen gallery3():
    tag menu

    use game_menu(_("Sidney's gallery"), scroll="page"):

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

                    if persistent.gal_Sidney_1:
                        imagebutton:
                            idle "gal_Sidney_01"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Sidney_PeekDressing")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Sidney_2:
                        imagebutton:
                            idle "gal_Sidney_02"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Sidney_fingerselfbath")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Sidney_3:
                        imagebutton:
                            idle "gal_Sidney_03"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Sidney_spycamroomhorny")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Sidney_4:
                        imagebutton:
                            idle "gal_Sidney_04"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Sidney_Ryan_room")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Sidney_5:
                        imagebutton:
                            idle "gal_Sidney_05"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Sidney_park_activities")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Sidney_6:
                        imagebutton:
                            idle "gal_Sidney_06"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Sidney_club_trick")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Sidney_7:
                        imagebutton:
                            idle "gal_Sidney_07"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Sidney_sex")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Sidney_8:
                        imagebutton:
                            idle "gal_Sidney_08"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Sidney_WR_sex")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Sidney_9:
                        imagebutton:
                            idle "gal_Sidney_09"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Sidney_park_sex")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Sidney_10:
                        imagebutton:
                            idle "gal_Sidney_10"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Sidney_BR_sex")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    imagebutton:
                            idle "images/interface_images/gallery_images/label_gal_no_bg.png"
                            action NullAction()

    imagebutton auto "images/interface_images/Button_backgal_%s.png" xpos 600 ypos 660 focus_mask True action ShowMenu("gallery2")

    imagebutton auto "images/interface_images/Button_nextgal_%s.png" xpos 848 ypos 660 focus_mask True action ShowMenu("gallery4")

####################################################################################################################################################
### Gallery No. 4: Aunt Camille

screen gallery4():
    tag menu

    use game_menu(_("Aunt Camille's gallery"), scroll="page"):

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

                    if persistent.gal_auntie_1:
                        imagebutton:
                            idle "gal_auntie_01"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_aunt_01")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_auntie_2:
                        imagebutton:
                                idle "gal_auntie_02"
                                idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                                focus_mask True
                                action ui.callsinnewcontext("label_gal_aunt_02")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_auntie_3:
                        imagebutton:
                                idle "gal_auntie_03"
                                idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                                focus_mask True
                                action ui.callsinnewcontext("label_gal_aunt_03")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
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

    imagebutton auto "images/interface_images/Button_backgal_%s.png" xpos 600 ypos 660 focus_mask True action ShowMenu("gallery3")

    imagebutton auto "images/interface_images/Button_nextgal_%s.png" xpos 848 ypos 660 focus_mask True action ShowMenu("gallery5")

####################################################################################################################################################
### Gallery No. 5: Cousin Mandy

screen gallery5():
    tag menu

    use game_menu(_("Mandy's gallery"), scroll="page"):

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

                    if persistent.gal_Mandy_1:
                        imagebutton:
                            idle "gal_Mandy_01"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_mandy_01")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Mandy_2:
                        imagebutton:
                                idle "gal_Mandy_02"
                                idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                                focus_mask True
                                action ui.callsinnewcontext("label_gal_mandy_02")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
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

    imagebutton auto "images/interface_images/Button_backgal_%s.png" xpos 600 ypos 660 focus_mask True action ShowMenu("gallery4")

    imagebutton auto "images/interface_images/Button_nextgal_%s.png" xpos 848 ypos 660 focus_mask True action ShowMenu("gallery6")

####################################################################################################################################################
### Gallery No. 6: Sidney&Lauren

screen gallery6():
    tag menu

    use game_menu(_("Harem \n     gallery"), scroll="page"):

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

                    if persistent.gal_harem_1:
                        imagebutton:
                            idle "gal_harem_01"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Sidney_and_Lauren_Sleeping_events")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_harem_2:
                        imagebutton:
                            idle "gal_harem_02"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_Xmas_event")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_harem_3:
                        imagebutton:
                            idle "gal_harem_03"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_truth_dare")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_harem_4:
                        imagebutton:
                            idle "gal_harem_04"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_diaz_again")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_harem_5:
                        imagebutton:
                            idle "gal_harem_05"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_best_polls_aftermath")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
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

    imagebutton auto "images/interface_images/Button_backgal_%s.png" xpos 600 ypos 660 focus_mask True action ShowMenu("gallery5")

    imagebutton auto "images/interface_images/Button_nextgal_%s.png" xpos 848 ypos 660 focus_mask True action ShowMenu("gallery7")

####################################################################################################################################################
### Gallery No. 7: Other girls

screen gallery7():
    tag menu

    use game_menu(_("Other girls gallery"), scroll="page"):

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

                    if persistent.gal_other_girls_1:
                        imagebutton:
                            idle "gal_other_girls_01"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_other_girls_stallbj")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_other_girls_2:
                        imagebutton:
                            idle "gal_other_girls_02"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_finished_painting")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_other_girls_3:
                        imagebutton:
                            idle "gal_other_girls_03"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_talk_to_megan")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_other_girls_4:
                        imagebutton:
                            idle "gal_other_girls_04"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_diaz_help")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
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

    imagebutton auto "images/interface_images/Button_backgal_%s.png" xpos 600 ypos 660 focus_mask True action ShowMenu("gallery6")

    imagebutton auto "images/interface_images/Button_nextgal_%s.png" xpos 848 ypos 660 focus_mask True action ShowMenu("gallery8")

####################################################################################################################################################
### Gallery No. 8: NTR

screen gallery8():
    tag menu

    use game_menu(_("NTR gallery"), scroll="page"):

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

                    if persistent.gal_NTR_1:
                        imagebutton:
                            idle "gal_ntr_01"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_ntr_stallbj")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_NTR_2:
                        imagebutton:
                            idle "gal_ntr_02"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_ntr_club")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_NTR_3:
                        imagebutton:
                            idle "gal_ntr_03"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_mr_peterson")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_NTR_4:
                        imagebutton:
                            idle "gal_ntr_04"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_ntr_blackmail")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_NTR_5:
                        imagebutton:
                            idle "gal_ntr_05"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_ntr_ph")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_NTR_6:
                        imagebutton:
                            idle "gal_ntr_06"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_election_lose")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_NTR_7:
                        imagebutton:
                            idle "gal_ntr_07"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_bad_polls_aftermath")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
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

    imagebutton auto "images/interface_images/Button_backgal_%s.png" xpos 600 ypos 660 focus_mask True action ShowMenu("gallery7")

    imagebutton auto "images/interface_images/Button_nextgal_%s.png" xpos 848 ypos 660 focus_mask True action ShowMenu("gallery9")

####################################################################################################################################################
### Gallery No. 9: Cosplay

screen gallery9():
    tag menu

    use game_menu(_("Cosplay gallery"), scroll="page"):

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

                    if persistent.gal_Cosplay_1:
                        imagebutton:
                            idle "gal_cosplay_01"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_cosplay_01")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Cosplay_2:
                        imagebutton:
                            idle "gal_cosplay_02"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_cosplay_02")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Cosplay_3:
                        imagebutton:
                            idle "gal_cosplay_03"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_cosplay_03")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
                            action NullAction()

                    if persistent.gal_Cosplay_4:
                        imagebutton:
                            idle "gal_cosplay_04"
                            idle_foreground "images/interface_images/gallery_images/gal_idle.png"
                            focus_mask True
                            action ui.callsinnewcontext("label_gal_cosplay_04")
                    else:
                        imagebutton:
                            idle "images/interface_images/gallery_images/locked.png"
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

    imagebutton auto "images/interface_images/Button_backgal_%s.png" xpos 600 ypos 660 focus_mask True action ShowMenu("gallery8")

    if persistent.patreon_gal_screens_on:
        imagebutton auto "images/interface_images/Button_nextgal_%s.png" xpos 848 ypos 660 focus_mask True action ShowMenu("gallery_patreon_5")

    if not persistent.patreon_gal_screens_on:
        imagebutton auto "images/interface_images/Button_nextgal_%s.png" xpos 848 ypos 660 focus_mask True action ShowMenu("gallery")

####################################################################################################################################################
### Buttons
####################################################################################################################################################

#    if gal_test:
#        imagebutton auto "images/interface_images/gallery_images/label_gal_%s.png":
#            focus_mask True
#            action ui.callsinnewcontext("label_gal")
#    else:
#        imagebutton:
#            idle "images/interface_images/gallery_images/locked.png"
#            action NullAction()

#                    imagebutton:
#                            idle "images/interface_images/gallery_images/label_gal_no_bg.png"
#                            action NullAction()
