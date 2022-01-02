# The script of the game goes in this file.
# progress = 9

#define persistent.patreonsafe = True

#define persistent.mom = "Jacky"
#define persistent.dad = "Tony"
#define persistent.uncle = "Bobby"

default persistent.mod_on = False
default persistent.patch_on = False
default persistent.patchFile_i_on = False
default persistent.modCaught_on = False
default persistent.patreon_gal_screens_on = False
default run_load_000001 = True
default run_load_000001_0_06b = True

label after_load_000001:

    if renpy.loadable("AFV_v0.06_iPatch/iPatch.rpyc"):
        $ persistent.patch_on = True
    else:
        $ persistent.patch_on = False

    if renpy.loadable("Patreon_$5_Gallery/D.S.Mod.rpyc"):
        $ persistent.mod_on = True
    else:
        $ persistent.mod_on = False

    # if _version < config.version:
    if loyaltycounter < 2 and run_load_000001:
    # This defines the items.
        python:
            jacky_bikini_01 = NewItem("Jacky's bikini 01", outfit=True, image="images/interface_images/inventory_images/inv_Jacky_bikini_1.png", amount=0, cost=0)

        $ futj_bikini_1 = 0
        $ invj_bikini_1 = 0
        $ run_load_000001 = False

    default caught_by_sidney = False
    if progress > 7:
        $ picturesofsidney = True
        $ sawsidneychanging = True
        $ caught_by_sidney = True

    if persistent.gal_Lauren_Sidney_1 and not persistent.gal_harem_1:
        $ persistent.gal_harem_1 = True

    if christmas_complete and not persistent.gal_harem_2:
        $ persistent.gal_harem_2 = True

    if float(config.version[:4]) >= 0.05 and run_load_000001_0_06b:
        python:
            ball_gag = NewItem("Ball Gag", permanent=True, image="images/interface_images/inventory_images/inv_ball_gag.png", amount=0, cost=0)

            ph_book1 = NewItem("Perry Hotter Book 1", permanent=True, book=True, image="images/interface_images/inventory_images/inv_ph_book1.png", amount=0, cost=0)
            ph_book2 = NewItem("Perry Hotter Book 2", permanent=True, book=True, image="images/interface_images/inventory_images/inv_ph_book2.png", amount=0, cost=0)
            ph_book3 = NewItem("Perry Hotter Book 3", permanent=True, book=True, image="images/interface_images/inventory_images/inv_ph_book3.png", amount=0, cost=0)

            store.run_load_000001_0_06b = False
            store.fut_ball_gag = 0
            store.fut_ph_book1 = 0
            store.fut_ph_book2 = 0
            store.fut_ph_book3 = 0
            store.invball_gag = 0
            store.invph_book1 = 0
            store.invph_book2 = 0
            store.invph_book3 = 0

#    if persistent.patch_on and persistent.patchFile_i_on:
#        $ persistent.patch_installed = True
#    else:
#        $ persistent.patch_installed = False


    return

#init -3 python:
#    persistent.patch_installed = False
#    persistent.patch_enabled = False

#init -1 python:
#    if not persistent.patch_installed:
#        persistent.patreonsafe = True

#    elif persistent.patch_installed and persistent.patch_enabled:
#        persistent.patreonsafe = False

init -1 python:
    persistent.patreonsafe = True

label start:

    # This defines the items.
    python:
        inventory = NewInventory()
        player = NewPlayer("Ryan", 100)
        ### consumable
        chocolate = NewItem("Chocolate", consumable=True, image="images/interface_images/inventory_images/inv_chocolate.png", amount=0, cost=0)
        giftcard = NewItem("Gift Card", consumable=True, image="images/interface_images/inventory_images/inv_giftcard.png", amount=0, cost=0)
        flowers = NewItem("Flowers", consumable=True, image="images/interface_images/inventory_images/inv_flowers.png", amount=0, cost=0)
        melatonin = NewItem("Melatonin", consumable=True, image="images/interface_images/inventory_images/inv_melatonin.png", amount=0, cost=0)
        spycam = NewItem("Spy-cam", consumable=True, image="images/interface_images/inventory_images/inv_spycam.png", amount=0, cost=0)
        ### permanent
        camera = NewItem("Camera", permanent=True, image="images/interface_images/inventory_images/inv_camera.png", amount=0, cost=0)
        green_screen = NewItem("Green screen", permanent=True, image="images/interface_images/inventory_images/inv_green_screen.png", amount=0, cost=0)
        pro_lights = NewItem("Pro lights", permanent=True, image="images/interface_images/inventory_images/inv_pro_lights.png", amount=0, cost=0)
        ball_gag = NewItem("Ball Gag", permanent=True, image="images/interface_images/inventory_images/inv_ball_gag.png", amount=0, cost=0)
        ### accessories for images
        camera_accessories_1 = NewItem("DSLR Lenses", accessories=True, image="images/interface_images/inventory_images/inv_camera_accessories_1.png", amount=0, cost=0)
        camera_accessories_2 = NewItem("DSLR Rubber Eyepiece", accessories=True, image="images/interface_images/inventory_images/inv_camera_accessories_2.png", amount=0, cost=0)
        camera_accessories_3 = NewItem("DSLR Hand Grip Wrist Strap", accessories=True, image="images/interface_images/inventory_images/inv_camera_accessories_3.png", amount=0, cost=0)
        camera_accessories_4 = NewItem("DSLR Ring Flash", accessories=True, image="images/interface_images/inventory_images/inv_camera_accessories_4.png", amount=0, cost=0)
        camera_accessories_5 = NewItem("DSLR Camera Professional Tripod & Monopod", accessories=True, image="images/interface_images/inventory_images/inv_camera_accessories_5.png", amount=0, cost=0)
        ### accessories for films
        camera_accessories_6 = NewItem("DSLR Microphone", accessories=True, image="images/interface_images/inventory_images/inv_camera_accessories_6.png", amount=0, cost=0)
        camera_accessories_7 = NewItem("DSLR Video Stabilizer", accessories=True, image="images/interface_images/inventory_images/inv_camera_accessories_7.png", amount=0, cost=0)
        camera_accessories_8 = NewItem("DSLR Shoulder Rig Pro", accessories=True, image="images/interface_images/inventory_images/inv_camera_accessories_8.png", amount=0, cost=0)
        ### cosplay outfits
        cosplay_outfit_space_01 = NewItem("Cosplay outfit - Space 01", outfit=True, image="images/interface_images/inventory_images/inv_Cosplay_Outfit_Space_1.png", amount=0, cost=0)
        cosplay_outfit_space_02 = NewItem("Cosplay outfit - Space 02", outfit=True, image="images/interface_images/inventory_images/inv_Cosplay_Outfit_Space_2.png", amount=0, cost=0)
        jacky_bikini_01 = NewItem("Jacky's bikini 01", outfit=True, image="images/interface_images/inventory_images/inv_Jacky_bikini_1.png", amount=0, cost=0)
        ### books
        ph_book1 = NewItem("Perry Hotter Book 1", permanent=True, book=True, image="images/interface_images/inventory_images/inv_ph_book1.png", amount=0, cost=0)
        ph_book2 = NewItem("Perry Hotter Book 2", permanent=True, book=True, image="images/interface_images/inventory_images/inv_ph_book2.png", amount=0, cost=0)
        ph_book3 = NewItem("Perry Hotter Book 3", permanent=True, book=True, image="images/interface_images/inventory_images/inv_ph_book3.png", amount=0, cost=0)
        #add items to the initial inventory:
        #inventory.add(chocolate)
        #inventory.add(giftcard)
        #inventory.add(flowers)
        #inventory.add(melatonin)
        #inventory.add(spycam)

    #$ ryan = "Ryan"
    $ timeofdaycounter = 1
    $ momaffection = 5
    $ laurenaffection = 3
    $ sidneyaffection = 0
    $ auntaffection = 0
    $ cousinaffection = 0
    $ momsubmission = 0
    $ laurensubmission = 0
    $ sidneysubmission = 0
    $ auntsubmission = 0
    $ cousinsubmission = 0
    $ money = 0
    $ momprogress = 1
    $ laurenprogress = 1
    $ sidneyprogress = 1
    $ auntprogress = 1
    $ cousinprogress = 1
    $ progress = 1
    $ momlibido = 0
    $ laurenlibido = 0
    $ sidneylibido = 0
    $ auntlibido = 0
    $ cousinlibido = 0
    $ momrespect = 0
    $ laurenrespect = 0
    $ sidneyrespect = 0
    $ auntrespect = 0
    $ cousinrespect = 0
    $ momanger = 0
    $ laurenanger = 0
    $ sidneyanger = 0
    $ auntanger = 0
    $ cousinanger = 0
    $ foundlaurenkey = 0
    $ laurenbedroomprogress = 1
    $ schoolprogress = 1
    $ lectureprogress = 1
    $ momfirstmorning = False
    $ laurenfirstmorning = False
    $ firstdinner = False
    $ stripstay = False
    $ fuckfamilyscheme = False
    $ laurennight = False
    $ momnight = False
    $ firsttimeshopping = False
    $ gavelaurengift = False
    $ gavesidneygift = False
    $ gavemomgift = False
    $ almostmeltdown = False
    $ laurenangrytv = False
    $ tvfirsttimelauren = False
    $ ntrcontent = False
    $ firstntrblowjob = False
    $ momgotobathroom = False
    $ sawsidneychanging = False
    $ caught_by_sidney = False
    $ picturesofsidney = False
    $ tookmelatonin = False
    $ failedsneakattempt = False
    $ boughtmelatonin = False
    $ liedaboutmoney = False
    $ momatclub = False
    $ sawmomstripping = False
    $ caughtattheclubagain = False
    $ caughtattheclubagain01 = False
    $ laurenfingered = False
    $ chatwithsidney = False
    $ spycaminbath = False
    $ spycamlaurenmbatebath = False
    $ spiedlaurenbathroom = False
    $ spycamlaurenshower = False
    $ spiedsidneybathroom = False
    $ spycamsidneymbatebath = False
    $ spycamsidneyshower = False
    $ spiedmombathroom = False
    $ spycammommbatebath = False
    $ spycammomshower = False
    $ spycaminlaurenroom = False
    $ laurenmbateonspycam = False
    $ sawlaurensquirt = False
    $ sidneymbateonspycam = False
    $ spycaminmomroom = False
    $ mommbateonspycam = False
    $ sidneymakingcosplay = False
    $ picsareposted = False
    $ forcedntrevents = 0
    $ clubcounter = 1
    $ picsarepostedcounter = 0
    $ cosplayoutfitcounter = 0
    $ familyofsquirters = 1
    $ shampoobottle = 0
    $ dadpictureprogress = 0
    $ mompictureprogress = 0
    $ sidneypictureprogress = 0
    $ laurenpictureprogress = 0
    $ ryanpictureprogress = 0
    $ daycounter = 6
    $ weekcounter = 1
    $ futchocolate = 0
    $ futgiftcard = 0
    $ futflowers = 0
    $ futmelatonin = 0
    $ futspycam = 0
    $ futgreen_screen = 0
    $ futpro_lights = 0
    $ futcamera = 0
    $ futaccessories_1 = 0
    $ futaccessories_2 = 0
    $ futaccessories_3 = 0
    $ futaccessories_4 = 0
    $ futaccessories_5 = 0
    $ futaccessories_6 = 0
    $ futaccessories_7 = 0
    $ futaccessories_8 = 0
    $ futj_bikini_1 = 0
    $ fut_ball_gag = 0
    $ invchocolate = 0
    $ invgiftcard = 0
    $ invflowers = 0
    $ invmelatonin = 0
    $ invspycam = 0
    $ invgreen_screen = 0
    $ invpro_lights = 0
    $ invcamera = 0
    $ invaccessories_1 = 0
    $ invaccessories_2 = 0
    $ invaccessories_3 = 0
    $ invaccessories_4 = 0
    $ invaccessories_5 = 0
    $ invaccessories_6 = 0
    $ invaccessories_7 = 0
    $ invaccessories_8 = 0
    $ invj_bikini_1 = 0
    $ invball_gag = 0
    $ invph_book1 = 0
    $ invph_book2 = 0
    $ invph_book3 = 0
    $ sidneyfingerlaurenprogress = 1
    $ memepage = 1
    $ deliverymoney = 1
    $ ntr_club_pic_01 = False
    $ gal_cosplay_items_01 = False
    scene bg SleepBlack
    $ renpy.pause (1.5, hard=True)

    call screen safewarningintromap

label truestart:
    if renpy.loadable("Patreon_$5_Gallery/D.S.Mod.rpyc"):
        $ persistent.mod_on = True
    else:
        $ persistent.mod_on = False
    if not persistent.patch_on:
        $ persistent.patreonsafe = True
    else:
        $ persistent.patreonsafe = False
    scene bg SleepBlack
    $ renpy.pause (1.5, hard=True)
    scene bg Intro01
    with fade
    $ renpy.pause (2.5, hard=True)
    scene bg SleepBlack
    with fade
    $ renpy.pause (1.0, hard=True)
    scene bg TitleWAttributions
    with fade
    $ renpy.pause (5.5, hard=True)
    scene bg SleepBlack
    if renpy.loadable("Patreon_$5_Gallery/D.S.Mod.rpy"):
        jump change_name_patreon
    else:
        jump skip_game

label skip_game:
    "If this is the first time you've ever played this game, we highly recommend that you watch the tutorial."
    menu:
        "Would you like to see the tutorial?"
        "Yes.":
            jump tutorial
        "No.":
            "Good luck!  I sure hope you know what you're doing."
    "For players who have already played AFV, we offer the option to skip the game's introduction. This includes the events that set the premise of the game in motion."
    menu skip:
        "Skip to the end of v0.01b":
            menu:
                "Chose your route!"
                "Loyalty route":
                    $ timeofdaycounter = 1
                    $ momaffection = 10
                    $ laurenaffection = 7
                    $ sidneyaffection = 0
                    $ auntaffection = 0
                    $ cousinaffection = 0
                    $ momsubmission = 5
                    $ laurensubmission = 5
                    $ sidneysubmission = 1
                    $ auntsubmission = 0
                    $ cousinsubmission = 0
                    $ money = 1000
                    $ momprogress = 2
                    $ laurenprogress = 2
                    $ sidneyprogress = 1
                    $ auntprogress = 1
                    $ cousinprogress = 1
                    $ progress = 7
                    $ momlibido = 9
                    $ laurenlibido = 9
                    $ sidneylibido = 5
                    $ auntlibido = 0
                    $ cousinlibido = 0
                    $ momrespect = 5
                    $ laurenrespect = 0
                    $ sidneyrespect = 1
                    $ auntrespect = 0
                    $ cousinrespect = 0
                    $ momanger = 0
                    $ laurenanger = 0
                    $ sidneyanger = 0
                    $ auntanger = 0
                    $ cousinanger = 0
                    $ foundlaurenkey = 0
                    $ laurenbedroomprogress = 2
                    $ schoolprogress = 2
                    $ lectureprogress = 2
                    $ momfirstmorning = True
                    $ laurenfirstmorning = True
                    $ firstdinner = True
                    $ stripstay = False
                    $ fuckfamilyscheme = True
                    $ laurennight = False
                    $ momnight = False
                    $ firsttimeshopping = True
                    $ gavelaurengift = False
                    $ gavesidneygift = False
                    $ gavemomgift = False
                    $ almostmeltdown = True
                    $ laurenangrytv = False
                    $ tvfirsttimelauren = True
                    $ momgotobathroom = False
                    $ sawsidneychanging = True
                    $ caught_by_sidney = True
                    $ picturesofsidney = True
                    $ tookmelatonin = True
                    $ failedsneakattempt = True
                    $ boughtmelatonin = True
                    $ liedaboutmoney = False
                    $ momatclub = False
                    $ sawmomstripping = False
                    $ caughtattheclubagain = False
                    $ caughtattheclubagain01 = False
                    $ laurenfingered = False
                    $ chatwithsidney = True
                    $ spycaminbath = False
                    $ spycamlaurenmbatebath = False
                    $ spiedlaurenbathroom = False
                    $ spycamlaurenshower = False
                    $ spiedsidnybathroom = False
                    $ spycamsidneymbatebath = False
                    $ spycamsidneyshower = False
                    $ spiedmombathroom = False
                    $ spycammommbatebath = False
                    $ spycammomshower = False
                    $ spycaminlaurenroom = False
                    $ laurenmbateonspycam = False
                    $ sawlaurensquirt = False
                    $ sidneymbateonspycam = False
                    $ spycaminmomroom = False
                    $ mommbateonspycam = False
                    $ sidneymakingcosplay = False
                    $ picsareposted = False
                    $ forcedntrevents = 0
                    $ clubcounter = 1
                    $ picsarepostedcounter = 0
                    $ cosplayoutfitcounter = 0
                    $ familyofsquirters = 1
                    $ shampoobottle = 0
                    $ dadpictureprogress = 2
                    $ mompictureprogress = 5
                    $ sidneypictureprogress = 8
                    $ laurenpictureprogress = 8
                    $ ryanpictureprogress = 1
                    $ daycounter = 6
                    $ weekcounter = 2
                    $ futchocolate = 0
                    $ futgiftcard = 0
                    $ futflowers = 0
                    $ futmelatonin = 0
                    $ futspycam = 0
                    $ futgreen_screen = 0
                    $ futpro_lights = 0
                    $ futcamera = 0
                    $ futaccessories_1 = 0
                    $ futaccessories_2 = 0
                    $ futaccessories_3 = 0
                    $ futaccessories_4 = 0
                    $ futaccessories_5 = 0
                    $ futaccessories_6 = 0
                    $ futaccessories_7 = 0
                    $ futaccessories_8 = 0
                    $ futj_bikini_1 = 0
                    $ fut_ball_gag = 0
                    $ invchocolate = 0
                    $ invgiftcard = 0
                    $ invflowers = 0
                    $ invmelatonin = 0
                    $ invspycam = 0
                    $ invgreen_screen = 0
                    $ invpro_lights = 0
                    $ invcamera = 0
                    $ invaccessories_1 = 0
                    $ invaccessories_2 = 0
                    $ invaccessories_3 = 0
                    $ invaccessories_4 = 0
                    $ invaccessories_5 = 0
                    $ invaccessories_6 = 0
                    $ invaccessories_7 = 0
                    $ invaccessories_8 = 0
                    $ invj_bikini_1 = 0
                    $ invball_gag = 0
                    $ sidneyfingerlaurenprogress = 4
                    $ memepage = 1
                    $ deliverymoney = 1

                    $ hardnlong_searched =True

                    $ persistent.gal_mom_1 = True
                    $ persistent.gal_mom_2 = True

                    $ persistent.gal_Lauren_1 = True
                    $ persistent.gal_Lauren_2 = True

                    $ persistent.gal_Sidney_1 = True
                    #$ persistent.gal_Sidney_1 = True

                    $ persistent.gal_harem_1 = True

                    play music Honey fadein 2.5
                    jump myroom
                "NTR route":
                    $ timeofdaycounter = 1
                    $ momaffection = 10
                    $ laurenaffection = 7
                    $ sidneyaffection = 0
                    $ auntaffection = 0
                    $ cousinaffection = 0
                    $ momsubmission = 5
                    $ laurensubmission = 5
                    $ sidneysubmission = 1
                    $ auntsubmission = 0
                    $ cousinsubmission = 0
                    $ money = 1000
                    $ momprogress = 2
                    $ laurenprogress = 2
                    $ sidneyprogress = 1
                    $ auntprogress = 1
                    $ cousinprogress = 1
                    $ progress = 7
                    $ momlibido = 9
                    $ laurenlibido = 9
                    $ sidneylibido = 5
                    $ auntlibido = 0
                    $ cousinlibido = 0
                    $ momrespect = 5
                    $ laurenrespect = 0
                    $ sidneyrespect = 1
                    $ auntrespect = 0
                    $ cousinrespect = 0
                    $ momanger = 0
                    $ laurenanger = 0
                    $ sidneyanger = 0
                    $ auntanger = 0
                    $ cousinanger = 0
                    $ foundlaurenkey = 0
                    $ laurenbedroomprogress = 2
                    $ schoolprogress = 2
                    $ lectureprogress = 2
                    $ momfirstmorning = True
                    $ laurenfirstmorning = True
                    $ firstdinner = True
                    $ stripstay = False
                    $ fuckfamilyscheme = True
                    $ laurennight = False
                    $ momnight = False
                    $ firsttimeshopping = True
                    $ gavelaurengift = False
                    $ gavesidneygift = False
                    $ gavemomgift = False
                    $ almostmeltdown = True
                    $ laurenangrytv = False
                    $ tvfirsttimelauren = True
                    $ ntrcontent = True #Player will need to choose at beginning
                    $ firstntrblowjob = True      #if ntrcontent == True
                    $ momgotobathroom = False
                    $ sawsidneychanging = True
                    $ caught_by_sidney = True
                    $ picturesofsidney = True
                    $ tookmelatonin = True
                    $ failedsneakattempt = True
                    $ boughtmelatonin = True
                    $ liedaboutmoney = False
                    $ momatclub = False
                    $ sawmomstripping = False
                    $ caughtattheclubagain = False
                    $ caughtattheclubagain01 = False
                    $ laurenfingered = False
                    $ chatwithsidney = True
                    $ spycaminbath = False
                    $ spycamlaurenmbatebath = False
                    $ spiedlaurenbathroom = False
                    $ spycamlaurenshower = False
                    $ spiedsidnybathroom = False
                    $ spycamsidneymbatebath = False
                    $ spycamsidneyshower = False
                    $ spiedmombathroom = False
                    $ spycammommbatebath = False
                    $ spycammomshower = False
                    $ spycaminlaurenroom = False
                    $ laurenmbateonspycam = False
                    $ sawlaurensquirt = False
                    $ sidneymbateonspycam = False
                    $ spycaminmomroom = False
                    $ mommbateonspycam = False
                    $ sidneymakingcosplay = False
                    $ forcedntrevents = 0
                    $ clubcounter = 1
                    $ picsareposted = False
                    $ picsarepostedcounter = 0
                    $ cosplayoutfitcounter = 0
                    $ familyofsquirters = 1
                    $ shampoobottle = 0
                    $ dadpictureprogress = 2
                    $ mompictureprogress = 5
                    $ sidneypictureprogress = 8
                    $ laurenpictureprogress = 8
                    $ ryanpictureprogress = 1
                    $ daycounter = 6
                    $ weekcounter = 2
                    $ futchocolate = 0
                    $ futgiftcard = 0
                    $ futflowers = 0
                    $ futmelatonin = 0
                    $ futspycam = 0
                    $ futgreen_screen = 0
                    $ futpro_lights = 0
                    $ futcamera = 0
                    $ futaccessories_1 = 0
                    $ futaccessories_2 = 0
                    $ futaccessories_3 = 0
                    $ futaccessories_4 = 0
                    $ futaccessories_5 = 0
                    $ futaccessories_6 = 0
                    $ futaccessories_7 = 0
                    $ futaccessories_8 = 0
                    $ futj_bikini_1 = 0
                    $ fut_ball_gag = 0
                    $ invchocolate = 0
                    $ invgiftcard = 0
                    $ invflowers = 0
                    $ invmelatonin = 0
                    $ invspycam = 0
                    $ invgreen_screen = 0
                    $ invpro_lights = 0
                    $ invcamera = 0
                    $ invaccessories_1 = 0
                    $ invaccessories_2 = 0
                    $ invaccessories_3 = 0
                    $ invaccessories_4 = 0
                    $ invaccessories_5 = 0
                    $ invaccessories_6 = 0
                    $ invaccessories_7 = 0
                    $ invaccessories_8 = 0
                    $ invj_bikini_1 = 0
                    $ invball_gag = 0
                    $ sidneyfingerlaurenprogress = 4
                    $ memepage = 1
                    $ deliverymoney = 1

                    $ hardnlong_searched =True

                    $ persistent.gal_mom_1 = True
                    $ persistent.gal_mom_2 = True

                    $ persistent.gal_Lauren_1 = True
                    $ persistent.gal_Lauren_2 = True

                    $ persistent.gal_Sidney_1 = True
                    #$ persistent.gal_Sidney_1 = True

                    $ persistent.gal_harem_1 = True

                    $ persistent.gal_NTR_1 = True

                    play music Honey fadein 2.5
                    jump myroom
                "Back":
                    jump skip
        "Don't skip the game":
            jump gamestart

label gamestart:

    #if persistent.patreonsafe == True:
    #    $ Mom = "Jacky"
    #    $ mom = "Jacky"
    #    $ mom_name = "Jacky"
    #    $ Dad = "Tony"
    #    $ dad = "Tony"
    #    $ dad_name = "Tony"
    #    $ uncle = "Bobby"

    #elif persistent.patreonsafe == False:
    #    $ Mom = "Mom"
    #    $ mom = "mom"
    #    $ mom_name = "Jacky"
    #    $ Dad = "Dad"
    #    $ dad = "dad"
    #    $ dad_name = "Tony"
    #    $ uncle = "Uncle Bobby"

    scene bg SleepBlack
    with fade
    play music Honey fadein 2.5
    M "[ryan], wake up!"
    scene bg BlurryWhite
    with fade
    scene bg SleepBlack
    with fade
    M "[upper_ryan], WAKE UP!"
    scene bg BlurryWhite
    with fade
    scene bg SleepBlack
    with fade
    M "WAKE UP!!!"
    scene bg BlurryWhite
    with fade
    with vpunch
    with hpunch
    R "Huh..."
    R "What?..."
    R "What is it?..."
    scene bg WakeUp01
    with fade
    R "What time is it?"
    M "It's only 5:30 AM.... sorry to wake you so early."
    R "Uhhh.... Isn't is Saturday?..."
    M "I know honey, but your no account, worthless father is on the phone for you..."
    scene bg Wakeup02
    with dissolve
    M "It's pretty important..."
    M "He's calling from jail!"
    R "WHAT?!"
    M "Oh, and honey?"
    R ".... Yeah?..."
    M ".... Could you maybe wear more to bed?..."
    M "Or at least cover yourself while I'm in here..."
    scene bg CoverUp01
    with dissolve
    M "I know it's just morning wood..."
    M "But what if one of your sisters walked in on you like this?"
    R "I'd tell them to get the fuck out of my room!"
    scene bg CoverUp02
    with dissolve
    M "Language please!"
    R "Sorry!"
    M "Here.... talk to Dad!"
    menu:
        "Peek down her robe":
            jump peek

        "Gross!! That's just weird!":
            jump gross

label peek:
    scene bg MomsTitts01
    with fade
    play music SexMusic
    RT "{i}Why is she telling me to cover up?.... {/i}"
    RT "{i}Mom's boobs are practically bursting out of her robe.... {/i}"
    RT "{i}Good thing I don't think of her like that.... {/i}"
    RT "{i}.... hmmm.... {/i}"
    RT "{i}.... aAAHH! Get out of my head Satan!{/i}"

    MT "{i}Did my boy just look down my robe?.... {/i}"
    MT "{i}Here I am lecturing him to cover up himself while my tits are halfway out.... {/i}"
    MT "{i}.... hmmm.... {p}I wonder if he'd have gotten hard if he wasn't already?.... {/i}"

    MT "{i}He is pretty well endowed... {/i}{p}{i}He doesn't take after his father... {/i}{p}{i}He must take after my dad... {/i}"

    MT "{i}.... hmmm.... {/i}"

    MT "{i}.... AAAHH!{p} Why am I thinking about my dads and sons penises?{p} Get out of my head Satan!.... {/i}"

    scene bg MomThinkingRobe01
    with fade
    M "Uhhh.... I'm going to go. Bring me my phone to the kitchen when you're done."
    RT "{i}SHIT! She saw me staring!{p} That was stupid.... {p} I need to go to church!{/i}"
    "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
    "{i}{b}\"Mom's Affection -1\"{/b}{/i}"
    $ momlibido += 1
    $ momaffection -= 1
    play music Honey
    jump main

label gross:
    scene bg MomWorriedRobe01
    with fade
    M "Ok, well I'm going to go.{p} Bring my phone to the kitchen when you're done."
    jump main

label main:
    scene bg OnPhoneBed01
    with fade
    R "Dad! Are you ok? Why are you in jail?!"
    D "Listen to me carefully son, I don't have a lot of time and this is my one phone call."
    R "Shouldn't you have called your lawyer?"
    D "JUST SHUT UP AND LISTEN!..."
    D "I need you to go to my warehouse this morning. Uncle Bobby is going to be there, and he's going to tell you everything you need to know..."
    D "Now I can't stress to you how important it is that you go and see him, and do exactly what he tells you to do..."
    D "Our family could be in some really bad trouble if you don't take care of this for me."
    scene bg OnPhone02
    with dissolve
    R "Don't worry Dad, I'll go over there as soon as I can."
    D "Thank you for this son!"
    R "Of course Dad! Are you going to be ok?"
    D ".... I might have to spend a good while in prison..."
    D "I need you to take care of this for me..."
    D "You're the man of the house now..."
    D "I know this is a lot to take in, but you've got to step up..."
    D "Our family's safety and success are now in your hands..."
    D "So don't fuck it up!"
    "\"{b}CLICK{/b}\""
    jump myroom
    with fade(2)

############  RYAN'S ROOM  ##########  RYAN'S ROOM  #############  RYAN'S ROOM  #############  RYAN'S ROOM  ######################################################

label myroom:
    if daycounter >= 4 and timeofdaycounter == 4 and progress == 4 and weekcounter == 2:
        scene bg RyansRoom01
        L "[ryan] can you come in to the lounge and help me!"
        scene bg LaurenRemoteSearch01
        with fade
        play music SexMusic
        RT "{i}What did I just walk in on? It's like Mom and Lauren are purposely trying to be cock-teases lately.{/i}"
        RT "{i}Has it always been like this, and now I'm just starting to notice? I'm sure I'm reading way more into this than I should.{/i}"
        menu:
            "Lauren, what the hell are you doing?":
                $ persistent.gal_Lauren_2 = True
                scene bg LaurenRemoteSearch02
                with dissolve
                L "I'm looking for the TV remote."
                L "Do you know where it is?"
                R "I'm sorry I haven't seen it."
                $ progress = 5
                L "Well, you were the last one to watch TV, so you must be the one who lost it."
                L "The least you can do is help me find it. Bend down here and help me look."
                scene bg LaurenRemoteSearch03
                with fade
                RT "{i}Look for the remote?{/i}"
                RT "{i}How am I supposed to concentrate on anything else besides this view right in front of me?{/i}"
                RT "{i}Hmmm.... I wonder.... {/i}"
                scene bg LaurenRemoteSearch04
                with fade
                RT "{i}Oh my God, I can!{/i}"
                RT "{i}I can kind of smell her pussy from this close.{/i}"
                RT "{i}I've never smelled a pussy before, I kind of like it.{/i}"
                RT "{i}I've got to get closer.{/i}"
                scene bg LaurenRemoteSearch05
                with dissolve
                RT "{i}Wow! That smells incredible!{/i}"
                RT "{i}I wish I could taste it.{/i}"
                RT "{i}It just turns me on so much!{/i}"
                L "Well, I don't see the remote in this corner, I'm coming back."
                R "Wait!"
                scene bg LaurenRemoteSearch06
                with dissolve
                with vpunch
                R "Mmphh..."
                scene bg LaurenRemoteSearch07
                with fade
                scene bg LaurenRemoteSearch06
                with fade
                scene bg LaurenRemoteSearch07
                with fade
                L "[ryan]?.... Is that your face in my ass?"
                L "[ryan]?..."
                "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                $ laurenlibido += 1
                scene bg LaurenRemoteSearch06
                with fade
                R "Uhh.... yeah.... sorry. I was just looking for the remote under this couch cushion, and didn't realize I was that close to you until you backed up."
                RT "{i}Oh my God, it smells so good I can almost taste it.{/i}"
                L "Well, would you mind removing it?"
                R "Oh yeah.... of course."
                if laurenanger >= 1:
                    scene bg LaurenWatchTV01
                    with fade
                    L "Well, that was a little awkward!"
                    R "Only if you make it. It was just an accident."
                    L "I guess."
                    R "So do you want to watch some TV?"
                    $ laurenangrytv = True
                    L "I'm still pissed off at you remember."
                    L "Ugghh.... I'm just going to go to my room."
                    scene bg FamilyRoom01
                    with fade
                    play music Honey
                    $ screen_on = "loungemap"
                    call screen loungemap
                else:
                    scene bg LaurenWatchTV02
                    with fade
                    R "Sorry, that was a little awkward!"
                    L "Only if you let it be, it was just an accident."
                    R "Yeah.... I guess so."
                    L "So do you want to watch TV with me?"
                    R "Ok, what are you watching?"
                    L "I'm just starting season one of \"Game of Thots\"."
                    L "Have you been following this show?"
                    R "No I've just seen the first episode."
                    scene bg LaurenWatchTV03
                    with dissolve
                    L "Awesome! We can watch the series together!"
                    L "All my friends love it!"
                    scene bg LaurenWatchTV06
                    with dissolve
                    RT "{i}I wonder if this is a little too explicit for Lauren?{/i}"
                    scene bg LaurenWatchTV05
                    with fade
                    RT "{i}Wow! I can't believe what they can get away with on TV anymore! This is awesome!{/i}"
                    scene bg LaurenWatchTV04
                    with fade
                    R "Man, that episode was intense! Lauren are you ok? You seem a little flushed."
                    L "Oh yeah, I'm fine. I was just a little surprised at that brother sister sex scene."
                    L "This show almost makes incest seem normal, like it's no big deal or something."
                    R "Yeah, well incest is only bad when society says it's bad. There have been lots of times in history where it was perfectly accepted."
                    L "I wouldn't say lots of times."
                    R "Well, not a ton, but to me it's like being gay. If two people are in love with each other, why do people think they have the right to tell them they can't be in love?"
                    L "I don't know it just seems really weird."
                    R "Only because you've been told all your life it's weird."
                    LT "{i}Hmmmm.... I'll have to think about that one.... {/i}"
                    $ laurenlibido += 1
                    $ laurenaffection += 1
                    "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                    $ timeofdaycounter += 1
                    $ tvfirsttimelauren = True
                    play music Honey
                    jump loungenightweekend
    if timeofdaycounter == 1:
        jump myroomearlymorning
    elif timeofdaycounter == 2:
        jump myroommorning
    elif timeofdaycounter == 3:
        jump myroomafternoon
    elif timeofdaycounter == 4:
        jump myroomevening
    else:
        jump myroomnight

label myroomearlymorning:
    if daycounter >= 6:
        jump myroomearlymorningweekend
    else:
        scene bg RyansRoom01
        with fade
        $ screen_on = "ryanmap"
        call screen ryanmap

label myroomearlymorningweekend:
    scene bg RyansRoom01
    with fade
    $ screen_on = "ryanmap"
    call screen ryanmap

label myroommorning:
    if daycounter >= 6:
        jump myroommorningweekend
    else:
        scene bg RyansRoom01
        with fade
        $ screen_on = "ryanmap"
        call screen ryanmap

label myroommorningweekend:
    scene bg RyansRoom01
    with fade
    $ screen_on = "ryanmap"
    call screen ryanmap

label myroomafternoon:
    if daycounter >= 6:
        jump myroomafternoonweekend
    else:
        scene bg RyansRoom01
        with fade
        $ screen_on = "ryanmap"
        call screen ryanmap

label myroomafternoonweekend:
    scene bg RyansRoom01
    with fade
    $ screen_on = "ryanmap"
    call screen ryanmap

label myroomevening:
    if daycounter >= 6:
        jump myroomeveningweekend
    elif inventory.has_item(ph_book1) and not read_book3:
        jump ph_reading_time
    elif first_book_owned and not read_book3:
        jump ph_reading_time
    else:
        scene bg RyansRoom01
        with fade
        $ screen_on = "ryanmap"
        call screen ryanmap

label myroomeveningweekend:
    scene bg RyansRoom01
    with fade
    $ screen_on = "ryanmap"
    call screen ryanmap

label myroomnight:
    if sidneys_working:
        scene bg MyRoomNight
        with fade
        RT "{i}My bed looks lonely without Sidney in it.{/i}"
        RT "{i}I hope she's ok at the club tonight.{/i}"
        $ screen_on = "ryanmapnight"
        call screen ryanmapnight

    if daycounter >= 6:
        jump myroomnightweekend
    if sidneyfingerlaurenprogress >= 5:
        scene bg MyRoomNightWSidney
        with fade
        $ screen_on = "ryanwithsidneymap"
        call screen ryanwithsidneymap
    else:
        scene bg MyRoomNight
        with fade
        $ screen_on = "ryanmapnight"
        call screen ryanmapnight

label myroomnightweekend:
    if sidneyfingerlaurenprogress >= 5:
        scene bg MyRoomNightWSidney
        with fade
        $ screen_on = "ryanwithsidneymap"
        call screen ryanwithsidneymap
    else:
        scene bg MyRoomNight
        with fade
        $ screen_on = "ryanmapnight"
        call screen ryanmapnight

label computer:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    if likes >= 1000 and  it_s_over_1000 == False:
        $ it_s_over_1000 = True
        if inventory.inv_amount(green_screen) == 1 and photoshoot_2 and it_s_over_1000: #>= 1000:
            $ gal_supporters = True
            play music Honey
            scene bg SleepBlack
            with fade
            scene bg CosplayWarehouse20
            with fade
            RT "{i}WOW! We reached 1000 likes.... {p}And CosplayHeaven just gave us access to a new feature.{/i}"
            RT "{i}It seems that we can increase our revenues if people decide to become our supporters and we'll get $[var_earnings_per_supporters] for each one.{/i}"
            RT "{i}Now it's the perfect time to use those lewd pictures I took of Lauren.{/i}"
            RT "{i}To bad that this is a monthly income, but still we can get more money and maybe I can use this to corrupt Lauren more.{/i}"
            RT "{i}Let's start uploading those pictures now.... {p}and click submit.... {p}and now we just wait to see if anyone likes them so much that they'll become our supporter.{/i}"
            RT "{i}Hmmm.... let me see how the page turned out before I go.{/i}"
            RT "{i}Click.... {p}click.... {p}click.... {/i}"
            scene bg SleepBlack
            with fade
            $ screen_on = "Cosplay_supporters_gallery"
            call screen Cosplay_supporters_gallery
        else:
            pass
    elif picsarepostedcounter == 1 and config_site and htbyd_most_recent == True:
        jump check_for_htbyd_likes
    elif picsarepostedcounter == 1 and config_site and progress <= 10:
        jump checkforlikes
    else:
        scene bg Desktop_login
        RT "{i}I must enter my password to Login!{/i}"
        RT "{i}Ha ha its \"B00Bies123.\"{/i}"
        scene bg Desktop_1
        with fade
        $ screen_on = "desktopcompmap"
        call screen desktopcompmap

