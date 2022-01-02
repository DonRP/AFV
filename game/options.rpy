## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("A Family Venture")

define config.layers = [ 'master', 'transient', 'screens', 'over_screens', 'overlay' ]



## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

## Remove the style from screens.rpy by finding:
## if gui.show_name:
##
##         vbox:
##             text "[config.name!t]":
##                 style "main_menu_title"
##
##             text "[config.version]":
##                 style "xmas_text"       #<== This is for Xmas style
##                 style "main_menu_version" #<== This is for normal style

define config.version = "0.07_extended_supporter" #{=xmas_text}


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "AFamilyVenture"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define audio.Honey = "music/YanTerrienRoseBaba.mp3"
define audio.SexMusic = "music/LeeRosevereWaitingFortheMomentThatNeverComes.mp3"
define audio.ClubMusic = "music/YshwaIwill.mp3"
define audio.Blow02 = "music/Blow02.mp3"
define audio.Blow03 = "music/Blow03.mp3"
define audio.Lauren01 = "music/Lauren01.mp3"
define audio.Mom02 = "music/Mom02.mp3"
define audio.Sidney01 = "music/Sidney01.mp3"
define audio.ClubGrind = "music/ClubGrind.mp3"
define audio.WeWishYou = "music/WeWishYou.mp3"
define audio.ChristmasRap = "music/ChristmasRap.mp3"
define audio.WizardingSchool = "music/WizardingSchool.wav"
define audio.Dance = "music/Dance.mp3"


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "music/MonplaisirBrotherhood.mp3"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "AFamilyVenture-1541518183"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("music", "all")
    build.archive("video", "all")
    build.archive("Patreon_extra", "all")
    build.archive("Spanish", "all")
    build.archive("Patch.07", "all")

    build.classify("game/Patreon_$5_Gallery/**.rpy", "Patreon_extra")
    build.classify("game/Patreon_$5_Gallery/**.rpyc", "Patreon_extra")
    build.classify("game/Patreon_$5_Gallery/Patreon IMG's/**.jpg", "Patreon_extra")
    build.classify("game/Patreon_$5_Gallery/Patreon IMG's/**.png", "Patreon_extra")
    build.classify("game/Patreon_$5_Gallery/Patreon IMG's/**.webp", "Patreon_extra")
##    build.classify("game/Patreon_$5_Gallery/Patreon IMG's/**.db", "Patreon_extra")

    build.classify("game/*.rpy", "scripts")
    build.classify("game/*.rpyc", "scripts")
#    build.classify("game/Xmas/*.rpy", "scripts")
    build.classify("game/images/interface_images/minigame/*.rpy", "scripts")
    build.classify("game/images/interface_images/minigame/*.rpyc", "scripts")
    build.classify("game/images/interface_images/nav_buttons/*.ttf", "scripts")
    build.classify("game/images/interface_images/blackjack/*.rpy", "scripts")
    build.classify("game/images/interface_images/blackjack/*.rpyc", "scripts")
    build.classify("game/images/interface_images/Roulette/*.rpy", "scripts")
    build.classify("game/images/interface_images/Roulette/*.rpyc", "scripts")
    build.classify("game/test/*.rpy", "scripts")
    build.classify("game/test/*.rpyc", "scripts")
    build.classify("game/test/func/*.rpy", "scripts")
    build.classify("game/test/func/*.rpyc", "scripts")

    build.classify("game/tl/spanish/*.rpy", "Spanish")
    build.classify("game/tl/spanish/*.rpyc", "Spanish")
    build.classify("game/tl/spanish/images/interface_images/minigame/*.rpy", "Spanish")
    build.classify("game/tl/spanish/images/interface_images/minigame/*.rpyc", "Spanish")
    build.classify("game/tl/spanish/images/interface_images/blackjack/*.rpy", "Spanish")
    build.classify("game/tl/spanish/images/interface_images/blackjack/*.rpyc", "Spanish")
    build.classify("game/tl/spanish/images/interface_images/Roulette/*.rpy", "Spanish")
    build.classify("game/tl/spanish/images/interface_images/Roulette/*.rpyc", "Spanish")
    build.classify("game/tl/spanish/Patreon_$5_Gallery/*.rpy", "Spanish")
    build.classify("game/tl/spanish/Patreon_$5_Gallery/*.rpyc", "Spanish")
    build.classify("game/tl/spanish/images/*.png", "Spanish")
    build.classify("game/tl/spanish/images/*.webp", "Spanish")
    build.classify("game/tl/spanish/images/interface_images/blackjack/*.png", "Spanish")
    build.classify("game/tl/spanish/images/interface_images/Roulette/*.png", "Spanish")
    build.classify("game/tl/spanish/gui/*.webp", "Spanish")


