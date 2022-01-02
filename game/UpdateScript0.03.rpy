
define audio.Splash = "music/Splash.wav"
define audio.Ejaculate = "music/Ejaculate.wav"
define audio.Scratch = "music/Scratch.mp3"
define audio.CloseDoor = "music/close_door.wav"
define audio.Slap = "music/Slap.wav"
define audio.Diaz01 = "music/Diaz01.wav"
define audio.PhoneVibrate = "music/PhoneVibrate.wav"

define K = Character(_("Kenzie"), color="FF0099", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define KT = Character(_("Kenzie's Thoughts"), color="FF0099", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define W = Character(_("Waitress"), color="3300CC", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define EBE = Character(_("Everybody Else"), color="9922BB", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define MBT = Character(_("Matt's Thoughts"), color="993300", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define AD = Character(_("Agent Diaz"), color="9135D1", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define ADT = Character(_("Agent Diaz's Thoughts"), color="9135D1", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])

define email_alert_one = False
define loyaltycounter = 0
define chosebluebikini = False
define boughtthebottle = False
define firstclubvisit = False
define lightscomment = False
define gscomment = False
define first_htbyd_shoot = True
define finished_htbyd_shoot = False
define htbyd_most_recent = False
define diazfirstvisit = False
define first_diaz_dance = False
define first_lauren_grind = False
define firstloyaltyblowjob = False
define bikini_show_seen = False
define bikini_show_failed = False
define days_until_next_photo_shoot = 0
define supporters_day_count = 0

init:
    image bg PStudioWR = "PStudioWR.webp"
    image bg EmailAlert01 = "EmailAlert01.webp"

    image bg MomDrinkingKitchen06 = "MomDrinkingKitchen06.webp"
    image bg MomDrinkingKitchen07 = "MomDrinkingKitchen07.webp"

    image bg BikiniShow01 = "BikiniShow01.webp"
    image bg BikiniShow02 = "BikiniShow02.webp"

    image bg BikiniShowPink01 = "BikiniShowPink01.webp"
    image bg BikiniShowPink02 = "BikiniShowPink02.webp"

    image bg BikiniShowBlue01 = "BikiniShowBlue01.webp"
    image bg BikiniShowBlue03 = "BikiniShowBlue03.webp"
    image bg BikiniShowBlue04 = "BikiniShowBlue04.webp"

    image bg Pool01 = "Pool01.webp"
    image bg Pool02 = "Pool02.webp"
    image bg Pool03 = "Pool03.webp"
    image bg Pool04 = "Pool04.webp"
    image bg Pool05 = "Pool05.webp"
    image bg Pool06 = "Pool06.webp"
    image bg Pool07 = "Pool07.webp"
    #image bg Pool08 = "Pool08.webp"
    #image bg Pool09 = "Pool09.webp"
    image bg Pool10 = "Pool10.webp"
    image bg Pool11 = "Pool11.webp"
    image bg Pool12 = "Pool12.webp"
    image bg Pool13 = "Pool13.webp"
    #image bg Pool14 = "Pool14.webp"
    #image bg Pool15 = "Pool15.webp"
    #image bg Pool16 = "Pool16.webp"
    image bg Pool17 = "Pool17.webp"
    #image bg Pool18 = "Pool18.webp"
    #image bg Pool19 = "Pool19.webp"
    #image bg Pool20 = "Pool20.webp"
    #image bg Pool21 = "Pool21.webp"
    #image bg Pool22 = "Pool22.webp"
    #image bg Pool23 = "Pool23.webp"
    #image bg Pool24 = "Pool24.webp"
    #image bg Pool25 = "Pool25.webp"
    #image bg Pool26 = "Pool26.webp"
    #image bg Pool27 = "Pool27.webp"
    #image bg Pool28 = "Pool28.webp"
    #image bg Pool29 = "Pool29.webp"
    #image bg Pool30 = "Pool30.webp"
    #image bg Pool31 = "Pool31.webp"
    image bg Pool32 = "Pool32.webp"
    image bg Pool33 = "Pool33.webp"
    #image bg Pool34 = "Pool34.webp"
    #image bg Pool35 = "Pool35.webp"
    #image bg Pool36 = "Pool36.webp"
    #image bg Pool37 = "Pool37.webp"
    #image bg Pool38 = "Pool38.webp"
    #image bg Pool39 = "Pool39.webp"
    #image bg Pool40 = "Pool40.webp"
    #image bg Pool41 = "Pool41.webp"
    image bg Pool42 = "Pool42.webp"
    image bg Pool43 = "Pool43.webp"
    #image bg Pool44 = "Pool44.webp"
    #image bg Pool45 = "Pool45.webp"
    #image bg Pool46 = "Pool46.webp"
    #image bg Pool47 = "Pool47.webp"
    #image bg Pool48 = "Pool48.webp"
    #image bg Pool49 = "Pool49.webp"
    #image bg Pool50 = "Pool50.webp"
    #image bg Pool51 = "Pool51.webp"
    #image bg Pool52 = "Pool52.webp"
    image bg Pool53 = "Pool53.webp"
    image bg Pool54 = "Pool54.webp"
    image bg Pool55 = "Pool55.webp"
    image bg Pool56 = "Pool56.webp"
    image bg Pool57 = "Pool57.webp"
    #image bg Pool58 = "Pool58.webp"
    image bg Pool59 = "Pool59.webp"
    image bg Pool60 = "Pool60.webp"
    image bg Pool61 = "Pool61.webp"
    image bg Pool62 = "Pool62.webp"
    image bg Pool63 = "Pool63.webp"
    #image bg Pool64 = "Pool64.webp"
    #image bg Pool65 = "Pool65.webp"
    image bg Pool67 = "Pool67.webp"
    image bg Pool68 = "Pool68.webp"
    image bg Pool69 = "Pool69.webp"
    image bg Pool70 = "Pool70.webp"
    image bg Pool71 = "Pool71.webp"

    #image bg PoolBlue01 = "PoolBlue01.webp"
    #image bg PoolBlue02 = "PoolBlue02.webp"
    #image bg PoolBlue03 = "PoolBlue03.webp"
    #image bg PoolBlue04 = "PoolBlue04.webp"
    #image bg PoolBlue05 = "PoolBlue05.webp"
    #image bg PoolBlue06 = "PoolBlue06.webp"
    #image bg PoolBlue07 = "PoolBlue07.webp"
    image bg PoolBlue08 = "PoolBlue08.webp"
    image bg PoolBlue09 = "PoolBlue09.webp"
    #image bg PoolBlue10 = "PoolBlue10.webp"
    #image bg PoolBlue11 = "PoolBlue11.webp"
    #image bg PoolBlue12 = "PoolBlue12.webp"
    #image bg PoolBlue13 = "PoolBlue13.webp"
    image bg PoolBlue14 = "PoolBlue14.webp"
    image bg PoolBlue15 = "PoolBlue15.webp"
    image bg PoolBlue16 = "PoolBlue16.webp"
    #image bg PoolBlue17 = "PoolBlue17.webp"
    image bg PoolBlue18 = "PoolBlue18.webp"
    image bg PoolBlue19 = "PoolBlue19.webp"
    image bg PoolBlue20 = "PoolBlue20.webp"
    image bg PoolBlue21 = "PoolBlue21.webp"
    image bg PoolBlue22 = "PoolBlue22.webp"
    image bg PoolBlue23 = "PoolBlue23.webp"
    image bg PoolBlue24 = "PoolBlue24.webp"
    image bg PoolBlue25 = "PoolBlue25.webp"
    image bg PoolBlue26 = "PoolBlue26.webp"
    image bg PoolBlue27 = "PoolBlue27.webp"
    image bg PoolBlue28 = "PoolBlue28.webp"
    image bg PoolBlue29 = "PoolBlue29.webp"
    image bg PoolBlue30 = "PoolBlue30.webp"
    image bg PoolBlue31 = "PoolBlue31.webp"
    #image bg PoolBlue32 = "PoolBlue32.webp"
    #image bg PoolBlue33 = "PoolBlue33.webp"
    image bg PoolBlue34 = "PoolBlue34.webp"
    image bg PoolBlue35 = "PoolBlue35.webp"
    image bg PoolBlue36 = "PoolBlue36.webp"
    image bg PoolBlue37 = "PoolBlue37.webp"
    image bg PoolBlue38 = "PoolBlue38.webp"
    image bg PoolBlue39 = "PoolBlue39.webp"
    image bg PoolBlue40 = "PoolBlue40.webp"
    image bg PoolBlue41 = "PoolBlue41.webp"
    image bg PoolBlue42 = "PoolBlue42.webp"
    image bg PoolBlue43 = "PoolBlue43.webp"
    image bg PoolBlue44 = "PoolBlue44.webp"
    image bg PoolBlue45 = "PoolBlue45.webp"
    image bg PoolBlue46 = "PoolBlue46.webp"
    image bg PoolBlue47 = "PoolBlue47.webp"
    image bg PoolBlue48 = "PoolBlue48.webp"
    image bg PoolBlue49 = "PoolBlue49.webp"
    image bg PoolBlue50 = "PoolBlue50.webp"
    image bg PoolBlue51 = "PoolBlue51.webp"
    image bg PoolBlue52 = "PoolBlue52.webp"
    #image bg PoolBlue53 = "PoolBlue53.webp"
    #image bg PoolBlue54 = "PoolBlue54.webp"
    #image bg PoolBlue55 = "PoolBlue55.webp"
    #image bg PoolBlue56 = "PoolBlue56.webp"
    #image bg PoolBlue57 = "PoolBlue57.webp"
    image bg PoolBlue58 = "PoolBlue58.webp"
    #image bg PoolBlue59 = "PoolBlue59.webp"
    #image bg PoolBlue60 = "PoolBlue60.webp"
    #image bg PoolBlue61 = "PoolBlue61.webp"
    #image bg PoolBlue62 = "PoolBlue62.webp"
    #image bg PoolBlue63 = "PoolBlue63.webp"
    image bg PoolBlue64 = "PoolBlue64.webp"
    image bg PoolBlue65 = "PoolBlue65.webp"
    image bg PoolBlue66 = "PoolBlue66.webp"
    #image bg PoolBlue67 = "PoolBlue67.webp"
    #image bg PoolBlue68 = "PoolBlue68.webp"
    #image bg PoolBlue69 = "PoolBlue69.webp"
    #image bg PoolBlue70 = "PoolBlue70.webp"
    #image bg PoolBlue71 = "PoolBlue71.webp"
    image bg PoolBlue72 = "PoolBlue72.webp"
    image bg PoolBlue73 = "PoolBlue73.webp"
    image bg PoolBlue74 = "PoolBlue74.webp"
    #image bg PoolBlue75 = "PoolBlue75.webp"

    image bg PoolBlueWine20 = "PoolBlueWine20.webp"
    image bg PoolBlueWine21 = "PoolBlueWine21.webp"
    image bg PoolBlueWine22 = "PoolBlueWine22.webp"
    image bg PoolBlueWine23 = "PoolBlueWine23.webp"
    image bg PoolBlueWine24 = "PoolBlueWine24.webp"
    image bg PoolBlueWine25 = "PoolBlueWine25.webp"

    #image bg PoolPink01 = "PoolPink01.webp"
    #image bg PoolPink02 = "PoolPink02.webp"
    #image bg PoolPink03 = "PoolPink03.webp"
    #image bg PoolPink04 = "PoolPink04.webp"
    #image bg PoolPink05 = "PoolPink05.webp"
    #image bg PoolPink06 = "PoolPink06.webp"
    #image bg PoolPink07 = "PoolPink07.webp"
    image bg PoolPink08 = "PoolPink08.webp"
    image bg PoolPink09 = "PoolPink09.webp"
    #image bg PoolPink10 = "PoolPink10.webp"
    #image bg PoolPink11 = "PoolPink11.webp"
    #image bg PoolPink12 = "PoolPink12.webp"
    #image bg PoolPink13 = "PoolPink13.webp"
    image bg PoolPink14 = "PoolPink14.webp"
    image bg PoolPink15 = "PoolPink15.webp"
    image bg PoolPink16 = "PoolPink16.webp"
    #image bg PoolPink17 = "PoolPink17.webp"
    image bg PoolPink18 = "PoolPink18.webp"
    image bg PoolPink19 = "PoolPink19.webp"
    image bg PoolPink20 = "PoolPink20.webp"
    image bg PoolPink21 = "PoolPink21.webp"
    image bg PoolPink22 = "PoolPink22.webp"
    image bg PoolPink23 = "PoolPink23.webp"
    #image bg PoolPink24 = "PoolPink24.webp"
    #image bg PoolPink25 = "PoolPink25.webp"
    image bg PoolPink26 = "PoolPink26.webp"
    image bg PoolPink27 = "PoolPink27.webp"
    #image bg PoolPink28 = "PoolPink28.webp"
    image bg PoolPink29 = "PoolPink29.webp"
    image bg PoolPink30 = "PoolPink30.webp"
    #image bg PoolPink31 = "PoolPink31.webp"
    #image bg PoolPink32 = "PoolPink32.webp"
    #image bg PoolPink33 = "PoolPink33.webp"
    image bg PoolPink34 = "PoolPink34.webp"
    image bg PoolPink35 = "PoolPink35.webp"
    image bg PoolPink36 = "PoolPink36.webp"
    image bg PoolPink37 = "PoolPink37.webp"
    image bg PoolPink38 = "PoolPink38.webp"
    image bg PoolPink39 = "PoolPink39.webp"
    image bg PoolPink40 = "PoolPink40.webp"
    image bg PoolPink41 = "PoolPink41.webp"
    image bg PoolPink42 = "PoolPink42.webp"
    image bg PoolPink43 = "PoolPink43.webp"
    image bg PoolPink44 = "PoolPink44.webp"
    image bg PoolPink45 = "PoolPink45.webp"
    image bg PoolPink46 = "PoolPink46.webp"
    image bg PoolPink47 = "PoolPink47.webp"
    image bg PoolPink48 = "PoolPink48.webp"
    image bg PoolPink49 = "PoolPink49.webp"
    image bg PoolPink50 = "PoolPink50.webp"
    image bg PoolPink51 = "PoolPink51.webp"
    image bg PoolPink52 = "PoolPink52.webp"
    #image bg PoolPink53 = "PoolPink53.webp"
    #image bg PoolPink54 = "PoolPink54.webp"
    #image bg PoolPink55 = "PoolPink55.webp"
    #image bg PoolPink56 = "PoolPink56.webp"
    #image bg PoolPink57 = "PoolPink57.webp"
    image bg PoolPink58 = "PoolPink58.webp"
    #image bg PoolPink59 = "PoolPink59.webp"
    #image bg PoolPink60 = "PoolPink60.webp"
    #image bg PoolPink61 = "PoolPink61.webp"
    #image bg PoolPink62 = "PoolPink62.webp"
    #image bg PoolPink63 = "PoolPink63.webp"
    image bg PoolPink64 = "PoolPink64.webp"
    image bg PoolPink65 = "PoolPink65.webp"
    image bg PoolPink66 = "PoolPink66.webp"
    #image bg PoolPink67 = "PoolPink67.webp"
    #image bg PoolPink68 = "PoolPink68.webp"
    #image bg PoolPink69 = "PoolPink69.webp"
    #image bg PoolPink70 = "PoolPink70.webp"
    #image bg PoolPink71 = "PoolPink71.webp"
    image bg PoolPink72 = "PoolPink72.webp"
    image bg PoolPink73 = "PoolPink73.webp"
    image bg PoolPink74 = "PoolPink74.webp"

    image bg PoolPinkWine20 = "PoolPinkWine20.webp"
    image bg PoolPinkWine21 = "PoolPinkWine21.webp"
    image bg PoolPinkWine22 = "PoolPinkWine22.webp"
    image bg PoolPinkWine23 = "PoolPinkWine23.webp"
    #image bg PoolPinkWine24 = "PoolPinkWine24.webp"
    #image bg PoolPinkWine25 = "PoolPinkWine25.webp"

    image bg PStudioEmpty = "PStudioEmpty.webp"
    image bg PStudioLights = "PStudioLights.webp"
    image bg PStudioGScreen = "PStudioGScreen.webp"
    image bg PStudioGScreenLights = "PStudioGScreenLights.webp"

    image bg KitchenArsetrid01 = "KitchenArsetrid01.webp"
    image bg KitchenArsetrid02 = "KitchenArsetrid02.webp"
    image bg KitchenArsetrid03 = "KitchenArsetrid03.webp"
    image bg KitchenArsetrid04 = "KitchenArsetrid04.webp"
    image bg KitchenArsetrid05 = "KitchenArsetrid05.webp"

    image bg PhotoStudio01 = "PhotoStudio01.webp"
    image bg PhotoStudio02 = "PhotoStudio02.webp"
    image bg PhotoStudio03 = "PhotoStudio03.webp"
    image bg PhotoStudio04 = "PhotoStudio04.webp"
    image bg PhotoStudio05 = "PhotoStudio05.webp"
    image bg PhotoStudio06 = "PhotoStudio06.webp"
    image bg PhotoStudio07 = "PhotoStudio07.webp"
    image bg PhotoStudio08 = "PhotoStudio08.webp"

    image bg HTBYD_E_00 = "HTBYD_E_00.webp"
    image bg HTBYD_E_01 = "HTBYD_E_01.webp"
    image bg HTBYD_E_02 = "HTBYD_E_02.webp"
    image bg HTBYD_E_03 = "HTBYD_E_03.webp"
    image bg HTBYD_E_04 = "HTBYD_E_04.webp"
    image bg HTBYD_E_05 = "HTBYD_E_05.webp"
    image bg HTBYD_E_06 = "HTBYD_E_06.webp"
    image bg HTBYD_E_07 = "HTBYD_E_07.webp"
    image bg HTBYD_E_08 = "HTBYD_E_08.webp"
    image bg HTBYD_E_09 = "HTBYD_E_09.webp"
    image bg HTBYD_E_29 = "HTBYD_E_29.webp"

    image bg HTBYD_GS_00 = "HTBYD_GS_00.webp"
    image bg HTBYD_GS_01 = "HTBYD_GS_01.webp"
    image bg HTBYD_GS_02 = "HTBYD_GS_02.webp"
    image bg HTBYD_GS_03 = "HTBYD_GS_03.webp"
    image bg HTBYD_GS_04 = "HTBYD_GS_04.webp"
    image bg HTBYD_GS_05 = "HTBYD_GS_05.webp"
    image bg HTBYD_GS_06 = "HTBYD_GS_06.webp"
    image bg HTBYD_GS_07 = "HTBYD_GS_07.webp"
    image bg HTBYD_GS_08 = "HTBYD_GS_08.webp"
    image bg HTBYD_GS_09 = "HTBYD_GS_09.webp"
    image bg HTBYD_GS_10 = "HTBYD_GS_10.webp"
    image bg HTBYD_GS_11 = "HTBYD_GS_11.webp"
    image bg HTBYD_GS_12 = "HTBYD_GS_12.webp"
    image bg HTBYD_GS_13 = "HTBYD_GS_13.webp"
    image bg HTBYD_GS_15 = "HTBYD_GS_15.webp"
    image bg HTBYD_GS_16 = "HTBYD_GS_16.webp"
    image bg HTBYD_GS_18 = "HTBYD_GS_18.webp"
    image bg HTBYD_GS_19 = "HTBYD_GS_19.webp"
    image bg HTBYD_GS_20 = "HTBYD_GS_20.webp"
    image bg HTBYD_GS_21 = "HTBYD_GS_21.webp"
    image bg HTBYD_GS_22 = "HTBYD_GS_22.webp"
    image bg HTBYD_GS_23 = "HTBYD_GS_23.webp"
    image bg HTBYD_GS_24 = "HTBYD_GS_24.webp"
    image bg HTBYD_GS_25 = "HTBYD_GS_25.webp"
    #image bg HTBYD_GS_26 = "HTBYD_GS_26.webp"
    image bg HTBYD_GS_27 = "HTBYD_GS_27.webp"
    image bg HTBYD_GS_28 = "HTBYD_GS_28.webp"
    image bg HTBYD_GS_29 = "HTBYD_GS_29.webp"
    image bg HTBYD_GS_30 = "HTBYD_GS_30.webp"
    image bg HTBYD_GS_31 = "HTBYD_GS_31.webp"
    image bg HTBYD_GS_32 = "HTBYD_GS_32.webp"
    image bg HTBYD_GS_33 = "HTBYD_GS_33.webp"
    image bg HTBYD_GS_34 = "HTBYD_GS_34.webp"
    image bg HTBYD_GS_35 = "HTBYD_GS_35.webp"
    image bg HTBYD_GS_36 = "HTBYD_GS_36.webp"
    image bg HTBYD_GS_37 = "HTBYD_GS_37.webp"

    image bg HTBYD_F_00 = "HTBYD_F_00.webp"
    image bg HTBYD_F_02 = "HTBYD_F_02.webp"
    image bg HTBYD_F_04 = "HTBYD_F_04.webp"
    image bg HTBYD_F_06 = "HTBYD_F_06.webp"
    image bg HTBYD_F_08 = "HTBYD_F_08.webp"
    image bg HTBYD_F_10 = "HTBYD_F_10.webp"
    image bg HTBYD_F_11 = "HTBYD_F_11.webp"
    image bg HTBYD_F_12 = "HTBYD_F_12.webp"
    image bg HTBYD_F_13 = "HTBYD_F_13.webp"
    image bg HTBYD_F_14 = "HTBYD_F_14.webp"
    image bg HTBYD_F_15 = "HTBYD_F_15.webp"
    image bg HTBYD_F_16 = "HTBYD_F_16.webp"
    image bg HTBYD_F_17 = "HTBYD_F_17.webp"
    image bg HTBYD_F_20 = "HTBYD_F_20.webp"
    image bg HTBYD_F_21 = "HTBYD_F_21.webp"
    image bg HTBYD_F_23 = "HTBYD_F_23.webp"
    image bg HTBYD_F_24 = "HTBYD_F_24.webp"
    image bg HTBYD_F_25 = "HTBYD_F_25.webp"
    image bg HTBYD_F_26 = "HTBYD_F_26.webp"

    image bg CheckHTBYDLikes01 = "CheckHTBYDLikes01.webp"
    image bg CheckHTBYDLikes02 = "CheckHTBYDLikes02.webp"
    image bg CheckHTBYDLikes03 = "CheckHTBYDLikes03.webp"
    image bg CheckHTBYDLikes04 = "CheckHTBYDLikes04.webp"
    image bg CheckHTBYDLikes05 = "CheckHTBYDLikes05.webp"
    image bg CheckHTBYDLikes06 = "CheckHTBYDLikes06.webp"
    image bg CheckHTBYDLikes07 = "CheckHTBYDLikes07.webp"
    image bg CheckHTBYDLikes08 = "CheckHTBYDLikes08.webp"

    image bg RyanWakingWithSid01 = "RyanWakingWithSid01.webp"

    image bg DiazVisit01 = "DiazVisit01.webp"
    image bg DiazVisit02 = "DiazVisit02.webp"
    image bg DiazVisit03 = "DiazVisit03.webp"
    image bg DiazVisit04 = "DiazVisit04.webp"
    image bg DiazVisit05 = "DiazVisit05.webp"
    image bg DiazVisit06 = "DiazVisit06.webp"
    image bg DiazVisit07 = "DiazVisit07.webp"
    image bg DiazVisit08 = "DiazVisit08.webp"
    image bg DiazVisit09 = "DiazVisit09.webp"
    image bg DiazVisit10 = "DiazVisit10.webp"
    image bg DiazVisit11 = "DiazVisit11.webp"
    image bg DiazVisit12 = "DiazVisit12.webp"
    image bg DiazVisit13 = "DiazVisit13.webp"
    image bg DiazVisit14 = "DiazVisit14.webp"
    image bg DiazVisit15 = "DiazVisit15.webp"
    image bg DiazVisit16 = "DiazVisit16.webp"
    image bg DiazVisit17 = "DiazVisit17.webp"
    image bg DiazVisit18 = "DiazVisit18.webp"
    image bg DiazVisit19 = "DiazVisit19.webp"
    image bg DiazVisit20 = "DiazVisit20.webp"
    image bg DiazVisit21 = "DiazVisit21.webp"
    image bg DiazVisit22 = "DiazVisit22.webp"
    image bg DiazVisit23 = "DiazVisit23.webp"
    image bg DiazVisit24 = "DiazVisit24.webp"
    image bg DiazVisit25 = "DiazVisit25.webp"
    image bg DiazVisit26 = "DiazVisit26.webp"
    image bg DiazVisit27 = "DiazVisit27.webp"
    image bg DiazVisit28 = "DiazVisit28.webp"
    image bg DiazVisit29 = "DiazVisit29.webp"
    image bg DiazVisit30 = "DiazVisit30.webp"
    image bg DiazVisit31 = "DiazVisit31.webp"
    image bg DiazVisit32 = "DiazVisit32.webp"
    image bg DiazVisit33 = "DiazVisit33.webp"
    image bg DiazVisit34 = "DiazVisit34.webp"
    image bg DiazVisit35 = "DiazVisit35.webp"
    image bg DiazVisit36 = "DiazVisit36.webp"
    image bg DiazVisit37 = "DiazVisit37.webp"
    image bg DiazVisit38 = "DiazVisit38.webp"
    image bg DiazVisit39 = "DiazVisit39.webp"
    image bg DiazVisit40 = "DiazVisit40.webp"
    image bg DiazVisit41 = "DiazVisit41.webp"
    image bg DiazVisit42 = "DiazVisit42.webp"
    image bg DiazVisit43 = "DiazVisit43.webp"
    image bg DiazVisit44 = "DiazVisit44.webp"
    image bg DiazVisit45 = "DiazVisit45.webp"
    image bg DiazVisit46 = "DiazVisit46.webp"
    image bg DiazVisit47 = "DiazVisit47.webp"
    image bg DiazVisit48 = "DiazVisit48.webp"

    image bg MeganInHall01 = "MeganInHall01.webp"
    image bg MeganInHall02 = "MeganInHall02.webp"
    image bg MeganInHall03 = "MeganInHall03.webp"
    image bg MeganInHall04 = "MeganInHall04.webp"
    image bg MeganInHall05 = "MeganInHall05.webp"

    image bg Memes09 = "Meme09.webp"
    image bg Memes10 = "Meme10.webp"
    image bg Memes11 = "Meme11.webp"
    image bg Memes12 = "Meme12.webp"

    image Memes09 = "Meme09.webp"
    image Memes10 = "Meme10.webp"
    image Memes11 = "Meme11.webp"
    image Memes12 = "Meme12.webp"


#################  RYAN'S ROOM  ##########################################################  RYAN'S ROOM  #####################################################################  RYAN'S ROOM  ####################################################################  RYAN'S ROOM  ########################################################################  RYAN'S ROOM  ####

label posting_the_htbyd_pics:
    $ persistent.gal_Cosplay_2 = True
    play music Honey
    scene bg SleepBlack
    with fade
    scene bg CosplayWarehouse20
    with fade
    if inventory.inv_amount(green_screen) == 1:
        RT "{i}I finally finished the Zad 3D work and photo editing.{/i}"
        RT "{i}They turned out pretty damn hot if I do say so myself.{/i}"
    RT "{i}Uploading the pictures now.... and click submit.... and now we just wait to see if anyone likes them.{/i}"
    RT "{i}I've got to be sure to check the website sometime tomorrow.{/i}"
    $ photoshoot_2 = True
    if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
        $ picsareposted = True
    else:
        pass
    $ weekly_htbyd_complete = True
    scene bg RyansRoom01
    with fade
    $ screen_on = "ryanmap"
    call screen ryanmap

label check_for_htbyd_likes:
    scene bg CosplayWarehouse20
    with fade
    RT "{i}Ok, I've got to just login with my username and password and we'll see if anyone liked the girls' pictures.{/i}"
    if inventory.inv_amount(green_screen) == 1:
        scene bg CheckHTBYDLikes02
        with dissolve
    else:
        scene bg CheckHTBYDLikes01
        with dissolve
    R "Oh, hey Lauren, what's up?"
    if laurenanger >= 1:
        L "Hey pervert, I just came to see if you'd posted those pictures online yet."
    else:
        L "Hey [ryan], I just came to see if you'd posted those pictures online yet."
    R "What a coincidence, I was just checking to see if they got any likes at exactly the same moment that you walked into my room."
    R "Why don't we take a look together?"
    if inventory.inv_amount(green_screen) == 1:
        scene bg CheckHTBYDLikes04
        with dissolve
    else:
        scene bg CheckHTBYDLikes03
        with dissolve
    L "Wow! Look how many people liked and commented on the outfit."
    R "Yeah, Sidney really did an amazing job on that one."
    if inventory.inv_amount(green_screen) == 1:
        scene bg CheckHTBYDLikes06
        with dissolve
    else:
        scene bg CheckHTBYDLikes05
        with dissolve
    R "Look how the amount of likes goes up consistently with the amount of skin you showed off."
    L "Wow! I can't believe how much a difference that made."
    if finished_htbyd_shoot == True:
        R "Let's take a look at how the photos I added backgrounds to did."
        scene bg CheckHTBYDLikes07
        with dissolve
        L "Oh my God! [ryan]! You asshole!"
        L "It looks like that dragon is going to fuck me!"
        scene bg CheckHTBYDLikes08
        with dissolve
        R "No, no, wait! Lauren look how many likes these pictures got!"
        R "They alone got enough likes to bump your overall ranking above thirteen other girls!"
        L "Huh?.... Oh, wow! Look how many fame points those pics got me.... and a ton of new followers."
        R "Well?..."
        L ".... Well, what?"
        R "I did good, didn't I?"
        L "Uuuuugghhh.... yeah, I guess I've got to admit it. You're idea worked amazingly."
        R "Dammit! I should have recorded you saying that."
        L "Yep, cuz you will probably never hear it again."
        "{i}{b}\"Lauren's Anger =0\"{/b}{/i}"
        $ laurenanger = 0
    else:
        pass
    L "Well.... your skin to likes ratio theory seems to hold true."
    L "I'll try to get up the courage to take the next shoot even farther."
    L "Thanks again for helping me try to get famous!"
    L "And for using the money to help Mom."
    L "You really are proving to be a great substitute for Dad."
    R "Thanks Lauren!"
    L "Ok, it's getting too mushy in here. I'll see you around the house sometime."
    $ picsarepostedcounter = 0
    $ picsareposted = False
    scene bg RyansRoom01
    with fade
    $ screen_on = "ryanmap"
    call screen ryanmap

###################  LOUNGE  #############################################################  LOUNGE  ##########################################################################  LOUNGE  ########################################################################  LOUNGE  ##########################################################################  LOUNGE  ############

label diazvisit:
    if truth_dare_completed:
        jump diaz_is_back
    if diazfirstvisit == False:
        scene bg SleepBlack
        with fade
        $ laurenpictureprogress = 14
        "{b}Ding Dong!{/b}"
        scene bg BlurryWhite
        with fade
        scene bg SleepBlack
        with fade
        "{b}Ding Dong!{/b}"
        scene bg BlurryWhite
        with fade
        scene bg SleepBlack
        with fade
        R "Who in the hell?"
        scene bg RyanWakingWithSid01
        S "It's only six in the morning!"
        S "Get the door [ryan], I'm too tired.... not dressed.... crusty.... panties.... {i}snore{/i}..."
        RT "{i}Anyone ringing the doorbell this early, can't be here with good news.{/i}"
        scene bg SleepBlack
        with fade
        scene bg DiazVisit02
        with fade
        AD "Well, good morning [ryan]!"
        $ diazfirstvisit = True
        R "Huh?.... Hi?.... How do you know me?"
        AD "My name is Special Agent Diaz of the FBI Criminal Investigation Division."
        AD "I've just been reassigned to head the case against your father."
        AD "Aren't you going to invite me in?"
        R "Uhhhh.... It's 6 in the morning.... do you have a warrant?"
        scene bg DiazVisit01
        with dissolve
        AD "It's not that kind of visit, and we have an ongoing warrant to search the premises whenever we feel there is a need."
        R "Ok, let me go get my mom."
        AD "She's not here, I just watched her drive away."
        AD "I've arranged for her to have an early morning meeting with her lawyer and the federal prosecutor each Thursday morning to go over details of the investigation against her husband."
        R "Then who are you here to see?"
        scene bg DiazVisit02
        with dissolve
        AD "I actually want to have a few words with you and your sister Lauren."
        R "What?"
        R "What could you possibly want with us?"
        AD "Why don't you go get your sister and I'll meet you in the lounge."
        R "Uhhhh.... ok.... let me show you where it..."
        AD "I know where it is.... just run and get Lauren."
        scene bg SleepBlack
        with fade
        RT "{i}Oh my God.... what is this about?.... I hope I haven't done anything to get Lauren in trouble.{/i}"
        scene bg DiazVisit03
        with fade
        AD "Good morning Lauren, I hope you slept well."
        L "Uuuuhhhh.... hi?"
        AD "I'm sorry, but did [ryan] tell you who I am?"
        L "He said you're in charge of building a case against our dad?"
        AD "I am, but I'm not here to talk about his case, I'm here because of the actions of you two."
        scene bg DiazVisit04
        with dissolve
        L "Oh, no.... what have we done?"
        R "Lauren.... let me do the talking. We have to be careful what we say here."
        AD "You bet your ass you do. You two have been naughty lately."
        L "No, we haven't."
        AD "So, you haven't been taking sexy pictures of yourself on the property of a company that has suspected dealings with the Mafia?"
        scene bg DiazVisit06
        with dissolve
        L "How do you know that?"
        R "They're watching everything we do..."
        AD "Oh, please.... you aren't making it hard."
        AD "Are you aware how easy it is to track your activity on the internet?"
        AD "Are you aware how easy it is to follow teens on their bikes and mopeds?"
        RT "{i}Oh my God, does that mean they know about me buying and installing my spy-cams?{/i}"
        AD "Your father obviously didn't teach you anything he knew about conducting business covertly."
        scene bg DiazVisit04
        with dissolve
        R "But Lauren and I are both adults. It's not illegal for us to take and pose for adult pictures, and we've set up everything legally online through Cosplay Heaven."
        AD "Yes, and you generated tax forms that prove you're making an income that you aren't reporting and surrendering to the FBI."
        R "Oh, shit.... that's right..."
        AD "And that's not even mentioning the money you're getting under the table from your uncle Bobby to help you pay off your weekly debt to the DeCapos."
        R "..."
        scene bg DiazVisit06
        with dissolve
        R "..."
        R "Wait!.... You know the DeCapos are extorting us for $1000 a week?"
        AD "And I know they're making your mom strip if they don't get their payment each week."
        scene bg DiazVisit05
        with dissolve
        L "What?.... Mom's not serving drinks at Joey's club? She's actually stripping?"
        R "Yeah.... she asked me not to tell you. I'll fill you in later."
        scene bg DiazVisit06
        with dissolve
        R "So, you know about all of this?.... And we're the ones who are in trouble? Why aren't you going after the DeCapo's?"
        AD "[ryan], you're a bright boy.... I'm sure you've seen Mafia movies before."
        AD "It shouldn't be too hard for you to put this together."
        scene bg DiazVisit04
        with dissolve
        R "..."
        R "Oh my God.... you're in the pocket of the DeCapos."
        L "Oh my God..."
        AD "Haha.... bingo."
        scene bg DiazVisit05
        with dissolve
        L "Well, thats not horrible news."
        L "You should be able to help get Dad off on all charges right?"
        AD "Well, that was the original plan."
        AD "But now Joey DeCapo is happier with the arrangement as it is now. He's getting paid each week, or he's getting a visit from your mom."
        AD "He actually enjoys those visits more than he does the money."
        AD "Now he wants to keep your dad in jail as long as possible."
        scene bg DiazVisit04
        with dissolve
        L "Well, what do you want with us?"
        AD "That's simple..."
        AD "I'm here to extort you."
        R "..."
        scene bg DiazVisit06
        with dissolve
        R "For what?"
        AD "Money and favors of course."
        R "Favors?"
        R "You mean if we don't pay you what you want, I have to do a strip dance for you?"
        AD "Haha.... do you see the pant-suit?"
        AD "It's not you I would want to see lose their clothes."
        L "Oh.... my.... God..."
        R "How much do we have to pay you?"
        AD "Oh, not much, just $500 a week."
        R "But what if we can't pay the DeCapo's because you're extorting us?"
        R "I'll make sure Joey knows it's you who's preventing us."
        AD "Joey already knows about this."
        AD "Like I said, he doesn't mind if you miss a payment here and there."
        L "Oh.... my.... God..."
        L "..."
        scene bg DiazVisit05
        with dissolve
        L "[ryan]!.... We can't give Diaz the money.... we've got to protect Mom."
        R "I think Mom would disagree.... she wouldn't want you to have to do favors for this pervy fed."
        L "It's better that I do favors for this pervy fed in the safety of our home, than for Mom to do favors for a bunch of dangerous pervy gangsters."
        AD "And I promise I won't take it too far. Haha.... unless you ask me to."
        AD "Oh, and you can't tell your mom about this at all."
        scene bg DiazVisit06
        with dissolve
        R "Or what?"
        AD "Or I tell her about everything else, the sexy pics, about posting them on the internet, and several other things I know [ryan]'s been up to around here lately."
        AD "You don't want me to be more specific in front of Lauren do you?..."
        scene bg DiazVisit05
        with dissolve
        L "What's she talking about?"
        R "Don't worry about that. We can't let Mom find out about the pictures."
        R "We have no choice, but to play along."
        AD "That's great news."
        AD "So, what's it gonna be?"
        menu:
            "Pay $500" if money >= 500:
                R "No question, we're paying the $500."
                L "But [ryan]? What about Mom?"
                if money >= 130:
                    R "Don't worry, I'll have enough money to pay for her too by Saturday."
                    L "Oh, thank God!"
                    "{i}{b}\"Lauren's Respect +1\"{/b}{/i}"
                    $ laurenrespect += 1
                else:
                    R "I'm a little short on money, but I'll do my best to get enough by Saturday."
                    L "Well, what if you can't?"
                    R "Then it will be up to Mom to take care of it this week. I know she'd prefer that, to letting you do favors for some horny corrupt FBI agent."
                    AD "You're pushing it [ryan]."
                R "Let me go grab you your money, and I'll meet you by the front door to show you out."
                scene bg DiazVisit02
                with fade
                R "Here's the $500."
                "{i}\"Money - $500\"{/i}"
                $ money -= 500
                AD "It's been a pleasure doing business with you."
                scene bg DiazVisit01
                with dissolve
                AD "And just so you know, I know exactly what's going on in this house. I know about the inappropriate gifts you buy on Hardnlong, and the little surveillance state you've got going on here."
                AD "So, you'd better be willing to play ball, or your life is going to get pretty uncomfortable."
                RT "{i}Shit.... I'm an idiot to think I was being so sneaky with the FBI watching me.{/i}"
                RT "{i}Maybe I'm lucky that a crooked agent is in charge of this case.{/i}"
                RT "{i}I'm not in trouble so to speak, and it sounds like Dad's going to be out of our lives, at least for the foreseeable future.{/i}"
                scene bg DiazVisit02
                with dissolve
                AD "And just between you and me, I, just like Joey, wouldn't mind even a little bit if you had to miss a payment here and there."
                R "I'll take that into consideration. Goodbye!"
                play sound CloseDoor
                scene bg DiazVisit47
                with dissolve
                RT "{i}Holy fucking shit!!.... What is happening with my life?.... {/i}"
                L "{i}(SHOUTING){/i} [ryan]!"
                R "{i}(SHOUTING){/i} Yeah?"
                L "Will you please come to my room?"
                scene bg SleepBlack
                with fade
                R "What is it?"
                L "Please sit down on my bed."
                jump ryan_and_lauren
            "Let Lauren pay in favors":
                if money <= 499:
                    R "Shit! I don't even have the money to pay you $500 right now, and getting $1000 by Saturday to pay for Mom is going to be almost impossible."
                    L "What have you been doing with the money? I know you go to work at Dad's warehouse almost every day, and what about the money we've made taking pictures?"
                    R "I've had to use it on other things."
                    L "Things that are more important than Mom?"
                    "{i}{b}\"Lauren's Respect -1\"{/b}{/i}"
                    $ laurenrespect -= 1
                    R "Well, why don't you try supporting the family?.... See how easy you think it is..."
                else:
                    R "Lauren.... I think you're right.... If we pay Diaz the $500, we may not have enough for Mom too."
                    R "And I think you're also right that Mom would be in more danger than you are here in the safety of our own home."
                    R "But are you sure you're willing to take one for the team?"
                    L "Of course! You're already doing your part. It's time for me to do mine."
                AD "So, I take it I'll be paid in favors this week?"
                AD "That's great! This is even better than the money.... I get so bored spying on you from my car."
                AD "Lauren, why don't we take this to your room. [ryan] you can go get ready for school."
                scene bg SleepBlack
                with fade
                AD "I'll just make myself comfortable on your bed."
                jump diaz_and_lauren
    else:
        scene bg SleepBlack
        with fade
        "{b}Ding Dong!{/b}"
        scene bg BlurryWhite
        with fade
        scene bg SleepBlack
        with fade
        "{b}Ding Dong!{/b}"
        scene bg BlurryWhite
        with fade
        scene bg SleepBlack
        with fade
        R "Shit!.... I know who that is..."
        scene bg RyanWakingWithSid01
        with fade
        S "It's only six in the morning!"
        S "Get the door [ryan], I'm too tired.... not dressed.... crusty.... panties.... {i}snore{/i}..."
        "It's time for the weekly Agent Diaz event, would you like to skip it this week?"
        menu:
            "Yes":
                "Ok... I get it... You've got other events to complete."
                "But are you going to protect Lauren and pay the $500 this week, or will you let Lauren pay Diaz in favors?"
                menu:
                    "Of course I'll protect Lauren!" if money >= 500:
                        "{i}\"Money -$500\"{/i}"
                        $ money -= 500
                        "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                        $ laurenaffection += 1
                        $ timeofdaycounter += 1
                        jump myroom
                    "Shit!.... I don't have the money to protect her this week!" if money <= 499:
                        "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                        $ laurensubmission += 1
                        $ timeofdaycounter += 1
                        jump myroom
                    "I need that money elsewhere.... Lauren's ass will have to pay the bill this week." if money >= 500:
                        "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                        $ laurensubmission += 1
                        $ timeofdaycounter += 1
                        jump myroom
            "No":
                pass
        if money >= 500:
            RT "{i}I better grab my cash in case I need it.{/i}"
        else:
            RT "{i}Shit, I'm short on cash this week.{/i}"
            RT "{i}I hope Lauren's ready to do her duty.{/i}"
        scene bg SleepBlack
        with fade
        scene bg DiazVisit02
        with fade
        AD "Well, good morning [ryan]!"
        R "Why do you always look so chipper this early in the morning?"
        AD "Well, I know that I'm either going to make $500 this morning, or get some really great entertainment."
        AD "That just puts me in a good mood."
        AD "So, what's it going to be this week?"
        menu:
            "Pay her $500." if money >= 500:
                R "Here, just take your money and get out of here."
                "{i}\"Money -$500\"{/i}"
                $ money -= 500
                scene bg DiazVisit01
                with dissolve
                AD "Now don't be like that..."
                AD "I'm going to be a big part of your family's lives here in the near future. So, let's try to keep things civil."
                scene bg DiazVisit02
                with dissolve
                AD "For now, let me just say, that I hope you enjoy your week."
                R "..."
                AD "Well?"
                R "{i}(muttering){/i} I hope you enjoy your week too."
                AD "Well, thank you! I'll see you next Thursday, bright and early!"
                play sound CloseDoor
                scene bg DiazVisit47
                with dissolve
                RT "{i}Oh, I hate that woman!{/i}"
                L "{i}(Shouting){/i} [ryan]! Was that who I think it was?"
                R "Yeah! But she's gone now!"
                L "You mean you paid her!?"
                R "I did!"
                L "Will you please come to my room?"
                scene bg SleepBlack
                with fade
                R "What is it?"
                L "Please sit down on my bed."
                jump ryan_and_lauren
            "Let Lauren pay in favors":
                if money <= 499:
                    R "Uuuuugghhh.... I don't have enough money this week."
                    AD "You've got to learn to manage your money better!"
                    AD "Lucky for you, your little sister can cover your ass, by using hers."
                    R "You bitch!"
                else:
                    R "I need my money for other things this week."
                    R "I'm just going to have to let Lauren take one for the team."
                    AD "Haha, I like that attitude!"
                    AD "Why put your ass on the line, when you can use hers."
                    R "You bitch!"
                scene bg DiazVisit02
                with dissolve
                AD "Now don't be like that..."
                AD "I'm going to be a big part of your family's lives here in the near future. So, let's try to keep things civil."
                scene bg DiazVisit02
                with dissolve
                AD "For now, let me just say, that I hope you enjoy your week."
                R "..."
                AD "Well?"
                R "{i}(muttering){/i} I hope you enjoy your week too."
                AD "Thank you, and now if you'll move aside, I'll just help myself to your little sister's room."
                scene bg SleepBlack
                with fade
                L "I thought I smelled brimstone."
                AD "Hahah.... you cheeky little minx."
                AD "I'll just make myself comfortable, shall I?"
                jump diaz_and_lauren

##################  KITCHEN  ############################################################  KITCHEN  #########################################################################  KITCHEN  #####################################################################  KITCHEN  #############################################################################  KITCHEN  ########

label firstloyaltyweekend:
    scene bg SleepBlack
    with fade
    scene bg RyanWakingWithSid01
    with fade
    RT "{i}10:00? I slept in, I must have been tired.{/i}"
    RT "{i}Of course Sidney is still asleep.{/i}"
    RT "{i}Well, it's time to go to the kitchen, I wonder if Mom made breakfast.{/i}"
    scene bg DrinkingKitchenMom
    with fade
    RT "{i}Oh, no.... it looks like Mom has started drinking early this morning.{/i}"
    menu:
        "Talk to Mom.":
            scene bg MomDrinkingKitchen01
            with fade
            R "Hey Mom, is everything ok this morning?"
            scene bg MomDrinkingKitchen05
            with dissolve
            M "Oh, good morning honey! Yeah, actually everything is great this morning!"
            menu:
                "Mention her drinking this early.":
                    R "But isn't it a little bit early to start drinking?"
                    scene bg MomDrinkingKitchen02
                    with dissolve
                    M "Well, let me correct myself, everything was great, until you came around and started sticking your nose into my business."
                    RT "{i}I'd love to stick my nose right directly into her business ;){/i}"
                    "{i}{b}\"Mom's Affection -2\"{/b}{/i}"
                    $ momaffection -= 2
                    R "Sorry Mom, I just can't help but worry about you."
                    R "I know you didn't like the fact that Dad told me that I'm the man of the house, when you think you should be,"
                    R "But I can't help but feel the need to protect you."
                    scene bg MomDrinkingKitchen03
                    with dissolve
                    M "Well, would it help your peace of mind if I told you I'm drinking in honor of you?"
                    R "Wait.... what?"
                    M "Yeah.... during my workout this morning, I was thinking about how grateful I am that I didn't have to go to the strip club last night, and for quite a few Saturdays now."
                    M "And then I thought about how that is all thanks to you."
                    scene bg MomDrinkingKitchen05
                    with dissolve
                    M "I just thought stripping was going to be part of my life again until your dad gets out of prison, but now I feel so much safer now that you've shown you're capable of paying your dad's debt."
                    "{i}{b}\"Mom's Respect +3\"{/b}{/i}"
                    $ momrespect += 3
                    R "It just makes me feel really good to take care of you and make you happy."
                    "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    $ momsubmission += 1
                    $ momaffection += 1
                "Just let it be.":
                    R "Good! I'm so glad to see you looking happy. I know your stress has to be through the roof."
                    R "I really admire how well you're handling everything that's going on."
                    "{i}{b}\"Mom's Affection +2\"{/b}{/i}"
                    $ momaffection += 2
                    M "Oh, honey, you're so sweet!"
                    M "Today I'm actually drinking in your honor."
                    R "Really?"
                    M "Yeah.... during my workout this morning, I was thinking about how grateful I am that I didn't have to go to the strip club last night, and for quite a few Saturdays now."
                    M "And then I thought about how that is all thanks to you."
                    scene bg MomDrinkingKitchen05
                    with dissolve
                    M "I just thought stripping was going to be part of my life again until your dad gets out of prison, but now I feel so much safer now that you've shown you're capable of paying your dad's debt."
                    "{i}{b}\"Mom's Respect +3\"{/b}{/i}"
                    $ momrespect += 3
                    R "It just makes me feel really good to take care of you and make you happy."

            scene bg MomDrinkingKitchen01
            with dissolve
            M "There has to be something I can do for my boy to thank you for everything you've done for me."
            R "Oh, you don't have to do anything for me, I'm just doing my job as the head of this household."
            scene bg MomDrinkingKitchen02
            with dissolve
            M "I'm still head of this household, you're just the man of the house!"
            RT "{i}YES!!.... She just acknowledged that I'm the man of the house!{/i}"
            MT "{i}Shit!! I just admitted to [ryan] that I think of him as the man of the house now. That's going to give him a bigger head.... the kind above his shoulders.... not the kind.... shit.... why did my mind go there?{/i}"
            scene bg MomDrinkingKitchen05
            with dissolve
            M "But really, I want to do something nice for just you to show how grateful I am to you. Isn't there anything you want to do? .... something that doesn't cost any money of course!"
            R "Hmmmm.... It's been a long time since we went swimming at the club, and we always go with Lauren and she takes all of your attention. I'd love to go with just you!"
            M "I said something that doesn't cost any money, dear..."
            R "Well, haven't you already paid the annual fee for the club membership?"
            M "Well, yeah.... I mean I guess we have.... but most of the fun is being able to eat at the club restaurant, and to be able to drink some wine and read my book while you kids swim in the pool."
            M "I don't know how much I would enjoy spending time at the club without..."
            scene bg MomDrinkingKitchen01
            with dissolve
            M "Wait.... sorry..."
            M "This isn't about what I want.... I want to reward you. So, if you want to go swimming at the club pool, then we'll go swimming at the club pool."
            M "Though, that's not asking much.... are you sure there's nothing else you want?"
            menu:
                "Can you show me one of the dances you did at the strip club?":
                    scene bg MomDrinkingKitchen02
                    with dissolve
                    if momlibido >= 6:
                        M "[upper_ryan]! I can't believe you have the balls to ask your own mother something like that!"
                        R "I know.... I'm sorry.... It's just that I've never seen a girl dance like that, and since I saw you dance at the club, and had to leave early when you saw me.... well.... I'm just really curious how a dance like that ends."
                        scene bg MomDrinkingKitchen02
                        with dissolve
                        M "[ryan] it's never appropriate to ask your mom to strip for you! What are you thinking?!"
                        R "Oh, no.... you misunderstood, I don't want you to strip for me, I just want to see the dance."
                        M "Oh.... you just want to see the dance? To see me shake my ass? And grind myself up on the pole.... hmmmm.... let me think about it.... how 'bout NO!!"
                        M "Now go get your swimming stuff and meet me in the car. You're lucky I'm still even taking you after asking me something like that!"
                        scene bg MomDrinkingKitchen01
                        MT "{i}Oh my God, that kid is getting ballsy! To ask ask your own mom to do a strip dance?.... Do I need to do something to put an end to this?.... {/i}"
                        MT "{i}Why is it that I'm not more upset about this? Do I feel flattered that my own son would want to see me shake my ass?{/i}"
                        MT "{i}Oh.... I know.... I'm just extra horny since [dad_name] hasn't been around to satisfy my needs, and a dildo and butt plug just aren't an adequate substitute.{/i}"
                        MT "{i}Otherwise.... I wouldn't let this kind of shit fly at all!!.... {/i}"
                        "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                        $ momlibido += 1
                        scene bg SleepBlack
                        with fade
                        $ renpy.pause (0.05)
                        jump clubpool
                    else:
                        scene bg MomDrinkingKitchen03
                        M "[upper_ryan]! I can't believe you have the balls to ask your own mother something like that!"
                        R "Oh, no.... I think you misunderst..."
                        M "I don't care what you meant, there is no possible way that you could have asked that in a way that is appropriate!"
                        M "I wanted to do something nice for you today to say thank you, but you have to go and act like this!?"
                        M "I still very much appreciate what you've done for me, but we'll have to see if you're more deserving for a reward next Sunday."
                        R "But I didn't mean..."
                        scene bg MomDrinkingKitchen02
                        with dissolve
                        M "No butts!"
                        M "I'm out of here!"
                        M "I've got to go cool down somewhere."
                        "{i}{b}\"Mom's Anger +1\"{/b}{/i}"
                        $ momanger += 1
                        $ timeofdaycounter += 1
                        scene bg Kitchen01
                        with fade
                        $ screen_on = "kitchenmap"
                        call screen kitchenmap
                "Can you try on your swimsuits, and let me choose which swimsuit you wear to the pool?" if inventory.inv_amount(jacky_bikini_01) == 1 and not bikini_show_failed:
                    if momsubmission >= 5 and momlibido >= 3:
                        scene bg MomDrinkingKitchen04
                        with dissolve
                        M "Oh.... my.... God.... [ryan]! Do you even know what the word subtle means?"
                        R "Huh?.... What do you mean?"
                        scene bg MomDrinkingKitchen05
                        with dissolve
                        M "I mean ever since you saw me at the club, you seem to be treating our relationship more intimate than a mother-son relationship should be."
                        M "And wanting to see me in my bikini just shows that you're getting brave enough to try to turn it into something it shouldn't be."
                        R "Mom! What are you talking about?"
                        M "Well.... just.... the fact that you're trying to get to see a fashion show in my.... bikini..."
                        R "Oh.... hohoho.... I get it.... you thought I was wanting to stare at your body in a bikini."
                        R "Hahah..."
                        scene bg MomDrinkingKitchen06
                        with dissolve
                        M "You aren't?"
                        R "Mom, as beautiful as you are, I've already seen you topless, and in a much more arousing setting I might add."
                        R "It's not like seeing you in a bikini is going to do more for me than that."
                        R "Also, no matter what swimsuit you wear, I'm going to eventually see it at the pool anyways, just like I have all of the other times we go swimming."
                        scene bg MomDrinkingKitchen02
                        with dissolve
                        M "Ok then you smart-ass, why would you ask for a swimsuit fashion show?"
                        R "Because I bought you a new swimming suit."
                        scene bg MomDrinkingKitchen06
                        with dissolve
                        M "You did what?..."
                        R "Yeah, I've been wanting to go to the pool, and I was worried that maybe you would say you couldn't take me because you don't have a new swimsuit to wear, you know, since the women at the club can be so judgy if they see you in the same swimsuit twice."
                        R "I was worried you'd use that as an excuse not to take me, like you have in the past."
                        R "And I know you don't have any money to buy one now, so when I asked for a fashion show, it was because I thought it would be a fun way to surprise you with a new one."
                        R "Although admittedly I do understand why you would have thought I was trying to get a sexy show."
                        R "And with your body, you can't help but make it sexy."
                        scene bg MomDrinkingKitchen01
                        with dissolve
                        M "[ryan], you can be such a flatterer."
                        M "You're so sweet to get me a new swimsuit, I guess we better go make sure it fits."
                        M "Go get the swimsuit and meet me outside my room."
                        jump bikinishow
                    else:
                        scene bg MomDrinkingKitchen02
                        with dissolve
                        M "[ryan]! I can't tell if that was supposed to be a joke or not, but either way it was inappropriate."
                        "{i}\"Mom's affection -3\"{/i}"
                        $ momaffection -= 3
                        R "But Mom, I was just..."
                        M "Just nothing! Sometimes your sense of humor and your sense of what's acceptable to say, and what's just creepy is a bit off."
                        R "No.... I.... just.... well I bought you a swimsuit..."
                        M "Once again that's a creepy thing to buy your mother.... why don't you just leave it by my bedroom door, and we'll meet in the car. Maybe I'll wear it sometime in the future."
                        jump clubpool
        "Just Leave her alone.":
            jump myroom

label commissionsecondoutfit:
    scene bg SidneyInKitchen
    with fade
    menu:
        "Talk to Sidney":
            scene bg SidneyKitchen01
            with fade
            S "Hey [ryan], what can I do for you?"
            R "Nothing, just felt like talking with you."
            scene bg SidneyKitchen03
            with dissolve
            S "Sorry little brother, but right now I'm really busy trying to finish up some designs."
            S "Come find me again when I'm not so busy."
            RT "{i}She's flashing me again!{/i}"
            RT "{i}Is she doing this on purpose?{/i}"
            RT "{i}Or could she really be this clueless?{/i}"
            R "Ok, I'll find you again soon."
            scene bg SidneyInKitchen
            with fade
            $ screen_on = "sidneykitchenmap"
            call screen sidneykitchenmap
        "Commission a new cosplay outfit.":
            scene bg SidneyKitchen01
            with fade
            $ laurenpictureprogress = 11
            S "Hey [ryan], what can I do for you?"
            R "I need you to make another cosplay outfit for Lauren."
            scene bg SidneyKitchen03
            with dissolve
            S "Really? There's not another convention for another 6 months. What's the occasion?"
            R "Lauren asked me to take pictures of her and Mandy in their outfits, and I posted them online."
            scene bg SidneyKitchen04
            with dissolve
            S "That sounds rather pervy!"
            R "No.... they asked me to!"
            S "Uh huh.... sure."
            R "Well anyways, their pictures got a ton of likes, and so sponsors are posting on their profile, and so basically, these pictures are making us a little money."
            R "I also sold both of the outfits, and people are commenting on their profile that they want to buy more outfits as well."
            R "They're offering more money if they don't wash them after wearing them for some reason."
            S "Uhhh.... that's because.... never mind."
            RT "{i}Haha.... she thinks I really don't know.{/i}"
            scene bg SidneyKitchen03
            with dissolve
            S "And obviously Lauren and Mandy are happy because they are getting attention online."
            R "Yep, they're on their way to achieving their dreams of getting internet famous."
            scene bg SidneyKitchen02
            with dissolve
            S "Hahah..."
            S "And how much are you paying them?"
            R "I'm not. All the money is going to pay Mom's Mafia debt each week."
            scene bg SidneyKitchen03
            with dissolve
            S "Does Mom know about this money?"
            R "Not yet, but don't tell her. I don't want to get her hopes up until we are doing better."
            S "More like you don't want Mom to shut you down when she realizes you're posting sexy pictures of her daughter online."
            R "Lauren is legally an adult. She can make that decision for herself."
            S "Ok, well sounds like you know what you're doing, and as long as I get paid, you can do whatever you want with these outfits."
            S "I'll charge you my standard rate."
            S "And what cosplay do you want?"
            R "I'll let you and Lauren work that out.... but it needs to be sexy!"
            S "Ok..."
            S "Oh, and you'll still be able to pay Mom's Mafia debt this week?"
            menu:
                "I have enough money for both." if money >= 800:
                    R "I've been working really hard lately, and I should have enough to pay for Lauren's outfit and the weekly Mafia debt."
                    "{i}{b}\"Sidney's Respect +1\"{/b}{/i}"
                    $ sidneyrespect += 1
                    S "Good for you little brother! Keep it up and maybe we will be able to get along without Dad after all."
                    "{i}\"Money - $400\"{/i}"
                    $ money -= 400
                "Mom can just work it off at the club this week.":
                    R "Why should I be the one responsible to pay off the debt every week, Mom can help out too."
                    S "Yeah, well I guess it's your money. You earned it. If you'd rather pay me for a sexy costume for your little sister then keep Mom safe from the Mafia that's up to you."
                    R "Oh please, Mom's not in any danger."
                    "{i}\"Money - $400\"{/i}"
                    $ money -= 400
                "You're right, I should save up a little more money first.":
                    scene bg SidneyInKitchen
                    with fade
                    $ screen_on = "sidneykitchenmap"
                    call screen sidneykitchenmap
            R "So, how long will it take to finish?"
            S "Give me a couple days and then I'll have it ready for fitting on Lauren."
            $ sidneymakingcosplay = True
            R "Awesome, I can't wait!"
            scene bg SidneyKitchen02
            with dissolve
            S "Haha, I'll bet you can't."
            R "What's that supposed to mean?"
            scene bg SidneyKitchen03
            with dissolve
            S "Oh, I think you know."
            S "I think you're enjoying more than the money from this little venture."
            RT "{i}She's flashing me again!{/i}"
            RT "{i}Is she doing this on purpose?{/i}"
            RT "{i}Or could she really be this clueless?{/i}"
            R "Whatever.... I'll keep checking back to see when you're done."
            scene bg SidneyInKitchen
            with fade
            $ screen_on = "sidneykitchenmap"
            call screen sidneykitchenmap
        "Never mind":
            $ screen_on = "sidneykitchenmap"
            call screen sidneykitchenmap

label secondcosplayfitting:
    $ sidneymakingcosplay = False
    $ cosplayoutfitcounter = 0
    scene bg KitchenArsetrid01
    with fade
    $ progress = 11
    R "Oh sweet! The new outfit is done!"
    $ laurenpictureprogress = 12
    R "Let me guess, Arsetrid, from \"How to Breed your Dragon\"?"
    L "Yep! Do you like it?"
    R "Yeah, but isn't that character a little young to be doing a sexy cosplay of her?"
    S "That's only in the first two movies, in the third movie Arsetrid is old enough that it shouldn't be weird."
    R "You sure know a lot about a kids movie series for a girl in college."
    scene bg KitchenArsetrid02
    with dissolve
    S "Oh, haha.... I'll have you know that almost half the audience of these animated movies are adults."
    R "Or are you just bumping the statistics by watching it over and over and over?"
    S "..."
    R "Ok then.... how close is it to being ready?"
    scene bg KitchenArsetrid03
    with dissolve
    S "Hmmm.... I'll have all the sizing done for the adjustments in about 10 minutes, and then I'll finish up all the sewing late tonight."
    S "So, you can probably take it anytime tomorrow."
    scene bg KitchenArsetrid04
    with dissolve
    R "Nice! Does tomorrow work for you Lauren?"
    L "My schedule is basically {b}weekdays in the late morning.{/b}"
    L "Just head to the {b}warehouse and give me a call{/b} when you're ready."
    R "Won't you miss school?"
    L "Yeah?.... So?.... Do you really expect me to sacrifice my free time to take pictures in a dirty old warehouse?"
    L "Besides.... Mom's letting you miss school to work."
    L "We'll just ask her to make the same exception for me."
    R "You haven't told her what you're doing for work, have you?"
    L "Haha of course not.... I'm leaving that up to you."
    RT "{i}Shit!.... How am I going to tell Mom about this?{/i}"
    RT "{i}Oh, well.... another problem for another day.{/i}"
    R "So, Sidney?"
    S "Yeah?"
    R "How easy is it to make adjustments to this outfit?"
    S "Do you mean how easy is it to strip this down into a skimpy whore outfit?"
    R ".... Basically.... yeah..."
    scene bg KitchenArsetrid05
    with dissolve
    S "Don't forget that it's your little sister you're taking pictures of please!"
    if sidneyfingerlaurenprogress >= 7:
        RT "{i}Says the girl jerking off her brother when she thinks he's sleeping.{/i}"
    R "Yeah, yeah.... I'll have you know I'm very respectful. I'm basically a feminist. This has been all Lauren's idea, and I'm just trying to help her feel empowered."
    S "{i}(sarcastically){/i} Wow!.... What a champion of women's rights!"
    L "Hahah..."
    R "K Lauren, so I'll give you a call when I'm ready."
    L "K bye!"
    scene bg RyansRoom01
    with fade
    $ screen_on = "ryanmap"
    call screen ryanmap

###########  JACKY'S ROOM  ################################################  JACKY'S ROOM  ################################################  JACKY'S ROOM  #######################################################  JACKY'S ROOM  #####################################################  JACKY'S ROOM  ##################################################MOM#Room##########

label bikinishow:
    $ bikini_show_seen = True
    scene bg BikiniShow01
    with fade
    M "Wow! I can't believe you bought me a Hyongu bikini. I know these aren't cheap!"
    M "How did you afford it? I better not have to strip at the club on Saturday because you spent too much on this bikini!"
    R "Don't worry, Mom, I found a really good deal. Plus I know how judgy the women at the club can be if they see you in a cheap swimsuit."
    R "And I know it's the kind of thing Dad would have bought for you."
    M "Well, thank you! Let me go try it on. Actually let me try on the one I've already got, and then I'll try on this new one. Then I'll let you decide which one I'm going to wear to the pool."
    R "Really? You're going to give me a bikini fashion show?!..."
    M "It's like you said, I guess.... you're going to see me in it at the pool anyways. And since you bought me this suit, I want you to decide if you like it enough for me to wear it to the club pool."
    M "But if there's a problem, and you can't keep \"little [ryan]\" from popping up and giving us a visit like he's been doing all too frequently lately, then the show will end, and we won't go to the pool. So, control yourself!"
    R "Of course.... I mean \"little [ryan]\" won't be visiting.... I mean.... yuck!.... Why would I react like that to my own mom?"
    M "Uh huh.... that's very reassuring."
    M "Give me just a second."
    scene bg BikiniShow02
    with dissolve
    RT "{i}I can't believe how easy it was to talk her into trying on bikinis for me.{/i}"
    RT "{i}I can't wait to see what I can talk her into next.{/i}"
    RT "{i}Maybe something at the pool.{/i}"
    play music SexMusic
    scene bg BikiniShowPink01
    with dissolve
    M "Ok, so this is the last swimsuit your father bought me before he was sent to prison."
    M "What do you think?"
    R "I think Dad has good taste."
    R "Pink looks really good on you."
    RT "{i}Oh my God.... stay in control. Stay in control. Stay in control.... {/i}"
    MT "{i}I wonder if I can get him excited. Then I wouldn't have to go to the pool.{/i}"
    scene bg BikiniShowPink02
    with dissolve
    M "It doesn't quite cover up as much of my ass as I would like it to though."
    R "Ummm.... yeah.... I think it's not.... too.... bad..."
    M "You doing ok back there [ryan]?"
    MT "{i}Haha.... I think I've almost got him.... {/i}"
    MT "{i}Shit.... what's the matter with me?.... {/i}"
    MT "{i}I shouldn't be trying to tease him in this way.{/i}"
    M "Alright, I'm going to try the other one on now."
    R "Ok.... I'll just.... wait here then..."
    MT "{i}Shit!.... Why did I agree to this?.... Why did I say those teasing comments?.... I've made it a bit awkward...{/i}"
    scene bg BikiniShow02
    with dissolve
    RT "{i}Oh my God!!.... Was Mom trying to turn me on, on purpose?!!.... {/i}"
    RT "{i}Ok.... un-sexy thought, un-sexy thoughts.... {/i}"
    RT "{i}Grandma naked, grandma naked, grandma naked.... {/i}"
    RT "{i}Shit.... grandma's too sexy also.... {/i}"
    RT "{i}I know.... grandpa naked on a cold day, grandpa naked on a cold day, grandpa naked on a cold day.{/i}"
    RT "{i}Oh thank God.... that took care of it.... {/i}"
    scene bg BikiniShowBlue01
    with dissolve
    M "Well?.... What do you think?"
    R "Wow!.... The blue is really pretty with your eyes!..."
    M "..."
    R "Turn around, let's see the back."
    M "Uhhh.... this one is too revealing in the back. I don't think I'd be comfortable wearing it in front of own son."
    M "Wait!.... I have an idea.... I'll be right back."
    scene bg BikiniShow02
    with dissolve
    R "{i}Shit! I was worried that buying a bikini with a thong bottom might be pushing it.{/i}"
    R "{i}I wonder if she'll even let me make a choice now.{/i}"
    scene bg BikiniShowBlue03
    with dissolve
    M "There. I found the perfect solution. It keeps me more modest in front of my son, but allows everyone at the club to imagine what's going on underneath them."
    RT "{i}Oh, I'm imagining all right.... shit.... I've got to stop imagining if I'm going to keep little [ryan] under control.{/i}"
    RT "{i}Grandpa naked on a cold day.... grandpa naked on a cold day.... grandpa naked on a cold day.... {/i}"
    RT "{i}Ok.... back in control.... {/i}"
    M "Well, what do you think?"
    R "I think it's a great idea. You're very resourceful."
    M "Haha.... thanks, I guess."
    scene bg BikiniShowBlue04
    with dissolve
    M "Ok, so what's it going to be? The pink one or the blue one?"
    RT "{i}Ok, well the pink one is more revealing since she's wearing the shorts. I mean I definitely get to see more of her ass.{/i}"
    RT "{i}The blue one is sexier, but those damn shorts!.... I wonder if there's some way I'll be able to get her to take them off at the club pool?{/i}"
    RT "{i}Which should I choose?{/i}"
    $ inventory.drop_outfit_inv(jacky_bikini_01)
    menu:
        "The Pink Bikini":
            R "Let's go with the pink one. I'm sorry about the other one, I couldn't tell from the online advertisement that it was going to be so immodest."
            M "You sure? I actually do love the Hyongu bikini, I just know I can't wear it without the shorts in front of my own son."
            R "Yeah, I think you'll still be more comfortable in the pink one."
            M "The pink one it is. Why don't you run and get ready and I'll meet you in the car."
            jump clubpool
        "The Blue Bikini":
            R "Let's go with the Hyongu. I really do love that color on you."
            M "So do I! Thank you so much for buying me something. I haven't been able to get anything new since the FBI cut off our discretionary spending."
            M "And a Hyongu is such a stylish bikini. I'll be proud to wear this one more than once."
            "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
            $ momaffection += 1
            M "Alright. Why don't you run and get ready for the pool, and I'll meet you in the car."
            $ chosebluebikini = True
            play music Honey
            jump clubpool

###########  LAUREN'S ROOM  ############################################  LAUREN'S ROOM  ##############################################  LAUREN'S ROOM  ######################################################  LAUREN'S ROOM  ##################################################  LAUREN'S ROOM  #####################################################

label diaz_and_lauren:

    $ persistent.gal_Lauren_5 = True

    scene bg DiazVisit07
    with fade
    if first_diaz_dance == True:
        L "And now what do you want from your toy?"
    else:
        L "And now what do you want from me?"
    AD "I just love me a girl in a school uniform, but I think you should sexy yours up just a bit."
    L ".... Fine!..."
    L "But I'm not getting naked in front of you. I'm going to go change in the bathroom."
    AD "That's fine.... suit yourself."
    scene bg DiazVisit10
    with dissolve
    LT "{i}I can't believe I've got a legitimate creeper in my room.{/i}"
    LT "{i}At least it's not some nasty old man like Mom has to deal with at the club.{/i}"
    LT "{i}I can't believe Mom hid that from me.{/i}"
    LT "{i}And that [ryan] knew, and didn't tell me.{/i}"
    LT "{i}He's just watching out for Mom, that's actually pretty sweet.{/i}"
    LT "{i}I wish he'd been able to get me out of this though.{/i}"
    LT "{i}Diaz is even pretty hot.... I wonder what drove her to like other women.... {/i}"
    LT "{i}Probably some kind of traumatic experience like this one.{/i}"
    if first_diaz_dance == True:
        LT "{i}Am I going to start liking other women?{/i}"
        LT "{i}I do think Diaz is pretty sexy!{/i}"
        LT "{i}And Kenzie and I have experimented a little.{/i}"
        LT "{i}But seeing [ryan]'s cock made me feel some pretty confusing feelings too.{/i}"
        LT "{i}Shit.... I'm getting pretty screwed up.{/i}"
    scene bg DiazVisit11
    with dissolve
    play music SexMusic
    L "Well, Is this sexy enough for you?"
    AD ".... Just.... wow!..."
    scene bg LaurenDoor
    with fade
    RT "{i}I've got to see this!{/i}"
    RT "{i}Not just for my own enjoyment, but to make sure Agent Diaz doesn't take things too far.{/i}"
    scene bg DiazVisit08
    with dissolve
    if first_park_run:
        RT "{i}Luckily Sidney will be out jogging this morning.  I have no idea how I'd explain this to her.{/i}"
    else:
        RT "{i}Luckily Sidney can sleep through a train driving through the house, cuz I don't know how I'd explain this to her.{/i}"
    scene bg DiazVisit09
    with fade
    RT "{i}Oh, wow! I wish she'd wear her uniform like that to school.{/i}"
    RT "{i}Hmmmmm.... I wonder if Mom could ever be convinced to allow that dress code in her class.{/i}"
    RT "{i}I know school board member Will Tylor would gladly agree to that kind of dress code.{/i}"
    scene bg DiazVisit11
    with fade
    AD "If we're going to count this favor against your debt, you have to at least pretend that you're enjoying this."
    AD "Why don't you start out with some sexy dancing. I'll turn on some music on my phone for you."
    play music ClubMusic
    AD "All right Lauren, let's see you move that body!"
    AD "Lauren..."
    L "Fine!"
    scene bg DiazVisit12
    with dissolve
    AD "That's right!"
    AD "Yeah.... move those hips..."
    LT "{i}This is kind of like dancing for my old boyfriend, I'll try to just go there mentally.{/i}"
    LT "{i}Shit, I hate him almost as much as Agent Diaz though.{/i}"
    AD "Let's see you shake that booty!"
    scene bg DiazVisit13
    with dissolve
    if first_diaz_dance == False:
        AD "Yeah, wow Lauren.... what an ass you've got!"
        L "Please don't objectify me like that. You're making me really uncomfortable."
        AD "What do you think you are?"
        AD "You \"are\" just an object for my enjoyment."
        $ first_diaz_dance = True
        play music SexMusic
        scene bg DiazVisit48
        with dissolve
        AD "I came in here and just took you like that, without having to hardly try."
        AD "You put on a sexy outfit for me just because I asked."
        L "No.... because you're blackmailing us."
        AD "That's right! My leverage over you makes you and your brother mine."
        AD "Now come climb over my knee, so I can show you that you're mine."
        L "No!"
        AD "Do it, or I arrest you and [ryan] for hiding your income from the IRS, and tell your mom all about your sexy picture shoots."
        L "Fine!"
        scene bg DiazVisit15
        with fade
        AD "There, now that's a much more obedient girl!"
        AD "Now let's uncover that beautiful little ass of yours."
        scene bg DiazVisit16
        with dissolve
        AD "Yes, that's very fine!"
        AD "And now it's time to teach you what you are."
        scene bg DiazVisit17
        with dissolve
        AD "Tell me that \"you\" are my toy."
        L "What the hell?.... I'm not saying that!"
        play sound Slap
        scene bg DiazVisit18
        with dissolve
        $ renpy.pause ()
        scene bg DiazVisit17
        with dissolve
        L "Ouch! You bitch!"
        AD "Say it!"
        L "No!"
        play sound Slap
        scene bg DiazVisit20
        with dissolve
        $ renpy.pause ()
        scene bg DiazVisit19
        with dissolve
        AD "I'm just going to keep spanking you until you admit that you're my toy."
        AD "So, say it."
        L "Never!"
        play sound Slap
        scene bg DiazVisit20
        with dissolve
        $ renpy.pause ()
        scene bg DiazVisit21
        with fade
        RT "{i}Oh my God! She's spanking Lauren!{/i}"
        play sound Slap
        scene bg DiazVisit22
        with fade
        RT "{i}Why do I find that so hot?.... {/i}"
        RT "{i}I've got the biggest boner right now!{/i}"
        play sound Slap
        RT "{i}I hope that slapping doesn't wake up Sidney.{/i}"
        scene bg DiazVisit19
        with fade
        AD "Well, are you going to say it?"
        L "Yes! I'll say it.... I'm.... your.... toy..."
        play sound Slap
        scene bg DiazVisit20
        with dissolve
        $ renpy.pause ()
        scene bg DiazVisit19
        with dissolve
        L "Ouch!.... I said it!.... Why did you spank me again?"
        AD "Say it louder like you mean it!"
        L "I'm your toy!!.... I'm your fucking toy!!..."
        AD "That's right, and here's a few more to seal that in your thick skull."
        play sound Slap
        scene bg DiazVisit20 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit19 with Dissolve (0.5)
        $ renpy.pause (1.0)
        play sound Slap
        scene bg DiazVisit20 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit19 with Dissolve (0.5)
        $ renpy.pause (1.0)
        play sound Slap
        scene bg DiazVisit20 with Dissolve (0.5)
        $ renpy.pause (1.0)
        AD "There now remember what you are on my next visit!"
        L "Yes, Agent Diaz, your toy will remember."
        AD "That's right!"
        AD "Maybe I'll see you next week. We'll see how your brother does."
        scene bg SleepBlack
        with fade
        scene bg DiazVisit02
        with fade
        play music Honey
        AD "Well, I hope you enjoyed the show."
        R ".... I.... how did?..."
        AD "Remember! I already know you're recording your family."
        AD "I can only assume you were watching that too."
        AD "And just to give you a little incentive, if your relationship with your sister gets a little more advanced,"
        AD "I just might start to include you in these little games of ours."
        R "Whaa.... what are you implying.... the very idea.... goodbye!"
        play sound CloseDoor
        scene bg DiazVisit47
        with dissolve
        RT "{i}Holy shit! I'm going to cum right here in my pants! The thought of Lauren and myself with Diaz!.... Shit, that's hot!{/i}"
        RT "{i}Shit!.... I'd better go check on Lauren.{/i}"
        scene bg SleepBlack
        with fade
        scene bg DiazVisit23
        with fade
        LT "{i}Damn my ass is really sore.{/i}"
        LT "{i}I can't believe that bitch made me call myself her toy.{/i}"
        LT "{i}How did she get that kind of power over me?{/i}"
        LT "{i}I couldn't do anything to stop her from doing that to me.{/i}"
        LT "{i}Like I really was her toy.... {/i}"
        LT "{i}Fuck!.... {/i}"
        scene bg DiazVisit24
        with dissolve
        R "Lauren?.... Are you ok?..."
        L "I don't know.... what do you think?..."
        L "She made me call myself her toy..."
        L "She wouldn't stop spanking me until I did..."
        R "You just said it to make it stop!"
        R "That doesn't mean you're really her toy!"
        scene bg DiazVisit25
        with dissolve
        L "Please, [ryan]! Do everything you can to make sure we can pay her next week!"
        L "I don't want to do anything for that bitch ever again."
        R "Yeah.... well, it's not all on me.... I've got two ransoms to pay now, don't I?"
        R "The best thing we can do is make sure the Cosplay business takes off."
        R "Are you willing to do your part to make that happen?"
        L "Yes! Please!.... I'll take more clothes off during picture shoots. Anything so I don't have to do that again!"
        R "Well, let's try to make some money then."
        L "Thank you!!"
        "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
        $ laurensubmission += 1
        R "We'd better get ready for school. We're going to be late."
        $ timeofdaycounter = 2
        jump myroom
    else:
        AD "Yeah, wow Lauren.... what an ass you've got!"
        AD "Does my toy like shaking it for me?"
        L "Yes, your toy loves shaking her ass for you."
        AD "And you're one sexy toy!"
        play music SexMusic
        scene bg DiazVisit14
        with dissolve
        L "You stopped the music!"
        L "Does that mean you want your toy to do something else?"
        AD "Your teacher called me."
        AD "She said you've been so naughty that she can't handle you."
        AD "She needed a real disciplinarian to take care of you!"
        AD "Is my toy a naughty girl?"
        L "Yes, Agent Diaz!"
        L "I'm a very naughty girl."
        AD "You'd better get your ass over my knee again then!"
        scene bg DiazVisit48
        with dissolve
        L "What? But I called myself your toy!"
        L "Why are you punishing me again?"
        AD "If you were my toy, you wouldn't argue."
        AD "Now get your ass over my knees!"
        L "Yes, Agent Diaz."
        scene bg DiazVisit15
        with fade
        AD "There, now that's a much more obedient girl!"
        AD "Now let's uncover that beautiful little ass of yours."
        scene bg DiazVisit16
        with dissolve
        AD "Yes, that's very fine!"
        AD "And now it's time to remind you what you are."
        scene bg DiazVisit17
        with dissolve
        AD "Tell me that \"you\" are my toy."
        play sound Slap
        scene bg DiazVisit18
        with dissolve
        $ renpy.pause ()
        scene bg DiazVisit17
        with dissolve
        L "Ouch! You bitch!"
        AD "Say it!"
        L "I'm your toy!"
        play sound Slap
        scene bg DiazVisit20
        with dissolve
        $ renpy.pause ()
        scene bg DiazVisit19
        with dissolve
        L "Ouch!.... I said it!.... Why did you spank me again?"
        AD "Say it louder like you mean it!"
        L "I'm your toy!!.... I'm your fucking toy!!..."
        AD "That's right, and here's a few more to solidify that in your thick skull."
        play sound Slap
        scene bg DiazVisit20 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit19 with Dissolve (0.5)
        $ renpy.pause (1.0)
        play sound Slap
        scene bg DiazVisit20 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit19 with Dissolve (0.5)
        $ renpy.pause (1.0)
        play sound Slap
        scene bg DiazVisit20 with Dissolve (0.5)
        $ renpy.pause (1.0)
        AD "There, now remember what you are on my next visit!"
        L "Yes, Agent Diaz, your toy will remember."
        AD "That's right!"
        AD "Maybe I'll see you again next week. We'll see how your brother does."
        scene bg SleepBlack
        with fade
        scene bg DiazVisit02
        with fade
        play music Honey
        AD "Well, I hope you enjoyed the show again."
        R "Yeah.... it's actually pretty hot."
        AD "And just to remind you. If your relationship with your sister gets a little more advanced,"
        AD "I just might start to include you in these little games of ours."
        R "I'll see what I can do!"
        AD "Hahah.... you're my toy now too!..."
        AD "I'll see you next week."
        play sound CloseDoor
        scene bg DiazVisit47
        with dissolve
        RT "{i}Holy shit! I'm going to cum right here in my pants! The thought of Lauren and myself with Diaz!.... Shit, that's hot!{/i}"
        RT "{i}Shit!.... I'd better go check on Lauren.{/i}"
        scene bg SleepBlack
        with fade
        scene bg DiazVisit23
        with fade
        LT "{i}Damn my ass is really sore.{/i}"
        LT "{i}It wasn't nearly as bad this time though.{/i}"
        LT "{i}Was it because I knew what to expect?{/i}"
        LT "{i}I felt so dirty to willingly call myself her toy.{/i}"
        LT "{i}My job is just to bring her pleasure.... {/i}"
        LT "{i}Fuck!.... Get out of my head.{/i}"
        scene bg DiazVisit24
        with dissolve
        R "Lauren?.... Are you ok?..."
        L "I don't know.... It wasn't nearly as bad this time..."
        L "I called myself her toy.... and she still spanked me."
        R "Did it hurt really bad?"
        L "Not as bad.... but in a strange way.... it felt kind of good..."
        scene bg DiazVisit25
        with dissolve
        L "Please, [ryan]! Do everything you can to make sure we can pay her next week!"
        L "I'm worried about what this is doing to me psychologically."
        R "You know I'm doing my best to cover for you and Mom!"
        R "The best thing we can do is make sure the Cosplay business takes off."
        R "Are you willing to do your part to make that happen?"
        L "Yes! Please!.... I'll take more clothes off during picture shoots. Anything so I don't have to do that again!"
        R "Well, let's try to make some money then."
        L "Thank you!!"
        "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
        $ laurensubmission += 1
        R "We'd better get ready for school. We're going to be late."
        $ timeofdaycounter = 2
        jump myroom

label ryan_and_lauren:

    $ persistent.gal_Lauren_5 = True

    if first_lauren_grind == False:
        scene bg DiazVisit26
        with fade
        L "I know we need to get ready for school, but I really wanted to thank you for protecting me from Agent Diaz."
        R "That's what big brothers are for, Lauren."
        "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
        $ laurenaffection += 1
        L "Well, lately you've been much more to me than a big brother."
        $ first_lauren_grind = True
        R "How do you mean?"
        L "I don't know, it's like you've changed since Dad went to prison. You've stepped up, but you've also been treating me differently."
        L "I don't know what changed you.... but I like it."
        RT "{i}I'm pretty sure jacking off to Mom while she was stripping changed me more than Dad going to prison.{/i}"
        RT "{i}In hindsight, I probably shouldn't have done that.{/i}"
        L "I've noticed you staring at my ass a lot lately, but you act like a professional during our photoshoots,"
        L "But I can't help but notice you're always pitching a tent once I start taking off my clothes."
        R "Just because I'm your brother doesn't mean I won't get turned on looking at your tits and ass."
        R "I've tried to tactfully conceal my hard-on."
        LT "{i}Yeah right, like you could do anything to hide that monster.{/i}"
        L "Well, no judgements, and anyways, this gives me an idea of how I can return the favor."
        L "Just sit there, close your eyes, and don't say anything."
        R "Ok..."
        scene bg SleepBlack
        with fade
        $ renpy.pause ()
        scene bg DiazVisit27
        with dissolve
        R "Holy shit Lauren, do you want me to leave?..."
        L "What?.... No.... you're not supposed to say anything yet.... and you're supposed to keep your eyes closed!..."
        R "{i}(whispering){/i} sorry..."
        scene bg SleepBlack
        with fade
        $ renpy.pause ()
        scene bg DiazVisit28
        with dissolve
        RT "{i}Oh my.... how am I supposed to keep my eyes shut for this.... {/i}"
        L "Ok, I'm serious, keep your eyes closed."
        scene bg SleepBlack
        with fade
        $ renpy.pause ()
        L "Ok, you can open your eyes now."
        scene bg DiazVisit29
        with fade
        R "Holy fuck, Lauren!.... Are you going to school like that?"
        L "No, you idiot!"
        L "This is for you."
        R "What?!!"
        L "Oh, God.... please tell me I didn't mis-read the situation?"
        L "I thought you might enjoy a little eye candy before school."
        L "Give you something to think about all day."
        R "Wow, Lauren! You look incredible!"
        L "Now that's the reaction I was hoping for."
        L "Now let me just turn on some music."
        play music ClubMusic
        scene bg DiazVisit30
        with dissolve
        R "Wow! I've seen a lot of your body on the photo shoots,"
        R "But I've never seen you move like this before."
        LT "{i}Oh, the look on his face!.... I think he's really enjoying this!{/i}"
        L "If you like that, I think you'll really like this."
        scene bg DiazVisit31
        with dissolve
        R "Oh fuck, Lauren.... your ass is beautiful!"
        L "Heheh.... I was always pretty sure you liked it."
        scene bg DiazVisit32
        with dissolve
        play music SexMusic
        L "So, Mr. [ryan]."
        R "Huh?.... Why did you stop the dancing?"
        L "I know I'm getting an \"F\" in Anatomy, so I was hoping there was something I could do to bring up my grade."
        RT "{i}Oh, nice! Lauren wants to do some role-play.{/i}"
        RT "{i}Maybe it's easier for her if she pretends I'm not her brother?{/i}"
        R "I don't know, young lady. You've skipped my class almost every day to make out with the head cheerleader, Megan."
        L "Megan!?.... Really?"
        R "Shhhh.... don't break out of character, it ruins the illusion."
        LT "{i}You asshole!{/i}"
        R "I can hardly allow you to pass on to the next grade after displaying that incredibly lewd, but sexy behavior."
        scene bg DiazVisit33
        with dissolve
        L "There must be something I can do to change your mind."
        R "Nope! There's nothing I can think of that would keep me from failing you."
        L "What if I show you..."
        scene bg DiazVisit34
        with dissolve
        L "These!..."
        R "..."
        R "I.... I.... I..."
        L "Hahaha.... what's under your pants is saying everything."
        R "Oh my God, Lauren.... I love those perky little titties!"
        scene bg DiazVisit35
        with dissolve
        L "I'm so sorry [ryan], but I need you to hold me like this!..."
        R "I had no idea you felt like this for me."
        R "I mean I hoped you did."
        L "[ryan], just shut up.... I know this is so wrong.... and we can't ever do more than this..."
        L "But I need to have at least this..."
        R "It's the fact that it is so forbidden that makes this so hard to resist."
        L "Oh, God.... I know..."
        scene bg DiazVisit36 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit37 with Dissolve (0.5)
        $ renpy.pause (1.0)
        play sound Lauren01 loop
        scene bg DiazVisit36 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit37 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit36 with Dissolve (0.5)
        $ renpy.pause (1.0)
        LT "{i}[ryan]'s cock is so big! He is just throbbing and twitching all the way through all of our clothes.{/i}"
        LT "{i}It's a good thing we'll never go further than this. I think I'd be fully impaled by his enormous shaft.{/i}"
        scene bg DiazVisit36 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit37 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit36 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit37 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit36 with Dissolve (0.5)
        $ renpy.pause (1.0)
        stop sound fadeout 1.0
        scene bg SleepBlack
        with fade
        if spycaminlaurenroom:
            scene bg DiazVisit38
            with fade
            ADT "{i}Ugghh.... back to my boring surveillance job for another week.{/i}"
            ADT "{i}At least I've got an extra $500 to enjoy.{/i}"
            scene bg DiazVisit39
            with fade
            ADT "{i}Time to watch my favorite family on the TV again.{/i}"
            ADT "{i}So much drama.... will they?.... Won't they?.... {/i}"
            ADT "{i}(sarcastically) I can't wait to watch the next episode.{/i}"
            ADT "{i}Pretty handy that [ryan] installed those spy cameras and saved me the hassle.{/i}"
            ADT "{i}They were so easy to hack into.{/i}"
            ADT "{i}I should check Lauren's room, she might be getting dressed for school.{/i}"
            scene bg DiazVisit40
            with dissolve
            ADT "{i}Oh my God.... this is interesting!{/i}"
            ADT "{i}Haha.... I'm not surprised!{/i}"
            scene bg DiazVisit41
            with fade
            ADT "{i}Just give them a little more time, and they'll be fucking like rabbits.{/i}"
            scene bg DiazVisit42 with Dissolve (0.5)
            $ renpy.pause (1.0)
            scene bg DiazVisit43 with Dissolve (0.5)
            $ renpy.pause (1.0)
            play sound Diaz01 loop
            scene bg DiazVisit42 with Dissolve (0.5)
            $ renpy.pause (1.0)
            scene bg DiazVisit43 with Dissolve (0.5)
            $ renpy.pause (1.0)
            scene bg DiazVisit42 with Dissolve (0.5)
            $ renpy.pause (1.0)
            scene bg DiazVisit43 with Dissolve (0.5)
            $ renpy.pause (1.0)
            scene bg DiazVisit42 with Dissolve (0.5)
            $ renpy.pause (1.0)
            scene bg DiazVisit43 with Dissolve (0.5)
            $ renpy.pause (1.0)
            scene bg DiazVisit42 with Dissolve (0.5)
            $ renpy.pause (1.0)
            scene bg DiazVisit43 with Dissolve (0.5)
            $ renpy.pause (1.0)
            stop sound fadeout 1.0
            scene bg SleepBlack
            with fade
        else:
            pass
        scene bg DiazVisit44
        with fade
        $ renpy.pause (1.0)
        play sound Lauren01 loop
        scene bg DiazVisit45 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit44 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit45 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit44 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit45 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit44 with Dissolve (0.5)
        $ renpy.pause (1.0)
        stop sound fadeout 1.0
        scene bg DiazVisit45 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit44 with Dissolve (0.5)
        $ renpy.pause (1.0)
        play sound Ejaculate
        scene bg DiazVisit45
        with dissolve
        $ renpy.pause ()
        play sound Ejaculate
        scene bg DiazVisit46
        with fade
        L "Well, big brother?"
        L "How was that?"
        R "Uuuuhhh..."
        L "Hahah.... that's what I thought."
        L "I think you came bucketloads."
        L "Your shorts are soaking wet."
        R "Uuuhhhhhh..."
        L "Hahah.... you'd better run and get ready for school. I'm already halfway dressed."
        $ timeofdaycounter = 2
        play music Honey
        jump myroom
    else:
        scene bg DiazVisit26
        with fade
        L "I know we need to get ready for school, but I really wanted to thank you again for protecting me from Agent Diaz."
        R "That's what big brothers are for, Lauren."
        "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
        $ laurenaffection += 1
        L "Well, I wanted to take this opportunity again to return the favor."
        R "Well, I'll never say not to that."
        L "Just sit there, close your eyes, and don't say anything."
        R "Ok..."
        scene bg SleepBlack
        with fade
        $ renpy.pause ()
        scene bg DiazVisit27
        with dissolve
        RT "{i}How am I supposed to resist a few peeks?{/i}"
        scene bg SleepBlack
        with fade
        $ renpy.pause ()
        scene bg DiazVisit28
        with dissolve
        L "[ryan]? Are you peeking?"
        scene bg SleepBlack
        with fade
        $ renpy.pause ()
        L "Ok, you can open your eyes now."
        scene bg DiazVisit29
        with fade
        R "Wow, Lauren! I'll never get tired of seeing you in that outfit."
        L "Just talk Mom into changing the dresscode for her class and you won't have to."
        R "Haha.... I know school board member Will Tylor would approve the changes."
        L "So, I thought you might enjoy a little eye candy before school again?"
        L "Give you something to think about all day."
        R "Well, you thought right!"
        L "Now let me just turn on some music."
        play music ClubMusic
        scene bg DiazVisit30
        with dissolve
        R "I love the way you move those hips."
        LT "{i}Oh, the look on his face!.... I think he's really enjoying this!{/i}"
        L "If you like that, I think you'll really like this."
        scene bg DiazVisit31
        with dissolve
        R "Oh fuck, Lauren.... your ass is beautiful!"
        L "Heheh.... I know you love it."
        scene bg DiazVisit32
        with dissolve
        play music SexMusic
        L "So, Mr. [ryan]."
        L "I know I'm getting an \"F\" in Anatomy, so I was hoping there was something I could do to bring up my grade."
        RT "{i}Oh, nice! Lauren wants to do some role-play.{/i}"
        R "I don't know, young lady. You've skipped my class almost every day to make out with the head cheerleader, Megan."
        L "That's because she tastes like cherries.... I love cherries."
        R "Maybe you could give my your cherry!"
        L "You might have to take it."
        R "But young woman, I can hardly allow you to pass on to the next grade after displaying that incredibly lewd, but sexy behavior."
        scene bg DiazVisit33
        with dissolve
        L "There must be something I can do to change your mind."
        R "Nope! There's nothing I can think of that would keep me from failing you."
        L "What if I show you..."
        scene bg DiazVisit34
        with dissolve
        L "These!..."
        R "Hmmmm.... well for those I might reconsider."
        L "Hahaha.... what's under your pants tells me that you will."
        R "Oh my God, Lauren.... I love those perky little titties!"
        scene bg DiazVisit35
        with dissolve
        L "I'm so sorry [ryan], but I need you to hold me like this!..."
        R "I thought you said we couldn't do this again."
        L "[ryan], just shut up.... I know this is so wrong.... and this has to be the last time..."
        L "But I need this today so badly!..."
        R "A little more forbidden fruit huh?"
        L "Oh, God.... yes..."
        scene bg DiazVisit36 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit37 with Dissolve (0.5)
        $ renpy.pause (1.0)
        play sound Lauren01 loop
        scene bg DiazVisit36 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit37 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit36 with Dissolve (0.5)
        $ renpy.pause (1.0)
        LT "{i}[ryan]'s cock is so big! He is just throbbing and twitching all the way through all of our clothes.{/i}"
        LT "{i}It's a good thing we'll never go further than this. I think I'd be fully impaled by his enormous shaft.{/i}"
        scene bg DiazVisit36 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit37 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit36 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit37 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit36 with Dissolve (0.5)
        $ renpy.pause (1.0)
        stop sound fadeout 1.0
        scene bg SleepBlack
        with fade
        if spycaminlaurenroom:
            scene bg DiazVisit38
            with fade
            ADT "{i}Ugghh.... back to my boring surveillance job for another week.{/i}"
            ADT "{i}At least I've got an extra $500 to enjoy.{/i}"
            scene bg DiazVisit39
            with fade
            ADT "{i}Time to watch my favorite family on the TV again.{/i}"
            ADT "{i}I wonder if [ryan] and Lauren are going at it again.{/i}"
            scene bg DiazVisit40
            with dissolve
            ADT "{i}Haha.... looks like I'm an aphrodisiac!{/i}"
            ADT "{i}I wonder when they'll take it further.{/i}"
            scene bg DiazVisit41
            with fade
            ADT "{i}Just give them a little more time, and they'll be fucking like rabbits.{/i}"
            scene bg DiazVisit42 with Dissolve (0.5)
            $ renpy.pause (1.0)
            scene bg DiazVisit43 with Dissolve (0.5)
            $ renpy.pause (1.0)
            play sound Diaz01 loop
            scene bg DiazVisit42 with Dissolve (0.5)
            $ renpy.pause (1.0)
            scene bg DiazVisit43 with Dissolve (0.5)
            $ renpy.pause (1.0)
            scene bg DiazVisit42 with Dissolve (0.5)
            $ renpy.pause (1.0)
            scene bg DiazVisit43 with Dissolve (0.5)
            $ renpy.pause (1.0)
            scene bg DiazVisit42 with Dissolve (0.5)
            $ renpy.pause (1.0)
            scene bg DiazVisit43 with Dissolve (0.5)
            $ renpy.pause (1.0)
            scene bg DiazVisit42 with Dissolve (0.5)
            $ renpy.pause (1.0)
            scene bg DiazVisit43 with Dissolve (0.5)
            $ renpy.pause (1.0)
            stop sound fadeout 1.0
            scene bg SleepBlack
            with fade
        else:
            pass
        scene bg DiazVisit44
        with fade
        $ renpy.pause (1.0)
        play sound Lauren01 loop
        scene bg DiazVisit45 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit44 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit45 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit44 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit45 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit44 with Dissolve (0.5)
        $ renpy.pause (1.0)
        stop sound fadeout 1.0
        scene bg DiazVisit45 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg DiazVisit44 with Dissolve (0.5)
        $ renpy.pause (1.0)
        play sound Ejaculate
        scene bg DiazVisit45
        with dissolve
        $ renpy.pause ()
        play sound Ejaculate
        scene bg DiazVisit46
        with fade
        L "Well, big brother?"
        L "How was that?"
        R "Uuuuhhh..."
        L "Hahah.... that's what I thought."
        L "I think you came bucketloads again."
        L "Your shorts are soaking wet."
        R "Uuuhhhhhh..."
        L "Hahah.... you'd better run and get ready for school. I'm already halfway dressed."
        $ timeofdaycounter = 2
        play music Honey
        jump myroom

#################  SCHOOL  #################################################  SCHOOL  ################################################  SCHOOL  ##################################################  SCHOOL  ##########################################  SCHOOL  ###############################################################  SCHOOL  ################

label meganloyaltyblowjob:
    $ firstloyaltyblowjob = True
    scene bg MeganInHall01
    with fade
    RT "{i}Shit.... I'm late again.... oh look there's Megan.... {/i}"
    RT "{i}She kind of looks like she's waiting for me.... {/i}"
    scene bg MeganInHall02
    with fade
    MG "Hey [ryan], How's my new favorite stud in school?"
    R "Uhhhh.... are you sure I'm who you think I am?.... You never talk to me.... plus we're late for class."
    MG "It's not that I've never wanted to talk to you.... It's just that Matt's my boyfriend, and he kind of tells me who I'm allowed to talk to."
    R "But I see you flirting with other guys and teachers all of the time."
    scene bg MeganInHall05
    with dissolve
    MG "Only guys and teachers that Matt is trying to get something out of."
    MG "And occasionally teachers when I want to get something out of them."
    R "Yeah.... that's very uhh.... well, kind of messed up."
    MG "Yeah.... I know.... but I'm afraid to end things with Matt."
    MG "He can be a little bit possessive, and sometimes violent."
    RT "{i}Man I'm glad I didn't accept his help. He sounds like a first class asshole.{/i}"
    RT "{i}Maybe I can show him that he's not the shit by messing with his girl.{/i}"
    RT "{i}I know she's probably trying to get something out of me, but why not try to get something out of her in return?{/i}"
    R "Do you ever feel like you want to end things with Matt?"
    scene bg MeganInHall02
    with dissolve
    MG "Sometimes, but then I remember the size of his cock, and you know what they say about how once you've had black..."
    RT "{i}Shit.... then the rumors are true.{/i}"
    MG "But I hear that you're quite a bit bigger than the average fucker."
    R "What?.... Who told you that?..."
    MG "I've been befriending Lauren the last couple days."
    MG "And she told me that you've got a monster in those pants."
    R "What?.... She.... saw it by accident.... she shouldn't be blabbing that around."
    MG "To be honest, it's not a bad bit of information to have out there.... It can really make you trend with the girls in the school."
    R "Well, why are you befriending Lauren in the first place?"
    scene bg MeganInHall05
    with dissolve
    MG "Because I saw her Cosplay Heaven profile, and her costumes and pics are amazing!"
    MG "I've always wanted to go viral in some way on the internet, and Cosplay has never been an option."
    MG "I tried making a costume once, and it just looked like a 5 yr old had made it. And the only pictures I'm good at taking are selfies."
    MG "Lauren told me that you're the one who has put the whole venture together, and that you even take the pictures."
    scene bg MeganInHall02
    with dissolve
    MG "So, how do you like taking those kinds of pictures of your own sister?"
    R "It's not like that.... It's completely professional..."
    MG "Except that Lauren told me you end up pitching a tent during the entire photo shoot."
    R "Why the hell is she telling you all of this?"
    MG "It's a gift. Girls love to tell me everything.... they are always trying to keep my attention."
    R "So, is there a point to everything you're telling me?"
    MG "Right. So, I want to be a model for your photo business."
    R "..."
    R "What?!!..."
    R "No way!..."
    R "This is a family business..."
    R "And we need all the money we make.... so.... so.... I can't afford to pay you."
    scene bg MeganInHall03
    with dissolve
    MG "Please!"
    MG "You can keep the money, If I can get famous enough, people will beg me to pose for money. I just need your help getting started."
    MG "I'll do anything you tell me to."
    MG "I'll pose nude, I'll let you photoshop me into kinky stuff."
    MG "I'll pose with girls, I'll pose with boys..."
    MG "Whatever you want."
    R ".... I don't know..."
    R "I'll have to think about it."
    scene bg MeganInHall04
    with dissolve
    MG "You'll think about it?"
    MG "That's all I ask!"
    MG "But let me give you something to help you make a decision."
    MG "Come on, follow me to the boy's bathroom."
    R "What?!"
    MG "Just come on..."
    scene bg SleepBlack
    with fade
    MG "Ok, so just sit down there on the toilet."
    R "Wait!.... I need to put a liner down first."
    MG "Are you trying to ruin the vibes?"
    R "Vibes for what?"
    MG "Just sit down."
    scene bg SchoolBathBlow03
    with dissolve
    play music SexMusic
    MG "So.... are you ready to get your knob polished?"
    R ".... What?!!.... Am I?.... Really?"
    MG "Yeah.... I've got to see for myself what your sister was bragging about."
    R "Just to be clear.... she only saw me by accident. She shouldn't be coming into my room early in the mornings!!"
    MG "Just relax, and unzip."
    R "Wow!"
    scene bg SchoolBathBlow04
    with fade
    MG "Wow yourself, you're already hard, and almost as big as Matt is!"
    MG "You've got the second biggest cock I've ever seen.... yummy..."
    MG "Now just relax while I take care of you."
    scene MeganHJVideo01
    with fade
    $ renpy.pause ()
    R "Oh shit, this feels so good."
    MG "Haha.... well, hold on a little longer."
    scene bg SchoolBathBlow07 with Dissolve(0.3)
    $ renpy.pause (0.1, hard=True)
    scene bg SchoolBathBlow08 with Dissolve(0.3)
    $ renpy.pause (0.1, hard=True)
    scene bg SchoolBathBlow09 with Dissolve(0.3)
    $ renpy.pause (0.1, hard=True)
    play sound Blow03 loop
    scene MeganBJVideo02
    with fade
    $ renpy.pause ()
    MG "{i}\"Bleurghch\"{/i}"
    $ renpy.pause ()
    MG "{i}\"Schhhhluurrrrp\"{/i}"
    $ renpy.pause ()
    menu:
        "Just the tip":
            jump megan_tip
        "Throat Fuck":
            jump megan_throat

label megan_cum:
    scene MeganBJVideo02
    with dissolve
    $ renpy.pause ()
    RT "{i}Oh my God, I'm gonna cum!{/i}"
    $ timeofdaycounter += 1
    RT "{i}Where should I do it?{/i}"
    menu:
        "Down Megan's throat":
            scene MeganBJVideo03
            with dissolve
            $ renpy.pause ()
            scene bg SchoolBathBlow13
            with fade
            stop sound fadeout 1.0
            $ renpy.pause ()
            R "Aaahhhh!!!..."
            play sound Ejaculate
            scene bg BlurryWhite
            with fade
            with vpunch
            with hpunch
            scene bg SchoolBathBlow14
            with fade
            MG "{i}\"Glurp.... glurp.... glurp.... \"{/i}"
            play sound Ejaculate
            scene bg BlurryWhite
            with fade
            with vpunch
            with hpunch
            scene bg SchoolBathBlow14
            with fade
            MG "{i}\"Glurp.... glurp.... glurp.... \"{/i}"
            play sound Ejaculate
            scene bg BlurryWhite
            with fade
            stop sound
            with vpunch
            with hpunch
            scene bg SchoolBathBlow15
            with fade
            MG "Oohh Mry Groshh!! Thrat wras sro mruch crumm!!"
            R "Oh my God!!.... My first blowjob!!.... That was incredible!!"
            MG "Hrahrahra.... wrell jrust remrembrer, there'rs mrore whrere thrat crame from irf ru lret mre mrodel fror ru."
            R "I think I'm sold."
            MG "Yray!!"
            MG "{i}\"Glurp.... glurp.... \"{/i}"
            play music Honey
            scene bg CityMap01
            with fade
            $ persistent.gal_other_girls_1 = True
            $ screen_on = "citymapmap"
            call screen citymapmap
        "All over her face":
            scene bg SchoolBathBlow13
            with fade
            stop sound fadeout 1.0
            $ renpy.pause ()
            R "Aaahhhh!!!..."
            scene bg BlurryWhite
            with fade
            with vpunch
            with hpunch
            play sound Ejaculate
            scene bg SchoolBathBlow16
            with fade
            MG "Wow, that was a lot of cum!"
            MG "Thank you for not getting it in my hair."
            R "Thank you for that, my first blowjob!!"
            MG "Hahaha.... don't mention it! And there's more where that came from if you'll let me model for you."
            R "I think I'm sold!"
            MG "Yay!!"
            play music Honey
            scene bg CityMap01
            with fade
            $ persistent.gal_other_girls_1 = True
            $ screen_on = "citymapmap"
            call screen citymapmap

##################  CLUB POOL  #############################################  CLUB POOL  ############################################  CLUB POOL  ###############################################  CLUB POOL  #######################################  CLUB POOL  #############################################################  CLUB POOL  ##########

label clubpool:
    if not bikini_show_seen:
        $ bikini_show_failed = True

    $ persistent.gal_mom_5 = True

    scene bg SleepBlack
    with fade
    $ renpy.pause (1.0)
    scene bg Pool01
    with fade
    $ firstclubvisit = True
    M "Ok, the rules are the same as always. Don't be an idiot and embarass me."
    M "Remember that the people here are unusually stuffy and stuck up, and they don't like to see horsing around."
    M "It looks like we dodged a bullet though, there's almost no one here, and definitely not anyone I know."
    R "What are you talking about, there's Lauren's friend Kenzie over there hanging out with Matt from our class."
    M "I meant I don't know anyone here that matters."
    R "Now you sound stuck up."
    M "Oh my God! You're right, I just get so worked up at this place."
    M "Ok, the most important thing is that you don't order anything to eat or drink. They might let us in here, but if we buy anything, our cards on file here will definitely get declined."
    M "That would kill me with embarrassment."
    M "Oh, God. What are you doing?.... Go change in the dressing room."
    scene bg Pool02
    with dissolve
    R "No need, I wore my swimsuit underneath my clothes."
    M "I'm just going to pretend I don't know you."
    scene bg Pool03
    with dissolve
    R "Wait!.... Mom!.... Over here!..."
    R "TAKE MY CLOTHES WITH YOU!..."
    M "..."
    M "Oh fine, just give my your goddamn clothes!"
    R "Language, Mom!"
    M "Urrrgghhh!"
    scene bg Pool04
    with dissolve
    $ renpy.pause ()
    play sound Splash
    scene bg Pool05
    with fade
    scene bg Pool05
    with dissolve
    R "Hey, what's up guys?"
    K "Oh, hey [ryan]."
    MB "Yo, what's up?"
    scene bg Pool06
    with dissolve
    R "So, where are your parents?"
    MB "Our Dads left us here while they go play a round of golf."
    MB "But I see you brought your gorgeous mom!"
    K "Oh Matt, would you stop perving on his mom?"
    scene bg Pool07
    with dissolve
    MB "What? You think she's ugly?"
    K "NO!.... I didn't say that.... she's a very beautiful woman, but..."
    MB "Kenzie.... you've got a thing for Miss [mom_name]?"
    K "Oh, shut up!"
    scene bg Pool06
    with dissolve
    MB "So, what's the deal? Is your mom going to come swim with us?"
    R "Yeah right, she usually just sits and reads a book, or sleeps in the shade."
    MB "Well, go talk her into swimming."
    MB "Tell her we want to play a pool game, but it will be more fun with more people."
    R "Why do you want my mom to play with us so bad?"
    MB "Well, can you think of a fun game to play with just three people?"
    R "Yeah, I guess you have a point."
    R "I'll go see what I can do."
    if chosebluebikini == True:
        scene bg PoolBlue08
        with fade
    else:
        scene bg PoolPink08
        with fade
    RT "{i}Yep, reading a book, just like always.{/i}"
    R "Hey, Mom!"
    M "Just a second, [ryan], let me finish my paragraph."
    R "..."
    if chosebluebikini == True:
        scene bg PoolBlue09
        with dissolve
    else:
        scene bg PoolPink09
        with dissolve
    M "Ok, what is it?"
    R "We were just wanting to play some pool games."
    M "Well, that's fine with me as long as you don't horse around too much..."
    M "Actually, what the heck.... horse around all you like, there's nobody here to complain."
    R "No.... Mom.... we want you to come play the pool games with us."
    M "Oh, no.... I'm very into this book, plus I don't think it would be in good decorum to be so informal with my students."
    R "Decor.... what?"
    M "Decorum honey, it means behaving in good taste."
    R "Hmmm.... I don't see what's wrong with it."
    M "Yes.... well.... some of your recent judgement hasn't been very good, has it?"
    R "What do you mean?"
    M "..."
    M "..."
    R "Ok, well maybe I've done some dumb things, but I've done a lot of good things for you too."
    M "That is true."
    M "I'll tell you what."
    M "Give me just 10 more minutes and I'll finish this chapter, and then if I'm feeling up to it, I'll come give you some attention."
    R "Ok, it's a deal."
    if chosebluebikini == True:
        scene bg PoolBlue08
        with dissolve
    else:
        scene bg PoolPink08
        with dissolve
    RT "..."
    RT "{i}If only I could get Mom some alcohol, she's always a lot more fun in social situations when she has a little liquid courage.{/i}"
    RT "{i}I can't order anything on credit, but I've got some cash in the wallet in my shorts, I wonder if they would accept cash here.{/i}"
    scene bg Pool10
    with fade
    R "Excuse me, miss?"
    scene bg Pool11
    with dissolve
    W "Yes, sir, what can I do for you?"
    R "How much is your wine?"
    W "Well, that depends on what kind of wine you order. And I would need to see some photo ID to prove you're over 21."
    R "No, it's not for me..."
    R "I want to buy it for my mom."
    R "Do you happen to know her? She's sitting right over there. Do you know what kind of wine she usually buys here?"
    W "Oh yes, she usually gets the Pinot Noir from our Oregon vineyard."
    R "Ok, I'd like to get her that."
    W "Ok, we'll just charge the card you have on file with us then?"
    R "Actually, can I pay in cash?"
    W "We don't usually allow that..."
    R "But it's a gift for my mother. I can't have her pay for her own gift."
    R "She's been going through some really hard things lately, and I just want to do something nice for her."
    W "Oh, that's sweet. I think we can make an exception this time."
    R "Awesome! How much do I owe you?"
    W "Do you want to buy her a glass of wine, or send her the whole bottle?"
    R "Well, what's the price difference?"
    W "By the glass it's $20, and by the bottle it's $100"
    R "Really? That's how much Mom usually spends on wine?"
    W "Haha, and that's not even close to our most expensive wine."
    R "Alright, I'll be right back, I just have to run and grab the cash out of my wallet."
    scene bg Pool12
    RT "{i}Umm.... ok, let me just think a second.{/i}"
    RT "{i}That's a lot of money for a little liquid refreshment,{/i}"
    RT "{i}But Mom really does loosen up with a few glasses of wine in her.{/i}"
    RT "{i}One glass might loosen her up a bit, but each glass she drinks after that might make her even more uninhibited.{/i}"
    menu:
        "Buy a Glass.":
            scene bg Pool13
            with dissolve
            R "I'll just get her a glass of wine."
            "{i}\"Money -$20\"{/i}"
            $ money -= 20
            W "Ok, I'll run and get her a glass and let her know it's from the gentleman in the blue swimsuit."
            RT "{i}Haha gentleman, yeah, that describes me pretty well.{/i}"
            R "Thank you!"
            W "You're very welcome."
            if chosebluebikini == True:
                scene bg PoolBlue14
                with fade
            else:
                scene bg PoolPink14
                with fade
        "Buy the Bottle." if money >= 100:
            scene bg Pool13
            with dissolve
            R "I'll get her the whole bottle."
            "{i}\"Money -$100\"{/i}"
            $ money -= 100
            $ boughtthebottle = True
            W "Ok, I'll run and get her a glass and let her know it's from the gentleman in the blue swimsuit."
            RT "{i}Haha gentleman, yeah, that describes me pretty well.{/i}"
            R "Thank you!"
            W "You're very welcome."
            if chosebluebikini == True:
                scene bg PoolBlue14
                with fade
            else:
                scene bg PoolPink14
                with fade

    MT "{i}Uuggh.... I am so sick of this Oedipus curriculum for my class. I can't wait until we get through the rest of this subject matter.{/i}"
    MT "{i}Fucking school board member Will Tylor. No wonder he demanded we study Oedipus Rex literature, his own textbook is part of the required reading.{/i}"
    MT "{i}It says here that \"Just like a child can get stuck in an oral phase if you take away their pacifier, or make them stop sucking their fingers before they are ready to give them up.{/i}"
    MT "{i}So too can a young man become stuck in an Oedipal phase if it isn't allowed to develop to a point.{/i}"
    MT "{i}Oh yeah, and what point is that Sigmund Freud? A titty fuck from his mom? Sounds like a bunch of bullshit to me.{/i}"
    MT "{i}At least I hope it's bullshit. [ryan] seems to be showing some signs of developing a little something.{/i}"
    if chosebluebikini == True:
        scene bg PoolBlue15
        with dissolve
    else:
        scene bg PoolPink15
        with dissolve
    W "Excuse me, ma'am."
    M "Yes?"
    M "Oh, no thank you.... I don't want to buy my usual wine."
    W "Oh, no.... well, I hope you at least want some, because it's already been paid for."
    M "What?!.... By whom?"
    if chosebluebikini == True:
        scene bg PoolBlue16
        with dissolve
    else:
        scene bg PoolPink16
        with dissolve
    W "Just a second, let me put down the wine so I can point him out."
    M "Him out? Well, that narrows it down to two, and neither of them are old enough to buy alcohol."
    W "Well, since it's not for them, and we try to treat members like gold..."
    W "There he is."
    scene bg Pool17
    with fade
    W "The one waving in the blue swimsuit."
    if boughtthebottle == True:
        M "Of course, buying me a $100 bottle of wine, something is definitely developing."
    else:
        M "Buying me a $20 glass of wine? How sweet!..."
    W "Excuse me?..."
    M "Oh, nothing, never mind.... thank you for your help.... I won't be needing anything else."
    if chosebluebikini == True:
        scene bg PoolBlue18
        with fade
    else:
        scene bg PoolPink18
        with fade
    MT "{i}Just look at that shit-eating grin on his face.{/i}"
    MT "{i}He's up to something.{/i}"
    if chosebluebikini == True:
        scene bg PoolBlue19
        with dissolve
    else:
        scene bg PoolPink19
        with dissolve
    MT "{i}Well, I guess I better get drinking.... It's already been opened and poured.... I'd hate for it to go to waste.{/i}"
    MT "{i}Is [ryan] buying me wine because he thinks it's something his father would do?....{/i}"
    if chosebluebikini == True:
        scene bg PoolBlue18
        with dissolve
    else:
        scene bg PoolPink18
        with dissolve
    MT "{i}Or is he really starting to enter an Oedipal phase? And if he is, will not allowing it to develop to a certain point really make him get stuck in it like the book said?{/i}"
    MT "{i}Shit, I hope that's bullshit!{/i}"
    MT "{i}He has really stepped up this last month though, I'm so relieved I haven't had to go back to the strip club in a while.{/i}"
    MT "{i}[ryan]'s kind of the only person watching out for me right now. No matter his motivation, I really owe him a lot.{/i}"
    if chosebluebikini == True:
        scene bg PoolBlue19
        with dissolve
    else:
        scene bg PoolPink19
        with dissolve
    MT "{i}I should just drink up and stop worrying about things, at least while I'm here.{/i}"
    MT "{i}I did bring [ryan] here to reward him, I should probably stop being so suspicious of him and just help him have a good time.{/i}"
    if chosebluebikini == True and boughtthebottle == True:
        scene bg PoolBlueWine20
        with fade
    elif chosebluebikini == True:
        scene bg PoolBlue20
        with fade
    elif boughtthebottle == True:
        scene bg PoolPinkWine20
        with fade
    else:
        scene bg PoolPink20
        with fade
    R "I hope the waitress was right. Is that the kind of wine you like?"
    M "Yes, honey. Thank you so much!"
    M "That was very thoughtful."
    if chosebluebikini == True and boughtthebottle == True:
        M "But where are you getting so much money from? First you pay off the Mafia debt all those weeks in a row, then you buy me a Hyongu bikini, and now a hundred dollar bottle of wine?"
        M "Please don't say I have to strip on Saturday because you're trying to spoil me now!"
        R "Don't worry, Mom, I'll keep paying that Mafia debt."
        "{i}{b}\"Mom's Affection +2\"{/b}{/i}"
        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
        $ momaffection += 2
        $ momsubmission += 1
        M "Maybe I should come work with you, you might be making more money than me, haha..."
        RT "{i}Hopefully someday you'll be working as a model for me in my photo studio.{/i}"
        RT "{i}I'd love to see you in one of Sidney's outfits!{/i}"
    elif chosebluebikini == True:
        M "But where are you getting so much money from? First you pay off the Mafia debt all those weeks in a row, then you buy me a Hyongu bikini, and now a twenty dollar glass of wine?"
        M "Please don't say I have to strip on Saturday because you're trying to spoil me now!"
        R "Don't worry, Mom, I'll keep paying that Mafia debt."
        "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
        $ momaffection += 1
        M "Maybe I should come work with you, you might be making more money than me, haha..."
        RT "{i}Hopefully someday you'll be working as a model for me in my photo studio.{/i}"
        RT "{i}I'd love to see you in one of Sidney's outfits!{/i}"
    elif boughtthebottle == True:
        M "But where are you getting so much money from? First you pay off the Mafia debt all those weeks in a row, and now a hundred dollar bottle of wine?"
        M "Please don't say I have to strip on Saturday because you're trying to spoil me now!"
        R "Don't worry, Mom, I'll keep paying that Mafia debt."
        "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
        $ momaffection += 1
        M "Maybe I should come work with you, you might be making more money than me, haha..."
        RT "{i}Hopefully someday you'll be working as a model for me in my photo studio.{/i}"
        RT "{i}I'd love to see you in one of Sidney's outfits!{/i}"
    else:
        M "But I know you don't have a ton of money lying around, you don't have to go spending it all on me."
    M "So, let me finish this wine, and I'll join you in the pool."
    R "Really?! That's awesome!"
    M "Yeah, give me just a second."
    if chosebluebikini == True and boughtthebottle == True:
        scene bg PoolBlueWine21
        with dissolve
        $ renpy.pause ()
        scene bg PoolBlueWine22
        with dissolve
        M "Okay, just a sec, I need another glass."
        scene bg PoolBlueWine20
        with dissolve
        $ renpy.pause ()
        scene bg PoolBlueWine21
        with dissolve
        $renpy.pause ()
        scene bg PoolBlueWine22
        with dissolve
        M "Ok, maybe just one more."
        scene bg PoolBlueWine20
        with dissolve
        $ renpy.pause ()
        scene bg PoolBlueWine21
        with dissolve
        $renpy.pause ()
        scene bg PoolBlueWine22
        with dissolve
        M "Okay, I think I'm ready."
        scene bg PoolBlue23
        with dissolve
    elif chosebluebikini == True:
        scene bg PoolBlue21
        with dissolve
        $ renpy.pause ()
        scene bg PoolBlue22
        with dissolve
        M "Okay, I think I'm ready."
        scene bg PoolBlue23
        with dissolve
    elif boughtthebottle == True:
        scene bg PoolPinkWine21
        with dissolve
        $ renpy.pause ()
        scene bg PoolPinkWine22
        with dissolve
        M "Okay, just a sec, I need another glass."
        scene bg PoolPinkWine20
        with dissolve
        $ renpy.pause ()
        scene bg PoolPinkWine21
        with dissolve
        $renpy.pause ()
        scene bg PoolPinkWine22
        with dissolve
        M "Ok, maybe just one more."
        scene bg PoolPinkWine20
        with dissolve
        $ renpy.pause ()
        scene bg PoolPinkWine21
        with dissolve
        $renpy.pause ()
        scene bg PoolPinkWine22
        with dissolve
        M "Okay, I think I'm ready."
        scene bg PoolPink23
        with dissolve
    else:
        scene bg PoolPink21
        with dissolve
        $ renpy.pause ()
        scene bg PoolPink22
        with dissolve
        M "Okay, I think I'm ready."
        scene bg PoolPink23
        with dissolve
    R "Mom, is it ok to swim after drinking?"
    M "Oh, don't worry, they say you shouldn't do a lot of things after drinking, yet people do."
    R "But that doesn't mean they're..."
    M "Shhhh..."
    if chosebluebikini == True and boughtthebottle == True:
        scene bg PoolBlueWine24
        with dissolve
        M "Don't be such a killjoy."
        R "Oh, wait! Mom!"
        R "You can't go swimming in those shorts!"
        M "What? Of course I can."
        R "No, you didn't bring any sunscreen, and if you swim with those shorts you'll get weird tan lines."
        M "Yeah, and what of it?"
        R "What if you have to go back and do a certain job?..."
        R "Those tan lines won't look very good, and Joey DeCapo might not be happy about it."
        M "What ever happened to \"Don't worry, Mom, I'll pay the Mafia debt\"?"
        R "Well, of course I'll keep trying, but what if I have an off week?"
        M "Shit! These bottoms are so revealing."
        M "But, I think you're right."
        scene bg PoolBlueWine25
        with dissolve
        M "Ok, try not to look too much."
    if chosebluebikini == True and boughtthebottle == False:
        scene bg PoolBlue24
        with dissolve
        M "Don't be such a killjoy."
        R "Oh, wait! Mom!"
        R "You can't go swimming in those shorts!"
        M "What? Of course I can."
        R "No, you didn't bring any sunscreen, and if you swim with those shorts you'll get weird tan lines."
        M "Yeah, and what of it?"
        R "What if you have to go back and do a certain job?..."
        R "Those tan lines won't look very good, and Joey DeCapo might not be happy about it."
        M "What ever happened to \"Don't worry, Mom, I'll pay the Mafia debt\"?"
        R "Well, of course I'll keep trying, but what if I have an off week?"
        M "Shit! These bottoms are so revealing."
        M "But, I think you're right."
        scene bg PoolBlue25
        with dissolve
        M "Ok, try not to look too much."
    if chosebluebikini == False:
        M "Don't be such a killjoy."
    else:
        pass
    M "And move over, I'm coming in!"
    if chosebluebikini == True:
        scene bg PoolBlue26
        with dissolve
    else:
        scene bg PoolPink26
        with dissolve
    play sound Splash
    scene bg SleepBlack
    with fade
    $ renpy.pause (0.5)
    if chosebluebikini == True:
        scene bg PoolBlue27
        with fade
        M "Oh, wow! That water is refreshing!"
        RT "{i}Oh my God! Mom's bikini is completely see-through when wet! She's going to want to kill me when she realizes, hopefully she just won't notice.{/i}"
        if boughtthebottle == False:
            M "Boys.... boys!..."
            scene bg PoolBlue28
            with dissolve
            M "My eyes are up here! Stop staring at my breasts! If there's going to be a problem, I'm going to leave."
            M "Are we going to have a problem?"
            "{i}{b}\"Mom's Anger +1\"{/b}{/i}"
            $ momanger += 1
            MB "No.... sorry! We'll behave!"
            R "No, I wasn't even looking at your.... I mean I was looking at.... something else."
            M "Well put!"
            scene bg PoolBlue29
            with dissolve
            M "Now, as I was saying..."
        else:
            MT "{i}Oh my God! Are these little horndogs staring at my breasts?{/i}"
            MT "{i}I'm not surprised about Matt, I know his reputation, and I've noticed the way he looks at me in class.{/i}"
            MT "{i}I wonder if the rumors about him and Miss Stone are true.... {/i}"
            MT "{i}But I can't believe [ryan] would be staring like that.... {/i}"
            MT "{i}Is he really developing an Oedipal complex?.... Why do I feel flattered?.... I think I drank too much wine.... {/i}"
            "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
            $ momlibido += 1
            MT "{i}Will trying to stamp it out really just make him get stuck in this phase like that textbook says?{/i}"
            scene bg PoolBlue31
            with dissolve
            MT "{i}I think maybe I just won't say anything.{/i}"

    else:
        scene bg PoolPink29
        with fade
    M "[ryan] was saying that you guys wanted to play some pool games?"
    MB "Yeah, let's play chicken!"
    M "Oh, no no, that one's a little too physical for me."
    M "Too easy to take advantage of the situation, if you know what I mean."
    RT "{i}She's probably played enough of those porn games I introduced her to, so she knows what we hope will happen in a chicken fight.{/i}"
    M "How about a game of Marco Polo."
    R "But that's a kiddy game!"
    MB "I think that's a great idea, Miss [mom_name]!"
    RT "{i}Ass kisser.{/i}"
    K "How do you play Marco Polo?"
    M "Whoever is it, has to close their eyes, and whenever they say \"Marco\", everyone in the pool has to say \"Polo\","
    M "And then the person who is it has to try to tag someone by only following the sound of their voice."
    M "And when they tag someone, they have to identify them by name. If they get it wrong then they are still it."
    R "Yeah, it's a kiddy game, let's do something else."
    K "I think that sounds like it could be fun."
    M "Alright, three of us to one of you [ryan], Marco Polo it is."
    MB "And I'll be it first."
    MB "I'll close my eyes and give you all a 10 second head start."
    MB "One..."
    if chosebluebikini == True:
        scene bg PoolBlue30
        with dissolve
    else:
        scene bg PoolPink30
        with dissolve
    MB "Two..."
    MB "Three..."
    scene bg SleepBlack
    with fade
    MB "Ten!.... Ready or not, here I come!"
    scene bg Pool32
    with fade
    MB "Marco!"
    scene bg Pool33
    with fade
    EBE "Polo!"
    MB "Marco!"
    EBE "Polo!"
    if chosebluebikini == True:
        scene bg PoolBlue34
        with fade
    else:
        scene bg PoolPink34
        with fade
    MB "Marco!"
    EBE "Polo!"
    MB "Marco!"
    EBE "Polo!"
    if chosebluebikini == True:
        scene bg PoolBlue35
        with fade
    else:
        scene bg PoolPink35
        with fade
    play music SexMusic
    MB "I've almost got someone!"
    MBT "{i}That's definitely Miss [mom_name]. a strong pull on that top should do the trick.{/i}"
    RT "{i}Is Matt going to do what I think he's doing?{/i}"
    RT "{i}I'd better get over there and help her.{/i}"
    MB "Is it.... miss [mom_name]?"
    "Pull.... yank..."
    if chosebluebikini == True:
        scene bg PoolBlue36
        with fade
    else:
        scene bg PoolPink36
        with fade
    MBT "{i}Yes, it worked!{/i}"
    MT "{i}Oh.... my.... God!.... {/i}"
    if chosebluebikini == True:
        scene bg PoolBlue37
        with dissolve
    else:
        scene bg PoolPink37
        with dissolve
    M "Gasp!.... OH MY GOD!!"
    M "[ryan]! What the hell are you doing?"
    R "What do you mean, what the hell am I doing?"
    R "Isn't it obvious?"
    R "I'm protecting your chastity!"
    M "By grabbing my breasts?!"
    R "No! By covering your breasts."
    R "You want the whole pool to see them?"
    if chosebluebikini == True:
        scene bg PoolBlue42
        with fade
    else:
        scene bg PoolPink42
        with fade
    RT "{i}Oh my God! I'm grabbing Mom's tits!!{/i}"
    if chosebluebikini == True:
        scene bg PoolBlue43
        with dissolve
    else:
        scene bg PoolPink43
        with dissolve
    RT "{i}Oh no! My swimsuit is shrinking!{/i}"
    if chosebluebikini == True:
        scene bg PoolBlue44
        with dissolve
    else:
        scene bg PoolPink44
        with dissolve
    RT "{i}I guess I should have expected this.{/i}"
    if chosebluebikini == True:
        scene bg PoolBlue37
        with fade
    else:
        scene bg PoolPink37
        with fade
    M "Why would you think that would be a good idea?"
    R "I'm sorry! I just could tell that Matt was about to rip your top off, so I reacted as quickly as I could."
    if boughtthebottle == True:
        R "I can see now that maybe that wasn't the best thing to do.... I'm so sorry!"
        if chosebluebikini == True:
            scene bg PoolBlue39
            with dissolve
        else:
            scene bg PoolPink39
            with dissolve
        M "Oh, honey! I'm sorry if I sounded mad..."
        M "It is so sweet the way you're always trying to protect me!"
        M "But this type of thing, I can do on my own."
        M "Now if you'll kindly close your eyes and remove your hands."
        if chosebluebikini == True:
            scene bg PoolBlue40
            with dissolve
        else:
            scene bg PoolPink40
            with dissolve
        M "Now Matt, would you please hand me my top?"
        M "And I'm going to assume that was an accident?"
        MB "Of course, Miss [mom_name]. My eyes were closed, I couldn't tell what I was grabbing for."
        M "Of course, that's what I suspected. I completely understand."
        M "Now, do you mind swimming away so I can get my top back on?"
        M "And [ryan] would you mind helping me make sure my top is fastened correctly?"
        if chosebluebikini == True:
            scene bg PoolBlue41
            with dissolve
        else:
            scene bg PoolPink41
            with dissolve
        R ".... Yeah!.... Of course!..."
        RT "{i}I can't believe she's not furious!{/i}"
        RT "{i}It must be all the wine.{/i}"
        R "There you go, nice and tight."
        M "Thanks, [ryan]!"
        M "Now I believe it's my turn to be \"it\" in Marco Polo. Matt correctly identified me when he grabbed my.... when he tagged me."
        R "Just a second, Mom, I need to have a quick word with Matt."
        M "Oh, [ryan] don't do anything stupid. It was just an accident!"
        R "Yeah, I intend to find that out."
    else:
        M "[ryan]! Don't be an idiot!"
        M "You don't have to protect me from everything!"
        if chosebluebikini == True:
            scene bg PoolBlue42
            with fade
        else:
            scene bg PoolPink42
            with fade
        RT "{i}Oh my God! I'm grabbing Mom's tits!!{/i}"
        if chosebluebikini == True:
            scene bg PoolBlue43
            with dissolve
        else:
            scene bg PoolPink43
            with dissolve
        RT "{i}Oh no! My swimsuit is shrinking!{/i}"
        if chosebluebikini == True:
            scene bg PoolBlue43
            with dissolve
        else:
            scene bg PoolPink43
            with dissolve
        RT "{i}I guess I should have expected this.{/i}"
        if chosebluebikini == True:
            scene bg PoolBlue37
            with fade
        else:
            scene bg PoolPink37
            with fade
        M "Now get your hands off my tits! I can cover them up myself."
        if chosebluebikini == True:
            scene bg PoolBlue38
            with fade
        else:
            scene bg PoolPink38
            with fade
        M "And you, Matt! You little pervert! Give me back my top."
        MB "I'm sorry Miss [mom_name]! I swear it was an accident. I had my eyes closed and couldn't see where I was grabbing."
        M "Yeah, well, I guess you're innocent until proven guilty, so let's just get on with the game."
        M "I believe it's my turn to be \"it\" in Marco Polo. Matt correctly identified me when he grabbed my.... when he tagged me."
        R "Just a second, Mom, I need to have a quick word with Matt."
        M "Oh, [ryan] don't do anything stupid. It was just an accident!"
    R "Yeah, I intend to find that out."
    play music Honey
    scene bg Pool42
    with fade
    R "Dude! I know you did that on purpose!"
    MB "Well, of course I did."
    MB "What? Don't tell me you didn't enjoy it."
    MB "I can tell you did by your flagpole standing at full attention."
    if ntrcontent == True:
        MB "Besides, I thought you wanted my help with all of this!"
        R "Yeah, well I've changed my mind. I can get Mom just fine on my own."
        if firstntrblowjob == True:
            MB "Yeah? Well, it's a little too late to be changing your mind now! I already let Megan suck your dick, and I'm going after your mom until I get repayment in kind."
        else:
            MB "Yeah? Well, a deal's a deal, and I'm not backing off until I get what I'm after."
            MB "So, you better protect your shit, cuz I'm coming for it."
        MT "{i}Look at them arguing over there. I'm pretty sure Matt did pull off my top on purpose.{/i}"
        MT "{i}That's pretty flattering that a stud as young as him would want to see my tits.{/i}"
        MT "{i}Too bad [ryan] never gave him a chance to see them.{/i}"
        MT "{i}I wonder what he's packing underneath those trunks.{/i}"
        "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
        $ momlibido += 1
        MT "{i}Shit, [mom_name]! Pull yourself together! You can't think about one of your students like that!{/i}"
        scene bg Pool43
        with dissolve
        RT "{i}Shit!! Matt's gonna come after Mom hard.{/i}"
        RT "{i}And that fucker has game.{/i}"
        RT "{i}How am I going to protect her from him?{/i}"
    else:
        R "I told you in the class room to fuck off, I can handle this myself!"
        R "I know you get a kick out of conquering the teachers at school, but I'm warning you, stay away from my mom!"
        MB "Yeah, and what are you going to do about it?"
        R "I might just come after something you love!"
        MB "Oh, you've got me shaking now!"
        MT "{i}Look at [ryan] over there defending my honor.{/i}"
        MT "{i}He's really the only man in my life right now who would do something like that for me.{/i}"
        MT "{i}With [dad_name] out of the picture, I'm actually really happy that [ryan] has stepped up to fill his role in some ways.{/i}"
        MT "{i}There's some roles of [dad_name]'s that [ryan] can't fill though.{/i}"
        MT "{i}And I'm starting to really need that kind of attention!{/i}"
        MT "{i}I can't believe how much bigger [ryan] is than [dad_name]!{/i}"
        MT "{i}Haha, [dad_name] would be so jealous to know!{/i}"
        MT "{i}Shit!!.... I'm thinking about [ryan]'s penis again!{/i}"
    K "Have you ladies finished your chatting over there?! My bikini is going out of style! Let's keep playing!"
    M "Kenzie's right, it's my turn to chase you all."
    M "I'm counting to 10."
    M "1..."
    M "2..."
    scene bg SleepBlack
    with fade
    $ renpy.pause (0.5)
    if chosebluebikini == True:
        scene bg PoolBlue45
        with fade
    else:
        scene bg PoolPink45
        with fade
    M "9..."
    M "10..."
    M "Marco!"
    EBE "Polo!"
    if chosebluebikini == True:
        scene bg PoolBlue46
        with fade
    else:
        scene bg PoolPink46
        with fade
    M "Marco!"
    EBE "Polo!"
    MT "{i}Hmmm.... who should I go for?{/i}"
    menu:
        "[ryan]":
            MT "{i}I'll go for [ryan], hopefully it will make his day more fun!{/i}"
            if chosebluebikini == True:
                scene bg PoolBlue49
                with fade
            else:
                scene bg PoolPink49
                with fade
            M "Marco!"
            EBE "Polo!"
            RT "{i}Holy shit!{/i}"
            RT "{i}Mom's a fast swimmer.{/i}"
            if chosebluebikini == True:
                scene bg PoolBlue52
                with fade
            else:
                scene bg PoolPink52
                with fade
            M "Marco"
            EBE "Polo!"
            play music SexMusic
            MT "{i}Ha! I've almost got someone, but I'm not positive it's [ryan].{/i}"
            RT "{i}Damn she's almost got me. Maybe I'd better start doing yoga too.{/i}"
            scene bg Pool53
            with fade
            MT "{i}Just a little bit farther.... {/i}"
            scene bg Pool54
            with dissolve
            M "Gotcha!..."
            M "But who are you?"
            scene bg Pool55
            with dissolve
            MT "{i}I thought I was chasing [ryan], but this feels more like one of Kenzie's small wrists.{/i}"
            scene bg Pool54
            with dissolve
            $ renpy.pause (0.03)
            scene bg Pool55
            with dissolve
            $ renpy.pause (0.03)
            scene bg Pool54
            with dissolve
            $ renpy.pause (0.03)
            scene bg Pool55
            with dissolve
            $ renpy.pause (0.03)
            MT "{i}Who the hell is this?{/i}"
            scene bg Pool56
            with fade
            RT "{i}Oh my God, oh my God, oh my God!!!.... Does Mom know she's jacking me off?{/i}"
            scene bg Pool54
            with fade
            $ renpy.pause (0.03)
            scene bg Pool55
            with dissolve
            $ renpy.pause (0.03)
            scene bg Pool54
            with dissolve
            $ renpy.pause (0.03)
            scene bg Pool55
            with dissolve
            $ renpy.pause (0.03)
            if boughtthebottle == True:
                MT "{i}Hmmmm.... I really think this must be Kenzie, but I know I heard her voice on the other side of the pool.{/i}"
                scene bg Pool54
                with dissolve
                $ renpy.pause (0.03)
                scene bg Pool55
                with dissolve
                $ renpy.pause (0.03)
                scene bg Pool54
                with dissolve
                $ renpy.pause (0.03)
                scene bg Pool55
                with dissolve
                $ renpy.pause (0.03)
                scene bg Pool59
                with fade
                RT "{i}Oh, shit!!!.... I can't hold back any more!{/i}"
                R "Hnnnngggghhhh!!"
                scene bg Pool57
                with fade
                with vpunch
                with hpunch
                play sound Ejaculate
                RT "{i}Holy fucking shit!!.... Mom just made me splooge in the pool!!{/i}"
                M "Ok, I'm guessing I've caught Kenzie!"
                stop music
                scene bg SleepBlack
                with fade
                play sound Scratch
                if chosebluebikini == True:
                    scene bg PoolBlue58
                    with fade
                else:
                    scene bg PoolPink58
                    with fade
                play music Honey
                M "Oh my God, [ryan]!"
                M "Was I grabbing?.... Did you just?.... Why didn't you?..."
                M "Oh my God, [ryan]!!"
                R "I'm sorry!.... You just grabbed it and started pulling.... I was hoping you would just let go without opening your eyes."
                R "But you just kept pulling!"
                R "I didn't know what to do..."
                M "Ok just shhh..."
                R "I'm sorry!..."
                M "It's ok, just keep it down..."
                if chosebluebikini == True:
                    scene bg PoolBlue73
                    with fade
                else:
                    scene bg PoolPink73
                    with fade
                M "{i}(whispering){/i} We don't want everyone in the pool to hear what happened. Hopefully they didn't notice."
                RT "{i}Yeah right, fat chance of that.{/i}"
                M "I'm not mad. Accidents happen."
                M "But let's just get our stuff and hurry out to the car."
                MT "{i}Oh my God! If that didn't let his Oedipal phase develop, I don't know what will.{/i}"
                MT "{i}I just made my own son blow his load!{/i}"
                MT "{i}Shit, [mom_name]!.... Stop thinking about your son's huge pulsing cock!{/i}"
                "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                $ momlibido += 1
                MT "{i}We've got to get out of here.{/i}"
                scene bg SleepBlack
                with fade
                $ timeofdaycounter = 4
                jump myroom
            else:
                M "Ok, I'm guessing I've caught Kenzie!"
                stop music
                scene bg SleepBlack
                with fade
                play sound Scratch
                if chosebluebikini == True:
                    scene bg PoolBlue58
                    with fade
                else:
                    scene bg PoolPink58
                    with fade
                play music Honey
                M "Oh my God, [ryan]!"
                M "Was I grabbing?.... Why didn't you say something?..."
                M "Oh my God, [ryan]!!"
                R "I'm sorry!.... You just grabbed it and started pulling.... I was hoping you would just let go without opening your eyes."
                R "I thought if I could get away you wouldn't realize what you had grabbed!"
                M "But why was it out?!..."
                R "It doesn't fit in my shorts when I'm hard..."
                R "And I've been hard ever since I grabbed your boobs."
                M "Oh my God, [ryan]!"
                if chosebluebikini == True:
                    scene bg PoolBlue74
                    with fade
                else:
                    scene bg PoolPink74
                    with fade
                M "{i}(whispering){/i} We don't want everyone in the pool to hear what happened. Hopefully they didn't notice."
                RT "{i}Yeah right, fat chance of that.{/i}"
                M "I've never been so embarrassed."
                "{i}\"Mom's Respect -1\"{/i}"
                $ momrespect -= 1
                M "Let's just get our stuff and hurry out to the car."
                MT "{i}Oh my God! If that didn't let his Oedipal phase develop, I don't know what will.{/i}"
                MT "{i}I was just jacking off my son's huge cock!{/i}"
                MT "{i}Shit, [mom_name]!.... Stop thinking about your son's huge pulsing cock!{/i}"
                "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                $ momlibido += 1
                MT "{i}We've got to get out of here.{/i}"
                scene bg SleepBlack
                with fade
                $ timeofdaycounter = 4
                jump myroom
        "Kenzie":
            MT "{i}I'll go for Kenzie, she should be easy to catch, and the sooner this game's done, the sooner we can go home!{/i}"
            if chosebluebikini == True:
                scene bg PoolBlue47
                with fade
            else:
                scene bg PoolPink47
                with fade
            M "Marco!"
            EBE "Polo!"
            MT "{i}I think I can hear Kenzie just ahead.{/i}"
            if chosebluebikini == True:
                scene bg PoolBlue50
                with fade
            else:
                scene bg PoolPink50
                with fade
            M "Marco"
            EBE "Polo!"
            play music SexMusic
            MT "{i}Ha! I've almost got someone, but I'm not positive it's Kenzie.{/i}"
            scene bg Pool61
            with fade
            MT "{i}Just a little bit farther.... {/i}"
            scene bg Pool62
            with dissolve
            M "Gotcha!..."
            M "But who are you?"
            scene bg Pool63
            with dissolve
            MT "{i}I thought I was chasing Kenzie, but I'm really not sure what I'm grabbing.{/i}"
            scene bg Pool62
            with dissolve
            $ renpy.pause (0.03)
            scene bg Pool63
            with dissolve
            $ renpy.pause (0.03)
            scene bg Pool62
            with dissolve
            $ renpy.pause (0.03)
            scene bg Pool63
            with dissolve
            $ renpy.pause (0.03)
            MT "{i}Who the hell is this?{/i}"
            if chosebluebikini == True:
                scene bg PoolBlue64
                with fade
            else:
                scene bg PoolPink64
                with fade
            KT "{i}Oh my God, oh my God, oh my God!!!.... Does Miss [mom_name] know she's groping my coochie and ass?!{/i}"
            scene bg Pool62
            with fade
            $ renpy.pause (0.03)
            scene bg Pool63
            with dissolve
            $ renpy.pause (0.03)
            scene bg Pool62
            with dissolve
            $ renpy.pause (0.03)
            scene bg Pool63
            with dissolve
            $ renpy.pause (0.03)
            if boughtthebottle == True:
                MT "{i}Hmmmm.... I'm not positive this is Kenzie, but I'm pretty sure. I'm just not sure what I'm feeling here.{/i}"
                scene bg Pool62
                with dissolve
                $ renpy.pause (0.03)
                scene bg Pool63
                with dissolve
                $ renpy.pause (0.03)
                scene bg Pool62
                with dissolve
                $ renpy.pause (0.03)
                scene bg Pool63
                with dissolve
                $ renpy.pause (0.03)
                if chosebluebikini == True:
                    scene bg PoolBlue65
                    with fade
                else:
                    scene bg PoolPink65
                    with fade
                KT "{i}Oh, shit!!!.... What do I do? I'd just swim away, but she's holding on tight.{/i}"
                KT "{i}But why oh why is it kinda turning me on to have my teacher groping my goodies?{/i}"
                scene bg Pool62
                with fade
                $ renpy.pause (0.03)
                scene bg Pool63
                with dissolve
                $ renpy.pause (0.03)
                scene bg Pool62
                with dissolve
                $ renpy.pause (0.03)
                scene bg Pool63
                with dissolve
                $ renpy.pause (0.03)
                KT "{i}I can't get away! Shit, I guess it's time to say something.{/i}"
                K "Ummmm.... miss [mom_name]!"
                stop music
                scene bg SleepBlack
                with fade
                play sound Scratch
                if chosebluebikini == True:
                    scene bg PoolBlue66
                    with fade
                else:
                    scene bg PoolPink66
                    with fade
                play music Honey
                M "Oh my God, Kenzie!"
                M "Was I grabbing?.... Why didn't you?..."
                M "Oh my God, Kenzie! I'm so so sorry!"
                K "I'm sorry!.... You just grabbed and started groping.... I was hoping you would just let go without opening your eyes."
                K "But you just kept groping!"
                K "I didn't know what to do..."
                M "Ok just shhh..."
                K "I'm sorry!..."
                M "It's ok, just keep it down..."
                M "Please don't say anything to anybody, especially Lauren."
                K "Ok, I promise."
                if chosebluebikini == True:
                    scene bg PoolBlue73
                    with fade
                else:
                    scene bg PoolPink73
                    with fade
                M "{i}(whispering){/i} Could you tell what just happened?"
                R "What do you mean? Did you get Kenzie? Is she it now?"
                RT "{i}Hahah.... I saw exactly what happened.{/i}"
                R "Or did you guess wrong. Are you coming after me next?"
                RT "{i}Why doesn't she seem more upset?{/i}"
                RT "{i}Maybe it's the alcohol.{/i}"
                M "No. I can't tell you what happened, but you'd probably die laughing if you saw..."
                R "What?"
                M "No.... sorry.... I can't tell you."
                RT "{i}Mom is a lot more fun when she's drunk.{/i}"
                M "Let's just say, it might be a little awkward for Kenzie to visit Lauren in the future.... hahah..."
                MT "{i}I can't believe I was groping her tight little pussy and ass like that.{/i}"
                MT "{i}And she just let it happen.... didn't say a word for a long time.... did she like it?.... {/i}"
                "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                $ momlibido += 1
                M "Come on [ryan], we've got to grab our stuff and get out of here."
                R "What!?.... Why?.... What happened?..."
                M "Just shut up and come on!"
                scene bg SleepBlack
                with fade
                $ timeofdaycounter = 4
                jump myroom
            else:
                M "Ok, I'm guessing I've caught Kenzie!"
                stop music
                scene bg SleepBlack
                with fade
                play sound Scratch
                if chosebluebikini == True:
                    scene bg PoolBlue66
                    with fade
                else:
                    scene bg PoolPink66
                    with fade
                play music Honey
                M "Oh my God, Kenzie!"
                M "Was I grabbing?.... Why didn't you?..."
                M "Oh my God, Kenzie! I'm so so sorry!"
                K "I'm sorry!.... You just grabbed and started groping.... I was hoping you would just let go without opening your eyes."
                K "But you just kept groping!"
                K "I didn't know what to do..."
                M "Ok just shhh..."
                K "I'm sorry!..."
                M "It's ok, just keep it down..."
                M "Please don't say anything to anybody, especially Lauren."
                K "Ok, I promise."
                if chosebluebikini == True:
                    scene bg PoolBlue74
                    with fade
                else:
                    scene bg PoolPink74
                    with fade
                M "{i}(whispering){/i} Could you tell what just happened?"
                R "What do you mean? Did you get Kenzie? Is she it now?"
                RT "{i}Hahah.... I saw exactly what happened.{/i}"
                R "Or did you guess wrong. Are you coming after me next?"
                RT "{i}She looks kind of upset?{/i}"
                M "No. Nothing happened, just forget I asked..."
                R "What?"
                M "No.... sorry.... I can't tell you."
                RT "{i}She looks really embarrassed.{/i}"
                MT "{i}I can't believe I was groping her tight little pussy and ass like that.{/i}"
                "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                $ momlibido += 1
                M "Come on [ryan], we've got to grab our stuff and get out of here."
                R "What!?.... Why?.... What happened?..."
                M "Just shut up and come on!"
                scene bg SleepBlack
                with fade
                $ timeofdaycounter = 4
                jump myroom
        "Matt" if ntrcontent == True:
            MT "{i}I'll go for Matt, maybe I can get some revenge for him stripping my top off!{/i}"
            if chosebluebikini == True:
                scene bg PoolBlue48
                with fade
            else:
                scene bg PoolPink48
                with fade
            M "Marco!"
            EBE "Polo!"
            MT "{i}I think that's Matt just ahead!{/i}"
            if chosebluebikini == True:
                scene bg PoolBlue51
                with fade
            else:
                scene bg PoolPink51
                with fade
            M "Marco"
            EBE "Polo!"
            play music SexMusic
            MT "{i}Ha! I've almost got Matt, the star of the basketball team. Is he even trying to get away from me?{/i}"
            MBT "{i}Alright, she's getting closer. Now to see if I can make this happen just right.{/i}"
            scene bg Pool67
            with dissolve
            M "Gotcha!..."
            M "But what do I have?"
            scene bg Pool68
            with dissolve
            MT "{i}I thought I was chasing Matt, but this feels more like one of [ryan]'s wrists.{/i}"
            scene bg Pool67
            with dissolve
            $ renpy.pause (0.03)
            scene bg Pool68
            with dissolve
            $ renpy.pause (0.03)
            scene bg Pool67
            with dissolve
            $ renpy.pause (0.03)
            scene bg Pool68
            with dissolve
            $ renpy.pause (0.03)
            MT "{i}Who the hell is this?{/i}"
            scene bg Pool69
            with fade
            MBT "{i}Oh my God, oh my God, oh my God!!!.... Does Miss [mom_name] know she's jacking me off?{/i}"
            scene bg Pool67
            with fade
            $ renpy.pause (0.03)
            scene bg Pool68
            with dissolve
            $ renpy.pause (0.03)
            scene bg Pool67
            with dissolve
            $ renpy.pause (0.03)
            scene bg Pool68
            with dissolve
            $ renpy.pause (0.03)
            if boughtthebottle == True:
                MT "{i}Hmmmm.... I really think this must be [ryan], but I thought I heard his voice on the other side of the pool.{/i}"
                scene bg Pool67
                with dissolve
                $ renpy.pause (0.03)
                scene bg Pool68
                with dissolve
                $ renpy.pause (0.03)
                scene bg Pool67
                with dissolve
                $ renpy.pause (0.03)
                scene bg Pool68
                with dissolve
                $ renpy.pause (0.03)
                scene bg Pool70
                with fade
                MBT "{i}Oh, shit!!!.... I can't hold back any more!{/i}"
                MB "Hnnnngggghhhh!!"
                scene bg Pool71
                with fade
                with vpunch
                with hpunch
                play sound Ejaculate
                MBT "{i}Holy fucking shit!!.... Miss [mom_name] just made me splooge in the pool!!{/i}"
                RT "Mom!.... Stop.... open your eyes!"
                M "Ok, I'm guessing I've caught [ryan]!"
                stop music
                scene bg SleepBlack
                with fade
                play sound Scratch
                if chosebluebikini == True:
                    scene bg PoolBlue72
                    with fade
                else:
                    scene bg PoolPink72
                    with fade
                play music Honey
                M "Oh my God, Matt!"
                M "Was I grabbing?.... Did you just?.... Why didn't you?..."
                M "Oh my God, Matt!!"
                MB "I'm sorry!.... You just grabbed it and started pulling.... I was hoping you would just let go without opening your eyes."
                MB "But you just kept pulling!"
                MB "I didn't know what to do..."
                M "Ok just shhh..."
                MB "I'm sorry!..."
                M "It's ok, just keep it down..."
                M "And please don't tell anyone what happened. Especially your parents."
                if chosebluebikini == True:
                    scene bg PoolBlue73
                    with fade
                else:
                    scene bg PoolPink73
                    with fade
                M "{i}(whispering){/i} Could you tell what just happened?"
                R "Yeah.... It was pretty obvious by the look on Matt's face!"
                MT "{i}Hahah.... I wish I had seen his face!{/i}"
                R "How could you not tell you had a grip on his cock?"
                M "Language, [ryan]! I thought I had you by the wrist."
                R "Me?.... By the wrist?.... Is Matt that big?"
                M "Oh.... yeah.... and I thought you were big."
                R "What?"
                M "I mean.... oh heck.... I'm sorry to compare you to him."
                RT "{i}Mom is kind of a floozy when she's drunk. I can't believe Matt already got the best of me! I've got to bring it to him hard!{/i}"
                M "Let's just say, I think he will have to find more experienced women, or he might just split them in half!"
                R "Mom!.... That's not any better!"
                MT "{i}And he just let it happen.... didn't say a word for a long time.... oh, I wish I'd seen his face.... {/i}"
                "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                $ momlibido += 1
                M "Come on [ryan], we've got to grab our stuff and get out of here."
                R "What!?.... Why?..."
                M "Just shut up and come on!"
                scene bg SleepBlack
                with fade
                $ timeofdaycounter = 4
                jump myroom
            else:
                R "Mom!.... Stop.... open your eyes!"
                M "Ok, I'm guessing I've caught [ryan]!"
                stop music
                scene bg SleepBlack
                with fade
                play sound Scratch
                if chosebluebikini == True:
                    scene bg PoolBlue72
                    with fade
                else:
                    scene bg PoolPink72
                    with fade
                play music Honey
                M "Oh my God, Matt."
                M "Was I grabbing?.... Why didn't you say something?..."
                M "Oh my God, Matt!!"
                MB "I'm sorry!.... You just grabbed it and started pulling.... I was hoping you would just let go without opening your eyes."
                MB "I thought if I could get away you wouldn't realize what you had grabbed!"
                M "But why was it out?!..."
                MB "It doesn't fit in my shorts when I'm hard..."
                MB "And I've been hard ever since I pulled your top off by accident."
                MT "{i}Pshhh.... accident my ass.{/i}"
                M "Oh my God, Matt!"
                M "Don't you dare say a word to anyone! Especially your parents!"
                if chosebluebikini == True:
                    scene bg PoolBlue74
                    with fade
                else:
                    scene bg PoolPink74
                    with fade
                M "{i}(whispering){/i} Could you tell what just happened?"
                R "Yeah.... It was pretty obvious by the look on Matt's face!"
                MT "Oh, God! I'm so humiliated!"
                R "How could you not tell you had a grip on his cock?"
                M "Language, [ryan]! I thought I had you by the wrist."
                R "Me?.... By the wrist?.... Is Matt that big?"
                M "Sshhhhh.... I don't want anyone to know what we're talking about!"
                R "What?"
                M "I mean.... oh heck.... I'm sorry to make you feel inadequate."
                MT "{i}Matt just let it happen.... didn't say a word for a long time.... would he have ever stopped me, or let me make him cum?.... {/i}"
                "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                $ momlibido += 1
                M "Come on [ryan], we've got to grab our stuff and get out of here."
                R "What!?.... Why?..."
                M "Just shut up and come on!"
                scene bg SleepBlack
                with fade
                $ timeofdaycounter = 4
                jump myroom

##################  WAREHOUSE  #############################################  WAREHOUSE  ###########################################wAREHOUSE######################################################  WAREHOUSE  #######################################  WAREHOUSE  ############################################  WAREHOUSE  #

label photostudio:
    if ready_for_hp:
        scene bg PStudioHP
        with fade
        $ screen_on = "pstudiohpmap"
        call screen pstudiohpmap
    if progress >= 14 and inventory.inv_amount(green_screen) == 1 and inventory.inv_amount(pro_lights) == 1:
        scene bg PStudioWR
        with fade
        $ screen_on = "pstudiowrmap"
        call screen pstudiowrmap
    elif inventory.inv_amount(green_screen) == 1 and inventory.inv_amount(pro_lights) == 1:
        scene bg PStudioGScreenLights
        with fade
        $ screen_on = "pstudiogscreenlightsmap"
        call screen pstudiogscreenlightsmap
    elif inventory.inv_amount(green_screen) == 1 and progress >= 14:
        scene bg PStudioGScreen
        with fade
        "{i}\"You will not have the option to start the Sidney photo-shoot until you have bought both the green screen and the professional lights.\"{/i}"
        $ screen_on = "pstudiogscreenmap"
        call screen pstudiogscreenmap
    elif inventory.inv_amount(green_screen) == 1:
        scene bg PStudioGScreen
        with fade
        $ screen_on = "pstudiogscreenmap"
        call screen pstudiogscreenmap
    elif inventory.inv_amount(pro_lights) == 1 and progress >= 14:
        scene bg PStudioLights
        with fade
        "{i}\"You will not have the option to start the Sidney photo-shoot until you have bought both the green screen and the professional lights.\"{/i}"
        $ screen_on = "pstudiolightsmap"
        call screen pstudiolightsmap
    elif inventory.inv_amount(pro_lights) == 1:
        scene bg PStudioLights
        with fade
        $ screen_on = "pstudiolightsmap"
        call screen pstudiolightsmap
    elif progress >= 14:
        scene bg PStudioEmpty
        with fade
        "{i}\"You will not have the option to start the Sidney photo-shoot until you have bought both the green screen and the professional lights.\"{/i}"
        $ screen_on = "pstudioemptymap"
        call screen pstudioemptymap
    else:
        scene bg PStudioEmpty
        with fade
        $ screen_on = "pstudioemptymap"
        call screen pstudioemptymap

label htbydshoot:

    if inventory.inv_amount(green_screen) == 1 and inventory.inv_amount(pro_lights) == 1 and timeofdaycounter != 2:
        scene bg PStudioGScreenLights
        "Lauren is only available to take pictures in the late morning."
        jump photostudio
    elif inventory.inv_amount(green_screen) == 1 and timeofdaycounter != 2:
        scene bg PStudioGScreen
        "Lauren is only available to take pictures in the late morning."
        jump photostudio
    elif inventory.inv_amount(pro_lights) == 1 and timeofdaycounter != 2:
        scene bg PStudioLights
        "Lauren is only available to take pictures in the late morning."
        jump photostudio
    elif timeofdaycounter != 2:
        scene bg PStudioEmpty
        "Lauren is only available to take pictures in the late morning."
        jump photostudio
    elif inventory.inv_amount(green_screen) == 1 and inventory.inv_amount(pro_lights) == 1 and finished_htbyd_shoot:
        scene bg PStudioGScreenLights
        "You have completed this photo session with Lauren entirely."
        "You can still play through the event, but you will not be able to increase Lauren's stats, or be able to generate any more likes for the Cosplay Heaven website."
    elif inventory.inv_amount(green_screen) == 1 and finished_htbyd_shoot:
        scene bg PStudioGScreen
        "You have completed this photo session with Lauren entirely."
        "You can still play through the event, but you will not be able to increase Lauren's stats, or be able to generate any more likes for the Cosplay Heaven website."
    elif inventory.inv_amount(green_screen) == 1 and inventory.inv_amount(pro_lights) == 1 and weekly_htbyd_complete:
        scene bg PStudioGScreenLights
        "You have already done this photo session with Lauren this week."
        "You will still be able to increase Lauren's stats and progress through this scene,"
        "But only the first playthrough of this event each week will generate likes for the Cosplay Heaven website."
    elif inventory.inv_amount(green_screen) == 1 and weekly_htbyd_complete:
        scene bg PStudioGScreen
        "You have already done this photo session with Lauren this week."
        "You will still be able to increase Lauren's stats and progress through this scene,"
        "But only the first playthrough of this event each week will generate likes for the Cosplay Heaven website."
    elif inventory.inv_amount(pro_lights) == 1 and weekly_htbyd_complete:
        scene bg PStudioLights
        "You have already done this photo session with Lauren this week."
        "You will still be able to increase Lauren's stats and progress through this scene,"
        "But only the first playthrough of this event each week will generate likes for the Cosplay Heaven website."
    elif weekly_htbyd_complete:
        scene bg PStudioEmpty
        "You have already done this photo session with Lauren this week."
        "You will still be able to increase Lauren's stats and progress through this scene,"
        "But only the first playthrough of this event each week will generate likes for the Cosplay Heaven website."
    else:
        pass

    scene bg PhotoStudio01
    show screen Points_screen_Lauren_cosplay
    with fade
    R "Yeah.... I'm already over here."
    "..."
    R "No.... I said I'm already here, I'm not coming to get you."
    "..."
    R "Just ride your bike, it's not that far."
    "..."
    R "Yeah and bring your cosplay costume."
    "..."
    R "No, I'm sure you can fit it in your backpack."
    "..."
    R "Ok, I'll get the studio ready while I'm waiting for you."
    scene bg SleepBlack
    with fade
    if inventory.inv_amount(pro_lights) == 1 and lightscomment == False and inventory.inv_amount(green_screen) == 0:
        scene bg PhotoStudio03
        with fade
        L "Wow! These are some professional looking lights! Were they expensive?"
        R "Of course, but it will be worth the investment with the quality of pictures we'll get out of them."
        $ lightscomment = True
        scene bg PhotoStudio04
        with dissolve
    elif inventory.inv_amount(pro_lights) == 1 and lightscomment == True and inventory.inv_amount(green_screen) == 0:
        scene bg PhotoStudio04
        with fade
    elif inventory.inv_amount(green_screen) == 1 and gscomment == False and inventory.inv_amount(pro_lights) == 0:
        scene bg PhotoStudio05
        with fade
        L "Nice background! But why is it green?"
        R "It will make it so we can add any background we want to the pictures later."
        R "I've been playing with the ZAD 3D computer program, and I should be able to do a lot of fun effects with the pictures we take."
        L "Awesome, I can't wait to see them!"
        $ gscomment = True
        scene bg PhotoStudio06
        with dissolve
    elif inventory.inv_amount(green_screen) == 1 and gscomment == True and inventory.inv_amount(pro_lights) == 0:
        scene bg PhotoStudio06
        with fade
    elif inventory.inv_amount(pro_lights) == 1 and inventory.inv_amount(green_screen) == 1 and lightscomment == True and gscomment == False:
        scene bg PhotoStudio07
        with fade
        L "Oh Nice! You've added a background as well, but why green?"
        R "It will make it so we can add any background we want to the pictures later."
        R "I've been playing with the ZAD 3D computer program, and I should be able to do a lot of fun effects with the pictures we take."
        L "Awesome, I can't wait to see them!"
        $ gscomment = True
        scene bg PhotoStudio08
        with dissolve
    elif inventory.inv_amount(pro_lights) == 1 and inventory.inv_amount(green_screen) == 1 and lightscomment == False and gscomment == True:
        scene bg PhotoStudio07
        with fade
        L "Oh, wow! You've added some really professional looking lights as well! Were they expensive?"
        R "Of course, but it will be worth the investment with the quality of pictures we'll get out of them."
        $ lightscomment = True
        scene bg PhotoStudio08
        with dissolve
    elif inventory.inv_amount(pro_lights) == 1 and inventory.inv_amount(green_screen) == 1 and lightscomment == False and gscomment == False:
        scene bg PhotoStudio07
        with fade
        L "Oh my gosh! You've upgraded the place! New professional looking lights, and a background that's green for some reason."
        R "The green screen will make it so we can add any background we want to the pictures later."
        R "I've been playing with the ZAD 3D computer program, and I should be able to do a lot of fun effects with the pictures we take."
        R "The lights will just make the quality of the pictures so much better. They will definitely be worth every penny we paid for them."
        L "Awesome! I can't wait the see how the pictures turn out."
        $ lightscomment = True
        $ gscomment = True
        scene bg PhotoStudio08
        with dissolve
    elif inventory.inv_amount(pro_lights) == 1 and inventory.inv_amount(green_screen) == 1 and lightscomment == True and gscomment == True:
        scene bg PhotoStudio08
        with fade
    else:
        scene bg PhotoStudio02
        with dissolve
    R "So, are you ready to get going?"
    L "So ready!"
    R "Ok, just run to the supply closet and get changed into your costume while I get a few more small details ready for the shoot."
    scene bg SleepBlack
    with fade
    $ days_until_next_photo_shoot = 0
    if inventory.inv_amount(green_screen) == 1:
        scene bg HTBYD_GS_01
        with fade
    else:
        scene bg HTBYD_E_01
        with fade
    L "Ok, I'm dressed, but I'm a little nervous about the shoot."
    $ weekly_htbyd_trigger = True
    $ htbyd_most_recent = True
    $ wr_most_recent = False
    if first_htbyd_shoot == True:
        R "Ok Lauren, I know this is only the second photoshoot you've ever done."
        $ laurenpictureprogress = 13
        R "But I'm going to try to be as professional as possible."
        R "I might push you a little bit out of your comfort zone, but remember, it's just because I know what people want to see on the internet,"
        R "And I'll only be suggesting things that will get you more likes and more money to help pay Mom's Mafia debt."
        R "If you're too uncomfortable to go any further with the shoot, we'll just call it a day, and see how we feel on the next one."
        RT "{i}{b}I've got to remember not to push Lauren too hard.  If I make her mad, she's just going to end the photo shoot and go home.{/b}{/i}"
        R "So, are you ready?"
        $ first_htbyd_shoot = False
        $ progress = 12
        L "I think so. Thanks for being so professional, I almost forgot you were my brother for a second."
        R "Good! Go with that. Try to think of me as a professional photographer who's going to make you an internet sensation."
        L "And you ruined it, now you're just my brother again."
        R "Ok, smartass, let's just get started."
    else:
        R "Ok Lauren, try not to be nervous, I'll try to be even more professional than last time."
        R "Just try to be open to more of my suggestions. Like I said before, I'm just trying to make your pictures get as many likes as possible."
        L "It just seems like you're being really pervy sometimes."
        R "Don't forget I'm your brother. I love you, and I've got your best interest at heart. You're safer with me, then anybody else."
        L "Yeah, yeah, let's just get this photoshoot started."
    R "Ok, let's start out with a pose like a warrior hunting in the forest."
    if inventory.inv_amount(green_screen) == 1:
        scene bg HTBYD_GS_00
        with dissolve
    else:
        scene bg HTBYD_E_00
        with dissolve
    L "How's this?"
    R "It's great!"
    R "Hold that pose while I take the picture."
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    if inventory.inv_amount(green_screen) == 1:
        scene bg HTBYD_GS_00
    else:
        scene bg HTBYD_E_00
    R "Perfect.... I got it."
    if inventory.inv_amount(green_screen) == 1:
        R "Since we've got this kick-ass green screen, I'll be able to add a forest background to this picture."
        R "I can see it now."
        scene bg BlurryWhite
        with fade
        scene bg HTBYD_F_00
        with fade
        $ renpy.pause ()
        scene bg BlurryWhite
        with fade
        scene bg HTBYD_GS_00
        with fade
        R "That's going to look really good."
    else:
        pass
    R "Now let's go for some sexier pictures."
    play music SexMusic
    R "Why don't you take off the leg warmers, the arm warmers and whatever that thing is around your torso."
    R "Then sit down on the floor like you're taking a break from your dragon hunting."
    L "Haha, yeah ok, that doesn't sound too bad."
    scene bg SleepBlack
    with fade
    if inventory.inv_amount(green_screen) == 1:
        scene bg HTBYD_GS_02
        with fade
    else:
        scene bg HTBYD_E_02
        with fade
    L "How's this pose?"
    R "Great as well. You look like one of those Playboy mudflap sillhouettes."
    L "Oh, hahah.... just take the picture already!"
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    if inventory.inv_amount(green_screen) == 1:
        scene bg HTBYD_GS_02
    else:
        scene bg HTBYD_E_02
    R "Beautiful smile!"
    L "Thanks."
    if inventory.inv_amount(green_screen) == 1:
        R "This one's going to look great with the forest background as well."
        scene bg BlurryWhite
        with fade
        scene bg HTBYD_F_02
        with fade
        $ renpy.pause ()
        scene bg BlurryWhite
        with fade
        scene bg HTBYD_GS_02
        with fade
    else:
        pass
    R "Lauren, you're so photogenic!"
    L "Ah.... thanks [ryan]!"
    RT "{i}Ok, should I keep going?{/i}"
    $ timeofdaycounter += 1
    menu:
        "Ask her to take off her skirt. {i}(submission 5+ {b}{color=#0000ff}or{/color}{/b} libido 9+){/i}":
            if laurensubmission >= 5 or laurenlibido >= 9:
                jump removeskirt
            else:
                R "Ok, how bout we make that outfit even more sexy."
                if inventory.inv_amount(green_screen) == 1:
                    scene bg HTBYD_GS_03
                    with fade
                else:
                    scene bg HTBYD_E_03
                    with fade
                L "Uhhh.... I don't think that's a good idea. Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's get rid of the skirt."
                L "But I've only got a buckskin thong on underneath!"
                R "Yeah, it will look fantastic in the pics."
                L "Yeah.... I don't think so. I'm going to get dressed and go home."
                L "We can try again next week if you're willing to be more professional."
                scene bg SleepBlack
                with fade
                "To get Lauren to take her skirt off you must have her submission at 5 points or her libido at 9 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Ask her to show her buckskin thong from behind. {i}(submission 7+ {b}{color=#0000ff}or{/color}{/b} libido 9+){/i}":
            if laurensubmission >= 7 or laurenlibido >= 9:
                R "How about we make that outfit even more sexy."
                L "How do you mean?"
                R "Let's get rid of the skirt and have you show off that thong from behind."
                if inventory.inv_amount(green_screen) == 1:
                    scene bg HTBYD_GS_03
                    with fade
                else:
                    scene bg HTBYD_E_03
                    with fade
                L "But that thong leaves so little to the imagination!"
                R "True, but it still does leave some things to the imagination."
                L "I'm a little uncomfortable with that."
                R "Alright, but I know it will boost the likes on your profile like crazy!"
                L "Well.... ok, I guess we can do that."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                else:
                    pass
                R "And get rid of that axe and shield while you're at it. We shouldn't need those any more."
                L "Ok, give me just a second."
                if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
                    $ photoshoot_kinky += 1
                else:
                    pass
                jump thongtime
            else:
                R "Ok, how bout we make that outfit even more sexy."
                if inventory.inv_amount(green_screen) == 1:
                    scene bg HTBYD_GS_03
                    with fade
                else:
                    scene bg HTBYD_E_03
                    with fade
                L "Uhhh.... I don't think that's a good idea. Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's get rid of the skirt and have you show off that thong from behind."
                L "But that thong leaves so little to the imagination!"
                R "Yeah, it will look fantastic in the pics."
                L "Yeah.... I don't think so. I'm going to get dressed and go home."
                "{i}\"Lauren Anger +1\"{/i}"
                $ laurenanger += 1
                "{i}\"Lauren Affection -1\"{/i}"
                $ laurenaffection -= 1
                L "We can try again next week if you're willing to be more professional."
                scene bg SleepBlack
                with fade
                "To get Lauren to take her skirt off and show off her thong, you must have her submission at 7 points or her libido at 9 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Ask her to take off her buckskin bra. {i}(submission 10+ {b}{color=#0000ff}or{/color}{/b} libido 10){/i}":
            if laurensubmission >= 10 or laurenlibido >= 10:
                R "How about we make that outfit even more sexy."
                L "How do you mean?"
                R "Let's get rid of the skirt and the buckskin bra."
                if inventory.inv_amount(green_screen) == 1:
                    scene bg HTBYD_GS_03
                    with fade
                else:
                    scene bg HTBYD_E_03
                    with fade
                L "What? I'm not ready to show off my breasts yet."
                R "Well, you can cover them with your hands."
                L "I'm a little uncomfortable with that."
                R "Alright, but I know it will boost the likes on your profile like crazy!"
                L "Well.... ok, I guess we can do that."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
                    $ photoshoot_kinky += 2
                else:
                    pass
                jump removebra
            else:
                R "Ok, how bout we make that outfit even more sexy."
                if inventory.inv_amount(green_screen) == 1:
                    scene bg HTBYD_GS_03
                    with fade
                else:
                    scene bg HTBYD_E_03
                    with fade
                L "Uhhh.... I don't think that's a good idea. Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's get rid of the skirt and buckskin bra."
                L "What? I'm not ready to show off my breasts yet."
                R "Well, you can cover them with your hands."
                R "Plus, it will look fantastic in the pics."
                L "Yeah.... I don't think so. I'm going to get dressed and go home."
                "{i}\"Lauren Anger +2\"{/i}"
                $ laurenanger += 2
                "{i}\"Lauren Affection -1\"{/i}"
                $ laurenaffection -= 1
                L "We can try again next week if you're willing to be more professional."
                scene bg SleepBlack
                with fade
                "To get Lauren to take her bra off you must have her submission at 10 points or her libido at 10 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Ask her to show her titties. {i}(submission 14+){/i}":
            if inventory.inv_amount(green_screen) == 0:
                R "Actually, let's call it a day. I've got some more great ideas for this photoshoot in the future, but I need to get a green screen first."
                L "Ok, I'll go get dressed and see you back at home."
                R "Later."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
            if laurensubmission >= 14:
                R "How about we make that outfit even more sexy."
                L "How do you mean?"
                R "Let's get rid of the skirt and the buckskin bra and get some tasteful pictures of your breasts."
                scene bg HTBYD_GS_03
                with fade
                L "What? I'm not letting you take pictures of my bare naked titties!"
                R "It's not like I'm asking you to go full nude or anything."
                L "I'm a little uncomfortable with that."
                R "Alright, but I know it will boost the likes on your profile like crazy!"
                L "Well.... ok, I guess we can do that, if it helps me get internet famous."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
                    $ photoshoot_kinky += 3
                else:
                    pass
                jump showtitties
            else:
                R "Ok, how bout we make that outfit even more sexy."
                scene bg HTBYD_GS_03
                with fade
                L "Uhhh.... I don't think that's a good idea. Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's get rid of the skirt and buckskin bra and get some nice pics of them titties."
                L "What? I'm not letting you take pictures of my bare naked titties!"
                R "It's not like I'm asking you to go full nude or anything."
                R "Plus, it will look fantastic in the pics."
                L "Yeah.... I don't think so. I'm going to get dressed and go home."
                "{i}\"Lauren Anger +3\"{/i}"
                $ laurenanger += 3
                "{i}\"Lauren Affection -1\"{/i}"
                $ laurenaffection -= 1
                L "We can try again next week if you're willing to be more professional."
                scene bg SleepBlack
                with fade
                "To get Lauren to take her bra off and show off her tits, you must have her submission at 14 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Ask her to take off her buckskin thong. {i}(submission 19+){/i}":
            if inventory.inv_amount(green_screen) == 0:
                R "Actually, let's call it a day. I've got some more great ideas for this photoshoot in the future, but I need to get a green screen first."
                L "Ok, I'll go get dressed and see you back at home."
                R "Later."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
            if laurensubmission >= 19:
                R "How about we make that outfit even more sexy."
                L "How do you mean?"
                R "Let's get rid of the bra and panties and take some tasteful nude shots."
                scene bg HTBYD_GS_03
                with fade
                L "What? I'm not completely stripping to nothing for you!"
                R "You won't be completely naked, you will still wear all of your accessories."
                L "That isn't helping. I'm really uncomfortable with this."
                R "Alright, your call, but I know it will boost the likes on your profile like crazy!"
                L "Well.... ok, I guess we can do that, if it helps me get internet famous."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
                    $ photoshoot_kinky += 4
                else:
                    pass
                jump removethong
            else:
                R "Ok, how bout we make that outfit even more sexy."
                scene bg HTBYD_GS_03
                with fade
                L "Uhhh.... I don't think that's a good idea. Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's get rid of the bra and panties and shoot the rest in the nude."
                L "What? I'm not completely stripping to nothing for you!"
                R "You won't be completely naked, you will still wear all of your accessories."
                R "Plus, it will look fantastic in the pics."
                L "Yeah.... I don't think so. I'm going to get dressed and go home."
                "{i}\"Lauren Anger +4\"{/i}"
                $ laurenanger += 4
                "{i}\"Lauren Affection -1\"{/i}"
                $ laurenaffection -= 1
                L "We can try again next week if you're willing to be more professional."
                scene bg SleepBlack
                with fade
                "To get Lauren to take everything off you must have her submission at 19 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Ask her for explicit close-ups. {i}(submission 25+){/i}":
            if inventory.inv_amount(green_screen) == 0:
                R "Actually, let's call it a day. I've got some more great ideas for this photoshoot in the future, but I need to get a green screen first."
                L "Ok, I'll go get dressed and see you back at home."
                R "Later."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
            if laurensubmission >= 25:
                R "Ok, how bout we take this shoot to a whole different level."
                L "How do you mean?"
                R "Let's get right to what the fans have been asking for."
                L "I'm afraid to ask."
                R "They're practically begging for some between the leg close-ups."
                scene bg HTBYD_GS_03
                with fade
                L "What? I'm not showing off my coochie for you!"
                R "You're not showing it to me, it's for your loyal fans who have become enchanted by you."
                L "I have been reading a lot of sweet comments from a lot of them, but I'm really uncomfortable with this."
                R "Alright, your call, but I think this will take you to a whole new level of internet fame!"
                L "Well.... ok, I guess we can do that, but only because I love my fans, and don't want to leave them with blue balls."
                R "It's not just guys."
                L "Oh my God, I know. hehehe..."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
                    $ photoshoot_kinky += 5
                else:
                    pass
                jump htbyd_closeups
            else:
                R "Ok, how bout we take this shoot to a whole different level."
                scene bg HTBYD_GS_03
                with fade
                L "Uhhh.... what do you mean? Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's get some close-ups of between your legs."
                L "What? I'm not showing off my coochie for you!"
                R "That's what your fans have been asking for in the comments section."
                R "I'm just trying to give the people what they want so we can get the most likes possible."
                L "Yeah.... I don't think so, and fuck you! I'm going to get dressed and go home."
                "{i}\"Lauren Anger +10\"{/i}"
                $ laurenanger += 10
                "{i}\"Lauren Affection -5\"{/i}"
                $ laurenaffection -= 5
                L "You better stop acting like an asshole if you want me to come again next week."
                scene bg SleepBlack
                with fade
                "To get Lauren to take explicit photos, submission must be at 25 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Finish Photo-shoot.":
            R "I think we've got all the pics we need for now."
            L "Really? We haven't taken that many."
            R "Yeah, but the ones we have are really good, and the only way they could be better, is if I pushed you to do something you might not be comfortable with."
            L "Oh, [ryan]! You're such a professional."
            L "And I really enjoyed the shoot!"
            L "And showing some skin was kind of exciting!"
            if not finished_htbyd_shoot:
                "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                "{i}{b}\"Lauren's Libido +2\"{/b}{/i}"
                $ laurenaffection += 1
                $ laurenlibido += 2
            L "I can't wait for the next photoshoot."
            L "I might be even more daring, and be willing to show a little more skin.... hahah..."
            R "Great! I can't wait either."
            R "You can get dressed and I'll see you back home."
            hide screen Points_screen_Lauren_cosplay
            jump posting_the_htbyd_pics

label removeskirt:
    R "How about we make that outfit even more sexy."
    L "How do you mean?"
    R "Let's take off that skirt so we can see just a little more skin."
    if inventory.inv_amount(green_screen) == 1:
        scene bg HTBYD_GS_03
        with fade
    else:
        scene bg HTBYD_E_03
        with fade
    L "Uhhh.... but all I have on is a buckskin thong underneath."
    R "That will make some super sexy pictures."
    L "I'm a little uncomfortable with that."
    R "Don't worry, we'll start out with just a side pic, so the thong won't reveal too much."
    L "Ok, I guess we can do that."
    if not finished_htbyd_shoot:
        "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
        $ laurensubmission += 1
    R "And get rid of that axe and shield while you're at it. We shouldn't need those any more."
    L "Ok, give me just a second."
    scene bg SleepBlack
    with fade
    if inventory.inv_amount(green_screen) == 1:
        scene bg HTBYD_GS_04
        with fade
    else:
        scene bg HTBYD_E_04
        with fade
    L "Is this kind of what you were thinking?"
    R "Once again, your posing talent amazes me."
    L "Are you just trying to butter me up?"
    R "Seriously, you look incredible."
    if not finished_htbyd_shoot:
        "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
        $ laurenlibido += 1
    if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
        $ photoshoot_kinky += 1
    else:
        pass
    R "Ok, just hold that pose."
    L "Hurry, it's making my legs tired."
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    if inventory.inv_amount(green_screen) == 1:
        scene bg HTBYD_GS_04
    else:
        scene bg HTBYD_E_04
    R "That shot will turn out great too."
    if inventory.inv_amount(green_screen) == 1:
        R "I'll make sure to add a background to this one later."
        scene bg BlurryWhite
        with fade
        scene bg HTBYD_F_04
        with fade
        $ renpy.pause ()
        scene bg BlurryWhite
        with fade
        scene bg HTBYD_GS_04
        with fade
    else:
        pass
    R "You're looking great!"
    RT "{i}Should I go on?{/i}"
    menu:
        "Ask her to show her buckskin thong from behind. {i}(submission 7+ {b}{color=#0000ff}or{/color}{/b} libido 9+){/i}":
            if laurensubmission >= 7 or laurenlibido >= 9:
                R "Let's see what we can do to that outfit to sexy it up even more."
                L "How do you mean?"
                R "Let's show off that thong from behind."
                if inventory.inv_amount(green_screen) == 1:
                    scene bg HTBYD_GS_05
                    with fade
                else:
                    scene bg HTBYD_E_05
                    with fade
                L "But that thong leaves so little to the imagination!"
                R "True, but it still does leave some things to the imagination."
                L "I'm a little uncomfortable with that."
                R "Alright, I wonder if this outfit would fit Mandy. She wouldn't have any problem doing that, and she'd get a ton of likes for it."
                L "Well.... ok, I guess we can do that."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                jump thongtime
            else:
                R "Ok, let's see what we can do to that outfit to sexy it up even more."
                if inventory.inv_amount(green_screen) == 1:
                    scene bg HTBYD_GS_05
                    with fade
                else:
                    scene bg HTBYD_E_05
                    with fade
                L "Uhhh.... I don't think that's a good idea. Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's show off that thong from behind."
                L "But that thong leaves so little to the imagination!"
                R "Yeah, it will look fantastic in the pics."
                L "Yeah.... I don't think so. I'm going to get dressed and go home."
                "{i}\"Lauren Anger +1\"{/i}"
                $ laurenanger += 1
                "{i}\"Lauren Affection -1\"{/i}"
                $ laurenaffection -= 1
                L "We can try again next week if you're willing to be more professional."
                scene bg SleepBlack
                with fade
                "To get Lauren to take her skirt off and show off her thong, you must have her submission at 7 points or her libido at 9 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Ask her to take off her buckskin bra. {i}(submission 10+ {b}{color=#0000ff}or{/color}{/b} libido 10){/i}":
            if laurensubmission >= 10 or laurenlibido >= 10:
                R "Let's see what we can do to that outfit to sexy it up even more."
                L "How do you mean?"
                R "Let's get rid of the buckskin bra."
                if inventory.inv_amount(green_screen) == 1:
                    scene bg HTBYD_GS_05
                    with fade
                else:
                    scene bg HTBYD_E_05
                    with fade
                L "What? I'm not ready to show off my breasts yet."
                R "Well, you can cover them with your hands."
                L "I'm a little uncomfortable with that."
                R "Alright, I wonder if this outfit would fit Mandy. She wouldn't have any problem doing that, and she'd get a ton of likes for it."
                L "Well.... ok, I guess we can do that."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
                    $ photoshoot_kinky += 1
                else:
                    pass
                jump removebra
            else:
                R "Ok, let's see what we can do to that outfit to sexy it up even more."
                if inventory.inv_amount(green_screen) == 1:
                    scene bg HTBYD_GS_05
                    with fade
                else:
                    scene bg HTBYD_E_05
                    with fade
                L "Uhhh.... I don't think that's a good idea. Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's get rid of the buckskin bra."
                L "What? I'm not ready to show off my breasts yet."
                R "Well, you can cover them with your hands."
                R "Plus, it will look fantastic in the pics."
                L "Yeah.... I don't think so. I'm going to get dressed and go home."
                "{i}\"Lauren Anger +2\"{/i}"
                $ laurenanger += 2
                "{i}\"Lauren Affection -1\"{/i}"
                $ laurenaffection -= 1
                L "We can try again next week if you're willing to be more professional."
                scene bg SleepBlack
                with fade
                "To get Lauren to take her bra off you must have her submission at 10 points or her libido at 10 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Ask her to show her titties. {i}(submission 14+){/i}":
            if inventory.inv_amount(green_screen) == 0:
                R "Actually, let's call it a day. I've got some more great ideas for this photoshoot in the future, but I need to get a green screen first."
                L "Ok, I'll go get dressed and see you back at home."
                R "Later."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
            if laurensubmission >= 14:
                R "Let's see what we can do to that outfit to sexy it up even more."
                L "How do you mean?"
                R "Let's get some tasteful pictures of your breasts."
                scene bg HTBYD_GS_05
                with fade
                L "What? I'm not letting you take pictures of my bare naked titties!"
                R "It's not like I'm asking you to go full nude or anything."
                L "I'm a little uncomfortable with that."
                R "Alright, I wonder if this outfit would fit Mandy. She wouldn't have any problem doing that, and she'd get a ton of likes for it."
                L "Well.... ok, I guess we can do that, if it helps me get internet famous."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
                    $ photoshoot_kinky += 2
                else:
                    pass
                jump showtitties
            else:
                R "Ok, let's see what we can do to that outfit to sexy it up even more."
                scene bg HTBYD_GS_05
                with fade
                L "Uhhh.... I don't think that's a good idea. Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's get some nice pics of them titties."
                L "What? I'm not letting you take pictures of my bare naked titties!"
                R "It's not like I'm asking you to go full nude or anything."
                R "Plus, it will look fantastic in the pics."
                L "Yeah.... I don't think so. I'm going to get dressed and go home."
                "{i}\"Lauren Anger +3\"{/i}"
                $ laurenanger += 3
                "{i}\"Lauren Affection -1\"{/i}"
                $ laurenaffection -= 1
                L "We can try again next week if you're willing to be more professional."
                scene bg SleepBlack
                with fade
                "To get Lauren to take her bra off and show off her tits, you must have her submission at 14 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Ask her to take off her buckskin thong. {i}(submission 19+){/i}":
            if inventory.inv_amount(green_screen) == 0:
                R "Actually, let's call it a day. I've got some more great ideas for this photoshoot in the future, but I need to get a green screen first."
                L "Ok, I'll go get dressed and see you back at home."
                R "Later."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
            if laurensubmission >= 19:
                R "Let's see what we can do to that outfit to sexy it up even more."
                L "How do you mean?"
                R "Let's get some tasteful nude shots."
                scene bg HTBYD_GS_05
                with fade
                L "What? I'm not completely stripping to nothing for you!"
                R "You won't be completely naked, you will still wear all of your accessories."
                L "That isn't helping. I'm really uncomfortable with this."
                R "Alright, your call, I wonder if this outfit would fit Mandy. She wouldn't have any problem doing that, and she'd get a ton of likes for it."
                L "Well.... ok, I guess we can do that, if it helps me get internet famous."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
                    $ photoshoot_kinky += 3
                else:
                    pass
                jump removethong
            else:
                R "Ok, let's see what we can do to that outfit to sexy it up even more."
                scene bg HTBYD_GS_05
                with fade
                L "Uhhh.... I don't think that's a good idea. Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's shoot the rest in the nude."
                L "What? I'm not completely stripping to nothing for you!"
                R "You won't be completely naked, you will still wear all of your accessories."
                R "Plus, it will look fantastic in the pics."
                L "Yeah.... I don't think so. I'm going to get dressed and go home."
                "{i}\"Lauren Anger +4\"{/i}"
                $ laurenanger += 4
                "{i}\"Lauren Affection -1\"{/i}"
                $ laurenaffection -= 1
                L "We can try again next week if you're willing to be more professional."
                scene bg SleepBlack
                with fade
                "To get Lauren to take everything off you must have her submission at 19 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Ask her for explicit close-ups. {i}(submission 25+){/i}":
            if inventory.inv_amount(green_screen) == 0:
                R "Actually, let's call it a day. I've got some more great ideas for this photoshoot in the future, but I need to get a green screen first."
                L "Ok, I'll go get dressed and see you back at home."
                R "Later."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
            if laurensubmission >= 25:
                R "Ok, how bout we take this shoot to a whole different level."
                L "How do you mean?"
                R "Let's get right to what the fans have been asking for."
                L "I'm afraid to ask."
                R "They're practically begging for some between the leg close-ups."
                scene bg HTBYD_GS_05
                with fade
                L "What? I'm not showing off my coochie for you!"
                R "You're not showing it to me, it's for your loyal fans who have become enchanted by you."
                L "I have been reading a lot of sweet comments from a lot of them, but I'm really uncomfortable with this."
                R "Alright, your call, but I think this will take you to a whole new level of internet fame!"
                L "Well.... ok, I guess we can do that, but only because I love my fans, and don't want to leave them with blue balls."
                R "It's not just guys."
                L "Oh my God, I know. hehehe..."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
                    $ photoshoot_kinky += 4
                else:
                    pass
                jump htbyd_closeups
            else:
                R "Ok, how bout we take this shoot to a whole different level."
                scene bg HTBYD_GS_05
                with fade
                L "Uhhh.... what do you mean? Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's get some close-ups of between your legs."
                L "What? I'm not showing off my coochie for you!"
                R "That's what your fans have been asking for in the comments section."
                R "I'm just trying to give the people what they want so we can get the most likes possible."
                L "Yeah.... I don't think so, and fuck you! I'm going to get dressed and go home."
                "{i}\"Lauren Anger +10\"{/i}"
                $ laurenanger += 10
                "{i}\"Lauren Affection -5\"{/i}"
                $ laurenaffection -= 5
                L "You better stop acting like an asshole if you want me to come again next week."
                scene bg SleepBlack
                with fade
                "To get Lauren to take explicit photos, submission must be at 25 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Finish Photo-shoot.":
            R "I think we've got all the pics we need for now."
            L "Really? We haven't taken that many."
            R "Yeah, but the ones we have are really good, and the only way they could be better, is if I pushed you to do something you might not be comfortable with."
            L "Oh, [ryan]! You're such a professional."
            L "And I really enjoyed the shoot!"
            L "And showing some skin was kind of exciting!"
            if not finished_htbyd_shoot:
                "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                "{i}{b}\"Lauren's Libido +2\"{/b}{/i}"
                $ laurenaffection += 1
                $ laurenlibido += 2
            L "I can't wait for the next photoshoot."
            L "I might be even more daring, and be willing to show a little more skin.... hahah..."
            R "Great! I can't wait either."
            R "You can get dressed and I'll see you back home."
            hide screen Points_screen_Lauren_cosplay
            jump posting_the_htbyd_pics

label thongtime:
    scene bg SleepBlack
    with fade
    if inventory.inv_amount(green_screen) == 1:
        scene bg HTBYD_GS_06
        with fade
    else:
        scene bg HTBYD_E_06
        with fade
    L "How's this one?"
    L "Are you liking what you see?"
    R "Oh, yeah! If I wasn't your brother, I'd hit that."
    L "Haha.... In your dreams!"
    if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
        $ photoshoot_kinky += 1
    else:
        pass
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    if inventory.inv_amount(green_screen) == 1:
        scene bg HTBYD_GS_06
    else:
        scene bg HTBYD_E_06
    R "You really do have a great ass."
    R "Do you do yoga or something?"
    L "No, it's just from jogging."
    R "Well, keep it up."
    if not finished_htbyd_shoot:
        "{i}\"Lauren Libido +1\"{/i}"
        $ laurenlibido += 1
    if inventory.inv_amount(green_screen) == 1:
        R "I can't wait to see this one with the new background."
        scene bg BlurryWhite
        with fade
        scene bg HTBYD_F_06
        with fade
        $ renpy.pause ()
        scene bg BlurryWhite
        with fade
        scene bg HTBYD_GS_06
        with fade
    else:
        pass
    RT "{i}Things seem to be going pretty well. Should I keep going?{/i}"
    menu:
        "Ask her to take off her buckskin bra. {i}(submission 10+ {b}{color=#0000ff}or{/color}{/b} libido 10){/i}":
            if laurensubmission >= 10 or laurenlibido >= 10:
                R "Let's see what we can do to that outfit to sexy it up even more."
                L "How do you mean?"
                R "Let's get rid of the buckskin bra."
                if inventory.inv_amount(green_screen) == 1:
                    scene bg HTBYD_GS_07
                    with fade
                else:
                    scene bg HTBYD_E_07
                    with fade
                L "What? I'm not ready to show off my breasts yet."
                R "Well, you can cover them with your hands."
                L "I'm a little uncomfortable with that."
                R "Alright, I only suggested it because I saw Jassica Nugru posted a similar picture on her profile, and her page almost shut down because of all the likes she got."
                L "Well.... ok, I guess we can do that."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                jump removebra
            else:
                R "Ok, let's see what we can do to that outfit to sexy it up even more."
                if inventory.inv_amount(green_screen) == 1:
                    scene bg HTBYD_GS_07
                    with fade
                else:
                    scene bg HTBYD_E_07
                    with fade
                L "Uhhh.... I don't think that's a good idea. Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's get rid of the buckskin bra."
                L "What? I'm not ready to show off my breasts yet."
                R "Well, you can cover them with your hands."
                R "Plus, it will look fantastic in the pics."
                L "Yeah.... I don't think so. I'm going to get dressed and go home."
                "{i}\"Lauren Anger +2\"{/i}"
                $ laurenanger += 2
                "{i}\"Lauren Affection -1\"{/i}"
                $ laurenaffection -= 1
                L "We can try again next week if you're willing to be more professional."
                scene bg SleepBlack
                with fade
                "To get Lauren to take her bra off you must have her submission at 10 points or her libido at 10 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Ask her to show her titties. {i}(submission 14+){/i}":
            if inventory.inv_amount(green_screen) == 0:
                R "Actually, let's call it a day. I've got some more great ideas for this photoshoot in the future, but I need to get a green screen first."
                L "Ok, I'll go get dressed and see you back at home."
                R "Later."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
            if laurensubmission >= 14:
                R "Let's see what we can do to that outfit to sexy it up even more."
                L "How do you mean?"
                R "Let's get some tasteful pictures of your breasts."
                scene bg HTBYD_GS_07
                with fade
                L "What? I'm not letting you take pictures of my bare naked titties!"
                R "It's not like I'm asking you to go full nude or anything."
                L "I'm a little uncomfortable with that."
                R "Alright, I only suggested it because I saw Jassica Nugru posted a similar picture on her profile, and her page almost shut down because of all the likes she got."
                L "Well.... ok, I guess we can do that, if it helps me get internet famous."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
                    $ photoshoot_kinky += 1
                else:
                    pass
                jump showtitties
            else:
                R "Ok, let's see what we can do to that outfit to sexy it up even more."
                scene bg HTBYD_GS_07
                with fade
                L "Uhhh.... I don't think that's a good idea. Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's get some nice pics of them titties."
                L "What? I'm not letting you take pictures of my bare naked titties!"
                R "It's not like I'm asking you to go full nude or anything."
                R "Plus, it will look fantastic in the pics."
                L "Yeah.... I don't think so. I'm going to get dressed and go home."
                "{i}\"Lauren Anger +3\"{/i}"
                $ laurenanger += 3
                "{i}\"Lauren Affection -1\"{/i}"
                $ laurenaffection -= 1
                L "We can try again next week if you're willing to be more professional."
                scene bg SleepBlack
                with fade
                "To get Lauren to take her bra off and show off her tits, you must have her submission at 14 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Ask her to take off her buckskin thong. {i}(submission 19+){/i}":
            if inventory.inv_amount(green_screen) == 0:
                R "Actually, let's call it a day. I've got some more great ideas for this photoshoot in the future, but I need to get a green screen first."
                L "Ok, I'll go get dressed and see you back at home."
                R "Later."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
            if laurensubmission >= 19:
                R "Let's see what we can do to that outfit to sexy it up even more."
                L "How do you mean?"
                R "Let's get some tasteful nude shots."
                scene bg HTBYD_GS_07
                with fade
                L "What? I'm not completely stripping to nothing for you!"
                R "You won't be completely naked, you will still wear all of your accessories."
                L "That isn't helping. I'm really uncomfortable with this."
                R "Alright, your call, I only suggested it because I saw Jassica Nugru posted a similar picture on her profile, and her page almost shut down because of all the likes she got."
                L "Well.... ok, I guess we can do that, if it helps me get internet famous."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
                    $ photoshoot_kinky += 2
                else:
                    pass
                jump removethong
            else:
                R "Ok, let's see what we can do to that outfit to sexy it up even more."
                scene bg HTBYD_GS_07
                with fade
                L "Uhhh.... I don't think that's a good idea. Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's shoot the rest in the nude."
                L "What? I'm not completely stripping to nothing for you!"
                R "You won't be completely naked, you will still wear all of your accessories."
                R "Plus, it will look fantastic in the pics."
                L "Yeah.... I don't think so. I'm going to get dressed and go home."
                "{i}\"Lauren Anger +4\"{/i}"
                $ laurenanger += 4
                "{i}\"Lauren Affection -1\"{/i}"
                $ laurenaffection -= 1
                L "We can try again next week if you're willing to be more professional."
                scene bg SleepBlack
                with fade
                "To get Lauren to take everything off you must have her submission at 19 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Ask her for explicit close-ups. {i}(submission 25+){/i}":
            if inventory.inv_amount(green_screen) == 0:
                R "Actually, let's call it a day. I've got some more great ideas for this photoshoot in the future, but I need to get a green screen first."
                L "Ok, I'll go get dressed and see you back at home."
                R "Later."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
            if laurensubmission >= 25:
                R "Ok, how bout we take this shoot to a whole different level."
                L "How do you mean?"
                R "Let's get right to what the fans have been asking for."
                L "I'm afraid to ask."
                R "They're practically begging for some between the leg close-ups."
                scene bg HTBYD_GS_07
                with fade
                L "What? I'm not showing off my coochie for you!"
                R "You're not showing it to me, it's for your loyal fans who have become enchanted by you."
                L "I have been reading a lot of sweet comments from a lot of them, but I'm really uncomfortable with this."
                R "Alright, your call, but I think this will take you to a whole new level of internet fame!"
                L "Well.... ok, I guess we can do that, but only because I love my fans, and don't want to leave them with blue balls."
                R "It's not just guys."
                L "Oh my God, I know. hehehe..."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
                    $ photoshoot_kinky += 3
                else:
                    pass
                jump htbyd_closeups
            else:
                R "Ok, how bout we take this shoot to a whole different level."
                scene bg HTBYD_GS_07
                with fade
                L "Uhhh.... what do you mean? Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's get some close-ups of between your legs."
                L "What? I'm not showing off my coochie for you!"
                R "That's what your fans have been asking for in the comments section."
                R "I'm just trying to give the people what they want so we can get the most likes possible."
                L "Yeah.... I don't think so, and fuck you! I'm going to get dressed and go home."
                "{i}\"Lauren Anger +10\"{/i}"
                $ laurenanger += 10
                "{i}\"Lauren Affection -5\"{/i}"
                $ laurenaffection -= 5
                L "You better stop acting like an asshole if you want me to come again next week."
                scene bg SleepBlack
                with fade
                "To get Lauren to take explicit photos, submission must be at 25 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Finish Photo-shoot.":
            R "I think we've got all the pics we need for now."
            L "Really? We haven't taken that many."
            R "Yeah, but the ones we have are really good, and the only way they could be better, is if I pushed you to do something you might not be comfortable with."
            L "Oh, [ryan]! You're such a professional."
            L "And I really enjoyed the shoot!"
            L "And showing some skin was kind of exciting!"
            if not finished_htbyd_shoot:
                "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                "{i}{b}\"Lauren's Libido +2\"{/b}{/i}"
                $ laurenaffection += 1
                $ laurenlibido += 2
            L "I can't wait for the next photoshoot."
            L "I might be even more daring, and be willing to show a little more skin.... hahah..."
            R "Great! I can't wait either."
            R "You can get dressed and I'll see you back home."
            hide screen Points_screen_Lauren_cosplay
            jump posting_the_htbyd_pics

label removebra:
    scene bg SleepBlack
    with fade
    L "I can't believe I'm going topless in a photoshoot. I think I need to close my eyes for this one."
    R "Just smile and try to look happy."
    if inventory.inv_amount(green_screen) == 1:
        scene bg HTBYD_GS_08
        with fade
    else:
        scene bg HTBYD_E_08
        with fade
    L "Like this?"
    R "That actually looks really good. It looks like you're blissfully enjoying the seclusion of the forest."
    L "Haha, you're such a nerd."
    R "No, really, even with your top off, I think most of the attention will be drawn to how pretty your face is."
    if not finished_htbyd_shoot:
        "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
        $ laurenaffection += 1
    L "You're a natural at helping your subject feel at ease."
    L "Let me know when you've taken the picture."
    if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
        $ photoshoot_kinky += 1
    else:
        pass
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    if inventory.inv_amount(green_screen) == 1:
        scene bg HTBYD_GS_08
    else:
        scene bg HTBYD_E_08
    R "I've taken it, and I think it will look great."
    if inventory.inv_amount(green_screen) == 1:
        scene bg BlurryWhite
        with fade
        scene bg HTBYD_F_08
        with fade
        $ renpy.pause ()
        scene bg BlurryWhite
        with fade
        scene bg HTBYD_GS_08
        with fade
    else:
        pass
    R "You can open your eyes if you want to."
    L "Is my top still off? If it is, I don't think I want to."
    R "{i}(sarcastically){/i} Haha.... you're so funny."
    RT "{i}Should I keep this going?{/i}"
    menu:
        "Ask her to show her titties. {i}(submission 14+){/i}":
            if inventory.inv_amount(green_screen) == 0:
                R "Actually, let's call it a day. I've got some more great ideas for this photoshoot in the future, but I need to get a green screen first."
                L "Ok, I'll go get dressed and see you back at home."
                R "Later."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
            if laurensubmission >= 14:
                R "Let's see what we can do to that outfit to sexy it up even more."
                L "How do you mean?"
                R "Let's get some tasteful pictures of your breasts."
                scene bg HTBYD_GS_09
                with fade
                L "What? I'm not letting you take pictures of my bare naked titties!"
                R "It's not like I'm asking you to go full nude or anything."
                L "I'm a little uncomfortable with that."
                R "Alright, but there's a lot of people out there trying to find fame on the internet who fail because they're unwilling to do the hard and uncomfortable stuff."
                L "Well.... ok, I guess we can do that, if it helps me get internet famous."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                jump showtitties
            else:
                R "Ok, let's see what we can do to that outfit to sexy it up even more."
                scene bg HTBYD_GS_09
                with fade
                L "Uhhh.... I don't think that's a good idea. Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's get some nice pics of them titties."
                L "What? I'm not letting you take pictures of my bare naked titties!"
                R "It's not like I'm asking you to go full nude or anything."
                R "Plus, it will look fantastic in the pics."
                L "Yeah.... I don't think so. I'm going to get dressed and go home."
                "{i}\"Lauren Anger +3\"{/i}"
                $ laurenanger += 3
                "{i}\"Lauren Affection -1\"{/i}"
                $ laurenaffection -= 1
                L "We can try again next week if you're willing to be more professional."
                scene bg SleepBlack
                with fade
                "To get Lauren to take her bra off and show off her tits, you must have her submission at 14 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Ask her to take off her buckskin thong. {i}(submission 19+){/i}":
            if inventory.inv_amount(green_screen) == 0:
                R "Actually, let's call it a day. I've got some more great ideas for this photoshoot in the future, but I need to get a green screen first."
                L "Ok, I'll go get dressed and see you back at home."
                R "Later."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
            if laurensubmission >= 19:
                R "Let's see what we can do to that outfit to sexy it up even more."
                L "How do you mean?"
                R "Let's get some tasteful nude shots."
                scene bg HTBYD_GS_09
                with fade
                L "What? I'm not completely stripping to nothing for you!"
                R "You won't be completely naked, you will still wear all of your accessories."
                L "That isn't helping. I'm really uncomfortable with this."
                R "Alright, your call, but there's a lot of people out there trying to find fame on the internet who fail because they're unwilling to do the hard and uncomfortable stuff."
                L "Well.... ok, I guess we can do that, if it helps me get internet famous."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
                    $ photoshoot_kinky += 1
                else:
                    pass
                jump removethong
            else:
                R "Ok, let's see what we can do to that outfit to sexy it up even more."
                scene bg HTBYD_GS_09
                with fade
                L "Uhhh.... I don't think that's a good idea. Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's shoot the rest in the nude."
                L "What? I'm not completely stripping to nothing for you!"
                R "You won't be completely naked, you will still wear all of your accessories."
                R "Plus, it will look fantastic in the pics."
                L "Yeah.... I don't think so. I'm going to get dressed and go home."
                "{i}\"Lauren Anger +4\"{/i}"
                $ laurenanger += 4
                "{i}\"Lauren Affection -1\"{/i}"
                $ laurenaffection -= 1
                L "We can try again next week if you're willing to be more professional."
                scene bg SleepBlack
                with fade
                "To get Lauren to take everything off you must have her submission at 19 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Ask her for explicit close-ups. {i}(submission 25+){/i}":
            if inventory.inv_amount(green_screen) == 0:
                R "Actually, let's call it a day. I've got some more great ideas for this photoshoot in the future, but I need to get a green screen first."
                L "Ok, I'll go get dressed and see you back at home."
                R "Later."
                hide screen Points_screen_Lauren_cosplays
                jump posting_the_htbyd_pics
            if laurensubmission >= 25:
                R "Ok, how bout we take this shoot to a whole different level."
                L "How do you mean?"
                R "Let's get right to what the fans have been asking for."
                L "I'm afraid to ask."
                R "They're practically begging for some between the leg close-ups."
                scene bg HTBYD_GS_09
                with fade
                L "What? I'm not showing off my coochie for you!"
                R "You're not showing it to me, it's for your loyal fans who have become enchanted by you."
                L "I have been reading a lot of sweet comments from a lot of them, but I'm really uncomfortable with this."
                R "Alright, your call, but I think this will take you to a whole new level of internet fame!"
                L "Well.... ok, I guess we can do that, but only because I love my fans, and don't want to leave them with blue balls."
                R "It's not just guys."
                L "Oh my God, I know. hehehe..."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
                    $ photoshoot_kinky += 2
                else:
                    pass
                jump htbyd_closeups
            else:
                R "Ok, how bout we take this shoot to a whole different level."
                scene bg HTBYD_GS_09
                with fade
                L "Uhhh.... what do you mean? Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's get some close-ups of between your legs."
                L "What? I'm not showing off my coochie for you!"
                R "That's what your fans have been asking for in the comments section."
                R "I'm just trying to give the people what they want so we can get the most likes possible."
                L "Yeah.... I don't think so, and fuck you! I'm going to get dressed and go home."
                "{i}\"Lauren Anger +10\"{/i}"
                $ laurenanger += 10
                "{i}\"Lauren Affection -5\"{/i}"
                $ laurenaffection -= 5
                L "You better stop acting like an asshole if you want me to come again next week."
                scene bg SleepBlack
                with fade
                "To get Lauren to take explicit photos, submission must be at 25 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Finish Photo-shoot.":
            R "I think we've got all the pics we need for now."
            if inventory.inv_amount(green_screen) == 1:
                scene bg HTBYD_GS_28
                with dissolve
            else:
                pass
            L "Really? We haven't taken that many."
            R "Yeah, but the ones we have are really good, and the only way they could be better, is if I pushed you to do something you might not be comfortable with."
            L "Oh, [ryan]! You're such a professional."
            L "And I really enjoyed the shoot!"
            L "And showing some skin was kind of exciting!"
            if not finished_htbyd_shoot:
                "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                $ laurenaffection += 1
            L "I can't wait for the next photoshoot."
            L "I might be even more daring, and be willing to show a little more skin.... hahah..."
            R "Great! I can't wait either."
            R "You can get dressed and I'll see you back home."
            hide screen Points_screen_Lauren_cosplay
            jump posting_the_htbyd_pics

label showtitties:
    scene bg SleepBlack
    with fade
    R "Since your cosplay is Arsetrid from How to Breed your Dragon, I want you to pose like a dragon is coming out of the sky and you're really surprised."
    L "I hope you appreciate what I'm doing here. Posing partially nude is a big step from a sexy costume."
    L "How's this pose by the way?"
    scene bg HTBYD_GS_10
    with fade
    R "Looks great. You should be an actress, your expressions are so good, and I do appreciate what you're doing, but from what I've read online, posing nude is really empowering."
    L "Yeah, right. How is posing nude empowering?"
    R "You're not allowing just a single man to have power over you, and allowing him to dictate that you only display your body for him. You're freely choosing to show it off on your own terms."
    L "Yeah, well maybe you should do it then."
    R "I would if I thought anybody would pay me for it."
    L "Haha I'm sure there's a few women, and men actually, who would love to see that big cock of yours!"
    R ".... Did you like seeing it?"
    if not finished_htbyd_shoot:
        "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
        $ laurenlibido += 1
    L ".... Are you going to make me pose like this all day, or are you going to take a picture?"
    R "Oh right.... sorry."
    if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
        $ photoshoot_kinky += 1
    else:
        pass
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg HTBYD_GS_10
    R "That's perfect, and I'll use ZAD Studio to render a dragon flying into the scene."
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_F_10
    with fade
    R "Ok, now you've realized you've left your axe and shield too far away to retrieve, you might have to fight him with your fists."
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_GS_11
    with dissolve
    R "Great!"
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg HTBYD_GS_11
    $ renpy.pause ()
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_F_11
    with fade
    R "Ok, you've lowered your defenses since you can tell he's a friendly dragon,"
    R "But you can't believe the size of the claws on his feet!"
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_GS_12
    with fade
    R "Ok, good, look up just a little more, and look more surprised."
    R "Perfect!"
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg HTBYD_GS_12
    $ renpy.pause ()
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_F_12
    with fade
    R "Ok, now he's going to come up and start licking your face, just like a little puppy."
    L "Yuk, I hate it when puppies lick my face."
    R "What's wrong with you?"
    R "Ok, act like someone who likes puppies licking their face."
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_GS_13
    with fade
    R "Awesome! I think I can do something with that."
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_F_13
    with fade
    R "Ok, now look a little shocked as the Dragon lowers his tongue from your face."
    scene bg HTBYD_F_14
    with dissolve
    L "Are you going to make him lick my tits?"
    R "Hey, good idea. it's nice to see you showing some initiative here."
    L "Whatever!"
    play sound CameraClick
    R "Ok, now his tongue is going to move down to your belly button."
    L "Oh good, I was afraid you were going to say somewhere lower."
    R "Ummm.... yeah.... I wouldn't.... do.... that..."
    L "Yeah, that sounded convincing."
    R "Ok, make an expression on your face like the pressure of his tongue on your belly is making you need to pee."
    scene bg HTBYD_F_15
    with dissolve
    R "Yes, that's perfect!"
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_GS_15
    with fade
    R "We might want to consider doing videos instead of pictures with how good of an actress you are!"
    L "I don't even know what kind of videos you would want to make."
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg HTBYD_GS_15
    $ renpy.pause ()
    L "What's next?"
    R "Ok, I'm thinking you could crouch down and inspect his tail, since you're going to be a dragon breeder, you need to inspect your stud.... that's right.... no, just a little higher.... now cup under his tail, and with the other hand stroke one of the spikes on his tail."
    scene bg HTBYD_GS_16
    with dissolve
    L "Does this work?"
    R "Nailed it!"
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg HTBYD_GS_16
    $ renpy.pause ()
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_F_16
    with fade
    R "Good, now try to look impressed at how massive the scales on his tail are."
    R "You should be excited because this dragon is going to make such a good stud dragon."
    R "Perfect, now just hold that pose while I get a close-up shot and a better angle."
    scene bg HTBYD_F_17
    with fade
    R "I'm really excited about these pictures! They are going to get the hell liked out of them!"
    L "Oh.... I really hope so!..."
    RT "{i}Lauren might be mad at first when she sees these, but I think her anger will wear off after she sees how popular these pics are going to be.{/i}"
    RT "{i}Now should I ask her to continue, or call it good?{/i}"
    menu:
        "Ask her to take off her buckskin thong. {i}(submission 19+){/i}":
            if laurensubmission >= 19:
                R "Let's see what we can do to sexy up this photoshoot even more."
                L "How do you mean?"
                R "Let's get some tasteful nude shots."
                scene bg BlurryWhite
                with fade
                scene bg HTBYD_GS_18
                with fade
                L "What? I'm not completely stripping to nothing for you!"
                R "You won't be completely naked, you will still wear all of your accessories."
                L "That isn't helping. I'm really uncomfortable with this."
                R "Lauren, at this point I shouldn't have to convince you anymore. Have I been wrong yet? You need to just learn to trust me."
                L "Well.... ok, I guess you've earned it."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                jump removethong
            else:
                R "Ok, let's see what we can do to sexy up this photoshoot even more."
                scene bg BlurryWhite
                with fade
                scene bg HTBYD_GS_18
                with fade
                L "Uhhh.... I don't think that's a good idea. Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's shoot the rest in the nude."
                L "What? I'm not completely stripping to nothing for you!"
                R "You won't be completely naked, you will still wear all of your accessories."
                R "Plus, it will look fantastic in the pics."
                L "Yeah.... I don't think so. I'm going to get dressed and go home."
                "{i}\"Lauren Anger +4\"{/i}"
                $ laurenanger += 4
                "{i}\"Lauren Affection -1\"{/i}"
                $ laurenaffection -= 1
                L "We can try again next week if you're willing to be more professional."
                scene bg SleepBlack
                with fade
                "To get Lauren to take everything off you must have her submission at 19 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Ask her for explicit close-ups. {i}(submission 25+){/i}":
            if laurensubmission >= 25:
                R "Ok, how bout we take this shoot to a whole different level."
                L "How do you mean?"
                R "Let's get right to what the fans have been asking for."
                L "I'm afraid to ask."
                R "They're practically begging for some between the leg close-ups."
                scene bg BlurryWhite
                with fade
                scene bg HTBYD_GS_18
                with fade
                L "What? I'm not showing off my coochie for you!"
                R "You're not showing it to me, it's for your loyal fans who have become enchanted by you."
                L "I have been reading a lot of sweet comments from a lot of them, but I'm really uncomfortable with this."
                R "Alright, your call, but I think this will take you to a whole new level of internet fame!"
                L "Well.... ok, I guess we can do that, but only because I love my fans, and don't want to leave them with blue balls."
                R "It's not just guys."
                L "Oh my God, I know. hehehe..."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
                    $ photoshoot_kinky += 1
                else:
                    pass
                jump htbyd_closeups
            else:
                R "Ok, how bout we take this shoot to a whole different level."
                scene bg BlurryWhite
                with fade
                scene bg HTBYD_GS_18
                with fade
                L "Uhhh.... what do you mean? Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's get some close-ups of between your legs."
                L "What? I'm not showing off my coochie for you!"
                R "That's what your fans have been asking for in the comments section."
                R "I'm just trying to give the people what they want so we can get the most likes possible."
                L "Yeah.... I don't think so, and fuck you! I'm going to get dressed and go home."
                "{i}\"Lauren Anger +10\"{/i}"
                $ laurenanger += 10
                "{i}\"Lauren Affection -5\"{/i}"
                $ laurenaffection -= 5
                L "You better stop acting like an asshole if you want me to come again next week."
                scene bg SleepBlack
                with fade
                "To get Lauren to take explicit photos, submission must be at 25 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Finish Photo-shoot.":
            scene bg HTBYD_GS_28
            with fade
            R "I think we've got all the pics we need for now."
            L "Really? You don't think we need more?"
            R "No, and the ones we have are really good, and the only way they could be better, is if I pushed you to do something you might not be comfortable with."
            L "Oh, [ryan]! You're such a professional."
            L "And I really enjoyed the shoot!"
            L "And showing some skin was kind of exciting!"
            if not finished_htbyd_shoot:
                "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                $ laurenaffection += 1
            L "I can't wait for the next photoshoot."
            L "I might be even more daring, and be willing to show a little more skin.... hahah..."
            R "Great! I can't wait either."
            R "You can get dressed and I'll see you back home."
            hide screen Points_screen_Lauren_cosplay
            jump posting_the_htbyd_pics

label removethong:
    scene bg SleepBlack
    with fade
    scene bg HTBYD_GS_19
    with fade
    L "I can't believe I've let you talk me into going this far."
    R "Don't think about it like I've talked you into anything."
    R "Think of me like a mentor, or a life coach, and I'm helping you to do what you need to achieve your life goal."
    R "And that goal is?..."
    L ".... {i}(talking quietly){/i} To be internet famous."
    R "What was that?..."
    L "To be internet famous you cheeky bastard."
    R "Hahaha.... that's right."
    R "And now for the next shot, let's get a picture of you from behind, but stand in a way that conceals your goodies."
    L "My goodies, what are you ten?"
    scene bg HTBYD_GS_20
    with fade
    R "Beautiful! And kind of turn your upper torso this way so we can see some side boob."
    L "Well, I don't have a whole lot of boob to see, even from the front."
    R "Don't worry, I love little titties like yours."
    L "Really?"
    R "Oh, yeah!..."
    if not finished_htbyd_shoot:
        "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
        $ laurenlibido += 1
    R "And hold that pose."
    if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
        $ photoshoot_kinky += 1
    else:
        pass
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg HTBYD_GS_20
    L "How will you work the dragon into this scene?"
    R "Hmmmm.... I think I'll just have him sleeping in the background."
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_F_20
    with fade
    R "Wow, this photosession is getting really hot."
    R "Even being your brother and all, I'll admit that I'm struggling not to get turned on."
    L "Just try to keep it in your pants, ok?"
    R "Haha.... of course."
    R "Ok, now let's just get a quick shot of you bending over just a little bit."
    scene bg HTBYD_F_21
    with dissolve
    L "Like this?"
    play sound CameraClick
    R "Yep, got it!"
    RT "{i}I think I might be able to get her to go just a little bit farther, but should I?{/i}"
    menu:
        "Ask her for explicit close-ups. {i}(submission 25+){/i}":
            if laurensubmission >= 25:
                R "Ok, how bout we take this shoot to a whole different level."
                L "How do you mean?"
                R "Let's get right to what the fans have been asking for."
                L "I'm afraid to ask."
                R "They're practically begging for some between the leg close-ups."
                scene bg BlurryWhite
                with fade
                scene bg HTBYD_GS_22
                with fade
                L "What? I'm not showing off my coochie for you!"
                R "You're not showing it to me, it's for your loyal fans who have become enchanted by you."
                L "I have been reading a lot of sweet comments from a lot of them, but I'm really uncomfortable with this."
                R "Alright, your call, but I think this will take you to a whole new level of internet fame!"
                L "Well.... ok, I guess we can do that, but only because I love my fans, and don't want to leave them with blue balls."
                R "It's not just guys."
                L "Oh my God, I know. hehehe..."
                if not finished_htbyd_shoot:
                    "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                    $ laurensubmission += 1
                L "Ok, give me just a second."
                jump htbyd_closeups
            else:
                R "Ok, how bout we take this shoot to a whole different level."
                scene bg BlurryWhite
                with fade
                scene bg HTBYD_GS_22
                with fade
                L "Uhhh.... what do you mean? Isn't this sexy enough?.... I mean you can see a lot of skin."
                R "Well yeah, it looks sexy, but if you're going for a lot of likes, you're going to have to go further than that."
                L "Further? How far are you trying to get me to go, you pervert?"
                R "Let's get some close-ups of between your legs."
                L "What? I'm not showing off my coochie for you!"
                R "That's what your fans have been asking for in the comments section."
                R "I'm just trying to give the people what they want so we can get the most likes possible."
                L "Yeah.... I don't think so, and fuck you! I'm going to get dressed and go home."
                "{i}\"Lauren Anger +10\"{/i}"
                $ laurenanger += 10
                "{i}\"Lauren Affection -5\"{/i}"
                $ laurenaffection -= 5
                L "You better stop acting like an asshole if you want me to come again next week."
                scene bg SleepBlack
                with fade
                "To get Lauren to take explicit photos, submission must be at 25 points."
                hide screen Points_screen_Lauren_cosplay
                jump posting_the_htbyd_pics
        "Finish Photo-shoot.":
            scene bg HTBYD_GS_28
            with fade
            R "I think we've got all the pics we need for now."
            L "Really? You don't think we need more?"
            R "No, and the ones we have are really good, and the only way they could be better, is if I pushed you to do something you might not be comfortable with."
            L "Oh, [ryan]! You're such a professional."
            L "And I really enjoyed the shoot!"
            L "And showing some skin was kind of exciting!"
            if not finished_htbyd_shoot:
                "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                $ laurenaffection += 1
            L "I can't wait for the next photoshoot."
            L "I might be even more daring, and be willing to show a little more skin.... hahah..."
            R "Great! I can't wait either."
            R "You can get dressed and I'll see you back home."
            hide screen Points_screen_Lauren_cosplay
            jump posting_the_htbyd_pics

label htbyd_closeups:
    hide screen Points_screen_Lauren_cosplay
    scene bg SleepBlack
    with fade
    L "I can't believe I'm about to share the most intimate parts of my body with anybody with an internet connection."
    L "I've got a similar rush as riding on a roller coaster."
    R "Oh good, cuz that's a fun feeling."
    L "Yeah, I guess.... I'm kind of in a daze right now."
    L "So, I guess just tell me what to do."
    R "Let's just do a simple bend over and spread'em."
    scene bg HTBYD_GS_23
    with fade
    R "Yeah, let me just zoom in and get a close-up shot."
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_F_23
    with fade
    $ renpy.pause ()
    if finished_htbyd_shoot == False and weekly_htbyd_complete == False:
        $ photoshoot_kinky += 1
    else:
        pass
    play sound CameraClick
    R "Ok, and now I need a front shot with your legs spread."
    R "Let's just see how flexible you are."
    L "Oh, I can be pretty flexible, just call me ElastiBabe."
    R "Hey, that's not a bad idea for a future cosplay costume."
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_GS_24
    with fade
    R "That's a very pretty sight."
    R "Let me just get a close-up shot on that too."
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_F_24
    with fade
    R "I hope this doesn't sound too weird, given this situation and all, but working like this with you really makes me feel like our relationship has become a lot closer."
    L "Yeah, I feel closer to you too."
    if not finished_htbyd_shoot:
        "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
        $ laurenaffection += 1
    R "And hold that pose."
    play sound CameraClick
    R "And I think we only need one more pose and we'll call it good."
    R "For this one I want you to pose face down ass up."
    L "Ok, I've gone this far, what's a little more."
    R "And I want a side shot."
    L "Really? Not a close-up between the legs?"
    R "Not on this one. But we could do that too if you want."
    L "I'm good."
    L "Like this?"
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_GS_25
    with fade
    R "Yeah, but now show a little more pain in your expression."
    R "That's great!"
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg HTBYD_GS_25
    L "Oh boy.... I don't know if I even want to know what you're going to do with this picture."
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_F_25
    with fade
    R "Oh, I won't do much to it, but I think you'll like it."
    L "For some reason, I have a feeling I won't."
    R "Hahah.... it just depends on what you're into."
    R "Let's just say you've got to earn the title of \"Dragon Breeder\"."
    L "Oh no, [ryan], don't you dare!"
    R "Don't worry, I won't do any penetration."
    L "Oh my God, [ryan]!"
    R "And let me zoom in just a little bit..."
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_F_26
    with fade
    R "That's great Lauren!"
    R "I think this one is going to be my favorite."
    R "You can get up now if you want."
    scene bg BlurryWhite
    with fade
    scene bg HTBYD_GS_27
    with fade
    L "So, that's it? We don't need any more shots this session?"
    R "No, I think we've got a lot of good stuff to work with."
    L "Oh.... ok.... good..."
    R "Let me just say, you did an amazing job!"
    R "You acted like a professional, did everything I told you to, and your presence in front of the camera is so natural."
    scene bg HTBYD_GS_30
    with dissolve
    R "And I had a lot of fun working with you."
    R "I'm glad we get to work together, because I miss all the time we used to spend together."
    scene bg HTBYD_GS_31
    with dissolve
    L "Oh, [ryan]!..."
    L "Thank's for being so professional, and helping me to fulfull my dream!"
    L "I've really enjoyed spending this time with you too."
    if tv_events >= 4 and not dragon_bj:
        jump htbyd_bj
    if tv_events >= 4 and not campaign_finished:
        jump htbyd_bj
    if campaign_finished:
        jump htbyd_fuck
    else:
        scene bg HTBYD_GS_32
        with dissolve
        if finished_htbyd_shoot == False:
            L "What are you doing?..."
            R "I'm just hugging you back."
            $ finished_htbyd_shoot = True
            scene bg HTBYD_GS_33
            with dissolve
            L "[ryan]? We're brother and sister.... you shouldn't hug your sister like this when she's completely naked."
            R "Why not?"
            L "Because this isn't just some episode of \"Game of Thots\", this is real life."
            R "I don't care."
            L "But society doesn't..."
            R "Fuck society."
            L "Well, if you don't mind..."
            L "Then..."
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_33
            with dissolve
            R "Oh my God, Lauren! I can't believe you just did that."
            L "Not done yet."
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            RT "{i}Oh, shit.... I got Lauren to grind me.... {/i}"
            RT "{i}She must want this as bad as me.{/i}"
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            RT "{i}Oh, man! I'm gonna cum.... {/i}"
            scene bg HTBYD_GS_36
            with dissolve
            R "Hnnnngggghhhh..."
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_37
            with dissolve
            L "Oh my God! Your pants are wet!"
            L "Did you just?..."
            R "Yeah.... I did..."
            L "But what if some got inside me?..."
            L "Could I get pregnant?"
            R "No.... I don't think so..."
            R "I think I'd have to be deep inside of you."
            scene bg HTBYD_GS_32
            with dissolve
            L "Oh, thank God!..."
            LT "{i}Mmmmmmmm.... [ryan] deep inside of me.... {/i}"
            if not finished_htbyd_shoot:
                "{i}{b}\"Lauren's Libido +10\"{/b}{/i}"
                $ laurenlibido += 10
            L "I can't believe that just happened."
            L "We can't let this go any further."
            R "Well, let's just see what happens."
            R "Try not to be too closed minded to future possibilities."
            L "Well, don't push your luck."
            L "I love you, but what if Mom or Sidney found out?"
            R "We'll worry about that when the time comes."
            L "No really, I don't think we should go any further."
            R "Ok, well we'll just have to worry about that when the time comes too."
            L "[ryan]! I'm serious!"
            R "Me too."
            scene bg HTBYD_GS_33
            with dissolve
            L "Well, I'd better go get my clothes back on. I'll see you back at home sometime?"
            R "Yeah.... I'll just clean things up here, and I'll be home soon too."
            jump posting_the_htbyd_pics
        else:
            L "Mmmmm.... I love your hugs."
            R "This feels so right."
            scene bg HTBYD_GS_33
            with fade
            L "[ryan]? I know I said we shouldn't go any farther, but it's ok if we just go as far as we did before right?"
            R "I think so."
            L "Good!"
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_33
            with dissolve
            R "Oh my God, Lauren! This feels so good!"
            L "Not done yet."
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            RT "{i}Oh, shit.... I got Lauren to grind me again.... {/i}"
            RT "{i}She won't admit it to herself, but she wants this as bad as me.{/i}"
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            RT "{i}Oh, man! I'm gonna cum.... {/i}"
            scene bg HTBYD_GS_36
            with dissolve
            R "Hnnnngggghhhh..."
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_35 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_34 with Dissolve(0.3)
            $ renpy.pause (0.05)
            scene bg HTBYD_GS_37
            with dissolve
            L "Oh my God! Your pants are wet!"
            L "I got you there again?..."
            R "Yeah.... you did..."
            scene bg HTBYD_GS_32
            with dissolve
            LT "{i}Mmmmmmmm.... I love his wet cum against my pussy.... {/i}"
            if not finished_htbyd_shoot:
                "{i}{b}\"Lauren's Libido +10\"{/b}{/i}"
                $ laurenlibido += 10
            L "I can't believe that just happened again."
            L "I told myself it wouldn't!"
            R "Well, sometimes you just have to live in the moment."
            L "Oh.... I really hope Mom and Sidney don't find out."
            L "They would be so disgusted."
            R "Well, you never know,"
            R "They might just have some surprises of their own."
            L "Doubt it would be anything like this."
            R "Who knows."
            scene bg HTBYD_GS_33
            with dissolve
            L "Well, I'd better go get my clothes back on. I'll see you back at home sometime?"
            R "Yeah.... I'll just clean things up here, and I'll be home soon too."
            jump posting_the_htbyd_pics

label emailalert:
    $ email_alert_one = True
    scene bg SleepBlack
    with fade
    play sound PhoneVibrate
    scene bg BlurryWhite
    with hpunch
    with vpunch
    scene bg RyanWakingWithSid01
    with fade
    RT "{i}Uuuuugghhh, who's texting me this early in the morning?{/i}"
    scene bg EmailAlert01
    with fade
    RT "{i}Oh man, it's just an email alert. You buy one thing at Hardnlong, and the emails never stop.{/i}"
    RT "{i}Huh? Oh, man! I'd love to see Mom in this! Maybe I should check the store and get it for her. I'm sure I can think of some way to get her to wear it.{/i}"
    jump myroom