label bed:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    if sidneys_working and timeofdaycounter == 5:
        menu:
            "Sleep":
                jump sidneys_home_late
            "Never mind":
                jump myroom
    if timeofdaycounter == 5 and sidneyfingerlaurenprogress >= 5:
        jump sidneysleepswithryan
    if daycounter == 6:
        while timeofdaycounter == 4:
            scene bg RyansRoom01
            RT "{i}I can't waste time right now, the DeCapos will be here any minute.{/i}"
            $ screen_on = "ryanmap"
            call screen ryanmap
        if daycounter == 6:
            while progress >= 4:
                menu:
                    "Memes (Advances time)" if timeofdaycounter <= 4:
                        if start_of_campaign and not campaign_finished and daycounter == 1 and timeofdaycounter == 2:
                            RT "{i}I need to go to school and see how Lauren is doing in the student body election poll.{/i}"
                            jump myroom
                        else:
                            $ memepage = renpy.random.randint(1, 28)
                            $ timeofdaycounter += 1

                            scene bg BlurryWhite

                            if memepage == 1:

                                show Memes01
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 2:

                                show Memes02
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 3:

                                show Memes03
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 4:

                                show Memes04
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 5:

                                show Memes05
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 6:

                                show Memes06
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 7:

                                show Memes07
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 8:

                                show Memes08
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 9:

                                show Memes09
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 10:

                                show Memes10
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 11:

                                show Memes11
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 12:

                                show Memes12
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 13:

                                show Meme13
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 14:

                                show Meme14
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 15:

                                show Meme15
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 16:

                                show Meme16
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 17:

                                show Meme17
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 18:

                                show Meme18
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 19:

                                show Meme19
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 20:

                                show Meme20
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 21:

                                show Meme21
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 22:

                                show Meme22
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 23:

                                show Meme23
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 24:

                                show Meme24
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 25:

                                show Meme25
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 26:

                                show Meme26
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            elif memepage == 27:

                                show Meme27
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom

                            else:

                                show Meme28
                                with fade
                                $ renpy.pause ()
                                scene bg RyansRoom01
                                jump myroom
                    "Sleep":
                        if start_of_campaign and not campaign_finished and daycounter == 1 and timeofdaycounter <= 2:
                            RT "{i}I need to go to school and see how Lauren is doing in the student body election poll.{/i}"
                            jump myroom
                        else:
                            jump sleep
    if progress >= 4:
        menu:
            "Memes (Advances time)" if timeofdaycounter <= 4:
                if start_of_campaign and not campaign_finished and daycounter == 1 and timeofdaycounter == 2:
                    RT "{i}I need to go to school and see how Lauren is doing in the student body election poll.{/i}"
                    jump myroom
                else:
                    $ memepage = renpy.random.randint(1, 28)
                    $ timeofdaycounter += 1

                    scene bg BlurryWhite

                    if memepage == 1:

                        show Memes01
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 2:

                        show Memes02
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 3:

                        show Memes03
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 4:

                        show Memes04
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 5:

                        show Memes05
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 6:

                        show Memes06
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 7:

                        show Memes07
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 8:

                        show Memes08
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 9:

                        show Memes09
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 10:

                        show Memes10
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 11:

                        show Memes11
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 12:

                        show Memes12
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 13:

                        show Meme13
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 14:

                        show Meme14
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 15:

                        show Meme15
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 16:

                        show Meme16
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 17:

                        show Meme17
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 18:

                        show Meme18
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 19:

                        show Meme19
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 20:

                        show Meme20
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 21:

                        show Meme21
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 22:

                        show Meme22
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 23:

                        show Meme23
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 24:

                        show Meme24
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 25:

                        show Meme25
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 26:

                        show Meme26
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    elif memepage == 27:

                        show Meme27
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

                    else:

                        show Meme28
                        with fade
                        $ renpy.pause ()
                        scene bg RyansRoom01
                        jump myroom

            "Sleep":
                if start_of_campaign and not campaign_finished and daycounter == 1 and timeofdaycounter <= 2:
                    RT "{i}I need to go to school and see how Lauren is doing in the student body election poll.{/i}"
                    jump myroom
                else:
                    jump sleep

label sleep:
    if sidneypictureprogress < 2 and daycounter == 5 and progress == 5:
        ### vars for likes
        $ advertising = False
        $ income_output = False
        $ day_likes = 0
        # for supporters gal
        if supporters_month_counter >= 4:
            $ supporters_income_output = False
        if gal_supporters:
            $ supporters_day_count +=1
        if days_until_next_photo_shoot <= 1 and not first_htbyd_shoot:
            $ days_until_next_photo_shoot += 1
        if photoshoot_1:
            $ likes_counter += 1

        $ timeofdaycounter = 4
        $ daycounter = 6
        scene bg SleepBlack
        with fade
        RT "{i}Shit, I have a ton of homework Mom gave me because of all the school I've been missing to work. I better get up.{/i}"
        scene bg RyanHomework01
        with fade
        RT "{i}Oh man, I'm so tired, I am not looking forward to this.{/i}"
        RT "{i}Well, I better get going, so I don't have to spend the entire day doing homework.{/i}"
        scene bg RyanHomework02
        with fade
        RT "{i}Ok, so the assignment is to write a paper on how the Greek play Oedipus Rex influenced Sigmund Freud's theory on the Oedipal complex.{/i}"
        RT "{i}What the hell is an Oedipal complex? Guess I better get reading.{/i}"
        RT "{i}Ok, here's the cliffnotes version.... so the premise of the Greek play Oedipus Rex is that .... {/i}"
        scene bg RyanHomework03
        with dissolve
        RT "{i}.... {/i}"
        scene bg SleepBlack
        with fade
        M "[ryan]!.... Hey, [ryan].... are you in you in your room?"
        scene bg RyanHomework03
        with fade
        M "Honey, come down and eat with us."
        scene bg RyanHomework04
        with fade
        R "Ok Mom, I'll be right there."
        scene bg Kitchen01
        with fade
        M "Honey, come sit down. We're having pizza for dinner."
        menu:
            "Go sit down":
                scene bg SidneyComesHome01
                with fade
                M "I hope you guys are hungry."
                $ progress = 6
                menu:
                    "Ask Mom about her day":
                        "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                        $ momaffection += 1
                        M "Oh, my day was fine. Did you finish the extra homework on Oedipus I gave you___"
                        S "AAHHAAHHAHHHEMMMMM..."
                        jump sidneyenters
                    "Ask Lauren about her day":
                        "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                        $ laurenaffection += 1
                        L "OMG [ryan].... so Kenzie was so funny today after PE she was all like___"
                        S "AAHHAAHHAHHHEMMMMM..."
                        jump sidneyenters
    if timeofdaycounter == 5:
        while fuckfamilyscheme == False:
            ### vars for likes
            $ advertising = False
            $ income_output = False
            $ day_likes = 0
            # for supporters gal
            if supporters_month_counter >= 4:
                $ supporters_income_output = False
            if gal_supporters:
                $ supporters_day_count +=1
            if days_until_next_photo_shoot <= 1 and not first_htbyd_shoot:
                $ days_until_next_photo_shoot += 1
            if photoshoot_1:
                $ likes_counter += 1

            scene bg MyRoomNight
            RT "{i}I hope Lauren was ok on her own, I should just go check on her before I go to bed.{/i}"
            $ screen_on = "ryanmapnight"
            call screen ryanmapnight
    if timeofdaycounter == 5:
        while daycounter == 7:
            if sidneymakingcosplay == True:
                $ cosplayoutfitcounter += 1
            else:
                pass
            if picsareposted == True:
                $ picsarepostedcounter += 1
            else:
                pass
            ### vars for likes
            $ advertising = False
            $ income_output = False
            $ day_likes = 0
            # for supporters gal
            if supporters_month_counter >= 4:
                $ supporters_income_output = False
            if gal_supporters:
                $ supporters_month_counter += 1
                $ supporters_day_count +=1
            if days_until_next_photo_shoot <= 1 and not first_htbyd_shoot:
                $ days_until_next_photo_shoot += 1
            if photoshoot_1:
                $ likes_counter += 1
            if laurenpictureprogress >= 10:
                $ aunt_visit_counter += 1
            if sidney_worked_late == 2:
                $ sidney_worked_late = 0
            if sidney_worked_late == 1:
                $ sidney_worked_late = 2
            if club_fun_counter == 2:
                $ club_fun_counter = 0
            if club_fun_counter == 1:
                $ club_fun_counter = 2
            if sixty_nined_bfast == 2:
                $ sixty_nined_bfast = 0
            if sixty_nined_bfast == 1:
                $ sixty_nined_bfast = 2
            if start_of_campaign and not campaign_finished:
                $ posters_bulbs = False
                $ posters_bad = False
                $ posters_good = False
                $ posters_dragon = False
                $ posters_me = False
                $ posters_matt = True
            if start_of_campaign and campaign_weeks <= 3:
                $ campaign_weeks += 1
            if inventory.has_item(ball_gag):
                $ ball_gag_owned = True
            $ timeofdaycounter = 1
            $ daycounter = 1
            $ weekcounter += 1
            $ laurennight = False
            $ laurenanger -= 1
            $ momanger -= 1
            $ sidneyanger -= 1
            $ auntanger -= 1
            $ cousinanger -= 1
            $ gavelaurengift = False
            $ gavesidneygift = False
            $ gavemomgift = False
            $ laurenangrytv = False
            $ momgotobathroom = False
            $ momnight = False
            $ sawsidneychanging = False
            $ liedaboutmoney = False
            $ momatclub = False
            $ laurenfingered = False
            $ laurenangrytv = False
            $ spiedlaurenbathroom = False
            $ spiedmombathroom = False
            $ spiedsidneybathroom = False
            $ sawlaurensquirt = False
            $ mm_fuckedtoday = False
            $ weekly_htbyd_complete = False
            $ weekly_wr_complete = False
            $ mom_squirted_today_bedroom = False
            $ sidneys_running = False
            $ sidneys_working = False
            $ visited_sid = False
            $ watched_with_Diaz = False
            $ monday_sid_worked = False
            $ lauren_door_locked = False
            $ daily_truth_counter = 0
            $ daily_dare_counter = 0
            $ truth_told = 0
            $ weekly_htbyd_trigger = False
            $ weekly_htbyd_complete = False
            $ weekly_wr_trigger = False
            $ weekly_wr_complete = False
            $ weekly_hp_trigger = False
            $ weekly_hp_complete = False
            $ saw_aunt_exercise = False
            $ couldnt_resist = False
            $ gaveauntgift = False
            $ gavecuzgift = False
            $ spiedgirlsbathroom = False
            $ spiedmandybathroom = False
            $ spiedauntbathroom = False
            $ visited_mandy_evening = False
            $ spied_mandy_bed = False
            $ played_the_game = False
            $ answered_ph_wrong = False
            $ mandy_spanked = False
            $ lauren_spanked = False
            $ weekly_poster_toggle = False
            $ bought_lauren_swag = False
            $ bought_diaz_votes = False
            $ win_eligible = False
            $ jackoff_week = False
            $ blowjob_week = False
            $ weekly_campaign_meeting = False
            $ campaign_finished_warning = 0
            $ lounge_creampie = False
            jump wakeupryan
        if timeofdaycounter == 5:
            if day_off_counter >= 1:
                $ aunt_day_off = False
                $ day_off_counter = 0
            if aunt_day_off == True:
                $ day_off_counter += 1
            if laurenpictureprogress >= 10:
                $ aunt_visit_counter += 1
            else:
                pass
            if sidneymakingcosplay == True:
                $ cosplayoutfitcounter += 1
            else:
                pass
            if picsareposted == True:
                $ picsarepostedcounter += 1
            else:
                pass
            ### vars for likes
            $ advertising = False
            $ income_output = False
            $ day_likes = 0
            # for supporters gal
            if supporters_month_counter >= 4:
                $ supporters_income_output = False
            if gal_supporters:
                $ supporters_day_count +=1
            if days_until_next_photo_shoot <= 1 and not first_htbyd_shoot:
                $ days_until_next_photo_shoot += 1
            if photoshoot_1:
                $ likes_counter += 1
            if sidney_worked_late == 2:
                $ sidney_worked_late = 0
            if sidney_worked_late == 1:
                $ sidney_worked_late = 2
            if club_fun_counter == 2:
                $ club_fun_counter = 0
            if club_fun_counter == 1:
                $ club_fun_counter = 2
            if sixty_nined_bfast == 2:
                $ sixty_nined_bfast = 0
            if sixty_nined_bfast == 1:
                $ sixty_nined_bfast = 2
            if weekly_wr_trigger == True:
                $ weekly_wr_complete = True
            if weekly_htbyd_trigger == True:
                $ weekly_htbyd_complete = True
            if weekly_hp_trigger == True:
                $ weekly_hp_complete = True
            if posters_good and daycounter <= 5:
                $ school_influence += 3
            if posters_dragon and daycounter <= 5:
                $ school_influence += 1
            if posters_me and daycounter <= 5:
                $ school_influence += 1
            if visits_to_stone >= 4:
                $ persistent.gal_other_girls_2 = True
            if fucked_lauren and campaign_win:
                $ persistent.gal_Lauren_7 = True
            if megan_told_counter >= 1:
                $ persistent.gal_other_girls_3 = True
            if locker_cam_placed:
                $ persistent.gal_Lauren_8 = True
            if mandy_joined:
                $ persistent.gal_harem_5 = True
            if first_train:
                $ persistent.gal_NTR_7 = True
            if diaz_van_counter >= 4:
                $ persistent.gal_other_girls_4 = True
            if inventory.has_item(ball_gag):
                $ ball_gag_owned = True
            $ timeofdaycounter = 1
            $ daycounter += 1
            $ laurennight = False
            $ laurenanger -= 1
            $ momanger -= 1
            $ sidneyanger -= 1
            $ auntanger -= 1
            $ cousinanger -= 1
            $ gavelaurengift = False
            $ gavesidneygift = False
            $ gavemomgift = False
            $ Laurenangrytv = False
            $ momgotobathroom = False
            $ momnight = False
            $ sawsidneychanging = False
            $ momatclub = False
            $ sawmomstripping = False
            $ laurenfingered = False
            $ laurenangrytv = False
            $ spiedlaurenbathroom = False
            $ spiedmombathroom = False
            $ spiedsidneybathroom = False
            $ sawlaurensquirt = False
            $ mm_fuckedtoday = False
            $ mom_squirted_today_bedroom = False
            $ sidneys_running = False
            $ sidneys_working = False
            $ visited_sid = False
            $ watched_with_Diaz = False
            $ monday_sid_worked = False
            $ lauren_door_locked = False
            $ daily_truth_counter = 0
            $ daily_dare_counter = 0
            $ truth_told = 0
            $ saw_aunt_exercise = False
            $ couldnt_resist = False
            $ gaveauntgift = False
            $ gavecuzgift = False
            $ spiedgirlsbathroom = False
            $ spiedmandybathroom = False
            $ spiedauntbathroom = False
            $ visited_mandy_evening = False
            $ spied_mandy_bed = False
            $ played_the_game = False
            $ answered_ph_wrong = False
            $ mandy_spanked = False
            $ lauren_spanked = False
            $ had_campaign_meeting = False
            $ visited_diaz_today = False
            $ sneak_locker_peek = False
            $ daily_megan_fuck = False
            $ propositioned_lauren = False
            $ lounge_creampie = False
            jump wakeupryan


    elif progress >= 4:
        "Are you sure you want to sleep until tomorrow?"
        menu:
            "Yes":
                if daycounter == 7:
                    if sidneys_working:
                        $ timeofdaycounter = 5
                        jump sidneys_home_late
                    if sidneymakingcosplay == True:
                        $ cosplayoutfitcounter += 1
                    else:
                        pass
                    if picsareposted == True:
                        $ picsarepostedcounter += 1
                    else:
                        pass
                    ### vars for likes
                    $ advertising = False
                    $ income_output = False
                    $ day_likes = 0
                    # for supporters gal
                    if supporters_month_counter >= 4:
                        $ supporters_income_output = False
                    if gal_supporters:
                        $ supporters_month_counter += 1
                        $ supporters_day_count +=1
                    if days_until_next_photo_shoot <= 1 and not first_htbyd_shoot:
                        $ days_until_next_photo_shoot += 1
                    if photoshoot_1:
                        $ likes_counter += 1
                    if laurenpictureprogress >= 10:
                        $ aunt_visit_counter += 1
                    if sidney_worked_late == 2:
                        $ sidney_worked_late = 0
                    if sidney_worked_late == 1:
                        $ sidney_worked_late = 2
                    if club_fun_counter == 2:
                        $ club_fun_counter = 0
                    if club_fun_counter == 1:
                        $ club_fun_counter = 2
                    if sixty_nined_bfast == 2:
                        $ sixty_nined_bfast = 0
                    if sixty_nined_bfast == 1:
                        $ sixty_nined_bfast = 2
                    if start_of_campaign and not campaign_finished:
                        $ posters_bulbs = False
                        $ posters_bad = False
                        $ posters_good = False
                        $ posters_dragon = False
                        $ posters_me = False
                        $ posters_matt = True
                    if start_of_campaign and campaign_weeks <= 3:
                        $ campaign_weeks += 1
                    if inventory.has_item(ball_gag):
                        $ ball_gag_owned = True
                    $ timeofdaycounter = 1
                    $ daycounter = 1
                    $ weekcounter += 1
                    $ laurennight = False
                    $ laurenanger -= 1
                    $ momanger -= 1
                    $ sidneyanger -= 1
                    $ auntanger -= 1
                    $ cousinanger -= 1
                    $ gavelaurengift = False
                    $ gavesidneygift = False
                    $ gavemomgift = False
                    $ laurenangrytv = False
                    $ momgotobathroom = False
                    $ momnight = False
                    $ sawsidneychanging = False
                    $ liedaboutmoney = False
                    $ momatclub = False
                    $ laurenfingered = False
                    $ laurenangrytv = False
                    $ spiedlaurenbathroom = False
                    $ spiedmombathroom = False
                    $ spiedsidneybathroom = False
                    $ sawlaurensquirt = False
                    $ mm_fuckedtoday = False
                    $ weekly_htbyd_complete = False
                    $ weekly_wr_complete = False
                    $ mom_squirted_today_bedroom = False
                    $ sidneys_running = False
                    $ sidneys_working = False
                    $ visited_sid = False
                    $ watched_with_Diaz = False
                    $ monday_sid_worked = False
                    $ lauren_door_locked = False
                    $ daily_truth_counter = 0
                    $ daily_dare_counter = 0
                    $ truth_told = 0
                    $ weekly_htbyd_trigger = False
                    $ weekly_htbyd_complete = False
                    $ weekly_wr_trigger = False
                    $ weekly_wr_complete = False
                    $ weekly_hp_trigger = False
                    $ weekly_hp_complete = False
                    $ saw_aunt_exercise = False
                    $ couldnt_resist = False
                    $ gaveauntgift = False
                    $ gavecuzgift = False
                    $ spiedgirlsbathroom = False
                    $ spiedmandybathroom = False
                    $ spiedauntbathroom = False
                    $ visited_mandy_evening = False
                    $ spied_mandy_bed = False
                    $ played_the_game = False
                    $ answered_ph_wrong = False
                    $ mandy_spanked = False
                    $ lauren_spanked = False
                    $ weekly_poster_toggle = False
                    $ bought_lauren_swag = False
                    $ bought_diaz_votes = False
                    $ win_eligible = False
                    $ jackoff_week = False
                    $ blowjob_week = False
                    $ weekly_campaign_meeting = False
                    $ campaign_finished_warning = 0
                    $ lounge_creampie = False
                    jump wakeupryan

                else:
                    if daycounter == 6:
                        "Today is Saturday, which is the day the DeCapos come for their payment."
                        "Would you like to skip this event today and jump to tomorrow morning, or would you like to go directly to the Mafia payment event?"
                        menu:
                            "Skip event and sleep till tomorrow":
                                "Ok... I get it... I'm sure you've got lots of other events to get to."
                                "But the Mafia still needs to get paid!"
                                "How will they recieve their payment?"
                                menu:
                                    "I'll pay them $1,000." if money >= 1000:
                                        "{i}\"Money -$1,000\"{/i}"
                                        $ money -= 1000
                                        $ loyaltycounter += 1
                                        "{i}{b}\"Mom's Affection +10\"{/b}{/i}"
                                        $ momaffection += 10
                                        "{i}{b}\"Mom's Anger = 0\"{/b}{/i}"
                                        $ momanger = 0
                                        "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                                        $ momlibido += 1
                                    "Shit!... I don't have enough money to pay the Mafia." if money <= 999:
                                        RT "{i}Looks like it's up to Mom to use her \"ass\"ets to pay the debt this week.{/i}"
                                        "{i}{b}\"Mom's Affection -5\"{/b}{/i}"
                                        $ momaffection -= 5
                                        $ clubcounter += 1
                                    "Let Mom use her \"ass\"ets to pay the debt this week." if money >= 1000:
                                        RT "{i}I need to use that money for other things.{/i}"
                                        "{i}{b}\"Mom's Affection -5\"{/b}{/i}"
                                        $ momaffection -= 5
                                        $ clubcounter += 1
                            "Jump to Mafia payment event.":
                                $ timeofdaycounter = 4
                                jump collectingpayment

                    if sidneys_working:
                        $ timeofdaycounter = 5
                        jump sidneys_home_late
                    if day_off_counter >= 1:
                        $ aunt_day_off = False
                        $ day_off_counter = 0
                    if aunt_day_off == True:
                        $ day_off_counter += 1
                    if laurenpictureprogress >= 10:
                        $ aunt_visit_counter += 1
                    else:
                        pass
                    if sidneymakingcosplay == True:
                        $ cosplayoutfitcounter += 1
                    else:
                        pass
                    if picsareposted == True:
                        $ picsarepostedcounter += 1
                    else:
                        pass
                    ### vars for likes
                    $ advertising = False
                    $ income_output = False
                    $ day_likes = 0
                    # for supporters gal
                    if supporters_month_counter >= 4:
                        $ supporters_income_output = False
                    if gal_supporters:
                        $ supporters_day_count +=1
                    if days_until_next_photo_shoot <= 1 and not first_htbyd_shoot:
                        $ days_until_next_photo_shoot += 1
                    if photoshoot_1:
                        $ likes_counter += 1
                    if sidney_worked_late == 2:
                        $ sidney_worked_late = 0
                    if sidney_worked_late == 1:
                        $ sidney_worked_late = 2
                    if club_fun_counter == 2:
                        $ club_fun_counter = 0
                    if club_fun_counter == 1:
                        $ club_fun_counter = 2
                    if sixty_nined_bfast == 2:
                        $ sixty_nined_bfast = 0
                    if sixty_nined_bfast == 1:
                        $ sixty_nined_bfast = 2
                    if posters_good and daycounter <= 5:
                        $ school_influence += 3
                    if posters_dragon and daycounter <= 5:
                        $ school_influence += 1
                    if posters_me and daycounter <= 5:
                        $ school_influence += 1
                    if visits_to_stone >= 4:
                        $ persistent.gal_other_girls_2 = True
                    if fucked_lauren and campaign_win:
                        $ persistent.gal_Lauren_7 = True
                    if megan_told_counter >= 1:
                        $ persistent.gal_other_girls_3 = True
                    if locker_cam_placed:
                        $ persistent.gal_Lauren_8 = True
                    if mandy_joined:
                        $ persistent.gal_harem_5 = True
                    if first_train:
                        $ persistent.gal_NTR_7 = True
                    if diaz_van_counter >= 4:
                        $ persistent.gal_other_girls_4 = True
                    if inventory.has_item(ball_gag):
                        $ ball_gag_owned = True
                    $ timeofdaycounter = 1
                    $ daycounter += 1
                    $ laurennight = False
                    $ laurenanger -= 1
                    $ momanger -= 1
                    $ sidneyanger -= 1
                    $ auntanger -= 1
                    $ cousinanger -= 1
                    $ gavelaurengift = False
                    $ gavesidneygift = False
                    $ gavemomgift = False
                    $ Laurenangrytv = False
                    $ momgotobathroom = False
                    $ momnight = False
                    $ sawsidneychanging = False
                    $ momatclub = False
                    $ sawmomstripping = False
                    $ laurenfingered = False
                    $ laurenangrytv = False
                    $ spiedlaurenbathroom = False
                    $ spiedmombathroom = False
                    $ spiedsidneybathroom = False
                    $ sawlaurensquirt = False
                    $ mm_fuckedtoday = False
                    $ mom_squirted_today_bedroom = False
                    $ sidneys_running = False
                    $ sidneys_working = False
                    $ visited_sid = False
                    $ watched_with_Diaz = False
                    $ monday_sid_worked = False
                    $ lauren_door_locked = False
                    $ daily_truth_counter = 0
                    $ daily_dare_counter = 0
                    $ truth_told = 0
                    $ saw_aunt_exercise = False
                    $ couldnt_resist = False
                    $ gaveauntgift = False
                    $ gavecuzgift = False
                    $ spiedgirlsbathroom = False
                    $ spiedmandybathroom = False
                    $ spiedauntbathroom = False
                    $ visited_mandy_evening = False
                    $ spied_mandy_bed = False
                    $ played_the_game = False
                    $ answered_ph_wrong = False
                    $ mandy_spanked = False
                    $ lauren_spanked = False
                    $ had_campaign_meeting = False
                    $ visited_diaz_today = False
                    $ sneak_locker_peek = False
                    $ daily_megan_fuck = False
                    $ propositioned_lauren = False
                    $ lounge_creampie = False
                    jump wakeupryan
            "No":
                scene bg RyansRoom01
                $ screen_on = "ryanmap"
                call screen ryanmap
    else:
        scene bg RyansRoom01
        RT "{i}I'm not tired yet.{/i}"
        $ screen_on = "ryanmap"
        call screen ryanmap

label wakeupryan:
    if diazfirstvisit and daycounter == 7 and progress <= 14 and lauren_mischief >= 2 and mom_mischief >= 2 and bathroom_boobs:
        jump move_in_day
    if diazfirstvisit == True and first_sixtynine == True and christmas_complete == False:
        jump xmas_dream
    if daycounter == 6 and aunt_second_visit == True:
        jump aunts_financials
    if aunt_visit_counter >= 5 and aunt_first_visit and diazfirstvisit and not bobby_send_text:
        jump bobbytext
    if loyaltycounter == 2 and email_alert_one == False:
        jump emailalert
    if daycounter == 4 and progress >= 12:
        jump diazvisit
    if loyaltycounter == 3 and money >= 20 and daycounter == 7 and firstclubvisit == False:
        jump firstloyaltyweekend
    if progress == 8:
        jump cosplaywakeme
    if progress == 3:
        $ persistent.gal_Lauren_1 = True
        scene bg SleepBlack
        with fade
        play music SexMusic
        L "[ryan]? Are you awake?"
        scene bg BlurryWhite
        with fade
        scene bg LaurenWakeMe1
        with fade
        R "Huh?.... Lauren.... why are you waking me up so early?"
        $ timeofdaycounter += 1
        L "Because I couldn't sleep anymore!"
        L "I was having the weirdest dreams about you."
        R "What kind of weird dreams?"
        L "Oh.... I don't really want to say..."
        L "They were a little bit disturbing..."
        RT "{i}I wonder if my visit last night caused any of those dreams.{/i}"
        RT "{i}Could my subliminal messages have actually worked?{/i}"
        L "Plus I am dying with curiosity about what happened with you and Mom last night."
        R "What do you mean \"with Mom and me last night\" nothing happened between us last night!"
        L "So.... you didn't follow her to see where she went?"
        R "Oh.... right.... yes.... I did follow her."
        menu:
            "Look down":
                scene bg LaurenWakeMe3
                with dissolve
                RT "{i}WOW.... what a view!{/i}"
                L "And?"
                R "Oh uhh.... they just took her to their night club."
                L "To their nightclub?"
                L "Huh.... I wonder what they would have her do there?"
                menu:
                    "Look up":
                        scene bg LaurenWakeMe4
                        with dissolve
                        RT "{i}Huh.... nothing as wonderful as Mom's, but her small titties have some appeal as well.{/i}"
                        L "Well, did you follow her in?"
                        R "Uh.... yeah, I did."
                        L "And?..."
                        R "Oh.... uh.... nothing weird or perverted or anything."
                        L "Huh?..."
                        R "I mean they just had her showing off to some customers.... uh.... serving them drinks.... I mean."
                        R "Why didn't you ask her about it?"
                        L "Oh, she's still asleep with her door locked."
                        L "She's grumpier than you are when I wake her up."
                        scene bg LaurenWakeMe2
                        with dissolve
                        L "Hey.... what the hell?"
                        R "Ohh.... uhh.... It's just morning wood."
                        L "Morning wood my ass. You didn't have it when you first woke up!"
                        R "Oh yeah, uhh.... it can still happen shortly after you wake up."
                        L "Yeah, I'm pretty sure that's not a thing."
                        R "No really.... that can happen."
                        L "Ok.... whatever.... you're the one with a penis."
                        L "Aren't you going to cover him up?"
                        menu:
                            "Cover up":
                                scene bg LaurenWakeMe5
                                with dissolve
                                L "You're actually bigger than I dreamt you were last ni.... I mean than I imagined you were."
                                L "I mean, I've never seen one in real life, just in porn..."
                                L "And you're as big as they are."
                                $ laurenlibido += 1
                                $ laurenaffection += 1
                                "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                                "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                                RT "{i}So she did dream about me last night. I'll have to keep whispering suggestions at night.{/i}"
                                R "Thanks.... I guess."
                                L "Anyways.... I should go and let you take care of that, or get dressed, or whatever you do to hide your boner."
                                R "Ok, see you later I guess."
                                play music Honey
                                scene bg RyansRoom01
                                with fade
                                $ screen_on = "ryanmap"
                                call screen ryanmap
                            "\"Why should I?\"":
                                scene bg LaurenWakeMe2
                                R "You're the one in my room uninvited."
                                L "Weird flex, but ok."
                                L "You're actually bigger than I dreamt you were last ni.... I mean than I imagined you were."
                                L "I mean, I've never seen one in real life, just in porn..."
                                L "And you're as big as they are."
                                $ laurenlibido += 5
                                "{i}{b}\"Lauren's Libido +5\"{/b}{/i}"
                                RT "{i}So she did dream about me last night. I'll have to keep whispering suggestions at night.{/i}"
                                R "Thanks.... I guess."
                                L "Do you mind me looking?"
                                R "No, not really. I know you're just curious."
                                R "I get curious too sometimes. Maybe you can show me something as well."
                                scene bg LaurenWakeMeAngry
                                with dissolve
                                L "Ohh! You Pervert!"
                                L "I should have known better then to talk about anything sexual with you!"
                                L "I'm leaving so you can take care of your little morning wood problem however you want!"
                                "{i}{b}\"Lauren's Anger +10\"{/b}{/i}"
                                $ laurenanger += 10
                                play music Honey
                                scene bg RyansRoom01
                                with fade
                                $ screen_on = "ryanmap"
                                call screen ryanmap
    else:
        scene bg SleepBlack
        with fade
        $ renpy.pause (0.5)
        scene bg RyansRoom01
        with fade
        $ renpy.pause (0.5)
        if sidney_took_job and daycounter == 1:
            $ sidneys_working = True
        $ screen_on = "ryanmap"
        call screen ryanmap

label fapmom:
    play music SexMusic
    scene JackOffVideo01
    with fade
    $ renpy.pause ()
    scene bg BlurryWhite
    with fade
    play sound Mom02 loop
    scene JoffMomVideo01
    with fade
    $ renpy.pause ()
    scene bg BlurryWhite
    with fade
    stop sound
    play sound Ejaculate
    scene bg RoomClimaxMom
    with fade
    $ renpy.pause ()
    scene bg BlurryWhite
    with fade
    stop sound
    with vpunch
    with hpunch
    play sound Ejaculate
    scene bg RoomCumWackMom01
    with fade
    with vpunch
    with hpunch
    $ renpy.pause ()
    scene bg RoomCumWackMom02
    with dissolve
    RT "{i}If only it was the real thing.{/i}"
    $ timeofdaycounter += 1
    play music Honey
    jump myroom

label faplauren:
    play music SexMusic
    scene JackOffVideo02
    with fade
    $ renpy.pause ()
    scene bg BlurryWhite
    with fade
    play sound Blow02 loop
    scene JoffLaurenVideo01
    with fade
    $ renpy.pause ()
    scene bg BlurryWhite
    with fade
    stop sound
    play sound Ejaculate
    scene bg RoomClimaxLauren
    with fade
    with vpunch
    with hpunch
    $ renpy.pause ()
    scene bg BlurryWhite
    with fade
    with vpunch
    with hpunch
    play sound Ejaculate
    scene bg RoomCumWackLauren01
    with fade
    with vpunch
    with hpunch
    $ renpy.pause ()
    scene bg RoomCumWackLauren02
    with dissolve
    RT "{i}If only it was the real thing.{/i}"
    $ timeofdaycounter += 1
    play music Honey
    jump myroom

label fapsidney:
    play music SexMusic
    scene JackOffVideo03
    with fade
    $ renpy.pause ()
    scene bg BlurryWhite
    with fade
    play sound Sidney01 loop
    scene JoffSidneyVideo01
    with fade
    $ renpy.pause ()
    scene bg BlurryWhite
    with fade
    stop sound
    play sound Ejaculate
    scene bg RoomClimaxSidney
    with fade
    with vpunch
    with hpunch
    $ renpy.pause ()
    scene bg BlurryWhite
    with fade
    with vpunch
    with hpunch
    play sound Ejaculate
    scene bg RoomCumWackSidney01
    with fade
    with vpunch
    with hpunch
    $ renpy.pause ()
    scene bg RoomCumWackSidney02
    with dissolve
    RT "{i}What is wrong with me?{/i}"
    $ timeofdaycounter += 1
    play music Honey
    jump myroom

#######  LOUNGE  #############  LOUNGE  ###############  LOUNGE  ################lOUNGE######################

label lounge:
    if timeofdaycounter == 1:
        jump loungeearlymorning
    elif timeofdaycounter == 2:
        jump loungemorning
    elif timeofdaycounter == 3:
        jump loungeafternoon
    elif timeofdaycounter == 4:
        jump loungeevening
    else:
        jump loungenight

label loungeearlymorning:
    if daycounter >= 6:
        jump loungeearlymorningweekend
    if sidneyfingerlaurenprogress >= 5 and sidneys_running == False:
        jump sidney_morning_jog
    if sidneyfingerlaurenprogress >= 4 and sidneys_running == False:
        scene bg SidneyLoungeMorning
        with fade
        $ screen_on = "sidneyloungemorningmap"
        call screen sidneyloungemorningmap
    else:
        scene bg FamilyRoom01
        with fade
        $ screen_on = "loungemap"
        call screen loungemap

label loungeearlymorningweekend:
    if sidneyfingerlaurenprogress >= 4:
        scene bg SidneyLoungeMorning
        with fade
        $ screen_on = "sidneyloungemorningmap"
        call screen sidneyloungemorningmap
    else:
        scene bg FamilyRoom01
        with fade
        $ screen_on = "loungemap"
        call screen loungemap

label loungemorning:
    if daycounter >= 6:
        jump loungemorningweekend
    if aunt_second_visit == True and aunts_new_uniform == False and aunt_visit_counter >= 3:
        jump maid_outfit_fitting
    else:
        scene bg FamilyRoom01
        with fade
        $ screen_on = "loungemap"
        call screen loungemap

label loungemorningweekend:
    if progress >= 4:
        jump honey_do_list
    else:
        scene bg FamilyRoom01
        with fade
        $ screen_on = "loungemap"
        call screen loungemap

label loungeafternoon:
    if daycounter >= 6:
        jump loungeafternoonweekend
    else:
        scene bg FamilyRoom01
        with fade
        $ screen_on = "loungemap"
        call screen loungemap

label loungeafternoonweekend:
    scene bg FamilyRoom01
    with fade
    $ screen_on = "loungemap"
    call screen loungemap

label loungeevening:
    if fucked_lauren_ntr and daycounter != 6:
        jump ntr_lounge_sex
    if fucked_lauren and daycounter != 6:
        jump lounge_sex
    if progress >= 15 and not mandy_at_school and daycounter <= 5:
        jump mandy_accepted
    if mom_mad_posters and not mom_lauren_fought:
        jump lauren_mom_fight
    if finished_htbyd_shoot and daycounter != 6 and laurenanger == 0:
        jump tv_together
    if first_lauren_grind and daycounter != 6 and laurenanger == 0:
        jump tv_together
    if progress == 8:
        scene bg FamilyRoom01
        with fade
        $ screen_on = "loungemap"
        call screen loungemap
    if daycounter == 7:
        jump loungeeveningweekend
    elif daycounter == 6:
        while progress >= 6:
            jump collectingpayment
        if daycounter == 6:
            jump loungeeveningweekend
    if laurenangrytv == True:
        scene bg FamilyRoom01
        with fade
        $ screen_on = "loungemap"
        call screen loungemap
    if progress == 4:
        scene bg LaurenRemoteSearch01
        with fade
        play music SexMusic
        RT "{i}What did I just walk in on? It's like Mom and Lauren are purposely trying to be cock-teases lately.{/i}"
        RT "{i}Has it always been like this, and now I'm just starting to notice? I'm sure I'm reading way more into this than I should.{/i}"
        menu:
            "Lauren, what the hell are you doing?":
                $ persistent.gal_Lauren_2 = True
                scene bg LaurenRemoteSearch02
                with dissolve
                L "I'm looking for the TV remote."
                L "Do you know where it is?"
                R "I'm sorry I haven't seen it."
                $ progress = 5
                L "Well, you were the last one to watch TV, so you must be the one who lost it."
                L "The least you can do is help me find it. Bend down here and help me look."
                scene bg LaurenRemoteSearch03
                with fade
                RT "{i}Look for the remote?{/i}"
                RT "{i}How am I supposed to concentrate on anything else besides this view right in front of me?{/i}"
                RT "{i}Hmmm.... I wonder.... {/i}"
                scene bg LaurenRemoteSearch04
                with fade
                RT "{i}Oh my God, I can!{/i}"
                RT "{i}I can kind of smell her pussy from this close.{/i}"
                RT "{i}I've never smelled a pussy before, I kind of like it.{/i}"
                RT "{i}I've got to get closer.{/i}"
                scene bg LaurenRemoteSearch05
                with dissolve
                RT "{i}Wow! That smells incredible!{/i}"
                RT "{i}I wish I could taste it.{/i}"
                RT "{i}It just turns me on so much!{/i}"
                L "Well, I don't see the remote in this corner, I'm coming back."
                R "Wait!"
                scene bg LaurenRemoteSearch06
                with dissolve
                with vpunch
                R "Mmphh..."
                scene bg LaurenRemoteSearch07
                with fade
                scene bg LaurenRemoteSearch06
                with fade
                scene bg LaurenRemoteSearch07
                with fade
                L "[ryan]?.... Is that your face in my ass?"
                L "[ryan]?..."
                "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                $ laurenlibido += 1
                scene bg LaurenRemoteSearch06
                with fade
                R "Uhh.... yeah.... sorry. I was just looking for the remote under this couch cushion, and didn't realize I was that close to you until you backed up."
                RT "{i}Oh my God, it smells so good I can almost taste it.{/i}"
                L "Well, would you mind removing it?"
                R "Oh yeah.... of course."
                if laurenanger >= 1:
                    scene bg LaurenWatchTV01
                    with fade
                    L "Well, that was a little awkward!"
                    R "Only if you make it. It was just an accident."
                    L "I guess."
                    R "So do you want to watch some TV?"
                    $ laurenangrytv = True
                    L "I'm still pissed off at you remember."
                    L "Ugghh.... I'm just going to go to my room."
                    scene bg FamilyRoom01
                    with fade
                    play music Honey
                    $ screen_on = "loungemap"
                    call screen loungemap
                else:
                    scene bg LaurenWatchTV02
                    with fade
                    R "Sorry, that was a little awkward!"
                    L "Only if you let it be, it was just an accident."
                    R "Yeah.... I guess so."
                    L "So do you want to watch TV with me?"
                    R "Ok, what are you watching?"
                    L "I'm just starting season one of \"Game of Thots\"."
                    L "Have you been following this show?"
                    R "No I've just seen the first episode."
                    scene bg LaurenWatchTV03
                    with dissolve
                    L "Awesome! We can watch the series together!"
                    L "All my friends love it!"
                    scene bg LaurenWatchTV06
                    with dissolve
                    RT "{i}I wonder if this is a little too explicit for Lauren?{/i}"
                    scene bg LaurenWatchTV05
                    with fade
                    RT "{i}Wow! I can't believe what they can get away with on TV anymore! This is awesome!{/i}"
                    scene bg LaurenWatchTV04
                    with fade
                    R "Man, that episode was intense! Lauren are you ok? You seem a little flushed."
                    L "Oh yeah, I'm fine. I was just a little surprised at that brother sister sex scene."
                    L "This show almost makes incest seem normal, like it's no big deal or something."
                    R "Yeah, well incest is only bad when society says it's bad. There have been lots of times in history where it was perfectly accepted."
                    L "I wouldn't say lots of times."
                    R "Well, not a ton, but to me it's like being gay. If two people are in love with each other, why do people think they have the right to tell them they can't be in love"
                    L "I don't know it just seems really weird."
                    R "Only because you've been told all your life it's weird."
                    LT "{i}Hmmmm.... I'll have to think about that one.... {/i}"
                    $ laurenlibido += 1
                    $ laurenaffection += 1
                    "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                    $ timeofdaycounter += 1
                    $ tvfirsttimelauren = True
                    play music Honey
                    jump loungenightweekend
    elif progress >= 5:
        while tvfirsttimelauren == False:
            scene bg LaurenPonieTV
            with fade
            RT "{i}I wonder if Lauren would mind if I joined her.{/i}"
            if laurenanger >= 1:
                scene bg LaurenWatchTV01
                with fade
                R "Do you mind if I watch some TV with you?"
                $ laurenangrytv = True
                L "I'm still pissed off at you remember."
                L "Ugghh.... I'm just going to go to my room."
                scene bg FamilyRoom01
                with fade
                $ screen_on = "loungemap"
                call screen loungemap
            else:
                scene bg LaurenWatchTV02
                with fade
                play music SexMusic
                L "Hey [ryan], do you want to watch something with me?"
                R "Ok, what are you watching?"
                L "I'm just starting season one of \"Game of Thots\"."
                L "Have you been following this show?"
                R "No I've just seen the first episode."
                scene bg LaurenWatchTV03
                with dissolve
                L "Awesome! We can watch the series together!"
                L "All my friends love it!"
                scene bg LaurenWatchTV06
                with dissolve
                RT "{i}I wonder if this is a little too explicit for Lauren?{/i}"
                scene bg LaurenWatchTV05
                with fade
                RT "{i}Wow! I can't believe what they can get away with on TV anymore! This is awesome!{/i}"
                scene bg LaurenWatchTV04
                with fade
                R "Man, that episode was intense! Lauren are you ok? You seem a little flushed."
                L "Oh yeah, I'm fine. I was just a little surprised at that brother sister sex scene."
                L "This show almost makes incest seem normal, like it's no big deal or something."
                R "Yeah, well incest is only bad when society says it's bad. There have been lots of times in history where it was perfectly accepted."
                L "I wouldn't say lots of times."
                R "Well, not a ton, but to me it's like being gay. If two people are in love with each other, why do people think they have the right to tell them they can't be in love?"
                L "I don't know it just seems really weird."
                R "Only because you've been told all your life it's weird."
                LT "{i}Hmmmm.... I'll have to think about that one.... {/i}"
                $ laurenlibido += 1
                $ laurenaffection += 1
                "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                $ timeofdaycounter += 1
                $ tvfirsttimelauren = True
                play music Honey
                jump loungenightweekend
        if progress >= 5:
            scene bg LaurenPonieTV
            with fade
            menu:
                "Watch TV with Lauren":
                    RT "{i}I wonder If Lauren would mind if I joined her?{/i}"
                    if laurenanger >= 1:
                        scene bg LaurenWatchTV01
                        with fade
                        R "Do you mind if I watch some TV with you?"
                        $ laurenangrytv = True
                        L "I'm still pissed off at you remember."
                        L "Ugghh.... I'm just going to go to my room."
                        scene bg FamilyRoom01
                        with fade
                        $ screen_on = "loungemap"
                        call screen loungemap
                    else:
                        scene bg LaurenWatchTV02
                        with fade
                        play music SexMusic
                        L "Hey [ryan], do you want to watch something with me?"
                        R "Ok, what are you watching?"
                        L "Let's watch the next episode of \"Game of Thots\"!"
                        scene bg LaurenWatchTV06
                        with dissolve
                        $ renpy.pause ()
                        scene bg LaurenWatchTV05
                        with fade
                        $ renpy.pause ()
                        scene bg LaurenWatchTV04
                        with fade
                        L "Does the brother and sister have to fuck each other in every episode?"
                        "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                        $ laurenlibido += 1
                        $ timeofdaycounter += 1
                        play music Honey
                        jump loungenightweekend
                "Never mind":
                    scene bg LaurenPonieTV
                    $ screen_on = "laurenponietvmap"
                    call screen laurenponietvmap
    else:
        scene bg FamilyRoom01
        with fade
        $ screen_on = "loungemap"
        call screen loungemap