#    build.classify("game/images/**.jpg", "images")
#    build.classify("game/images/**.png", "images")
#    build.classify("game/gui/**.png", "images")
#    build.classify("game/gui/**.webp", "images")
#    build.classify("game/gui/bar/**.png", "images")
#    build.classify("game/gui/button/**.png", "images")
#    build.classify("game/gui/overlay/**.png", "images")
#    build.classify("game/gui/phone/**.png", "images")
#    build.classify("game/gui/phone/bar/**.png", "images")
#    build.classify("game/gui/phone/button/**.png", "images")
#    build.classify("game/gui/phone/overlay/**.png", "images")
#    build.classify("game/gui/phone/scrollbar/**.png", "images")
#    build.classify("game/gui/phone/slider**.png", "images")
#    build.classify("game/gui/scrollbar/**.png", "images")
#    build.classify("game/gui/slider/**.png", "images")
#    build.classify("game/images/interface_images/**.webp", "images")
#    build.classify("game/images/interface_images/**.png", "images")
#    build.classify("game/images/interface_images/booble_images/**.jpg", "images")
#    build.classify("game/images/interface_images/cosplay_gallery_images/**.png", "images")
#    build.classify("game/images/interface_images/cosplay_gallery_images/**.psd", "images")
#    build.classify("game/images/interface_images/cosplay_gallery_images/old/**.png", "images")
#    build.classify("game/images/interface_images/cosplay_gallery_images/supporters_img/**.png", "images")
#    build.classify("game/images/interface_images/credits_images/**.png", "images")
#    build.classify("game/images/interface_images/credits_images/**.psd", "images")
#    build.classify("game/images/interface_images/gallery_images/**.png", "images")
#    build.classify("game/images/interface_images/inventory_images/**.png", "images")
#    build.classify("game/images/interface_images/nav_buttons/**.png", "images")
#    build.classify("game/images/interface_images/pc_gallery_images/**.png", "images")
#    build.classify("game/images/interface_images/pc_gallery_images/**.psd", "images")
#    build.classify("game/images/interface_images/phone_screen_images/**.png", "images")
#    build.classify("game/images/interface_images/points_images/**.webp", "images")
#    build.classify("game/images/interface_images/shopping_gallery_images/**.png", "images")

    build.classify("game/images/LaurenEvents115.webp", "Patch.07")
    build.classify("game/images/LaurenEvents116.webp", "Patch.07")
    build.classify("game/images/NSidneyKitchen06.webp", "Patch.07")
    build.classify("game/images/NSidneyKitchen10.webp", "Patch.07")
    build.classify("game/images/NSidneyKitchen11.webp", "Patch.07")
    build.classify("game/images/NSidneyKitchen12.webp", "Patch.07")
    build.classify("game/images/NSidneyKitchen13.webp", "Patch.07")
    build.classify("game/images/NSidneyKitchen14.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge01.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge02.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge03.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge04.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge05.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge06.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge07.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge08.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge09.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge10.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge11.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge12.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge13.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge14.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge15.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge16.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLounge17.webp", "Patch.07")
    build.classify("game/images/FuckLaurenLounge01.webp", "Patch.07")
    build.classify("game/images/FuckLaurenLounge02.webp", "Patch.07")
    build.classify("game/images/FuckLaurenLounge03.webp", "Patch.07")
    build.classify("game/images/FuckLaurenLounge04.webp", "Patch.07")
    build.classify("game/images/FuckLaurenLounge05.webp", "Patch.07")
    build.classify("game/images/FuckLaurenLounge06.webp", "Patch.07")
    build.classify("game/images/FuckLaurenLounge07.webp", "Patch.07")
    build.classify("game/images/FuckLaurenLounge08.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot01.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot02.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot03.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot04.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot05.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot06.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot07.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot08.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot09.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot10.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot11.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot12.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot13.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot14.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot15.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot16.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot17.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot18.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot19.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot20.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot21.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot22.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot23.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot24.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot25.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot26.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot27.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot28.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot29.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot30.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot31.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot32.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot33.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot34.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot35.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot36.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot37.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot38.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot39.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot40.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShoot41.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex01.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex02.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex03.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex04.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex05.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex06.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex07.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex08.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex09.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex10.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex11.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex12.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex13.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex14.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex15.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex16.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex17.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex18.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex19.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex20.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex21.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex22.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex23.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex24.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex25.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex26.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex27.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex28.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex29.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex30.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex31.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex32.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex33.webp", "Patch.07")
    build.classify("game/images/LaurenBathSex34.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLoungeVideo01F01.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLoungeVideo02F01.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLoungeVideo03F01.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLoungeVideo04F01.webp", "Patch.07")
    build.classify("game/images/NTRLaurenLoungeVideo05F01.webp", "Patch.07")
    build.classify("game/images/FuckLaurenLoungeVideo01F01.webp", "Patch.07")
    build.classify("game/images/FuckLaurenLoungeVideo02F01.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShootVideo01F01.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShootVideo02F01.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShootVideo03F01.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShootVideo04F01.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShootVideo05F01.webp", "Patch.07")
    build.classify("game/images/AfterLaurenShootVideo06F01.webp", "Patch.07")
    build.classify("game/images/LaurenBathSexVideo01F01.webp", "Patch.07")
    build.classify("game/images/LaurenBathSexVideo02F01.webp", "Patch.07")
    build.classify("game/images/LaurenBathSexVideo03F01.webp", "Patch.07")

    build.classify("game/music/Piper01.wav", "Patch.07")
    build.classify("game/music/Piper02.wav", "Patch.07")
    build.classify("game/music/Gag.wav", "Patch.07")
    build.classify("game/music/Knock.mp3", "Patch.07")

    build.classify("game/video/NTRLaurenLoungeVideo01.webm", "Patch.07")
    build.classify("game/video/NTRLaurenLoungeVideo02.webm", "Patch.07")
    build.classify("game/video/NTRLaurenLoungeVideo03.webm", "Patch.07")
    build.classify("game/video/NTRLaurenLoungeVideo04.webm", "Patch.07")
    build.classify("game/video/NTRLaurenLoungeVideo05.webm", "Patch.07")
    build.classify("game/video/FuckLaurenLoungeVideo01.webm", "Patch.07")
    build.classify("game/video/FuckLaurenLoungeVideo02.webm", "Patch.07")
    build.classify("game/video/AfterLaurenShootVideo01.webm", "Patch.07")
    build.classify("game/video/AfterLaurenShootVideo02.webm", "Patch.07")
    build.classify("game/video/AfterLaurenShootVideo03.webm", "Patch.07")
    build.classify("game/video/AfterLaurenShootVideo04.webm", "Patch.07")
    build.classify("game/video/AfterLaurenShootVideo05.webm", "Patch.07")
    build.classify("game/video/AfterLaurenShootVideo06.webm", "Patch.07")
    build.classify("game/video/LaurenBathSexVideo01.webm", "Patch.07")
    build.classify("game/video/LaurenBathSexVideo02.webm", "Patch.07")
    build.classify("game/video/LaurenBathSexVideo03.webm", "Patch.07")



#    build.classify("game/**.mp3", "music")
#    build.classify("game/**.wav", "music")

#    build.classify("game/video/**.webm", "video")


    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## Set this to a string containing your Apple Developer ID Application to enable
## codesigning on the Mac. Be sure to change it to your own Apple-issued ID.

# define build.mac_identity = "Developer ID Application: Guy Shy (XHTE5H7Z42)"


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
init -1:
    python hide:
        config.developer = True
