define audio.Pop = "music/Pop.wav"
define audio.Twinkle = "music/Twinkle.wav"
define audio.MetalDoor = "music/MetalDoor.wav"
define audio.Fart = "music/Fart.wav"

define GP = Character(_("Ghost of XXX-mas Past"), color="AC0A1B", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define GCP = Character(_("Ghost of XXX-mas Present"), color="06740B", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define GF = Character(_("Ghost of XXX-mas Future"), color="09238E", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
#define WT = Character(_("Will Tylor"), color="9135D1", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])

define christmas_complete = False
define first_xmas_ntr = False
define second_xmas_ntr = False
define mom_first_xmas_fuck = False
define sidney_first_xmas_fuck = False
define lauren_first_xmas_fuck = False

init:

    image Christmas01 = Movie(play="video/ChristmasVid01.webm", start_image="images/ChristmasMovieStart01.webp")
    image Christmas02 = Movie(play="video/ChristmasVid02.webm", start_image="images/ChristmasMovieStart02.webp")
    image LChristmasMovie01 = Movie(play="video/LChristmasMovie01.webm", start_image="images/LChristmasMovie01Start.webp")
    image LChristmasMovie02 = Movie(play="video/LChristmasMovie02.webm", start_image="images/LChristmasMovie02Start.webp")
    image SChristmasMovie01 = Movie(play="video/SChristmasMovie01.webm", start_image="images/SChristmasMovie01Start.webp")
    image PreggyMovie01 = Movie(play="video/PreggyMovie01.webm", start_image="images/PreggyMovie01Start.webp")
    image PreggyMovie02 = Movie(play="video/PreggyMovie02.webm", start_image="images/PreggyMovie02Start.webp")
    image PreggyMovie03 = Movie(play="video/PreggyMovie03.webm", start_image="images/PreggyMovie03Start.webp")
    image bg SChristmasMovie01Start = "SChristmasMovie01Start.webp"
    image bg ChristmasIntro = "ChristmasIntro.webp"
    image bg ChristmasEvent01 = "ChristmasEvent01.webp"
    image bg ChristmasEvent02 = "ChristmasEvent02.webp"
    image bg ChristmasEvent03 = "ChristmasEvent03.webp"
    image bg ChristmasEvent04 = "ChristmasEvent04.webp"
    image bg ChristmasEvent05 = "ChristmasEvent05.webp"
    image bg ChristmasEvent06 = "ChristmasEvent06.webp"
    image bg ChristmasEvent07 = "ChristmasEvent07.webp"
    image bg ChristmasEvent08 = "ChristmasEvent08.webp"
    image bg ChristmasEvent09 = "ChristmasEvent09.webp"
    image bg ChristmasEvent10 = "ChristmasEvent10.webp"
    image bg ChristmasEvent11 = "ChristmasEvent11.webp"
    image bg ChristmasEvent12 = "ChristmasEvent12.webp"
    image bg ChristmasEvent13 = "ChristmasEvent13.webp"
    image bg ChristmasEvent14 = "ChristmasEvent14.webp"
    image bg ChristmasEvent15 = "ChristmasEvent15.webp"
    image bg ChristmasEvent16 = "ChristmasEvent16.webp"
    image bg ChristmasEvent17 = "ChristmasEvent17.webp"
    image bg ChristmasEvent18 = "ChristmasEvent18.webp"
    image bg ChristmasEvent19 = "ChristmasEvent19.webp"
    image bg ChristmasEvent20 = "ChristmasEvent20.webp"
    image bg ChristmasEvent21 = "ChristmasEvent21.webp"
    image bg ChristmasEvent22 = "ChristmasEvent22.webp"
    image bg ChristmasEvent23 = "ChristmasEvent23.webp"
    image bg ChristmasEvent24 = "ChristmasEvent24.webp"
    image bg ChristmasEvent25 = "ChristmasEvent25.webp"
    image bg ChristmasEvent26 = "ChristmasEvent26.webp"
    image bg ChristmasEvent27 = "ChristmasEvent27.webp"
    image bg ChristmasEvent28 = "ChristmasEvent28.webp"
    image bg ChristmasEvent29 = "ChristmasEvent29.webp"
    image bg ChristmasEvent30 = "ChristmasEvent30.webp"
    image bg ChristmasEvent31 = "ChristmasEvent31.webp"
    image bg ChristmasEvent32 = "ChristmasEvent32.webp"
    image bg ChristmasEvent33 = "ChristmasEvent33.webp"
    image bg ChristmasEvent34 = "ChristmasEvent34.webp"
    image bg ChristmasEvent35 = "ChristmasEvent35.webp"
    image bg ChristmasEvent36 = "ChristmasEvent36.webp"
    image bg ChristmasEvent37 = "ChristmasEvent37.webp"
    image bg ChristmasEvent38 = "ChristmasEvent38.webp"
    image bg ChristmasEvent39 = "ChristmasEvent39.webp"
    image bg ChristmasEvent40 = "ChristmasEvent40.webp"
    image bg ChristmasEvent41 = "ChristmasEvent41.webp"
    image bg ChristmasEvent42 = "ChristmasEvent42.webp"
    image bg ChristmasEvent43 = "ChristmasEvent43.webp"
    image bg ChristmasEvent44 = "ChristmasEvent44.webp"
    image bg ChristmasEvent45 = "ChristmasEvent45.webp"
    image bg ChristmasEvent46 = "ChristmasEvent46.webp"
    image bg ChristmasEvent47 = "ChristmasEvent47.webp"
    image bg ChristmasEvent48 = "ChristmasEvent48.webp"
    image bg ChristmasEvent49 = "ChristmasEvent49.webp"
    image bg ChristmasEvent50 = "ChristmasEvent50.webp"
    image bg ChristmasEvent51 = "ChristmasEvent51.webp"
    image bg ChristmasEvent52 = "ChristmasEvent52.webp"
    image bg ChristmasEvent53 = "ChristmasEvent53.webp"
    image bg ChristmasEvent54 = "ChristmasEvent54.webp"
    image bg ChristmasEvent55 = "ChristmasEvent55.webp"
    image bg ChristmasEvent56 = "ChristmasEvent56.webp"
    image bg ChristmasEvent57 = "ChristmasEvent57.webp"
    image bg ChristmasEvent58 = "ChristmasEvent58.webp"
    image bg ChristmasEvent59 = "ChristmasEvent59.webp"
    image bg ChristmasEvent60 = "ChristmasEvent60.webp"
    image bg ChristmasEvent61 = "ChristmasEvent61.webp"
    image bg ChristmasEvent62 = "ChristmasEvent62.webp"
    image bg ChristmasEvent63 = "ChristmasEvent63.webp"
    image bg ChristmasEvent64 = "ChristmasEvent64.webp"
    image bg ChristmasEvent65 = "ChristmasEvent65.webp"
    image bg ChristmasEvent66 = "ChristmasEvent66.webp"
    image bg ChristmasEvent67 = "ChristmasEvent67.webp"
    image bg ChristmasEvent68 = "ChristmasEvent68.webp"
    image bg ChristmasEvent69 = "ChristmasEvent69.webp"
    image bg ChristmasEvent70 = "ChristmasEvent70.webp"
    image bg LChristmas01 = "LChristmas01.webp"
    image bg LChristmas02 = "LChristmas02.webp"
    image bg LChristmas03 = "LChristmas03.webp"
    image bg LChristmas04 = "LChristmas04.webp"
    image bg LChristmas05 = "LChristmas05.webp"
    image bg LChristmas06 = "LChristmas06.webp"
    image bg LChristmas07 = "LChristmas07.webp"
    image bg LChristmas08 = "LChristmas08.webp"
    image bg LChristmas09 = "LChristmas09.webp"
    image bg LChristmas10 = "LChristmas10.webp"
    image bg LChristmas11 = "LChristmas11.webp"
    image bg LChristmas12 = "LChristmas12.webp"
    image bg LChristmas13 = "LChristmas13.webp"
    image bg LChristmas14 = "LChristmas14.webp"
    image bg LChristmas15 = "LChristmas15.webp"
    image bg LChristmas16 = "LChristmas16.webp"
    image bg LChristmas17 = "LChristmas17.webp"
    image bg LChristmas18 = "LChristmas18.webp"
    image bg LChristmas19 = "LChristmas19.webp"
    image bg LChristmas20 = "LChristmas20.webp"
    image bg LChristmas21 = "LChristmas21.webp"
    image bg LChristmas22 = "LChristmas22.webp"
    image bg LChristmas23 = "LChristmas23.webp"
    image bg LChristmas24 = "LChristmas24.webp"
    image bg LChristmas25 = "LChristmas25.webp"
    image bg LChristmas26 = "LChristmas26.webp"
    image bg LChristmas27 = "LChristmas27.webp"
    image bg LChristmas28 = "LChristmas28.webp"
    image bg LChristmas29 = "LChristmas29.webp"
    image bg LChristmas30 = "LChristmas30.webp"
    image bg LChristmas31 = "LChristmas31.webp"
    image bg LChristmas32 = "LChristmas32.webp"
    image bg LChristmas33 = "LChristmas33.webp"
    image bg LChristmas34 = "LChristmas34.webp"
    image bg LChristmas35 = "LChristmas35.webp"
    image bg LChristmas36 = "LChristmas36.webp"
    image bg LChristmas37 = "LChristmas37.webp"
    image bg LChristmas38 = "LChristmas38.webp"
    image bg LChristmas39 = "LChristmas39.webp"
    image bg LChristmas40 = "LChristmas40.webp"
    image bg LChristmas41 = "LChristmas41.webp"
    image bg LChristmas42 = "LChristmas42.webp"
    image bg LChristmas43 = "LChristmas43.webp"
    image bg LChristmas44 = "LChristmas44.webp"
    image bg LChristmas45 = "LChristmas45.webp"
    image bg LChristmas46 = "LChristmas46.webp"
    image bg LChristmas47 = "LChristmas47.webp"
    image bg LChristmas48 = "LChristmas48.webp"
    image bg LChristmas49 = "LChristmas49.webp"
    image bg LChristmas50 = "LChristmas50.webp"
    image bg LChristmas51 = "LChristmas51.webp"
    image bg LChristmas52 = "LChristmas52.webp"
    image bg LChristmas53 = "LChristmas53.webp"
    image bg LChristmas54 = "LChristmas54.webp"
    image bg LChristmas55 = "LChristmas55.webp"
    image bg LChristmas56 = "LChristmas56.webp"
    image bg LChristmas57 = "LChristmas57.webp"
    image bg LChristmas58 = "LChristmas58.webp"
    image bg LChristmas59 = "LChristmas59.webp"
    image bg LChristmas60 = "LChristmas60.webp"
    image bg SChristmas01 = "SChristmas01.webp"
    image bg SChristmas02 = "SChristmas02.webp"
    image bg SChristmas03 = "SChristmas03.webp"
    image bg SChristmas04 = "SChristmas04.webp"
    image bg SChristmas05 = "SChristmas05.webp"
    image bg SChristmas06 = "SChristmas06.webp"
    image bg SChristmas07 = "SChristmas07.webp"
    image bg SChristmas08 = "SChristmas08.webp"
    image bg SChristmas09 = "SChristmas09.webp"
    image bg SChristmas10 = "SChristmas10.webp"
    image bg SChristmas11 = "SChristmas11.webp"
    image bg SChristmas12 = "SChristmas12.webp"
    image bg SChristmas13 = "SChristmas13.webp"
    image bg SChristmas14 = "SChristmas14.webp"
    image bg SChristmas15 = "SChristmas15.webp"
    image bg SChristmas16 = "SChristmas16.webp"
    image bg SChristmas17 = "SChristmas17.webp"
    image bg SChristmas18 = "SChristmas18.webp"
    image bg SChristmas19 = "SChristmas19.webp"
    image bg SChristmas20 = "SChristmas20.webp"
    image bg SChristmas21 = "SChristmas21.webp"
    image bg SChristmas22 = "SChristmas22.webp"
    image bg SChristmas23 = "SChristmas23.webp"
    image bg SChristmas24 = "SChristmas24.webp"
    image bg SChristmas25 = "SChristmas25.webp"
    image bg SChristmas26 = "SChristmas26.webp"
    image bg SChristmas27 = "SChristmas27.webp"
    image bg SChristmas28 = "SChristmas28.webp"
    image bg SChristmas29 = "SChristmas29.webp"
    image bg SChristmas30 = "SChristmas30.webp"
    image bg SChristmas31 = "SChristmas31.webp"
    image bg SChristmas32 = "SChristmas32.webp"
    image bg SChristmas33 = "SChristmas33.webp"
    image bg SChristmas34 = "SChristmas34.webp"
    image bg SChristmas35 = "SChristmas35.webp"
    image bg SChristmas36 = "SChristmas36.webp"
    image bg SChristmas37 = "SChristmas37.webp"
    image bg SChristmas38 = "SChristmas38.webp"
    image bg SChristmas39 = "SChristmas39.webp"
    image bg SChristmas40 = "SChristmas40.webp"
    image bg SChristmas41 = "SChristmas41.webp"
    image bg SChristmas42 = "SChristmas42.webp"
    image bg SChristmas43 = "SChristmas43.webp"
    image bg Tutorial01 = "Tutorial01.webp"
    image bg Tutorial02 = "Tutorial02.webp"
    image bg Tutorial03 = "Tutorial03.webp"
    image bg Tutorial04 = "Tutorial04.webp"
    image bg Tutorial05 = "Tutorial05.webp"
    image bg Tutorial06 = "Tutorial06.webp"
    image bg Tutorial07 = "Tutorial07.webp"
    image bg Tutorial08 = "Tutorial08.webp"
    image bg Tutorial09 = "Tutorial09.webp"
    image bg Tutorial10 = "Tutorial10.webp"
    image bg Tutorial11 = "Tutorial11.webp"
    image bg Tutorial12 = "Tutorial12.webp"
    image bg Tutorial13 = "Tutorial13.webp"
    image bg Tutorial14 = "Tutorial14.webp"
    image bg Tutorial15 = "Tutorial15.webp"
    image bg Tutorial16 = "Tutorial16.webp"
    image bg Tutorial17 = "Tutorial17.webp"
    image bg Tutorial18 = "Tutorial18.webp"
    image bg Tutorial19 = "Tutorial19.webp"
    image bg Tutorial20 = "Tutorial20.webp"
    image bg Tutorial21 = "Tutorial21.webp"
    image bg Tutorial22 = "Tutorial22.webp"
    image bg Tutorial23 = "Tutorial23.webp"
    image bg Tutorial24 = "Tutorial24.webp"
    image bg Tutorial25 = "Tutorial25.webp"
    image bg Tutorial26 = "Tutorial26.webp"
    image bg Tutorial27 = "Tutorial27.webp"
    image bg Tutorial28 = "Tutorial28.webp"
    image bg Tutorial29 = "Tutorial29.webp"
    image bg Tutorial30 = "Tutorial30.webp"
    image bg Tutorial31 = "Tutorial31.webp"
    image bg Tutorial32 = "Tutorial32.webp"
    image bg Tutorial33 = "Tutorial33.webp"
    image bg Tutorial34 = "Tutorial34.webp"
    image bg Tutorial35 = "Tutorial35.webp"
    image bg Tutorial36 = "Tutorial36.webp"
    image bg Tutorial37 = "Tutorial37.webp"
    image bg Tutorial38 = "Tutorial38.webp"

#############  RYAN'S ROOM  ################################  RYAN'S ROOM  ######################################################  RYAN'S ROOM  #####################################################  RYAN'S ROOM  ###############################################################  RYAN'S ROOM  ############################################################  RYAN'S ROOM  ################################

label xmas_dream:
    scene bg SleepBlack
    with fade
    "Welcome to our Christmas event!  WARNING!!  This event has elements of NTR, that are completely avoidable!  Choices that lead to NTR content are clearly marked!"
    "Do not choose an NTR option if it offends you, only to complain about it later on some online forum!!"
    "This event also has pregnancy content."
    "Would you like to play the Christmas event at this time? (Choosing \"No\" will complete this event and make it so you can only watch it in the gallery menu.)"
    menu:
        "Yes":
            pass
        "No":
            $ persistent.gal_harem_2 = True
            $ christmas_complete = True
            jump sleep
    scene bg SleepBlack
    with fade
    play music WeWishYou
    scene bg ChristmasIntro
    with fade
    $ renpy.pause (5.5, hard=True)
    scene bg SleepBlack
    with fade
    "{i}A tribute to Charles Dickens and his timeless classic, \"A Christmas Carol.\"{/i}"
    "..."
    RT "{i}Thank God the Christmas break is coming! I'm so tired of school.{/i}"
    RT "{i}Now I'll have even more time to work on seducing the girls.{/i}"
    RT "{i}I've got to really work hard if I want to unwrap those beautiful boxes for the holidays.{/i}"
    RT "{i}And those are some great mental images to fall asleep to.... zzzzzz.... {/i}"
    RT "{i}zzzzzzz.... {/i}"
    "..."
    X "[ryan]..."
    X "Hey [ryan]..."
    scene bg BlurryWhite
    with fade
    scene bg SleepBlack
    with fade
    X "Wake up [ryan]!..."
    scene bg BlurryWhite
    with fade
    scene bg SleepBlack
    with fade
    X "Hey [ryan]!.... Wake up!"
    RT "{i}Huh.... what?....{/i}"
    scene bg ChristmasEvent01
    with fade
    scene bg SleepBlack
    with fade
    scene bg ChristmasEvent01
    with fade
    scene bg SleepBlack
    with fade
    scene bg ChristmasEvent02
    with fade
    RT "{i}What the hell?{/i}"
    RT "{i}What a weird dream! There's a tiny Mom on my chest{/i}"
    X "[ryan].... this isn't a dream.... and I'm not a tiny Mom"
    RT "{i}You have to be a dream.... you can read my thoughts....{/i}"
    X "[ryan].... I'm the ghost of Christmas past."
    R "What?.... Bullshit!.... Then why do you look like a half-naked version of my mom?"
    GP "Well.... I'm a ghost.... so my true form might have scared you to death."
    GP "I've been given the power to take the form of the person in your life that brings you the most comfort."
    GP "What I'm wearing is also a product of what your mind would prefer to see this person wearing, mixed with a little Christmas flair for the season."
    GP "I look like your mom, you say?"
    GP "..."
    GP "You sick fuck!"
    R "This is so weird!"
    R "Though I'm still about 90 percent sure that this is just a dream."
    R "You're just something I ate.... an undigested piece of pizza..."
    R "Yeah.... that's all you are..."
    R "Which means I can do whatever I want to you."
    scene bg ChristmasEvent03
    with dissolve
    GP "Ooofff..."
    R "Holy shit!.... I can touch you!"
    play sound Twinkle
    scene bg ChristmasEvent04
    with dissolve
    R "Oh, shit!.... Where did she go?"
    scene bg ChristmasEvent05
    with dissolve
    R "She's gone!..."
    R "I guess I was dreaming after all."
    play sound Twinkle
    scene bg ChristmasEvent06
    with dissolve
    GP "You son of a bitch!"
    GP "You try a move like that again and I'll cut your cock off!"
    GP "If you still think you're dreaming, come at me!"
    R "Ok.... ok.... I won't grab you again!.... Just let me go..."
    scene bg ChristmasEvent07
    with dissolve
    GP "Woah.... holy shit!"
    GP "Haha.... you like it when I'm rough with you, don't you?"
    GP "You dirty boy!"
    R "Yes.... I mean no!.... Can you please let my cock go?"
    GP "Hmmmm.... I guess I could, if you promise not to touch me, and to sit there and listen to me."
    R "Ok, I promise!"
    RT "{i}I wonder if I could capture her in a jar or something.{/i}"
    GP "[ryan]! I can hear your thoughts, remember? And no, I'd just disappear out of a jar."
    R "Sorry.... I won't do anything stupid."
    scene bg ChristmasEvent08
    with dissolve
    GP "Great!.... Because you've got a very busy night ahead of you."
    R "Huh?....I can't move!..."
    GP "Just a safety precaution."
    GP "You will be visited by three spirits, including myself, obviously."
    R "What?.... But why?"
    GP "Your actions have caught the attention of \"The Woman Upstairs.\""
    R "What really?.... So God's a woman?"
    GP "Actually a woman that can grow a penis.... I think you would call her a \"futa.\""
    R "Wow!"
    R "And what have I done to get her attention on me?"
    GP "What do you think?"
    GP "I'll give you three guesses.... and they all live in this house."
    GP "And we can sense that you're about to turn up your devious efforts a few notches over the Christmas holidays."
    R "Oh.... you guys have been listening to my thoughts, huh?"
    GP "Oh, yes.... and we're here to show you the consequences of your actions."
    GP "While we don't have problems with sexual promiscuity in general,"
    GP "we tend to frown on fucking your own family."
    GP "It just causes complications down the line."
    scene bg ChristmasEvent09
    with dissolve
    GP "Although, I do see why the women in your family are so tempting for you."
    GP "I mean, look at that ass!"
    R "I know, right?..."
    GP "I haven't had a good taste of ass in a millennium."
    GP "I've just been stuck in the spirit realm serving \"Her\", ever since I died."
    GP "No tasty asses there, only dead ones."
    R "Weren't we talking about the consequences of my actions?"
    GP "Were we?.... Uh.... just give me a second."
    scene bg ChristmasEvent10
    with dissolve
    R "You can fly?..."
    GP "Of course!.... You really don't know much about ghosts, do you?"
    R "What are you doing?"
    GP "I said just give me a second."
    scene bg ChristmasEvent11
    with dissolve
    R "..."
    R "Hey!.... What are you doing?"
    GP "I'm sorry!.... I just can't resist"
    R "But that's your daughter.... I mean my sister!"
    GP "What's the matter [ryan], jealous?"
    GP "Then why don't you come and stop me?"
    R "Because I can't move!"
    GP "Haha.... that's right."
    GP "I guess you'll just have to watch."
    scene bg ChristmasEvent12
    with dissolve
    GP "Oh, man!.... I've missed this!"
    RT "{i}Holy shit.... I know that's not really Mom licking Sidney, but that's actually pretty hot!{/i}"
    GP "Mmmppphhh.... haha.... remrembrere rhat I cran strill hear your throts..."
    R "Shit!"
    S "(sleepily mumbling) mmmmmmm.... [ryan].... that feels really.... nice.... "
    scene bg ChristmasEvent11
    with dissolve
    GP "There.... my spiritual batteries are all re-charged."
    GP "So, are you ready for our journey?"
    R "What journey?"
    R "I'm not going anywhere with you."
    scene bg ChristmasEvent13
    with dissolve
    GP "I'm going to take you on a journey into Christmas past."
    GP "To a time when your parents first met."
    GP "I want you to see first hand, the beginning of the relationship that concieved you and your sisters, and the relationship you're currently trying to destroy."
    R "Can't you just tell me about it? I really need to get my sleep. I've got a busy day of seducing ahead of me tomorrow."
    GP "Haha.... you lazy, cheeky, asshole."
    GP "You don't have a choice."
    GP "Now get ready, because this could possibly give you motion sickness."
    scene bg ChristmasEvent14
    with dissolve
    $ renpy.pause ()
    scene bg ChristmasEvent15
    with dissolve
    $ renpy.pause ()
    scene bg ChristmasEvent16
    with fade
    scene bg BlurryWhite
    with fade
    scene bg SleepBlack
    with fade
    RT "{i}Ahhhh!.... Where the hell am I?{/i}"
    GP "You're dissolving through the wormholes of time."
    GP "Just relax, we'll be there in just a couple more seconds."
    jump christmas_club

label xmas_present:
    scene bg SleepBlack
    RT "{i}zzzzzzz.... {/i}"
    "..."
    X "[ryan]..."
    X "Hey [ryan]..."
    scene bg BlurryWhite
    with fade
    scene bg SleepBlack
    with fade
    X "Wake up [ryan]!..."
    scene bg BlurryWhite
    with fade
    scene bg SleepBlack
    with fade
    X "Hey [ryan]!.... Wake up!"
    RT "{i}Huh.... what?....{/i}"
    scene bg LChristmas01
    with fade
    scene bg SleepBlack
    with fade
    scene bg LChristmas01
    with fade
    scene bg SleepBlack
    with fade
    scene bg LChristmas02
    with fade
    R "Lauren?..."
    X "Guess again."
    R "Oh, fuck!.... I thought I was done with this dream."
    X "Maybe it's not a dream."
    R "Wouldn't you just tell me it's not a dream, if it weren't really a dream?"
    X "That wouldn't be any fun, if we took out the wonder."
    X "We're doing this for your welfare."
    R "Wouldn't a night of uninterrupted sleep be better for my welfare?"
    X "For your salvation then."
    R "Salvation from what?"
    X "From being such a creepy little pervert."
    RT "{i}Hah.... good luck!{/i}"
    X "I can read thoughts."
    R "Oh, yeah..."
    R "So, are you \"The Leprechaun of Christmas Present\", or something?"
    scene bg LChristmas03
    with dissolve
    X "I'm the \"Ghost of Christmas Present.\""
    R "Well, of course you are."
    GCP "I see my sister's anger at you was not misplaced."
    GCP "After the experience with the first ghost, a client is usually well on his way to being reclaimed, but my sister thinks that you actually regressed with your first visitation."
    if first_xmas_ntr == False:
        GCP "She also warned me to stay away from the end of your penis."
        GCP "Haha.... I've never seen her so mad."
    else:
        pass
    GCP "She did tell me that I must try the local flavor while I'm here in town though."
    scene bg LChristmas04
    with dissolve
    GCP "Oh, yes!.... And there she is."
    scene bg LChristmas05
    with dissolve
    GCP "Oh, my.... It looks like she was right. That is one tasty looking ass."
    GCP "This job has very few benefits, but it does have it's moments sometimes."
    scene bg LChristmas06
    with dissolve
    R "Dammit, I'm stuck again!"
    R "Stop eating my sister's ass!"
    GCP "Hahaha.... yeah the Ghrost urf Chrismras prast warned mre that thris wourd priss ru orff."
    GCP "Sro I trook the proper precrautions."
    R "What is it with ghosts and eating ass?"
    S "(sleepily muttering).... ohhhhh.... [ryan].... since when do you like eating ass?.... That feels soooo good!"
    R "And why is it ok for you to be sexually depraved, but you want to stop me from doing just that."
    scene bg LChristmas07
    with dissolve
    GCP "Well, the difference is she's not my sister."
    R "Well, I guess you've got me there."
    GCP "Great! So, are you ready for your next adventure?"
    R "I'd rather keep sleeping, to be honest."
    GCP "Come on, party pooper!"
    GCP "We're going to the Christmas Present."
    R "So, the Christmas that's about to happen this year?"
    GCP "That's right."
    scene bg LChristmas08
    with dissolve
    GCP "So, get ready!"
    GCP "And try not to puke!"
    play sound Twinkle
    scene bg LChristmas09
    with dissolve
    $ renpy.pause ()
    scene bg LChristmas10
    with fade
    scene bg BlurryWhite
    with fade
    scene bg SleepBlack
    with fade
    R "Oh, I hate this part!"
    GCP "Yeah, you never really get used to it either."
    GCP "Just relax, we'll be there in just a couple more seconds."
    jump christmas_shoot

label xmas_future:
    scene bg SleepBlack
    with fade
    "Shlurp.... shluurp.... smack"
    RT "{i}What is that noise?{/i}"
    scene bg BlurryWhite
    with fade
    scene bg SleepBlack
    with fade
    "Shlurp, shlirrk, shmork"
    S "(sleepily) Again!.... Oh [ryan]!.... That feels so good!"
    scene bg BlurryWhite
    with fade
    scene bg SChristmas10
    with fade
    scene bg SChristmas01
    with dissolve
    "Shlirk, shmlack"
    R "What the hell is going on?"
    scene bg SChristmas02
    with dissolve
    X "Oh.... hey [ryan]!"
    X "Sorry I woke you!"
    X "My sisters both told me I had to try out the all you can eat breakfast buffet."
    X "They said you got a little hot under the collar when they did this."
    X "So, I thought I'd just get it out of the way before you woke up."
    X "But I think I've had my fill. Should we get down to business?"
    scene bg SChristmas03
    with dissolve
    $ renpy.pause ()
    scene bg SChristmas04
    with dissolve
    X "Do I need to introduce myself, or do you already know who I am?"
    R "The ghost of Christmas Future, I presume?"
    GF "You are correct!"
    GF "And do you know why I'm here?"
    R "To stop me from fucking my family?"
    GF "Haha.... that's pretty blunt and to the point."
    GF "But that's actually where you're wrong."
    GF "I'm not here to stop you from doing anything."
    GF "In fact, I don't give a fuck about what you choose to do with your life."
    GF "I'm just here as a guide, to take you a couple of years into the Christmas future, to show you the consequences of your actions."
    GF "If you like the results, great! If not, you can decide to make different choices."
    GF "Whatever tickles your pickle."
    R "Well, I've got to say it's nice to meet a ghost that's not so judgy."
    GF "Yeah, my sisters can be real condescending bitches."
    GF "Haha.... but you brought them down a peg."
    GF "God's not going to be super happy with them after tonight's over."
    GF "I wouldn't be surprised if she sends them to the sex dungeon for a decade."
    R "Oh, no!.... That sounds awful! Now I feel really bad that I didn't try to follow their game plan better."
    GF "Ahhh.... don't worry about it, everyone secretly likes the sex dungeon anyways."
    GF "I've been there so many times, they've made me an honorary torturer."
    R "Is that why you don't shine as bright as your sisters?"
    GF "Naaahhh.... It's just because I'm supposed to be the more scary ghost."
    GF "You see, most people fear their future, so they gave me this whole facade to make me more scary."
    GF "Do I seem scarier to you?"
    R "Nah.... making you look like my hot sister Sidney, kind of takes away the whole fear factor."
    GF "See! That's what I've been saying! Let me wear a holocaust robe, and give me a skull for a head, you know, like they did in the old days."
    GF "Too much PC shit in Heaven. We're not allowed to scare anyone too badly anymore."
    GF "Ahhh.... but we shouldn't be discussing heavenly politics. I've got a job to do, and not a lot of time to get it done."
    GF "Are you ready to go to the future?"
    R "I guess! Go ahead and blow that magic fairy dust on me"
    GF "Yeah.... I'm not into that flowery bull-shit. I do things a little differently."
    scene bg SChristmas05
    with dissolve
    R "What are you doing?"
    GF "Just give me a second."
    scene bg SChristmas06
    with dissolve
    GF "Huhhnngghhhh..."
    R "Oh, no!"
    play sound Fart
    scene bg SChristmas07
    with dissolve
    R "Ohhhh..."
    R "Oh, my God!..."
    R "What in Futa God's name?..."
    R "Huh.... weird.... It.... smells like.... candy canes."
    scene bg SChristmas10
    with fade
    stop sound
    scene bg SleepBlack
    with fade
    RT "{i}What the.... I'm still in bed.... I don't think I've even moved.... these dreams are getting weird.{/i}"
    M "Wake up [ryan]!.... It's Christmas!"
    scene bg SChristmasMovie01Start
    with fade
    M "Good morning [ryan]!"
    R "....Mmm.... Mom?"
    M "That's right, honey.... merry Christmas!.... I wanted to be the first to give you a present."
    play music SexMusic
    M "I hope you enjoy it!"
    scene SChristmasMovie01
    with dissolve
    R "Ohhh.... Mom!"
    RT "{i}Ok.... Mom's giving me a morning handy!.... I'm definitely in the future.{/i}"
    RT "{i}What the hell? If I get to wake up to this in the morning, why would I want to change anything?{/i}"
    RT "{i}Ohhh.... that feels so good!{/i}"
    RT "{i}And the fact that Mom is doing it is a dream come true. I wonder what else we do together in the future.{/i}"
    M "Oh, that's such a handful!"
    M "You're my big boy!"
    RT "{i}Ohhh.... she knows how to talk sexy too.{/i}"
    RT "{i}I shouldn't be surprised, I guess. {/i}"
    M "Are you going to blow your huge load all over my face?"
    R "Yes!.... I want to sooo bad!"
    M "Your cock is just pulsing in my hand! Are you close?"
    R "Yes, Mom!.... I'm so close!"
    scene bg SChristmasMovie01Start
    with dissolve
    R "..."
    R "Why did you stop?"
    M "Because it's barely morning! It's a big day today. You're going to need your stamina."
    R "But.... but that's just cruel!"
    M "Haha.... no, It will put you in the right mood for the rest of the day! I'll see you in just a bit. I've got to run use the bathroom."
    play music WeWishYou
    scene bg SChristmas08
    with dissolve
    RT "{i}What in the!....{/i}"
    RT "{i}Holy shit!....{/i}"
    RT "{i}Is Mom?....{/i}"
    play sound Twinkle
    scene bg SChristmas09
    with dissolve
    GF "Holy shit, dude! Is your mom pregnant?"
    RT "{i}Uhhh.... It kind of looks that way!{/i}"
    RT "{i}Unless she ate a really big breakfast burrito.{/i}"
    GF "Holy shit! I wonder if it's yours!"
    RT "{i}Could I have knocked up my own mother?{/i}"
    GF "That would be fucking legendary!"
    scene bg SChristmas11
    with fade
    R "Uhhh.... Mom!..."
    M "Hnnnhhh...Yeah honey?"
    R "I need to talk to you a little before you leave!"
    scene bg SChristmas12
    with dissolve
    M "Alright, well make it fast."
    M "You know how a pregnant woman's bladder is."
    M "And unless you're into water sports..."
    R "Mom!..."
    M "Haha.... what is it you want?"
    R "Uhhh.... I hope this isn't too indelicate to ask?"
    R "But.... how far along are you?"
    M "Hmmm.... let me think..."
    M "I should be about 7 months along now."
    R "Wow!.... I mean you still look great!"
    M "Haha.... thanks hon!"
    R "Uhhhh.... and do we think it's mine?"
    scene bg SChristmas14
    with dissolve
    M "Are you serious?"
    R "Uhhh.... yeah.... I mean..."
    M "You must still have foggy morning brain, or pent up sexual energy brain, or something."
    R "Well?..."
    if first_xmas_ntr:
        M "Of course it's not yours!"
        M "How do you think you could get me pregnant, when I only let you have sex with my butt?"
        R "Well.... yeah.... I suppose that's a pretty effective form of birth control."
        M "You know my pussy is reserved for [dad_name]!"
        R "So Dad got you pregnant?"
        R "Did he get out of prison?"
        M "[ryan]? Are you sure you're ok? I wonder if you have a fever or something."
        R "What? No.... I mean yes.... I'm ok, but is Dad out of prison?"
        scene bg SChristmas13
        with dissolve
        M "Of course not honey! I know you miss him.... but I'm afraid he's going to be gone a very long time."
        RT "{i}Oh Thank God?{/i}"
        R "So, how did you get pregnant?"
        M "I know you've heard of conjugal visits."
        R "And you're ok raising him as a single mom?"
        M "No silly. You said you'd help! You'll be like his second daddy!"
        RT "{i}You've got to be fucking kidding me!{/i}"
        GF "Oh man, and you're going to have to support his kid financially! You totally got cucked!"
        RT "{i}Oh shit! I can't believe this is happening!{/i}"
        GF "Hey, don't sweat it too bad! This hasn't happened yet. Now you can take steps to prevent this."
        GF "You know, like rolling back scenes in one of those crappy incest H-games you like, so you can make the better decision?"
        GF "You can fix this!"
        RT "{i}Yeah, you're right! Oh Thank Futa God!{/i}"
        M "Don't worry! You'll be the best surrogate dad!"
    else:
        M "Well, of course it's yours!"
        M "Who else's would it be?"
        M "Your father is in prison."
        M "And between posing for pictures for you, and working at the school, I have no time to meet any other men."
        scene bg SChristmas12
        with dissolve
        M "And I'm kind of freaking out here because I'm carrying your baby."
        M "And your father is going to murder me when he gets out, and meet's his grandbaby slash step-son!"
        M "Meanwhile, I have to raise and care for another baby! I thought I was done with that stage of my life!"
        R "Hey.... hey.... relax!.... It's ok!..."
        R "I'm going to be there to help take care of the baby!"
        R "I'll take care of you financially."
        scene bg SChristmas13
        with dissolve
        R "I have it on good authority that Dad's not getting out of prison any time before we can cut all ties to him."
        R "It's all going to be alright!"
        RT "{i}Holy shit!.... I'm going to be a daddy!{/i}"
        GF "Sure! If that's the way you want it.... that's the beauty of this gift you're receiving from us."
        GF "It's like having the ability to roll back life. You know, like one of those crappy incest H-games you like, where you can roll back to make the better choice if you fuck up."
        GF "If you want to be a dad, good job. If you decide you don't want to be. You can decide to wear a condom, or only have anal sex."
        RT "{i}Thank you! That is a pretty sweet gift.{/i}"
        M "Thanks for the pep talk honey!"
    scene bg SChristmas16
    with dissolve
    M "If that's it, I'm going to run to the bathroom before I piss myself."
    M "You should get out of your room, and go see Lauren and Sidney. I think Lauren is baking cookies in the kitchen, and I think Sidney is in the lounge making sure everything is ready for our Christmas gift exchange."
    M "After that, we'll all meet in the lounge for the gift exchange. I think you'll like the gift we're all going to give you."
    scene bg SChristmas15
    with dissolve
    scene bg SChristmas16
    with dissolve
    $ renpy.pause ()
    scene bg SChristmas11
    with dissolve
    $ renpy.pause ()
    scene bg SChristmas34
    with dissolve
    $ renpy.pause ()
    scene bg SChristmas17
    with dissolve
    GF "Hahahaha.... holy shit!"
    if first_xmas_ntr:
        GF "In all the years I've been showing people their Christmas futures, I've never seen anyone cucked as hard as that!"
        GF "Are you ok? Should I call an ambulance so the crew can come fuck your mom and then take you to the hospital?"
        RT "{i}Fuck off!{/i}"
        GF "I'm sorry! I really do feel sorry for you, man!"
        GF "But like I said. This is not final. And even if it were, at least you're getting some side action from that hot piece of ass."
    else:
        GF "You are amazing!"
        GF "In all the years I've been showing people their Christmas futures, I've never seen anyone be surprised with impregnating their mom!"
        GF "Ohhh.... hoho.... the look on your face!"
        GF "I've got to say! That's pretty damn awesome! What better way to claim a woman for yourself, than to impregnate her."
        GF "I don't know if I'd change a thing. Unless you hate kids or something."
    GF "So, are you ready to move on?"
    GF "I think your mom said something about cookies downstairs. Let's go see if they're done, and we can talk to Lauren while we're at it."
    scene bg SleepBlack
    with fade
    jump cookies_in_oven

label xmas_goodbye:
    scene bg SChristmas04
    with fade
    GF "Sorry that we weren't able to stay longer."
    GF "Sometimes at these things you can't wait to get away, and sometimes you wish you could stay forever."
    GF "You definitely left on a high note though."
    GF "So, did you learn anything?"
    R "I learned that life is like a Ren'Py game.... It's full of choices, and I just need to make the ones that make me the happiest."
    R "The best choice, usually leads to the outcome that makes the other NPC's happy too."
    R "No one can tell me which choices are right for me, because each player can make whatever choices makes them the happiest."
    R "And if they want to judge me, like some troll in some incest game forum."
    R "I just need to ignore them and keep living life the way I want."
    GF "That's a great lesson, and anyone who tries to impose their version of morals on you can go fuck themselves."
    GF "Haha.... just like Futa God is going to be fucking my sisters as soon as Christmas is over."
    GF "I hope your upcoming Christmases are all better than the last."
    GF "It's been fun!"
    GF "Keep it up, and maybe Futa God will send us back next year!"
    GF "Merry Christmas!"
    play sound Twinkle
    scene bg ChristmasEvent57
    with dissolve
    RT "{i}Holy shit!.... Dream or not, I don't want to ever forget that experience.{/i}"
    RT "{i}Oh Futa God.... I'm so tired now.... but will I even remember this dream when I wake up?{/i}"
    scene bg SleepBlack
    play music Honey
    jump myroom

label tutorial:
    play music Honey
    scene bg SleepBlack
    with fade
    scene bg Tutorial36
    with dissolve
    $ renpy.pause ()
    scene bg Tutorial37
    with fade
    $ renpy.pause (0.75)
    scene bg Tutorial27
    with fade
    R "Testing.... testing.... ok.... It looks like it's recording."
    scene bg Tutorial34
    with dissolve
    R "My name is [ryan].... and if you are watching this recording, it means that I am dead."
    R "Or I guess it could mean the extremely unlikely scenario that my computer was hacked, and now some schmuck is using my story for financial gain."
    scene bg Tutorial28
    with dissolve
    R "Because the series of events I'm going to tell you about is so unbelievable, it would make a great movie or TV series."
    R "But probably the kind of TV series you could only see on HBO."
    scene bg Tutorial33
    with dissolve
    R "Please God, just don't let anybody make a crappy H-game out of this."
    scene bg Tutorial38
    with dissolve
    $ renpy.pause ()
    WT "Ummm.... hi!"
    WT "Sorry to interrupt."
    WT "My name is Will Tylor and I just wanted to take this opportunity to welcome you to our \"awesome\" H-game, \"A Family Venture!\""
    WT "Back to you, [ryan]."
    scene bg Tutorial33
    with dissolve
    scene bg Tutorial28
    with dissolve
    R "I wanted to record my version of the remarkable events that have occurred over the last little while."
    R "I know many wouldn't understand why I've been doing the things I'm doing, if I didn't explain myself, so this is my attempt to justify my actions."
    R "I've been acquiring many items to help me achieve my goals, of saving those I love, and helping that love to become even more realized."
    scene bg Tutorial29
    with dissolve
    WT "Thanks [ryan].  Let me do a little explaining from here."
    scene bg Tutorial01
    with fade
    WT "This is a typical in-game screen.  As [ryan] mentioned, you will acquire many items in the game."
    scene bg Tutorial02
    with dissolve
    WT "You can keep track of the items you acquire by clicking on this blue backpack."
    scene bg Tutorial08
    with dissolve
    WT "This will open up your inventory,"
    scene bg Tutorial09
    with dissolve
    WT "where you will be able to see how much money you have earned,"
    scene bg Tutorial10
    with dissolve
    WT "and what items you have acquired."
    scene bg Tutorial01
    with dissolve
    WT "There are several other important items on the game screen I'd like to draw your attention to."
    scene bg Tutorial03
    with dissolve
    WT "This symbol shows you what day of the week it is,"
    scene bg Tutorial04
    with dissolve
    WT "while this symbol shows you the time of day."
    scene bg Tutorial29
    with fade
    WT "I'll let you get back to [ryan] again."
    scene bg Tutorial28
    with dissolve
    R "I've had to become very good at managing my money.  I've got debts I have to pay, and items I need to buy, to help influence those around me."
    scene bg Tutorial30
    with dissolve
    R "I've become aware that someone, or several someones, have been tracking my movements. So, I have learned to be stealthy, and to watch my back wherever I go."
    scene bg Tutorial31
    with dissolve
    WT "Let me just pause you again for a second.  [ryan] brings up a good point about getting around."
    WT "You will find that navigation is very important in this type of game, so let me just show you how that's done."
    scene bg Tutorial01
    with dissolve
    WT "On the game screen, you can get around to many locations by using the travel buttons."
    scene bg Tutorial06
    with dissolve
    WT "This button right here, will open up a map of the house, where you can pick any room you would like to go to."
    scene bg Tutorial07
    with dissolve
    WT "You can also hover your cursor over this button, to open up the quick travel options."
    WT "These buttons will take you to any room in the house, as well as the world map."
    WT "Exploring the AFV world is vitally important, as you will find that some events only happen at certain times, and in certain places."
    WT "So, have fun exploring!"
    scene bg Tutorial31
    with fade
    $ renpy.pause ()
    scene bg Tutorial30
    with dissolve
    R "I never can be sure who is following me, even though I have my suspicions."
    R "Always having to watch my back has made me grow closer to the few people I can trust."
    R "And who can I trust better than those that live right here with me?"
    "{i}\"(knock knock knock....)\"{/i}"
    M "{i}(muffled voice){/i} [ryan]?   Why is the door locked?  You're not looking at porn and masturbating again are you?"
    scene bg Tutorial32
    with dissolve
    R "No, Mom!.... But I'm really busy right now!"
    M "With what?"
    R "Ummm.... homework.... of course!"
    M "Well, ok.... but you know you don't need to take care of yourself like that anymore, right?"
    M "You know that if you need some relief, you just need to let me know.  And if I'm too busy, I'm sure Lauren or Sidney would be happy to help you out."
    scene bg Tutorial33
    with dissolve
    R "Ok!.... Thanks, Mom!"
    R "Please, don't judge me until you've heard my side of the story."
    scene bg Tutorial34
    with dissolve
    R "It's like I said.... with so many shady characters around tracking my movements, I've needed to grow closer to the people around me."
    scene bg Tutorial35
    with dissolve
    WT "Let me just jump in here one more time."
    scene bg Tutorial01
    with fade
    WT "To be successful, [ryan] has to influence those around him."
    WT "Relationship management is the most important part of this game."
    WT "You will need to make choices throughout the game that will influence the way the girls in your life feel about you."
    WT "So, it's pretty important that you keep track of those stats."
    WT "You can access a girl's stats,"
    scene bg Tutorial19
    with dissolve
    WT "by pressing the \"P\" button on your keyboard."
    scene bg Tutorial20
    with dissolve
    WT "You can cycle through the girls in the game by clicking on the left or right arrows."
    scene bg Tutorial21
    with dissolve
    WT "Once you've found the girl you want to track, you can figure out her stats by looking at the icons by her name and picture."
    scene bg Tutorial22
    with dissolve
    WT "The heart icon stands for love."
    scene bg Tutorial23
    with dissolve
    WT "These hands represent respect."
    scene bg Tutorial24
    with dissolve
    WT "The angry emoji stands for a girl's anger towards you.  It's hard to get them to do anything for you when they are mad."
    scene bg Tutorial25
    with dissolve
    WT "This whip icon, represents a girl's submission to you."
    scene bg Tutorial26
    with dissolve
    WT "And these lips represent a girl's libido."
    scene bg Tutorial01
    with dissolve
    WT "To close the stats window, just press the \"P\" on your keyboard again."
    WT "Another handy way to track a girl's stats is through your phone."
    scene bg Tutorial05
    with dissolve
    WT "You can access your phone by clicking on this button."
    scene bg Tutorial11
    with dissolve
    WT "Once your phone is pulled up, you can track a girl's stats,"
    scene bg Tutorial13
    with dissolve
    WT "by clicking on this button right here."
    scene bg Tutorial11
    with dissolve
    WT "There are also some other handy things you can do with your phone as well."
    scene bg Tutorial12
    with dissolve
    WT "For those of you who support us at the \"Friend\" tier on SubscribeStar or Patreon, you can install a mod that you can access by pressing on this button."
    WT "The mod is pretty awesome!  It allows you to change the name of your character, manipulate the stats of other characters, add and remove items, and add money to your backpack."
    scene bg Tutorial14
    with dissolve
    WT "This button allows you to track your progress.  When you click on it,"
    scene bg Tutorial17
    with dissolve
    WT "A screen that lists events will pop up."
    scene bg Tutorial18
    with dissolve
    WT "And when you click on the three question marks \"???\", you will receive hints to help you know how to complete that event."
    scene bg Tutorial11
    with dissolve
    WT "A couple other useful buttons are on the bottom of the phone."
    scene bg Tutorial15
    with dissolve
    WT "This button lets you see any pictures of girls that you may take throughout the course of the game."
    scene bg Tutorial16
    with dissolve
    WT "And this extremely useful button lets you move forward in time."
    scene bg Tutorial01
    with dissolve
    WT "So, that's all the tips we have for you.  Everything else you will have to figure out on your own, or I guess you could always find the walkthrough, or ask for help online."
    WT "However you decide to play, we hope you enjoy the game!"
    scene bg Tutorial35
    with dissolve
    WT "Go ahead and take it from here, [ryan]!"
    scene bg Tutorial34
    with dissolve
    R "I guess the best thing I can do is to tell you my story, and let whomever watches this to be the judge of my actions."
    R "And once again, hope this story gets turned into a kick-ass HBO series, and not a fucking lame-ass H-game."
    scene bg Tutorial30
    with dissolve
    R ".... So, until fairly recently, I was just a normal teenage kid like everybody else."
    R "Until I was awoken really early one morning by a phone call that would change my life forever..."
    R "..."
    scene bg SleepBlack
    with fade
    "End of tutorial."
    jump gamestart

############  LOUNGE  ##############################  LOUNGE  ##################################  LOUNGE  ###########################  LOUNGE  ################################  LOUNGE  ##########################  LOUNGE  ####################################  LOUNGE  ################################  LOUNGE  #####################################  LOUNGE  ##################################lOUNGE##

label sidney_prego_too:
    scene bg SChristmas28
    with fade
    GF "Oh, look! There she is, adjusting something on the Christmas tree."
    RT "I'll wager money that when she turns around, she'll have a pregnant belly too."
    GF "Yeah, I'm not betting you. I think the odds are too much in your favor."
    scene bg SChristmas29
    with dissolve
    RT "{i}Ha!.... Called it!{/i}"
    GF "Congratulations for being able to see obvious plot points in simple-minded stories."
    RT "{i}Huh?....{/i}"
    GF "Never mind."
    S "Merry Christmas, [ryan]!"
    scene bg SChristmas30
    with fade
    R "Oh, hey Sidney! Merry Christmas! I love your sweater!"
    S "Thanks! I made it myself. I thought it was pretty festive."
    S "But it's too damn hot!"
    S "This baby is like having my own personal space heater attached to me."
    scene bg SChristmas31
    with dissolve
    S "I can't seem to get cool, no matter what I do."
    RT "{i}I think I'm starting to understand why guys get pregnancy fetishes.{/i}"
    RT "{i}Every single one of the girls still looks sexy as hell, even with their huge baby bumps.{/i}"
    RT "{i}I guess I should just add this fetish to the list.{/i}"
    GF "They should hand out fetish merit badges. You'd be one of the most decorated perverts out there."
    RT "{i}And to think, I was a totally normal kid, not too long ago.{/i}"
    GF "Well, every pervert's got to start somewhere."
    RT "I've got to find out who's the father of Sidney's baby."
    GF "Maybe you could try the \"Keeping a History of Events for the Year,\" route with Sidney."
    GF "That worked well with Lauren."
    R "So, I've been trying to record all of the notable events for this year. You know.... kind of a journal, so we can look back and remember the good times."
    R "After talking with Mom and Sidney, I think I've got most of the events covered. The last thing I need for the record, is your version of how you got pregnant."
    if first_xmas_ntr == True and second_xmas_ntr == True:
        scene bg SChristmas33
        with dissolve
        S "Nice try, [ryan]! I know you're only bringing this up so you can reprimand me again for what stupid decisions I make."
        S "I already know it was stupid of me to follow Mom to Joey's strip club."
        S "I already know it was stupid of me to accept the work that Joey was offering."
        S "I know it was stupid of me to let him buy me nice things."
        S "I know it was stupid of me to think he would ever leave his wife for me."
        S "I don't know how, or why, I let him manipulate me to become his tool to blackmail powerful men."
        S "I'd sleep with them, and Joey would record it all, to use the pictures later for blackmail."
        scene bg SChristmas31
        with dissolve
        S "And now I've slept with most of the powerful men in the state, and I don't know if my baby's father is Senator McFeely, Archbishop SaintFister, Governor LeGroper,"
        S "Chief O'CummingHand, Don BiggusDickus.... (rambling on)"
        GF "Oh, damn! Holy shit! You're zero for three."
        GF "I don't want to sound too intrusive or judgy, but you might want to do a few things to try and change this future."
        GF "Unless you get off on other men fucking your women. Like I said, I don't judge."
        RT "{i}Trust me, I'm keeping a mental list of things I need to change.{/i}"
        RT "{i}Though they're not the kind of changes your sisters would want me to make.{/i}"
        GF "Ahhh.... Fuck 'em."
        RT "{i}They're too small.{/i}"
        GF "Hahaha.... you'd be surprised at how much they can stretch."
        S "Principle Wankright, School board member Will Tylor."
        R "Sidney! Shut up for a second"
        scene bg SChristmas33
        with dissolve
        R "I understand you slept with half the state, but is there any possible way that I could be the daddy?"
        S "No.... I wasn't living at home at the time. I was too busy with the DeCapos. Joey had me living in his high rise apartment."
        S "And you refused to even come visit me."
        scene bg SChristmas31
        with dissolve
        S "But I was so grateful that you let me come back home, even though I was hooked on meth and had a vagina looser than a wizards sleeve."
        R "Ok Sidney, just stop. I've got everything I need for the family history. And your section of it is going to be quite a legacy."
        S "Ahhh.... Fuck it. I know what I am."
        S "I was quite the prude at one time, then it all changed when I started molesting people in their sleep."
        S "You remember that?"
        R "Of course I do."
        S "Sorry if that messed you up at all."
        S "I know it did me."
        RT "{i}Shit.... I've ruined her life. And now she's apologizing to me, for something I made her do.{/i}"
        RT "{i}Fuck! I'm ready to go back right now, and try to fix some things.{/i}"
        GF "Well, you know how this works. We've got to wait in the future until our time is up. While you're waiting, go look around and maybe you can find something that will cheer you up."
        S "Oh look, Here comes Mom and Lauren."
        S "I'm just going to go sit down and have a little break. My back is killing me."
    elif first_xmas_ntr:
        scene bg SChristmas32
        with dissolve
        S "Hahah.... nice try, [ryan]!"
        S "I know you're only bringing that up because you like to gloat that you were able to knock up both me and Lauren."
        GF "Ahhh! Way to go! Two out of three's not bad at all!"
        S "And yes, we all think you're amazing, and yes we're super grateful for all of the shit you've done for us."
        scene bg SChristmas31
        S "I hope you don't keep bringing it up because you don't feel appreciated!"
        S "Because what you did to get us out from under the thumb of those Mafia goons!.... Well, it was so heroic."
        S "Not many people are able to shrug off the Mafia like you did, without having to go into witness protection."
        S "And now, you've gained both their respect and their apathy."
        S "You really should write a book about it someday!"
        R "Really? Tell me!.... What did I do!?..."
        scene bg SChristmas33
        S "Ohhhhh.... of course you know!.... And there's no need for false modesty."
        S "Needless to say. Lauren and I, are both very proud to be carrying your babies!"
        S "We don't give a fuck about what other people think."
        S "Though we still will probably lie about who their father is."
        GF "Yeah, It will be confusing enough to try to explain to them that they are both cousins and siblings."
        S "Oh look, here comes Mom and Lauren. I'm just going to go sit on the couch and take a little break. My back is killing me."
    elif second_xmas_ntr:
        scene bg SChristmas32
        with dissolve
        S "Hahah.... nice try, [ryan]!"
        S "I know you're only bringing that up because you like to gloat that you were able to knock up both me and Mom."
        GF "Ahhh! Way to go! Two out of three's not bad at all!"
        S "And yes, we all think you're amazing, and yes we're super grateful for all of the shit you've done for us."
        scene bg SChristmas31
        S "I hope you don't keep bringing it up because you don't feel appreciated!"
        S "Because what you did to get us out from under the thumb of those Mafia goons!.... Well, it was so heroic."
        S "Not many people are able to shrug off the Mafia like you did, without having to go into witness protection."
        S "And now, you've gained both their respect and their apathy."
        S "You really should write a book about it someday!"
        R "Really? Tell me!.... What did I do!?..."
        scene bg SChristmas33
        S "Ohhhhh.... of course you know!.... And there's no need for false modesty."
        S "Needless to say. Mom and I, are both very proud to be carrying your babies!"
        S "We don't give a fuck about what other people think."
        S "Though we still will probably lie about who their father is."
        GF "Yeah, It will be confusing enough to try to explain to them that they are simultaneously aunt or uncle, niece or nephew, and siblings."
        S "Oh look, here comes Mom and Lauren. I'm just going to go sit on the couch and take a little break. My back is killing me."
    else:
        scene bg SChristmas32
        with dissolve
        S "Hahah.... nice try, [ryan]!"
        S "I know you're only bringing that up because you like to gloat that you were able to knock up all three of us."
        S "Yes, you have amazing swimmers!"
        GF "All three!!!.... You sir, are a fucking legend!"
        S "And yes, we all think you're amazing, and yes we're super grateful for all of the shit you've done for us."
        scene bg SChristmas31
        S "I hope you don't keep bringing it up because you don't feel appreciated!"
        S "Because what you did to get us out from under the thumb of those Mafia goons!.... Well, it was so heroic."
        S "Not many people are able to shrug off the Mafia like you did, without having to go into witness protection."
        S "And now, you've gained both their respect and their apathy."
        S "You really should write a book about it someday!"
        R "Really? Tell me!.... What did I do!?..."
        scene bg SChristmas33
        S "Ohhhhh.... of course you know!.... And there's no need for false modesty."
        S "Needless to say. All three of us are very proud to be carrying your babies!"
        S "We don't give a fuck about what other people think."
        S "Though we still will probably lie about who their father is."
        GF "Yeah, It will be confusing enough to try to explain to them that they are simultaneously aunt or uncle, nieces or nephews, cousins, and siblings.."
        S "Oh look, here comes Mom and Lauren. I'm just going to go sit on the couch and take a little break. My back is killing me."
    scene bg BlurryWhite
    with fade
    scene bg SChristmas35
    with fade
    GF "Looks like the ladies are all worn out."
    RT "{i}Yeah, I hear pregnancy takes a lot out of you.{/i}"
    R "You girls look beat!"
    scene bg SChristmas36
    with dissolve
    R "Is there anything I can do for any of you?"
    L "Ohh.... that's so sweet!"
    S "And we're not totally beat. We're just conserving our energy for when we give you our present."
    GF "I like that sound of that!.... But I will warn you.... you better hurry. Our time here is almost up."
    M "So, are you ready now for our present?"
    R "More ready than anything!"
    M "Ok.... all you have to do, is take off your clothes, lie on the coffee table, and pick one of us."
    R "Pick one of you?"
    R "What for?"
    M "Just do as I say. Take off your clothes, lie down, and pick one of us."
    RT "{i}How on earth will I choose?{/i}"
    GF "I'd pick Sidney, but then again, I'm slightly biased."
    play music SexMusic
    menu:
        "Mom":
            jump mom_xmas_fuck
        "Sidney":
            jump sidney_xmas_fuck
        "Lauren":
            jump lauren_xmas_fuck

label mom_xmas_fuck:
    if mom_first_xmas_fuck:
        stop sound
        play sound MattMegan loop
        scene PreggyMovie03
        with fade
        $ renpy.pause ()
        $ renpy.pause ()
        menu:
            "Fuck Sidney":
                jump sidney_xmas_fuck
            "Fuck Lauren":
                jump lauren_xmas_fuck
            "Cum" if sidney_first_xmas_fuck == True and lauren_first_xmas_fuck == True:
                jump xmas_facial
    else:
        stop sound
        play sound MattMegan loop
        scene PreggyMovie03
        with fade
        RT "{i}This might just be a dream, but to fuck Mom in the ass, makes it the best dream I've ever had.{/i}"
        S "Wow Mom! You need to teach us to take a cock in the ass like that!"
        L "Yeah! [ryan]'s always been too big for us."
        $ mom_first_xmas_fuck = True
        menu:
            "Fuck Sidney":
                jump sidney_xmas_fuck
            "Fuck Lauren":
                jump lauren_xmas_fuck
            "Cum" if sidney_first_xmas_fuck == True and lauren_first_xmas_fuck == True:
                jump xmas_facial

label sidney_xmas_fuck:
    if sidney_first_xmas_fuck:
        stop sound
        play sound Sidney01 loop
        scene PreggyMovie01
        with fade
        $ renpy.pause ()
        $ renpy.pause ()
        menu:
            "Fuck Mom":
                jump mom_xmas_fuck
            "Fuck Lauren":
                jump lauren_xmas_fuck
            "Cum" if mom_first_xmas_fuck == True and lauren_first_xmas_fuck == True:
                jump xmas_facial
    else:
        stop sound
        play sound Sidney01 loop
        scene PreggyMovie01
        with fade
        RT "{i}Wow! I would be fine if this dream never ended.{/i}"
        GF "Or is it a dream?"
        M "Honey! You're doing so good! Not many pussies can take a cock as big as [ryan]'s"
        L "Well, mine can take even bigger."
        $ sidney_first_xmas_fuck = True
        menu:
            "Fuck Mom":
                jump mom_xmas_fuck
            "Fuck Lauren":
                jump lauren_xmas_fuck
            "Cum" if mom_first_xmas_fuck == True and lauren_first_xmas_fuck == True:
                jump xmas_facial

label lauren_xmas_fuck:
    if lauren_first_xmas_fuck:
        stop sound
        play sound Lauren01 loop
        scene PreggyMovie02
        with fade
        $ renpy.pause ()
        $ renpy.pause ()
        menu:
            "Fuck Mom":
                jump mom_xmas_fuck
            "Fuck Sidney":
                jump sidney_xmas_fuck
            "Cum" if mom_first_xmas_fuck == True and sidney_first_xmas_fuck == True:
                jump xmas_facial
    else:
        stop sound
        play sound Lauren01 loop
        scene PreggyMovie02
        with fade
        RT "{i}Well, if this is a dream, I have a feeling it's going to be a wet one.{/i}"
        S "Lauren, you've got the cutest little asshole!"
        M "The trick is to get it so it can take a huge dick, but still look cute. It's not easy."
        $ lauren_first_xmas_fuck = True
        menu:
            "Fuck Mom":
                jump mom_xmas_fuck
            "Fuck Sidney":
                jump sidney_xmas_fuck
            "Cum" if mom_first_xmas_fuck == True and sidney_first_xmas_fuck == True:
                jump xmas_facial

label xmas_facial:
    stop sound
    scene bg SChristmas37
    with fade
    M "Ok, baby!.... Drench us in your baby gravy!"
    S "Spray me first!"
    L "No, me first!"
    R "Mom always gets to go first"
    R "Ohhhh.... here I cummmm!!!..."
    play sound Ejaculate
    scene bg SChristmas38
    with dissolve
    with hpunch
    with vpunch
    $ renpy.pause ()
    play sound Ejaculate
    scene bg SChristmas39
    with dissolve
    with hpunch
    with vpunch
    $ renpy.pause ()
    play sound Ejaculate
    scene bg SChristmas40
    with dissolve
    with hpunch
    with vpunch
    $ renpy.pause ()
    scene bg SChristmas41
    with dissolve
    M "Good job my big boy!"
    S "I just wish you'd covered me even more."
    L "Yeah.... usually you cum almost twice this much."
    RT "{i}Is she fucking kidding me?{/i}"
    RT "{i}I've never cum so much in my life.{/i}"
    M "Now, are you ready to watch us make out, and lick all of this cum off each other?"
    R "Oh God, yes!"
    S "Then we can grab the dildos and really get down to business!"
    L "Yay! A whole day of fucking!.... I love Christmas!"
    GF "Sorry buddy, but you won't get to do any of that. Our time is up in 5.... 4..."
    RT "{i}Noooo!.... Not yet!....{/i}"
    GF "3.... 2..."
    RT "{i}Goodbye, my beauties! We'll continue this in the future!{/i}"
    GF "1.... 0..."
    play sound Twinkle
    scene bg SChristmas42
    with dissolve
    $ renpy.pause ()
    scene bg SChristmas43
    with dissolve
    $ renpy.pause ()
    $ persistent.gal_harem_2 = True
    $ christmas_complete = True
    play music WeWishYou
    scene bg SleepBlack
    with fade
    $ renpy.pause ()
    jump xmas_goodbye

############  KITCHEN  ################################  KITCHEN  #####################################################  KITCHEN  ##############################################################  KITCHEN  ###########################################################  KITCHEN  #############################################################  KITCHEN  ##########################################

label cookies_in_oven:
    scene bg SChristmas18
    with fade
    R "Oh, man! Look how Lauren's dressing now, just to do something as casual as making cookies."
    if first_xmas_ntr:
        R "At least this future isn't completely bad."
    else:
        R "I'm really liking this future so far."
    R "Good morning Lauren! Are the cookies ready yet?"
    L "Good morning [ryan]! Merry Christmas! I'm just getting the cookies in the oven, so they're going to be a few minutes."
    scene bg SChristmas19
    with dissolve
    L "Ok.... I'll set the timer for twelve minutes."
    scene bg SChristmas20
    with dissolve
    L "Wow, cooking makes me get so hot when I'm like this!"
    RT "{i}No.... Fucking.... way!{/i}"
    play sound Twinkle
    scene bg SChristmas21
    with dissolve
    GF "Hahaha.... unbelievable!"
    RT "{i}You're telling me!{/i}"
    RT "{i}I've.... I've got to be the father of this one, I'm sure!{/i}"
    GF "Ohhhh.... I don't know.... I'd tread lightly here."
    scene bg SChristmas20
    with dissolve
    R "So.... hey, Lauren!"
    L "Yeah?..."
    R "What was the due date for your baby again?"
    scene bg SChristmas22
    with dissolve
    L "Hmmmmm.... It's January 23rd, so I've got about a month left of being pregnant!"
    L "Thank God.... I can't wait to get this thing out of me."
    L "But I guess I can't complain too much.... look!"
    scene bg SChristmas23
    with dissolve
    L "My tits have gotten even bigger in the last couple days."
    L "Remember when they looked like swollen mosquito bites?"
    R "Uhhh.... haha.... yeah.... It feels like yesterday."
    scene bg SChristmas24
    with dissolve
    L "Hhhhnnnnnn.... I just hope.... they get big enough to provide an entire meal for the baby."
    R "Do you want some help there?"
    L "hhnnn.... no.... I've got this."
    scene bg SChristmas27
    with dissolve
    L "There.... I made it up!"
    R "Wow! What a great accomplishment!"
    L "Haha.... you smart ass!"
    L "I hate these tall chairs now."
    R "So, have we settled on any names for the baby yet?"
    scene bg SChristmas25
    with dissolve
    L "Yeah.... remember? We talked about this."
    R "Yeah, just refresh my memory."
    L "If it's a boy, we'll name him [ryan], and if it's a girl, we'll name her after Mom."
    R "So [ryan].... after his..."
    if second_xmas_ntr:
        L "Uncle.... you weirdo."
        GF "Haha.... that was smooth!"
        R "His uncle? You mean I'm not the?..."
        scene bg SChristmas26
        with dissolve
        L "[ryan]! What the hell is wrong with you?"
        L "Did you fall off your scooter and hit your head, or something?"
        R "I'm sorry.... just remind me.... who's the father of your baby?"
        GF "Well, that went from smooth to cringy in just a few seconds."
        L "Is this because you're still angry at Agent Diaz?"
        R "What does Diaz have to do with any of this?"
        L "You know you've always been sore that we didn't let you father our child."
        R "Our child.... you mean that you and Diaz are.... together?"
        scene bg SChristmas27
        with dissolve
        L "Yep! We've been married for three weeks now."
        L "You were one of the witnesses."
        L "Ohh.... this is some kind of joke or game isn't it."
        R "Uhhh.... kind of.... I'm actually.... trying to document all of the important events that happened this year."
        R "You know, so we won't forget them in the future. I know a lot has happened to us these last couple years."
        R "So, if I ask you something that sounds like I should already know, just remember it's for the record."
        R "Here.... I'm recording you on my phone. Now will you please state for the record, how you got pregnant."
        R "And please give all the details."
        scene bg SChristmas25
        with dissolve
        L "Well.... agent Diaz wanted our baby to have half of her genetics. So, we were going to have her brother fertilize one of my eggs."
        L "You refused to pay for the treatment, so we did it the cheap and dirty way."
        L "So, I fucked her older brother every day for two months..."
        GF "Oooohhhhh..."
        R "What?!.... Are you serious!?"
        R "And I was ok with this?"
        L "Well, we didn't ask you."
        L "So, when her older brother couldn't knock me up, we let her younger brother give it a try."
        L "A few months later, and still no baby."
        L "So, Diaz's father volunteered to knock me up."
        scene bg SChristmas27
        with dissolve
        L "So, I fucked him for a while."
        L "And for good measure I kept fucking her brothers too. Sometimes all of them at the same time."
        L "And so I wouldn't feel too awkward, Agent Diaz would join us sometimes."
        R "Holy shit!"
        scene bg SChristmas26
        with dissolve
        L "Is this detailed enough for you?"
        R "Yeah, just skip to the part where you got pregnant."
        L "Well, there's not much more to the story."
        L "Eventually one of them slipped one past the goalie, and now I'm pregnant with one of their babies."
        R "And you don't even know which one of them got you pregnant?"
        L "It doesn't matter. It's Agent Diaz's and my baby not theirs."
        R "You guys are married, and you still call her Agent Diaz?"
        L "Well, yeah! It's respectful. I call her by her first name when we're in our apartment."
        R "So, what is her first name?"
        scene bg SChristmas25
        with dissolve
        L "I've already told you several times. If you can't remember, you're on your own."
        R "This is for the record."
        L "well then state it for the record yourself."
        R "Ok.... never mind."
        R "Are you screwing anybody else?"
        L "Of course not!.... I only screwed Agent Diaz's brothers and father to get pregnant."
        L "Although, to be totally honest, I'm still screwing them, so that their swimmers will still be strong when we're ready for baby number two."
        R "That doesn't make any sense."
        L "Yeah it does. It makes perfect sense. I'll just have Agent Diaz explain it to you, the same way she explained it to me. You'll see."
        GF "Holy shit! I thought you were the DaVinci of bullshit, but you're just a toddler compared with her!"
        RT "{i}No shit!.... Once I go back to the present, I've got to remember to get that toxic woman out of our lives.{/i}"
        RT "{i}What the hell? Screwing the entire Diaz family?.... I'm pretty sure she's still a virgin in the present.... hmmmm.... I wonder if....{/i}"
        R "So.... since you got married. Are we ever.... you know..."
        L "Intimate?"
        R "Yeah."
        L "Oh.... of course! Diaz knows I would have never married her if she tried to take away what we have."
        L "And I know you enjoy it when Diaz joins in."
        L "Although I'm pretty sure you just like to hate fuck her."
        GF "No wonder!"
        scene bg SChristmas27
        with dissolve
        L "She told me to tell you that if you ever fuck her ass that hard again, she's going to have an FBI drug dog bite your cock off."
        GF "Well, at least you have that perk."
        R "But if.... we're intimate.... how can you be sure the baby's not mine?"
        L "Because we made you wear a condom until I was pregnant."
        L "So, unless you were poking holes in the condom."
        L "And I warn you that you better not have!"
        L "If Agent Diaz suspects that child isn't half hers, she'll do a DNA test, and if you're the father, she'll deport both of you to Cuba."
        GF "Agent Diaz makes the Mafia look like the boy scouts."
        "DING"
        L "Oh, there goes the cookies. Why don't you run and see if Sidney's almost ready for the gift exchange, and I'll get the cookies ready, and bring them out when I'm done."
        R "Yeah, ok."
        scene bg SChristmas24
        with dissolve
        L "Ohhh.... these stupid, tall chairs!"
        L "And where did I throw that apron?.... Baking in the buff is not a good idea."
        RT "{i}Shit!.... I can't even believe what Lauren just told me!{/i}"
        RT "{i}How am I going to get rid of that woman, before she can do that much damage? She's got my balls in a vice as it is! I've got to search for some kind of opportunity.{/i}"
        GF "Or at least help Lauren see how evil she is."
        scene bg SChristmas19
        with dissolve
        RT "{i}That's definitely something from the future that has to change!{/i}"
        GF "Yeah that sucks!.... Should we go see what the damage is with Sidney?"
        scene bg SChristmas20
        with dissolve
        RT "{i}Yeah, although at this point, I'm almost afraid to ask.{/i}"
        scene bg SleepBlack
        with fade
        jump sidney_prego_too
    else:
        L "Father, you weirdo!"
        GF "Haha.... that was pretty smooth."
        RT "{i}Thanks.{/i}"
        R "And are you ok with getting pregnant from your brother?"
        L "[ryan]!.... We've already talked about this!"
        L "Is this some kind of trick, or Christmas game?"
        R "Uhhh.... kind of.... I'm actually.... trying to document all of the important events that happened this year."
        R "You know, so we won't forget them in the future. I know a lot has happened to us these last couple years."
        R "So, if I ask you something that sounds like I should already know, just remember it's for the record."
        R "Here.... I'm recording you on my phone. Now will you please state for the record, the story of your pregnancy."
        L "Well, it's not much of a story."
        L "I just kept falling more and more in love with you, as I watched you work so hard to take care of us."
        L "Even though at any point, you could have done the easy thing, and left us to care for ourselves."
        scene bg SChristmas27
        with dissolve
        L "But I think the moment I was head over heels for you, was when you finally were able to get Agent Diaz off our backs, or I guess out of my pants in my case."
        R "Ooohhh, that sounds like a good story!.... Why don't you tell me about that!.... For the record."
        L "You already know the story!.... And I'm pretty sure we don't want that on any kind of record."
        L "You know.... Incriminating evidence and that sort of thing."
        RT "{i}Damn!{/i}"
        RT "{i}It sure would be helpful to know how I'm going to finally nail that bitch!{/i}"
        GF "Well, it looks like you were able to figure it out on your own, so when you go back to the present, just keep an eye out for that opportunity."
        L "But I'm so glad you let me be part of her weekly punishment."
        scene bg SChristmas25
        with dissolve
        L "I know this sounds cruel, but I love humiliating that bitch every week!"
        RT "{i}Oh.... I want to know so bad!{/i}"
        R "So, did you get pregnant on purpose?"
        L "No.... but when you fuck as often as we do, we were bound to slip up one of those times."
        scene bg SChristmas27
        with dissolve
        L "When it happened though, It just made me happy!"
        L "And I'm so glad that you're ok with being a daddy!"
        if first_xmas_ntr == False:
            R "How do you feel about the fact that I got Mom pregnant too?"
            scene bg SChristmas26
            with dissolve
            L "You know I'm fine with it!"
            L "Kind of happy even."
            scene bg SChristmas27
            with dissolve
        else:
            R "Hypothetically, would it bother you if I shared my affection with another?"
            scene bg SChristmas27
            with dissolve
            L "Haha.... \"Hypothetical\", my ass!"
            L "You know, that I know, that you're intimate with Mom and Sidney."
        L "You work so hard for all of us, and it's only natural that we all have those kinds of feelings towards you."
        L "And you deserve to receive all of our thanks for your dedication to us."
        GF "You sir, are the Ernest Hemingway of bullshit and manipulation. My Santa hat is off to you!"
        "DING"
        L "Oh, there goes the cookies. Why don't you run and see if Sidney's almost ready for the gift exchange, and I'll get the cookies ready, and bring them out when I'm done."
        R "Yeah, ok."
        scene bg SChristmas24
        with dissolve
        L "Ohhh.... these stupid, tall chairs!"
        L "And where did I throw that apron?.... Baking in the buff is not a good idea."
        if first_xmas_ntr == False:
            RT "{i}I don't know how I feel about taking care of two babies, but so far, this future is looking pretty awesome.{/i}"
        else:
            RT "{i}I'm not super excited about Mom being pregnant by Dad, but so far this future doesn't seem too bad.{/i}"
        GF "Yeah, and if you're not super jazzed about taking care of babies, you can always just get a vasectomy when you're back to the present."
        GF "Should we go see what the damage is with Sidney?"
        scene bg SChristmas19
        with dissolve
        RT "{i}Yeah, I wonder what my future has in store with her.{/i}"
        scene bg SleepBlack
        with fade
        jump sidney_prego_too

###########################  WAREHOUSE  ###############################################################  WAREHOUSE  ############################################################################  WAREHOUSE  ####################################################################  WAREHOUSE  ############################################################################  WAREHOUSE  ##########

label christmas_shoot:
    scene bg LChristmas11
    with fade
    scene bg LChristmas12
    with dissolve
    $ renpy.pause ()
    play sound Twinkle
    scene bg LChristmas13
    with dissolve
    R "Aaahhh..."
    scene bg LChristmas14
    with dissolve
    R "Ooofff.... "
    GCP "Oh, no!.... Not again!"
    scene bg LChristmas15
    with fade
    GCP "That's so embarrassing!"
    GCP "I'm so sorry! I didn't mean to."
    R "Are you sure the Ghost of Christmas Past didn't put you up to it?"
    GCP "Haha.... no, but I'm sure it will help cheer her up when I tell her."
    R "This is my photo studio.... what are we doing here?"
    GCP "That's a good question. Why on earth would you make your sisters do a photo shoot on Christmas Eve?"
    R "Uhhhh.... well.... I don't have any plans for a photo shoot as of right now.... but, Christmas is coming really soon..."
    R "That's not a bad idea! There's just enough time for Sidney to make some sexy Christmas costumes."
    R "And if I post them on Christmas Eve night, They'll pick up tons of fans and likes!"
    R "Are you sure we're not doing this photo shoot because you gave me the idea?"
    GCP "Of course not!.... I don't think..."
    GCP "But anyways, it's a bad idea!"
    GCP "And I want you to see how much they resent you for it."
    GCP "And how much they resent you for making them show off their bodies for money."
    R "How will you be able to show me that?"
    GCP "I'm giving you the power to read their thoughts."
    R "What?.... That's awesome!"
    GCP "It will only work while we're here in the \"Christmas Present\". And we'll only be here a very short while."
    GCP "And you may not enjoy it as much as you think, once you hear how your sisters really feel towards you, and your slimy manipulations."
    GCP "After you hear how they feel about you, you should send them home, instead of making them do the photo shoot."
    GCP "I think once you hear how happy that will make them, you'll have a stronger desire to treat them, and their bodies, with respect."
    R "Alright.... well let's see what happens."
    S "Who are you talking too?"
    scene bg LChristmas16
    with dissolve
    L "Were you just talking to yourself?"
    scene bg LChristmas17
    with dissolve
    R "Ummmm.... yeah, I do that every once in a while to organize my thoughts..."
    ST "{i}Yep.... what a simple-minded idiot!{/i}"
    R "What did you call me?"
    S "Huh?.... I didn't call you anything!"
    GCP "[ryan]! She just thought that, she didn't actually say it, you simple-minded idiot!"
    RT "{i}Oh right!.... Whoops!{/i}"
    R "Uhhh.... never mind."
    R "You girls look incredible by the way!"
    scene bg LChristmas18
    with dissolve
    R "Sidney, you never fail to amaze me!"
    LT "{i}Ohh.... that's sweet.... except for the fact that he's ogling us like a creep.{/i}"
    S "Thanks, These were actually pretty technical. The stitching took forever!"
    S "I should have charged you more than the $1,500 dollars you gave me."
    R "(Cough).... excuse me? How much?"
    S "$1,500! You remember!.... You made almost as big a deal of it as you are now."
    ST "{i}I know that cheapskate's making more money off of us then he's telling us, and he's still complaining every time I tell him the price of an outfit!{/i}"
    ST "{i}I can tell he doesn't trust or appreciate me.{/i}"
    RT "{i}She's right.... I do make a big deal every time I have to pay for an outfit. I need to change that.{/i}"
    R "I'm sorry, Sidney. I shouldn't have made such a big deal about that.... looking at you both in these outfits, I realize they were worth every penny."
    scene bg LChristmas19
    with dissolve
    GCP "Aaahhhh.... that was really sweet! This is going so well already! The Ghost of Christmas Past is going to be so jealous!"
    scene bg LChristmas18
    with dissolve
    S "Thanks [ryan]! It's always nice to get some appreciation."
    scene bg LChristmas17
    ST "{i}It's almost like he read my mind!{/i}"
    GCP "Yeah.... be careful.... If you always talk about what they are thinking, they'll get pretty weirded out."
    L "So, can we get this photoshoot done?"
    L "I want to get this over with, so I can get that Hard'n'long gift card you promised me."
    L "I've got a ton of Christmas shopping I need to do."
    LT "{i}Only fucking reason he could get me here on Christmas Eve, I hate how he uses money to control us.{/i}"
    RT "{i}Wow! You're right! They really do have a lot of negative feelings towards me.{/i}"
    GCP "Yep. I told ya. Now all you have to do is give them the day off, and for good measure, you could throw in those gift cards as Christmas gifts."
    GCP "You'll see how much better they think of you, and that should make you want to stop exploiting them."
    RT "{i}Alright, I'll give it a try.{/i}"
    RT "..."
    R "Uhh.... I've actually been thinking."
    R "Asking you to come in on Christmas Eve wasn't very cool of me."
    R "Christmas only comes once a year, and I manipulated you into spending it with me, at work."
    R "Why don't you take the day off, and you can even have those gift cards I promised you as a gift, instead of as a wage for today's work."
    scene bg LChristmas19
    with dissolve
    $ renpy.pause ()
    scene bg LChristmas18
    with dissolve
    L "Wow, [ryan]! That's so sweet of you!"
    LT "{i}Maybe I should think better of him. He really is trying his best to be a good brother. Plus, he has all the responsibility of providing for us.{/i}"
    scene bg LChristmas16
    with fade
    S "Yeah, [ryan]! That's amazing of you!"
    ST "{i}Well, I can't let this outfit go to waste.... I know.... I can wear it for [ryan] tonight in bed.{/i}"
    RT "{i}Oh my.... spirit?.... Can I please see that part of the \"Christmas Present\" timeline?{/i}"
    GCP "No you cannot! What a hussy! No wonder you're struggling so much with this!"
    play sound MetalDoor
    scene bg LChristmas20
    with fade
    L "Oh, shit! It's Agent Diaz!.... What is she doing here?"
    R "Yeah, what the fuck?"
    GCP "Who's Agent Diaz? I didn't see her named in my file."
    RT "{i}She's an FBI agent that has been extorting us for money.{/i}"
    RT "{i}I think I've learned my lesson. Can we just disappear now?{/i}"
    GCP "No.... remember. Just like in the past, We're stuck here for a certain amount of time."
    GCP "Let's hurry and head her off before she ruins everything I've taught you here."
    R "..."
    GCP "Run!"
    scene bg LChristmas21
    with fade
    $ renpy.pause ()
    scene bg LChristmas23
    with fade
    R "(breathing heavily) What are you doing here?"
    AD "Now that's not a very nice way to greet me!"
    R "Sorry!.... What the hell are you doing here.... ma'am."
    AD "Well, I came by the house for my usual payoff, and found that everyone was gone."
    R "Shit! It's Thursday?.... But it's Christmas Eve!"
    AD "Yeah, and I wanted my present. So, I tracked you here."
    R "How!?"
    AD "I work for the FBI.... I know a hundred ways to track you."
    AD "And I'm so glad I did!"
    scene bg LChristmas22
    with dissolve
    AD "Now I get to see where the magic happens."
    GCP "Get rid of her!"
    R "Uhhh.... I suppose you want your money."
    AD "Actually, there's something I want even more than my money."
    AD "If you'll let me be the director and photographer of your photo shoot, you won't have to pay me for this week, or next week."
    "{i}\"Offer only valid in the Christmas present.\"{/i}"
    AD "So, what do you say?"
    GCP "Pay her, and get her out of here!"
    RT "{i}Why is she making you so nervous?{/i}"
    GCP "Because she's an unknown entity. I have no idea what will happen if she meddles."
    menu:
        "Pay Diaz.":
            R "Yeah, I don't think so! Here's the $500, and why don't you take your broom and fly away."
            scene bg LChristmas23
            with dissolve
            AD "Fine!.... But make sure you're home next week! If I have to track you down again, I'm going to be taking both forms of payment."
            GCP "Good job! Now let's go give the girls their gift cards, and we'll call today a success!"
            scene bg LChristmas24
            with dissolve
            S "What's going on, [ryan]?"
            S "Is she gone?"
            R "Yeah.... you know, it was just some woman looking for her cat."
            scene bg LChristmas25
            S "You don't have to lie.... Lauren just told me what's going on."
            R "You told her?"
            L "Well, not everything, but most of it."
            R "Did you tell her what happens when I don't have enough money to pay her?"
            L "Yeah.... well, not all the details."
            LT "{i}I didn't tell her that I'm mostly scared that I kind of like it.{/i}"
            RT "{i}Whoa! What was that?{/i}"
            GCP "Yeah.... all of you are a bunch of deviants."
            S "That disgusting old sleaze hole!"
            R "Well, the good news is that I paid her, and now I can give you these gift cards, and we can all go enjoy the Christmas holiday."
            GCP "Yay!"
            S "Yeah.... I don't think so."
            GCP "Wait, what?"
            S "I'm sorry [ryan].... I had no idea you had this added pressure on you, on top of everything else you're trying to do to keep a roof over our heads."
            ST "{i}Now that's a real man!{/i}"
            RT "{i}That's so nice!{/i}"
            ST "{i}Even if he doesn't look like it.{/i}"
            RT "{i}Ouch!{/i}"
            GCP "No! This can't be happening."
            S "We're going to do the photo shoot!"
            S "I know it has the potential to bring in a lot of money, and I want to help you out by doing my part."
            S "Are you in, Lauren?"
            L "Yeah, and I think we can make it fun!"
            S "We'll think of a good pose to start with."
            scene bg LChristmas39
            with dissolve
            LT "{i}It's not everyday I get to spend time with my sister. At least not dressed like total sluts. Damn, she looks hot!{/i}"
            GCP "You degenerates!"
            RT "{i}What's the matter? This is awesome! They now love and respect me more, and they're going to do the photo shoot without having to be manipulated.{/i}"
            RT "{i}Isn't this what you wanted?{/i}"
            scene bg LChristmas38
            with dissolve
            GCP "No!.... I wanted you to see the error of your ways, and stop taking sexy pictures of your sisters!"
            RT "But why? They're into it now. They're fully consenting adults."
            GCP "I've had it with your family!"
            GCP "I'm going to see if I can pillage some liquor from the bar down the street!"
            GCP "I'll be back when it's time to go."
            scene bg LChristmas39
            with dissolve
            RT "{i}Shoot! I made another ghost disappointed.{/i}"
            scene bg LChristmas28
            with dissolve
            L "So, are you ready to shoot us in sexy poses?"
            S "And how's this for a first pose?"
            R "Great! I like the buddy-buddy pose."
            R "That will make a great first pic."
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            scene bg LChristmas28
            R "I think I'll add a homey Christmas background."
            scene bg BlurryWhite
            with fade
            scene bg LChristmas29
            with fade
            R "I can see it all now!"
            RT "..."
            R "Ok.... now I want you to do some Christmassy things."
            L "I can make it look like I'm hanging Christmas tree ornaments."
            S "And I'll make it look like I'm hanging stockings."
            R "Sounds good, but do it in a sexy way."
            L "Well, duh..."
            scene bg LChristmas30
            with dissolve
            R "Nice! That looks super sexy!"
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            scene bg LChristmas30
            R "Beautiful!"
            LT "{i}It's kind of fun posing with my sister.{/i}"
            ST "{i}My sister looks sexy as hell in that costume I made for her.{/i}"
            RT "{i}This is awesome! I wish I could read minds all the time.{/i}"
            R "Ok.... moving on.... I think I see some prop presents against the wall."
            R "Let's do a scene with you opening them"
            S "Those aren't actually props. Sidney and I decided to give each other our Christmas presents early, since, well.... at least my present isn't appropriate to open under the tree in front of Mom."
            L "Haha, yeah.... mine isn't, either."
            R "Do you guys mind opening them now, for the photo shoot?"
            S "No, we don't mind."
            R "Geat! Run and grab them, and then get into a good pose."
            scene bg SleepBlack
            with fade
            scene bg LChristmas31
            with fade
            R "You two are becoming naturals at this."
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            scene bg LChristmas31
            R "Once you get them open, show each other what you got."
            scene bg LChristmas32
            with dissolve
            S "Haha.... I can't believe we got each other the same thing!"
            L "Yeah.... just different colors!"
            R "I guess horny minds think alike."
            R "This is great! The natural reaction makes an even better picture than if you girls were acting!"
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            scene bg LChristmas32
            ST "{i}I can't wait to get home and try it.{/i}"
            LT "{i}I wish I could try this right now!{/i}"
            R "Alright.... why don't you thank each other with a passionate kiss."
            scene bg LChristmas33
            with dissolve
            S "What!?..."
            R "For the photo shoot!"
            R "Not for real."
            R "You don't actually have to make out."
            R "Just make it look like you are."
            L "But we're sisters!"
            R "Yeah, well, none of your online fans know that. And even if they did, it would just make you two even more popular."
            RT "{i}Maybe I should put that in their bios.{/i}"
            R "If you want to learn to be good models, you'll have to learn to go outside your comfort zones a little."
            S "Uhhh.... this is outside a lot!"
            LT "{i}Oh my God! Will Sidney agree to do this with me? Why am I getting butterflies in my pussy when I think about it?{/i}"
            L "Come on Sidney, Let's just get it over with."
            S "Fine!"
            R "Lauren, why don't you just straddle Sidney and..."
            scene bg LChristmas34
            with dissolve
            R "Oh, yeah.... that's perfect!"
            R "Wow! That's pretty hot!"
            S "Just hurry up and take the picture!"
            scene bg LChristmas35
            with fade
            ST "{i}Before my pussy betrays me and leaves a puddle on the floor!{/i}"
            ST "{i}This is so wrong!{/i}"
            ST "{i}Why is it making my pussy tingle so much?{/i}"
            LT "{i}Why does this turn me on so bad?{/i}"
            LT "{i}I've already been having confusing thoughts about women, but now I'm getting turned on by my sister?{/i}"
            LT "{i}God, I hope I don't drip all over her lap.{/i}"
            LT "{i}I can't believe she made a costume that doesn't include panties.{/i}"
            RT "{i}Wow! They're kind of into each other.{/i}"
            RT "{i}It sounds like they just need a little persuading.{/i}"
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            scene bg LChristmas35
            R "I think we're ready for the next pose."
            $ renpy.pause ()
            R "Unless you want to keep kissing, but I'm thinking we should take a few shots with you playing with your new toys."
            scene bg LChristmas36
            with dissolve
            S "Play with our..."
            L "(Gulp) Toys?..."
            S "How do you mean?"
            LT "{i}Oh my.... he wants us to dildo each other.... shit!.... I think I just dripped onto Sidney's leg!{/i}"
            LT "{i}I hope she doesn't notice.{/i}"
            ST "{i}Holy shit!.... I think Lauren just leaked onto my leg!.... Does the thought of us playing with toys together get her excited?{/i}"
            R "Haha.... I'm not expecting you to screw each other with your new dildos."
            RT "{i}These girls are going to make me nut in my pants!{/i}"
            R "Just get into a position so it looks like Sidney is penetrating Lauren with the dildo."
            R "But you won't actually penetrate."
            R "Just make it look like it."
            R "Unless you want to keep making out!"
            LT "{i}I kind of do.{/i}"
            S "Uuuhhh.... ok Lauren.... let's.... get.... into position."
            scene bg LChristmas37
            with fade
            play music SexMusic
            S "Does this look ok?"
            R "Yeah, that's pretty convincing."
            R "Let me get a quick shot of it."
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            scene bg LChristmas37
            R "Great! Now move the dildo a little closer."
            R "And if Lauren's ok with it, just kind of prod and push the dildo between her thigh gap."
            R "From my perspective, it should look pretty convincing."
            scene bg LChristmas41
            with fade
            ST "{i}Hmmmm.... I think I should use this opportunity to tease Lauren.{/i}"
            ST "{i}After all, she did let her pussy leak her naughty juices all over my leg.{/i}"
            RT "{i}Oh, no way!.... I always thought Sidney was too much of a prude to do anything like that to her own sister!{/i}"
            RT "{i}I wonder what she'll do to her.{/i}"
            scene LChristmasMovie01
            with fade
            LT "{i}Oh.... my.... God!....{/i}"
            LT "{i}What the hell is Sidney thinking?{/i}"
            LT "{i}Where does she get the balls to do this to her own sister?{/i}"
            LT "{i}Keep quiet.... not a sound.... that would be so embarassing if [ryan] knew!{/i}"
            scene bg LChristmas41
            with fade
            ST "{i}Haha.... look at her squirm.... this is driving her crazy!{/i}"
            RT "{i}Damn, from this angle I can't see what she's doing.{/i}"
            scene LChristmasMovie01
            with fade
            RT "{i}I can only imagine what's going on back there.{/i}"
            scene bg LChristmas42
            LT "{i}Why does it feel so much better when Sidney does that to me, then when I do it to myself?{/i}"
            LT "{i}It's really starting to feel good!{/i}"
            scene bg LChristmas43
            LT "{i}Oh God!.... This is driving me crazy!.... What if that ho gives me an orgasm, right here in front of [ryan]?{/i}"
            S "(whispering) This is what you get for dripping your dirty juices all over my leg."
            L "(whispering) Oh my God.... you.... noticed that?"
            S "(whispering) Yes, I noticed that!.... And now I'm going to do this until [ryan] tells me to stop."
            RT "{i}Whatever Sidney is doing to Lauren, I should let it continue for a little while.{/i}"
            R "Can you girls keep holding that pose for a bit? There's something funny going on with this camera, just hold that until I get it working."
            scene LChristmasMovie01
            with fade
            LT "{i}You've got to be kidding me!{/i}"
            S "(whispering) Oh my God Sidney!.... Today is your lucky day."
            L "(whispering) You're so mean today!"
            S "(whispering) I'll bet your slutty little pussy wishes I'd go further in, doesn't it?"
            L "(whispering) Nnnn....nnoo...that's disgusting!"
            L "(whispering) I.... I don't.... want my own sister.... to fuck my pussy!"
            S "(whispering) You don't sound very convincing."
            scene bg LChristmas43
            L "(whispering) When did you become such a pervert?"
            S "(whispering) hmmm.... well.... lately there's been some things going on, that have opened me up to be a little more sexually adventurous."
            ST "{i}Thank you [ryan].{/i}"
            L "(whispering) You mean like molesting me in my sleep?"
            L "Did you do that on purpose!?"
            S "Ssshhhh.... (whispering loudly) Of course I didn't."
            S "(whispering) But it did start a chain of events that brought me to where I am now."
            S "(whispering) Maybe I'll tell you some day."
            S "(whispering) Maybe it would help you be a little more adventurous."
            LT "{i}She has no idea!{/i}"
            LT "{i}She would probably think I'm such a dirty pervert if she knew that I've been dry humping my own brother.{/i}"
            LT "{i}Oh I wish it was his cock rubbing against my pussy!{/i}"
            RT "{i}Holy shit!.... If this isn't a dream, I could really ramp things up between the two of them.{/i}"
            RT "{i}But how will I ever be sure?{/i}"
            L "(whispering loudly) Aaahhhhh.... Fuck you, Sidney.... you're driving me completely crazy! Just fuck my pussy already!"
            stop music
            play sound Scratch
            scene bg LChristmas44
            with fade
            $ renpy.pause ()
            play music SexMusic
            S "(whispering) Are you fucking kidding me?"
            L "(whispering) No.... you ho! You started this."
            L "(whispering) I'm literally dying with lust right now!"
            S "(whispering) Is it really turning you on that bad to have your sister rub your pussy?"
            L "(whispering) Well, obviously I'm thinking of someone else while you're doing that."
            LT "{i} Like my brother's cock.... shit!.... That feels sooo wrong when I think those things!.... So why does it turn me on so bad?{/i}"
            L "(whispering) I will admit, having you do this to me, right in front of [ryan], and he has no idea, is making this so much hotter!"
            S "(whispering) Aren't you worried that he'll notice?"
            L "(whispering) No.... he'll think you're just sliding it between my thighs like he suggested.... plus he's got all his attention focused on his camera right now."
            S "(whispering) Alright.... you asked for it!"
            scene bg LChristmas45
            with dissolve
            $ renpy.pause ()
            scene LChristmasMovie02
            with fade
            L "Oh, my fuck!..."
            R "Are you ok over there?"
            S "(whispering loudly) Lauren!.... What the fuck?"
            L "Yeah.... I'm.... ok.... I think I just.... kneeled on a.... pebble."
            R "Ok good!.... I'm glad that's all it is."
            R "I'll be done with the camera soon. Just hang on a little longer!"
            RT "{i}Holy Futa God!.... Sidney penetrated Lauren before I got to!{/i}"
            RT "{i}I'm kind of jealous!{/i}"
            RT "{i}But at the same time.... that's pretty fucking hot!{/i}"
            scene bg LChristmas46
            with fade
            LT "{i}Holy fuck!.... My sister is fucking me.... right in front of my brother.... and he has no idea!....{/i}" #l_xmas_5
            RT "{i}Well, maybe more than you think.{/i}"
            LT "{i}I've never been more turned on in my life!{/i}"
            LT "{i}Oh....no.... what if I cum?.... It will be so obvious if I squirt all over the green screen!{/i}"
            LT "{i}Fuck!.... What will.... [ryan] think?....{/i}"
            scene LChristmasMovie02
            with fade
            LT "{i}I can't believe Sidney is into this!.... Now we have a secret together.{/i}"
            LT "{i}Now we can do some real sisterly bonding in the future!{/i}"
            LT "{i}I wonder if she'll be up for using Mr. Snuggles' strap-on?{/i}"
            LT "{i}Fuck!.... I can just imagine her pounding me from behind!{/i}"
            scene bg LChristmas45
            with fade
            ST "{i}Why am I enjoying this so much?{/i}"
            ST "{i}It's not like it's my pussy that's getting all the attention.{/i}"
            ST "{i}Good God!.... I can't believe this is happening!{/i}"
            ST "{i}One day I'm sucking my brother's dick, and the next day I'm pounding my sister's pussy!{/i}"
            scene bg LChristmas60
            with dissolve
            ST "{i}This is so bad!{/i}"
            ST "{i}I'm not supposed to be turned on by my siblings!{/i}"
            ST "{i}What's next? Fantasies about my mom?{/i}"
            ST "{i}Shit, Sidney!.... Don't even go there!{/i}"
            ST "{i}With her perfect ass and titties!{/i}"
            scene bg LChristmas45
            with dissolve
            ST "{i}Aaahhh.... maybe I should just embrace my perversions.{/i}"
            ST "{i}[ryan] doesn't seem to follow any kind of code of ethics.{/i}"
            RT "{i}Ouch!.... Yeah.... I kind of let those ethics die the night I saw Mom at the club.... and started letting my cock do all my thinking.{/i}"
            scene LChristmasMovie02
            with fade
            RT "{i}Maybe poor self control is a weakness in our genetics.{/i}"
            RT "{i}Hmmmm.... maybe a weakness that I can take advantage of.{/i}"
            $ renpy.pause ()
            LT "{i}Fuck.... Fuck.... Fuck.... Fuck....{/i}"
            LT "{i}I'm getting sooo close!{/i}"
            scene bg LChristmas46
            LT "{i}Fuck.... Fuck.... Fuck.... Fuck....{/i}"
            LT "{i}What am I going to do?{/i}"
            LT "{i}I can't control if I squirt or not!{/i}"
            LT "{i}And as turned on as I am, it's basically a sure thing!{/i}"
            RT "{i}I should stop her before she makes a mess!.... Plus if she's not allowed a release, maybe she'll be dying to do something with me later.{/i}"
            R "I got the camera working! Good job girls! That's a very convincing pose."
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            scene bg LChristmas46
            LT "{i}Fuck.... I was so close!{/i}"
            scene bg LChristmas43
            with dissolve
            LT "{i}Oh, thank God he stopped her!{/i}"
            LT "{i}As much as I wanted that.... that would have been a disaster.{/i}"
            scene bg LChristmas42
            with dissolve
            LT "{i}But now I really need to get off! How am I going to take care of this?{/i}"
            play music WeWishYou
            scene bg LChristmas57
            with fade
            R "You girls did really good today!"
            R "I think we need to have you two pose together more often."
            L "I'm all for it!"
            S "Yeah, that was kind of fun!"
            scene bg LChristmas56
            with dissolve
            S "(whispering) Lauren? Are you ok?.... I know you didn't get to satisfy your itch."
            scene bg LChristmas57
            with dissolve
            L "(whispering) No!.... I'm so horny right now!"
            RT "{i}I'll help her take care of that.{/i}"
            scene bg LChristmas56
            with dissolve
            S "(whispering) When we go to the storage shed to change, I'll finish what I started.... I can't leave my own sister in such pain."
            scene bg LChristmas58
            with dissolve
            L "(whispering) Oh my God!.... I have the best sister in the world.... I can't wait!"
            RT "{i}Shit! Sidney's taking over!{/i}"
            scene bg LChristmas57
            with dissolve
            R "Uhh.... Sidney, we're all done here.... you can run home. Lauren?.... Would you mind sticking around here and helping me clean up?"
            L "Sorry [ryan], but Sidney and I have plans to go shopping right now. Normally I'd stay and help, but we need to get our shopping done before all the stores close."
            L "I'm really sorry!"
            RT "{i}Yeah.... sure you are.... at least that storage shed has so many holes in it, it will be easy to spy on them.{/i}"
            R "Alright.... I understand. I'll take care of it myself. Go ahead and get changed."
            scene bg LChristmas59
            with dissolve
            "{i}\"Sound of girls giggling as they run off.\"{/i}"
            RT "{i}Dammit!.... Sidney cock-blocked me!{/i}"
            RT "{i}I'll give them just a second, and then I'm definitely spying on them.{/i}"
            play sound Twinkle
            scene bg LChristmas50
            with dissolve
            R "Ahh.... shit! You scared me!"
            R "Feeling any better?"
            GCP "Well, the alcohol has numbed me a little, but no, I'm still feeling pretty shitty."
            GCP "How were things while I was gone?"
            R "Oh, you know.... nothing eventful happened here."
            GCP "You don't have to lie to me. All your thoughts were so sexually charged, I could hear them all the way in the bar down the street."
            GCP "I have never failed so spectacularly in all the decades I've been doing this."
            GCP "I won't be gettin my wings anytime soon."
            GCP "Plus, God's definitely going to ream my tiny ass with her huge futa cock, when I get back."
            R "Oh, God!.... I'm so sorry!"
            R "But if it makes you feel better.... I learned a couple really valuable things."
            GCP "Oh?.... Like what?"
            R "I know that Sidney and Lauren are starting to think like me..."
            GCP "(sarcastically) Oh, wonderful."
            R "And I learned that I need to keep them from getting too intimate with each other right away, or they're going to cut me out of their sex lives."
            R "I think I need to work on getting each one of them attached to me more, before I bring them together."
            GCP "(sarcastically) What a treasure trove of moral lessons you've learned today."
            R "I really am sorry it didn't work out for you the way you wanted. But if you'll now excuse me. I've got a pretty hot event I need to go spy on."
            R "Haha.... yeah, you know what I'm talking about."
            GCP "Yeah, sorry about that, but you won't have time."
            R "What?"
            GCP "Yeah, it's about time to go."
            GCP "You can expect the third, and final ghost, when the clock strikes three."
            R "No, I don't want to go yet!.... And once again, we don't have a clock tower."
            GCP "In 5.... 4.... 3..."
            R "Nooooo!..."
            GCP "2.... 1..."
            play sound Twinkle
            scene bg SleepBlack
            with fade
            $ renpy.pause ()
            scene bg ChristmasEvent58
            with fade
            RT "{i}Oh Futa God.... I'm back in my bed?.... Another weird dream?{/i}"
            RT "{i}At least, I think they were dreams!{/i}"
            RT "{i}They were both just so vivid! Huh.... {/i}"
            RT "{i}I guess I'll have to wait till three o'clock to find out.{/i}"
            RT "{i}Ohhh.... so tired.... zzzzzzz....{/i}"
            scene bg SleepBlack
            with fade
            $ renpy.pause ()
            jump xmas_future
        "Shit! Did I leave my money at home? (NTR Warning!!)":
            R "Yeah, I don't think so! I'm going to pay you the $500, and then you can take your broom and fly away."
            scene bg LChristmas23
            with dissolve
            RT "{i}I'll just pull it out of my magic pockets.... shit!.... It's not working!{/i}"
            RT "{i}Ghost of Christmas Present! Why aren't my magic pockets working?{/i}"
            GCP "Magic Pockets?"
            RT "{i}Yeah, in the past, I could just think about what I needed, and then I could pull it out of my pockets.{/i}"
            GCP "Oh, right!"
            GCP "You see, each ghost has one magic trick. The Ghost of Christmas Past could make you produce anything you needed."
            GCP "But my magic trick is to let you read minds, so sorry! No magic pockets."
            GCP "But damn, I wish you had them. We need this bitch to leave!"
            R "Uhhh.... actually it seems that I don't have the money on me."
            scene bg LChristmas22
            with dissolve
            AD "So.... I guess I'll show myself in then."
            RT "{i}Shit!{/i}"
            GCP "Shit!"
            scene bg LChristmas24
            with fade
            R "Ummmm.... girls.... It seems that I forgot that I was bringing in an, ummm.... intern photography student.... who wants to help with the photo shoot today."
            "{i}\"Furiously winking at Lauren.\"{/i}"
            S "You don't have to lie to us. Lauren just told me everything."
            R "Everything?"
            scene bg LChristmas26
            with dissolve
            AD "Like how I'm extorting you for money and favors in exchange for letting you continue your legally questionable business and other activities, and also not throwing you in prison like your father?"
            AD "Is that what she told you?"
            S "Basically."
            AD "Great! I'm glad we're all up to speed."
            AD "And today is Thursday, and [ryan] failed to produce the needed cash for my buy off, so for my payment in favors, I get to take the pictures today instead."
            GCP "No! If this photo shoot takes place, then I'll fail my part of the mission too!"
            S "You can't do that!"
            GCP "Yeah!"
            AD "Oh, really? Because I happen to know that you make and get paid for costumes, as part of a business that is not in of itself illegal, but is hiding funds from the FBI to avoid garnishments."
            AD "Now, I can either keep this knowledge safe, and actually completely hide this illegal cash flow, or I can expose it, and you can do hard time in federal prison for financial fraud."
            S "You goddamn dirty cop!"
            GCP "You chode-munching, cock-gobbling, anal prolapse-licking, whore of Babylon!"
            RT "{i}Are you ok?{/i}"
            GCP "Uuuurrrggghhhh!!"
            AD "(sarcastically) Ouch.... I can't tell you how much that hurts."
            AD "So, are you all going to play ball?"
            S "I don't see another choice."
            AD "Good! I'm glad you're being sensible."
            AD "[ryan], give me the camera, and girls, go do a nice pose! And make these pics good, or else!"
            scene bg LChristmas27
            with dissolve
            AD "Girls?.... While I'm figuring out this camera, run to my car and grab the two gifts in the back seat. They were for a couple of my girl friends, but I think we can make better use of them during the photo shoot."
            L "{i}I hate this bitch!{/i}"
            GCP "I wish God was as vengeful to the wicked as she used to be. Turn her into a pillar of salt or better yet, a puddle of cum."
            scene bg LChristmas59
            with dissolve
            $ renpy.pause ()
            scene bg LChristmas50
            with dissolve
            GCP "This is a disaster!"
            RT "{i}Isn't there anything we can do to salvage things?{/i}"
            GCP "I don't know.... I give up.... try to keep your eyes out for some life lessons.... I guess."
            GCP "I'll be pillaging the bar down the street for some hard liquor. I'll be back when it's time to go."
            play sound Twinkle
            scene bg LChristmas59
            with dissolve
            RT "{i}Wow, She really seems sad.{/i}"
            RT "{i}I hope Futa God isn't too hard on her.{/i}"
            RT "{i}Haha....Futa God.... hard....{/i}"
            RT "{i}Too bad she left. That joke would have cheered her up.{/i}"
            L "Ok, We're back!"
            AD "Great! I think I've got the camera figured out, so go strike a pose."
            scene bg LChristmas28
            with dissolve
            L "Ok Agent Diaz, I think we're ready"
            S "Is this ok?"
            AD "Great! I like the buddy-buddy pose."
            R "That will make a great first pic."
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            scene bg LChristmas28
            AD "Can you add a homey Christmas background later or something?"
            R "Uh, yeah. That's what I'll do."
            scene bg BlurryWhite
            with fade
            scene bg LChristmas29
            with fade
            AD "I can see it all now!"
            $ renpy.pause ()
            AD "Ok.... now I want you to do some Christmassy things."
            S "Like what?"
            AD "I don't know. Do I have to think of everything for you?"
            L "I can make it look like I'm hanging Christmas tree ornaments, I guess."
            S "And I'll make it look like I'm hanging stockings."
            AD "Yeah.... whatever! Just make it sexy!"
            ST "{i}Agent Diaz has a terrible disposition for a photographer.{/i}"
            ST "{i}I miss how professional [ryan] is.{/i}"
            scene bg LChristmas30
            with dissolve
            AD "Nice! That looks super hot!"
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            scene bg LChristmas30
            AD "I think I got a lady boner!"
            LT "{i}It's kind of fun posing with my sister, and Agent Diaz dominating this photo shoot is kind of turning me on.{/i}"
            ST "{i}My sister looks sexy as hell in that costume I made for her. Plus, it's kind of turning me on to pose in front of someone else besides [ryan].{/i}"
            RT "{i}This is insightful! I wish I could read minds all the time.{/i}"
            AD "Ok.... enough of that!.... I think it's time to pull out the presents I brought."
            AD "Let's do some shots with you opening them."
            scene bg LChristmas31
            with fade
            AD "God, you two are sexy! I love those outfits, Sidney!"
            S "Uhh.... thanks?"
            AD "Yeah, I've got a great shot of both of your sexy young pussies."
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            scene bg LChristmas31
            AD "Once you get them open, show each other what was in them."
            AD "And try to look happy about what's inside!"
            scene bg LChristmas32
            with dissolve
            ST "{i}Oh God!.... Of course they're dildos{/i}"
            LT "{i}What a predatory pervert!{/i}"
            AD "This is great! You two are great actresses!"
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            scene bg LChristmas32
            ST "{i}If she offers to screw me with it, I'm going home!{/i}"
            LT "{i}What if she makes us use them?{/i}"
            AD "Alright.... why don't you two pretend to thank each other with a passionate kiss."
            scene bg LChristmas33
            with dissolve
            S "What!?..."
            AD "For the photo shoot!"
            AD "Not for real."
            AD "Though, I think you'd both enjoy a good makeout session with each other, or you can come make out with me if that doesn't do it for you."
            S "Gross!"
            S "I'd rather make out with Lauren, than with you."
            AD "Great, then go ahead and do that."
            L "But we're sisters!"
            AD "Yeah, well, none of your online fans know that. And even if they did, it would just make you two even more popular."
            RT "{i}Maybe I should put that in their bios.{/i}"
            AD "Are you gonna sit there like little bitches, or can we get on with this?"
            LT "{i}Oh my God! Will Sidney agree to do this with me? Why am I getting butterflies in my pussy when I think about it?{/i}"
            L "Come on Sidney, Let's just get it over with."
            S "Fine!"
            AD "Lauren, why don't you just straddle Sidney and..."
            scene bg LChristmas34
            with dissolve
            AD "Oh, yeah.... that's perfect!"
            R "Wow! That's pretty hot!"
            AD "I know, right?"
            S "Just hurry up and take the picture!"
            scene bg LChristmas35
            with fade
            ST "{i}Before my pussy betrays me and leaves a puddle on the floor!{/i}"
            ST "{i}This is so wrong!{/i}"
            ST "{i}Why is it making my pussy tingle so much?{/i}"
            LT "{i}Why does this turn me on so bad?{/i}"
            LT "{i}I've already been having confusing thoughts about women, thanks to Agent Diaz, but now I'm getting turned on by my sister?{/i}"
            LT "{i}God, I hope I don't drip all over her lap.{/i}"
            LT "{i}I can't believe she made a costume that doesn't include panties.{/i}"
            RT "{i}Wow! They're kind of into each other.{/i}"
            RT "{i}It sounds like they just need a little persuading.{/i}"
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            scene bg LChristmas35
            AD "Great! I think we're ready for the next pose."
            $ renpy.pause ()
            AD "Unless you want to keep kissing, but I'm thinking we should take a few shots playing with your new toys."
            scene bg LChristmas36
            S "Play with our..."
            L "(Gulp) Toys?..."
            S "How do you mean?"
            LT "{i}Oh my.... she wants us to dildo each other.... shit!.... I think I just dripped onto Sidney's leg!{/i}"
            LT "{i}I hope she doesn't notice.{/i}"
            ST "{i}Holy shit!.... I think Lauren just leaked onto my leg!.... Does the thought of us playing with toys together get her excited?{/i}"
            AD "Haha.... I'm not expecting you to screw each other with your new dildos."
            RT "{i}These girls are going to make me nut in my pants!{/i}"
            AD "Just get into a position so it looks like Sidney is penetrating Lauren with the dildo."
            AD "But you won't actually penetrate.... haha, unless you want to."
            AD "Whatever you choose, Just make it look like it."
            AD "Unless you want to keep making out all day!"
            LT "{i}I kind of do.{/i}"
            S "Uuuhhh.... ok Lauren.... let's get.... into position."
            scene bg LChristmas37
            with fade
            play music SexMusic
            S "Does this look ok?"
            AD "Yeah, that's pretty convincing."
            AD "Let me get a quick shot of it."
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            scene bg LChristmas37
            AD "Great! Now move the dildo a little closer."
            AD "So.... just kind of prod and push the dildo between her thigh gap."
            AD "From my perspective, it should look pretty convincing."
            scene bg LChristmas41
            with fade
            ST "{i}Hmmmm.... I think I should use this opportunity to punish Lauren for not telling me about Agent Diaz. This might not have been so shocking, had I been warned.{/i}"
            ST "{i}Not only that, but she did let her pussy leak her naughty juices all over my leg.{/i}"
            RT "{i}Oh, no way!.... I always thought Sidney was too much of a prude to do anything like that to her own sister!{/i}"
            RT "{i}I wonder what she'll do to her.{/i}"
            scene LChristmasMovie01
            with fade
            LT "{i}Oh.... my.... God!....{/i}"
            LT "{i}What the hell is Sidney thinking?{/i}"
            LT "{i}Where does she get the balls to do this to her own sister?{/i}"
            LT "{i}Keep quiet.... not a sound.... that would be so embarassing if [ryan] and Agent Diaz knew!{/i}"
            scene bg LChristmas41
            with fade
            ST "{i}Haha.... look at her squirm.... this is driving her crazy!{/i}"
            RT "{i}Damn, from this angle I can't see what she's doing.{/i}"
            scene LChristmasMovie01
            with fade
            RT "{i}I can only imagine what's going on back there.{/i}"
            scene bg LChristmas42
            LT "{i}Why does it feel so much better when Sidney does that to me, then when I do it to myself?{/i}"
            LT "{i}It's really starting to feel good!{/i}"
            scene bg LChristmas43
            LT "{i}Oh God!.... This is driving me crazy!.... What if that ho gives me an orgasm, right here in front of [ryan] and Agent Diaz?{/i}"
            S "(whispering) This is what you get for not telling me about Agent Diaz, and for dripping your dirty juices all over my leg."
            L "(whispering) Oh my God.... you.... noticed that?"
            S "(whispering) Yes, I noticed that!.... And now I'm going to do this until Agent Diaz tells me to stop."
            RT "{i}Whatever Sidney is doing to Lauren, I should help it continue for a little while.{/i}"
            R "Agent Diaz? Can I quickly show you a couple of settings on that camera that will make the shots even better?"
            AD "Yeah.... I want these pics to turn out well too."
            R "Great! Let me show you a few things."
            scene LChristmasMovie01
            with fade
            LT "{i}You've got to be kidding me!{/i}"
            S "(whispering) Oh my God Sidney!.... Today is your lucky day."
            L "(whispering) You're so mean today!"
            S "(whispering) I'll bet your slutty little pussy wishes I'd go further in, doesn't it?"
            L "(whispering) Nnnn....nnoo...that's disgusting!"
            L "(whispering) I.... I don't.... want my own sister.... to fuck my pussy!"
            S "(whispering) You don't sound very convincing."
            scene bg LChristmas43
            L "(whispering) When did you become such a pervert?"
            S "(whispering) hmmm.... well.... lately there's been some things going on, that have opened me up to be a little more sexually adventurous."
            ST "{i}Thank you [ryan].{/i}"
            L "(whispering) You mean like molesting me in my sleep?"
            L "Did you do that on purpose!?"
            S "Ssshhhh.... (whispering loudly) Of course I didn't."
            S "(whispering) But it did start a chain of events that brought me to where I am now."
            S "(whispering) Maybe I'll tell you some day."
            S "(whispering) Maybe it would help you be a little more adventurous."
            LT "{i}She has no idea!{/i}"
            LT "{i}She would probably think I'm such a dirty pervert if she knew that I've been dry humping my own brother.{/i}"
            LT "{i}Oh I wish it was his cock rubbing against my pussy!{/i}"
            RT "{i}Holy shit!.... If this isn't a dream, I could really ramp things up between the two of them.{/i}"
            RT "{i}But how will I ever be sure?{/i}"
            L "(whispering loudly) Aaahhhhh.... Fuck you, Sidney.... you're driving me completely crazy! Just fuck my pussy already!"
            stop music
            play sound Scratch
            scene bg LChristmas44
            with fade
            $ renpy.pause ()
            play music SexMusic
            S "(whispering) Are you fucking kidding me?"
            L "(whispering) No.... you ho! You started this."
            L "(whispering) I'm literally dying with lust right now!"
            S "(whispering) Is it really turning you on that bad to have your sister rub your pussy?"
            L "(whispering) Well, obviously I'm thinking of someone else while you're doing that."
            LT "{i}Like Agent Diaz spanking me in my room!.... That feels sooo wrong when I think those things!.... So why does it turn me on so bad?{/i}"
            L "(whispering) I will admit, having you do this to me, right in front of [ryan] and Agent Diaz, while they look on, completely clueless. Well, it's making this so much hotter!"
            S "(whispering) Aren't you worried they'll notice?"
            L "(whispering) No.... they'll think you're just sliding it between my thighs like she suggested.... plus he's got all her attention focused on his camera right now."
            S "(whispering) Alright.... you asked for it!"
            scene bg LChristmas45
            with dissolve
            $ renpy.pause ()
            scene LChristmasMovie02
            with fade
            L "Oh, my fuck!..."
            R "Are you ok over there?"
            S "(whispering loudly) Lauren!.... What the fuck?"
            L "Yeah.... I'm.... ok.... I think I just.... kneeled on a.... pebble."
            R "Ok good!.... I'm glad that's all it is."
            R "We'll be done with the camera soon, I just have a few more things to show Agent Diaz. Just hang on a little longer!"
            RT "{i}Holy Futa God!.... Sidney penetrated Lauren before I got to!{/i}"
            RT "{i}I'm kind of jealous!{/i}"
            RT "{i}But at the same time.... that's pretty fucking hot!{/i}"
            scene bg LChristmas46
            with fade
            LT "{i}Holy fuck!.... My sister is fucking me.... right in front of my brother and this perverted woman.... and they have no idea!....{/i}" #l_xmas_5
            RT "{i}Well, maybe more than you think.{/i}"
            LT "{i}I've never been more turned on in my life!{/i}"
            LT "{i}Oh....no.... what if I cum?.... It will be so obvious if I squirt all over the green screen!{/i}"
            LT "{i}Fuck!.... What will.... they think?....{/i}"
            scene LChristmasMovie02
            with fade
            LT "{i}I can't believe Sidney is into this!.... Now we have a secret together.{/i}"
            LT "{i}Now we can do some real sisterly bonding in the future!{/i}"
            LT "{i}I wonder if she'll be up for using Mr. Snuggles' strap-on?{/i}"
            LT "{i}Fuck!.... I can just imagine her pounding me from behind!{/i}"
            scene bg LChristmas45
            with fade
            ST "{i}Why am I enjoying this so much?{/i}"
            ST "{i}It's not like it's my pussy that's getting all the attention.{/i}"
            ST "{i}Good God!.... I can't believe this is happening!{/i}"
            ST "{i}One day I'm sucking my brother's dick, and the next day I'm pounding my sister's pussy!{/i}"
            scene bg LChristmas60
            with dissolve
            ST "{i}This is so bad!{/i}"
            ST "{i}I'm not supposed to be turned on by my siblings!{/i}"
            ST "{i}What's next? Fantasies about my mom?{/i}"
            ST "{i}Shit, Sidney!.... Don't even go there!{/i}"
            ST "{i}With her perfect ass and titties!{/i}"
            scene bg LChristmas45
            with dissolve
            ST "{i}Aaahhh.... maybe I should just embrace my perversions.{/i}"
            ST "{i}[ryan] doesn't seem to follow any kind of code of ethics.{/i}"
            RT "{i}Ouch!.... Yeah.... I kind of let those ethics die the night I saw Mom at the club.... and started letting my cock do all my thinking.{/i}"
            scene LChristmasMovie02
            with fade
            RT "{i}Maybe poor self control is a weakness in our genetics.{/i}"
            RT "{i}Hmmmm.... maybe a weakness that I can take advantage of.{/i}"
            $ renpy.pause ()
            LT "{i}Fuck.... Fuck.... Fuck.... Fuck....{/i}"
            LT "{i}I'm getting sooo close!{/i}"
            scene bg LChristmas46
            LT "{i}Fuck.... Fuck.... Fuck.... Fuck....{/i}"
            LT "{i}What am I going to do?{/i}"
            LT "{i}I can't control if I squirt or not!{/i}"
            LT "{i}And as turned on as I am, it's basically a sure thing!{/i}"
            RT "{i}I should stop her before she makes a mess!.... I don't even want to know what Agent Diaz would do. Probably make Sidney lick it up.{/i}"
            R "So that should be all! I think that will improve your pictures a lot!"
            AD "Hmmmm.... that seemed like a lot of explaining for just a couple little adjustments."
            AD "Oh, well.... you girls are looking amazing. That dildo thigh humping looks pretty convincing, huh?"
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            scene bg LChristmas46
            LT "{i}Fuck.... I was so close!{/i}"
            scene bg LChristmas43
            with dissolve
            LT "{i}Oh Thank God she stopped her!{/i}"
            LT "{i}As much as I wanted that.... that would have been a disaster.{/i}"
            scene bg LChristmas42
            with dissolve
            LT "{i}But now I really need to get off! How am I going to take care of this?{/i}"
            play music WeWishYou
            scene bg LChristmas51
            with fade
            AD "Ok, I have just one more pic for you girls to pose to."
            AD "I'm going to be in this one, so [ryan], take the camera."
            AD "And give me just a second to strip down to my panties."
            RT "{i}Holy shit! Diaz is going to pose with them! I'll have pictures that will force the FBI to fire her.{/i}"
            RT "{i}That is, assuming this isn't just a dream.... and.... shit, even if it isn't, this isn't happening right now, on my timeline.{/i}"
            RT "{i}Dammit!{/i}"
            S "Really? You're taking off your top too?"
            AD "Haha.... you know you like what you see!"
            LT "{i}She does have really sexy breasts.{/i}"
            scene bg LChristmas52
            with dissolve
            AD "Alright ladies. I want you to both get into a kneeling position, and then I want a shot where it looks like one of you is licking my crotch from the front, and one is licking my ass from behind."
            S "Are you fucking kidding me?"
            RT "{i}Oh my God!....{/i}"
            AD "If you complain too much, I'll take off the panties too."
            L "I call crotch!"
            AD "Ohh.... Lauren! I like the eagerness."
            L "I just don't want to get stuck with licking your ass."
            AD "Haha.... I like the way you think!"
            AD "You ready, Sidney?"
            S "I don't want to lick your ass!"
            AD "Then don't! Just make it look like you are."
            AD "Come on, it's the last picture, don't make me bring up my leverage over you."
            S "Fine!"
            AD "Awesome! Ok [ryan], we'll let you know when we're in position."
            AD "How's it looking?"
            R "Just make your face look more orgasmic, and I think it will look amazing."
            scene bg LChristmas53
            with dissolve
            ST "{i}How long do I have to hold this pose? Luckily it doesn't smell too much like ass. Mostly just sweat.{/i}"
            ST "{i}I guess it could be worse.{/i}"
            LT "{i}This is the closest I've ever been to another girl's pussy.{/i}"
            LT "{i}Her scent is different than mine, but still sweet, and.... sexy.{/i}"
            LT "{i}Oh God!.... I feel like I'm going to squirt, and I'm not even getting my pussy played with.{/i}"
            LT "{i}Fuck.... I need a release sooooo bad!{/i}"
            R "There.... that pose is perfect!"
            AD "This is going out as my Christmas card to my close girlfriends."
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            scene bg LChristmas53
            R "Alright, I got it. I think that might end up being the best of the set."
            scene bg BlurryWhite
            with fade
            scene bg LChristmas54
            with fade
            AD "Awesome! Too bad for you, it's not going with the rest of the set."
            R "What why not?"
            AD "Haha.... I'm sure you'd like that.... but I'm not an idiot. I know what damage that picture would cause in the wrong hands."
            scene bg LChristmas55
            with dissolve
            AD "I'll just be taking the SD card."
            R "What about the other pics?"
            AD "You're a fan of my work, are you?"
            AD "I'll send you the rest."
            AD "After I get what I want off of it."
            AD "You girls did really good today!"
            AD "I can't wait to see what kind of photo shoots [ryan] puts you together in down the road."
            AD "I am one of your subscribers on Cosplay Heaven, by the way."
            AD "My user name is BigDykeDiaz, haha..."
            L "Uhhh.... we'll look for you on there..."
            AD "Thank you all for your time and hard work!"
            AD "The pleasure was all mine!"
            AD "Later, perpetrators!"
            scene bg SleepBlack
            with fade
            scene bg LChristmas56
            with dissolve
            S "(whispering) Lauren? Are you ok?.... I know you didn't get to satisfy your itch."
            scene bg LChristmas57
            with dissolve
            L "(whispering) No!.... I'm so horny right now!"
            RT "{i}I'll help her take care of that.{/i}"
            scene bg LChristmas56
            with dissolve
            S "(whispering) When we go to the storage shed to change, I'll finish what I started.... I can't leave my own sister in such pain."
            scene bg LChristmas58
            with dissolve
            L "(whispering) Oh my God!.... I have the best sister in the world.... I can't wait!"
            RT "{i}Shit! Sidney's taking over!{/i}"
            scene bg LChristmas57
            with dissolve
            R "Uhh.... Sidney, we're all done here.... you can run home. Lauren?.... Would you mind sticking around here and helping me clean up?"
            L "Sorry [ryan], but Sidney and I have plans to go shopping right now. Normally I'd stay and help, but we need to get our shopping done before all the stores close."
            L "I'm really sorry!"
            RT "{i}Yeah.... sure you are.... at least that storage shed has so many holes in it, it will be easy to spy on them.{/i}"
            R "Alright.... I understand. I'll take care of it myself. Go ahead and get changed."
            scene bg LChristmas59
            with dissolve
            "{i}\"Sound of girls giggling as they run off.\"{/i}"
            RT "{i}Holy hell!.... I can't believe that all just happened.{/i}"
            RT "{i}Agent Diaz is even more unhinged than I thought!{/i}"
            RT "{i}Maybe even more so than me.{/i}"
            RT "{i}And what's the deal with Sidney cock-blocking me?{/i}"
            RT "{i}I'll give them just a second, and then I'm definitely spying on them.{/i}"
            play sound Twinkle
            scene bg LChristmas50
            with dissolve
            R "Ahh.... shit! You scared me!"
            R "Feeling any better?"
            GCP "Well, the alcohol has numbed me a little, but no, I'm still feeling pretty shitty."
            GCP "How were things while I was gone?"
            R "Oh, you know.... nothing eventful happened here."
            GCP "You don't have to lie to me. All your thoughts were so sexually charged, I could hear them all the way in the bar down the street."
            GCP "Fucking Diaz!"
            R "Fucking Diaz."
            GCP "I have never failed so spectacularly in all the decades I've been doing this."
            GCP "I won't be gettin my wings anytime soon."
            GCP "Plus, God's definitely going to ream my tiny ass with her huge futa cock, when I get back."
            R "Oh, God!.... I'm so sorry!"
            R "But if it makes you feel better.... I learned a few really valuable lessons."
            GCP "Oh?.... Like what?"
            R "I learned that Diaz is really dangerous, and I need to make sure I keep things under control with her."
            R "I learned that Sidney and Lauren are starting to think like me."
            GCP "(sarcastically) Oh, wonderful."
            R "And I learned that I need to keep them from getting too intimate with each other right away, or they're going to cut me out of their sex lives."
            R "I think I need to work on getting each one of them attached to me more, before I bring them together."
            GCP "(sarcastically) What a treasure trove of moral lessons you've learned today."
            R "I really am sorry it didn't work out for you the way you wanted. But if you'll now excuse me. I've got a pretty hot event I need to go spy on."
            R "Haha.... yeah, you know what I'm talking about."
            GCP "Yeah, sorry about that, but you won't have time."
            R "What?"
            GCP "Yeah, it's about time to go."
            GCP "You can expect the third, and final ghost, when the clock strikes three."
            R "No, I don't want to go yet!.... And once again, we don't have a clock tower."
            GCP "In 5.... 4.... 3..."
            R "Nooooo!..."
            GCP "2.... 1..."
            play sound Twinkle
            scene bg SleepBlack
            with fade
            $ renpy.pause ()
            scene bg ChristmasEvent58
            with fade
            RT "{i}Oh Futa God.... I'm back in my bed?.... Another weird dream?{/i}"
            RT "{i}At least, I think they were dreams!{/i}"
            RT "{i}They were both just so vivid! Huh.... {/i}"
            RT "{i}I guess I'll have to wait till three o'clock to find out.{/i}"
            RT "{i}Ohhh.... so tired.... zzzzzzz....{/i}"
            $ second_xmas_ntr = True
            scene bg SleepBlack
            with fade
            $ renpy.pause ()
            jump xmas_future

##########################CHRISTMAS#CLUB###############################################################CHRISTMAS#CLUB#######################################################################CHRISTMAS#CLUB#################################################################CHRISTMAS#CLUB######################################################################CHRISTMAS#CLUB################

label christmas_club:
    play music ChristmasRap
    scene bg ChristmasEvent17
    with fade
    scene bg ChristmasEvent18
    with fade
    $ renpy.pause ()
    play sound Twinkle
    scene bg ChristmasEvent19
    with dissolve
    $ renpy.pause ()
    play sound Twinkle
    scene bg ChristmasEvent20
    with dissolve
    RT "{i}Holy shit!.... I think I'm going to puke!{/i}"
    GP "Just hold it in for a second.... the feeling wears off really quick."
    scene bg ChristmasEvent21
    with fade
    R "What the fuck!.... Where are we?"
    GP "Sssshhhhhh.... try not to speak out loud to me in public. Don't forget, I can hear your thoughts. People will think you're loony if you're talking to someone on your shoulder."
    RT "{i}I have gone loony!.... I'm talking to a ten inch version of my own mom!{/i}"
    RT "{i}And now I'm just thinking at her!{/i}"
    RT "{i}And I assume that I'm the only one who can see or hear you?{/i}"
    GP "You have assumed correctly."
    RT "{i}So, where the fuck are we?{/i}"
    GP "The more appropriate question would be, \"When are we?\""
    RT "{i}Ok.... I'll bite.... when are we?{/i}"
    GP "So glad you asked.... we have gone back to a Christmas 20 years ago."
    GP "To the day that your parents met."
    RT "{i}Really?.... Cuz Mom told me that they met when she was working at a strip club.{/i}"
    GP "Oh, shit!.... Is that true?.... Dammit.... I knew I should have read your whole file."
    GP "Well, that's not a problem!.... It doesn't matter where two people fall in love.... just that they do."
    GP "And you're lucky enough to get to see it."
    scene bg ChristmasEvent22
    with dissolve
    RT "{i}You do realize that my infatuation with my mom and sisters started because I saw my mom stripping at a strip club, right?{/i}"
    GP "Well, the first time was traumatic, so hopefully this time will be therapeutic."
    RT "{i}Where is everybody? The club seems empty.{/i}"
    GP "Well, it's Christmas! All the men should be home with their families."
    GP "So, let's look around and see if we can find your parents."
    VOM "Let's welcome to the stage the only one of our dancers desperate enough to come in on Christmas, to perform for a single patron, Oh, I guess there's two of you now.... I didn't see you come in."
    VOM "{i}(Whispering over mic){/i} Honestly Bill, it was a terrible idea to be open on Christmas."
    VOM "{i}(Other muffled voice){/i} Ssshhhh.... they can hear you over the mic!"
    VOM "Once again! Let's welcome to the stage, Santa's sexy helper, the one and only, [mom_name]!"
    scene bg ChristmasEvent23
    with dissolve
    R "Oh.... my.... God!..."
    GP "....Holy Virgin Futa!"
    scene bg ChristmasEvent24
    with fade
    RT "{i}We did go through time.... that's my mom!.... Only.... much younger.{/i}"
    RT "{i}She looks incredible!{/i}"
    GP "Yeah, well.... stop ogling at your mother.... and don't forget why we're here!"
    RT "{i}Why are we here again?{/i}"
    GP "So you can see your parents fall in love! I'm pretty sure If you see the moment they fall in love, you wouldn't possibly want to do anything to ruin their marriage."
    GP "Though I'll admit.... I had hoped for a more romantic setting.... I should have done my homework."
    GP "Well, let's make the most of it anyways."
    GP "Look! Is that your dad over there?"
    scene bg ChristmasEvent25
    with fade
    RT "{i}Holy shit.... yeah.... only way younger and thinner.{/i}"
    RT "{i}I wonder if he's as much of a douche in the past, as he is in the present.{/i}"
    GP "Well.... let's watch and find out."
    scene bg ChristmasEvent26
    with fade
    GP "Oh look, how sweet!.... He's tipping your mom for her hard work!"
    RT "{i}You think tipping a stripper is sweet?.... Angels have a strange moral code.{/i}"
    GP "I'm not an angel, I'm a ghost.... and it's sweet because it's going to lead to them falling in love!"
    RT "{i}Well, I know seeing Mom strip made me fall in love.... that is, I already loved her, but now I want to bang her.{/i}"
    GP "Oh, stop thinking with your cock, and try to appreciate this moment. You're about to see them fall in love!"
    scene bg ChristmasEvent27
    with dissolve
    D "Hey buddy!.... Are you just going to stare at us all day? Why don't you be a gentleman and tip the nice lady. It is Christmas, you know."
    R "Uhhhhh..."
    RT "{i}Shit!.... What do I do?{/i}"
    GP "OK.... don't panic.... I gave you some Christmas magic when I blew that Christmas dust on you."
    GP "You should be able to pull anything you need out of your pocket.... you know, like money.... all you need to do is think really hard about it."
    M "Oh, be nice!.... Nobody should feel pressured into tipping me, but I'll tell you what I'll do. Whichever of you tips me the most tonight will get a private lap dance from me."
    M "Are you both up for it?"
    D "I'm in!"
    GP "I'm not sure this is a good idea..."
    RT "{i}Why?.... Is it like the movie \"Back to the Future\", where I'll stop existing if my parents don't fall in love?{/i}"
    GP "No.... It's nothing like that! There isn't anything we can do here that will change the future. The past is already written."
    GP "These are just shadows of the past, but with Christmas magic, we can interact with them."
    RT "{i}Well, what can go wrong then?{/i}"
    GP "Well, you might not learn the lesson that I'm trying to teach you!"
    R "I'm in too!"
    GP "Dammit! You better let your dad win!"
    M "Yay!.... I'll start dancing and you guys start tipping!"
    M "Let the \"tip off\" begin!"
    scene bg ChristmasEvent28
    with fade
    RT "{i}Wow!.... Look at her!.... And you're trying to teach me that I shouldn't get a hard-on when I look at that?{/i}"
    GP "Well, there's a big difference in getting a hard-on and actually trying to fuck her!"
    RT "{i}You're right.... I should try to fuck her!....{/i}"
    scene bg ChristmasEvent29
    with dissolve
    GP "Dammit!.... No!"
    scene bg ChristmasEvent30
    with dissolve
    GP "Get away you hussy!"
    GP "She needs to be giving her attention to your dad!"
    scene bg ChristmasEvent31
    with dissolve
    RT "{i}Is it accurate to say that this is bringing back memories, if this event technically takes place before I saw Mom in the club for the first time?{/i}"
    GP "I don't know.... don't ask me stupid questions."
    D "Hey baby!. I've got something for you over here."
    scene bg ChristmasEvent32
    with fade
    GP "That's it [dad_name]! Keep on bidding! Win [mom_name]'s love!"
    RT "{i}Damn! I'm jealous of the view he's getting!{/i}"
    scene bg ChristmasEvent33
    with fade
    RT "{i}So, I'm assuming that if I were to win the tip war, you wouldn't let me stay and enjoy it. You'd just zap me back to my room, right?{/i}"
    GP "Well..."
    RT "{i}\"Well\" what?{/i}"
    GP "Weeelllll..."
    RT "{i}What is it you don't want to tell me?{/i}"
    GP "Urrrrgggghhhh!.... We're not allowed to lie to our clients, otherwise I damn well would right now."
    GP "When we go through a time worm hole, it kind of acts like an hour-glass, and we're stuck here until we run out of time."
    GP "I was thinking that maybe we could hit the bar while we wait to go back. You know.... after your parents fall in love?"
    GP "I haven't had a good drink in a few decades!"
    RT "{i}I'm not old enough to buy alcohol.{/i}"
    GP "You'd just have to think about an ID hard enough, and then you could pull it out of your pocket."
    RT "{i}Haha....Yeah, that's right!{/i}"
    RT "{i}Hmmmm.... you know what? Let's just play it by ear.{/i}"
    GP "Shit!!.... I don't like the sound of that."
    scene bg ChristmasEvent34
    with fade
    GP "Alright [ryan].... I think this should be our last tip.... I don't know how much more [dad_name] can afford."
    scene bg ChristmasEvent35
    with dissolve
    RT "{i}I've got an endless supply of money in my pocket.... how on earth would I be able to resist tipping that sexy minx?{/i}"
    GP "Don't forget why we're here!"
    GP "If you don't get to see your parents fall in love than this whole trip will have been for nothing!"
    RT "{i}Alright, I promise I'll try!{/i}"
    scene bg ChristmasEvent36
    with dissolve
    RT "{i}But the look in those eyes!{/i}"
    RT "{i}And those perfect breasts!{/i}"
    scene bg ChristmasEvent37
    with dissolve
    RT "{i}Oh, God.... I think the only thing you've succeeded in doing is making me fall deeper in love with Mom.{/i}"
    GP "Dammit [ryan]! Show some self-restraint, for God's sake!"
    GP "Resist that perfect ass!"
    scene bg ChristmasEvent38
    with dissolve
    RT "{i}I'm trying!{/i}"
    RT "{i}But I've got a hard-on that could cut glass!{/i}"
    D "Hey, sexy! I've got something over here that's going to sweeten your whole Christmas!"
    scene bg ChristmasEvent39
    with fade
    D "And just so you know, little boy.... hey!.... Are you even old enough to be in a bar?"
    R "I've got ID. I've just got one of those baby faces, ya know?"
    D "Well.... I'm going to send you home crying like a baby."
    R "Wow.... clever..."
    D "Fuck you.... see, I don't ever lose.... and I also like to make grand gestures..."
    D "And this beauty deserves a real man to dance for tonight, not some little boy!"
    D "So, feel free to leave any time, because I can guarantee your Christmas is going to end in disappointment."
    scene bg ChristmasEvent40
    with dissolve
    D "Merry Christmas, beautiful!"
    M "Oh, my God!..."
    M "That's got to be at least a thousand dollars!..."
    D "It's actually one thousand, five hundred, to be exact!"
    M "That's the biggest tip I've ever seen!"
    scene bg ChristmasEvent41
    with dissolve
    M "Oh.... I want to rub your huge tip all over my pussy!"
    D "Holy shit.... that's hot!"
    GP "Yes! [ryan]! You did it!"
    RT "{i}What did I do?{/i}"
    GP "You forced your dad to make a grand gesture to win over your mom!"
    GP "They look like they are falling in love already!"
    RT "{i}Who said I'm going to let him win?{/i}"
    GP "Oh no, please, [ryan]! It's too perfect! Please!.... Just let it play out from here!"
    RT "{i}Hmmmmm....{/i}"
    menu:
        "Let Dad win. (NTR Warning!!)":
            R "Well, congratulations.... you win..."
            scene bg ChristmasEvent59
            with dissolve
            D "That's right, I win."
            D "Because I always win..."
            D "So head on home, back to mommy, little boy."
            D "Maybe you can suck on her tits tonight."
            RT "{i}Dammit! If he even knew, that he stole that chance from me!....{/i}"
            GP "He didn't steal that chance! You weren't even born yet, you idiot!"
            RT "{i}UUURRRGGGHHHH.... I still hate to lose to that asshat!{/i}"
            GP "Well, just remember.... If he didn't fuck your mom, you wouldn't have been born."
            GP "Soooo..."
            scene bg ChristmasEvent44
            with fade
            RT "{i}And there goes that beautiful ass! I wish I was following it!{/i}"
            scene bg ChristmasEvent60
            with dissolve
            D "Get one good last look, loser! Because that ass is going to be rubbing all over my lap tonight!"
            RT "{i}Ugghh.... what an asshole!{/i}"
            scene bg ChristmasEvent61
            with dissolve
            RT "{i}How did Mom ever fall in love with that jerk?{/i}"
            scene bg ChristmasEvent62
            with dissolve
            GP "Well?..."
            GP "Wasn't that amazing?.... You know.... to see the beginnings of your parents's relationship?"
            GP "Should we hit the bar, until our time here runs out?"
            RT "{i}No!.... If anything, it makes me even more convinced that Mom shouldn't stay together with Dad, and that she would be happier with me.{/i}"
            GP "No!.... That's not right!"
            GP "This has to be a life changing event for you!"
            GP "This is supposed to make you want to stop trying to fuck your mom, and stop trying to fuck over your dad!"
            GP "Uhhhhh..."
            GP "I guess.... we need to keep watching."
            RT "{i}I don't want to see my mom giving my dad a lapdance!{/i}"
            GP "Well, tough shit!"
            GP "You haven't had a life changing event, so we're going to follow them until you do!"
            GP "Now follow me upstairs!"
            scene bg ChristmasEvent63
            with fade
            GP "Ok, now see if you can open the door a crack and take a peek."
            RT "{i}It's locked.{/i}"
            GP "Hmmmm..."
            scene bg ChristmasEvent64
            with dissolve
            GP "Well, I don't really hear any talking..."
            GP "We're going to have to go in."
            RT "{i}Once again.... I don't want to see their lapdance, and I'm not invisible like you.{/i}"
            GP "You're right, that's why I'm going to let you see through my eyes."
            GP "You'll just wait out here, and I'll magic myself inside, and then you will see everything I see."
            GP "Here I go"
            play sound Twinkle
            scene bg ChristmasEvent63
            with dissolve
            $ renpy.pause ()
            scene bg BlurryWhite
            with fade
            GP "Ok, can you see anything yet?."
            RT "{i}I can only see white!{/i}"
            GP "OK, give it just another second."
            play music SexMusic
            play sound Blow02 loop
            scene Christmas01
            with fade
            RT "{i}Oh what the hell?{/i}"
            RT "{i}I thought Mom was just going to give him a lap dance.{/i}"
            GP "Well, he did just tip her $1,500. Your little competition raised the stakes."
            GP "I'm sure she felt like she owed him a little more for such a generous tip."
            GP "I need to check for sure, but I don't even think he got a lap dance in the actual version of the past."
            GP "This is all thanks to you."
            RT "{i}Goddammit, Ghost of Christmas Past! I don't want to watch this.{/i}"
            RT "{i}Ahhh.... I can't look away or close my eyes!{/i}"
            GP "That's because you can only see what I can see."
            RT "{i}Well, look the hell away then!{/i}"
            GP "Just a little longer."
            GP "When a man ejaculates, it releases all kinds of chemicals that could make [mom_name] fall in love with [dad_name]."
            GP "I need you to see them fall in love! For your own good."
            RT "{i}Yuck!.... Do you realize I'm going to need to see a psychologist after you're done helping me?{/i}"
            GP "Just shut up and watch."
            RT "{i}Dad's pretty small though.{/i}"
            RT "{i}Too bad his penis isn't as big as his tip.{/i}"
            RT "{i}No wonder Mom seems so impressed when she gets a look at me.{/i}"
            GP "It's not about size."
            RT "{i}It kind of is.{/i}"
            scene bg ChristmasEvent65
            with dissolve
            GP "Oh, look! He's about to paint her face with his cum!"
            GP "She looks excited!"
            RT "{i}Yeah.... she really looks like she can't wait.{/i}"
            RT "{i}Shit.... I am going to have to see her fall in love with him.{/i}"
            play sound Ejaculate
            scene bg ChristmasEvent66
            with dissolve
            RT "{i}Oh.... haha!.... Look at how small that was.{/i}"
            scene bg ChristmasEvent67
            with dissolve
            RT "{i}Look at how disappointed Mom looks!{/i}"
            RT "{i}Haha!.... He really should have let her fall in love with him before he showed her his little cock!{/i}"
            GP "It's not that little! It's just little compared to yours."
            GP "Goddammit!"
            play music WeWishYou
            scene bg BlurryWhite
            with fade
            $ renpy.pause ()
            scene bg ChristmasEvent68
            with fade
            GP "Well, that was a complete waste of time!"
            GP "There's no way God's going to give me my wings now!"
            GP "Maybe she'll give me some if I give her a really good blow job."
            RT "{i}Wings? I thought you were a ghost, not an angel?{/i}"
            GP "Ghosts can get wings too.... you really don't know anything about ghosts."
            RT "{i}Yeah, I've never really claimed to, either.{/i}"
            GP "Well, the only thing you need to know about them right now is that you should expect the next ghost when the bell tolls two."
            RT "{i}What bell?{/i}"
            GP "You know.... like the bell in the clock tower."
            RT "{i}Our town doesn't have a clock tower.{/i}"
            GP "Well.... shit!"
            GP "That isn't nearly as dramatic."
            GP "I guess just go to sleep and the ghost will wake you up when it gets there."
            scene bg BlurryWhite
            with fade
            RT "{i}But wait!{/i}"
            scene bg ChristmasEvent58
            with fade
            RT "{i}What the hell?.... I'm back in my bed?.... Was that just a dream?{/i}"
            RT "{i}Maybe Sidney's getting revenge and spiking my tea with LSD.{/i}"
            RT "{i}That was such a crazy dream.... It felt so real.... then again, most do.{/i}"
            RT "{i}I do feel pretty tired.{/i}"
            $ first_xmas_ntr = True
            play music WeWishYou
            scene bg SleepBlack
            with fade
            $ renpy.pause ()
            jump xmas_present
        "Show that mother fucker who's boss.":
            R "Well played!.... That is quite the grand gesture."
            D "That's right! So, why don't you just head on out of here! [mom_name] has a little private dance she's dying to give me."
            R "Yeah, well, I wouldn't be too sure about that."
            GP "[ryan] No!.... Please let [dad_name] win!"
            R "And you should stop rubbing that money all over yourself.... you don't know where it's been."
            scene bg ChristmasEvent42
            with dissolve
            R "I can guarantee my money isn't nearly as dirty as his."
            GP "[ryan]!.... You asshole!"
            M "Holy shit!.... How much money is that?"
            R "Two thousand dollars, which, unless you have more money, makes me the winner."
            R "Oh.... and you should probably get used to losing to me more in the future."
            scene bg ChristmasEvent43
            with dissolve
            D "Who the fuck are you even?"
            D "And what's that supposed to mean?"
            R "You'll find out in about 20 years."
            GP "Urrrgghhh, you're such an idiot!"
            D "You're not making any sense!"
            D "I'm leaving! There's nothing else for me to stick around here for."
            R "Good, because we've never needed you anyway!"
            D "What the hell are you talking about?"
            M "Yeah.... how about we finish this conversation, and you come follow me to my dressing room."
            R "Oh, hell yeah!"
            scene bg ChristmasEvent44
            with fade
            RT "{i}Oh yeah! I'd follow that ass anywhere!{/i}"
            play sound Twinkle
            scene bg ChristmasEvent45
            RT "{i}Ahhh...Holy shit! You scared me!{/i}"
            RT "{i}Hey.... are you ok?{/i}"
            GP "Yeah.... not really."
            GP "That's not how this was supposed to go."
            GP "I was supposed to show you the error of your ways, and now, you'll be getting a lap dance from your mom because of me."
            RT "{i}Don't blame yourself!{/i}"
            RT "{i}It's not your fault that I can't stop thinking with my cock.{/i}"
            GP "Yeah, well.... I don't really have a desire to watch you enjoy my failure, so I'm going to go and see if I can steal some booze from the bar while you get a lap dance."
            RT "{i}Damn!.... You're making me feel really bad for what I just did.{/i}"
            play sound Twinkle
            scene bg ChristmasEvent46
            with dissolve
            M "Are you coming?"
            R "Oh, hell yeah!"
            scene bg SleepBlack
            with fade
            scene bg ChristmasEvent47
            with fade
            M "So, are you ready for that lap dance?"
            R "You have no idea!"
            M "Are you sure you're 21?"
            R "Of course! They wouldn't have let me in otherwise."
            M "I'd have a hard time even believing that you're 18."
            R "I just look young, ok?"
            M "Yeah ok, but you remind me of someone I know."
            M "You kind of look like a young version of my Dad.... and my brother..."
            M "You're not from around here are you?"
            R "No.... I'm from.... another country..."
            R "Uhhh.... from Idaho, yeah!"
            M "Huh.... I've never heard of it."
            R "Yeah.... most people haven't."
            M "Alright, well I'm just going to start dancing then."
            R "Wait!"
            M "What?"
            R "I just gave you $2,000. Don't you think I deserve more than a dance?"
            M "I'm going to be rubbing my ass all over your dick. What more do you want?"
            R "I was just wondering what you'd be willing to do for another two grand?"
            scene bg ChristmasEvent48
            with fade
            M "Holy shit, that's a lot of money in one day!.... But I'm not a prostitute!"
            M "I'm not going to fuck you for any amount of money."
            R "Oh, no!.... I wasn't trying to put any presssure on you to fuck me. Although I wouldn't object if you were willing."
            R "I just meant like a blowjob or something."
            M "A blowjob?"
            M "Hmmmm..."
            MT "{i}Holy shit, [mom_name]! What are you thinking?....{/i}"
            MT "{i}You swore you would never do anything like this if you became an exotic dancer.{/i}"
            MT "{i}But I never dreamt one guy would offer me $4,000 dollars in one night!{/i}"
            MT "{i}I'll have enough to pay for a semester of modeling school.{/i}"
            MT "{i}That could be enough for me to get my start in the industry.{/i}"
            MT "{i}And I wouldn't ever have to come back to this sleaze hole again{/i}"
            MT "{i}It's worth it!{/i}"
            MT "{i}Plus, he's cute!{/i}"
            MT "{i}Even if he does look like he could be your brother.{/i}"
            M "Take your pants off!"
            R "Really!?"
            M "Hurry before I change my mind..."
            play music SexMusic
            scene bg ChristmasEvent70
            with fade
            MT "{i}Wow! Look at the size of this cock!{/i}"
            MT "{i}He's as big as the men in my family!{/i}"
            scene Christmas02
            with fade
            play sound Blow03 loop
            RT "{i}Holy shit! Mom's sucking my cock!{/i}"
            RT "{i}It might just be a dream, but what an amazing dream!{/i}"
            MT "{i}Shit! This is so weird!{/i}"
            MT "{i}Why does it feel like I'm giving a blowjob to my brother?{/i}"
            MT "{i}Shit, [mom_name]! Stop thinking so much about your brother!{/i}"
            stop sound
            scene bg ChristmasEvent49
            with fade
            $ renpy.pause ()
            play sound Twinkle
            scene bg ChristmasEvent50
            with dissolve
            GP "Oh, hey.... I'm done drinking, and I wanted to tell you that it's almost time to go!"
            RT "{i}Not now I'm almost done!{/i}"
            GP "Oh, sorry. I didn't know you would still be busy.... I'll just let you get on with it."
            play sound Twinkle
            scene bg ChristmasEvent49
            with dissolve
            $ renpy.pause ()
            scene Christmas02
            with fade
            play sound Blow03 loop
            RT "{i}I'm so close!{/i}"
            RT "{i}Oh my God!.... I'm going to explode down my mom's throat!{/i}"
            stop sound
            scene bg ChristmasEvent49
            with fade
            $ renpy.pause ()
            play sound Twinkle
            scene bg ChristmasEvent51
            with dissolve
            GP "Wait! What the hell are you doing! You were just supposed to get a lap dance! Not let your own mother suck your cock!"
            GP "What a tramp! No wonder you're so messed up!"
            scene bg ChristmasEvent52
            with dissolve
            GP "Good thing it's time to go!"
            RT "{i}No not yet! I'm sooooo close!{/i}"
            RT "{i}I'm....{/i}"
            play sound Twinkle
            play sound Ejaculate
            scene bg ChristmasEvent53
            with fade
            RT "{i}Cuuuumming!{/i}"
            play sound Ejaculate
            scene bg ChristmasEvent54
            with dissolve
            GP "Oh, shit!.... What the fuck!"
            play sound Ejaculate
            scene bg ChristmasEvent55
            with dissolve
            GP "[ryan]! You mother-fucking son of a bitch!"
            GP "In all the centuries I've been doing this, I've never failed to change the course of a client!"
            GP "And this, sure as shit, is the first time I've ever been drenched in their cum!"
            GP "I think you have a problem! You're like a cum fire hose!.... That much cum is not normal!"
            GP "There's no way God's going to give me my wings now!"
            GP "Maybe she'll give me some if I let her fuck my ass."
            RT "{i}Wings? I thought you were a ghost, not an angel?{/i}"
            GP "Ghosts can get wings too.... you really don't know anything about ghosts."
            RT "{i}Yeah, I've never really claimed to, either.{/i}"
            GP "Well, the only thing you need to know about them right now is that you should expect the next ghost when the bell tolls two."
            RT "{i}What bell?{/i}"
            GP "You know.... like the bell in the clock tower."
            RT "{i}Our town doesn't have a clock tower.{/i}"
            GP "Well.... shit!"
            GP "That isn't nearly as dramatic."
            GP "I guess just go to sleep and the ghost will wake you up when it gets there."
            GP "I pray to our Futa God that she'll have better luck than I did!"
            GP "Goodbye [ryan]!.... Maybe I'll see you in hell!"
            play sound Twinkle
            scene bg ChristmasEvent56
            with dissolve
            play music WeWishYou
            RT "{i}But wait!{/i}"
            RT "{i}What the hell?.... She's gone!.... Was that just a dream?{/i}"
            RT "{i}Maybe Sidney's getting revenge and spiking my tea with LSD.{/i}"
            RT "{i}That was such a crazy dream.... It felt so real.... then again, most do.{/i}"
            RT "{i}I do feel pretty tired.{/i}"
            scene bg SleepBlack
            with fade
            $ renpy.pause ()
            jump xmas_present