label loungeeveningweekend:
    if laurenangrytv == True:
        scene bg FamilyRoom01
        with fade
        $ screen_on = "loungemap"
        call screen loungemap
    if progress == 4:
        scene bg LaurenRemoteSearch01
        with fade
        play music SexMusic
        RT "{i}What did I just walk in on? It's like Mom and Lauren are purposely trying to be cock-teases lately.{/i}"
        RT "{i}Has it always been like this, and now I'm just starting to notice? I'm sure I'm reading way more into this than I should.{/i}"
        menu:
            "Lauren, what the hell are you doing?":
                $ persistent.gal_Lauren_2 = True
                scene bg LaurenRemoteSearch02
                with dissolve
                L "I'm looking for the TV remote."
                L "Do you know where it is?"
                R "I'm sorry I haven't seen it."
                $ progress = 5
                L "Well, you were the last one to watch TV, so you must be the one who lost it."
                L "The least you can do is help me find it. Bend down here and help me look."
                scene bg LaurenRemoteSearch03
                with fade
                RT "{i}Look for the remote?{/i}"
                RT "{i}How am I supposed to concentrate on anything else besides this view right in front of me?{/i}"
                RT "{i}Hmmm.... I wonder.... {/i}"
                scene bg LaurenRemoteSearch04
                with fade
                RT "{i}Oh my God, I can!{/i}"
                RT "{i}I can kind of smell her pussy from this close.{/i}"
                RT "{i}I've never smelled a pussy before, I kind of like it.{/i}"
                RT "{i}I've got to get closer.{/i}"
                scene bg LaurenRemoteSearch05
                with dissolve
                RT "{i}Wow! That smells incredible!{/i}"
                RT "{i}I wish I could taste it.{/i}"
                RT "{i}It just turns me on so much!{/i}"
                L "Well, I don't see the remote in this corner, I'm coming back."
                R "Wait!"
                scene bg LaurenRemoteSearch06
                with dissolve
                with vpunch
                R "Mmphh..."
                scene bg LaurenRemoteSearch07
                with fade
                scene bg LaurenRemoteSearch06
                with fade
                scene bg LaurenRemoteSearch07
                with fade
                L "[ryan]?.... Is that your face in my ass?"
                L "[ryan]?..."
                "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                $ laurenlibido += 1
                scene bg LaurenRemoteSearch06
                with fade
                R "Uhh.... yeah.... sorry. I was just looking for the remote under this couch cushion, and didn't realize I was that close to you until you backed up."
                RT "{i}Oh my God, it smells so good I can almost taste it.{/i}"
                L "Well, would you mind removing it?"
                R "Oh yeah.... of course."
                if laurenanger >= 1:
                    scene bg LaurenWatchTV01
                    with fade
                    L "Well, that was a little awkward!"
                    R "Only if you make it. It was just an accident."
                    L "I guess."
                    R "So do you want to watch some TV?"
                    $ laurenangrytv = True
                    L "I'm still pissed off at you remember."
                    L "Ugghh.... I'm just going to go to my room."
                    scene bg FamilyRoom01
                    with fade
                    play music Honey
                    $ screen_on = "loungemap"
                    call screen loungemap
                else:
                    scene bg LaurenWatchTV02
                    with fade
                    R "Sorry, that was a little awkward!"
                    L "Only if you let it be, it was just an accident."
                    R "Yeah.... I guess so."
                    L "So do you want to watch TV with me?"
                    R "Ok, what are you watching?"
                    L "I'm just starting season one of \"Game of Thots\"."
                    L "Have you been following this show?"
                    R "No I've just seen the first episode."
                    scene bg LaurenWatchTV03
                    with dissolve
                    L "Awesome! We can watch the series together!"
                    L "All my friends love it!"
                    scene bg LaurenWatchTV06
                    with dissolve
                    RT "{i}I wonder if this is a little too explicit for Lauren?{/i}"
                    scene bg LaurenWatchTV05
                    with fade
                    RT "{i}Wow! I can't believe what they can get away with on TV anymore! This is awesome!{/i}"
                    scene bg LaurenWatchTV04
                    with fade
                    R "Man, that episode was intense! Lauren are you ok? You seem a little flushed."
                    L "Oh yeah, I'm fine. I was just a little surprised at that brother sister sex scene."
                    L "This show almost makes incest seem normal, like it's no big deal or something."
                    R "Yeah, well incest is only bad when society says it's bad. There have been lots of times in history where it was perfectly accepted."
                    L "I wouldn't say lots of times."
                    R "Well, not a ton, but to me it's like being gay. If two people are in love with each other, why do people think they have the right to tell them they can't be in love?"
                    L "I don't know it just seems really weird."
                    R "Only because you've been told all your life it's weird."
                    LT "{i}Hmmmm.... I'll have to think about that one.... {/i}"
                    $ laurenlibido += 1
                    $ laurenaffection += 1
                    "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                    $ timeofdaycounter += 1
                    $ tvfirsttimelauren = True
                    play music Honey
                    jump loungenightweekend
    elif progress >= 5:
        while tvfirsttimelauren == False:
            scene bg LaurenPonieTV
            with fade
            RT "{i}I wonder if Lauren would mind if I joined her.{/i}"
            if laurenanger >= 1:
                scene bg LaurenWatchTV01
                with fade
                R "Do you mind if I watch some TV with you?"
                $ laurenangrytv = True
                L "I'm still pissed off at you remember."
                L "Ugghh.... I'm just going to go to my room."
                scene bg FamilyRoom01
                with fade
                $ screen_on = "loungemap"
                call screen loungemap
            else:
                scene bg LaurenWatchTV02
                with fade
                play music SexMusic
                L "Hey [ryan], do you want to watch something with me?"
                R "Ok, what are you watching?"
                L "I'm just starting season one of \"Game of Thots\"."
                L "Have you been following this show?"
                R "No I've just seen the first episode."
                scene bg LaurenWatchTV03
                with dissolve
                L "Awesome! We can watch the series together!"
                L "All my friends love it!"
                scene bg LaurenWatchTV06
                with dissolve
                RT "{i}I wonder if this is a little too explicit for Lauren?{/i}"
                scene bg LaurenWatchTV05
                with fade
                RT "{i}Wow! I can't believe what they can get away with on TV anymore! This is awesome!{/i}"
                scene bg LaurenWatchTV04
                with fade
                R "Man, that episode was intense! Lauren are you ok? You seem a little flushed."
                L "Oh yeah, I'm fine. I was just a little surprised at that brother sister sex scene."
                L "This show almost makes incest seem normal, like it's no big deal or something."
                R "Yeah, well incest is only bad when society says it's bad. There have been lots of times in history where it was perfectly accepted."
                L "I wouldn't say lots of times."
                R "Well, not a ton, but to me it's like being gay. If two people are in love with each other, why do people think they have the right to tell them they can't be in love?"
                L "I don't know it just seems really weird."
                R "Only because you've been told all your life it's weird."
                LT "{i}Hmmmm.... I'll have to think about that one.... {/i}"
                $ laurenlibido += 1
                $ laurenaffection += 1
                "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                $ timeofdaycounter += 1
                $ tvfirsttimelauren = True
                play music Honey
                jump loungenightweekend
        if progress >= 5:
            scene bg LaurenPonieTV
            with fade
            menu:
                "Watch TV with Lauren":
                    RT "{i}I wonder If Lauren would mind if I joined her?{/i}"
                    if laurenanger >= 1:
                        scene bg LaurenWatchTV01
                        with fade
                        R "Do you mind if I watch some TV with you?"
                        $ laurenangrytv = True
                        L "I'm still pissed off at you remember."
                        L "Ugghh.... I'm just going to go to my room."
                        scene bg FamilyRoom01
                        with fade
                        $ screen_on = "loungemap"
                        call screen loungemap
                    else:
                        scene bg LaurenWatchTV02
                        with fade
                        play music SexMusic
                        L "Hey [ryan], do you want to watch something with me?"
                        R "Ok, what are you watching?"
                        L "Let's watch the next episode of \"Game of Thots\"!"
                        scene bg LaurenWatchTV06
                        with dissolve
                        $ renpy.pause (2, hard=True)
                        scene bg LaurenWatchTV05
                        with fade
                        $ renpy.pause (2, hard=True)
                        scene bg LaurenWatchTV04
                        with fade
                        L "Does the brother and sister have to fuck each other in every episode?"
                        "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                        $ laurenlibido += 1
                        $ timeofdaycounter += 1
                        play music Honey
                        jump loungenightweekend
                "Never mind":
                    scene bg LaurenPonieTV
                    $ screen_on = "laurenponietvmap"
                    call screen laurenponietvmap
    else:
        scene bg FamilyRoom01
        with fade
        $ screen_on = "loungemap"
        call screen loungemap

label loungenight:
    if laurenfingered == True:
        scene bg SidneyLoungeNight
        with fade
        RT "{i}I better not push it any further tonight.{/i}"
        $ screen_on = "sidneyloungenightmap"
        call screen sidneyloungenightmap
    if sidneyfingerlaurenprogress == 4:
        jump getsidneyoffthecouch
    if daycounter >= 6:
        jump loungenightweekend
    else:
        scene bg LoungeNight
        with fade
        $ screen_on = "loungemapnight"
        call screen loungemapnight

label loungenightweekend:
    scene bg LoungeNight
    with fade
    $ screen_on = "loungemapnight"
    call screen loungemapnight

label tv:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    if timeofdaycounter == 5:
        scene bg LoungeNight
        RT "{i}I'd wake everyone up if I watch TV now.{/i}"
        jump lounge
    else:
        scene bg FamilyRoom01
        RT "{i}I don't have time for that now.{/i}"
        $ screen_on = "loungemap"
        call screen loungemap

label familypic:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    scene bg FamilyPhotoAdjusted
    $ screen_on = "familyphotomap"
    call screen familyphotomap

label sidney:
    if sidneypictureprogress == 10:
        scene bg FamilyPhotoAdjusted
        RT "{i}I love her face in this picture.... I wonder what it will take to get closer to her!{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif sidneypictureprogress == 9:
        scene bg FamilyPhotoAdjusted
        RT "{i}I love her face in this picture.... I wonder what it will take to get closer to her!{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif sidneypictureprogress == 8:
        scene bg FamilyPhotoAdjusted
        RT "{i}I love her face in this picture.... I wonder what it will take to get closer to her!{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif sidneypictureprogress == 7:
        scene bg FamilyPhotoAdjusted
        RT "{i}I love her face in this picture.... I wonder what it will take to get closer to her!{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif sidneypictureprogress == 6:
        scene bg FamilyPhotoAdjusted
        RT "{i}I love her face in this picture.... I wonder what it will take to get closer to her!{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif sidneypictureprogress == 5:
        scene bg FamilyPhotoAdjusted
        RT "{i}I love her face in this picture.... I wonder what it will take to get closer to her!{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif sidneypictureprogress == 4:
        scene bg FamilyPhotoAdjusted
        RT "{i}I love her face in this picture.... I wonder what it will take to get closer to her!{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif sidneypictureprogress == 3:
        scene bg FamilyPhotoAdjusted
        RT "{i}I love her face in this picture.... I wonder what it will take to get closer to her!{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif sidneypictureprogress == 2:
        scene bg FamilyPhotoAdjusted
        RT "{i}I love her face in this picture.... I wonder what it will take to get closer to her!{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif sidneypictureprogress == 1:
        scene bg FamilyPhotoAdjusted
        RT "{i}I love her face in this picture.... I wonder what it will take to get closer to her!{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    else:
        scene bg FamilyPhotoAdjusted
        RT "{i}This is my older sister Sidney,{p}She moved out of the house last year.{/i}"
        RT "{i}She still lives here in the city,{p}but she wanted to be on her own while she attends college.{/i}"
        RT "{i}She attends the Fine Arts Academy,{p}she's majoring in fashion design.{/i}"
        RT "{i}Dad pays for everything.{p}We hardly ever see her anymore.{/i}"
        $ sidneypictureprogress = 1
        if in_family_photomap:
            return
        else:
            jump familypic

label ryan:
    if ryanpictureprogress == 1:
        scene bg FamilyPhotoAdjusted
        RT "{i}Why do I always have a goofy smile in family pictures?{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    else:
        scene bg FamilyPhotoAdjusted
        RT "{i}Well, that's me,{p} Mom says I'm handsome,{p} though I've never really had any luck with the ladies.{/i}"
        RT "{i}I got mono last year,{p} as in \"mononucleosis.\"{p} I had to miss a ton of school.{/i}"
        RT "{i}I have to make up some of my credits again this year before they will give me my diploma.{/i}"
        RT "{i}Lucky for me, my mom's my teacher this year, and she goes pretty easy on me,{p} she understands my situation.{/i}"
        RT "{i}My idiot dad has been trying to get me to drop out of school and join him in the family business.{/i}"
        RT "{i}But I have no interest in shipping things around the country,{/i}"
        RT "{i}I want to make money by broadcasting me playing video games, or maybe more realistically, a photographer or something along those lines.{/i}"
        $ ryanpictureprogress = 1
        if in_family_photomap:
            return
        else:
            jump familypic

label lauren:
    if laurenpictureprogress == 14:
        scene bg FamilyPhotoAdjusted
        RT "{i}I miss how close we used to be.... I wonder how we can get closer.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    if laurenpictureprogress == 13:
        scene bg FamilyPhotoAdjusted
        RT "{i}I miss how close we used to be.... I wonder how we can get closer.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    if laurenpictureprogress == 12:
        scene bg FamilyPhotoAdjusted
        RT "{i}I miss how close we used to be.... I wonder how we can get closer.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    if laurenpictureprogress == 11:
        scene bg FamilyPhotoAdjusted
        RT "{i}I miss how close we used to be.... I wonder how we can get closer.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    if laurenpictureprogress == 10:
        scene bg FamilyPhotoAdjusted
        RT "{i}I miss how close we used to be.... I wonder how we can get closer.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif laurenpictureprogress == 9:
        scene bg FamilyPhotoAdjusted
        RT "{i}I miss how close we used to be.... I wonder how we can get closer.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif laurenpictureprogress == 8:
        scene bg FamilyPhotoAdjusted
        RT "{i}I miss how close we used to be.... I wonder how we can get closer.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif laurenpictureprogress == 7:
        scene bg FamilyPhotoAdjusted
        RT "{i}I miss how close we used to be.... I wonder how we can get closer.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif laurenpictureprogress == 6:
        scene bg FamilyPhotoAdjusted
        RT "{i}I miss how close we used to be.... I wonder how we can get closer.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif laurenpictureprogress == 5:
        scene bg FamilyPhotoAdjusted
        RT "{i}I miss how close we used to be.... I wonder how we can get closer.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif laurenpictureprogress == 4:
        scene bg FamilyPhotoAdjusted
        RT "{i}I miss how close we used to be.... I wonder how we can get closer.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif laurenpictureprogress == 3:
        scene bg FamilyPhotoAdjusted
        RT "{i}I miss how close we used to be.... I wonder how we can get closer.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif laurenpictureprogress == 2:
        scene bg FamilyPhotoAdjusted
        RT "{i}I miss how close we used to be.... I wonder how we can get closer.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif laurenpictureprogress == 1:
        scene bg FamilyPhotoAdjusted
        RT "{i}I miss how close we used to be.... I wonder how we can get closer.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    else:
        scene bg FamilyPhotoAdjusted
        RT "{i}This is my little sister Lauren,{p} We were super close through most of our childhood,{p} but now her best friend is her phone.{/i}"
        RT "{i}My mom just recently allowed her onto social media,{p} and now the floodgates have opened.{/i}"
        RT "{i}I really miss spending more time with her.{p} Lucky for me, she is in my class, although, I'm not sure if she's noticed.{/i}"
        $ laurenpictureprogress = 1
        if in_family_photomap:
            return
        else:
            jump familypic

label dad:
    if dadpictureprogress == 2:
        scene bg FamilyPhotoAdjusted
        RT "{i}What a douche! I can't believe the trouble he's gotten us into.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif dadpictureprogress == 1:
        scene bg FamilyPhotoAdjusted
        RT "{i}What a douche! I can't believe the trouble he's gotten us into.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    else:
        scene bg FamilyPhotoAdjusted
        RT "{i}This is my dad, [dad_name], {p}The best way to describe him is \"Larger Than Life.\"{/i}"
        RT "{i}He started his own shipping and delivery business, and has been very successful.{/i}"
        RT "{i}He runs his family like he does his business. {p}With complete control. {p}He says jump, we all say \"How high?\".{/i}"
        RT "{i}He's never been physically abusive, {p}but he's made up for that through mental and emotional abuse.{/i}"
        RT "{i}If he didn't provide all the money we needed to survive, we would all probably be happier with him in prison.{/i}"
        $ dadpictureprogress = 1
        if in_family_photomap:
            return
        else:
            jump familypic

label mom:
    if mompictureprogress == 5:
        scene bg FamilyPhotoAdjusted
        RT "{i}She's still pretty hot for a mom. It would be fun to see more of her wild side.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif mompictureprogress == 4:
        scene bg FamilyPhotoAdjusted
        RT "{i}She's still pretty hot for a mom. It would be fun to see more of her wild side.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif mompictureprogress == 3:
        scene bg FamilyPhotoAdjusted
        RT "{i}She's still pretty hot for a mom. It would be fun to see more of her wild side.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif mompictureprogress == 2:
        scene bg FamilyPhotoAdjusted
        RT "{i}She's still pretty hot for a mom. It would be fun to see more of her wild side.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    elif mompictureprogress == 1:
        scene bg FamilyPhotoAdjusted
        RT "{i}She's still pretty hot for a mom. It would be fun to see more of her wild side.{/i}"
        if in_family_photomap:
            return
        else:
            jump familypic
    else:
        scene bg FamilyPhotoAdjusted
        RT "{i}This is my mom Jackelyn, she goes by [mom_name] but we call her Mom.{/i}"
        RT "{i}She's always been a good mother, as far as providing for our physical needs,{/i}"
        RT "{i}But she's always focused more attention on the things that kept my dad happy, rather than giving us the attention we needed and wanted.{/i}"
        RT "{i}I guess she used to be quite the party girl in high school.{p}Now my dad proudly boasts how he tamed her into an obedient wife and mother.{/i}"
        RT "{i}She always has plenty of bad things to say about him, {p}but only behind his back. {p}She wouldn't dream of saying anything to his face.{/i}"
        RT "{i}She started teaching high school about five years ago, {p}I think just to get out of the house and be more social. {p}I think it has made her happier.{/i}"
        RT "{i}And now Lauren and I are lucky enough to be in her class.{/i}"
        $ mompictureprogress = 1
        if in_family_photomap:
            return
        else:
            jump familypic

label backbutton:
    if timeofdaycounter == 5:
        scene bg LoungeNight
        jump lounge
    else:
        scene bg FamilyRoom01
        jump lounge

#####  BATH  ##############  BATH  ######################  BATH  ###################  BATH  ##########################  BATH  ###############

label bath:
    if timeofdaycounter == 1:
        jump bathearlymorning
    elif timeofdaycounter == 2:
        jump bathmorning
    elif timeofdaycounter ==3:
        jump bathafternoon
    elif timeofdaycounter == 4:
        jump bathevening
    else:
        jump bathnight

label bathearlymorning:
    if daycounter >= 6:
        jump bathearlymorningweekend
    if progress >= 15:
        jump sharing_shower
    if laurenlibido == 10:
        jump laurenhornybathroom
    if spycaminbath == True:
        jump laurenbathspycam
    else:
        scene bg BathroomDoor
        with fade
        RT "{i}Lauren is taking her early morning shower, I wonder if there is some way to spy on her.{/i}"
        $ screen_on = "bathdoormap"
        call screen bathdoormap

label bathearlymorningweekend:
    if campaign_finished and daycounter == 6:
        jump lauren_bath_alone
    if progress >= 15 and cousinlibido == 10 and daycounter == 7:
        jump mandyhornybathroom
    if progress >= 15 and laurenlibido == 10 and daycounter == 6:
        jump laurenhornybathroom
    if progress >= 15 and daycounter == 7:
        jump mandybathspycam
    if progress >= 15 and daycounter == 6:
        jump laurenbathspycam
    if spycaminbath == False and progress >= 6:
        while inventory.inv_amount(spycam) >= 1:
            jump spycambath
        if spycaminbath == False:
            scene bg bathroom01
            with fade
            $ screen_on = "bathmap"
            call screen bathmap
    scene bg bathroom01
    with fade
    $ screen_on = "bathmap"
    call screen bathmap

label laurenhornybathroom:
    if spycaminbath == True:
        scene bg BathroomDoor
        with fade
        play sound Lauren01 loop
        RT "{i}Lauren is taking her early morning shower. Wait.... did I just hear some moaning? Let's just take a quick look.{/i}"
        menu:
            "Look.":
                jump laurenfingerselfbath
            "Never mind.":
                scene bg BathroomDoor
                "{i}{b}\"Lauren's Libido -5\"{/b}{/i}"
                $ laurenlibido -= 5
                stop sound fadeout 1.0
                $ screen_on = "bathdoormap"
                call screen bathdoormap
    else:
        scene bg BathroomDoor
        with fade
        play sound Lauren01 loop
        RT "{i}Lauren is taking her early morning shower. Wait.... did I just hear some moaning?, uggh I've got to find a way to see what's going on in there.{/i}"
        "{i}{b}\"Lauren's Libido -5\"{/b}{/i}"
        $ laurenlibido -= 5
        stop sound fadeout 1.0
        $ screen_on = "bathdoormap"
        call screen bathdoormap

label bathmorning:
    if daycounter >= 6:
        jump bathmorningweekend
    if sidneylibido == 10:
        jump sidneyhornybathroom
    if spycaminbath == True:
        jump sidneybathspycam
    if progress >= 6:
        scene bg BathroomDoor
        with fade
        RT "{i}Sidney must be taking a shower, Mom and Lauren already left for school.{/i}"
        $ screen_on = "bathdoormap"
        call screen bathdoormap
    else:
        scene bg bathroom01
        with fade
        $ screen_on = "bathmap"
        call screen bathmap

label bathmorningweekend:
    if sidneylibido == 10:
        jump sidneyhornybathroom
    if spycaminbath == True:
        jump sidneybathspycam
    if progress >= 6:
        scene bg BathroomDoor
        with fade
        RT "{i}Sidney must be taking a shower.{/i}"
        $ screen_on = "bathdoormap"
        call screen bathdoormap
    else:
        scene bg bathroom01
        with fade
        $ screen_on = "bathmap"
        call screen bathmap

label sidneyhornybathroom:
    if spycaminbath == True:
        scene bg BathroomDoor
        with fade
        play sound Sidney01 loop
        RT "{i}Sidney must be taking a shower. Wait.... did I just hear some moaning? Let's just take a quick look through the spy-cam.{/i}"
        menu:
            "Look.":
                jump sidneyfingerselfbath
            "Never mind.":
                scene bg BathroomDoor
                "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
                $ sidneylibido -= 5
                stop sound fadeout 1.0
                $ screen_on = "bathdoormap"
                call screen bathdoormap
    else:
        scene bg BathroomDoor
        with fade
        play sound Sidney01 loop
        RT "{i}Sidney must be taking a shower. Wait.... did I just hear some moaning?, uggh I've got to find a way to see what's going on in there.{/i}"
        "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
        $ sidneylibido -= 5
        stop sound fadeout 1.0
        $ screen_on = "bathdoormap"
        call screen bathdoormap

label bathafternoon:
    if daycounter >= 6:
        jump bathafternoonweekend
    if progress >= 15 and auntlibido == 10:
        jump aunthornybathroom
    if progress >= 15:
        jump auntbathspycam
    if spycaminbath == False and progress >= 6:
        while inventory.inv_amount(spycam) >= 1:
            jump spycambath
        if spycaminbath == False:
            scene bg bathroom01
            with fade
            $ screen_on = "bathmap"
            call screen bathmap
    else:
        scene bg bathroom01
        with fade
        $ screen_on = "bathmap"
        call screen bathmap

label bathafternoonweekend:
    if progress == 4:
        scene bg BathroomDoor
        with fade
        RT "{i}I think that's Mom. I'm so glad she finally came out of her room. Sounds like she's taking a shower.{/i}"
        RT "{i}If only I could see her. I should check online for some ideas on how I can spy behind locked doors.{/i}"
        $ screen_on = "bathdoormap"
        call screen bathdoormap
    if spycaminbath == False and progress >= 6:
        while inventory.inv_amount(spycam) >= 1 and progress >= 6:
            jump spycambath
        if spycaminbath == False:
            scene bg bathroom01
            with fade
            $ screen_on = "bathmap"
            call screen bathmap
    else:
        scene bg bathroom01
        with fade
        $ screen_on = "bathmap"
        call screen bathmap

label bathevening:
    if daycounter >=6:
        jump batheveningweekend
    if momlibido == 10:
        jump momhornybathroom
    if spycaminbath == True:
        jump mombathspycam
    if progress >= 6:
        scene bg BathroomDoor
        with fade
        RT "{i}That must be Mom in the shower.{/i}"
        $ screen_on = "bathdoormap"
        call screen bathdoormap
    if momgotobathroom == True:
        scene bg BathroomDoor
        with fade
        RT "{i}Mom must be getting ready for bed.{/i}"
        $ screen_on = "bathdoormap"
        call screen bathdoormap
    else:
        scene bg bathroom01
        with fade
        $ screen_on = "bathmap"
        call screen bathmap

label batheveningweekend:
    if spycaminbath == False and progress >= 6:
        while inventory.inv_amount(spycam) >= 1:
            jump spycambath
        if spycaminbath == False:
            scene bg bathroom01
            with fade
            $ screen_on = "bathmap"
            call screen bathmap
    else:
        scene bg bathroom01
        with fade
        $ screen_on = "bathmap"
        call screen bathmap

label momhornybathroom:
    if spycaminbath == True:
        scene bg BathroomDoor
        with fade
        play sound Mom02 loop
        RT "{i}Mom is taking her after school shower. Wait.... did I just hear some moaning? Let's just take a quick look.{/i}"
        menu:
            "Look.":
                jump momfingerselfbath
            "Never mind.":
                scene bg BathroomDoor
                "{i}{b}\"Mom's Libido -5\"{/b}{/i}"
                $ momlibido -= 5
                stop sound fadeout 1.0
                $ screen_on = "bathdoormap"
                call screen bathdoormap
    else:
        scene bg BathroomDoor
        with fade
        play sound Mom02 loop
        RT "{i}That must be Mom in the shower. Wait.... did I just hear some moaning?, uggh I've got to find a way to see what's going on in there.{/i}"
        "{i}{b}\"Mom's Libido -5\"{/b}{/i}"
        $ momlibido -= 5
        stop sound fadeout 1.0
        $ screen_on = "bathdoormap"
        call screen bathdoormap

label bathnight:
    if daycounter >= 6:
        jump bathnightweekend
    if spycaminbath == False and progress >= 6:
        while inventory.inv_amount(spycam) >= 1:
            jump spycambath
        if spycaminbath == False:
            scene bg bathroom01
            with fade
            $ screen_on = "bathmap"
            call screen bathmap
    else:
        scene bg bathroom01
        with fade
        $ screen_on = "bathmap"
        call screen bathmap

label bathnightweekend:
    if spycaminbath == False:
        while inventory.inv_amount(spycam) >= 1 and progress >= 6:
            jump spycambath
        if spycaminbath == False:
            scene bg bathroom01
            with fade
            $ screen_on = "bathmap"
            call screen bathmap
    else:
        scene bg bathroom01
        with fade
        $ screen_on = "bathmap"
        call screen bathmap

label toilet:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    scene bg bathroom01
    RT "{i}I'm alright for now.{/i}"
    $ screen_on = "bathmap"
    call screen bathmap

label shower:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    scene bg bathroom01
    RT "{i}No time for a shower.{/i}"
    $ screen_on = "bathmap"
    call screen bathmap

##########  KITCHEN  ##############  KITCHEN  ###############  KITCHEN  #######################  KITCHEN  ##################

label kitchen:
    if inventory.inv_amount(melatonin) == 1:
        jump spikethetea
    if timeofdaycounter == 1:
        jump kitchenearlymorning
    elif timeofdaycounter == 2:
        jump kitchenmorning
    elif timeofdaycounter == 3:
        jump kitchenafternoon
    elif timeofdaycounter == 4:
        jump kitchenevening
    else:
        jump kitchennight

label kitchenearlymorning:
    if daycounter >= 6:
        jump kitchenearlymorningweekend
    if progress >= 15 and not mandy_at_school and not mandy_breakfast:
        jump mandy_school_breakfast
    if will_visit and not will_breakfast:
        jump breakfast_for_will
    if progress >= 4:
        jump breakfast_events
    else:
        scene bg Kitchen01
        with fade
        $ screen_on = "kitchenmap"
        call screen kitchenmap

label kitchenearlymorningweekend:
    if progress == 1:
        while momfirstmorning == False:
            scene bg MomSleepIsland
            with fade
            RT "{i}.... oh, Mom must have fallen asleep waiting for her tea to boil.{/i}"
            RT "{i}She still hasn't changed out of her nightgown.{/i}"
            menu:
                "Peek":
                    scene bg IslandPeek
                    play music SexMusic
                    RT "{i}I still can't believe she got after me this morning for sleeping in my underwear.{/i}"
                    RT "{i}I mean look at her, exposing herself all over the house. {p}She must have been up most of the night worrying.{/i}"
                    RT "{i}I'll just leave her phone on the counter next to her.{/i}"
                    $ momfirstmorning = True
                    scene bg MomSleepKitchen
                    with fade
                    play music Honey
                    $ screen_on = "kitchenmapsleep"
                    call screen kitchenmapsleep
        if progress == 1:
            scene bg MomSleepKitchen
            with fade
            $ screen_on = "kitchenmapsleep"
            call screen kitchenmapsleep
    if progress >= 4:
        jump breakfast_events
    else:
        scene bg Kitchen01
        with fade
        $ screen_on = "kitchenmap"
        call screen kitchenmap

label kitchenmorning:
    if daycounter >= 6:
        jump kitchenmorningweekend
    if aunts_new_uniform == True and aunt_day_off == False:
        jump assign_chores
    else:
        scene bg Kitchen01
        with fade
        $ screen_on = "kitchenmap"
        call screen kitchenmap

label kitchenmorningweekend:
    scene bg Kitchen01
    with fade
    $ screen_on = "kitchenmap"
    call screen kitchenmap

label kitchenafternoon:
    if daycounter >= 6:
        jump kitchenafternoonweekend
    else:
        scene bg Kitchen01
        with fade
        $ screen_on = "kitchenmap"
        call screen kitchenmap

label kitchenafternoonweekend:
    if sidneyfingerlaurenprogress >= 2:
        jump sidneyinthekitchen
    else:
        scene bg Kitchen01
        with fade
        $ screen_on = "kitchenmap"
        call screen kitchenmap

label kitchenevening:
    if cosplayoutfitcounter >= 3 and daycounter != 6 and commissioned_hp_outfit:
        jump ph_cosplayfitting
    if aunt_visit_counter >= 2 and bobby_says_bye == True and aunt_second_visit == False and daycounter != 6:
        jump sad_aunt
    if aunt_visit_counter == 10 and aunt_first_visit == False and daycounter != 6:
        jump bitchy_aunt
    if cosplayoutfitcounter >= 3 and daycounter != 6 and progress == 13:
        jump wr_cosplayfitting
    if cosplayoutfitcounter >= 3 and daycounter != 6 and progress == 10:
        jump secondcosplayfitting
    if progress >= 8:
        jump sidneyinthekitchen
    if cosplayoutfitcounter >= 3 and daycounter != 6:
        jump kitchencosplayfitting
    if daycounter >= 6:
        jump kitcheneveningweekend
    if sidneyfingerlaurenprogress >= 2:
        jump sidneyinthekitchen
    if progress == 5:
        jump sidneycomeshome
    else:
        scene bg Kitchen01
        with fade
        $ screen_on = "kitchenmap"
        call screen kitchenmap

label kitcheneveningweekend:
    if sidneyfingerlaurenprogress >= 2:
        jump sidneyinthekitchen
    if progress == 2:
        while firstdinner == False:
            scene bg Kitchen01
            with fade
            M "Oh, there you are, honey. Please come sit down and have some dinner."
            $ firstdinner = True
            menu:
                "Have Dinner":
                    jump dinnerfirst
        if progress == 2:
            scene bg Kitchen01
            with fade
            $ screen_on = "kitchenmap"
            call screen kitchenmap
    elif progress >= 4:
        while almostmeltdown == False:
            scene bg DrinkingKitchenMom
            with fade
            RT "{i}Oh good, Mom is finally up and about, I wonder if she's doing any better.{/i}"
            $ almostmeltdown = True
            $ momgotobathroom = True
            scene bg MomDrinkingKitchen01
            with fade
            menu:
                "Hey Mom, it's good to see you up and about!":
                    M "Oh, hi honey, yes, I'm doing much better now."
                    R "What are you drinking?"
                    M "Oh, just a little wine to help me with my hangover."
                    R "Is putting more of what caused your hangover into your body really the best way to treat a hangover?"
                    scene bg MomDrinkingKitchen04
                    with dissolve
                    M "Haha.... yeah, it's called the hair of the dog remedy."
                    R "Hair of the dog?"
                    M "Yeah I'm not really sure what it means, something about dog hair and curing rabies bites."
                    M "I just really can't deal with the symptoms of a hangover right now with the stress I'm under. So I'm just doing a little self medicating."
                    scene bg MomDrinkingKitchen05
                    with dissolve
                    R "Mom, I really want to help out with the mess we are in."
                    R "Is there anything I can do to help relieve some of your stress?"
                    M "You really are such a good boy."
                    M "You're already working at Dad's warehouse to help pay the weekly Mafia bill."
                    M "And I don't want you missing any more school than you have to. You have to graduate this year!"
                    R "You really can't think of anything else I could do to be helpful?"
                    M "Well.... If you really want to, you could make sure the dishes get done in the evening."
                    M "If I didn't have to worry about cleaning the dinner mess, I could have more time for grading papers and getting my lessons ready."
                    R "Sure, I can do that."
                    M "That would be so great!"
                    M "But don't stress too much if you don't have time, I'll take care of it if you're too busy."
                    R "Ok, Mom."
                    scene bg MomDrinkingKitchen01
                    with dissolve
                    M "Can you find yourself something to eat tonight? I just don't have it in me to make dinner."
                    R "Sure, Mom."
                    M "Thanks, honey. I'm going to go to bed early tonight."
                    M "Good night sweety. See you in the morning."
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    $ momaffection += 1
                    RT "{i}Oh Man! I don't think I've ever seen Mom this stressed out. She's trying to put on a strong face, but I can see the worry in her eyes.{/i}"
                    RT "{i}If I can replace all the things Dad did for her, I think she would be relaxed and happy again.{/i}"
                    RT "{i}All I have to do is get the cash flowing into the household. Which will be no easy thing.{/i}"
                    RT "{i}But that seems to be the only contribution he was making.{/i}"
                    RT "{i}He and Mom hardly even talk to each other anymore.{/i}"
                    RT "{i}So maybe I can be everything to her that he wasn't.{/i}"
                    $ screen_on = "kitchenmap"
                    call screen kitchenmap
                "Are you drinking again?!":
                    scene bg MomDrinkingKitchen03
                    with dissolve
                    M "And how is that any of your business?"
                    R "Mom! You drank all night, and you've been drinking all day."
                    "{i}{b}\"Mom's Affection -1\"{/b}{/i}"
                    $ momaffection -= 1
                    M "Yeah.... well.... my husband is in jail, we're being investigated by the FBI, I have no money to go shopping, I have to pay the Mafia off every week,"
                    M "I have to go back to stripping to make enough money to pay them off, oh, and on top of all that, my son attended my grand return strip show!"
                    M "You tell me a healthy way to deal with all of that."
                    R "Well, not getting alcohol poisoning would be a good start!"
                    scene bg MomDrinkingKitchen02
                    with dissolve
                    M "Like I said, it's not any of your business, but since you feel you need to intrude into my business, I'm only drinking a little so my hangover won't be so bad."
                    R "Is putting more of what caused your hangover into your body really the best way to treat a hangover?"
                    M "It's not a great method, but it seems to have some effect."
                    M "It's called the hair of the dog remedy, or something like that."
                    R "Hmmm.... well do you promise me you won't drink anymore today?"
                    M "I don't have to promise you anything!"
                    R "Mom! I'm just really worried about you! I know you're under a lot of stress."
                    R "That's why I'm going to help make everything be ok."
                    $ momsubmission += 2
                    "{i}{b}\"Mom's Submission +2\"{/b}{/i}"
                    scene bg MomDrinkingKitchen05
                    with dissolve
                    M "Oh, honey! You don't need to take that kind of responsibility on yourself."
                    R "I really want to help make all of these changes easier on you!"
                    M "You really are such a good boy."
                    M "You're already working at your dad's warehouse to help pay the weekly Mafia bill."
                    M "And I don't want you missing any more school than you have to. You have to graduate this year!"
                    R "You really can't think of anything else I could do to be helpful?"
                    M "Well.... If you really want to, you could make sure the dishes get done in the evening."
                    M "If I didn't have to worry about cleaning the dinner mess, I could have more time for grading papers and getting my lessons ready."
                    R "Sure, I can do that."
                    M "That would be so great!"
                    M "But don't stress too much if you don't have time, I'll take care of it if you're too busy."
                    R "Ok, Mom."
                    scene bg MomDrinkingKitchen01
                    with dissolve
                    M "Can you find yourself something to eat tonight? I just don't have it in me to make dinner."
                    R "Sure, Mom."
                    M "Thanks, honey. I'm going to go to bed early tonight."
                    M "Good night sweety. See you in the morning."
                    RT "{i}Oh Man! I don't think I've ever seen Mom this stressed out. She's trying to put on a strong face, but I can see the worry in her eyes.{/i}"
                    RT "{i}If I can replace all the things my dad did for her, I think she would be relaxed and happy again.{/i}"
                    RT "{i}All I have to do is get the cash flowing into our household. Which will be no easy thing.{/i}"
                    RT "{i}But that seems to be the only contribution he was making.{/i}"
                    RT "{i}He and Mom hardly even talk to each other anymore.{/i}"
                    RT "{i}So maybe I can be everything to her that he wasn't.{/i}"
                    $ screen_on = "kitchenmap"
                    call screen kitchenmap
        if progress >= 4:
            scene bg Kitchen01
            with fade
            $ screen_on = "kitchenmap"
            call screen kitchenmap
    else:
        scene bg Kitchen01
        with fade
        $ screen_on = "kitchenmap"
        call screen kitchenmap

label kitchennight:
    if daycounter >= 6:
        jump kitchennightweekend
    else:
        scene bg KitchenNight
        with fade
        $ screen_on = "kitchenmapnight"
        call screen kitchenmapnight

label kitchennightweekend:
    scene bg KitchenNight
    with fade
    $ screen_on = "kitchenmapnight"
    call screen kitchenmapnight

label dishes:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    if progress == 1:
        scene bg MomSleepKitchen
        RT "{i}No dishes to do right now.{/i}"
        $ screen_on = "kitchenmapsleep"
        call screen kitchenmapsleep
    elif timeofdaycounter == 5:
        scene bg KitchenNight
        RT "{i}It's too late to do dishes right now.{/i}"
        jump kitchen
    elif daycounter >= 4 and timeofdaycounter == 4 and progress == 4:
        scene bg RyanDishes
        L "[ryan] can you come in to the lounge and help me!"
        scene bg LaurenRemoteSearch01
        with fade
        play music SexMusic
        RT "{i}What did I just walk in on? It's like Mom and Lauren are purposely trying to be cock-teases lately.{/i}"
        RT "{i}Has it always been like this, and now I'm just starting to notice? I'm sure I'm reading way more into this than I should.{/i}"
        menu:
            "Lauren, what the hell are you doing?":
                $ persistent.gal_Lauren_2 = True
                scene bg LaurenRemoteSearch02
                with dissolve
                L "I'm looking for the TV remote."
                L "Do you know where it is?"
                R "I'm sorry I haven't seen it."
                $ progress = 5
                L "Well, you were the last one to watch TV, so you must be the one who lost it."
                L "The least you can do is help me find it. Bend down here and help me look."
                scene bg LaurenRemoteSearch03
                with fade
                RT "{i}Look for the remote?{/i}"
                RT "{i}How am I supposed to concentrate on anything else besides this view right in front of me?{/i}"
                RT "{i}Hmmm.... I wonder.... {/i}"
                scene bg LaurenRemoteSearch04
                with fade
                RT "{i}Oh my God, I can!{/i}"
                RT "{i}I can kind of smell her pussy from this close.{/i}"
                RT "{i}I've never smelled a pussy before, I kind of like it.{/i}"
                RT "{i}I've got to get closer.{/i}"
                scene bg LaurenRemoteSearch05
                with dissolve
                RT "{i}Wow! That smells incredible!{/i}"
                RT "{i}I wish I could taste it.{/i}"
                RT "{i}It just turns me on so much!{/i}"
                L "Well, I don't see the remote in this corner, I'm coming back."
                R "Wait!"
                scene bg LaurenRemoteSearch06
                with dissolve
                with vpunch
                R "Mmphh..."
                scene bg LaurenRemoteSearch07
                with fade
                scene bg LaurenRemoteSearch06
                with fade
                scene bg LaurenRemoteSearch07
                with fade
                L "[ryan]?.... Is that your face in my ass?"
                L "[ryan]?..."
                "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                $ laurenlibido += 1
                scene bg LaurenRemoteSearch06
                with fade
                R "Uhh.... yeah.... sorry. I was just looking for the remote under this couch cushion, and didn't realize I was that close to you until you backed up."
                RT "{i}Oh my God, it smells so good I can almost taste it.{/i}"
                L "Well, would you mind removing it?"
                R "Oh yeah.... of course."
                if laurenanger >= 1:
                    scene bg LaurenWatchTV01
                    with fade
                    L "Well, that was a little awkward!"
                    R "Only if you make it. It was just an accident."
                    L "I guess."
                    R "So do you want to watch some TV?"
                    $ laurenangrytv = True
                    L "I'm still pissed off at you remember."
                    L "Ugghh.... I'm just going to go to my room."
                    scene bg FamilyRoom01
                    with fade
                    play music Honey
                    $ screen_on = "loungemap"
                    call screen loungemap
                else:
                    scene bg LaurenWatchTV02
                    with fade
                    R "Sorry, that was a little awkward!"
                    L "Only if you let it be, it was just an accident."
                    R "Yeah.... I guess so."
                    L "So do you want to watch TV with me?"
                    R "Ok, what are you watching?"
                    L "I'm just starting season one of \"Game of Thots\"."
                    L "Have you been following this show?"
                    R "No I've just seen the first episode."
                    scene bg LaurenWatchTV03
                    with dissolve
                    L "Awesome! We can watch the series together!"
                    L "All my friends love it!"
                    scene bg LaurenWatchTV06
                    with dissolve
                    RT "{i}I wonder if this is a little too explicit for Lauren?{/i}"
                    scene bg LaurenWatchTV05
                    with fade
                    RT "{i}Wow! I can't believe what they can get away with on TV anymore! This is awesome!{/i}"
                    scene bg LaurenWatchTV04
                    with fade
                    R "Man, that episode was intense! Lauren are you ok? You seem a little flushed."
                    L "Oh yeah, I'm fine. I was just a little surprised at that brother sister sex scene."
                    L "This show almost makes incest seem normal, like it's no big deal or something."
                    R "Yeah, well incest is only bad when society says it's bad. There have been lots of times in history where it was perfectly accepted."
                    L "I wouldn't say lots of times."
                    R "Well, not a ton, but to me it's like being gay. If two people are in love with each other, why do people think they have the right to tell them they can't be in love?"
                    L "I don't know it just seems really weird."
                    R "Only because you've been told all your life it's weird."
                    LT "{i}Hmmmm.... I'll have to think about that one.... {/i}"
                    $ laurenlibido += 1
                    $ laurenaffection += 1
                    "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                    $ timeofdaycounter += 1
                    $ tvfirsttimelauren = True
                    play music Honey
                    jump loungenightweekend
    elif timeofdaycounter == 4:
        jump dishesevening
    else:
        scene bg Kitchen01
        RT "{i}No dishes to do right now.{/i}"
        jump kitchen

label dishesevening:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    if almostmeltdown == True:
        while daycounter == 6:
            scene bg Kitchen01
            RT "{i}No time, the DeCapos will be here any minute.{/i}"
            $ screen_on = "kitchenmap"
            call screen kitchenmap
        if almostmeltdown == True:
            scene bg RyanDishes
            with fade
            RT "{i}Is a little extra affection from Mom even worth all this work?{/i}"
            "{i}\'Mom's Affection +1\"{/i}"
            $ momaffection += 1
            $ timeofdaycounter += 1
            jump kitchen
    else:
        scene bg Kitchen01
        RT "{i}Nah.... I don't want to do any dishes right now.{/i}"
        $ screen_on = "kitchenmap"
        call screen kitchenmap

label sidneycomeshome:
    scene bg Kitchen01
    with fade
    M "Hey honey, come sit down. We're having pizza for dinner."
    menu:
        "Go sit down":
            scene bg SidneyComesHome01
            with fade
            M "I hope you guys are hungry."
            $ progress = 6
            menu:
                "Ask Mom about her day":
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    $ momaffection += 1
                    M "Oh, my day was fine. How did you think my lesson on Oedipu___"
                    S "AAHHAAHHAHHHEMMMMM..."
                    jump sidneyenters
                "Ask Lauren about her day":
                    "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                    $ laurenaffection += 1
                    L "OMG [ryan].... so Kenzie was so funny today after PE she was all like___"
                    S "AAHHAAHHAHHHEMMMMM..."
                    jump sidneyenters

label sidneyenters:
    scene bg SidneyComesHome02
    with dissolve
    $ sidneypictureprogress = 2
    M "Oh my God, look everyone, Sidney is home!"
    M "It's so good to see you!"
    M "How's everything going at school?"
    scene bg SidneyComesHome03
    with dissolve
    S "How's everything going at school?"
    S "How's everything going at school!!!?"
    S "If you'd answer your phone you would know how everything is going at school!"
    M "I'm sorry honey, but I've been a little indisposed!"
    L "{i}(whispers){/i} More like drunk!"
    R "{i}(whispers){/i} Lauren, shut up!"
    S "And what about you Lauren? Why did you keep ignoring my calls?"
    L "My friend Brittney has been going through a messy breakup and has needed my support!"
    L "I haven't exactly had time to have any long converstations with anyone else."
    S "Long conversations!? I just needed you to get Mom for me!"
    R "You could have called me."
    S "I never call you. I don't even think I have your number!"
    RT "{i}Ouch.... {/i}"
    M "Honey! Please just sit and try to calm down. Then you can tell us what's wrong."
    scene bg SidneyComesHome04
    with dissolve
    S "I've been kicked out of school!"
    M "What?"
    S "They said the check for this coming semester's tuition bounced, and they can't keep on students who don't pay their bills."
    S "They kicked me out of the dorm, took away my meal plan."
    S "It was soooo embarassing!"
    S "So, I tried to call Dad because he takes care of my tuition and housing."
    S "But all I get when I call Dad is a message that his phone's been disconnected.!"
    S "Mom? Where's Dad and why can't I get a hold of him?"
    scene bg SleepBlack
    with fade
    "Mom tells Sidney about the events that took place over the weekend."
    "10 minutes later."
    scene bg SidneyComesHome04
    with fade
    S "Wow! That is unbelievable! It sounds like a bad plotline for a crappy Mafia movie, or a bad computer game!"
    M "Oh yes!"
    L "Absolutely!"
    R "The worst!"
    S "So would it help if I came and served drinks with you at your weekend Mafia jo..."
    M "NOOO!.... No no.... no.... thank you. I don't want my girls around the Mafia type men."
    scene bg SidneyComesHome05
    with dissolve
    L "You mean Mafia type men, as in men like Dad?"
    M "No, your dad isn't in the Mafia. He just works sometimes with the Mafia."
    M "Anyways, it goes to show that crime doesn't pay."
    M "Honey, I will feel much better if you can find a better way to make money than working at your father's warehouse."
    R "Yeah, well I'm trying to figure something else out, so I'll let you know when I do."
    L "Well, nobody hold your breath."
    R "Suck a dick!"
    M "[ryan]! Language! Please!"
    S "So can I have my old bedroom back?"
    L "You mean my bedroom? No way! I'm not moving back in with [ryan], we're too old now. Plus I think [ryan] is kind of a pervert."
    R "No I'm not!"
    RT "{i}She's got me pegged.{/i}"
    scene bg SidneyComesHome06
    with dissolve
    M "No, Sidney is right. He and Lauren have matured too much to share a room now. You're going to have to move into Lauren's room."
    L "But Mom, we got rid of her bed."
    M "Yes, and bought you a nice big queen size bed. You're going to have to share it with Sidney."
    L "But, Mom..."
    M "We all have to make sacrifices."
    L "Ok, fine."
    M "Now let's eat before our food gets any colder."
    scene bg Kitchen01
    with fade
    $ screen_on = "kitchenmap"
    call screen kitchenmap

label spikethetea:
    $ laurenpictureprogress = 7
    $ sidneypictureprogress = 6
    scene bg Kitchen01
    with fade
    RT "{i}Ok, I have the melatonin, now I need to figure out how to drug the girls without drugging myself.{/i}"
    menu:
        "Look around":
            scene bg SpikeTheTea01
            with fade
            RT "{i}Ok, coffee? No.... I drink that.{/i}"
            RT "{i}Sugar?.... No.... {/i}"
            RT "{i}Tea?.... Perfect.{/i}"
            RT "{i}All the girls drink a cup of tea before bed.{/i}"
            RT "{i}I've just got to grind it up, and mix it in.{/i}"
            scene bg SpikeTheTea02
            with dissolve
            RT "{i}Now I just wait for tonight to see how well it works.{/i}"
            $ inventory.drop(melatonin)
            $ tookmelatonin = True
            jump kitchen

label sidneyinthekitchen:
    if sidneyanger >= 1:
        scene bg SidneyInKitchen
        with fade
        menu:
            "Talk to Sidney":
                scene bg SidneyKitchen01
                with fade
                S "What do you want pervert?"
                R "I just wanted to talk with you."
                scene bg SidneyKitchen04
                with dissolve
                S "Yeah, well besides me being extremely busy, I'm also still pretty pissed off at you."
                S "So why don't you just go piss up a rope."
                R "Ok, fine I'm leaving."
                S "Not soon enough!"
                scene bg SidneyInKitchen
                with fade
                $ screen_on = "sidneykitchenmap"
                call screen sidneykitchenmap
            "Never mind":
                $ screen_on = "sidneykitchenmap"
                call screen sidneykitchenmap
    if commissioned_hp_outfit and sidneymakingcosplay:
        jump im_working_on_it
    if blackmailed_mom_matt and commissioned_hp_outfit == False and sidneymakingcosplay == False:
        jump commission_ph_outfit
    if blackmailed_mom_megan and commissioned_hp_outfit == False and sidneymakingcosplay == False:
        jump commission_ph_outfit
    if progress == 13 and sidneymakingcosplay == True:
        jump im_working_on_it
    if progress == 13 and sidneymakingcosplay == False:
        jump commission_wr_outfit
    if progress == 10 and sidneymakingcosplay == False:
        jump commissionsecondoutfit
    if chatwithsidney == False:
        scene bg SidneyInKitchen
        with fade
        menu:
            "Talk to Sidney":
                scene bg SidneyKitchen01
                with fade
                $ chatwithsidney = True
                R "Hey Sidney, what's up?"
                S "Just a second, let me just finish this up.... and.... done."
                scene bg SidneyKitchen03
                with dissolve
                S "What can I do for you?"
                RT "{i}Oh, shit.... I can see up her skirt.... {/i}"
                menu:
                    "Try to keep eye contact":
                        R "Oh, nothing, just wondering what you're up to."
                        S "Oh, I'm just finishing up some design work for a cosplay outfit I was going to make for Lauren."
                        R "Cosplay?.... I didn't know Lauren was into that."
                        S "I don't think she is, but our cousin Mandy asked her to go to the Comic-Con Expo, and begged her to dress in cosplay with her."
                        R "I didn't know you knew how to make cosplay costumes."
                        scene bg SidneyKitchen02
                        with dissolve
                        S "Well, what do you think I've been doing at college dipshit!"
                        R "I don't know, like fancy dresses and shit."
                        scene bg SidneyKitchen03
                        with dissolve
                        S "Well, I have been doing that too, but I've also been studying all forms of fashion."
                        S "Designing some cosplay outfits isn't anything too out there, considering how far out some of the avant-garde styles can be."
                        R "I don't know what that means."
                        S "Avant-garde is just fashion that is meant to push boundaries, or just be outside of the norm."
                        S "You know like hmmm.... like the stuff Mugatu wears on the movie Zoolander?"
                        R "Oh right gotcha..."
                        RT "{i}Is she flashing me on purpose, to see if I'll look?{/i}"
                        RT "{i}This is just cruel.{/i}"
                        menu:
                            "Just a really quick peek":
                                scene bg SidneyKitchen05
                                with dissolve
                                $ renpy.pause (1.5)
                                scene bg SidneyKitchen03
                                with dissolve
                                RT "{i}Wow! That was awesome! I don't think she noticed.{/i}"
                                jump sidneyinthekitchencontinued
                            "Don't risk it":
                                jump sidneyinthekitchencontinued
            "Never mind":
                scene bg SidneyInKitchen
                $ screen_on = "sidneykitchenmap"
                call screen sidneykitchenmap
    if sidneymakingcosplay == True:
        scene bg SidneyInKitchen
        with fade
        $ renpy.pause ()
        scene bg SidneyKitchen01
        with fade
        S "I'm still working on Lauren's costume. Try back again tomorrow, maybe I'll be done by then."
        scene bg SidneyInKitchen
        with fade
        $ screen_on = "sidneykitchenmap"
        call screen sidneykitchenmap
    else:
        scene bg SidneyInKitchen
        with fade
        menu:
            "Talk to Sidney":
                scene bg SidneyKitchen01
                with fade
                S "Hey [ryan], what can I do for you?"
                R "Nothing, just felt like talking with you."
                if talked_about_hp:
                    scene bg NSidneyKitchen03
                    with dissolve
                else:
                    scene bg SidneyKitchen03
                with dissolve
                S "Sorry little brother, but right now I'm really busy trying to finish up some designs."
                S "Come find me again when I'm not so busy."
                if talked_about_hp:
                    RT "{i}I can't believe she enjoys flashing me her naked pussy so much!{/i}"
                    scene bg NSidneyKitchen09
                    with dissolve
                    $ renpy.pause (0.3)
                    scene bg NSidneyKitchen03
                    with dissolve
                else:
                    RT "{i}She's flashing me again!{/i}"
                    RT "{i}Is she doing this on purpose?{/i}"
                    RT "{i}Or could she really be this clueless.{/i}"
                R "Ok, I'll find you again soon."
                scene bg SidneyInKitchen
                with fade
                $ screen_on = "sidneykitchenmap"
                call screen sidneykitchenmap
            "Give her money for Lauren's cosplay outfit." if money >= 400 and progress ==7:
                jump givesidneymoneyforcosplay
            "Ask her to work at club." if sidney_took_job and sidneys_working == False and daycounter != 1 and daycounter != 6:
                jump please_go_work
            "Never mind":
                $ screen_on = "sidneykitchenmap"
                call screen sidneykitchenmap

label sidneyinthekitchencontinued:
    scene bg SidneyKitchen03
    S "I don't really know why I'm wasting my time designing it though.... It will never get made."
    R "What?.... Why not?"
    S "The kind of stuff I need for cosplay costumes are expensive."
    S "Now that I've been cut off from Dad's credit card.... I don't have a job yet, or any way to pay for the materials."
    S "Lauren's just going to have to go without a costume."
    R "Well, how much does it cost? Maybe I could pay for it."
    S "Well, I was going to charge Dad $500 for it."
    R ".... Hack.... cough.... wheeze.... did you just say $500 for a costume?"
    scene bg SidneyKitchen02
    with dissolve
    S "Haha.... yeah, but that included my labor costs. If it was just materials it will only cost $250."
    R "Wow!"
    S "Haha.... I know! Why do you think I wanted to get into fashion design. There is some serious money to be made if you do it right."
    scene bg SidneyKitchen03
    with dissolve
    R "So, to make the outfit, you're going to need $250?"
    S "At least $400."
    R "But you said..."
    S "I love Lauren, but I'm not going to go to all that work just for charity."
    S "Making a costume is a really big job."
    R "Ok, so if I can get you $400, you will go ahead and make Lauren her costume?"
    S "Yeah I guess, but why are you so interested in helping Lauren?"
    R "Well.... to make her happy."
    S "Yeah.... I don't buy it. That can't be your only motivation."
    S "What else is in it for you?"
    R "Honestly?.... I guess I just want to show our family that I can take care of them..."
    R "I want our family to be able to continue living normally while Dad is in prison."
    R "Dad told me I'm the man of the house now, so I want to prove that I'm up to the..."
    S "Pffff.... pffff.... pffffffff..."
    R "What the?..."
    scene bg SidneyKitchen02
    with dissolve
    S "HAAHAAHAA.... hahahah!!!"
    R "What?"
    S "Hahaha.... you.... think you.... can replace Dad?.... Hahaha."
    R "Well, no.... but I'm going to try to..."
    S "HAhahahah.... do you know how hard he's had to work to build his business?..."
    R "Well, I know it won't be easy but..."
    S "Hahaha.... won't be easy?.... Hahahah.... you're in high school.... hahaha."
    R "Stop laughing!.... It's not that funny!"
    S "Hahahahahahha.... I'm sorry.... hahahahha.... I can't stop thinking about you.... hahhahah..."
    S "I suppose you will want Lauren and me to call you daddy?!.... Hahahhahhah..."
    RT "{i}What a bitch! I was trying to bare my soul to her!{/i}"
    RT "{i}Tried to resist looking at her partially exposed pussy!{/i}"
    RT "{i}And she has the nerve to just laugh at me?.... {/i}"
    RT "{i}I should just take a look as payment for her making fun of me.{/i}"
    menu:
        "Take a look":
            scene bg SidneyKitchen05
            with dissolve
            S "Hahahahahha..."
            RT "{i}If she can get so much pleasure out of me.... {/i}"
            RT "{i}Than I'm going to enjoy myself too.{/i}"
            S "Hahahahh..."
            "{i}\"(abrubt end to laughing)\"{/i}"
            scene bg SidneyKitchen06
            with dissolve
            menu:
                "Look up":
                    scene bg SidneyKitchen04
                    with dissolve
                    S "What were you looking at!?"
                    menu:
                        "What do you think, slut?!":
                            scene bg SidneyKitchen08
                            with dissolve
                            S "Oh, I see, you think just because I was laughing at you, you have the right to act like a perverted asshole?"
                            S "That just because I didn't realize I was flashing you, you have the right to look?"
                            S "Well, you'd better check your white male privilege you chauvinistic..."
                            R "Sidney.... please don't start with the liberal arts social justice BS!"
                            S "BS? That's exactly what a priviledged white boy from a patriarchal..."
                            menu:
                                "Just walk away":
                                    scene bg SidneyKitchen08
                                    S "Don't you dare walk away from me while I'm trying to educate you about..."
                                    "{i}{b}\"Sidney's Anger +10\"{/b}{/i}"
                                    $ sidneyanger += 10
                                    jump myroom
                        "Nothing!":
                            scene bg SidneyKitchen04
                            R "I'm sorry, I was just looking down because your laughing embarassed me."
                            R "And I had just barely noticed you were flashing before you did."
                            S "Well, I hope that's true, because that would be pretty fucked up if you were staring at your sister's pussy!"
                            "{i}{b}\"Sidney's Anger +5\"{/b}{/i}"
                            $ sidneyanger += 5
                            R "No I wouldn't stare at your lovely.... I mean..."
                            R "I didn't mean to say it was lovely.... I just meant that..."
                            S "[ryan], why don't you just run along and go play with your video games or something."
                            S "And let the adults actually worry about taking care of this family."
                            "{i}\"[ryan] Leaves\"{/i}"
                            scene bg SidneyKitchen07
                            with dissolve
                            ST "{i}Oh my God! Could I have been subconsciously flashing my brother on purpose?{/i}"
                            ST "{i}Is something wrong with me?{/i}"
                            ST "{i}First I'm molesting my sister in her sleep, and now this.{/i}"
                            ST "{i}Worst of all, [ryan] seemed to like it.{/i}"
                            ST "{i}Ha the look on his face when I caught him.{/i}"
                            ST "{i}I don't buy that it was an accident.{/i}"
                            ST "{i}But am I just as perverted as him?.... {/i}"
                            "{i}{b}\"Sidney's Libido +3\"{/b}{/i}"
                            $ sidneylibido += 3
                            scene bg SidneyInKitchen
                            with fade
                            $ screen_on = "sidneykitchenmap"
                            call screen sidneykitchenmap
        "Stay Strong":
            scene bg SidneyKitchen03
            with dissolve
            S "Oh my.... I'm sorry.... I really am sorry for laughing."
            S "That just really hit my funny bone."
            R "Yeah, well laugh all you want!"

            R "Once I figure out how to provide for this family, you will have to come to me for your spending money."
            R "And thanks for the suggestion, when you want money from me in the future, I'll make you call me daddy to get it."

            "{i}\"[ryan] storms out\"{/i}"
            scene bg SidneyKitchen07
            with dissolve
            ST "{i}Wow, I think I really pissed him off.{/i}"
            ST "{i}He sure looked determined when he left.{/i}"
            ST "{i}It made me almost believe him when he says he's going to provide for the family.{/i}"
            ST "{i}Shit, if he succeeds, would I really be willing to call him daddy to get money from him?{/i}"
            "{i}\"Sidney's Submission +1\"{/i}"
            $ sidneysubmission += 1
            ST "{i}I wonder if [ryan] understands the sexual connotation of a woman calling him daddy.{/i}"
            "{i}{b}\"Sidney's Libido +1\"{/b}{/i}"
            $ sidneylibido += 1
            jump myroom

######  JACKY'S ROOM  ###################  JACKY'S ROOM  ########################  JACKY'S ROOM  ######################MOM#ROOM

label momroom:
    if timeofdaycounter == 1:
        jump momearlymorning
    elif timeofdaycounter == 2:
        jump mommorning
    elif timeofdaycounter == 3:
        jump momafternoon
    elif timeofdaycounter == 4:
        jump momevening
    else:
        jump momnight

label momearlymorning:
    if daycounter >= 6:
        jump momearlymorningweekend
    if momanger >= 1:
        jump momangryroom
    if momlibido == 10:
        jump momhornybedroom
    if spycaminmomroom == True:
        jump momspycamroom
    if progress >= 3:
        scene bg MomDoor
        with fade
        RT "{i}She's always got her door locked in the morning when she does yoga and gets ready for the day. If only there was some way to see her.{/i}"
        $ screen_on = "momdoormap"
        call screen momdoormap
    else:
        scene bg MomsRoom
        with fade
        $ screen_on = "momsmap"
        call screen momsmap

label momearlymorningweekend:
    if momanger >= 1:
        jump momangryroom
    if momlibido == 10:
        jump momhornybedroom
    if spycaminmomroom == True:
        jump momspycamroom
    if progress >= 3:
        scene bg MomDoor
        with fade
        RT "{i}She's always got her door locked when she's getting ready in the morning. If only there was some way to see her.{/i}"
        $ screen_on = "momdoormap"
        call screen momdoormap
    else:
        scene bg MomsRoom
        with fade
        $ screen_on = "momsmap"
        call screen momsmap

label mommorning:
    if daycounter >= 6:
        jump mommorningweekend
    if spycaminmomroom == False and inventory.inv_amount(spycam) >= 1 and progress >= 6:
        jump spycammomroom
    else:
        scene bg MomsRoom
        with fade
        $ screen_on = "momsmap"
        call screen momsmap

label mommorningweekend:
    if spycaminmomroom == False and inventory.inv_amount(spycam) >= 1 and progress >= 6:
        jump spycammomroom
    if progress == 3:
        scene bg MomDoor
        with fade
        RT "{i}Huh.... It's late morning, and Mom still hasn't come out of her room. That's pretty unusual for her.{/i}"
        RT "{i}I'd better check on her.{/i}"
        menu:
            "Knock on her door":
                $ mompictureprogress = 4
                scene bg MomDoor
                RT "{i}Hmmm.... no answer. I don't have a key, but I'm started to get a little worried about her.{/i}"
                RT "{i}There's a sliding door outside on the patio into her room. Hopefully it's unlocked.{/i}"
                scene bg DrunkMomRoom01
                with fade
                play music SexMusic
                RT "{i}Bingo.... {/i}"
                RT "{i}Looks like she's passed out.{/i}"
                RT "{i}Is that one of Dad's empty whiskey bottles she's cuddling?{/i}"
                RT "{i}I wonder how much of it she drank. I don't think I've actually ever seen her dead drunk before.{/i}"
                RT "{i}Last night must have been pretty traumatic for her.{/i}"
                RT "{i}She didn't even change. I can see she's still wearing the thong from last night.{/i}"
                scene bg DrunkMomRoom02
                with dissolve
                M "Mmmhhh.... who.... who's there?"
                R "Hey Mom, it's ok, it's just me."
                M "[ryan]?.... What are you doing in my room?"
                R "I was worried about you, so I came through the patio door to check on you."
                scene bg DrunkMomRoom03
                with dissolve
                M "You were worried about me?..."
                M "Really?.... I thought you hated me after last night."
                R "Hated you.... Mom.... I could never hate you!.... I love you!"
                M "Really?.... But the way you were looking at me last night when you walked in on my dance..."
                M "You looked so ashamed of me..."
                M "No boy should see their mother like that..."
                M "So, I just thought you hated me for it."
                R "Oh God, no, Mom, to be completely honest I looked that way because I was ashamed of myself."
                M "Oh, honey.... why would you be ashamed of yourself?"
                R "Because I thought you looked amazing.... , and I know that sons shouldn't think that way about their moms."
                scene bg DrunkMomRoom04
                with dissolve
                M "Oh, honey.... that's one of the cutest things I've ever heard you say."
                R "Cute?..."
                M "I mean yes.... hahaha.... boys should not think of their mothers that way, but that's very flattering to me that you thought I looked amazing."
                M "I know those horny old farts at the club like what they see, but the fact that I'm still attractive to a young man is nice for me to hear."
                M "And it's not weird to have those kind of thoughts when you see a mostly nude woman moving that way on a stripper pole."
                M "That's totally normal, so don't feel ashamed of yourself."
                scene bg DrunkMomRoom03
                with dissolve
                M "The fact that it was your mom on the pole was just a fucked up situation, that you had no control over. Oh.... sorry about my language."
                M "But just so we're clear, I want you to try and get those images of me stripping out of your head. Continuing to think about that wouldn't be normal. Just kind of creepy."
                R "Oh.... I know that."
                M "Good!"
                M "How did you get into the club?"
                R "They just let me in without even asking if I was old enough."
                MT "{i}That stupid asshole Joey!{/i}"
                R "And I just searched around until I found you."
                R "I wanted to be sure you were safe."
                scene bg DrunkMomRoom04
                with dissolve
                M "That is so chival.... chiverrll.... chivalrous of you!"
                M "What a perfect little gentleman I raised."
                R "Yeah, well Dad said I'm the man of the house now."
                R "So, I felt responsible for keeping you safe."
                M "Ok, let's get this straight. You may be the only male in the house, but I'm the man of the house so to speak! I'm responsible for this family!"
                R "Well, still.... I'm going to try to work my ass off to make sure you don't have to go back there next week."
                M "Ok honey, that's very noble of you, but don't forget that you have to go to school too. I would feel like a terrible mother if you didn't graduate again this year."
                R "Well, lucky for me you're my teacher, so you can give me extra help at home, and cover for me in the afternoons when I have to go work at Dad's warehouse."
                scene bg DrunkMomRoom03
                with dissolve
                M "Are you sure working at your dad's warehouse is such a great idea? His business is what got us into this mess in the first place."
                R "Yeah.... well.... I'm not doing anything illegal there, just doing some cleaning and light maintenance."
                M "Ok, I'm going to cover for you temporarily until we figure something else out."
                R "Thanks, Mom! I won't let you down. I'll try to make sure you never have to get on that pole again."
                R "Oh, and Mom?"
                M "Yes?..."
                R "Why is it you're so good at pole dancing?"
                M "Oh, God.... I hoped you wouldn't ask me that!"
                R "..."
                M "Well, to tell you the truth. Before I met your father I did some stripping at a night club."
                R "I figured that must have been it."
                M "Yeah, well I really wanted to go to modeling school, so I needed the money to pay for it."
                M "I also thought being on a stage in front of people would give me good experience."
                M "The money I made also kept me fed and a roof over my head."
                R "And is that where you met Dad?"
                M "Yes.... not a very romantic tale for your kids, is it?"
                R "I guess not..."
            ###
                M "So we met, he liked me a lot, kept coming in while I was working, giving me lots of tips, soon he asked me out, and not long after I was pregnant with Sidney."
                M "Once I was pregnant we had to get married, both of us coming from strict Catholic families."
                M "And then the rest just kind of fell into place."
                R "Why didn't you finish modeling school?"
                M "Your selfish, over protective, jealous dad didn't want anyone else even looking at me."
                M "Once I was his property, he only wanted me for his own eyes."
                M "Kind of hard to be a model in that situation."
                R "Well, I think you would have made an amazing model."
                scene bg DrunkMomRoom05
                with dissolve
                M "You are just the sweetest boy in the world."
                M "I need to get a hug from my new \"big man of the house and protector\"."
                scene bg DrunkMomRoom06
                with dissolve
                RT "{i}Mom's extra affectionate when she's drunk. I'll have to remember that. Ohhh this hug feels so good.{/i}"
                MT "{i}Uh oh, I think this hug might be getting [ryan] a little too excited.{/i}"
                "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                $ momlibido += 1
                $ timeofdaycounter += 1
                $ progress = 4
                M "Ok [ryan], why don't you run along."
                R "Ok, love you, Mom."
                M "Love you too."
                play music Honey
                $ screen_on = "momdoormap"
                call screen momdoormap

    else:
        scene bg MomsRoom
        with fade
        $ screen_on = "momsmap"
        call screen momsmap

label momafternoon:
    if daycounter >= 6:
        jump momafternoonweekend
    if spycaminmomroom == False and inventory.inv_amount(spycam) >= 1 and progress >= 6:
        jump spycammomroom
    else:
        scene bg MomsRoom
        with fade
        $ screen_on = "momsmap"
        call screen momsmap

label momafternoonweekend:
    if spycaminmomroom == False and inventory.inv_amount(spycam) >= 1 and progress >= 6:
        jump spycammomroom
    else:
        scene bg MomsRoom
        with fade
        $ screen_on = "momsmap"
        call screen momsmap

label momevening:
    if progress >= 15:
        jump camille_workout
    if daycounter >= 6:
        jump momeveningweekend
    if spycaminmomroom == False and inventory.inv_amount(spycam) >= 1 and progress >= 6:
        jump spycammomroom
    else:
        scene bg MomsRoom
        with fade
        $ screen_on = "momsmap"
        call screen momsmap

label momeveningweekend:
    if spycaminmomroom == False and inventory.inv_amount(spycam) >= 1 and progress >= 6:
        jump spycammomroom
    if progress == 4:
        while almostmeltdown == True:
            scene bg MomDoor
            with fade
            RT "{i}She just went in to go to bed, I should at least give her a little time to fall asleep before I try to sneak in.{/i}"
            $ screen_on = "momdoormap"
            call screen momdoormap
        if progress == 4:
            scene bg MomsRoom
            with fade
            $ screen_on = "momsmap"
            call screen momsmap
    else:
        scene bg MomsRoom
        with fade
        $ screen_on = "momsmap"
        call screen momsmap

label momnight:
    if progress >= 15:
        jump no_more_night_fun_with_mom
    if momatclub == True:
        scene bg MomRoomNight
        with fade
        $ screen_on = "momsmapnight"
        call screen momsmapnight
    if momanger >= 1:
        jump momangryroom
    if momlibido == 10:
        jump momhornybedroom
    if daycounter >= 6:
        jump momnightweekend
    elif progress >= 4:
        jump momsneakingnight
    else:
        scene bg MomRoomNight
        with fade
        $ screen_on = "momsmapnight"
        call screen momsmapnight

label momnightweekend:
    if momatclub == True:
        scene bg MomRoomNight
        with fade
        $ screen_on = "momsmapnight"
        call screen momsmapnight
    if momanger >= 1:
        jump momangryroom
    if momlibido == 10:
        jump momhornybedroom
    if progress >= 4:
        jump momsneakingnight
    else:
        scene bg MomRoomNight
        with fade
        $ screen_on = "momsmapnight"
        call screen momsmapnight

label momsneakingnight:
    if found_bathrobe:
        jump naughty_pranks_on_mom
    if look_for_bathrobe and not found_bathrobe:
        scene bg MomInBedAtNight
        with fade
        RT "{i}Not much I can do until I find and get rid of that bathrobe.{/i}"
        $ screen_on = "momsleepingnightmap"
        call screen momsleepingnightmap
    if momsubmission >= 5:
        scene bg MomInBedAtNight
        with fade
        RT "{i}I don't think the subliminal messages are having any more effect, I'll have to think of something else to make her more submissive.{/i}"
        RT "{i}With her in such a deep sleep, I could probably get away with a few naughty pranks.{/i}"
        RT "{i}That bathrobe might make things a little bit difficult though.{/i}"
        RT "{i}I Need to find where she keeps it when she's not in the room... I'll have to come back and look around later.{/i}"
        $ look_for_bathrobe = True
        $ screen_on = "momsleepingnightmap"
        call screen momsleepingnightmap
    if momprogress == 1:
        scene bg MomInBedAtNight
        with fade
        RT "{i}Oh there she is! The object of my desire!{/i}"
        menu:
            "Look closer.":
                scene bg NightSneakMom01
                with dissolve
                play music SexMusic
                $ momprogress = 2
                $ momnight = True
                RT "{i}Why does she even wear that robe? Does she think she's being modest? I've seen more skin from her in the last few days, than I have in my whole life.{/i}"
                RT "{i}Still, I wish I could see more. Maybe I should make that robe disappear.{/i}"
                RT "..."
                RT "{i}So Mom thinks she's the \"man of the house\"huh?.... I've got to prove to her that I should have that role.{/i}"
                RT "{i}I'm going to have to find a way to make more money than she does. That just seems so impossible since I'm just a high schooler, but I've got to come up with a better idea than just delivering packages for Dad.{/i}"
                RT "{i}Now that I know he's making dirty money, I'll never take over his business. But I've got to figure out how to replace his income.{/i}"
                RT "{i}I know if she keeps having to strip for the extra money each week, she'll never respect me enough for me to take charge.{/i}"
                RT "{i}I guess for now there's no real way to convince her otherwise.{/i}"
                RT "{i}Huhhh.... unless!{/i}"
                menu:
                    "Try using subliminal messages":
                        scene bg NightSneakMom02
                        with dissolve
                        RT "{i}Ok, here goes nothing.{/i}"
                        R "{i}(Whispering){/i} \"[ryan] should be man of the house.... \" \"[ryan] should be man of the house.... \" \"[ryan] should be man of the house.... \" \"[ryan] should be man of the house.... \""
                        scene bg BlurryWhite
                        with fade
                        scene bg SleepBlack
                        with fade
                        scene bg BlurryWhite
                        with fade
                        scene bg NightSneakMom02
                        with fade
                        "10 minutes later."
                        R "{i}(Whispering){/i} \"[ryan] should be man of the house.... \" \"[ryan] should be man of the house.... \" \"[ryan] should be man of the house.... \" \"[ryan] should be man of the house.... \""
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                        RT "{i}Ok, I've got to call it a night, my legs are asleep.{/i}"
                        scene bg MomInBedAtNight
                        with fade
                        play music Honey
                        $ screen_on = "momsleepingnightmap"
                        call screen momsleepingnightmap
                    "Just leave her alone, she's had a rough few days.":
                        scene bg MomInBedAtNight
                        with fade
                        play music Honey
                        $ screen_on = "momsleepingnightmap"
                        call screen momsleepingnightmap
    if momnight == False:
        scene bg MomInBedAtNight
        with fade
        RT "{i}I hope I don't wake her!{/i}"
        menu:
            "Look closer.":
                scene bg NightSneakMom01
                with dissolve
                RT "{i}Ok, let's try the subliminal messages again.{/i}"
                menu:
                    "Subliminal messages":
                        scene bg NightSneakMom02
                        with dissolve
                        play music SexMusic
                        R "{i}(Whispering){/i} \"[ryan] should be man of the house.... \" \"[ryan] should be man of the house.... \" \"[ryan] should be man of the house.... \" \"[ryan] should be man of the house.... \""
                        scene bg BlurryWhite
                        with fade
                        scene bg SleepBlack
                        with fade
                        scene bg BlurryWhite
                        with fade
                        scene bg NightSneakMom02
                        with fade
                        "10 minutes later."
                        R "{i}(Whispering){/i} \"[ryan] should be man of the house.... \" \"[ryan] should be man of the house.... \" \"[ryan] should be man of the house.... \" \"[ryan] should be man of the house.... \""
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                        $ momnight = True
                        RT "{i}Ok, I've got to call it a night, my legs are asleep.{/i}"
                        scene bg MomInBedAtNight
                        with fade
                        play music Honey
                        $ screen_on = "momsleepingnightmap"
                        call screen momsleepingnightmap
                    "Just leave her alone, she's had a rough few days.":
                        scene bg MomInBedAtNight
                        with fade
                        $ screen_on = "momsleepingnightmap"
                        call screen momsleepingnightmap
    else:
        scene bg MomInBedAtNight
        with fade
        $ screen_on = "momsleepingnightmap"
        call screen momsleepingnightmap

label momangryroom:
    if timeofdaycounter == 5:
        while spycaminmomroom == True:
            scene bg MomDoorNight
            with fade
            RT "{i}She locked her door! Mom must still be pissed off. I could take a little peek and see what she's doing.{/i}"
            menu:
                "Peek through the spy-cam.":
                    jump momspycamroommad
                "Nah, she's probably just sleeping.":
                    scene bg MomDoorNight
                    $ screen_on = "momdoornightmap"
                    call screen momdoornightmap
        if timeofdaycounter == 5:
            scene bg MomDoorNight
            with fade
            RT "{i}She locked her door! Mom must still be pissed off. I guess I better just let her sleep.{/i}"
            $ screen_on = "momdoornightmap"
            call screen momdoornightmap
    else:
        scene bg MomDoor
        RT "{i}She's always got her room locked in the morning while she does yoga and gets ready.... I wonder if she's still mad at me though.{/i}"
        RT "{i}Should I see if I can smooth things over?{/i}"
        menu:
            "Knock":
                scene bg MomMadInRoom01
                with fade
                R "Hey Mom, doing some yoga?"
                M "Honey, I really don't want to talk to you right now!"
                menu:
                    "Give her a gift":
                        if gavemomgift == False:
                            scene bg MomMadInRoom02
                            with dissolve
                            M "You bought me a gift?"
                            menu:
                                "Give her a chocolate bar" if inventory.inv_amount(chocolate) >= 1:
                                    scene bg MomMadInRoom04
                                    with dissolve
                                    M "Thank you I love chocolate!"
                                    "{i}{b}\"Mom's Anger -2\"{/b}{/i}"
                                    $ momanger -= 2
                                    $ inventory.drop(chocolate)
                                    $ gavemomgift = True
                                    if momanger >= 1:
                                        scene bg MomMadInRoom05
                                        with dissolve
                                        M "But don't think that I've forgiven you yet. Whether intentional or not, your actions were completely inappropriate."
                                        $ screen_on = "momdoormap"
                                        call screen momdoormap
                                    else:
                                        scene bg MomMadInRoom04
                                        M "Thank you honey! What kind of mom would I be if I didn't forgive you?"
                                        $ screen_on = "momdoormap"
                                        call screen momdoormap

                                "Give her Hardnlong gift card" if inventory.inv_amount(giftcard) >= 1:
                                    scene bg MomMadInRoom04
                                    with dissolve
                                    M "That's so thoughtful, especially since the FBI won't let me go shopping with any of our credit cards!"
                                    "{i}{b}\"Mom's Anger -5\"{/b}{/i}"
                                    $ momanger -= 5
                                    $ inventory.drop(giftcard)
                                    $ gavemomgift = True
                                    if momanger >= 1:
                                        scene bg MomMadInRoom05
                                        with dissolve
                                        M "But don't think that I've forgiven you yet. Whether intentional or not, your actions were completely inappropriate."
                                        $ screen_on = "momdoormap"
                                        call screen momdoormap
                                    else:
                                        scene bg MomMadInRoom04
                                        M "Thank you honey! What kind of mom would I be if I didn't forgive you?"
                                        $ screen_on = "momdoormap"
                                        call screen momdoormap
                                "Give her flowers" if inventory.inv_amount(flowers) >= 1:
                                    $ inventory.drop(flowers)
                                    if momaffection <= 50:
                                        scene bg MomMadInRoom03
                                        with dissolve
                                        M "honey, this is completely inappropriate! I'm your mom, not your girlfriend!"
                                        "{i}\"Throws them in her trash\"{/i}"
                                        M "I'm sorry, I just can't keep them."
                                        M "Maybe next time try to think of something a little less creepy."
                                        "{i}{b}\"Mom's Affection -1\"{/b}{/i}"
                                        "{i}{b}\"Mom's Anger +2\"{/b}{/i}"
                                        "{i}\"You need higher affection to gift flowers.\"{/i}"
                                        $ momanger += 2
                                        $ momaffection -= 1
                                        $ screen_on = "momdoormap"
                                        call screen momdoormap
                                    else:
                                        scene bg MomMadInRoom04
                                        with dissolve
                                        M "Oh how sweet! I love them!"
                                        M "You're such a little gentleman!"
                                        M "If I didn't know any better, I would think you were trying to put the moves on me!"
                                        $ momaffection += 1
                                        $ momanger = 0
                                        "{i}{b}\"Mom's Anger -10\"{/b}{/i}"
                                        "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                                        scene bg MomMadInRoom06
                                        M "Thank you so much!"
                                        RT "{i}Oh, wow.{/i}"
                                        $ screen_on = "momdoormap"
                                        call screen momdoormap
                                "Never mind":
                                    scene bg MomMadInRoom03
                                    with dissolve
                                    M "Honey, I'm trying to get ready. Don't bother me anymore!"
                                    "{i}{b}\"Mom's Anger +1\"{/b}{/i}"
                                    $ momanger += 1
                                    $ screen_on = "momdoormap"
                                    call screen momdoormap
                        else:
                            scene bg MomMadInRoom03
                            with dissolve
                            M "You already gave me a gift honey. Any more than that is just crossing the creep line!"
                            $ momanger += 1
                            "{i}{b}\"Mom's Anger +1\"{/b}{/i}"
                            $ screen_on = "momdoormap"
                            call screen momdoormap
                    "I just wanted to apologize":
                        scene bg MomMadInRoom03
                        with dissolve
                        M "Well, it's going to take more than just words for me to forgive you for what you did!"
                        RT "{i}I guess I better give her some time, or maybe I can get her a present so she won't be so mad.{/i}"
                        $ screen_on = "momdoormap"
                        call screen momdoormap
            "Peek through spy-cam" if spycaminmomroom == True:
                jump momspycamroommad
            "I'm just going to give her some time to cool down":
                $ screen_on = "momdoormap"
                call screen momdoormap

label momnightstand:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    if timeofdaycounter == 5 and momatclub:
        scene bg MomRoomNight
        with dissolve
        "{i}Nope.... no loose money lying around.{/i}"
        jump momroom
    elif timeofdaycounter == 5 and progress >= 4:
        scene bg MomInBedAtNight
        with dissolve
        "{i}Nope.... no loose money lying around.{/i}"
        jump momroom
    elif timeofdaycounter == 5:
        scene bg MomRoomNight
        with dissolve
        "{i}Nope.... no loose money lying around.{/i}"
        jump momroom
    else:
        scene bg MomsRoom
        RT "{i}Nope.... no loose money lying around.{/i}"
        jump momroom

label momdresser:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    if look_for_bathrobe and momatclub and not found_bathrobe and first_bfast:
        scene bg MomRoomNight
        with dissolve
        RT "{i}Surprisingly I've never really dug through her underwear.{/i}"
        RT "{i}Ahh... Yes!  I found the robe!{/i}"
        show Brobe
        RT "{i}Now I have to get rid of it, but how?...{/i}"
        RT "{i}I'll just stuff it under my bed for now.{/i}"
        RT "{i}I just better not forget to destroy the evidence later.{/i}"
        hide Brobe
        scene bg SleepBlack
        with fade
        RT "{i}There... I'm sure Mom won't think to look in that box that says \"Keep out\".{/i}"
        RT "{i}She'll have to dig through the vintage porn magazines I found in Dad's office a long time ago.{/i}"
        $ found_bathrobe = True
        jump myroom
    if look_for_bathrobe and not found_bathrobe and timeofdaycounter != 5 and first_bfast:
        scene bg MomsRoom
        with dissolve
        RT "{i}Surprisingly I've never really dug through her underwear.{/i}"
        RT "{i}Ahh... Yes!  I found the robe!{/i}"
        show Brobe
        RT "{i}Now I have to get rid of it, but how?...{/i}"
        RT "{i}I'll just stuff it under my bed for now.{/i}"
        RT "{i}I just better not forget to destroy the evidence later.{/i}"
        hide Brobe
        scene bg SleepBlack
        with fade
        RT "{i}There... I'm sure Mom won't think to look in that box that says \"Keep out\".{/i}"
        RT "{i}She'll have to dig through the vintage porn magazines I found in Dad's office a long time ago.{/i}"
        $ found_bathrobe = True
        jump myroom
    if timeofdaycounter == 5:
        while progress >= 4:
            scene bg MomInBedAtNight
            with dissolve
            "{i}Yeah, nice underwear!{/i}"
            jump momroom
        if timeofdaycounter == 5:
            scene bg MomRoomNight
            with dissolve
            "{i}Yeah, nice underwear!{/i}"
            jump momroom
    else:
        scene bg MomsRoom
        RT "{i}Why would I go through her underwear?{/i}"
        jump momroom

######  LAUREN'S ROOM  #######################  LAUREN'S ROOM  ##########################  LAUREN'S ROOM  ############################  LAUREN'S ROOM  #####################

label laurenroom:
    if timeofdaycounter == 1:
        jump laurenearlymorning
    elif timeofdaycounter == 2:
        jump laurenmorning
    elif timeofdaycounter == 3:
        jump laurenafternoon
    elif timeofdaycounter == 4:
        jump laurenevening
    else:
        jump laurenatnight

label laurenearlymorning:
    if daycounter >= 6:
        jump laurenearlymorningweekend
    if sidneyfingerlaurenprogress > 4 and spycaminlaurenroom == False and inventory.inv_amount(spycam) >= 1 and progress >= 6:
        jump spycamlaurenroom
    if sidneyfingerlaurenprogress >= 4:
        scene bg LaurenRoom01
        with fade
        $ screen_on = "laurenmap"
        call screen laurenmap
    if sidneylibido == 10:
        jump sidneyhornybedroom
    if sidneyanger >= 1:
        jump sidneyangryroom
    if progress >= 6:
        scene bg SidneySleepIn01
        with fade
        $ screen_on = "sidneysleepinmap"
        call screen sidneysleepinmap
    else:
        scene bg LaurenRoom01
        with fade
        $ screen_on = "laurenmap"
        call screen laurenmap

label laurenearlymorningweekend:
    if progress >= 15 and daycounter == 7:
        jump lauren_sleep_in
    if progress >= 15 and daycounter == 6:
        jump mandy_sleep_in
    if laurenanger >= 1 and timeofdaycounter == 3:
        jump laurenangryroom
    if sidneyfingerlaurenprogress >= 4:
        scene bg LaurenSleepIn
        with fade
        $ screen_on = "laurenmapsleepin"
        call screen laurenmapsleepin
    if sidneyanger >= 1:
        jump sidneyangryroom
    if progress >= 6:
        scene bg SidneyLaurenSleeping01
        with fade
        $ screen_on = "sidneylaurensleepingmap"
        call screen sidneylaurensleepingmap
    elif progress == 1:
        while laurenfirstmorning == False:
            scene bg LaurenInBed
            RT "{i}It's still too early for her to get up and get ready for school. She doesn't dress any more modestly than I do for bed. {p}Why is Mom only on my case about it?{/i}"
            menu:
                "Get a closer look":
                    jump peeklaurenroom
                "Why would I even think of looking?":
                    RT "{i}I should just turn her lights back off and let her get a few more minutes of sleep.{/i}"
                    $ laurenfirstmorning = True
                    scene bg LaurenSleepIn
                    with fade
                    $ screen_on = "laurenmapsleepin"
                    call screen laurenmapsleepin
        if progress == 1:
            scene bg LaurenSleepIn
            with fade
            $ screen_on = "laurenmapsleepin"
            call screen laurenmapsleepin
    else:
        scene bg LaurenSleepIn
        with fade
        $ screen_on = "laurenmapsleepin"
        call screen laurenmapsleepin

label laurenmorning:
    if daycounter >= 6:
        jump laurenmorningweekend
    if spycaminlaurenroom == False and inventory.inv_amount(spycam) >= 1 and sidneyfingerlaurenprogress > 4 and progress >= 6:
        jump spycamlaurenroom
    else:
        scene bg LaurenRoom01
        with fade
        $ screen_on = "laurenmap"
        call screen laurenmap

label laurenmorningweekend:
    if laurenanger >= 1:
        jump laurenangryroom
    if laurenlibido == 10:
        jump laurenhornybedroom
    if spycaminlaurenroom == True:
        jump laurenspycamroom
    else:
        scene bg LaurenDoor
        with fade
        RT "{i}The door's locked, Lauren must be getting dressed. I wish there was a way to spy on her. I'll have to check online for ideas.{/i}"
        $ screen_on = "laurendoormap"
        call screen laurendoormap

label laurenafternoon:
    if daycounter >= 6:
        jump laurenafternoonweekend
    if sidneyanger >= 1:
        jump sidneyangryroom
    if sidneylibido >= 10:
        jump sidneyhornybedroom
    if progress >= 6 and spycaminlaurenroom == True:
        while sawsidneychanging == False:
            jump sidneychanging
        if progress >= 6 and caught_by_sidney == False:
            jump caughtbysidney
        else:
            jump sidneyspycamroom
    if progress >= 6 and spycaminlaurenroom == False:
        while sawsidneychanging == False:
            jump sidneychanging
        if progress >= 6 and caught_by_sidney == False:
            jump caughtbysidney
    else:
        scene bg LaurenRoom01
        with fade
        $ screen_on = "laurenmap"
        call screen laurenmap

label laurenafternoonweekend:
    if progress >= 4:
        while laurenanger >= 1:
            jump laurenangryroom
        if progress >= 4:
            jump laurenroomhang
    else:
         scene bg LaurenRoom01
         with fade
         $ screen_on = "laurenmap"
         call screen laurenmap

label laurenevening:
    if daycounter >= 6:
        jump laureneveningweekend
    if laurenangrytv == True:
        while laurenanger >= 1:
            jump laurenangryroom
        if laurenangrytv == True:
            jump laurenroomhang
    if progress >= 15:
        jump mandy_study
    if spycaminlaurenroom == False and inventory.inv_amount(spycam) >= 1 and sidneyfingerlaurenprogress > 4 and progress >= 6:
        jump spycamlaurenroom
    else:
        scene bg LaurenRoom01
        with fade
        $ screen_on = "laurenmap"
        call screen laurenmap

label laureneveningweekend:
    if laurenangrytv == True:
        while laurenanger >= 1:
            jump laurenangryroom
        if laurenangrytv == True:
            jump laurenroomhang
    if progress >= 15:
        jump mandy_study
    if spycaminlaurenroom == False and inventory.inv_amount(spycam) >= 1 and sidneyfingerlaurenprogress > 4 and progress >= 6:
        jump spycamlaurenroom
    else:
        scene bg LaurenRoom01
        with fade
        $ screen_on = "laurenmap"
        call screen laurenmap

label laurenatnight:
    if progress >= 15:
        jump lauren_night
    if progress == 8:
        scene bg LaurenNightEmpty
        with fade
        RT "{i}Huh... Mandy and Lauren aren't back from their convention yet. Or maybe they are spending the night with Mandy over at Uncle Bobby's house.{/i}"
        $ screen_on = "laurennightemptymap"
        call screen laurennightemptymap
    if sawlaurensquirt == True:
        scene bg LaurenDoorNight
        with fade
        RT "{i}Her door's still locked, and after what I just saw, I'm sure it won't be opening again until morning.{/i}"
        $ screen_on = "laurendoornightmap"
        call screen laurendoornightmap
    if daycounter >= 6:
        jump laurennightweekend
    if laurenanger >= 1:
        jump laurenangryroom
    if laurenlibido == 10:
        jump laurenhornybedroom
    if sidneyfingerlaurenprogress >= 4:
        jump laurensneakingnight
    if sidneyanger >= 1:
        jump sidneyangryroom
    if tookmelatonin == True:
        jump sidneylaurensneakingnight
    if progress >= 6:
        jump sidneylaurensneakattempt
    elif progress >= 3:
        jump laurensneakingnight
    else:
        scene bg NightLauren01
        with fade
        $ screen_on = "laurenmapnight"
        call screen laurenmapnight

label laurennightweekend:
    if laurenanger >= 1:
        jump laurenangryroom
    if laurenlibido == 10:
        jump laurenhornybedroom
    if sidneyfingerlaurenprogress >= 4:
        jump laurensneakingnight
    if sidneyanger >= 1:
        jump sidneyangryroom
    if tookmelatonin == True:
        jump sidneylaurensneakingnight
    if progress >= 6:
        jump sidneylaurensneakattempt
    elif progress >=3:
        jump laurensneakingnight
    else:
        scene bg NightLauren01
        with fade
        $ screen_on = "laurenmapnight"
        call screen laurenmapnight

label laurenhornybedroom:
    if spycaminlaurenroom == True:
        while timeofdaycounter == 5:
            scene bg LaurenDoorNight
            with fade
            play sound Lauren01 loop
            RT "{i}Hmmm.... I wonder why the door is locked?{/i}"
            RT "{i}Wait.... is that Lauren moaning?{/i}"
            RT "{i}I should check it out.{/i}"
            menu:
                "Use spy-cam.":
                    jump laurenspycamroomhorny
                "Not right now.":
                    RT "{i}Sounds like things are winding down. I'm probably too late to see anything good.{/i}"
                    stop sound
                    "{i}{b}\"Lauren's Libido -5\"{/b}{/i}"
                    $ laurenlibido -= 5
                    $ screen_on = "laurendoornightmap"
                    call screen laurendoornightmap
        if spycaminlaurenroom == True:
            scene bg LaurenDoor
            with fade
            play sound Lauren01 loop
            RT "{i}Hmmm.... I wonder why the door is locked?{/i}"
            RT "{i}Wait.... is that Lauren moaning?{/i}"
            RT "{i}I should check it out.{/i}"
            menu:
                "Use spy-cam.":
                    jump laurenspycamroomhorny
                "Not right now.":
                    RT "{i}Sounds like things are winding down. I'm probably too late to see anything good.{/i}"
                    stop sound
                    "{i}{b}\"Lauren's Libido -5\"{/b}{/i}"
                    $ laurenlibido -= 5
                    $ screen_on = "laurendoormap"
                    call screen laurendoormap
    if timeofdaycounter == 5:
        while sidneyfingerlaurenprogress >= 4:
            scene bg LaurenDoorNight
            with fade
            play sound Lauren01 loop
            RT "{i}Hmmm.... I wonder why the door is locked?{/i}"
            RT "{i}Wait.... is that Lauren moaning? I've got to figure out a way to see in there!{/i}"
            $ laurenlibido -= 5
            "{i}{b}\"Lauren's Libido -5\"{/b}{/i}"
            stop sound fadeout 1.0
            $ screen_on = "laurendoornightmap"
            call screen laurendoornightmap
        if timeofdaycounter == 5:
            scene bg LaurenDoorNight
            with fade
            play sound Lauren01 loop
            RT "{i}Hmmm.... I wonder why the door is locked?{/i}"
            RT "{i}Wait.... is that Lauren moaning?.... Sidney is in there too!! What could they be doing? I've got to figure out a way to see in there!{/i}"
            $ laurenlibido -= 5
            "{i}{b}\"Lauren's Libido -5\"{/b}{/i}"
            stop sound fadeout 1.0
            $ screen_on = "laurendoornightmap"
            call screen laurendoornightmap
    else:
        scene bg LaurenDoor
        with fade
        play sound Lauren01 loop
        RT "{i}The door's locked, she must be getting dressed. {p}Wait, is that moaning I hear?{p}I'm pretty sure that's moaning.{/i}"
        "{i}{b}\"Lauren's Libido -5\"{/b}{/i}"
        $ laurenlibido -= 5
        RT "{i}I've got to figure out a way to spy on her.{/i}"
        stop sound fadeout 1.0
        $ screen_on = "laurendoormap"
        call screen laurendoormap

label sidneyhornybedroom:
    if spycaminlaurenroom == True:
        scene bg LaurenDoor
        with fade
        play sound Sidney01 loop
        RT "{i}I'm sure it's locked as usual.{/i}"
        RT "{i}Wait.... is that Sidney moaning?{/i}"
        RT "{i}I should check it out.{/i}"
        menu:
            "Use spy-cam.":
                jump sidneyspycamroomhorny
            "Not right now.":
                RT "{i}Sounds like things are winding down. I'm probably too late to see anything good.{/i}"
                stop sound
                "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
                $ sidneylibido -= 5
                $ screen_on = "laurendoormap"
                call screen laurendoormap
    else:
        scene bg LaurenDoor
        with fade
        play sound Sidney01 loop
        RT "{i}The door's locked, Sidney must be getting dressed. {p}Wait, is that moaning I hear? {p}I'm pretty sure that's moaning.{/i}"
        "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
        $ sidneylibido -= 5
        RT "{i}I've got to figure out a way to spy on her.{/i}"
        stop sound fadeout 1.0
        $ screen_on = "laurendoormap"
        call screen laurendoormap

label peeklaurenroom:
    scene bg LaurenInBed
    RT "{i}Why would I want to look closer? {p}It would take some kind of life changing event to make me want to look at my sister that way.{/i}"
    RT "{i}I should just turn her lights back off and let her get a few more minutes of sleep.{/i}"
    $ laurenfirstmorning = True
    scene bg LaurenSleepIn
    with fade
    $ screen_on = "laurenmapsleepin"
    call screen laurenmapsleepin

label laurenangryroom:
    if timeofdaycounter == 5:
        while spycaminlaurenroom == True:
            RT "{i}She locked her door! Lauren must still be pissed off.{/i}"
            menu:
                "Take a peek.":
                    jump laurenspycamroommad
                "Never mind.":
                    $ screen_on = "laurendoornightmap"
                    call screen laurendoornightmap
        if timeofdaycounter == 5:
            scene bg LaurenDoorNight
            with fade
            RT "{i}She locked her door! Lauren must still be pissed off. I guess I better just let her sleep.{/i}"
            $ screen_on = "laurendoornightmap"
            call screen laurendoornightmap
    else:
        scene bg LaurenDoor
        RT "{i}Her door's locked. Lauren's pretty pissed off at me.{/i}"
        menu:
            "Knock":
                scene bg LaurenMadInRoom01
                with fade
                L "What do you want dickwad?"
                menu:
                    "Give her a gift":
                        if gavelaurengift == False:
                            scene bg LaurenMadInRoom02
                            with dissolve
                            L "You have something for me?"
                            menu:
                                "Give her a chocolate bar" if inventory.inv_amount(chocolate) >= 1:
                                    scene bg LaurenMadInRoom04
                                    with dissolve
                                    L "Thank you I love chocolate!"
                                    "{i}{b}\"Lauren's Anger -2\"{/b}{/i}"
                                    $ laurenanger -= 2
                                    $ inventory.drop(chocolate)
                                    $ gavelaurengift = True
                                    if laurenanger >= 1:
                                        scene bg LaurenMadInRoom05
                                        with dissolve
                                        L "But this doesn't mean I'm not mad at you anymore. That was a dick move, and it's going to take me some more time to forgive you."
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap
                                    else:
                                        scene bg LaurenMadInRoom04
                                        L "Thank you brother! It's hard to stay mad for very long at someone as sweet as you!"
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap

                                "Give her Hardnlong gift card" if inventory.inv_amount(giftcard) >= 1:
                                    scene bg LaurenMadInRoom04
                                    with dissolve
                                    L "Thank you! I'm going to use it right now!"
                                    "{i}{b}\"Lauren's Anger -5\"{/b}{/i}"
                                    $ laurenanger -= 5
                                    $ inventory.drop(giftcard)
                                    $ gavelaurengift = True
                                    if laurenanger >= 1:
                                        scene bg LaurenMadInRoom05
                                        with dissolve
                                        L "But this doesn't mean I'm not mad at you anymore. That was a dick move, and it's going to take me some more time to forgive you."
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap
                                    else:
                                        scene bg LaurenMadInRoom04
                                        L "Thank you brother! It's hard to stay mad for very long at someone as sweet as you!"
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap
                                "Give her flowers" if inventory.inv_amount(flowers) >= 1:
                                    $ inventory.drop(flowers)
                                    if laurenaffection <= 50:
                                        scene bg LaurenMadInRoom03
                                        with dissolve
                                        L "What the hell kind of present is that? I'm not your girlfriend!"
                                        "{i}\"Throws them in her trash\"{/i}"
                                        L "Thanks, I hate it!"
                                        L "Maybe next time try to think of something a little less creepy."
                                        "{i}{b}\"Lauren's Affection -1\"{/b}{/i}"
                                        "{i}{b}\"Lauren's Anger +2\"{/b}{/i}"
                                        "{i}\"You need higher affection to gift flowers.\"{/i}"
                                        $ laurenanger += 2
                                        $ laurenaffection -= 1
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap
                                    else:
                                        scene bg LaurenMadInRoom04
                                        with dissolve
                                        L "Oh my gosh! I love them!"
                                        L "You're such a charmer!"
                                        L "If I didn't know any better, I would think you were trying to put the moves on me!"
                                        $ laurenanger = 0
                                        $ laurenaffection += 1
                                        "{i}{b}\"Lauren's Anger -10\"{/b}{/i}"
                                        "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                                        scene bg LaurenMadInRoom06
                                        L "Thank you so much!"
                                        RT "{i}Oh, wow.{/i}"
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap
                                "Never mind":
                                    scene bg LaurenMadInRoom03
                                    with dissolve
                                    L "OMG! You made me get up for that."
                                    "{i}{b}\"Lauren's Anger +1\"{/b}{/i}"
                                    $ laurenanger += 1
                                    $ screen_on = "laurendoormap"
                                    call screen laurendoormap
                        else:
                            scene bg LaurenMadInRoom03
                            with dissolve
                            L "You already gave me a gift. Stop being creepy!"
                            $ laurenanger += 1
                            "{i}{b}\"Lauren's Anger +1\"{/b}{/i}"
                            $ screen_on = "laurendoormap"
                            call screen laurendoormap
                    "I just wanted to apologize":
                        scene bg LaurenMadInRoom03
                        with dissolve
                        L "Well, it's going to take more than just words for me to forgive you for what you did!"
                        RT "{i}I guess I better give her some time, or maybe I can get her a present so she won't be so mad.{/i}"
                        $ screen_on = "laurendoormap"
                        call screen laurendoormap
            "Let's just take a peek at what she's doing." if spycaminlaurenroom == True:
                jump laurenspycamroommad
            "I'm just going to give her some time to cool down":
                $ screen_on = "laurendoormap"
                call screen laurendoormap

label sidneyangryroom:
    if timeofdaycounter == 5:
        scene bg LaurenDoorNight
        with fade
        RT "{i}She locked her door! Sidney must still be pissed off. I guess I better just let her sleep.{/i}"
        $ screen_on = "laurendoornightmap"
        call screen laurendoornightmap
    if sawsidneychanging == True:
        scene bg LaurenDoor
        with fade
        RT "{i}She's pissed off at me already for watching her change, I think I better give her just a little more time before I try to smooth things over with her.{/i}"
        $ screen_on = "laurendoormap"
        call screen laurendoormap
    else:
        scene bg LaurenDoor
        with fade
        RT "{i}Her door's locked. Sidney's pretty pissed off at me.{/i}"
        menu:
            "Knock":
                scene bg SidneyAngry01
                with fade
                S "What do you want pervert?"
                menu:
                    "Give her a gift":
                        if gavesidneygift == False:
                            scene bg SidneyAngry02
                            with dissolve
                            S "You have something for me?"
                            menu:
                                "Give her a chocolate bar" if inventory.inv_amount(chocolate) >= 1:
                                    scene bg SidneyAngry04
                                    with dissolve
                                    S "Thank you I love chocolate!"
                                    "{i}{b}\"Sidney's Anger -2\"{/b}{/i}"
                                    $ sidneyanger -= 2
                                    $ inventory.drop(chocolate)
                                    $ gavesidneygift = True
                                    if sidneyanger >= 1:
                                        scene bg SidneyAngry05
                                        with dissolve
                                        S "But this doesn't mean I'm not mad at you anymore. It's going to take me some more time to forgive you."
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap
                                    else:
                                        scene bg SidneyAngry04
                                        S "Thank you! I can't stay mad at my sweet little brother!"
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap

                                "Give her Hardnlong gift card" if inventory.inv_amount(giftcard) >= 1:
                                    scene bg SidneyAngry04
                                    with dissolve
                                    S "Thank you! I'm going to use it right now!"
                                    "{i}{b}\"Sidney's Anger -5\"{/b}{/i}"
                                    $ sidneyanger -= 5
                                    $ inventory.drop(giftcard)
                                    $ gavesidneygift = True
                                    if sidneyanger >= 1:
                                        scene bg SidneyAngry05
                                        with dissolve
                                        S "But this doesn't mean I'm not mad at you anymore. It's going to take me some more time to forgive you."
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap
                                    else:
                                        scene bg SidneyAngry04
                                        S "Thank you! I can't stay mad at my sweet little brother!"
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap
                                "Give her flowers" if inventory.inv_amount(flowers) >= 1:
                                    $ inventory.drop(flowers)
                                    if sidneyaffection <= 50:
                                        scene bg SidneyAngry03
                                        with dissolve
                                        S "Why the hell do you think I would want flowers from you? You're not my boyfriend!"
                                        "{i}\"Throws them in her trash\"{/i}"
                                        S "Maybe next time try to think of something that doesn't imply you want in my pants!"
                                        "{i}{b}\"Sidney's Affection -1\"{/b}{/i}"
                                        "{i}{b}\"Sidney's Anger +2\"{/b}{/i}"
                                        "{i}\"You need higher affection to gift flowers.\"{/i}"
                                        $ sidneyanger += 2
                                        $ sidneyaffection -= 1
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap
                                    else:
                                        scene bg SidneyAngry04
                                        with dissolve
                                        S "Oh my gosh! They're beautiful!"
                                        S "You're such a charmer!"
                                        S "If I didn't know any better, I would think you were trying to put the moves on me!"
                                        $ sidneyanger = 0
                                        $ sidneyaffection += 1
                                        "{i}{b}\"Sidney's Anger -10\"{/b}{/i}"
                                        "{i}{b}\"Sidney's Affection +1\"{/b}{/i}"
                                        scene bg SidneyAngry06
                                        S "Thank you so much!"
                                        RT "{i}Oh, wow.{/i}"
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap
                                "Never mind":
                                    scene bg SidneyAngry03
                                    with dissolve
                                    S "You jerk! You made me get up for that."
                                    "{i}{b}\"Sidney's Anger +1\"{/b}{/i}"
                                    $ sidneyanger += 1
                                    $ screen_on = "laurendoormap"
                                    call screen laurendoormap
                        else:
                            scene bg SidneyAngry03
                            with dissolve
                            S "You already gave me a gift. Stop being pervy!"
                            $ sidneyanger += 1
                            "{i}{b}\"Sidney's Anger +1\"{/b}{/i}"
                            $ screen_on = "laurendoormap"
                            call screen laurendoormap
                    "I just wanted to apologize":
                        scene bg SidneyAngry03
                        with dissolve
                        S "Well, it's going to take more than just words for me to forgive you for what you did!"
                        RT "{i}I guess I better give her some time, or maybe I can get her a present so she won't be so mad.{/i}"
                        $ screen_on = "laurendoormap"
                        call screen laurendoormap
            "Let's just take a peek at what she's doing." if spycaminlaurenroom == True:
                jump sidneyspycamroom
            "I'm just going to give her some time to cool down":
                $ screen_on = "laurendoormap"
                call screen laurendoormap

label laurendresser:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    if timeofdaycounter == 1:
        jump dresserearlymorning
    if timeofdaycounter == 5:
        jump dressernight
    if progress == 1:
        scene bg LaurenSleepIn
        RT "{i}Why would I go through her stuff?{/i}"
        $ screen_on = "laurenmapsleepin"
        call screen laurenmapsleepin
    else:
        scene bg LaurenRoom01
        RT "{i}Why would I go through her stuff?{/i}"
        jump laurenroom

label dresserearlymorning:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    if progress == 1:
        scene bg LaurenSleepIn
        RT "{i}Why would I go through her stuff?{/i}"
        $ screen_on = "laurenmapsleepin"
        call screen laurenmapsleepin
    if daycounter >=6 and sidneyfingerlaurenprogress >= 4:
        scene bg LaurenSleepIn
        RT "{i}Those are some sexy panties, I'll bet they smell amazing. If only she wasn't lying just right there.{/i}"
        $ screen_on = "laurenmapsleepin"
        call screen laurenmapsleepin
    if progress >= 6:
        while daycounter >= 6:
            scene bg SidneyLaurenSleeping01
            RT "{i}Nothing interesting here.{/i}"
            $ screen_on = "sidneylaurensleepingmap"
            call screen sidneylaurensleepingmap
        if progress >= 6:
            while sidneyfingerlaurenprogress >= 4:
                scene bg LaurenRoom01
                RT "{i}Nice Panties. They smell great!{/i}"
                $ screen_on = "laurenmap"
                call screen laurenmap
            if progress >= 6:
                scene bg SidneySleepIn01
                RT "{i}Nothing interesting here.{/i}"
                $ screen_on = "sidneysleepinmap"
                call screen sidneysleepinmap
    if daycounter >= 6:
        scene bg LaurenSleepIn
        RT "{i}Why would I go through all her stuff?{/i}"
        $ screen_on = "laurenmapsleepin"
        call screen laurenmapsleepin
    else:
        scene bg LaurenRoom01
        RT "{i}Nothing interesting here.{/i}"
        $ screen_on = "laurenmap"
        call screen laurenmap

label dressernight:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    if sidneyfingerlaurenprogress >= 4:
        scene bg NightLauren01
        RT "{i}Some sexy undies! They don't smell as good as the ones in the laundry basket!{/i}"
        $ screen_on = "laurenmapnight"
        call screen laurenmapnight
    if progress >= 6:
        while sidneyfingerlaurenprogress >= 4:
            scene bg NightLauren01
            RT "{i}Nothing interesting here.{/i}"
            $ screen_on = "laurenmapnight"
            call screen laurenmapnight
        if progress >= 6:
            scene bg SidneyLaurenSleep01
            RT "{i}Nothing interesting here.{/i}"
            $ screen_on = "sidneylaurennightmap"
            call screen sidneylaurennightmap
    else:
        scene bg NightLauren01
        RT "{i}Nothing interesting here.{/i}"
        $ screen_on = "laurenmapnight"
        call screen laurenmapnight

label laurenlaundry:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    if timeofdaycounter == 1:
        jump laundryearlymorning
    if timeofdaycounter == 5:
        jump laundrynight
    if progress == 1:
        scene bg LaurenSleepIn
        RT "{i}Dirty laundry, gross!{/i}"
        $ screen_on = "laurenmapsleepin"
        call screen laurenmapsleepin
    elif timeofdaycounter == 5:
        scene bg NightLauren01
        RT "{i}Dirty laundry, gross!{/i}"
        jump laurenroom
    else:
        scene bg LaurenRoom01
        RT "{i}Dirty laundry, gross!{/i}"
        jump laurenroom

label laundryearlymorning:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    if progress == 1:
        scene bg LaurenSleepIn
        RT "{i}Dirty Laundry, gross!{/i}"
        $ screen_on = "laurenmapsleepin"
        call screen laurenmapsleepin
    if daycounter >= 6 and sidneyfingerlaurenprogress >= 4:
        scene bg LaurenSleepIn
        RT "{i}There's some of Lauren's used panties. I'll bet they smell even better than the ones in her drawers. I don't want her to see me sniffing her panties though.{/i}"
        $ screen_on = "laurenmapsleepin"
        call screen laurenmapsleepin
    if progress >= 6:
        while daycounter >= 6:
            scene bg SidneyLaurenSleeping01
            RT "{i}Dirty Laundry, gross!{/i}"
            $ screen_on = "sidneylaurensleepingmap"
            call screen sidneylaurensleepingmap
        if progress >= 6:
            while sidneyfingerlaurenprogress >= 4:
                scene bg LaurenRoom01
                RT "{i}There's some sexy used panties, I guess it couldn't hurt to give them a sniff.... sniffffffff.... oh yeah! Instant boner.{/i}"
                $ screen_on = "laurenmap"
                call screen laurenmap
            scene bg SidneySleepIn01
            RT "{i}Dirty Laundry, gross!{/i}"
            $ screen_on = "sidneysleepinmap"
            call screen sidneysleepinmap
    if daycounter >= 6:
        scene bg LaurenSleepIn
        RT "{i}Dirty Laundry, gross!{/i}"
        $ screen_on = "laurenmapsleepin"
        call screen laurenmapsleepin
    else:
        scene bg LaurenRoom01
        RT "{i}Dirty Laundry, gross!{/i}"
        $ screen_on = "laurenmap"
        call screen laurenmap

label laundrynight:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    if sidneyfingerlaurenprogress >= 4:
        scene bg NightLauren01
        RT "{i}There's some sexy used panties, I guess it couldn't hurt to give them a sniff.... sniffffffff.... oh yeah! Instant boner.{/i}"
        $ screen_on = "laurenmapnight"
        call screen laurenmapnight
    if progress >= 6:
        scene bg SidneyLaurenSleep01
        RT "{i}Dirty Laundry, gross!{/i}"
        $ screen_on = "sidneylaurennightmap"
        call screen  sidneylaurennightmap
    else:
        scene bg NightLauren01
        RT "{i}Dirty Laundry, gross!{/i}"
        $ screen_on = "laurenmapnight"
        call screen laurenmapnight

label laurensneakingnight:
    if no_more_sub and laurennight == False:
        jump lauren_night

    if laurensubmission >= 5 and no_more_sub == False:
        scene bg NightLauren01
        with fade
        RT "{i}I don't think the subliminal messages are having any more effect, I'll have to think of something else to make her more submissive.{/i}"
        RT "{i}I should start thinking of other fun things I can do to her while she's in such a deep sleep.{/i}"
        $ no_more_sub = True
        $ screen_on = "laurenmapnight"
        call screen laurenmapnight

    if fuckfamilyscheme == False:
        scene bg NightLauren01
        with fade
        play music SexMusic
        $ laurenpictureprogress = 4
        RT "{i}I just can't get Mom's amazing bare tits and sculpted ass out of my mind! The way she moved.... her perfect body!.... She has a body that could be in porn!{/i}"
        RT "{i}And just like porn, I'm addicted to seeing Mom naked. I've got to see more of it! I've got those pictures on my computer now, but that's not enough!!{/i}"
        RT "{i}I need to touch her.... taste her.... smell her!{/i}"
        RT "{i}Ohhh man.... I am so messed up right now!.... I know it's so incredibly wrong.... but I've just got to make her mine!{/i}"
        RT "{i}This is all her fault! Since when is she so good at shaking her perfect tits in public? Where did she learn to move like that?.... That's so.... hot!{/i}"
        RT "{i}I've never wanted or lusted for someone so badly! And that person being my own mother?!!!.... Could it even be possible?... {/i}"
        RT "{i}Just look at little Lauren sleeping innocently in bed. So innocent, so naive about how slutty her mom is.{/i}"
        RT "{i}Actually.... she looks a lot like Mom!.... Just a little mini version of her.{/i}"
        RT "{i}I mean her tits are tiny, but I'm sure they've got plenty of growth left in them, but that ass is perfect, just like Mom's.{/i}"
        RT "{i}Hmmmm.... just a mini version of Mom.... probably easier to manipulate though.... yeah.... she'd be perfect to practice on.{/i}"
        RT "{i}If I can make my sister mine, there might be hope for me with Mom! I might even be able to get her to help me conquer her.{/i}"
        RT "{i}For such an impossible quest, I'm going to need allies!{/i}"
        RT "{i}Could I do that to Lauren though?.... I mean every quest and battle has collateral damage.{/i}"
        RT "{i}And I wouldn't force her to do anything against her will.{/i}"
        RT "{i}I'd just help her realize that she wants this as badly as I do.{/i}"
        RT "{i}Should I add her to my \"expedition to conquer Mom party?\"{/i}"
        menu:
            "Yes, I need an ally":
                scene bg LaurenNightPeek1
                with  fade
                RT "{i}I mean look at that ass! I can't believe I've never been tempted by it before! Then again, I was never tempted by Mom's ass either, {p}till I saw her polishing the stripper pole with it.{/i}"
                scene bg LaurenNightPeek2
                with dissolve
                RT "{i}I need a picture of that perfect backside!{/i}"
                RT "{i}I'll certainly enjoy this later!{/i}"
                scene bg LaurenNightPeek1
                with dissolve
                RT "{i}Ok.... now how will I start to win her over?{/i}"
                RT "{i}Hmmmm.... {/i}"
                RT "{i}I've heard subliminal messages while sleeping can be very effective.{/i}"
                RT "{i}Guess I could give that a try.{/i}"
                scene bg LaurenNightPeek3
                with dissolve
                R "{i}(Whispering){/i} You think your brother is sexy.... you think your brother is sexy.... you think your brother is sexy..."
                scene bg BlurryWhite
                with fade
                scene bg SleepBlack
                with fade
                scene bg BlurryWhite
                with fade
                scene bg LaurenNightPeek3
                with fade
                "10 minutes later."
                R "{i}(Whispering){/i} You think your brother is sexy.... you think your brother is sexy.... you think your brother is sexy..."
                "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                $ laurensubmission += 1
                RT "{i}That's all I can do tonight. My legs are tingling like crazy.{/i}"
                RT "{i}I wonder if it had any effect?{/i}"
                RT "{i}I should go back to my room and try to get some sleep.{/i}"
                $ laurenprogress = 2
                $ laurennight = True
                $ fuckfamilyscheme = True
                scene bg NightLauren01
                with fade
                play music Honey
                $ screen_on = "laurenmapnight"
                call screen laurenmapnight
    if laurennight == False:
        scene bg NightLauren01
        with fade
        menu:
            "More subliminal messages!":
                scene bg LaurenNightPeek1 with Dissolve(0.5)
                $ renpy.pause (0.5, hard=True)
                play music SexMusic
                scene bg LaurenNightPeek3
                with dissolve
                R "{i}(Whispering){/i} You think your brother is sexy.... you think your brother is sexy.... you think your brother is sexy..."
                scene bg BlurryWhite
                with fade
                scene bg SleepBlack
                with fade
                scene bg BlurryWhite
                with fade
                scene bg LaurenNightPeek3
                with fade
                "10 minutes later."
                R "{i}(Whispering){/i} You think your brother is sexy.... you think your brother is sexy.... you think your brother is sexy..."
                "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                $ laurensubmission += 1
                RT "{i}That's all I can do tonight. My legs are tingling like crazy.{/i}"
                RT "{i}I wonder if it had any effect?{/i}"
                RT "{i}I should go back to my room and try to get some sleep.{/i}"
                $ laurennight = True
                scene bg NightLauren01
                with fade
                play music Honey
                $ screen_on = "laurenmapnight"
                call screen laurenmapnight
            "Not tonight.":
                scene bg NightLauren01
                with fade
                $ laurennight = True
                $ screen_on = "laurenmapnight"
                call screen laurenmapnight
    else:
        scene bg NightLauren01
        with fade
        $ screen_on = "laurenmapnight"
        call screen laurenmapnight

label laurenroomhang:
    if laurenbedroomprogress == 1:
        scene bg HangingInRoomLauren01
        with fade
        $ laurenbedroomprogress = 2
        L "Hey brother, just give me a sec, I've just got to finish sending this text."
        LT "{i}Ok, heart emoji, heart emoji, smiley face with heart eyes emoji, and.... send.{/i}"
        scene bg HangingInRoomLauren02
        with dissolve
        L "So what's up?"
        R "Oh, nothing, I'm just really bored so I thought I'd come and see what you're up to."
        L "I know right? Now that we have no money, there's nothing to do."
        scene bg HangingInRoomLauren05
        with dissolve
        L "Usually Mom and I are shopping right now."
        L "I guess we won't be going shopping any time soon."
        R "Oh, I don't know, I'm going to figure out how to get us some money."
        R "I don't think it'll be long till you're able to go out shopping again."
        scene bg HangingInRoomLauren03
        with dissolve
        L "Hahaha.... yeah right! You're just a lazy high schooler, who didn't even graduate when you were supposed to."
        R "You know that was Dad's fault!"
        R "And I'll admit I've been a little lazy, but now that Dad's gone I'm really going to step it up."
        scene bg HangingInRoomLauren02
        with dissolve
        L "I'll believe it when I see it."
        R "You really don't think I'm capable of taking care of our family?"
        L "I know you're not!"
        R "Well, when I do, I'm going to take Mom shopping and I'm going to leave you home."
        scene bg HangingInRoomLauren03
        with dissolve
        L "Ok.... ok.... ok.... since I've offended your honor, I'll tell you what I'm going to do to make it up."
        L "If you do prove me wrong, I will owe you a big favor."
        L "I will let you decide what it is, as long as it isn't too expensive, since you know I'm broke. And it can't be too crazy either."
        L "If you try to go too far, I'll just say no, and we'll both have lost out on an opportunity."
        L "So get working hard! I really do hope you prove me wrong!"
        scene bg HangingInRoomLauren01
        with dissolve
        L "Now if you'll excuse me, there's some hardcore drama that I'm missing out on."
        RT "{i}Hmmm.... any favor I want huh?{/i}"
        RT "{i}I'll have to start thinking of something good.{/i}"
        RT "{i}Maybe I could have her clean my room for a week.{/i}"
        RT "{i}Or maybe I could have her try on some sexy clothes for me.{/i}"
        RT "{i}Maybe she would even let me see her tits.{/i}"
        RT "{i}That would probably be the too crazy she was talking about.{/i}"
        RT "{i}But I'm really curious to see what I'll be able to get away with.{/i}"
        scene bg LaurenDoor
        with fade
        $ screen_on = "laurendoormap"
        call screen laurendoormap
    else:
        scene bg HangingInRoomLauren01
        with fade
        L "Is there something you need?"
        R "Do you want to do something?"
        L "Sorry, but my friend Chloe is really upset about a guy, and just really needs all of my attention right now."
        L "I'll come find you if I get done texting her soon."
        scene bg LaurenDoor
        with fade
        $ screen_on = "laurendoormap"
        call screen laurendoormap

label sidneychanging:
    $ persistent.gal_Sidney_1 = True
    if spycaminlaurenroom and picturesofsidney:
        jump sidneyspycamroom
    if picturesofsidney == True:
        scene bg LaurenDoor
        with fade
        RT "{i}Well shit, she's locking the door to change now.{/i}"
        RT "{i}She definitely doesn't want me spying on her changing again.{/i}"
        RT "{i}I've got to get a spy cam in there or something.{/i}"
        $ screen_on = "laurendoormap"
        call screen laurendoormap
    else:
        scene bg LaurenDoor
        with fade
        menu:
            "Spy on Sidney":
                $ sidneypictureprogress = 3
                scene bg PeekSidneyDressing01
                with fade
                play music SexMusic
                $ sawsidneychanging = True
                RT "{i}Oh no! Hello temptation my old friend.{/i}"
                RT "{i}I really shouldn't watch this.... but I can't look away!{/i}"
                scene bg PeekSidneyDressing02
                with dissolve
                RT "{i}Shit! Why couldn't the women in my family be ugly?{/i}"
                RT "{i}Then I wouldn't have this moral dilemma.{/i}"
                scene bg PeekSidneyDressing03
                with dissolve
                RT "{i}Oh My Gosh! I'm going to explode in my pants!{/i}"
                RT "{i}I have to capture this moment!{/i}"
                scene bg PeekSidneyDressing04
                with dissolve
                RT "{i}There, now I have some more fapping material for later.{/i}"
                $ picturesofsidney = True
                scene bg PeekSidneyDressing05
                with dissolve
                $ renpy.pause ()
                scene bg PeekSidneyDressing06
                with dissolve
                $ renpy.pause ()
                scene bg PeekSidneyDressing07
                with dissolve
                RT "{i}Well, I guess all good things must come to an end.{/i}"
                scene bg PeekSidneyDressing08
                with fade
                ST "{i}I love this outfit, it looks so cute on me!{/i}"
                scene bg PeekSidneyDressing09
                with fade
                ST "{i}Oh my God, is that?.... {/i}"
                scene bg PeekSidneyDressing10
                with fade
                RT "{i}Oh no, her face in the mirror looks like she might've seen me.{/i}"
                RT "{i}I've got to get out of here!{/i}"
                scene bg PeekSidneyDressing11
                with fade
                ST "{i}Oh wait, there's nothing there.... {/i}"
                scene bg PeekSidneyDressing12
                with fade
                ST "{i}Did I just imagine it?{/i}"
                ST "{i}Who could it have been? Isn't everyone at school?{/i}"
                ST "{i}Could a stranger have been watching me change?{/i}"
                ST "{i}More likely it's just [ryan] skipping class.{/i}"
                ST "{i}I sure hope it was [ryan].{/i}"
                ST "{i}Wait.... that sounded weird in my head.{/i}"
                ST "{i}I shouldn't be hoping that my brother is watching me change.{/i}"
                ST "{i}Why does that thought turn me on just a little?{/i}"
                "{i}{b}\"Sidney's Libido +1\"{/b}{/i}"
                $ sidneylibido += 1
                play music Honey
                scene bg RyansRoom01
                with fade
                RT "{i}Holy shit, that was close, but I don't think she saw me.{/i}"
                scene bg RyansRoom01
                with fade
                $ screen_on = "ryanmap"
                call screen ryanmap
            "Keep looking around":
                scene bg LaurenDoor
                $ screen_on = "laurendoormap"
                call screen laurendoormap

label caughtbysidney:
    $ caught_by_sidney = True
    $ persistent.gal_Sidney_1 = True
    scene bg LaurenDoor
    with fade
    RT "{i}Sidney locked the door. Oh crap she must have seen something! I wonder if she knows it was me?{/i}"
    RT "{i}I think I can hear her talking with someone on her phone. Could she be telling Mom on me?{/i}"
    RT "{i}I need to get closer to see if I can hear.{/i}"
    RT "{i}Maybe if I put my ear on the door I can.... {/i}"
    scene bg CaughtBySidney01
    with dissolve
    S "Haa.... I knew it was you!"
    S "Why are you lurking at my door you little pervert!"
    scene bg CaughtBySidney02
    with dissolve
    R "I'm sorry, I just wasn't sure if you were home, and wanted to see if you were. I thought maybe we could hang out?"
    S "Oh, and I'm supposed to believe that you weren't peeking in at me dressing just a few minutes ago?"
    S "How much did you see?"
    menu:
        "Just a little bit":
            R "Not much, you were mostly dressed when I saw you. I ran away as soon as I realized you were changing."
            S "You better not be lying!"
            "{i}{b}\"Sidney's Anger +5\"{/b}{/i}"
            $ sidneyanger += 5
            S "You know you could have just knocked."
            R "Sorry, I'll try to do that next time."
            S "Whatever!"
            scene bg LaurenDoor
            with fade
            $ screen_on = "laurendoormap"
            call screen laurendoormap
        "Nothing":
            R "I have no idea what you're talking about."
            S "Yeah right you little liar!"
            "{i}{b}\"Sidney's Anger +10\"{/b}{/i}"
            $ sidneyanger += 10
            S "If you need to talk to me, just knock on the door,"
            S "Instead of creeping around like some depraved pervert."
            R "Sorry, I'll try to do that next time."
            S "Whatever!"
            scene bg LaurenDoor
            with fade
            $ screen_on = "laurendoormap"
            call screen laurendoormap

label sidneylaurensneakattempt:
    if failedsneakattempt == False:
        scene bg SidneyLaurenSleep01
        with fade
        $ sidneypictureprogress = 4
        $ laurenpictureprogress = 5
        RT "{i}Ok.... so having Sidney in bed with Lauren might complicate things just a little bit.{/i}"
        RT "{i}I guess I could try and see if Sidney will sleep through the subliminal messages.{/i}"
        RT "{i}I could even try some on her after I'm done with Lauren.{/i}"
        RT "{i}Hmmm.... should I risk it?{/i}"
        menu:
            "Of course!":
                scene bg SidneyLaurenSneak01
                with dissolve
                play music SexMusic
                $ failedsneakattempt = True
                RT "{i}Two hotties in one bed!{/i}"
                RT "{i}I'm sure glad Mom keeps the house so warm. It would be a shame to put a blanket over these bodies!{/i}"
                scene bg SidneyLaurenSneak02
                with dissolve
                R "{i}(Whispering){/i} You think your brother is sexy.... you think your brother is sexy..."
                R "{i}(Whispering){/i} You think your brother is .... oh, shit!"
                scene bg SidneyLaurenSneak03
                with fade
                S "Hmmmmm?.... Lauren?.... Did you say something?"
                scene bg SidneyLaurenSneak04
                with fade
                S "Lauren.... are you asleep?"
                S "Ok?.... I guess it was my imagination?..."
                RT "{i}Shit!! Sidney is a super light sleeper!{/i}"
                RT "{i}I've got to think of some other way to keep her progress going.{/i}"
                RT "{i}I guess I'll just wait here until I'm sure Sidney has fallen back asleep.{/i}"
                scene bg LaurenDoorNight
                with fade
                RT "{i}Shit, that was close!{/i}"
                RT "{i}How am I going to win over Lauren now? I'll need to look around for inspiration.{/i}"
                play music Honey
                $ screen_on = "laurendoornightmap"
                call screen laurendoornightmap
    else:
        scene bg SidneyLaurenSleep01
        with fade
        RT "{i}They look so vulnerable while they are asleep, but if I tried anything and they woke up.... {/i}"
        RT "{i}I'd be kicked out of the house, maybe disowned. I've got to play this smart.{/i}"
        $ screen_on = "sidneylaurennightmap"
        call screen sidneylaurennightmap

label sidneylaurensneakingnight:
    if laurenfingered and progress >= 7:
        scene bg SidneyLaurenSleep01
        with fade
        RT "{i}I better not push it any further tonight.{/i}"
        $ screen_on = "laurenmapnight"
        call screen laurenmapnight
    if laurenfingered == True:
        scene bg SidneyLaurenSleep01
        with fade
        RT "{i}I better not push it any further tonight.{/i}"
        $ screen_on = "sidneylaurennightmap"
        call screen sidneylaurennightmap
    if sidneyfingerlaurenprogress == 3:
        scene bg SidneyLaurenSleep01
        with fade
        RT "{i}They should be sleeping pretty soundly. They both have a habit of drinking tea before bed.{/i}"
        RT "{i}The melatonin worked pretty well last time. Should I check it out again?{/i}"
        $ sidneyfingerlaurenprogress = 4
        $ laurenfingered = True
        menu:
            "Continue sneaking":
                $ laurenpictureprogress = 9
                $ sidneypictureprogress = 8
                scene bg SidneyLaurenSneak01
                with dissolve
                play music SexMusic
                RT "{i}If they are sleeping as soundly as last time, I might be able to get away with a little more.{/i}"
                scene bg SidneyLaurenSneak05
                with fade
                RT "{i}Ok, here goes nothing.{/i}"
                scene bg SidneyLaurenSneak06
                with dissolve
                $ renpy.pause (2, hard=True)
                scene bg SidneyLaurenSneak08
                with dissolve
                $ renpy.pause (2, hard=True)
                scene bg SidneyLaurenSneak10
                with dissolve
                RT "{i}Wow! I can't believe that didn't wake her up.{/i}"
                RT "{i}So now it's time for me to wake her up.{/i}"
                scene bg SidneyLaurenSneak19
                with dissolve
                RT "{i}If this doesn't get her kicked out of Lauren's room, I don't know what will.{/i}"
                RT "{i}Just a pinch and let's see what happens.{/i}"
                scene bg SidneyLaurenSneak15
                with dissolve
                LT "{i}Yaawnn.... hmmm.... I think I really need to poop.... I should get up and.... {/i}"
                LT "{i}Wait.... my panties are pulled down again.... {/i}"
                scene bg SidneyLaurenSneak17
                with dissolve
                L "OH MY FUCKING GOSH!!!!"
                L "SIDNEY!!!"
                scene bg SidneyLaurenSneak20
                with dissolve
                L "WAKE UP, WAKE UP, WAKE UP!!!!"
                S "Lauren what the hell? Why are you freaking out?"
                S "Oh, no! Let me guess! You think I did it again?"
                L "Yes, you did it again!"
                L "Only this time, you were fingering my asshole!"
                S "WHAAAT?"
                scene bg SidneyLaurenSneak22
                with dissolve
                M "Again?! You two little shits have got to be kidding me!.... I'm sorry, please excuse my language, but I'm so tired from getting woken up every night!"
                L "Mom! You have to do something this time!"
                scene bg SidneyLaurenSneak23
                with dissolve
                L "This time her finger was up my asshole!"
                M "Oh geez! Lauren, your dreams are getting weirder and weirder!"
                scene bg SidneyLaurenSneak21
                with fade
                L "But Mom, I wasn't dreaming! My panties were pulled down, and by the time I realized what was happening, I was wide awake!"
                M "Sidney, smell your fingers, maybe you couldn't smell Lauren's pussy, but I'm sure you would be able to smell her butt."
                S "Mom! Really?"
                M "NOW!"
                scene bg SidneyLaurenSneak25
                with dissolve
                ST "{i}Oh no! What if?.... {/i}"
                ST "{i}Shit!.... {/i}"
                ST "{i}I put my finger up Lauren's ass?{/i}"
                ST "{i}I really did have my finger up her ass.... {/i}"
                ST "{i}Why would I do that?.... {/i}"
                "{i}{b}\"Sidney's Libido +1\"{/b}{/i}"
                $ sidneylibido += 1
                M "Well?"
                S "Well.... ummmm..."
                M "Here, let me smell."
                scene bg SidneyLaurenSneak26
                with dissolve
                S "Hey!"
                MT "{i}I think there is a faint smell of ass.{/i}"
                MT "{i}Sidney really has been doing weird things to her sister in her sleep.{/i}"
                MT "{i}At least I hope she's been asleep while she was putting her fingers in her sister's holes!{/i}"
                MT "{i}That sounds so naughty in my head!{/i}"
                "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                $ momlibido += 1
                L "Well?!"
                scene bg SidneyLaurenSneak25
                with dissolve
                M "Well, I think I do smell a slight smell on Sidney's finger."
                M "It's not enough to be positive, but I think it's enough to take action to avoid any further possible incidents."
                M "Sidney, you're going to have to start sleeping somewhere else."
                scene bg SidneyLaurenSneak24
                with dissolve
                S "But I just moved all my stuff in here! I just got everything unpacked!"
                M "No.... you will still keep all your stuff in here, and change your clothes in here, and all that, but at night you will just sleep elsewhere."
                S "Where?"
                M "Well, you can try my room. But I'll only give you one chance and then you'll have to sleep somewhere else!"
                S "You mean like with [ryan]?!"
                RT "{i}Please say yes! Please say yes! Please say yes!{/i}"
                M "Oh God, no!"
                RT "{i}Dammit!{/i}"
                M "If you can't keep your hands to yourself in your sleep, I don't want you corrupting my little boy!"
                RT "{i}Big boy!{p}.... man.... I mean man!{/i}"
                M "You'll just have to sleep on the couch."
                S "Well, why don't I just skip a step and I'll just start sleeping there now."
                M "That's a great idea. Go sleep on the couch!"
                S "Fine!"
                M "Good night, girls!"
                $ progress = 7
                scene bg MyRoomNight
                with fade
                RT "{i}I finally did it! All the girls have been separated. That should make my nighttime efforts easier.{/i}"
                play music Honey
                $ persistent.gal_Lauren_Sidney_1 = True
                $ screen_on = "ryanmapnight"
                call screen ryanmapnight
            "Leave":
                scene bg LaurenDoorNight
                with fade
                $ screen_on = "laurendoornightmap"
                call screen laurendoornightmap
    elif sidneyfingerlaurenprogress == 2:
        scene bg SidneyLaurenSleep01
        with fade
        RT "{i}They should be sleeping pretty soundly. They both have a habit of drinking tea before bed.{/i}"
        RT "{i}The melatonin worked pretty well last time. Should I check it out again?{/i}"
        menu:
            "Continue sneaking":
                scene bg SidneyLaurenSneak01
                with dissolve
                play music SexMusic
                $ sidneyfingerlaurenprogress = 3
                $ laurenfingered = True
                RT "{i}If they are sleeping as soundly as last time, I might be able to get away with a little more.{/i}"
                scene bg SidneyLaurenSneak05
                with fade
                RT "{i}Ok, here goes nothing.{/i}"
                scene bg SidneyLaurenSneak06
                with dissolve
                $ renpy.pause (2, hard=True)
                scene bg SidneyLaurenSneak08
                with dissolve
                $ renpy.pause (2, hard=True)
                scene bg SidneyLaurenSneak09
                with dissolve
                RT "{i}There, Lauren will never let Sidney sleep with her after this.{/i}"
                RT "{i}Is this crossing a line though?.... {/i}"
                RT "{i}Stop it, [ryan]!.... Stop second guessing yourself.{/i}"
                RT "{i}Time to wake her up.{/i}"
                scene bg SidneyLaurenSneak18
                with dissolve
                RT "{i}Ok, another light pinch to bring her out of her melatonin enhanced sleep.{/i}"
                scene bg SidneyLaurenSneak14
                with dissolve
                L "Hmmm.... yaawn.... what was that?..."
                scene bg SidneyLaurenSneak16
                with dissolve
                L "Ohh My.... are her fingers in.... my.... pussy?..."
                scene bg SidneyLaurenSneak20
                with dissolve
                L "SIDNEY DAMN YOU! Wake up!..."
                S "Huhh?.... Why are you.... waking me up again?"
                L "WHY? So you can kindly get your fingers out of my pussy!"
                S "WHAT? Have you lost your mind?"
                L "No, I haven't lost my mind! And I wasn't dreaming either!"
                scene bg SidneyLaurenSneak22
                with fade
                M "Are you two at it again!?"
                M "What does it take to get a full nights sleep around here?"
                scene bg SidneyLaurenSneak23
                with dissolve
                L "Mom she molested me in my sleep again!"
                S "I did not, she must have been dreaming again!"
                scene bg SidneyLaurenSneak21
                with dissolve
                M "Lauren, if you're waking me up over some weird sexual dream of yours, I'm not going to be very happy with you!"
                L "But Mom, it's not a dream!"
                M "How do you know? You were both asleep!"
                L "Sidney, smell your fingers, I'll bet they smell like my pussy."
                S "Smell my fingers?"
                S "This is so weird."
                M "Do it Sidney! Smell your fingers."
                scene bg SidneyLaurenSneak25
                with dissolve
                ST "{i}Oh my God! My fingers do smell like pussy!{/i}"
                ST "{i}Hmmm.... it must be Lauren's smell after all, it smells different than mine, I guess sweeter, or younger or something.... {/i}"
                ST "{i}Why do I like that smell?{/i}"
                "{i}{b}\"Sidney's Libido +1\"{/b}{/i}"
                $ sidneylibido += 1
                ST "{i}Shit! I can't admit to this!{/i}"
                M "Well, what's the verdict?"
                S "No, they don't smell like anything."
                scene bg SidneyLaurenSneak24
                with dissolve
                M "There Lauren, you see? Just some weird perverted dream."
                M "Ok, now you girls need to go back to bed and stop being so loud!"
                M "I can't even imagine what your brother would think if he could hear this conversation about you playing with each others pussies!"
                L "Mom!"
                RT "{i}Oh my gosh! I can't believe Mom just said that.{/i}"
                scene bg SidneyLaurenSleep01
                with fade
                RT "{i}I can't believe this didn't work again.{/i}"
                RT "{i}I'll be back again. Hopefully the third times the charm.{/i}"
                play music Honey
                $ screen_on = "sidneylaurennightmap"
                call screen sidneylaurennightmap
            "Leave":
                scene bg LaurenDoorNight
                with fade
                $ screen_on = "laurendoornightmap"
                call screen laurendoornightmap
    elif sidneyfingerlaurenprogress == 1:
        scene bg SidneyLaurenSleep01
        with fade
        RT "{i}They should be sleeping pretty soundly. They both have a habit of drinking tea before bed.{/i}"
        RT "{i}Should I see if the melatonin works as advertised?{/i}"
        menu:
            "Continue sneaking":
                $ laurenpictureprogress = 8
                $ sidneypictureprogress = 7
                scene bg SidneyLaurenSneak01
                with dissolve
                play music SexMusic
                $ sidneyfingerlaurenprogress = 2
                $ laurenfingered = True
                RT "{i}So far so good.... If they really are in a deep sleep, I should be able to get away with more than just whispering in their ears.{/i}"
                RT "{i}It's always going to be hard for me to get away with much if they are in the same bed.{/i}"
                RT "{i}I've got to come up with a way to get them sleeping in separate rooms.{/i}"
                RT "{i}And I think I've got the perfect idea.{/i}"
                scene bg SidneyLaurenSneak05
                with fade
                RT "{i}Lauren won't let Sidney sleep with her if she's a little too handsy in her sleep.{/i}"
                scene bg SidneyLaurenSneak06
                with dissolve
                $ renpy.pause (2, hard=True)
                scene bg SidneyLaurenSneak07
                with dissolve
                RT "{i}Is this going too far? I know this is an asshole move, but am I willing to get my hands, or I guess Sidney's hands this dirty?{/i}"
                RT "{i}Yes... of course... The end justifies the means! {p}My family needs a real man, and not some criminal like my father. I've just got to get them to realize it.{/i}"
                RT "{i}Ok.... hand is in place. Now I need Lauren to catch her in the act.{/i}"
                RT "{i}Problem is, Lauren is sound asleep.... I have to wake her up without being seen.{/i}"
                scene bg SidneyLaurenSneak11
                with fade
                RT "{i}Hopefully a pinch will do the trick.{/i}"
                scene bg SidneyLaurenSneak12
                with fade
                L "Hmmm.... ouch.... what was that?..."
                scene bg SidneyLaurenSneak13
                with dissolve
                LT "{i}Is someone's hand carressing my ass?!!{/i}"
                scene bg SidneyLaurenSneak20
                with fade
                L "Sidney, what the hell?!!!"
                S ".... Huh.... what?..."
                L "Huh.... what?.... Why the hell was your hand exploring beneath my panties?!"
                S "What are you talking about?"
                S "I've just been sleeping this whole time. Why did you wake me up?"
                L "Just sleeping huh? Well you're a pretty handsy sleeper!"
                scene bg SidneyLaurenSneak22
                with fade
                M "What the hell is going on in here?"
                M "You're making enough noise to wake the dead!"
                scene bg SidneyLaurenSneak23
                with dissolve
                L "Oh, nothing much! Sidney is just molesting me while I sleep!"
                S "I was not!"
                scene bg SidneyLaurenSneak21
                with dissolve
                M "Lauren, I think you must have been dreaming."
                M "And if you weren't I'm sure Sidney was just doing it in her sleep."
                M "Once people start having sex, it's pretty normal for them to be a little handsy while they sleep."
                M "Your father is a really handsy sleeper."
                S "Eww Mom, TMI! And I haven't started having sex yet!"
                M "Please! I'm not stupid. You're in college."
                S "Well, I'm not a virgin, but I don't just sleep around with all the guys at school!"
                scene bg SidneyLaurenSneak24
                with dissolve
                RT "{i}Uhh.... I hope they wrap this up soon, this is getting uncomfortable.{/i}"
                S "My first time wasn't a good experience, and I haven't really wanted to do much since then."
                M "Well, I'm sorry to hear that, then maybe you're being handsy in your sleep because of built up sexual frustration."
                S "I'm not being handsy in my sleep!"
                M "Alright! Well, it's time for you two to shut up and go to sleep! I don't want your brother to wake up and hear about all of this!"
                M "Ok?"
                L "Alright."
                S "Ok, goodnight."
                scene bg SidneyLaurenSneak20
                with fade
                L "Try to keep your hands to yourself for the rest of the night."
                S "Yeah, fuck you too. Goodnight."
                scene bg SidneyLaurenSleep01
                with fade
                RT "{i}Oh, thank God, they are finally asleep again!{/i}"
                RT "{i}That didn't go exactly as I hoped, but it was still very interesting.{/i}"
                RT "{i}I think I'll have to give it another try.{/i}"
                play music Honey
                $ screen_on = "sidneylaurennightmap"
                call screen sidneylaurennightmap
            "Leave":
                scene bg LaurenDoorNight
                with fade
                $ screen_on = "laurendoornightmap"
                call screen laurendoornightmap
    else:
        scene bg SidneyLaurenSleep01
        with fade
        $ screen_on = "sidneylaurennightmap"
        call screen sidneylaurennightmap

#####  SCHOOL  ########################  SCHOOL  ######################  SCHOOL  ########################  SCHOOL  ##########################################################################################

#####  SCHOOL HALL  ###################  SCHOOL HALL  #################  SCHOOL HALL  ###################  SCHOOL HALL  #####################################################################################

label school:
    if timeofdaycounter == 1:
        jump schoolearlymorning
    elif timeofdaycounter == 2 and start_of_campaign:
        jump newschoolhallwaymorning
    elif timeofdaycounter == 2:
        jump schoolhallwaymorning
    elif timeofdaycounter == 3 and start_of_campaign:
        jump newschoolhallwayafternoon
    elif timeofdaycounter == 3:
        jump schoolhallwayafternoon
    elif timeofdaycounter == 4:
        jump schoolevening
    else:
        jump schoolnight

label schoolearlymorning:
    if daycounter >= 6:
        jump schoolearlymorningweekend
    if diaz_van_counter == 1 and not locker_cam_placed:
        jump locker_room_run
    else:
        scene bg CityMap01
        "It's too early to go to school."
        $ screen_on = "citymapmap"
        call screen citymapmap

label schoolearlymorningweekend:
    scene bg CityMap01
    "There's no school on the weekend."
    $ screen_on = "citymapmap"
    call screen citymapmap

label schoolhallwaymorning:
    if not first_htbyd_shoot and not ntrcontent and not firstloyaltyblowjob and daycounter <= 5:
        jump meganloyaltyblowjob
    if daycounter >= 6:
        jump schoolmorningweekend
    else:
        scene bg SchoolHallway01
        with fade
        RT "{i}I'm going to be late for class if I don't hurry.{/i}"
        $ screen_on = "schoolhallmap"
        call screen schoolhallmap

label schoolmorningweekend:
    scene bg CityMap01
    "There's no school on the weekend."
    $ screen_on = "citymapmap"
    call screen citymapmap

label schoolhallwayafternoon:
    if daycounter >= 6:
        jump schoolafternoonweekend
    else:
        scene bg SchoolHallway01
        with fade
        RT "{i}Should I sit through another class, or find something else to do?{/i}"
        $ screen_on = "schoolhallmap"
        call screen schoolhallmap

label schoolafternoonweekend:
    scene bg CityMap01
    "There's no school on the weekend."
    $ screen_on = "citymapmap"
    call screen citymapmap

label schoolevening:
    if daycounter >= 6:
        jump schooleveningweekend
    else:
        scene bg CityMap01
        "School's over for the day."
        $ screen_on = "citymapmap"
        call screen citymapmap

label schooleveningweekend:
    scene bg CityMap01
    "No school on the weekend."
    $ screen_on = "citymapmap"
    call screen citymapmap

label schoolnight:
    if daycounter >= 6:
        jump schoolnightweekend
    else:
        scene bg CityMapNight
        "It's too late to go to school."
        $ screen_on = "citymapmapnight"
        call screen citymapmapnight

label schoolnightweekend:
    scene bg CityMapNight
    "No school on the weekend."
    $ screen_on = "citymapmapnight"
    call screen citymapmapnight

label mylocker:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    RT "{i}I don't need anything out of there right now.{/i}"
    jump school

#######  CLASSROOM  ######################  CLASSROOM  ############################  CLASSROOM  #############################  CLASSROOM  #####################################################################

label classroom:
    if timeofdaycounter == 2:
        jump classroommorning
    else:
        jump classroomafternoon

label classroommorning:
    if schoolprogress == 1:
        jump firstdayofschool
    if ntrcontent == True:
        scene bg NewClassroom01
        with fade
        menu:
            "Attend Class":
                scene bg Classroom03
                with dissolve
                M "Okay class, let's pick up where we left off last time with our discussion on the Oedipus tragedy, and its influence today."
                jump classlecture
            "Keep looking around":
                $ screen_on = "ntrclassmap"
                call screen ntrclassmap
            "Start Election Campaign Storyline" if tv_events >= 1 and daycounter == 1:
                "{b}{i}\"WARNING\"{/i}{/b}"
                "{i}\"It is highly recommended that you don't start this part of the storyline until you have a decent income.\"{/i}"
                "{i}\"If your only source of income is your daily delivery job, you might want to wait until you've built up a new source of income.\"{/i}"
                "{i}\"This storyline requires you to spend a lot of money to be successful. The results of failure are not pretty (NTR Warning)!\"{/i}"
                "{i}\"There, now you can't say I didn't warn you.\"{/i}"
                "{i}\"Are you sure you'd like to start the \"Election Campaign Storyline?\"{/i}"
                menu:
                    "Yes":
                        jump election_announcement
                    "No":
                        jump classroommorning
    else:
        scene bg Classroom01
        with fade
        menu:
            "Attend Class":
                scene bg Classroom03
                with dissolve
                M "Okay class, let's pick up where we left off last time with our discussion on the Oedipus tragedy, and its influence today."
                jump classlecture
            "Keep looking around":
                $ screen_on = "classmap"
                call screen classmap
            "Start Election Campaign Storyline" if tv_events >= 1 and daycounter == 1:
                "{b}{i}\"WARNING\"{/i}{/b}"
                "{i}\"It is highly recommended that you don't start this part of the storyline until you have a decent income.\"{/i}"
                "{i}\"If your only source of income is your daily delivery job, you might want to wait until you've built up a new source of income.\"{/i}"
                "{i}\"This storyline requires you to spend a lot of money to be successful. The results of failure are not pretty (NTR Warning)!\"{/i}"
                "{i}\"There, now you can't say I didn't warn you.\"{/i}"
                "{i}\"Are you sure you'd like to start the \"Election Campaign Storyline?\"{/i}"
                menu:
                    "Yes":
                        jump election_announcement
                    "No":
                        jump classroommorning

label classroomafternoon:
    if schoolprogress == 1:
        jump firstdayofschool
    if ntrcontent == True:
        scene bg NewClassroom01
        with fade
        menu:
            "Attend Class":
                scene bg Classroom03
                with dissolve
                M "Okay class, let's pick up where we left off last time with our discussion on the Oedipus tragedy, and its influence today."
                jump classlecture
            "Talk to Mom about Oedipus assignment" if lectureprogress >= 2 and mm_fuckedtoday == False:
                jump invitemomtooffice
            "Keep looking around":
                $ screen_on = "ntrclassmap"
                call screen ntrclassmap
    else:
        scene bg Classroom01
        with fade
        menu:
            "Attend Class":
                scene bg Classroom03
                with dissolve
                M "Okay class, let's pick up where we left off last time with our discussion on the Oedipus tragedy, and its influence today."
                jump classlecture
            "Talk to Mom about Oedipus assignment" if lectureprogress >= 2 and mm_fuckedtoday == False:
                jump invitemomtooffice
            "Keep looking around":
                $ screen_on = "classmap"
                call screen classmap

label firstdayofschool:
    $ persistent.gal_mom_2 = True
    scene bg Classroom01
    with fade
    RT "{i}Looks like just any other day at school.{/i}"
    RT "{i}Mom and Lauren seem to be acting normal.{/i}"
    RT "{i}Hopefully we can keep the fact that our dad was thrown in prison a secret.{/i}"
    RT "{i}If these snobby private school kids find out, we'll be treated like garbage.{/i}"
    scene bg Classroom05
    with fade
    RT "{i}Lauren is talking to her friend Kenzie. I'm actually pretty shocked that they are talking face to face, and not by texting while sitting at their desks.{/i}"
    RT "{i}Kenzie is pretty hot. I've tried to get her to notice me, but I get tongue tied around her, and she treats me like a loser.{/i}"
    scene bg Classroom07
    with fade
    RT "{i}I wonder what Zack and Matt are talking about.{/i}"
    RT "{i}Zack's probably trying to get dating tips from Matt.{/i}"
    RT "{i}I know I should. Matt's freaking smooth. He's probably nailed half the girls in our school,{/i}"
    RT "{i}And then there's the rumors that he fucked Mrs. Stone the art teacher and Mrs. Perry the girls PE teacher.{/i}"
    RT "{i}As if being charming and confident weren't enough, being captain of the freaking basketball team can't hurt either.{/i}"
    RT "{i}And on top of that there's also the rumor that he's hung like a horse.{/i}"
    RT "{i}I can tell by the way he stares at Mom, he's more than a little interested.{/i}"
    scene bg Classroom06
    with fade
    RT "{i}Looks like Mom's having to explain something else to Megan.{/i}"
    RT "{i}She may not be the sharpest tool in the shed, but she might just be the prettiest.{/i}"
    RT "{i}I wonder if she's still dating Matt. Not that they have ever been exclusive or anything.{/i}"
    RT "{i}I think she's fucked a teacher or two to get her grades up. I know she got an A in chemistry, and I know it wasn't for her academic performance.{/i}"
    RT "{i}She was my lab partner and I only got a B-.{/i}"
    RT "{i}Unfortunately for Megan, she can't fuck her way to an A in this class. I'll bet she wishes the teacher was a guy.{/i}"
    RT "{i}I wonder if she would even try on Mom. I don't know if Megan swings that way or not.{/i}"
    RT "{i}Hmmm.... that's fun to imagine.{/i}"
    M "Ok class, everyone take your seats!"
    $ schoolprogress = 2
    scene bg Classroom02
    with fade
    M "For our next section in our literature class, we will be studying the Greek tragedy Oedipus Rex. We will also study further writings and studies that have used this play as a reference work."
    M "Our story starts out in Thebes, at the royal palace where Oedipus is greeted by a procession of priests..."
    M ".... Plague{p}.... creon{p}.... apollo{p}.... thebes..."
    scene bg Classroom1stPerson02
    with fade
    RT "{i}Oh my gosh this is so boring! Greek plays are the worst, how am I supposed to pay attention to this. I've never heard of Oedipus before, why should I care about him now?{/i}"
    RT "{i}Oh, yeah! I just remembered that Mom is wearing the same outfit that she wore on the stage at the strip club!{/i}"
    RT "{i}Those are some good memories.... {/i}"
    play music ClubMusic fadein 2.0
    scene bg StripPeek001
    with fade
    scene bg StripperPole01
    with dissolve
    scene bg StripperPole02
    with dissolve
    scene bg StripperPole03
    with dissolve
    scene bg StripperPole04
    with dissolve
    scene bg StripperPole05
    with dissolve
    scene bg StripperPole06
    with dissolve
    scene bg StripperPole07
    with dissolve
    scene bg StripCaught
    with dissolve
    scene bg Classroom1stPerson01
    with fade
    $ renpy.pause (2, hard=True)
    scene bg SleepBlack
    with fade
    scene bg BlurryWhite
    with fade
    scene bg ClassroomStrip01
    with fade
    RT "{i}Why does Mom have to be so hot?{/i}"
    RT "{i}Why did I have to see her humping that pole?{/i}"
    scene bg ClassroomStrip02
    with dissolve
    RT "{i}I'll never be able to look at her the same again.{/i}"
    RT "{i}I just wish I could knock off my dad and take his place in her bed.{/i}"
    RT "{i}Wooow, that's pretty fucked up, I'll bet there's not even a name for this sick psychotic condition I have.{/i}"
    M "And so Oedipus orders that the murderer of Laius be driven out..."
    scene bg ClassroomStrip03
    with dissolve
    RT "{i}I wish I could just taste that beautiful ass!{/i}"
    scene bg ClassroomStrip04
    with dissolve
    M "Lauren? What was Laius' relationship to Oedipus?"
    L "He was his father, but Oedipus didn't know it."
    M "Correct! Now you get a prize for such a good answer."
    M "Just come and take it."
    play sound Mom02 loop
    scene bg ClassroomStrip05 with Dissolve(0.3)
    $ renpy.pause (0.1, hard=True)
    scene bg ClassroomStrip06 with Dissolve(0.3)
    $ renpy.pause (0.1, hard=True)
    scene bg ClassroomStrip05 with Dissolve(0.3)
    $ renpy.pause (0.1, hard=True)
    scene bg ClassroomStrip06 with Dissolve(0.3)
    $ renpy.pause (0.1, hard=True)
    scene bg ClassroomStrip05 with Dissolve(0.3)
    $ renpy.pause (0.1, hard=True)
    M "[ryan]?"
    scene bg ClassroomStrip06 with Dissolve(0.3)
    $ renpy.pause (0.1, hard=True)
    scene bg ClassroomStrip05 with Dissolve(0.3)
    $ renpy.pause (0.1, hard=True)
    scene bg ClassroomStrip06 with Dissolve(0.3)
    $ renpy.pause (0.1, hard=True)
    M "[ryan]?"
    scene bg ClassroomStrip05 with Dissolve(0.3)
    $ renpy.pause (0.1, hard=True)
    scene bg ClassroomStrip06 with Dissolve(0.3)
    $ renpy.pause (0.1, hard=True)
    scene bg ClassroomStrip05 with Dissolve(0.3)
    $ renpy.pause (0.1, hard=True)
    scene bg ClassroomStrip06 with Dissolve(0.3)
    $ renpy.pause (0.1, hard=True)
    stop sound
    M "[upper_ryan]!"
    scene bg BlurryWhite
    with fade
    play music Honey
    scene bg Classroom04
    with fade
    R "Huh?..."
    M "[ryan] you were falling asleep. I need you to pay attention. You will be graded on your participation."
    R "Yeah, I know.... I'll try..."
    scene bg Classroom03
    with dissolve
    $ timeofdaycounter += 1
    M "And so hearing all of this, Oedipus decides to solve the mystery of Laius' murder..."
    X "Pssst.... {p}Pssst.... {p}PSSSSSTTTTT!!!!!!!!"
    scene bg Classroom1stPerson03
    with fade
    MB "{i}(whispering){/i} Your mom has one fine ass! Don't you think?"
    R "{i}(whispering desperately){/i}.... what, are you crazy! She's my mom! I would never think of her like that!"
    MB "{i}(whispering){/i} yeah right, and that's just a circus tent under your pants."
    MB "{i}(whispering){/i} I know the hunger that's in your expression as you stare at her."
    scene bg Classroom1stPerson02
    with fade
    MB "{i}(whispering){/i} Relax though.... I don't judge, and I don't blame you one little bit."
    MB "{i}(whispering){/i} In fact, I can help you get what you want."
    scene bg Classroom1stPerson03
    with fade
    R "{i}(whispering){/i} What do you mean?"
    MB "{i}(whispering){/i} I mean I can help you conquer your mom."
    R "{i}(whispering){/i} Ha.... yeah right."
    MB "{i}(whispering){/i} I'm serious, all I would want in return is a go at her myself."
    MB "{i}(whispering){/i} And if you're willing to share, I'd be willing to share what I have with you."
    scene bg Classroom1stPerson01
    with fade
    RT "{i}If anyone could help me seduce Mom, it would probably be Matt.{/i}"
    RT "{i}Would I really be willing to share Mom with someone?{/i}"
    RT "{i}I could always use another ally in my quest to fuck Mom{/i}"
    RT "{i}But would it bother me if the treasure gets passed around?{/i}"
    RT "{i}And if I get to share what's Matt's, I could be getting way more treasure than just Mom.{/i}"
    RT "{i}Hmmm.... what should I do?{/i}"
    menu:
        "Accept Matt's help (\"WARNING\" future NTR content)":
            scene bg Classroom1stPerson03
            with fade
            $ ntrcontent = True
            R "{i}(whispering){/i} Ok, but the deal is that I get her first. After I've \"conquered\" her, then you can have a go at her."
            MB "{i}(whispering){/i} Ha.... I knew you were a horndog like me! Ok, just give me a little time and I'll figure something out."
            MB "{i}(whispering){/i} And to show you how committed I am, go into the first bathroom stall in the boy's bathroom during the afternoon and I'll send you a surprise."
            RT "{i}Hmmmm.... I wonder what the surprise could be.{/i}"
            M "So, to help him find the murderer, Oedipus calls for the great prophet Tiresias..."
            scene bg Classroom01
            with fade
            RT "{i}Oh good, class is finally over.{/i}"
            $ screen_on = "classmap"
            call screen classmap
        "Tell Matt to go fuck himself":
            scene bg Classroom1stPerson03
            with fade
            R "{i}(whispering){/i} You're a sick fuck. Did you know that?"
            R "{i}(whispering){/i} I don't know what your perverted imagination is coming up with, but I don't want to fuck my own mother!"
            MB "{i}(whispering){/i} yeah, well you're clearly in denial, and since you're pretending not to be interested, I think I'll just try to have a go at her anyways."
            R "{i}(whispering){/i} Don't you dare!"
            MB "{i}(whispering){/i} Ah ha.... I knew it!"
            MB "{i}(whispering){/i} Don't worry, I won't tell anyone, and I won't go after her, but if she comes sniffing around here, I won't be able to resist myself."
            R "{i}(whispering){/i} Yeah, right.... like that would ever happen."
            RT "{i}Would that ever happen?{/i}"
            RT "{i}I never thought Mom would take off her clothes in front of a bunch of horny guys either, but my own eyes proved me otherwise.{/i}"
            RT "{i}Maybe I better keep a close eye on her, now that Dad's in prison, she just might start shopping around. I better make sure she only has eyes for me.{/i}"
            M "So, to help him find the murderer, Oedipus calls for the great prophet Tiresias..."
            scene bg Classroom01
            with fade
            RT "{i}Oh good, class is finally over.{/i}"
            $ screen_on = "classmap"
            call screen classmap

label classlecture:
    if lectureprogress == 1:
        scene bg Classroom1stPerson01
        with fade
        M "Now Tiresias is being pressured by Oedipus to reveal to him what he knows of the murder of Laius..."
        RT "{i}So boring, how am I going to stay focused?{/i}"
        scene bg Classroom10
        with fade
        RT "{i}At least there is some good eye candy to entertain me through the lecture.{/i}"
        M "Oedipus grows angry, because Tiresias wishes he did not know who Laius' murderer is, and does not want to reveal to Oedipus and Thebes the truth."
        scene bg BlurryWhite
        with fade
        scene bg Classroom09
        with fade
        RT "{i}I can remember exactly what they look like.{/i}"
        RT "{i}To think I used to suck on those things! I wish I was right now!{/i}"
        M "Oedipus grows so angry after Tiresias reveals that Oedipus is the curse of Thebes, that he accuses Tiresias of conspiring with Creon to overthrow him."
        $ timeofdaycounter += 1
        $ lectureprogress = 2
        scene bg SleepBlack
        with fade
        scene bg Classroom03
        with fade
        M "Remember to read lines 508 to 750, and we'll start from here next time."
        "{i}{b}\"Mom's Respect +1\"{/b}{/i}"
        $ momrespect += 1
        if timeofdaycounter >=4:
            scene bg CityMap01
            with fade
            $ screen_on = "citymapmap"
            call screen citymapmap
        else:
            scene bg Classroom01
            with dissolve
            $ screen_on = "classmap"
            call screen classmap
    else:
        scene bg Classroom1stPerson01
        with fade
        RT "{i}So boring, how am I going to stay focused?{/i}"
        scene bg Classroom10
        with fade
        RT "{i}At least there is some good eye candy to entertain me through the lecture.{/i}"
        with fade
        scene bg Classroom09
        with fade
        RT "{i}I can remember exactly what they look like.{/i}"
        RT "{i}To think I used to suck on those things! I wish I was right now!{/i}"
        $ timeofdaycounter += 1
        if lectureprogress >= 3:
            scene bg SleepBlack
            with fade
        else:
            $ lectureprogress = 2
            scene bg SleepBlack
            with fade
        scene bg Classroom03
        with fade
        M "And we'll start from here next time."
        "{i}{b}\"Mom's Respect +1\"{/b}{/i}"
        $ momrespect += 1
        if timeofdaycounter >=4:
            scene bg CityMap01
            with fade
            $ screen_on = "citymapmap"
            call screen citymapmap
        elif timeofdaycounter == 3:
            jump classroomafternoon
        else:
            scene bg Classroom01
            with dissolve
            $ screen_on = "classmap"
            call screen classmap

##############  SCHOOL BATHROOM  ##################################

label schoolbathroom:
    if timeofdaycounter == 2:
        jump schoolbathroommorning
    else:
        jump schoolbathroomafternoon

label schoolbathroommorning:
    scene bg SchoolBathroom01
    with fade
    $ screen_on = "schoolbathmap"
    call screen schoolbathmap

label schoolbathroomafternoon:
    scene bg SchoolBathroom01
    with fade
    $ screen_on = "schoolbathmap"
    call screen schoolbathmap

label bathstall:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    if ntrcontent == True:
        while firstntrblowjob == False:
            jump stallbj
        if ntrcontent == True:
            scene bg SchoolBathroom01
            RT "{i}The scene of my first blowjob. Man! That was awesome! I've got to convince Matt to let Megan give me some more action.{/i}"
            $ screen_on = "schoolbathmap"
            call screen schoolbathmap
    else:
        if firstloyaltyblowjob:
            scene bg SchoolBathroom01
            RT "{i}The scene of my first blowjob. Man! That was awesome!{/i}"
            $ screen_on = "schoolbathmap"
            call screen schoolbathmap
        else:
            scene bg SchoolBathroom01
            RT "{i}I don't need to use the bathroom right now.{/i}"
            $ screen_on = "schoolbathmap"
            call screen schoolbathmap

label stallbj:
    $ persistent.gal_NTR_1 = True
    scene bg SchoolBathBlow01
    with fade
    play music SexMusic
    RT "{i}Ok, so Matt said to wait in the afternoon and he'd send me a surprise.{/i}"
    RT "{i}I wonder what it could be. Hmmm maybe dirty pictures of girls in our school? That would be awesome.{/i}"
    scene bg SchoolBathBlow02
    with dissolve
    "{i}\"knock knock knock\"{/i}"
    X "{i}(whispering){/i} Hey [ryan], is that you?"
    RT "{i}(whispering){/i} Yes it's me. Who's asking?"
    $ firstntrblowjob = True
    scene bg SchoolBathBlow03
    with dissolve
    MG "Hey there, stud. Are you ready to get your knob polished?"
    R ".... What?!!.... Am I?.... Did Matt send you?"
    MG "No, I've just had an insatiable craving for your cock!.... Haha.... of course Matt sent me."
    MG "He said he owes you a favor?"
    R "Well yeah, but this isn't what I was expecting.... wow!!"
    scene bg SchoolBathBlow04
    with fade
    MG "Wow yourself, you're already hard, and almost as big as he is!"
    MG "Now just relax while I take care of you."
    MG "You'll find that it's nice to have Matt owe you a favor."
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

label megan_tip:
    play sound Blow02 loop
    scene MeganBJVideo01
    with dissolve
    $ renpy.pause ()
    menu:
        "Deeper":
            play sound Blow03 loop
            jump megan_deeper
        "Throat Fuck":
            play sound Blow03 loop
            jump megan_throat
        "Cum" if firstntrblowjob:
            play sound Blow03 loop
            jump megan_cum_ntr
        "Cum" if firstloyaltyblowjob:
            play sound Blow03 loop
            jump megan_cum

label megan_deeper:
    scene MeganBJVideo02
    with dissolve
    $ renpy.pause ()
    menu:
        "Just the tip":
            jump megan_tip
        "Throat Fuck":
            jump megan_throat
        "Cum" if firstntrblowjob:
            jump megan_cum_ntr
        "Cum" if firstloyaltyblowjob:
            jump megan_cum

label megan_throat:
    scene MeganBJVideo03
    with dissolve
    $ renpy.pause ()
    menu:
        "Just the tip":
            jump megan_tip
        "Deeper":
            jump megan_deeper
        "Cum" if firstntrblowjob:
            jump megan_cum_ntr
        "Cum" if firstloyaltyblowjob:
            jump megan_cum

label megan_cum_ntr:
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
            MG "Hrahrahra.... wrell gret Mratt tro owre ru anrother fravor, arnd I'rrll sree ru agrain sroon."
            MG "{i}\"Glurp.... glurp.... \"{/i}"
            play music Honey
            scene bg CityMap01
            with fade
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
            R "Thank you for that my first blowjob!!"
            MG "Hahaha.... don't mention it! Just get Matt to owe you some more favors and there will be more where that came from."
            play music Honey
            scene bg CityMap01
            with fade
            $ screen_on = "citymapmap"
            call screen citymapmap

####  Girls Lockers  ########################  Girls Lockers  ##############################  Girls Lockers  ###############################################################################################

label girlslockers:
    if timeofdaycounter == 2:
        jump girlslockersmorning
    else:
        jump girlslockersafternoon

label girlslockersmorning:
    scene bg LockerRoom03
    with fade
    RT "{i}What am I doing here? I could get in a lot of trouble if somebody sees me.{/i}"
    $ screen_on = "girlslockermap"
    call screen girlslockermap

label girlslockersafternoon:
    scene bg LockerRoom03
    with fade
    RT "{i}What am I doing here? I could get in a lot of trouble if somebody sees me.{/i}"
    $ screen_on = "girlslockermap"
    call screen girlslockermap

label girllocker:
    if show_map:
        $ show_map = False
        if any([screen_on == "{}".format(k) for k in nav_home_location]):
            hide screen nav_house
        elif any([screen_on == "{}".format(k) for k in nav_school_location]):
            hide screen nav_school
    scene bg LockerRoom
    RT "{i}Nothing in here.{/i}"
    if not start_of_campaign:
        $ screen_on = "girlslockermap"
        call screen girlslockermap
    else:
        $ screen_on = "newgirlslockermap"
        call screen newgirlslockermap

################################################################################################################################################################################################

label citymap:
    if timeofdaycounter == 5:
        scene bg CityMapNight
        with fade
        $ screen_on = "citymapmapnight"
        call screen citymapmapnight

    if timeofdaycounter >= 2 and timeofdaycounter <= 3 and will_strategy and not will_visit:
        jump will_meeting_map

    if timeofdaycounter == 4 and daycounter <= 5 and strategy_set and not campaign_finished:
        jump diaz_help_map

    else:
        scene bg CityMap01
        with fade
        $ screen_on = "citymapmap"
        call screen citymapmap

label stripclub:
    if first_mafia_chat and first_money_chat and first_club_fun and park_full_menu and daycounter == 1 and progress == 15:
        jump sid_sex_event
    if timeofdaycounter == 5 and sidney_took_job and daycounter != 6 and sidneys_working and visited_sid == False:
        jump club_casino_with_sid
    if visited_sid:
        scene bg CityMapNight
        RT "{i}I've already been there tonight.{/i}"
        $ screen_on = "citymapmapnight"
        call screen citymapmapnight
    if sawmomstripping == True:
        scene bg CityMapNight
        RT "{i}I better not try to push my luck anymore tonight.{/i}"
        $ screen_on = "citymapmapnight"
        call screen citymapmapnight
    if momatclub == True:
        jump club_casino
    if timeofdaycounter == 5:
        while progress >= 3:
            scene bg CityMapNight
            RT "{i}They'll only let me in while Mom is working.{/i}"
            $ screen_on = "citymapmapnight"
            call screen citymapmapnight
        if timeofdaycounter == 5:
            scene bg CityMapNight
            RT "{i}They wouldn't let a minor in.{/i}"
            $ screen_on = "citymapmapnight"
            call screen citymapmapnight

    else:
        scene bg CityMap01
        RT "{i}It's only open at night.{/i}"
        $ screen_on = "citymapmap"
        call screen citymapmap

label warehous_studion:
    scene bg streets
    with fade
    RT "{i}Ok, off to the studio!{/i}"
    scene TravelVideo01
    with dissolve
    $ renpy.pause (1.5)
    scene bg TravelVideoF01
    $ renpy.pause (0.95)

    jump photostudio

label warehouse:
    if dadpictureprogress == 0:
        scene bg CityMap01
        "(Wait! I know you're in a hurry to go see Uncle Bobby, but you really need to go check out the portrait in the lounge.)"
        "(It's just nice to have some back-story.)"
        "(If you're just really not into backstory, you can just click on [dad_name], the dad, and rush through his whole spiel, then you will be able to come back here and see Uncle Bobby.)"
        "(Good Luck)"
        jump lounge
    if timeofdaycounter == 5:
        scene bg CityMapNight
        RT "{i}It's too dangerous to go at night.{/i}"
        $ screen_on = "citymapmapnight"
        call screen citymapmapnight
    elif bobby_send_text == True and bobby_says_bye == False:
        jump bye_bobby
    else:
        scene bg streets
        with fade
        RT "{i}Ok, off to the warehouse!{/i}"
        scene TravelVideo01
        with dissolve
        $ renpy.pause (2.5)
        scene bg TravelVideoF01
        $ renpy.pause ()
        scene bg warehouse
        with fade

        if progress == 1:

            RT "{i}I wonder where he is?{/i}"
            show 03Bobbythink
            with dissolve
            B "Oh good, you're finally here!"
            R ".... What in the hell is going on, Uncle Bobby?..."
            $ mompictureprogress = 2
            $ laurenpictureprogress = 2
            $ dadpictureprogress = 2
            show 04Bobbyconcerned
            with dissolve
            B "Relax kid, you're out of breath, have some whisky or something."
            R "I'm too young to drink."
            B "Ehh.... suit yourself. More for me. {p}God knows I need a few more!"
            show 01Bobbynormal
            with dissolve
            R "What's going on, Uncle Bobby?"
            B "The Feds got wise to us, is what's going on."
            R "The Feds got wise to what?"
            show 01Bobbynormal
            B "To our not so legitimate business operations."
            R ".... {p}..."
            show 02Bobbylookup
            with dissolve
            B "To the fact that we have been facilitating the movement of items of questionable legality for groups of questionable reputation."
            R ".... What?.... Dad's been breaking the law?!"
            hide 02Bobbylookup
            with dissolve
            hide 01Bobbynormal
            hide 04Bobbyconcerned
            B "More like skirting the law, but the Feds don't seem to notice no distinction."
            R ".... I.... I.... can't believe this? my father's a real-life criminal?"
            B "Yeah.... well, don't think too bad of your old man. {p}Your family's been living pretty well as a result of his hard work."
            B "He's built this business from nothing, and taken some incredible risks along the way. {p}All of which have paid off in the end."
            R "Paid off!?! He's in fucking jail!"
            show 04Bobbyconcerned
            with dissolve
            B "Yeah, well... present circumstances excluded."
            R "How did he get caught?"
            B "They busted him last night on a late delivery.{p}Luckily he wasn't in a company ride, or on company property, but now we're being heavily watched and investigated."
            R "Dad said on the phone that we could be in danger, or trouble?"
            show 01Bobbynormal
            with dissolve
            B "Yes.... so that's the tricky part. {p}Your dad recently took out a sizable loan from the DeCapo crime family."
            B "It's a personal handshake loan, no paper trail, so the feds have no idea about it. {p}But just because your dads going to be in prison, doesn't mean they don't expect to be paid."
            B "The good news is we talked this morning, and I let 'em know about present circumstances."
            B "As a good will gesture to [dad_name] for not ratting them out, they said they're willing to accept interest-only payments for a short while, until we can figure something else out."
            R "WHAT?.... We're expected to pay Dad's loan while he's in prison?..."
            B "Well, [dad_name] used his household as collateral, and since we're dealing with the Mafia, that includes human capital. So, if you don't pay, they'll basically human traffic you into white slavery... Even you pretty boy."
            R "Fuck!"
            hide 01Bobbynormal
            with dissolve
            R "Can't you?.... Or.... or.... or.... the business pay back the loan for us?"
            B "I'm sorry, but this is strictly off the books, and the Feds have seized all our cash, frozen all of our assets and accounts, including my personal ones."
            B "We have a federal accountant in our office, right now, as we speak, that will be controlling all the movement of funds until the investigation is over."
            B "If I had anything extra to give you, it would be yours, but I have to take care of my own wife and daughter. The Feds will only allow me enough to survive on."
            R "Can't we just tell the police about the DeCapos?"
            B "If you want the DeCapos to put a hit on your old man, they can get him in prison you know.{p}But they'll come after his wife first, to teach him a lesson.{p}They have people everywhere. The police can't protect her."
            show 02Bobbylookup
            with dissolve
            R "Shit..."
            R "Shit!..."
            R ".... SHIT!!..."
            R "Well, how much are the payments?"
            B "For now.... only $1,000 dollars each week."
            R "Pfft.... $1,000 DOLLARS EACH WEEK? I'm only in high school. Where am I going to come up with that kind of cash?"
            B "Just relax kid, I have a way for you to make some extra money."
            B "We still have a pretty large pile of contraband in our underground warehouse, and we still have clients who expect delivery of said goods."
            B "If you can come here during the afternoons, you can make these deliveries for us. I even have a little pizza box container we can attach right onto your scooter to carry the packages."
            B "No one will ever suspect a young pizza delivery boy."
            B "The clients will pay you directly, and you can keep the money they give you."
            B "Some of them are fairly generous and will even give you some decent tips."
            B "The FBI has no reason to suspect you, so it should be relatively low risk."
            show 01Bobbynormal
            with dissolve
            B "If you're not able to make the deliveries some days, or if you find a better way to make the cash, I'll just have to make the deliveries myself.{p}It will be riskier since I'm being watched, but the deliveries have to be made."
            B "So what do you think?"
            R ".... {p}I don't think I have a choice,{p}.... so I guess I'm in?..."
            B "Great!.... Oh, and here's the little bit of cash I do have,"
            "{i}Received $300 dollars.{/i}"
            $ money += 300
            B "Hopefully It can help you make this week's payment."
            R ".... Thanks.... oh, and how do I make the payments?"
            B "Every Saturday evening, the DeCapos will send a couple guys to your front door to pick up the money."
            hide 01Bobbynormal
            with dissolve
            hide 02Bobbylookup
            hide 04Bobbyconcerned
            B "You pay them the money and bada bing bada boom, they'll be on their merry way."
            R "Saturday!.... But that's today!!.... How will I get the money together by this evening?"
            B "With the $300 I gave you, and if you make deliveries today. And hopefully your mom has a little cash on her. Hopefully you'll have enough..."
            B ".... I'll be praying to the Virgin Mary that you can make it."
            R "{i}(sarcastically){/i} Oh.... that's a relief."
            show 04Bobbyconcerned
            with dissolve
            B "Sorry.... I wish there was more I could do.... If there was anything else I'd do it."
            R "I know.... really.... thanks for helping us out."
            B "You're welcome! And be safe on your deliveries. Try to make sure no one is following you, and if they are, return here immediately."
            R "Alright, I'll keep an eye out,{p}and thanks again."
            B "Oh Right.... one more thing I almost forgot! If your mom asks what you're doing to make this extra money, just tell her you're doing some janitorial work for us."
            B "I don't thinks she'd be too thrilled if she suspected you were making deliveries for your old man."
            show 02Bobbylookup
            with dissolve
            B "Capisce?"
            R "Yeah.... I capisce."
            B "Great, now go hook that pizza box to your scooter, and go make some deliveries."
            $ progress = 2
            $ timeofdaycounter += 2
            menu:
                "Make Deliveries":
                    scene TravelVideo02
                    with fade
                    $ renpy.pause (4.5)
                    scene bg TravelVideoF01
                    $ renpy.pause ()
                    $ deliverymoney = renpy.random.randint(1, 6)
                    if deliverymoney == 1:
                        $ money += 200
                        "{i}\"You received $200 and no tips.\"{/i}"
                        $ timeofdaycounter +=1
                        scene bg CityMap01
                        with fade
                        $ screen_on = "citymapmap"
                        call screen citymapmap
                    elif deliverymoney == 2:
                        $ money += 250
                        "{i}\"You received $200 and $50 in tips.\"{/i}"
                        $ timeofdaycounter +=1
                        scene bg CityMap01
                        with fade
                        $ screen_on = "citymapmap"
                        call screen citymapmap
                    elif deliverymoney == 3:
                        $ money += 300
                        "{i}\"You received $200 and $100 in tips.\"{/i}"
                        $ timeofdaycounter +=1
                        scene bg CityMap01
                        with fade
                        $ screen_on = "citymapmap"
                        call screen citymapmap
                    elif deliverymoney == 4:
                        $ money += 350
                        "{i}\"You received $200 and $150 in tips.\"{/i}"
                        $ timeofdaycounter +=1
                        scene bg CityMap01
                        with fade
                        $ screen_on = "citymapmap"
                        call screen citymapmap
                    elif deliverymoney == 5:
                        $ money += 400
                        "{i}\"You received $200 and $200 in tips.\"{/i}"
                        $ timeofdaycounter +=1
                        scene bg CityMap01
                        with fade
                        $ screen_on = "citymapmap"
                        call screen citymapmap
                    elif deliverymoney == 6:
                        $ money += 450
                        "{i}\"You received $200 and $250 in tips.\"{/i}"
                        $ timeofdaycounter +=1
                        scene bg CityMap01
                        with fade
                        $ screen_on = "citymapmap"
                        call screen citymapmap
        else:
            menu:
                "Make Deliveries":
                    if timeofdaycounter == 3:
                        scene TravelVideo02
                        with fade
                        $ renpy.pause (4.5)
                        scene bg TravelVideoF01
                        $ renpy.pause ()
                        $ deliverymoney = renpy.random.randint(1, 6)
                        if deliverymoney == 1:
                            $ money += 200
                            "{i}\"You received $200 and no tips.\"{/i}"
                            $ timeofdaycounter +=1
                            scene bg CityMap01
                            with fade
                            $ screen_on = "citymapmap"
                            call screen citymapmap
                        elif deliverymoney == 2:
                            $ money += 250
                            "{i}\"You received $200 and $50 in tips.\"{/i}"
                            $ timeofdaycounter +=1
                            scene bg CityMap01
                            with fade
                            $ screen_on = "citymapmap"
                            call screen citymapmap
                        elif deliverymoney == 3:
                            $ money += 300
                            "{i}\"You received $200 and $100 in tips.\"{/i}"
                            $ timeofdaycounter +=1
                            scene bg CityMap01
                            with fade
                            $ screen_on = "citymapmap"
                            call screen citymapmap
                        elif deliverymoney == 4:
                            $ money += 350
                            "{i}\"You received $200 and $150 in tips.\"{/i}"
                            $ timeofdaycounter +=1
                            scene bg CityMap01
                            with fade
                            $ screen_on = "citymapmap"
                            call screen citymapmap
                        elif deliverymoney == 5:
                            $ money += 400
                            "{i}\"You received $200 and $200 in tips.\"{/i}"
                            $ timeofdaycounter +=1
                            scene bg CityMap01
                            with fade
                            $ screen_on = "citymapmap"
                            call screen citymapmap
                        elif deliverymoney == 6:
                            $ money += 450
                            "{i}\"You received $200 and $250 in tips.\"{/i}"
                            $ timeofdaycounter +=1
                            scene bg CityMap01
                            with fade
                            $ screen_on = "citymapmap"
                            call screen citymapmap
                    else:
                        "I can only make deliveries in the afternoon."
                        scene bg CityMap01
                        with fade
                        $ screen_on = "citymapmap"
                        call screen citymapmap
                "Pick up Items" if progress >= 3:
                    scene bg warehouse
                    if futchocolate == 1:
                        scene bg warehouse
                        $ inventory.add(chocolate)
                        $ futchocolate = 0
                        "\"You received a chocolate bar\""
                    elif futchocolate == 2:
                        scene bg warehouse
                        $ inventory.add(chocolate)
                        $ inventory.add(chocolate)
                        $ futchocolate = 0
                        "\"You received two chocolate bars\""
                    elif futchocolate == 3:
                        scene bg warehouse
                        $ inventory.add(chocolate)
                        $ inventory.add(chocolate)
                        $ inventory.add(chocolate)
                        $ futchocolate = 0
                        "\"You received three chocolate bars\""
                    if futgiftcard == 1:
                        scene bg warehouse
                        $ inventory.add(giftcard)
                        $ futgiftcard = 0
                        "\"You received a gift card.\""
                    elif futgiftcard == 2:
                        scene bg warehouse
                        $ inventory.add(giftcard)
                        $ inventory.add(giftcard)
                        $ futgiftcard = 0
                        "\"You received two gift cards.\""
                    elif futgiftcard == 3:
                        scene bg warehouse
                        $ inventory.add(giftcard)
                        $ inventory.add(giftcard)
                        $ inventory.add(giftcard)
                        $ futgiftcard = 0
                        "\"You received three gift cards.\""
                    if futflowers == 1:
                        scene bg warehouse
                        $ inventory.add(flowers)
                        $ futflowers = 0
                        "\"You received a bouquet of flowers.\""
                    elif futflowers == 2:
                        scene bg warehouse
                        $ inventory.add(flowers)
                        $ inventory.add(flowers)
                        $ futflowers = 0
                        "\"You received two bouquet of flowers.\""
                    elif futflowers == 3:
                        scene bg warehouse
                        $ inventory.add(flowers)
                        $ inventory.add(flowers)
                        $ inventory.add(flowers)
                        $ futflowers = 0
                        "\"You received three bouquet of flowers.\""
                    if futmelatonin == 1:
                        scene bg warehouse
                        $ inventory.add(melatonin)
                        "\"You received one bottle of Melatonin\""
                        $ sidneypictureprogress = 5
                        $ laurenpictureprogress = 6
                        $ futmelatonin = 0
                    if futspycam == 1:
                        scene bg warehouse
                        $ inventory.add(spycam)
                        $ futspycam = 0
                        "\"You received a webcam.\""
                    elif futspycam == 2:
                        scene bg warehouse
                        $ inventory.add(spycam)
                        $ inventory.add(spycam)
                        $ futspycam = 0
                        "\"You received two webcams.\""
                    elif futspycam == 3:
                        scene bg warehouse
                        $ inventory.add(spycam)
                        $ inventory.add(spycam)
                        $ inventory.add(spycam)
                        $ futspycam = 0
                        "\"You received three webcams.\""
                    if futgreen_screen == 1:
                        scene bg warehouse
                        $ inventory.add(green_screen)
                        $ futgreen_screen = 0
                        "\"You received a green screen.\""
                    if futpro_lights == 1:
                        scene bg warehouse
                        $ inventory.add(pro_lights)
                        $ futpro_lights = 0
                        "\"You received some photo studio professional lights.\""
                    if futcamera == 1:
                        scene bg warehouse
                        $ inventory.add(camera)
                        $ futcamera = 0
                        "\"You received a DSLR camera.\""
                    if futaccessories_1 == 1:
                        scene bg warehouse
                        $ inventory.add(camera_accessories_1)
                        $ futaccessories_1 = 0
                        "\"You received a new camera accessory.\""
                    if futaccessories_2 == 1:
                        scene bg warehouse
                        $ inventory.add(camera_accessories_2)
                        $ futaccessories_2 = 0
                        "\"You received a new camera accessory.\""
                    if futaccessories_3 == 1:
                        scene bg warehouse
                        $ inventory.add(camera_accessories_3)
                        $ futaccessories_3 = 0
                        "\"You received a new camera accessory.\""
                    if futaccessories_4 == 1:
                        scene bg warehouse
                        $ inventory.add(camera_accessories_4)
                        $ futaccessories_4 = 0
                        "\"You received a new camera accessory.\""
                    if futaccessories_5 == 1:
                        scene bg warehouse
                        $ inventory.add(camera_accessories_5)
                        $ futaccessories_5 = 0
                        "\"You received a new camera accessory.\""
                    if futaccessories_6 == 1:
                        scene bg warehouse
                        $ inventory.add(camera_accessories_6)
                        $ futaccessories_6 = 0
                        "\"You received a new camera accessory.\""
                    if futaccessories_7 == 1:
                        scene bg warehouse
                        $ inventory.add(camera_accessories_7)
                        $ futaccessories_7 = 0
                        "\"You received a new camera accessory.\""
                    if futaccessories_8 == 1:
                        scene bg warehouse
                        $ inventory.add(camera_accessories_8)
                        $ futaccessories_8 = 0
                        "\"You received a new camera accessory.\""
                    if futj_bikini_1 == 1:
                        scene bg warehouse
                        $ inventory.add(jacky_bikini_01)
                        $ futj_bikini_1 = 0
                        "\"You received a new swimsuit.\""
                    if fut_ball_gag == 1:
                        scene bg warehouse
                        $ ball_gag_owned = True
                        $ inventory.add(ball_gag)
                        $ fut_ball_gag = 0
                        "\"You received a ball gag.\""
                    if fut_ph_book1 == 1:
                        scene bg warehouse
                        $ first_book_owned = True
                        $ inventory.add(ph_book1)
                        $ fut_ph_book1 = 0
                        "\"You recieved the book \"Perry Hotter and the Sorceror's Bone\""
                    if fut_ph_book2 == 1:
                        scene bg warehouse
                        $ second_book_owned = True
                        $ inventory.add(ph_book2)
                        $ fut_ph_book2 = 0
                        "\"You recieved the book \"Perry Hotter and her Chambers of Secrets.\""
                    if fut_ph_book3 == 1:
                        scene bg warehouse
                        $ third_book_owned = True
                        $ inventory.add(ph_book3)
                        $ fut_ph_book3 = 0
                        "\"You recieved the book \"Perry Hotter and the prisoner of Moldevorts Dungeon.\""
                    else:
                        scene bg warehouse
                        "\"There's nothing else to do here.\""
                    jump warehousealso
                "Go to Photo Studio." if progress >= 11 and daycounter != 6 and daycounter != 7:
                    jump photostudio
                "Return to Map":
                    scene bg CityMap01
                    with fade
                    $ screen_on = "citymapmap"
                    call screen citymapmap

label warehousealso:
    scene bg warehouse
    with fade
    menu:
        "Make Deliveries":
            if timeofdaycounter == 3:
                scene TravelVideo02
                with fade
                $ renpy.pause (4.5)
                scene bg TravelVideoF01
                $ renpy.pause ()
                $ deliverymoney = renpy.random.randint(1, 6)
                if deliverymoney == 1:
                    $ money += 200
                    "{i}\"You received $200 and no tips.\"{/i}"
                    $ timeofdaycounter +=1
                    scene bg CityMap01
                    with fade
                    $ screen_on = "citymapmap"
                    call screen citymapmap
                elif deliverymoney == 2:
                    $ money += 250
                    "{i}\"You received $200 and $50 in tips.\"{/i}"
                    $ timeofdaycounter +=1
                    scene bg CityMap01
                    with fade
                    $ screen_on = "citymapmap"
                    call screen citymapmap
                elif deliverymoney == 3:
                    $ money += 300
                    "{i}\"You received $200 and $100 in tips.\"{/i}"
                    $ timeofdaycounter +=1
                    scene bg CityMap01
                    with fade
                    $ screen_on = "citymapmap"
                    call screen citymapmap
                elif deliverymoney == 4:
                    $ money += 350
                    "{i}\"You received $200 and $150 in tips.\"{/i}"
                    $ timeofdaycounter +=1
                    scene bg CityMap01
                    with fade
                    $ screen_on = "citymapmap"
                    call screen citymapmap
                elif deliverymoney == 5:
                    $ money += 400
                    "{i}\"You received $200 and $200 in tips.\"{/i}"
                    $ timeofdaycounter +=1
                    scene bg CityMap01
                    with fade
                    $ screen_on = "citymapmap"
                    call screen citymapmap
                elif deliverymoney == 6:
                    $ money += 450
                    "{i}\"You received $200 and $250 in tips.\"{/i}"
                    $ timeofdaycounter +=1
                    scene bg CityMap01
                    with fade
                    $ screen_on = "citymapmap"
                    call screen citymapmap
            else:
                "I can only make deliveries in the afternoon."
                scene bg CityMap01
                with fade
                $ screen_on = "citymapmap"
                call screen citymapmap
        "Pick up Items" if progress >= 3:
            scene bg warehouse
            if futchocolate == 1:
                scene bg warehouse
                $ inventory.add(chocolate)
                $ futchocolate = 0
                "\"You received a chocolate bar\""
            elif futchocolate == 2:
                scene bg warehouse
                $ inventory.add(chocolate)
                $ inventory.add(chocolate)
                $ futchocolate = 0
                "\"You received two chocolate bars\""
            elif futchocolate == 3:
                scene bg warehouse
                $ inventory.add(chocolate)
                $ inventory.add(chocolate)
                $ inventory.add(chocolate)
                $ futchocolate = 0
                "\"You received three chocolate bars\""
            if futgiftcard == 1:
                scene bg warehouse
                $ inventory.add(giftcard)
                $ futgiftcard = 0
                "\"You received a gift card.\""
            elif futgiftcard == 2:
                scene bg warehouse
                $ inventory.add(giftcard)
                $ inventory.add(giftcard)
                $ futgiftcard = 0
                "\"You received two gift cards.\""
            elif futgiftcard == 3:
                scene bg warehouse
                $ inventory.add(giftcard)
                $ inventory.add(giftcard)
                $ inventory.add(giftcard)
                $ futgiftcard = 0
                "\"You received three gift cards.\""
            if futflowers == 1:
                scene bg warehouse
                $ inventory.add(flowers)
                $ futflowers = 0
                "\"You received a bouquet of flowers.\""
            elif futflowers == 2:
                scene bg warehouse
                $ inventory.add(flowers)
                $ inventory.add(flowers)
                $ futflowers = 0
                "\"You received two bouquet of flowers.\""
            elif futflowers == 3:
                scene bg warehouse
                $ inventory.add(flowers)
                $ inventory.add(flowers)
                $ inventory.add(flowers)
                $ futflowers = 0
                "\"You received three bouquet of flowers.\""
            if futmelatonin == 1:
                scene bg warehouse
                $ inventory.add(melatonin)
                "\"You received one bottle of Melatonin\""
                $ sidneypictureprogress = 5
                $ laurenpictureprogress = 6
                $ futmelatonin = 0
            if futspycam == 1:
                scene bg warehouse
                $ inventory.add(spycam)
                $ futspycam = 0
                "\"You received a webcam.\""
            elif futspycam == 2:
                scene bg warehouse
                $ inventory.add(spycam)
                $ inventory.add(spycam)
                $ futspycam = 0
                "\"You received two webcams.\""
            elif futspycam == 3:
                scene bg warehouse
                $ inventory.add(spycam)
                $ inventory.add(spycam)
                $ inventory.add(spycam)
                $ futspycam = 0
                "\"You received three webcams.\""
            if futgreen_screen == 1:
                scene bg warehouse
                $ inventory.add(green_screen)
                $ futgreen_screen = 0
                "\"You received a green screen.\""
            if futpro_lights == 1:
                scene bg warehouse
                $ inventory.add(pro_lights)
                $ futpro_lights = 0
                "\"You received some photo studio professional lights.\""
            if futcamera == 1:
                scene bg warehouse
                $ inventory.add(camera)
                $ futcamera = 0
                "\"You received a DSLR camera.\""
            if futaccessories_1 == 1:
                scene bg warehouse
                $ inventory.add(camera_accessories_1)
                $ futaccessories_1 = 0
                "\"You received a new camera accessory.\""
            if futaccessories_2 == 1:
                scene bg warehouse
                $ inventory.add(camera_accessories_2)
                $ futaccessories_2 = 0
                "\"You received a new camera accessory.\""
            if futaccessories_3 == 1:
                scene bg warehouse
                $ inventory.add(camera_accessories_3)
                $ futaccessories_3 = 0
                "\"You received a new camera accessory.\""
            if futaccessories_4 == 1:
                scene bg warehouse
                $ inventory.add(camera_accessories_4)
                $ futaccessories_4 = 0
                "\"You received a new camera accessory.\""
            if futaccessories_5 == 1:
                $ inventory.add(camera_accessories_5)
                $ futaccessories_5 = 0
                "\"You received a new camera accessory.\""
            if futaccessories_6 == 1:
                scene bg warehouse
                $ inventory.add(camera_accessories_6)
                $ futaccessories_6 = 0
                "\"You received a new camera accessory.\""
            if futaccessories_7 == 1:
                scene bg warehouse
                $ inventory.add(camera_accessories_7)
                $ futaccessories_7 = 0
                "\"You received a new camera accessory.\""
            if futaccessories_8 == 1:
                scene bg warehouse
                $ inventory.add(camera_accessories_8)
                $ futaccessories_8 = 0
                "\"You received a new camera accessory.\""
            if futj_bikini_1 == 1:
                scene bg warehouse
                $ inventory.add(jacky_bikini_01)
                $ futj_bikini_1 = 0
                "\"You received a new swimsuit.\""
            if fut_ball_gag == 1:
                scene bg warehouse
                $ ball_gag_owned = True
                $ inventory.add(ball_gag)
                $ fut_ball_gag = 0
                "\"You received a ball gag.\""
            if fut_ph_book1 == 1:
                scene bg warehouse
                $ first_book_owned = True
                $ inventory.add(ph_book1)
                $ fut_ph_book1 = 0
                "\"You recieved the book \"Perry Hotter and the Sorceror's Bone\""
            if fut_ph_book2 == 1:
                scene bg warehouse
                $ second_book_owned = True
                $ inventory.add(ph_book2)
                $ fut_ph_book2 = 0
                "\"You recieved the book \"Perry Hotter and her Chambers of Secrets.\""
            if fut_ph_book3 == 1:
                scene bg warehouse
                $ third_book_owned = True
                $ inventory.add(ph_book3)
                $ fut_ph_book3 = 0
                "\"You recieved the book \"Perry Hotter and the prisoner of Moldevorts Dungeon.\""
            else:
                scene bg warehouse
                "\"There's nothing left to do here.\""
            jump warehousealso
        "Go to Photo Studio." if progress >= 11 and daycounter != 6 and daycounter != 7:
            jump photostudio
        "Return to Map":
            scene bg CityMap01
            with fade
            $ screen_on = "citymapmap"
            call screen citymapmap

label dinnerfirst:
    scene bg FirstDinner
    with fade
    RT "{i}Oh, man.... I can't get my conversation with Uncle Bobby out of my head. {p}More importantly, how do I tell Mom and Lauren about it?{/i}"
    menu:
        "Ask Mom about her day":
            scene bg DinnerAttnMom03
            with dissolve
            $ momaffection += 1
            "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
            M "Oh, honey, it was just terrible.... men from the FBI were here all day, going through our things, digging through our garbage, making copies of all our computer drives."
            RT "{i}Oh, shit.... well, I guess they're going to find my porn collection. Hopefully they don't know what kind of games \"Milfy City\" and \"Big Brother\" are.{/i}"
            M "Having your privacy invaded like that makes me feel so vulnerable. Almost naked, you know?"
            M "So what did Uncle Bobby have to say?"
            menu:
                "Tell them about the conversation with Uncle Bobby":
                    scene bg SleepBlack
                    with fade
                    "{i}10 minutes later.... {/i}"

        "Ask Lauren about her day":
            scene bg DinnerAttnLauren01
            with dissolve
            $ laurenaffection += 1
            "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
            L "OMG [ryan], you missed everything! A bunch of hunky FBI guys were here digging through all our junk, combing through our trash. They even copied everything on my phone and our computers! I better not find any of my selfies on the internet!"
            RT "{i}Oh, shit.... well, I guess they're going to find my porn collection. Hopefully they don't know what kind of games \"Milfy City\" and \"Big Brother\" are.{/i}"
            L "One of the agents kept staring at my ass. She really gave me the creeps!"
            L "So where have you been all day?"
            menu:
                "Tell them about visit with Uncle Bobby":
                    scene bg SleepBlack
                    with fade
                    "{i}10 minutes later.... {/i}"

    scene bg DinnerAttnRyan02
    with fade
    $ progress = 3
    R "And so somehow we have to come up with the rest of the money before the DeCapo thugs come over, which could be any minute!"
    R "Do either of you have any cash lying around?"
    $ mompictureprogress = 3
    $ laurenpictureprogress = 3
    scene bg DinnerAttnMom01
    with dissolve
    M "OH NO!.... No! We don't have any extra cash!{p}The FBI made me open our safe and they confiscated all our emergency cash. They gave me this debit card, with only enough money to pay our bills and buy food, and they are monitoring all of our transactions."
    scene bg DinnerAttnLauren02
    with dissolve
    L "Don't look at me, it's not like I have a secret stash of cash hidden under my bed!"
    scene bg DinnerAttnLauren03
    with dissolve
    R "Well, shit! What are we going to do?"
    scene bg DinnerAttnRyan01
    with dissolve
    M "Language, [ryan]!"
    R "We're about to have our legs broken, and you're worried about me saying \"shit\"?"
    M "Yes! Where did you ever learn to be so crass?"
    "\"{b}KNOCK\" \"KNOCK\" \"KNOCK{/b}\""
    scene bg MomCloseupDinner
    with fade
    M "Oh, fuck! Oh, shit! They're here!"
    MT "{i}SHIT!! Think [mom_name]! Think! What am I going to do?{/i}"
    scene bg DinnerAttnMom01
    with fade
    M "[ryan].... give me the cash that you have."
    "{i}\"Money = $0\"{/i}"
    $ money = 0
    M "Lauren, you and [ryan] go into the kitchen and do the dishes while I go talk to the gentlemen at the door."
    M "I'm sure I can work something out that doesn't involve violence."
    M "So just get the dishes done, and I'll be back as soon as I'm done talking to them!"
    scene bg DoingDishesWLauren01
    with fade
    "{i}10 minutes later.... {/i}"
    L "... And all the sexts I sent to my ex-boyfriend were still on my phone."
    R "Would you shut up about your stupid phone? We're about to be murdered by the mob, and all you can think of is your stupid phone!"
    L "Oh, just relax!.... Mom will take care of everything. She always does."
    scene bg DoingDishesWLauren02
    with dissolve
    R "Dad said I'm the man of the house now! I'm the one who should be out there working things out with the DeCapo's!"
    L "Hahahaha.... you the man of the house? Hahaha.... I wouldn't trust you to work things out with the school bully, let alone a bunch of Mafiosos."
    R "Just wait and see! I'll fix all of this, and earn everyone's respect!"
    L "Yeah, and on that day I'll let you fuck me in the ass!"
    R "Gross, why would you say something like that!"
    scene bg DoingDishesMom01
    with dissolve
    M "Hey guys, I'm back. Thanks for cleaning up!"
    scene bg DoingDishesMom02
    with dissolve
    R "Oh, thank God! Is everything ok?"
    M "Yes, everything is fine. I worked everything out with Joey."
    L "Joey, who's Joey?"
    M "Oh, I don't know his last name, maybe it's DeCapo, but he was over this summer for your lousy dad's work BBQ."
    M "Way overdressed for the occasion."
    L "Oh yeah, I think I remember him."
    scene bg DoingDishesMom03
    with dissolve
    M "Right, so he has a small job tonight that he said I'm more than qualified for, and can earn the other $500 in just a couple hours."
    R "No, wait!.... You're going to take a job from a Mafia goon, where you'll make $500 in a couple hours? That sounds like a bad idea!"
    M "Yeah, well it's not like I have a lot of options here!{p}I don't want to go, but at least it will keep us safe until we have to make another payment next week!"
    R "Ok.... so then what is the job?"
    M ".... It's none of your business!"
    R "Is it legal?"
    M "Of course it's legal! What do you think I am?"
    R "Well, why won't you tell us, and what's with the bag?"
    M "I already told you that it's none of your business! So don't ask again!"
    M "Finish cleaning up!"
    M "I'll be home very late!"
    scene bg DishesNoMom01
    with dissolve
    R "Oh, shit!"
    L "What?"
    R "What do you mean \"What?\"."
    R "Mom's leaving our house with the mob, to do a job for the mob, to pay off the mob!"
    L "I'm sure she's going to be fine?"
    R "I'm going to follow her, and make sure she'll be ok."
    scene bg DishesNoMom02
    with dissolve
    L "What about me? You can't just leave me here alone."
    L "I'll be too scared."
    R "I'm sorry, but I have to follow Mom to make sure she's safe. She's my responsibility now."
    R "You'll be safe if you lock the door."
    R "And if anything happens, just call our new friends at the FBI."
    scene bg SleepBlack
    pause 2.5
    scene bg StreetNight
    with fade
    G "Hey, Boss?"
    J "What is it?"
    G "There's some twerp following us on a little scooter."
    M "Oh, no! That's probably my son!"
    G "Do you want me to lose him?"
    M "Oh, please do! I don't want him to see where you're making me work!"
    J "No! Let him follow us. I want the little bastard to know what happens to his mom when they don't pay us what they owes us."
    M "No! Please!"
    J "Listen! You don't get to make any demands!{p}You're lucky I don't turn around and have my driver run him over."
    J "So just sit there quietly and prepare yourself mentally for what it's going to take to earn the rest of what you owe me."
    J "You had better be as good at this job as you say you are, you've got a lot of money you have to make tonight!"
    scene bg SleepBlack
    pause 2
    scene bg ClubEntrance01
    with fade
    M "Well, I hope you're happy!?!"
    M "He's followed us all the way down the street and is watching us go in right now!"
    M "I can only thank God that he is too young to be let into a place like this."
    MT "{i}I'll just tell him I'm serving drinks.... or something like that.... {/i}"
    J "Yeah, yeah.... give me a break and just go get ready, will yah?"
    scene bg ClubEntrance02
    with dissolve
    J "If the kid wants to come in, go ahead and let 'im."
    J "He can have a look around and see if he finds anything interesting."
    G "Ok, Boss!"
    scene bg SleepBlack
    pause 2
    scene bg WalkingBar
    with fade
    play music ClubMusic
    RT "{i}So this place is some kind of bar? The guy at the door welcomed me in without checking my ID.{/i}"
    RT "{i}Nice!.... I guess I just look like I'm over 21 now!{/i}"
    RT "{i}So I wonder if Mom will be serving drinks or something.{/i}"
    scene bg WalkingCasino
    with fade
    RT "{i}Well, she's not by the bar, I wonder if she's serving the people in the casino?{/i}"
    RT "{i}Maybe they have her working a blackjack table or something.{/i}"
    VOM "Next up on stage we have a beautiful dancer here for her debut performance at the club."
    VOM "A hot housewife and teasing teacher, will make you want to misbehave to have her paddle your bum with her yardstick."
    VOM "Come and show her how bad you want to be the teacher's pet!"
    RT "{i}A teacher! What the hell! Are they talking about Mom!?! I've got to find out where that stage is.{/i}"
    scene bg StripPeek01
    with fade
    RT "{i}OH.... mY.... gOD!!!{/i}"
    RT "{i}It's Mom!{/i}"
    RT "{i}On a stripper pole!{/i}"
    RT "{i}Jeeze! What in the hell should I do?{/i}"
    $ sawmomstripping = True
    $ timeofdaycounter = 5
    menu:
        "Stay and Watch":
            $ persistent.gal_mom_1 = True
            scene bg StripperPole01
            with fade
            RT "{i}This is soooo wrong!.... {p}But I've got to know if she even knows what she's doing.... {p}How would she know how to work a stripper pole?{/i}"
            RT "{i}The look in her eyes is at least pretty confident.{/i}"
            MT "{i}Thank God they gave me free alcohol!.... It really takes the edge off!{/i}"
            MT "{i}And thank God my husband and kids don't know what I'm doing right now!{/i}"
            MT "{i}Oh my God! Oh my God! Oh my God! This can't really be happening!{/i}"
            MT "{i}How did I get into this situation?!.... {p}And I have to put a fucking smile on my face and pretend I'm having fun if I'm going to make any money!{/i}"
            scene bg StripperPole02
            with dissolve
            RT "{i}Oh, wow! She's taking off her shirt! I guess this is going to be more than just a sexy dance!{/i}"
            RT "{i}What is wrong with me? Why can't I look away?{/i}"
            MT "{i}Oh.... I am a terrible person. I thought I put this kind of thing behind me when I got married!{/i}"
            MT "{i}I never thought I'd be on a pole again.{/i}"
            MT "{i}I am a terrible wife and mother!{/i}"
            MT "{i}Oh thank God they can't see me now!{/i}"
            scene bg StripperPole03
            with dissolve
            RT "{i}Oh, shit! I can see her panties.{p}Oh.... they're practically see through! Unnnhhhh.... {/i}"
            RT "{i}Noo!.... I'm getting a hardon watching my own mother!.... I've got some serious problems....{/i}"
            MT "{i}Oh, God! Why me? What did I do wrong to end up like this? Get me out of this situation, and I'll be the most pure and chaste woman there is! I'll leave my husband and become a nun!{/i}"
            scene bg StripperPole04
            with dissolve
            RT "{i}Just look at that ass! It really is amazing that she's able to stay in such good shape.{/i}"
            RT "{i}All that yoga is paying off.... Anyone would appreciate an ass like that! Even if it is their own mother's.{/i}"
            MT "{i}Outside I'm smiling and happy, but I've never felt so down and depressed.{/i}"
            scene bg StripperPole05
            with dissolve
            RT "{i}Ok.... now her boobs are out!.... I can't believe this is happening.{p}Is this going to damage me psychologically? Should I keep watching?{/i}"
            menu:
                "Keep Watching":
                    scene bg StripperPole05
                    RT "{i}I'll take the psychological damage! It's not everyday you get in a situation like this. I'll deal with the consequences later.{/i}"
                    MT "{i}Ok, I can't let myself get so down! This isn't my fault.{/i}"
                    MT "{i}I can't let the consequences of my husband's actions make me feel so bad about myself. Stripping doesn't make me a bad person! I used to know lots of good people who were strippers.{/i}"
                    scene bg CreepShot01
                    with fade
                    RT "{i}I've got to save this moment forever.{/i}"
                    RT "{i}Hopefully the FBI isn't still monitoring my computer and phone, because this image will upload automatically to my computer.{/i}"
                    RT "{i}I can't wait to check it out later.{/i}"
                    scene bg PeekJack01
                    with dissolve
                    RT "{i}Oh, wow! My cock could cut diamonds right now!{/i}"
                    RT "{i}I've got to give myself some relief!{/i}"
                    RT "{i}Oh, this is sooo wrong. But I think that's why it's sooo hot!{/i}"
                    RT "{i}I've never felt this horny in my life!{/i}"
                    scene ClubStripVideo01
                    with fade
                    $ renpy.pause ()
                    scene SidClubVideo03
                    with fade
                    $ renpy.pause ()
                    scene bg StripperPole06
                    with fade
                    RT "{i}Ohhhh.... I'm not going to last much longer!{/i}"
                    MT "{i}Ok, [mom_name], pull yourself together. This isn't so bad.{/i}"
                    MT "{i}Just remember what those mommy blog podcasts taught you.{/i}"
                    MT "{i}I can't always control the situation, but I can always control how I react to it!{/i}"
                    scene bg CreepShot02
                    with fade
                    RT "{i}Oh, shit! I've got to get a picture of that amazing ass!{/i}"
                    RT "{i}Where did she learn to move like that!{/i}"
                    RT "{i}She looks and moves just like a pornstar!{/i}"
                    scene ClubStripVideo02
                    with fade
                    $ renpy.pause ()
                    scene SidClubVideo03
                    with fade
                    $ renpy.pause ()
                    scene bg StripperPole07
                    MT "{i}This is actually pretty exhilarating!{/i}"
                    MT "{i}Nobody but my husband has seen my tits since we were married.{/i}"
                    MT "{i}And these men seem to appreciate them more than my husband does.{/i}"
                    MT "{i}They keep throwing me money. I'll bet I'm close to making the $500 I need.{/i}"
                    MT "{i}This beats a lot of other ways of making money.{/i}"
                    MT "{i}Oh, God! Am I actually enjoying this? I think I'm starting to get wet!{/i}"
                    "{i}{b}\"Mom's Libido +5\"{/b}{/i}"
                    $ momlibido += 5
                    scene SidClubVideo03
                    with fade
                    RT "{i}Oh, shit! Here I CUMMMM!!{/i}"
                    scene bg JackoffClub05 with Dissolve(0.5)
                    $ renpy.pause (0.2, hard=True)
                    scene bg JackoffClub06 with Dissolve(0.5)
                    $ renpy.pause (0.2, hard=True)
                    RT "{i}NNNNyyyyhhhhhaaaaa.... !!{/i}"
                    scene bg JackoffClub07 with Dissolve(0.5)
                    with vpunch
                    with hpunch
                    scene bg JackoffClub08 with Dissolve(0.5)
                    $ renpy.pause (0.8, hard=True)
                    "..."
                    scene bg PeekCaught01
                    with fade
                    RT "{i}Oh no, good feelings gone, what have I done?!{/i}"
                    RT "{i}I am such a fucking pervert! How could I do this watching my own mother!{/i}"
                    RT "{i}This might really have messed me up.{/i}"
                    scene bg StripCaught
                    with fade
                    MT "{i}OH MY GOD!! Is that [ryan] peeking around the corner?!!{/i}"
                    MT "{i}Oh, no.... he looks so ashamed of me.{/i}"
                    "{i}{b}\"Mom's Libido -3\"{/b}{/i}"
                    "{i}{b}\"Mom's Affection -5\"{/b}{/i}"
                    "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                    $ momlibido -= 3
                    $ momaffection -= 5
                    $ momsubmission += 1
                    scene bg PeekCaught02
                    with fade
                    RT "{i}OH shit!{/i}"
                    RT "{i}She saw me!{/i}"
                    RT "{i}I hope she doesn't realize what I just did!{/i}"
                    RT "{i}I have to get out of here right now!{/i}"
                    play music Honey
                    jump citymap
                "Go home":
                    scene bg FamilyPhotoAdjusted
                    with fade
                    "You picked a boring option! What, you didn't want to take any risks?"
                    "You were able to make enough deliveries to keep making the payments."
                    "Your dad soon got out of jail and took back over as man of the house and emotionally abusive asshole."
                    "Everything went back to the way it was, except that you can't get these images out of your head."
                    scene bg StripperPole01 with Dissolve(0.5)
                    $ renpy.pause (0.5, hard=True)
                    scene bg StripperPole02 with Dissolve(0.5)
                    $ renpy.pause (0.5, hard=True)
                    scene bg StripperPole03 with Dissolve(0.5)
                    $ renpy.pause (0.5, hard=True)
                    scene bg StripperPole04 with Dissolve(0.5)
                    $ renpy.pause (0.5, hard=True)
                    scene bg StripperPole05 with Dissolve(0.5)
                    $ renpy.pause (0.5, hard=True)
                    scene bg FamilyPhotoAdjusted
                    with fade
                    "And now you can't help but get a hard-on every time your mom bends over."
                    scene bg SleepBlack
                    with fade
                    "Game Over"
                    "You might want to roll back now."
                    "Seriously, one more click and you'll be back to the game menu."
                    return
        "Go home":
            scene bg FamilyPhotoAdjusted
            with fade
            "You picked the most boring option! What, you didn't want to take any risks?"
            "You were able to make enough deliveries to keep making the payments."
            "Your dad soon got out of jail and took back over as man of the house and emotionally abusive asshole."
            "You went on to live a completely normal, unremarkable life."
            "You married a normal boring girl."
            "Your love life is almost non-existant, except for birthdays and anniversaries, the only action you get is from your hand while looking at a computer."
            scene bg SleepBlack
            with fade
            "Game Over"
            "You might want to roll back now."
            "Seriously, one more click and you'll be back to the game menu."
            return

label collectingpayment:
    if finished_wr_shoot and sidney_spy == False:
        jump sidney_search
    if jr_watched:
        jump reward_for_payment
    else:
        scene bg LaurenPonieTV
        with fade
        RT "{i}Looks like Lauren's watching her ponies show again.{/i}"
        "DING DONG"
        RT "{i}That's the doorbell. I'm pretty sure I know who that is.{/i}"
        menu:
            "Go answer the door":
                scene bg FrontDoor01
                with fade
                J "Hello little boy, is your mom at home?"
                RT "{i}Little boy, what an asshole!{/i}"
                R "Just a second."
                R "Hey Mom, there's some strange men at the door for you!"
                scene bg FrontDoor02
                with dissolve
                R "Wow, Mom! You look great!"
                M "Please, [ryan].... not now."
                $ timeofdaycounter += 1
                M "Were you able to get enough money together to pay them off this week?"
                menu:
                    "Yes" if money >= 1000:
                        R "Of course, Mom, did you really doubt me?"
                        "{i}\"Money -$1,000\"{/i}"
                        $ money -= 1000
                        $ loyaltycounter += 1
                        scene bg FrontDoor03
                        with dissolve
                        play music SexMusic
                        M "Oh, my little guy!"
                        M "Joey, thanks for dropping by, and I'm sure we'll see you next week!"
                        J "Well, I'll admit I'm a little disappointed. I mean don't get me wrong, it's admirable that you were able to pay your debt,"
                        J "But I enjoy your company more than I enjoy the money."
                        J "We'll see you next week."
                        scene bg FrontDoor06
                        with dissolve
                        M "Oh, thank you! Thank you! Thank you!!"
                        "{i}{b}\"Mom's Affection +10\"{/b}{/i}"
                        "{i}{b}\"Mom's Anger =0\"{/b}{/i}"
                        $ momaffection += 10
                        M "I am so relieved I don't have to go shake my ass for them tonight!"
                        scene bg FrontDoor07
                        with fade
                        RT "{i}Oh, but it's such a firm ass!{/i}"
                        scene bg FrontDoor10
                        with fade
                        RT "{i}And these perfect milky white breasts right in my face!{/i}"
                        RT "{i}I'm so glad I could make her feel so happy.{/i}"
                        scene bg FrontDoor08
                        with fade
                        RT "{i}And this hug is making me so happy!{/i}"
                        RT "..."
                        RT "{i}Maybe a little bit too happy!{/i}"
                        RT "{i}Oh, no.... stay down.... stay down.... stay down!.... {/i}"
                        scene bg FrontDoor09
                        with dissolve
                        RT "{i}Shit!.... {/i}"
                        RT "{i}She's going to notice any moment.... {/i}"
                        MT "{i}Oh my God! Is that what I think it is?{/i}"
                        RT "{i}Aaahhhh.... what should I do?{/i}"
                        scene bg FrontDoor11
                        with fade
                        M "Ouch, honey! Why did you drop me?"
                        R "Sorry, Mom! I've got to run!"
                        R "It's an emergency! I think I've got diarrhea!"
                        MT "{i}Diarrhea my bruised ass!{/i}"
                        MT "{i}My little pervert boy had a hardon for me.{/i}"
                        MT "{i}Shit.... I guess it was my fault for pressing my body against him like that.{/i}"
                        MT "{i}Probably perfectly normal for boys his age with raging hormones.{/i}"
                        MT "{i}But it makes me happy that I can still do that to boys his age.{/i}"
                        "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                        $ momlibido += 1
                        play music Honey
                        jump lounge
                    "No (lie)" if money >= 1000:
                        $ liedaboutmoney = True
                        $ loyaltycounter = 0
                        jump momdissapointed
                    "No" if money <= 999:
                        $ loyaltycounter = 0
                        jump momdissapointed

label momdissapointed:
    scene bg FrontDoor04
    with dissolve
    R "Sorry, Mom! I wasn't able to get enough money together this week."
    M "Oh sweety, don't worry about it. It was just too much to ask of you."
    RT "{i}Oh no! I feel like a piece of shit! Look how sad I've made her.{/i}"
    "{i}{b}\"Mom's Affection -5\"{/b}{/i}"
    $ momaffection -= 5
    $ momatclub = True
    $ clubcounter += 1
    scene bg FrontDoor05
    with dissolve
    RT "{i}There she goes off to the club.{/i}"
    RT "{i}I wonder if I should go make sure she is ok again.{/i}"
    scene bg CityMapNight
    with fade
    $ screen_on = "citymapmapnight"
    call screen citymapmapnight

label nightclubbing:
    if clubcounter >= 4 and forcedntrevents == 0:
        jump ntrclub
    else:
        scene bg WalkingBar
        with fade
        play music ClubMusic
        RT "{i}I think I remember my way to the strip pole.... {/i}"
        scene bg WalkingCasino
        with fade
        RT "{i}Past the bar, through the casino, and Bingo!{/i}"
        scene bg StripPeek01
        with fade
        RT "{i}Noish! I haven't missed anything yet!{/i}"
        RT "{i}Ehh.... she's wearing the same outfit as last time. They should have her do different outfits every week or something.{/i}"
        RT "{i}Still, I'm pretty damn hot for teacher!{/i}"
        scene bg StripperPole01
        with fade
        RT "{i}Ok, I've just got to be extra careful this time! It will be pretty hard to explain to her what I'm doing here, now that she knows, that I know, what she's doing here.{/i}"
        RT "{i}The look in her eyes is at least pretty confident.{/i}"
        MT "{i}The alchohol is kicking in already, I'm feeling much more loose!{/i}"
        MT "{i}This is so much easier than the first time.{/i}"
        scene bg StripperPole02
        with dissolve
        MT "{i}I still can't believe my son snuck in here and saw me stripping.{/i}"
        scene bg StripperPole03
        with dissolve
        MT "{i}I hope that didn't traumatize him too much!{/i}"
        scene bg StripperPole04
        with dissolve
        MT "{i}Actually, if I remember right, he said I looked amazing!{/i}"
        scene bg StripperPole05
        with dissolve
        MT "{i}He really is such a sweet boy. Maybe a little perverted, but that probably is just because he's got raging hormones and is living in a house full of girls.{/i}"
        scene bg PeekJack01
        with dissolve
        RT "{i}Oh, wow! My cock could cut diamonds right now!{/i}"
        RT "{i}I've got to give myself some relief!{/i}"
        RT "{i}Oh, this is sooo wrong. But I think that's why it's sooo hot!{/i}"
        RT "{i}I feel bad for whoever has to clean up after me.{/i}"
        scene ClubStripVideo01
        with fade
        $ renpy.pause ()
        scene SidClubVideo03
        with fade
        $ renpy.pause ()
        scene bg StripperPole06
        with fade
        MT "{i}I shouldn't be thinking about my own son so much while I'm up here shaking my ass!{/i}"
        MT "{i}Yet for some reason thinking of him watching me strip in public excites me just a bit.{/i}"
        "{i}{b}\"Mom's Libido +3\"{/b}{/i}"
        $ momlibido += 3
        MT "{i}I've got to be careful, or this pole will get too wet and slippery for the next girl.{/i}"
        scene ClubStripVideo02
        with fade
        $ renpy.pause ()
        scene SidClubVideo03
        with fade
        $ renpy.pause ()
        if liedaboutmoney == True:
            while caughtattheclubagain01 == False:
                scene bg StripperPole07
                with fade
                MT "{i}This is actually pretty exhilarating!{/i}"
                MT "{i}Nobody but my husband has seen my tits since we were married. Well, now just my own son and a bunch of random men.{/i}"
                MT "{i}And they seem to appreciate them more than my husband does.{/i}"
                MT "{i}They keep throwing me money. I'll bet I'm close to making the $1000 I need.{/i}"
                MT "{i}This beats a lot of other ways of making money.{/i}"
                MT "{i}Oh, God! Am I actually enjoying this. I think I'm getting really wet!{/i}"
                $ caughtattheclubagain01 = True
                scene bg StripCaught
                with fade
                MT "{i}OH MY GOD!! Is my own son peeking around the corner again?!!{/i}"
                MT "{i}Oh no! I really have fucked him up!{/i}"
                "{i}{b}\"Mom's Libido -3\"{/b}{/i}"
                "{i}{b}\"Mom's Affection -5\"{/b}{/i}"
                "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                $ momlibido -= 3
                $ momaffection -= 5
                $ momsubmission += 1
                scene bg PeekCaught02
                with fade
                RT "{i}OH shit!{/i}"
                RT "{i}She saw me!{/i}"
                RT "{i}I need to get my dick back in my pants!{/i}"
                RT "{i}Now careful not to zip him up!{/i}"
                scene bg StripCaught02
                with dissolve
                RT "{i}Shit!.... She's coming over here!{/i}"
                RT "{i}Shit, shit, shit!.... What am I going to say?{/i}"
                scene bg StripCaught03
                with dissolve
                M "[ryan]! What the hell are you doing here again!"
                R "I.... I.... I..."
                scene bg StripCaught04
                with dissolve
                M "[ryan]?.... [ryan]!"
                M "Eyes up here!"
                scene bg StripCaught05
                with dissolve
                R "Sorry, it's just you're naked, and it's really distracting."
                M "Well, do I need to go get some clothes on?"
                R "No!.... I mean.... only if you.... want to."
                M "HA!.... I knew it."
                R "Knew what?"
                scene bg StripCaught03
                with dissolve
                M "You're a little lying pervert!"
                "{i}{b}\"Mom's Anger +10\"{/b}{/i}"
                $ momanger += 10
                R "What?!..."
                M "Did you really not have enough money to pay off our weekly Mafia debt?"
                R "What are you saying?"
                M "I'm saying that I'm beginning to suspect that even if you had the money, you wouldn't have given it to the DeCapos bacause you wanted to come here and stare at your mom naked!"
                R "Oh my God! Mom!..."
                scene bg StripCaught04
                with dissolve
                R "How could you even say such a thing!"
                M "[ryan]! Your eyes are wandering again! Look up here!"
                scene bg StripCaught03
                with dissolve
                R "What was I saying?"
                M "You were trying to convince me that you wouldn't fail to make a payment, just so you can stare at your mom's tits!"
                M "And not very convincingly!"
                R "Mom.... I'm so offended..."
                R "I'll admit they are distracting when you're standing right in front of me with them on full display."
                R "But I'm only here with honorable intentions."
                M "Honorable? That's hard to believe when You're pitching a tent the size of a horse!"
                R "You think I'm that big?..."
                R "I mean compared with other men you've seen?"
                M "[ryan].... that is besides the point! And how many do you think I've seen?!!"
                R "Right.... well.... It's..."
                R "Anyways, I'm not hard because of you!"
                R "I mean you're beautiful and all.... and if you weren't my mom..."
                M "[ryan]!"
                R "Well.... what I'm trying to say is that I'm just excited by the situation.... I mean, I'm in a strip club! I've had a boner since I first started thinking about coming in here."
                R "It's not because I was watching you."
                scene bg StripCaught05
                with dissolve
                M "Is that right?"
                R "I'm just here to keep you safe."
                M "Ha! You're here to keep me safe?"
                R "Well, yeah.... to protect you."
                R "I mean.... this is a rough side of town.... there are men of questionable motives here."
                R "What if someone tries to grab you or something?"
                scene bg StripCaught03
                with dissolve
                M "[ryan]! That's why they have bouncers!"
                M "Joey gives me an escort both here and back home again."
                M "I'm perfectly safe here without you!"
                R "Hmmm.... well, I guess I didn't think about that."
                M "Obviously not!"
                R "Sorry.... I'm just trying to do what Dad told me to do."
                M "Oh, did he tell you to perv out on your mom while he's gone?"
                R "No!, just.... he told me to keep my family safe."
                M "Well, I'm perfectly safe, so just.... just.... get your ass home and keep your mouth shut about what I do here."
                M "And just to make it clear! This.... this right here.... this isn't normal!.... Sons aren't supposed to see so much skin from their moms!"
                M "This isn't the kind of example I want to set for your sisters."
                scene bg StripCaught05
                with dissolve
                RT "{i}Hmmm.... that's not a bad idea. Maybe they would be a little less prudish if they saw what Mom does on the weekends.{/i}"
                MT "{i}Did he really come here with good intentions?{/i}"
                MT "{i}If he did, I really feel kind of bad for yelling at him.{/i}"
                MT "{i}But if he didn't, I might really have a growing problem on my hands.{/i}"
                RT "{i}Well, I guess I should get one more peek for the road.{/i}"
                scene bg StripCaught04
                with dissolve
                M "[ryan]! It's time for you to leave!"
                R "Of course, I'm leaving right now."
                R "I love you, mom!"
                M "I know.... I'll see you tomorrow."
                $ sawmomstripping = True
                play music Honey
                scene bg CityMapNight
                with fade
                $ screen_on = "citymapmapnight"
                call screen citymapmapnight
            if liedaboutmoney == True:
                scene bg StripperPole07
                with fade
                MT "{i}This is actually pretty exhilarating!{/i}"
                MT "{i}Nobody but my husband has seen my tits since we were married. Well, now just my own son and a bunch of random men.{/i}"
                MT "{i}And they seem to appreciate them more than my husband does.{/i}"
                MT "{i}They keep throwing me money. I'll bet I'm close to making the $1000 I need.{/i}"
                MT "{i}This beats a lot of other ways of making money.{/i}"
                MT "{i}Oh, God! Am I actually enjoying this. I think I'm getting really wet!{/i}"
                scene SidClubVideo03
                with fade
                RT "{i}Oh, shit! Here I CUMMMM!!{/i}"
                scene bg JackoffClub05 with Dissolve(0.5)
                $ renpy.pause (0.2)
                scene bg JackoffClub06 with Dissolve(0.5)
                $ renpy.pause (0.2)
                RT "{i}NNNNyyyyhhhhhaaaaa.... !!{/i}"
                scene bg JackoffClub07 with Dissolve(0.5)
                with vpunch
                with hpunch
                scene bg JackoffClub08 with Dissolve(0.5)
                $ renpy.pause (0.8, hard=True)
                "..."
                scene bg PeekCaught01
                with fade
                RT "{i}And queue the post-coital regret!{/i}"
                RT "{i}I am such a fucking pervert! How could I do this watching my own mother!{/i}"
                RT "{i}I'm out of control.... maybe I should get help?.... Nah this is just harmless fun.{/i}"
                RT "{i}Now I better get out of here before she notices me.{/i}"
                $ sawmomstripping = True
                play music Honey
                scene bg CityMapNight
                with fade
                $ screen_on = "citymapmapnight"
                call screen citymapmapnight
        else:
            scene bg StripperPole07
            with fade
            MT "{i}This is actually pretty exhilarating!{/i}"
            MT "{i}Nobody but my husband has seen my tits since we were married. Well, now just my own son and a bunch of random men.{/i}"
            MT "{i}And they seem to appreciate them more than my husband does.{/i}"
            MT "{i}They keep throwing me money. I'll bet I'm close to making the $1000 I need.{/i}"
            MT "{i}This beats a lot of other ways of making money.{/i}"
            MT "{i}Oh, God! Am I actually enjoying this. I think I'm getting really wet!{/i}"
            scene SidClubVideo03
            with fade
            RT "{i}Oh, shit! Here I CUMMMM!!{/i}"
            scene bg JackoffClub05 with Dissolve(0.5)
            $ renpy.pause (0.2)
            scene bg JackoffClub06 with Dissolve(0.5)
            $ renpy.pause (0.2)
            RT "{i}NNNNyyyyhhhhhaaaaa.... !!{/i}"
            scene bg JackoffClub07 with Dissolve(0.5)
            with vpunch
            with hpunch
            scene bg JackoffClub08 with Dissolve(0.5)
            $ renpy.pause (0.8, hard=True)
            "..."
            scene bg PeekCaught01
            with fade
            RT "{i}Good feelings gone. What's wrong with me!{/i}"
            RT "{i}I am such a fucking pervert! How could I do this watching my own mother!{/i}"
            RT "{i}I'm out of control.... maybe I should get help?.... Nah this is just harmless fun.{/i}"
            RT "{i}Now I better get out of here before she notices me.{/i}"
            $ sawmomstripping = True
            play music Honey
            scene bg CityMapNight
            with fade
            $ screen_on = "citymapmapnight"
            call screen citymapmapnight

label endgame:
    return
