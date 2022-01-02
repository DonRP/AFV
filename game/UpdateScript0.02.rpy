
define audio.CameraClick = "music/cameraclick.mp3"

#############  RYAN'S ROOM  #############################################  RYAN'S ROOM  ###############################################  RYAN'S ROOM  #####################################  RYAN'S ROOM  ##################################################

label cosplaywakeme:
    scene bg SleepBlack
    with fade
    play music SexMusic
    L "See, it's like this almost every morning."
    scene bg BlurryWhite
    with fade
    scene bg SleepBlack
    with fade
    MD "I've never seen one before. That's about average size right?"
    L "Haha, you've been watching too much porn. Most guys aren't nearly this big."
    scene bg BlurryWhite
    with fade
    scene bg CosplayWakeMe01
    with fade
    MD "Well, I would hope not. How would a normal girl ever be able to fit that inside of them?"
    L "I think you just stretch and get used to it over time. I've been doing some exercises with a dildo in case my first time is on a rod that big."
    MD "Hehehehehhehe."
    L "Hehehhehehe."
    R "Wha.... what.... what are you girls doing in my bed?"
    scene bg CosplayWakeMe02
    with dissolve
    MD "Oh, good. We've just been waiting for you to wake up."
    L "Yeah, we've got a really good idea that we want you to be a part of."
    R "I think I know where this is going, but are you really ready to go full Alabama?"
    scene bg CosplayWakeMe03
    with dissolve
    $ renpy.pause ()
    R "Ok.... ok.... relax.... I was joking."
    RT "{i}Not joking.{/i}"
    R "But couldn't this have waited until later?"
    scene bg CosplayWakeMe02
    with dissolve
    L "No, we're too excited!"
    R "Well, what's going on?"
    MD "Well, Lauren and I met a really cool girl at the convention last night."
    L "Yeah and she's famous!"
    R "Yeah?.... Have I ever heard of her?"
    MD "Her name is Jassica Nugru!"
    R "Oh yeah, I've seen her stuff. It's pretty hot."
    scene bg CosplayWakeMe04
    with dissolve
    L "Haha.... see, I told you he's a pervert."
    R "Just because I know who she is doesn't make me a pervert."
    scene bg CosplayWakeMe02
    with dissolve
    L "Yeah, but looking at cosplay porn all day does."
    R "Well, whatever.... I like what I like."
    R "Does this conversation have a point?"
    MD "Do you know how many views her Cosplay Heaven profile gets a day?"
    R "No, do you?"
    MD "Well, no.... but it's a lot!"
    L "And now we have these kick-ass costumes, that even Jassica Nugru thought were amazing."
    MD "And we want to get internet famous too!"
    L "And since you have that nice camera Dad gave you, and you're pretty good at taking pictures, we thought..."
    scene bg CosplayWakeMe04
    with dissolve
    MD "That you would enjoy taking pictures of us!"
    L "So that we can post them online and become internet famous like Jassica!"
    scene bg CosplayWakeMe02
    with dissolve
    $ renpy.pause ()
    L "Well, what do you think?"
    R "It's worth a shot I guess. I mean.... if.... and that's a big if..."
    scene  bg CosplayWakeMe03
    with dissolve
    R "If you become internet famous..."
    R "We might even be able to make some decent money so we can help Mom out of her situation with the Mafia."
    L "For Mom? We want the money for ourselves!"
    R "Oh come on! If Dad is in prison for as long as I think he's going to be, Mom's going to be in debt to the mob for the rest of her life."
    R "I'm currently giving her everything I make to pay just the weekly interest on the debt."
    R "The least you can do is help out a little bit."
    R "And then once we've paid the Mafia everything Mom owes them, then we can use the money for ourselves."
    L "What do you mean for ourselves?"
    L "You think we're going to give you any?"
    R "If you want to succeed you better."
    R "Besides just taking pictures, I know how to market you all over the internet so that you can actually get people to see your pictures, and then I know how to convert those views into money."
    R "So, if you want to be successful, you're going to have to let me manage everything."
    scene bg CosplayWakeMe02
    with dissolve
    MD "Ok! We agree. I just want to get famous."
    L "Yeah, can you imagine having thousands of people see pictures of us every day?"
    scene bg CosplayWakeMe04
    with dissolve
    MD "I know I would check out pictures of you in your space suit!"
    L "And your little ass looks so good from behind in your outfit!"
    scene bg CosplayWakeMe02
    with dissolve
    R "We've just got to get Sidney on board with making us more costumes."
    R "She told me you can sell them for quite a bit more than you can make them for."
    R "Maybe we could make money off of selling the outfits as well."
    L "Well, unlike us, she's not going to be willing to do it for free."
    L "You're definitely going to have to pay her for each outfit she makes."
    L "But if you can do that, she will be more than happy to help I'm sure! I'll talk to her and convince her to do it."
    L "That's what she's going to school for after all."
    R "All right, let's do this!"
    R "And for my first decision as manager, is that we are going to go take some pictures at Dad's warehouse."
    scene bg CosplayWakeMe03
    with dissolve
    $ renpy.pause ()
    R "What?!"
    MD "It's so dirty and gross there. Plus, there are a bunch of nasty old warehouse workers that would just stare at us and cat-call us in our costumes."
    MD "Mom and I only go there every once in a while to pick up Dad from work. But even then, all the men just stare at us, and undress us with their eyes."
    R "Well, don't worry. There's an empty building where we can find some privacy, and there's a lot less workers there since the FBI has been investigating."
    if daycounter <= 5:
        R "I hope you don't mind missing a day of school to go take these pictures."
    elif daycounter == 6:
        R "I hope you don't mind spending your Saturday taking pictures."
    else:
        R "I hope you don't mind spending your Sunday taking pictures."
    scene bg CosplayWakeMe02
    with dissolve
    L "Are you kidding? We can't wait! Internet fame, here we come!"
    scene bg CosplayWakeMe04
    with dissolve
    MD "Hehehehehe."
    L "Hehehehehe."
    R "Ok, give me the costumes and I'll bring them over there on my scooter. You guys jump on your bikes and meet me over there."
    scene bg CosplayWakeMe01
    with dissolve
    MD "Ok, we'll just leave you and little [ryan] to get ready, and we'll see you over there in 30 minutes!"
    R "Little [ryan]? Why didn't you tell me I was hanging out?"
    L "Yeah right! Like you didn't know..."
    R "I didn't!"
    RT "{i}I did.{/i}"
    "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
    $ laurenlibido += 1
    "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
    $ cousinlibido += 1
    $ progress = 9
    MD "Well, whatever, we'll see you over there. And feel free to bring little [ryan] along too."
    R "Well, I don't go anywhere without him. We'll see you there soon."
    scene bg SleepBlack
    with fade
    "{i}\"33 minutes later\"{/i}"
    play music Honey
    jump emptywarehouse

label postingthepics:
    scene bg CosplayWarehouse19
    with fade
    RT "{i}Good thing the girls believed me when I told them I know how to market their pictures, because I actually have no fucking idea how to do it.{/i}"
    RT "{i}Hopefully a little bit of searching on Booble will give me the answers I need.{/i}"
    scene bg BlurryWhite
    with fade
    "{i}\"A little bit later\"{/i}"
    scene bg CosplayWarehouse20
    with fade
    RT "{i}Well, this looks promising.{/i}"
    RT "{i}A website to post cosplay photos, get paid for likes through their advertisers, and even sell the costumes.{/i}"
    RT "{i}That's perfect.{/i}"
    RT "{i}Uploading the pictures now.... and click submit.... and now we just wait to see if anyone likes them.{/i}"
    RT "{i}I've got to be sure to check the website sometime tomorrow.{/i}"
    $ picsareposted = True
    $ config_site = True
    $ cosplay_search = False
    $ cosplay_searched = True
    $ persistent.gal_Cosplay_1 = True
    $ gal_cosplay_items_01 = True
    $ laurenpictureprogress = 10
    scene bg RyansRoom01
    with fade
    $ screen_on = "ryanmap"
    call screen ryanmap

label checkforlikes:
    scene bg CosplayWarehouse20
    with fade
    RT "{i}Ok, I've got to just login with my username and password and we'll see if anyone liked the girls' pictures.{/i}"
    scene bg CosplayWarehouse22
    with dissolve
    R "Oh, hey Lauren, what's up?"
    if laurenanger >= 1:
        L "Hey pervert, I just came to see if you'd posted those pictures online yet."
    else:
        L "Hey [ryan], I just came to see if you'd posted those pictures online yet."
    R "What a coincidence, I was just checking to see if they got any likes at exactly the same moment that you walked into my room."
    R "Why don't we take a look together?"
    scene bg CosplayWarehouse23
    with dissolve
    L "Why did you post all of Mandy's pictures above mine?"
    R "I didn't, they are just appearing in the order that received the most likes."
    L "Wait.... what!?.... Mandy's pictures got more likes than mine?"
    scene bg CosplayWarehouse24
    with dissolve
    R "Well yeah, because Mandy took better pictures than you did."
    L "By better, you mean more revealing."
    R "Of course I do, look."
    scene bg CosplayWarehouse23
    with dissolve
    R "All of the pictures where she showed more skin than you, she got more likes."
    L "That slut!"
    R "She's just willing to do what it takes to get internet famous."
    R "If you'd listened to me at the photoshoot, your photos would have gotten more likes than hers."
    R "See in the ones of hers that aren't showing as much skin, your pics did better."
    scene bg CosplayWarehouse24
    with dissolve
    L "Hmmmm.... well maybe on the next shoot, I'll try not to be such a prude."
    L "I'll try to be better at following your guidance. Sorry, I just thought you were being a perv."
    R "I just want to see this venture succeed. I would love to help Mom pay off her debt."
    "{i}{b}\"Lauren's Anger =0\"{/b}{/i}"
    $ laurenanger = 0
    L "Ok, I'll try harder next time, but don't push me too hard or I'll end the shoot."
    R "Ok, just as long as you're willing to be a bit open minded, and not just assume I'm trying to get just a bunch of eye candy for myself."
    L "It is eye candy though isn't it? I mean Mandy and I look really hot."
    R "Yeah, you guys did good. And if we were to get some professional equipment, like lighting, or a backdrop, or more stuff like that. Your pictures will be amazing!"
    R "I think you girls could just pull this off."
    L "Thanks, [ryan]!"
    if progress < 10:
        $ progress = 10
    $ picsarepostedcounter = 0
    $ picsareposted = False
    scene bg RyansRoom01
    with fade
    $ screen_on = "ryanmap"
    call screen ryanmap

label sidneysleepswithryan:
    if finished_wr_shoot == True:
        jump nightly_sixtynine
    if progress >= 13:
        jump awkward_sidney
    if first_htbyd_shoot == False:
        jump get_sidney_modeling
    if sidneyfingerlaurenprogress == 9:
        scene bg MyRoomNightWSidney
        RT "{i}In my bed again as always, let's see how far she'll go on her own again tonight.{/i}"
        menu:
            "What will she do?":
                play music SexMusic
                scene bg SleepBlack
                with fade
                scene bg SleepWithSidney14
                with fade
                RT "{i}Ok, she looks like she's asleep, but let's find out if she really is.{/i}"
                RT "{i}Hmmmm.... {/i}"
                scene bg SleepBlack
                with fade
                scene bg BlurryWhite
                with fade
                scene bg SleepBlack
                with fade
                RT "{i}Hmmm.... what is that feeling?.... Did I doze off?.... Where am I?.... {/i}"
                scene bg SleepWithSidney25
                with fade
                RT "{i}Oh yeah, now I remember! Better keep my eyes shut. Sidney's jerkin on my gerkin again!{/i}"
                scene bg SleepWithSidney27
                with dissolve
                ST "{i}Why can't I get enough of this?{/i}"
                scene bg SleepWithSidney26 with Dissolve(0.5)
                $ renpy.pause (0.5)
                scene bg SleepWithSidney27 with Dissolve(0.5)
                $ renpy.pause (0.5)
                scene bg SleepWithSidney26 with Dissolve(0.5)
                $ renpy.pause (0.5)
                ST "{i}Time to take the cum shower precaution again.{/i}"
                scene bg SleepWithSidney35
                with fade
                ST "{i}If I wipe it up with my panties again, he'll never be the wiser.{/i}"
                scene bg SleepWithSidney36
                with fade
                ST "{i}There we go. Now let's play a little more with this little purple helmet.{/i}"
                RT "{i}Oh, shit! I'm about to blow again! I still don't have any stamina?{/i}"
                scene bg SleepWithSidney37
                with fade
                RT "{i}And there's my sister's bare ass on my bed again, just playing with my cock as if it's just a normal everyday occurrence.{/i}"
                RT "{i}I think I've made her just as twisted as me.{/i}"
                RT "{i}But when is she going to sit on my cock?{/i}"
                RT "{i}Oh, shit!!! Just the thought!! I'm losing it again!!!{/i}"
                scene bg BlurryWhite
                with fade
                with vpunch
                with hpunch
                scene bg SleepWithSidney38
                with fade
                S "{i}(Whispering){/i} That's it little brother, cum for me.... cum right into my panties.... that's a good brother."
                ST "{i}Now to get rid of the evidence.{/i}"
                ST "{i}I don't really feel like running to the bathroom again, or sleeping on the couch. I think I'll just stay right here.{/i}"
                scene bg SleepWithSidney39
                ST "{i}After all, it's not like cum soaked panties will get me pregnant or anything.{/i}"
                RT "{i}Oh my God, she's putting her panties with my cum all over them back on!{/i}"
                scene bg SleepWithSidney43
                with fade
                ST "{i}Oh, yes.... I'll sleep good tonight with those sticky panties between my legs.{/i}"
                "{i}{b}\"Sidney's Libido +1\"{/b}{/i}"
                $ sidneylibido += 1
                RT "{i}My sister's wearing her panties with her own brother's cum on them! Shit, I'm cumming again in my own underwear!{/i}"
                scene bg BlurryWhite
                with fade
                with vpunch
                with hpunch
                scene bg SleepWithSidney43
                with fade
                $ renpy.pause ()
                scene bg SleepWithSidney42
                with dissolve
                RT "{i}Wow, that was intense!{/i}"
                RT "{i}But she didn't really go any further.{/i}"
                RT "{i}I guess it's time to start thinking of ways to make these new exciting events go even further.{/i}"
                RT "{i}Now it's time for me to get some sleep.{/i}"
                play music Honey
                scene bg SleepBlack
                with fade
                $ persistent.gal_Sidney_4 = True
                jump sleep
            "Skip event.":
                jump sleep
    if sidneyfingerlaurenprogress == 8:
        scene bg MyRoomNightWSidney
        RT "{i}Oh yes, she must be enjoying this! Even after cumming in front of her, she still wants to sleep in my bed.{/i}"
        menu:
            "Let's keep things going with Sidney.":
                play music SexMusic
                scene bg SleepBlack
                with fade
                scene bg SleepWithSidney14
                with fade
                RT "{i}Ok, she should be pretty sound asleep by now.{/i}"
                RT "{i}I'm pretty tired myself.{/i}"
                RT "{i}I'm not really sure what I should do to her next.{/i}"
                RT "{i}I guess I should just lie here and think a little bit more about how I'm going to progress this.{/i}"
                RT "{i}Hmmmm.... {/i}"
                scene bg SleepBlack
                with fade
                scene bg BlurryWhite
                with fade
                scene bg SleepBlack
                with fade
                RT "{i}Hmmm.... what is that feeling?.... Did I doze off?.... {/i}"
                scene bg SleepWithSidney25
                with fade
                RT "{i}Oh my God!! I don't dare open my eyes, but I think Sidney has grabbed my dick by her own free will and choice!!{/i}"
                scene bg SleepWithSidney27
                with dissolve
                ST "{i}Oh my God, I've made this move on my own, and not just subconsciously.{/i}"
                ST "{i}After what happened last night, I haven't been able to think of anything else.{/i}"
                scene bg SleepWithSidney26 with Dissolve(0.5)
                $ renpy.pause (0.5)
                scene bg SleepWithSidney27 with Dissolve(0.5)
                $ renpy.pause (0.5)
                scene bg SleepWithSidney26 with Dissolve(0.5)
                $ renpy.pause (0.5)
                ST "{i}I don't want to get covered in his cum again like I did last night though.{/i}"
                ST "{i}Hmmmm.... If I wipe it up with his blankets or sheets, he probably will notice.{/i}"
                ST "{i}If I wipe it up with some of my clothes, he might see that too. Plus I don't know if it stains or not.{/i}"
                ST "{i}There is one item of my clothes he doesn't ever see though.{/i}"
                scene bg SleepWithSidney35
                with fade
                ST "{i}If I wipe it up with my panties, he'll never be the wiser.{/i}"
                scene bg SleepWithSidney36
                with fade
                ST "{i}There we go. Now let's play a little more with this little purple helmet.{/i}"
                RT "{i}Oh, shit! I'm about to blow again! Why don't I have any stamina?{/i}"
                scene bg SleepWithSidney37
                with fade
                RT "{i}Maybe it's because my sister is sitting bare assed on my bed and playing with my cock.{/i}"
                RT "{i}Why in hell did she take her panties off?{/i}"
                RT "{i}Maybe she's planning on sitting on my cock!{/i}"
                RT "{i}Oh, shit!!! Just the thought!! I'm losing it!!!{/i}"
                scene bg BlurryWhite
                with fade
                with vpunch
                with hpunch
                scene bg SleepWithSidney38
                with fade
                S "{i}(Whispering){/i} That's it little brother, cum for me.... cum right into my panties.... that's a good brother."
                "{i}{b}\"Sidney's Libido +1\"{/b}{/i}"
                $ sidneylibido += 1
                ST "{i}Now to get rid of the evidence.{/i}"
                scene bg SleepWithSidney34
                with fade
                RT "{i}Holy Hell! She made me bust on purpose! Right into her panties!{/i}"
                RT "{i}Will she go further? Do I just leave it up to her now?{/i}"
                RT "{i}There's always tomorrow night to see if she'll go further.{/i}"
                $ sidneyfingerlaurenprogress = 9
                $ sidneypictureprogress = 10
                play music Honey
                scene bg SleepBlack
                with fade
                jump sleep
            "Just sleep.":
                jump sleep
    elif sidneyfingerlaurenprogress == 7:
        scene bg MyRoomNightWSidney
        RT "{i}Sweet! She came back!{/i}"
        menu:
            "Let's keep things going with Sidney.":
                play music SexMusic
                scene bg SleepBlack
                with fade
                scene bg SleepWithSidney14
                with fade
                RT "{i}Ok, she should be pretty sound asleep by now.{/i}"
                RT "{i}Time to have some more fun.{/i}"
                scene bg SleepWithSidney15
                with dissolve
                $ renpy.pause ()
                scene bg SleepWithSidney16
                with dissolve
                $ renpy.pause ()
                scene bg SleepWithSidney17
                with dissolve
                $ renpy.pause ()
                RT "{i}Ok, I'm all ready. Let's see if I can get her into position again without waking her up.{/i}"
                scene bg SleepWithSidney18
                with dissolve
                RT "{i}Ok, and now to just move her hand into place.{/i}"
                scene bg SleepWithSidney19
                with dissolve
                RT "{i}Ohh.... ho.... hngggg.... wow!{/i}"
                RT "{i}She just started gripping like before! Like she was expecting it.{/i}"
                RT "{i}Oh my God!! I've got my own sister gripping my naked cock again!{/i}"
                RT "{i}My own sister has my cock in her soft lovely hands! I love having her sleep in my room!{/i}"
                RT "{i}I've got to really try hard not to just lose my load right now!{/i}"
                RT "{i}Ok, [ryan] concentrate! I don't want to ruin it already!{/i}"
                scene bg SleepWithSidney20
                with dissolve
                RT "{i}Now, I just have to give her a little pinch again, and act like I'm still asleep.{/i}"
                scene bg SleepWithSidney21
                with dissolve
                ST "{i}Huh.... did.... what?.... {/i}"
                ST "{i}Is that [ryan]'s cock in my hands again?.... {/i}"
                scene bg SleepWithSidney25
                with dissolve
                ST "{i}It looks like he is still asleep.{/i}"
                S "{i}(whispering){/i} pssst.... [ryan].... are you asleep?"
                ST "{i}Good, he's sound asleep.{/i}"
                scene bg SleepWithSidney27
                with dissolve
                ST "{i}I just can't control myself.{/i}"
                ST "{i}Why do I want to do this so bad?{/i}"
                scene bg SleepWithSidney26 with Dissolve(0.5)
                $ renpy.pause (0.5)
                scene bg SleepWithSidney27 with Dissolve(0.5)
                $ renpy.pause (0.5)
                scene bg SleepWithSidney26 with Dissolve(0.5)
                $ renpy.pause (0.5)
                ST "{i}I need to get a closer look.{/i}"
                scene bg SleepWithSidney28
                with fade
                ST "{i}My old boyfriend said the top of the penis is the most sensitive.{/i}"
                ST "{i}It's so soft and smooth.{/i}"
                RT "{i}Shit! She's playing with my head!!!!{/i}"
                RT "{i}That feels so good!!!!{/i}"
                RT "{i}I'm not going to be able to hold back much longer.{/i}"
                scene bg SleepWithSidney29
                with dissolve
                ST "{i}Holy shit! His veins are just bulging!{/i}"
                ST "{i}And the way it's just throbbing and twitching in my hand.... {/i}"
                ST "{i}It's almost like he's about to.... oh.... no.... {/i}"
                scene bg BlurryWhite
                with fade
                with vpunch
                with hpunch
                scene bg SleepWithSidney30
                with fade
                ST "{i}Holy shit!!{/i}"
                ST "{i}All over my face!!{/i}"
                scene bg BlurryWhite
                with fade
                with vpunch
                with hpunch
                scene bg SleepWithSidney31
                with fade
                ST "{i}Fuck, he's still going!{/i}"
                scene bg BlurryWhite
                with fade
                with vpunch
                with hpunch
                scene bg SleepWithSidney32
                with fade
                ST "{i}Why won't it stop?!!{/i}"
                scene bg SleepWithSidney33
                with fade
                ST "{i}What in the actual fuck was that?{/i}"
                ST "{i}I didn't know guys could cum that much.{/i}"
                ST "{i}He must have been very backed up.{/i}"
                ST "{i}Maybe he's not jacking off every free moment like I thought he was.{/i}"
                ST "{i}I am just covered in my own brother's cum!{/i}"
                ST "{i}That is the naughtiest thing I've ever thought of!{/i}"
                ST "{i}Why do taboo things turn me on so much?{/i}"
                "{i}{b}\"Sidney's Libido +1\"{/b}{/i}"
                $ sidneylibido += 1
                RT "{i}OH MY GOD that felt so good! I think I nutted a lot.{/i}"
                RT "{i}I think all of the jacking off I've been doing has been making me able to cum more.{/i}"
                ST "{i}I need to go clean up. I think I'll spend the rest of the night on the couch.{/i}"
                scene bg SleepWithSidney34
                with dissolve
                RT "{i}She left. Did she need to go clean up?{/i}"
                RT "{i}I wonder if some of my cum ended up on her.{/i}"
                RT "{i}I hope cumming in front of her didn't freak her out too bad.{/i}"
                RT "{i}I guess I'll find out if she show's up tomorrow night.{/i}"
                $ sidneyfingerlaurenprogress = 8
                play music Honey
                scene bg SleepBlack
                with fade
                jump sleep
            "Just sleep.":
                jump sleep
    elif sidneyfingerlaurenprogress == 6:
        scene bg MyRoomNightWSidney
        RT "{i}Sweet! She came back!{/i}"
        menu:
            "Let's keep things going with Sidney.":
                play music SexMusic
                scene bg SleepBlack
                with fade
                scene bg SleepWithSidney14
                with fade
                RT "{i}Ok, she should be pretty sound asleep by now.{/i}"
                RT "{i}Time to have some more fun.{/i}"
                scene bg SleepWithSidney15
                with dissolve
                $ renpy.pause ()
                scene bg SleepWithSidney16
                with dissolve
                $ renpy.pause ()
                scene bg SleepWithSidney17
                with dissolve
                $ renpy.pause ()
                RT "{i}Ok, I'm all ready. Let's see if I can get her into position again without waking her up.{/i}"
                scene bg SleepWithSidney18
                with dissolve
                RT "{i}Ok, and now to just move her hand into place.{/i}"
                scene bg SleepWithSidney19
                with dissolve
                RT "{i}Ohh.... ho.... hngggg.... wow!{/i}"
                RT "{i}She just started gripping like before! Like she was expecting it.{/i}"
                RT "{i}Oh my God!! I've got my own sister gripping my naked cock again!{/i}"
                RT "{i}My own sister has my cock in her soft lovely hands! I love having her sleep in my room!{/i}"
                RT "{i}I've got to really try hard not to just lose my load right now!{/i}"
                RT "{i}Ok, [ryan] concentrate! I don't want to ruin it already!{/i}"
                scene bg SleepWithSidney20
                with dissolve
                RT "{i}Now, I just have to give her a little pinch again, and act like I'm still asleep.{/i}"
                scene bg SleepWithSidney21
                with dissolve
                ST "{i}Huh.... did.... what?.... {/i}"
                ST "{i}What's.... in my hands?.... {/i}"
                scene bg SleepWithSidney22
                with dissolve
                ST "{i}Oh, shit! Not again!.... {/i}"
                scene bg SleepWithSidney25
                with dissolve
                ST "{i}Wait.... Is he still asleep?{/i}"
                S "{i}(whispering){/i} pssst.... [ryan].... are you asleep?"
                ST "{i}Good, he's sound asleep.{/i}"
                scene bg SleepWithSidney27
                with dissolve
                ST "{i}I've never held a cock this big in my hand before.{/i}"
                ST "{i}I can feel his blood pumping through his throbbing veins!{/i}"
                ST "{i}I wonder if I.... {/i}"
                scene bg SleepWithSidney26 with Dissolve(0.5)
                $ renpy.pause (0.5)
                scene bg SleepWithSidney27 with Dissolve(0.5)
                $ renpy.pause (0.5)
                scene bg SleepWithSidney26 with Dissolve(0.5)
                $ renpy.pause (0.5)
                R "Hnnnngggghhhh..."
                scene bg SleepWithSidney23
                with dissolve
                $ renpy.pause ()
                scene bg SleepWithSidney24
                with fade
                ST "{i}Oh, God! Was he waking up?{/i}"
                ST "{i}I think I almost gave him an orgasm!{/i}"
                ST "{i}Thank God my brother is a deep sleeper.{/i}"
                ST "{i}What's gotten into me?{/i}"
                ST "{i}What was I thinking?{/i}"
                ST "{i}I really do have pent up sexual frustration.{/i}"
                ST "{i}But to try to release it on my own brother?{/i}"
                ST "{i}What is wrong with me?{/i}"
                ST "{i}Why did it turn me on to have his cock throbbing in my hand?{/i}"
                "{i}{b}\"Sidney's Libido +1\"{/b}{/i}"
                $ sidneylibido += 1
                ST "{i}Shit, Sidney! Think of something else, of something that's not sexy. Not like your brother's penis!{/i}"
                ST "{i}Shit! I just admitted to myself that I think my brother's penis is sexy!{/i}"
                ST "{i}AAAARRRGGGHHH.... get a grip, Sidney!{/i}"
                ST "{i}Just go back to sleep!{/i}"
                ST "{i}Just go back to sleep!{/i}"
                scene bg SleepWithSidney40
                with dissolve
                ST "{i}.... just.... go.... to.... sleep.... my brother's penis.... {/i}"
                scene bg SleepWithSidney24
                with dissolve
                ST "{i}No! Don't think about your brother's penis! Just go to sleep!{/i}"
                ST "{i}Just go to sleep.... just go to sleep.... {/i}"
                scene bg SleepWithSidney41
                with dissolve
                $ renpy.pause ()
                scene bg SleepWithSidney42
                with dissolve
                RT "{i}Dammit!{/i}"
                RT "{i}I ruined it by making that involuntary groan!{/i}"
                RT "{i}How far would she have gone if I'd just kept my mouth shut?{/i}"
                RT "{i}I guess I'll find out next time, if she keeps coming back to sleep in here.{/i}"
                RT "{i}She hasn't left yet so that's a good sign.{/i}"
                RT "{i}I guess I'll just have to wait until tomorrow night to know for sure.{/i}"
                scene bg SleepWithSidney40
                with dissolve
                $ renpy.pause ()
                $ sidneyfingerlaurenprogress = 7
                play music Honey
                scene bg SleepBlack
                with fade
                jump sleep
            "Just sleep.":
                jump sleep
    elif sidneyfingerlaurenprogress == 5:
        scene bg MyRoomNightWSidney
        menu:
            "Let's keep things going with Sidney.":
                play music SexMusic
                scene bg SleepBlack
                with fade
                scene bg SleepWithSidney14
                with fade
                RT "{i}Ok, she should be pretty sound asleep by now.{/i}"
                RT "{i}Time to have a little fun.{/i}"
                scene bg SleepWithSidney15
                with dissolve
                $ renpy.pause ()
                scene bg SleepWithSidney16
                with dissolve
                $ renpy.pause ()
                scene bg SleepWithSidney17
                with dissolve
                $ renpy.pause ()
                RT "{i}Ok, I'm all ready. Let's see if I can get her into position without waking her up.{/i}"
                scene bg SleepWithSidney18
                with dissolve
                RT "{i}Ok, and now to just move her hand into place.{/i}"
                scene bg SleepWithSidney19
                with dissolve
                RT "{i}Ohh.... ho.... hngggg.... wow!{/i}"
                RT "{i}She just started gripping like she was expecting it.{/i}"
                RT "{i}Oh my God!! I've got Sidney gripping my naked cock!{/i}"
                RT "{i}Sidney has my cock in her soft lovely hands! This worked out better than I could have hoped for!{/i}"
                RT "{i}I've got to really try hard not to just lose my load right now!{/i}"
                RT "{i}Ok, [ryan] concentrate! I don't want to ruin it already!{/i}"
                scene bg SleepWithSidney20
                with dissolve
                RT "{i}Now, I just have to give her a little pinch, and act like I'm still asleep.{/i}"
                scene bg SleepWithSidney21
                with dissolve
                ST "{i}Huh.... did.... what?.... {/i}"
                ST "{i}What's.... in my hands?.... {/i}"
                scene bg SleepWithSidney22
                with dissolve
                ST "{i}Oh, shit!.... {/i}"
                scene bg SleepWithSidney23
                with dissolve
                $ renpy.pause ()
                scene bg SleepWithSidney24
                with fade
                ST "{i}Oh, God! I've done it again!{/i}"
                ST "{i}Why can't I just keep my hands to myself while I'm sleeping?{/i}"
                ST "{i}Thank God my brother is a deep sleeper.{/i}"
                ST "{i}Do I need to ask [ryan] to tie my hands before I go to sleep?{/i}"
                ST "{i}Then he'd probably take advantage of me.{/i}"
                ST "{i}What am I saying? I'm the one who molests everyone in their sleep.{/i}"
                ST "{i}Do I just have a ton of pent up sexual frustration like Mom said?{/i}"
                ST "{i}Does my body subconsciously need the sexual contact?{/i}"
                ST "{i}I can't believe I grabbed my brother's dick!{/i}"
                ST "{i}That was such a big handful!{/i}"
                ST "{i}He's way bigger than my old boyfriend.{/i}"
                "{i}{b}\"Sidney's Libido +1\"{/b}{/i}"
                $ sidneylibido += 1
                ST "{i}Shit, Sidney! Stop thinking about your brother's penis!{/i}"
                ST "{i}What is wrong with me?{/i}"
                ST "{i}Just go back to sleep!{/i}"
                ST "{i}Just go back to sleep!{/i}"
                scene bg SleepWithSidney40
                with dissolve
                ST "{i}.... just.... go.... to.... sleep.... my brother's penis.... {/i}"
                scene bg SleepWithSidney24
                with dissolve
                ST "{i}No! Don't think about your brother's penis! Just go to sleep!{/i}"
                ST "{i}Just go to sleep.... just go to sleep.... {/i}"
                scene bg SleepWithSidney41
                with dissolve
                $ renpy.pause ()
                scene bg SleepWithSidney42
                with dissolve
                RT "{i}Oh, that was awesome!{/i}"
                RT "{i}I hope that didn't scare her too much.{/i}"
                RT "{i}I really hope she comes back again tomorrow night so I can continue our progress.{/i}"
                RT "{i}She hasn't left yet, so that's a good sign.{/i}"
                RT "{i}I guess I'll just have to wait until tomorrow night to know for sure.{/i}"
                scene bg SleepWithSidney40
                with dissolve
                $ renpy.pause ()
                $ sidneyfingerlaurenprogress = 6
                play music Honey
                scene bg SleepBlack
                with fade
                jump sleep
            "Just sleep.":
                jump sleep
    else:
        scene bg SleepBlack
        with fade
        RT "{i}Ok.... I hear her coming.... she's opening the door.... just pretend you're asleep.{/i}"
        S "Pssstttt.... hey, [ryan].... are you awake?"
        scene bg BlurryWhite
        with fade
        scene bg SleepWithSidney11
        with fade
        R "Hey, Sidney. What are you doing in my room in the middle of the night?"
        S "You said I could come wake you if I heard any noises in the night."
        R "Yeah, I remember."
        R "But I checked things out and didn't see anything."
        S "Still, I'm pretty shaken up by the thought that someone could be watching me sleep."
        S "Do you mind if I sleep in here so I'm not alone?"
        R "Well, why don't you sleep with Lauren or Mom?"
        RT "{i}Hehehehe.... {/i}"
        S ".... Umm.... I uh.... just feel safer with you."
        R "You said you think Mom is probably stronger than me."
        S "Yeah, well.... I was just being a bratty sister."
        R "Well, as long as you're willing to admit that, than I guess I'll let you sleep in here with me."
        R "But don't you usually sleep in your panties?"
        S "Yeah, well I'd be an idiot to sleep with a suspected pervert in nothing but my panties wouldn't I?"
        R "Oh, hardy har har!"
        R "I'm not a pervert."
        RT "{i}I'm the worst kind of pervert.{/i}"
        S "(Just stares at you)"
        R "Ok, maybe just a little teenage curiosity."
        R "But don't worry, I'm a very deep sleeper."
        R "I take melatonin at night to help me sleep."
        R "You should try it."
        S "I don't think I need it, I've been sleeping pretty deeply myself lately."
        ST "{i}With the exception of a few interruptions.{/i}"
        S "So, will you scoot over and let me sleep with you? I'm pretty tired."
        R "Ok.... I guess.... but you owe me."
        S "Owe you what?"
        R "I don't know, I'll think of something."
        S "Whatever!"
        S "Oh, and honey?"
        R "Yeah?"
        S "Don't tell Mom or Lauren that I'm sleeping with you."
        R "Why not?"
        S "They would just think it's weird, in fact I'm going to get up early enough that no one will suspect I'm sleeping in here."
        S "It will give me a great excuse to do a morning jog in the park."
        S "Promise not to tell."
        R "Ok, I can do that."
        scene bg SleepWithSidney12
        with dissolve
        RT "{i}Ohhohoho yes.... that was a lot of work, but now the real fun can begin.{/i}"
        RT "{i}She's had a rough few nights, so I think I'll give her a break right now, but tomorrow.... we'll just see.{/i}"
        $ sidneyfingerlaurenprogress = 5
        $ sidneypictureprogress = 9
        jump sleep

############  LOUNGE  ################################################  LOUNGE  ###################################################  LOUNGE  ######################################  LOUNGE  #######################################################

label getsidneyoffthecouch:
    scene bg SidneyLoungeNight
    with fade
    RT "{i}I feel kind of bad for everything I've put Sidney through to get her out of Lauren's room.{/i}"
    RT "{i}Now she's stuck sleeping on this uncomfortable couch. Maybe there's a way to make it better for both of us.{/i}"
    menu:
        "Try to make it better.":
            scene bg SleepWithSidney01
            with dissolve
            RT "{i}Ok, it's time to put my acting skills to the test.{/i}"
            RT "{i}It looks like she's pretty out of it, I'd better make some noise to wake her up.{/i}"
            menu:
                "Bang your metal bat on the floor":
                    scene bg SleepWithSidney02
                    with fade
                    S "[ryan]? Why are you making so much noise..."
                    S "And why do you have a bat in your hands?"
                    S "Are you here to kill me?"
                    R "Oh, haha.... sorry to wake you, I didn't mean to drop my bat."
                    R "I was just checking the house to make sure everything is safe."
                    R "I heard some noises around the house like someone was sneaking around."
                    S "It was probably just Mom or Lauren using the bathroom."
                    R "It wasn't, I already checked on them."
                    R "It sounded more like a window opening and closing, and booted footsteps sneaking around in this room."
                    R "Did you see or hear anything?"
                    S "No, are you sure you heard these noises?"
                    R "Not completely, but with everything that's going on with the Mafia and the FBI, I thought it's very possible for either of them to be sneaking around in here."
                    R "Just the thought of them sneaking around and spying on us in our underwear as we sleep motivated me to grab a bat and come check things out."
                    S "Well, go back to sleep, I'm sure you were just imagining things."
                    R "Ok, but if you hear anything, come and tell me, ok?"
                    S "Yeah right, I think I'd go tell Mom she's probably stronger than you."
                    R "No, she's not!"
                    S "Ok whatever, just go back to sleep."
                    R "Ok, goodnight."
                    scene bg SleepWithSidney03
                    with dissolve
                    ST "{i}Shit, I hope [ryan] was just imagining things.{/i}"
                    ST "{i}What if some pervert from the FBI or Mafia was snooping around in here?{/i}"
                    ST "{i}I would be their first victim. I have no protection of a room or a locked door.{/i}"
                    ST "{i}Shit, now I'm just freaking myself out.{/i}"
                    ST "{i}I've got to control my imagination.{/i}"
                    menu:
                        "Make some creepy noises":
                            ST "{i}Oh, shit! What was that?{/i}"
                            scene bg SleepWithSidney04
                            with dissolve
                            ST "{i}I'm getting out of here. There should be room in Mom's bed.{/i}"
                            RT "{i}Shit, she's going to Mom's bed. I really was hoping that she would come to me for protection.{/i}"
                            RT "{i}Well, I've got a few more tricks up my sleeve.{/i}"
                            jump mominbedwithsidney
        "Just leave her alone, you've tortured her enough.":
            $ screen_on = "sidneyloungenightmap"
            call screen sidneyloungenightmap

#############  KITCHEN  ###############################################  KITCHEN  ##################################################  KITCHEN  #####################################  KITCHEN  #####################################################

label givesidneymoneyforcosplay:
    scene bg SidneyKitchen01
    with fade
    S "Hey [ryan], what can I do for you?"
    R "I've got the money for Lauren's cosplay outfit."
    scene bg SidneyKitchen03
    with dissolve
    S "Are you sure? Aren't you supposed to be saving up to pay the DeCapos at the end of the week?"
    menu:
        "I have enough money for both." if money >= 800:
            R "I've been working really hard lately, and I should have enough to pay for Lauren's outfit and the weekly Mafia debt."
            "{i}{b}\"Sidney's Respect +1\"{/b}{/i}"
            $ sidneyrespect += 1
            S "Good for you little brother! Keep it up and maybe we will be able to get along without Dad."
            "{i}\"Money - $400\"{/i}"
            $ money -= 400
        "Mom can just work it off at the club this week.":
            R "Why should I be the one responsible to pay off the debt every week, Mom can help out too."
            S "Yeah, well I guess it's your money. You earned it. If you'd rather pay me for a sexy costume for your little sister then keep Mom safe from the Mafia that's up to you."
            R "Oh please, our mom isn't in any danger."
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
    S "I don't believe your motives are entirely altruistic."
    RT "{i}She's flashing me again!{/i}"
    RT "{i}Is she doing this on purpose?{/i}"
    RT "{i}Or could she really be this clueless.{/i}"
    R "Whatever.... I'll just check back in a few days to see if you're done."
    scene bg SidneyInKitchen
    with fade
    $ screen_on = "sidneykitchenmap"
    call screen sidneykitchenmap

label kitchencosplayfitting:
    scene bg CosplayIntro01
    with fade
    R "Oh hey, it's cousin Mandy! That outfit looks incredible."
    R "You look just like Novina from \"SolarCraft\"!"
    MD "Thanks! Sidney made it for me weeks ago. She really did do an incredible job!"
    R "I'll say, and Lauren's outfit must be Penny Roberson from \"Missing in Space\". Way to pick the sexiest red-head on TV!"
    R "Though I must say, this costume is a little sexier than the one she wears."
    L "Haha, you idiot."
    R "Why didn't you tell me the outfits were done?"
    S "I was going to get them all fitted and then come and find you."
    R "They look great!"
    L "Why do you care that our outfits are done?"
    S "Didn't [ryan] tell you, he's the one who paid for your outfit, Lauren."
    L "Really? Why did you do that?"
    R "Because it's what Dad would have done."
    S "I think it's because he wanted to see your ass in it."
    scene bg CosplayIntro02
    with dissolve
    S "Hey don't move, I'm not done yet."
    ST "{i}Wow, she really does have a great ass.{/i}"
    "{i}{b}\"Sidney's Libido +1\"{/b}{/i}"
    $ sidneylibido += 1
    L "Haha, did you really just want to check out my ass?"
    R "Of course not! I didn't even know what outfit Sidney was going to make for you."
    R "And even if she'd told me, Penny's outfit on the show doesn't quite show off her ass like that."
    S "Ok, and all done."
    scene bg CosplayIntro03
    with dissolve
    L "Ok, so how does it look from the front?"
    scene bg CosplayIntro09
    with fade
    $ renpy.pause ()
    scene bg CosplayIntro08
    with fade
    $ renpy.pause ()
    scene bg CosplayIntro03
    with fade
    R "Ummmm.... uuhh.... really great!"
    S "Haha.... I can tell by your face that you love it."
    S "And it's a good thing too. I've worked my ass off to get it ready for this convention."
    L "I know.... thank you so much.... but we really need to get going. We've already missed a ton of it!"
    MD "Don't worry too much. The best stuff doesn't happen until night anyways."
    R "Well, before you go, let's see you strike a pose."
    L "Ok.... fine.... but really quick."
    scene bg CosplayIntro04
    with dissolve
    R "Haha.... ok.... nice!.... That's just how you need to pose for the creepy fanboys that will want to take pictures of you."
    menu:
        "Now let's see how you pose when they ask you to take pics from behind.":
            if laurenaffection <= 4:
                scene bg CosplayIntro05
                with dissolve
                L "No you asshole. That's creepy for a brother to ask that, and we're in a hurry. You'll just have to use your imagination for now."
                R "But I'm the one who bought the costume for you."
                L "That doesn't buy you the right to stare at my ass!"
                L "Come on, cuz. We need to go to the convention."
            else:
                scene bg CosplayIntro06
                with dissolve
                L "Isn't it just a bit weird for a brother to ask his sister and cousin to see their asses?"
                R "I think it would be weirder if I didn't appreciate a couple sexy girls in sexy costumes."
                R "The fact that we're related has nothing to do with it."
                MD "Oh, so you think we're sexy?"
                R "I'd have to be gay to think otherwise."
                "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
                $ laurenlibido += 1
                $ cousinlibido += 1
                L "Ok, let's just do it, after all he did pay for my costume."
                scene bg CosplayIntro07
                with dissolve
                MD "Well, what do you think?"
                R "Really sexy, but Sidney should have made your shorts as revealing as Lauren's."
                S "Actually, those shorts are adjustable, they can be modified to show some cheeks."
                R "Oh awesome, let's see that!"
                MD "Haha, sorry but we don't have time."
                L "Yeah, let's go cuz, we've already missed a lot of the convention."
            MD "You're right, we have to leave this second."
            $ progress = 8
            $ sidneymakingcosplay = False
            $ cosplayoutfitcounter = 0
            scene bg Kitchen01
            with fade
            $ screen_on = "kitchenmap"
            call screen kitchenmap
        "Have a good time at the convention!":
            scene bg CosplayIntro04
            L "Thanks we will. And I really owe you for paying for my costume."
            R "I'll remember that."
            MD "Haha I'm sure you will."
            $ progress = 8
            $ sidneymakingcosplay = False
            $ cosplayoutfitcounter = 0
            scene bg Kitchen01
            with fade
            $ screen_on = "kitchenmap"
            call screen kitchenmap

#############  BATHROOM  ##############################################  BATHROOM  #################################################  BATHROOM  ############################################  BATHROOM  #############################################

label spycambath:
    scene bg bathroom01
    with fade
    menu:
        "Set up new spy-cam.":
            scene bg SpyCamBath01
            with fade
            RT "{i}So, the instructions on the spy-cam say that I can link my phone to the live video feed.{/i}"
            RT "{i}It doesn't actually record video, I can only see what's going on live.{/i}"
            RT "{i}But it does have the option for me to snap pictures when I'm watching a live stream.{/i}"
            RT "{i}Ok, let's get this baby set up.{/i}"
            scene bg SpyCamBath02
            with fade
            RT "{i}Ok, I just need to get this footstool moved over here.... {/i}"
            RT "{i}And use this screwdriver to open this vent.... {/i}"
            RT "{i}Dammit!.... That hurt!.... {/i}"
            RT "{i}You stupid goddamn piece of shit! Open up.{/i}"
            RT "{i}You son of a bitch mother fucker!{/i}"
            RT "{i}Finally!.... Ok, just place it so it can see between the grates.... {/i}"
            RT "{i}And turn it on!{/i}"
            scene bg SpyCamBath03
            with dissolve
            RT "{i}Ok, perfect.... It should be streaming to my phone now.{/i}"
            scene bg SpyCamBath04
            with fade
            RT "{i}All right, just a slight adjustment so I have a good view of the shower,{/i}"
            RT "{i}.... and now I should be able to see live streams of whatever it is the girls do in here.{/i}"
            RT "{i}I can't wait! It's amazingly convenient that the girls all have predictable bathroom schedules.... hmmmm.{/i}"
            $ spycaminbath = True
            scene bg bathroom01
            with fade
            $ inventory.drop(spycam)
            $ screen_on = "bathmap"
            call screen bathmap
        "Not right now.":
            $ screen_on = "bathmap"
            call screen bathmap

label laurenbathspycam:
    scene bg BathroomDoor
    RT "{i}Lauren's taking her early morning shower before school. Thanks to my new spy-cam, I can take a peek.{/i}"
    menu:
        "Take a peek.":
            if spiedlaurenbathroom == True:
                scene bg BathroomDoor
                RT "{i}She's already showered, she'll be coming out that door any second. I don't want to be creeping around when she does.{/i}"
                $ screen_on = "bathdoormap"
                call screen bathdoormap
            else:
                scene bg SCLaurenShowerBathDoor
                with dissolve
                play music SexMusic
                RT "{i}These little cameras have pretty decent reception and video quality.{/i}"
                scene bg LaurenInShower01
                with fade
                RT "{i}Nice! It's time for a show!{/i}"
                RT "{i}Best thousand dollars I've ever spent.{/i}"
                scene bg LaurenInShower02
                with fade
                RT "{i}The zoom function on this camera is pretty good too.{/i}"
                RT "{i}Oh, I love those tiny titties!{/i}"
                scene bg LaurenInShower03
                with fade
                RT "{i}Oh, yeah! Get that dirty body clean!{/i}"
                RT "{i}If only she'd just turn a little to the left.{/i}"
                if spycamlaurenshower == False:
                    RT "{i}Oh, well, this will still make a great picture.{/i}"
                    play sound CameraClick
                    show CamaraFlash
                    pause (0.25)
                    scene bg LaurenInShower03
                    $ renpy.pause ()
                RT "{i}Aaauhh.... I've been here too long, I'd better go before I'm caught.{/i}"
                $ spycamlaurenshower = True
                play music Honey
                scene bg BathroomDoor
                with fade
                $ screen_on = "bathdoormap"
                call screen bathdoormap
        "Never mind.":
            $ screen_on = "bathdoormap"
            call screen bathdoormap

label laurenfingerselfbath:
    if spiedlaurenbathroom == True:
        scene bg BathroomDoor
        RT "{i}She's already showered, she'll be coming out that door any second. I don't want to be creeping around when she does.{/i}"
        $ screen_on = "bathdoormap"
        call screen bathdoormap
    else:
        scene bg SCLaurenHornyBathDoor
        with dissolve
        play music SexMusic
        RT "{i}These little cameras have pretty decent reception and video quality.{/i}"
        scene bg LaurenMastBateBath01
        with fade
        RT "{i}Oh my God, yes! This is so awesome!{/i}"
        RT "{i}And thanks to modern technology I can watch it all.{/i}"
        scene LaurenShowerVideo01
        with fade
        $ renpy.pause ()
        RT "{i}She seems to be extra horny lately. I wonder if watching \"Game of Thots\" has been making her think more about incest.{/i}"
        RT "{i}Or maybe my subliminal messages are getting through to her, and she's trying to repress feelings for her brother.{/i}"
        RT "{i}Most likely she's not thinking of me at all, but I can dream!{/i}"
        RT "{i}I'm sure that little pussy is tight and inexperienced. I know she's not innocent, but I think she's still a virgin.{/i}"
        scene LaurenShowerVideo02
        with dissolve
        $ renpy.pause ()
        RT "{i}Oh, yeah!.... Getting some love from the shampoo bottle now.{/i}"
        if spycamlaurenmbatebath == False:
            RT "{i}I have to capture this moment. ok, just double tapping the screen while watching a livefeed should take a pic.{/i}"
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            hide CamaraFlash
            play sound Lauren01 loop
            $ renpy.pause ()
            RT "{i}Perfect! That beautiful image will be on my computer next time I check it.{/i}"
        RT "{i}Look at that tiny pussy stretch!{/i}"
        if shampoobottle == 3:
            RT "{i}Fucking lucky bottle!{/i}"
            jump laurenfingerselfbathcontinued
        if shampoobottle == 2:
            while spycamlaurenmbatebath == False:
                RT "{i}Maybe she's not quite as tight as I imagined, if she normally sticks random household objects up her pussy.{/i}"
                RT "{i}I wonder what Lauren would think if she knew that same bottle has been in Sidney's pussy and Mom's ass.{/i}"
                jump laurenfingerselfbathcontinued
            if shampoobottle == 2:
                RT "{i}I wonder what Lauren would think if she knew that same bottle has been in Sidney's pussy and Mom's ass.{/i}"
                jump laurenfingerselfbathcontinued
        if shampoobottle == 1:
            while spycamlaurenmbatebath == False:
                RT "{i}Maybe she's not quite as tight as I imagined, if she normally sticks random household objects up her pussy.{/i}"
                RT "{i}Is it normal to be jealous of a shampoo bottle? Getting inside one girl in this house would be a major achievement, this bottle's gotten in two!{/i}"
                jump laurenfingerselfbathcontinued
            if shampoobottle == 1:
                RT "{i}Is it normal to be jealous of a shampoo bottle? Getting inside one girl in this house would be a major achievement, this bottle's gotten in two!{/i}"
                jump laurenfingerselfbathcontinued
        if shampoobottle == 0:
            while spycamlaurenmbatebath == False:
                RT "{i}Maybe she's not quite as tight as I imagined, if she normally sticks random household objects up her pussy.{/i}"
                RT "{i}I guess anything's a dildo if you're brave enough.{/i}"
                jump laurenfingerselfbathcontinued
            if shampoobottle == 0:
                RT "{i}I guess anything's a dildo if you're brave enough.{/i}"
                jump laurenfingerselfbathcontinued

label laurenfingerselfbathcontinued:
    RT "{i}She looks really into it. Could she possibly be imagining that the shampoo bottle is me?{/i}"
    RT "{i}She'll need more than a shampoo bottle to get herself ready for me.{/i}"
    if laurenmbateonspycam:
        RT "{i}Oh!.... I think she's about there!{/i}"
        scene bg LaurenShowerClimax
        with fade
        with hpunch
        $ renpy.pause ()
        RT "{i}Holy shit!.... She's trying to give the shower head some competition!{/i}"
        RT "{i}What an amazing talent! She'd be a natural porn star.{/i}"
    else:
        pass
    RT "{i}Maybe I should take off before someone sees me just staring at my phone in front of the bathroom door.{/i}"
    RT "{i}Thanks for the show Lauren!{/i}"
    "{i}{b}\"Lauren's Libido -5\"{/b}{/i}"
    if spycamlaurenmbatebath == False:
        $ shampoobottle += 1
    else:
        pass
    $ spiedlaurenbathroom = True
    $ laurenlibido -= 5
    $ timeofdaycounter += 1
    $ spycamlaurenmbatebath = True
    $ persistent.gal_Lauren_3 = True
    play music Honey
    stop sound
    scene bg BathroomDoor
    with fade
    $ screen_on = "bathdoormap"
    call screen bathdoormap

label sidneybathspycam:
    scene bg BathroomDoor
    if daycounter >= 6:
        RT "{i}Sidney must be taking a shower. Mom and Lauren don't seem to be around.{/i}"
    else:
        RT "{i}Sidney must be taking a shower. Mom and Lauren are already at school.{/i}"
    RT "{i}Thanks to my new spy-cam, I can take a peek and see.{/i}"
    menu:
        "Take a peek.":
            if spiedsidneybathroom == True:
                scene bg BathroomDoor
                RT "{i}She's already showered, she'll be coming out that door any second. I don't want to be creeping around when she does.{/i}"
                $ screen_on = "bathdoormap"
                call screen bathdoormap
            else:
                scene bg SCSidneyShowerBathDoor
                with dissolve
                play music SexMusic
                RT "{i}These little cameras have pretty decent reception and video quality.{/i}"
                scene bg SidneyInShower01
                with fade
                RT "{i}Nice! I should have made popcorn!{/i}"
                RT "{i}This is the best show in town.{/i}"
                scene bg SidneyInShower02
                with fade
                RT "{i}The zoom function on this camera is pretty good too.{/i}"
                RT "{i}She has probably got the finest ass I've ever seen, and those tan lines just make me want to nut on the spot!{/i}"
                scene bg SidneyInShower03
                with fade
                RT "{i}Oh, yeah! Wash that dirty hair!{/i}"
                RT "{i}Thank you for spreading those legs.{/i}"
                if spycamsidneyshower == False:
                    RT "{i}This will make a great picture.{/i}"
                    play sound CameraClick
                    show CamaraFlash
                    pause (0.25)
                    scene bg SidneyInShower03
                    $ renpy.pause ()
                RT "{i}Aaauhh.... I've been here too long, I'd better go before I'm caught.{/i}"
                $ spycamsidneyshower = True
                play music Honey
                scene bg BathroomDoor
                with fade
                $ screen_on = "bathdoormap"
                call screen bathdoormap
        "Never mind.":
            $ screen_on = "bathdoormap"
            call screen bathdoormap

label sidneyfingerselfbath:
    if spiedsidneybathroom == True:
        scene bg BathroomDoor
        RT "{i}She's already showered, she'll be coming out that door any second. I don't want to be creeping around when she does.{/i}"
    else:
        scene bg SCSidneyHornyBathDoor
        with dissolve
        play music SexMusic
        RT "{i}These little spy-cameras are awesome.{/i}"
        scene bg SidneyMastBateBath01
        with fade
        RT "{i}She's watching herself finger her own pussy in the glass!{/i}"
        RT "{i}Little does she know she has an audience of more than one.{/i}"
        scene SidneyShowerVideo01
        with fade
        $ renpy.pause ()
        RT "{i}What would she do if she knew her own brother was staring at her every move?{/i}"
        RT "{i}I hope her recent experiences with Lauren in bed, have at least opened her mind to some new taboo ideas.{/i}"
        RT "{i}Most likely she's not thinking about messing around with me or Lauren yet, but I can dream!{/i}"
        RT "{i}I heard her say that she's no virgin, but that she hasn't enjoyed her sexual experiences up to now. Maybe I can change that.{/i}"
        scene SidneyShowerVideo02
        with dissolve
        $ renpy.pause ()
        RT "{i}Oh, nice!.... Got to get those hard to reach places.{/i}"
        if spycamsidneymbatebath == False:
            RT "{i}I have to capture this moment. ok, just double tapping the screen while watching a livefeed should take a pic.{/i}"
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            hide CamaraFlash
            play sound Sidney01 loop
            $ renpy.pause ()
            RT "{i}Perfect! That beautiful image will be on my computer next time I check it.{/i}"
        RT "{i}Look at that bottle just slide in and out!{/i}"
        if shampoobottle == 3:
            RT "{i}Fucking lucky bottle!{/i}"
            jump sidneyfingerselfbathcontinued
        if shampoobottle == 2:
            while spycamsidneymbatebath == False:
                RT "{i}Wow, a shampoo bottle, she needs to get herself a real toy. Or better yet, a real man, or at least one who's conveniently located.{/i}"
                RT "{i}I wonder what Sidney would think if she knew that same bottle has been in Lauren's pussy and Mom's ass.{/i}"
                jump sidneyfingerselfbathcontinued
            if shampoobottle == 2:
                RT "{i}I wonder what Sidney would think if she knew that same bottle has been in Lauren's pussy and Mom's ass.{/i}"
                jump sidneyfingerselfbathcontinued
        if shampoobottle == 1:
            while spycamsidneymbatebath == False:
                RT "{i}Wow, a shampoo bottle, she needs to get herself a real toy. Or better yet, a real man, or at least one who's conveniently located.{/i}"
                RT "{i}Is it normal to be jealous of a shampoo bottle? Getting inside one girl in this house would be a major achievement, this bottle's gotten in two!{/i}"
                jump sidneyfingerselfbathcontinued
            if shampoobottle == 1:
                RT "{i}Is it normal to be jealous of a shampoo bottle? Getting inside one girl in this house would be a major achievement, this bottle's gotten in two!{/i}"
                jump sidneyfingerselfbathcontinued
        if shampoobottle == 0:
            while spycamsidneymbatebath == False:
                RT "{i}Wow, a shampoo bottle, she needs to get herself a real toy. Or better yet, a real man, or at least one who's conveniently located.{/i}"
                RT "{i}I guess anything's a dildo if you're brave enough.{/i}"
                jump sidneyfingerselfbathcontinued
            if shampoobottle == 0:
                RT "{i}I guess anything's a dildo if you're brave enough.{/i}"
                jump sidneyfingerselfbathcontinued

label sidneyfingerselfbathcontinued:
    RT "{i}I feel really sad that Sidney has to get herself off like this, when there's someone right here who's all ready and willing to help her out.{/i}"
    RT "{i}She'll need more than a shampoo bottle to get herself ready for me.{/i}"
    RT "{i}Maybe I can find something in the online store to help her with that.{/i}"
    if sidneymbateonspycam:
        RT "{i}Oh!.... I think she's about there!{/i}"
        scene bg SidneyShowerClimax
        with fade
        with hpunch
        $ renpy.pause ()
        RT "{i}Holy shit!.... This is like shower-ception!{/i}"
        RT "{i}But if this is a dream, I don't want to wake up.... But....{/i}"
    else:
        pass
    RT "{i}Maybe I should take off before someone sees me just staring at my phone in front of the bathroom door.{/i}"
    RT "{i}Thanks Sidney! Same time tomorrow?{/i}"
    "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
    if spycamsidneymbatebath == False:
        $ shampoobottle += 1
    else:
        pass
    $ persistent.gal_Sidney_2 = True
    $ spiedsidneybathroom = True
    $ sidneylibido -= 5
    $ timeofdaycounter += 1
    $ spycamsidneymbatebath = True
    play music Honey
    stop sound
    scene bg BathroomDoor
    with fade
    $ screen_on = "bathdoormap"
    call screen bathdoormap

label mombathspycam:
    scene bg BathroomDoor
    RT "{i}Mom's taking her after school shower. Thanks to my new spy-cam, I can take a peek.{/i}"
    menu:
        "Take a peek.":
            if spiedmombathroom == True:
                scene bg BathroomDoor
                RT "{i}She's already showered, she'll be coming out that door any second. I don't want to be creeping around when she does.{/i}"
                $ screen_on = "bathdoormap"
                call screen bathdoormap
            else:
                scene bg SCMomShowerBathDoor
                with dissolve
                play music SexMusic
                RT "{i}These little cameras have pretty decent reception and video quality.{/i}"
                scene bg MomInShower01
                with fade
                RT "{i}Oh, Mom looks so tired, probably all the stress of everything going on!{/i}"
                RT "{i}I wish I could go in there and give her some physical comfort.{/i}"
                scene bg MomInShower02
                with fade
                RT "{i}I wonder what's going through Mom's head.{/i}"
                scene bg MomInShower03
                with fade
                RT "{i}Oh, good! The show's getting better. I could never get tired of looking at her in the shower from this angle!{/i}"
                RT "{i}Although Mom does look really good on a pole.{/i}"
                if spycammomshower == False:
                    RT "{i}I'll just have to save this for later.{/i}"
                    play sound CameraClick
                    show CamaraFlash
                    pause (0.25)
                    scene bg MomInShower03
                    $ renpy.pause ()
                RT "{i}Aaauhh.... I've been here too long, I'd better go before I'm caught.{/i}"
                $ spycammomshower = True
                play music Honey
                scene bg BathroomDoor
                with fade
                $ screen_on = "bathdoormap"
                call screen bathdoormap
        "Never mind.":
            $ screen_on = "bathdoormap"
            call screen bathdoormap

label momfingerselfbath:
    if spiedmombathroom == True:
        scene bg BathroomDoor
        RT "{i}She's already showered, she'll be coming out that door any second. I don't want to be creeping around when she does.{/i}"
    else:
        scene bg SCMomHornyBathDoor
        with dissolve
        play music SexMusic
        RT "{i}Alright, show me what I paid $1000 for.{/i}"
        scene bg MomMastBateBath01
        with fade
        RT "{i}Oh man, Mom's going for it!{/i}"
        RT "{i}Without Dad, she must be feeling pretty lonely.{/i}"
        scene MomShowerVideo01
        with fade
        $ renpy.pause ()
        RT "{i}Oh.... ho.... ho.... Mom really is a naughty girl, giving her asshole a little attention too.{/i}"
        RT "{i}What is it that's making her so horny?{/i}"
        RT "{i}Is she thinking about all those men watching her strip?{/i}"
        RT "{i}Is she thinking about me sneaking into the club to watch her strip?{/i}"
        scene MomShowerVideo02
        with dissolve
        $ renpy.pause ()
        RT "{i}Did she just stick that shampoo bottle into her ass?{/i}"
        if spycammommbatebath == False:
            RT "{i}I have to capture this moment. ok, just double tapping the screen while watching a livefeed should take a pic.{/i}"
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            hide CamaraFlash
            play sound Mom02 loop
            $ renpy.pause ()
            RT "{i}Awesome! I've got a picture of Mom pleasuring her asshole!{/i}"
        RT "{i}It goes in so easy! Dad doesn't seem like the kind of guy that would be into anal. Maybe she's always had to pleasure herself this way.{/i}"
        RT "{i}Well, I'll be happy to fill that void for her, so to speak.{/i}"
        if shampoobottle == 3:
            RT "{i}Fucking lucky bottle!{/i}"
            jump momfingerselfbathcontinued
        if shampoobottle == 2:
            while spycammommbatebath == False:
                RT "{i}What I wouldn't give to be in that bottle's place right now!{/i}"
                RT "{i}I can't believe Sidney and Lauren are using this same bottle to get themselves off.{/i}"
                jump momfingerselfbathcontinued
            if shampoobottle == 2:
                RT "{i}I can't believe Sidney and Lauren are using this same bottle to get themselves off.{/i}"
                jump momfingerselfbathcontinued
        if shampoobottle == 1:
            while spycammommbatebath == False:
                RT "{i}What I wouldn't give to be in that bottle's place right now!{/i}"
                RT "{i}Is it normal to be jealous of a shampoo bottle? Getting inside one girl in this house would be a major achievement, this bottle's gotten in two!{/i}"
                jump momfingerselfbathcontinued
            if shampoobottle == 1:
                RT "{i}Is it normal to be jealous of a shampoo bottle? Getting inside one girl in this house would be a major achievement, this bottle's gotten in two!{/i}"
                jump momfingerselfbathcontinued
        if shampoobottle == 0:
            while spycammommbatebath == False:
                RT "{i}What I wouldn't give to be in that bottle's place right now!{/i}"
                RT "{i}I guess anything's a dildo if you're brave enough.{/i}"
                jump momfingerselfbathcontinued
            if shampoobottle == 0:
                RT "{i}I guess anything's a dildo if you're brave enough.{/i}"
                jump momfingerselfbathcontinued

label momfingerselfbathcontinued:
    RT "{i}Soon Mom won't have to resort to such measures to get her itches scratched.{/i}"
    RT "{i}Her son will be more than willing.{/i}"
    RT "{i}I've just got to get her to overcome her already formed ideas of where that kind of love should come from.{/i}"
    RT "{i}I've still got a lot of work ahead of me.{/i}"
    if mommbateonspycam:
        RT "{i}Oh!.... I think she's about there!{/i}"
        scene bg MomShowerClimax
        with fade
        with hpunch
        $ renpy.pause ()
        RT "{i}Holy shit!.... If her spray range gets much bigger, she's going to ruin my camara!{/i}"
        RT "{i}And I don't think I can send her the bill for a replacement.{/i}"
    else:
        pass
    RT "{i}Great job today, Mom! I'll try to make it to your next show.{/i}"
    "{i}{b}\"Mom's Libido -5\"{/b}{/i}"
    if spycammommbatebath == False:
        $ shampoobottle += 1
    else:
        pass
    $ spiedmombathroom = True
    if daycounter == 6:
        $ momlibido -=5
    else:
        $ momlibido -= 5
        $ timeofdaycounter += 1
    $ spycammommbatebath = True
    $ persistent.gal_mom_3 = True
    play music Honey
    stop sound
    scene bg BathroomDoorNight
    with fade
    $ screen_on = "bathdoornightmap"
    call screen bathdoornightmap

#############  JACKY'S ROOM  ##############################  JACKY'S ROOM  #################################  JACKY'S ROOM  ###########################  JACKY'S ROOM  ##################################  JACKY'S ROOM  ##########################################  JACKY'S ROOM  #####

label spycammomroom:
    scene bg MomsRoom
    with fade
    menu:
        "Set up new spy-cam.":
            scene bg SpyCamMomBedroom13
            with fade
            RT "{i}So, the instructions on the spy-cam say that I can link my phone to the live video feed.{/i}"
            RT "{i}It doesn't actually record video, I can only see what's going on live.{/i}"
            RT "{i}But it does have the option for me to snap pictures when I'm watching a live stream.{/i}"
            RT "{i}Ok, let's get this baby set up.{/i}"
            scene bg SpyCamMomBedroom14
            with fade
            RT "{i}Ok, I just need to climb up on this cabinet.... {/i}"
            RT "{i}And use this screwdriver to open this vent.... {/i}"
            RT "{i}Ouch.... dammit!.... That hurt!.... {/i}"
            RT "{i}You cunt sucking douche mouth!{/i}"
            RT "{i}Chode licking, cock gobbler!{/i}"
            RT "{i}Finally!.... Ok, just place it so it can see between the grates.... {/i}"
            RT "{i}And turn it on!{/i}"
            scene bg SpyCamMomBedroom15
            with dissolve
            RT "{i}Ok, perfect.... It should be streaming to my phone now.{/i}"
            scene bg SpyCamMomBedroom05
            with fade
            RT "{i}All right, just a slight adjustment so I have a good view of the bed.{/i}"
            RT "{i}.... and now I should be able to see live streams of whatever it is Mom does in here.{/i}"
            RT "{i}I can't wait! It's amazingly convenient that Mom has a predictable daily schedule.... hmmmm.{/i}"
            $ spycaminmomroom = True
            scene bg MomsRoom
            with fade
            $ inventory.drop(spycam)
            $ screen_on = "momsmap"
            call screen momsmap
        "Not right now.":
            $ screen_on = "momsmap"
            call screen momsmap

label momhornybedroom:
    if spycaminmomroom == True:
        while timeofdaycounter == 5:
            scene bg MomDoorNight
            with fade
            play sound Mom02 loop
            RT "{i}Hmmm.... I wonder why the door is locked?{/i}"
            RT "{i}Wait.... is that Mom moaning?{/i}"
            RT "{i}I should check it out.{/i}"
            menu:
                "Use spy-cam.":
                    jump momspycamroomhorny
                "Not right now.":
                    RT "{i}Sounds like things are winding down. I'm probably too late to see anything good.{/i}"
                    stop sound
                    "{i}{b}\"Mom's Libido -5\"{/b}{/i}"
                    $ momlibido -= 5
                    $ screen_on = "momdoornightmap"
                    call screen momdoornightmap
        if spycaminmomroom == True:
            scene bg MomDoor
            with fade
            play sound Mom02 loop
            RT "{i}Hmmm.... I wonder why the door is locked?{/i}"
            RT "{i}Wait.... is that Mom moaning?{/i}"
            RT "{i}I should check it out.{/i}"
            menu:
                "Use spy-cam.":
                    jump momspycamroomhorny
                "Not right now.":
                    RT "{i}Sounds like things are winding down. I'm probably too late to see anything good.{/i}"
                    stop sound
                    "{i}{b}\"Mom's Libido -5\"{/b}{/i}"
                    $ momlibido -= 5
                    $ screen_on = "momdoormap"
                    call screen momdoormap
    if timeofdaycounter == 5:
        scene bg MomDoorNight
        with fade
        play sound Mom02 loop
        RT "{i}Hmmm.... I wonder why the door is locked?{/i}"
        RT "{i}Wait.... is that Mom moaning? I've got to figure out a way to see in there!{/i}"
        $ momlibido -= 5
        "{i}{b}\"Mom's Libido -5\"{/b}{/i}"
        stop sound fadeout 1.0
        $ screen_on = "momdoornightmap"
        call screen momdoornightmap
    else:
        scene bg MomDoor
        with fade
        play sound Mom02 loop
        RT "{i}The door's locked, she must be getting dressed. {p}Wait, is that moaning I hear?{p}I'm pretty sure that's moaning.{/i}"
        "{i}{b}\"Mom's Libido -5\"{/b}{/i}"
        $ momlibido -= 5
        RT "{i}I've got to figure out a way to spy on her.{/i}"
        stop sound fadeout 1.0
        $ screen_on = "momdoormap"
        call screen momdoormap

label momspycamroom:
    if aunts_new_uniform == True:
        jump yoga_with_aunt
    else:
        scene bg MomDoor
        with fade
        RT "{i}She's always got her door locked in the morning when she does yoga and gets ready for the day. Now I can see exactly what she does.{/i}"
        menu:
            "Peek through spy-cam.":
                play music SexMusic
                scene bg SpyCamMomBedroom17
                with dissolve
                RT "{i}That's how she stays in such great shape.{/i}"
                scene bg SpyCamMomBedroom01
                with fade
                $ renpy.pause ()
                scene bg SpyCamMomBedroom02
                with dissolve
                $ renpy.pause ()
                scene bg SpyCamMomBedroom06
                with fade
                RT "{i}Oh yes, finally the good part.{/i}"
                scene bg SpyCamMomBedroom07
                with dissolve
                RT "{i}Just.... wow.... what a body!{/i}"
                scene bg SleepBlack
                with fade
                "{i}\"A little while later.\"{/i}"
                scene bg SpyCamMomBedroom03
                with fade
                RT "{i}Looks like she's about done, I should get out of here before she walks out that door.{/i}"
                $ timeofdaycounter += 1
                play music Honey
                scene bg MomDoor
                with fade
                $ screen_on = "momdoormap"
                call screen momdoormap
            "Never mind.":
                $ screen_on = "momdoormap"
                call screen momdoormap

label momspycamroomhorny:
    if timeofdaycounter == 5:
        scene bg SpyCamMomBedroom16
        with dissolve
        play music SexMusic
        RT "{i}Looks like Mom's feeling a little lonely without Dad, I've got to convince her that she can come to me for this kind of attention.{/i}"
    else:
        scene bg SpyCamMomBedroom18
        with dissolve
        RT "{i}Looks like Mom's feeling a little lonely without Dad, I've got to convince her that she can come to me for this kind of attention.{/i}"
    scene bg SpyCamMomBedroom04
    with fade
    RT "{i}Good timing on my part, I think she's just getting started.{/i}"
    stop sound
    scene bg SpyCamMomBedroom08
    with fade
    $ mom_squirted_today_bedroom = True
    if mommbateonspycam == False:
        RT "{i}Is that a fucking butt plug?{/i}"
        RT "{i}I guess Mom's into that kind of thing.{/i}"
        MT "{i}Time to give the new plug a try.{/i}"
        MT "{i}Uuug.... why did [dad_name] force anal on me? Now it's hard for me to even cum without something in my ass.{/i}"
    else:
        RT "{i}There's that butt plug again.{/i}"
        MT "{i}Uuug.... why did [dad_name] force anal on me? Now it's hard for me to even cum without something in my ass.{/i}"
    scene bg SpyCamMomBedroom09
    with fade
    if mommbateonspycam == False:
        RT "{i}Holy.... she's sliding it in slowly.... I've got to get a picture.{/i}"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg SpyCamMomBedroom09
        RT "{i}There's some future jack-off material.{/i}"
        MT "{i}Oh God, it's been a little while.{/i}"
    else:
        RT "{i}The look on her face.... It looks so uncomfortable.... does she really like it?{/i}"
        MT "{i}Fucking [dad_name]!{/i}"
    scene bg SpyCamMomBedroom10
    with fade
    play sound Mom02 loop
    if mommbateonspycam == False:
        RT "{i}She needs a vibrator too to get off?{/i}"
        RT "{i}I hope when my time comes I can compete with all that hardware.{/i}"
    else:
        RT "{i}I hope one day soon I can pleasure her better than a vibrator and butt plug can.{/i}"
    if first_bath_hjob and mommbateonspycam:
        MT "{i}Oh God!.... I crossed the touching line with [ryan]!{/i}"
        MT "{i}I actually gave him a handjob!{/i}"
        MT "{i}That cock is so huge, I could barely wrap my hand around it!{/i}"
        MT "{i}I know it can't be good for him to have so much cum stored up, but God, seeing that big of a cumshot really turned me on!{/i}"
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        MT "{i}Oh, Fuuuuuuck!!!{/i}"
        scene bg SpyCamMomBedroom12 with Dissolve(0.3)
        $ renpy.pause (2.0)
        MT "{i}Oh my God!.... I'm squirting!!{/i}"
        scene bg SpyCamMomBedroom20
        with fade
        stop sound
        MT "{i}Oh Yes!! Fucking squirted again!{/i}"
        MT "{i}What's the harm in a little imagination?{/i}"
        MT "{i}But that felt sooooo good!{/i}"
        MT "{i}What's wrong with me.{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Squirting is obviously hereditary.{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Mom's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Mom just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Mom's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Mom's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ momlibido -= 5
        if timeofdaycounter == 5:
            scene bg MomDoorNight
            with fade
            RT "{i}I should probably go get some sleep now, maybe.... {/i}"
            play music Honey
            $ screen_on = "momdoornightmap"
            call screen momdoornightmap
        else:
            scene bg MomDoor
            with fade
            RT "{i}I should run before I get caught.{/i}"
            $ screen_on = "momdoormap"
            call screen momdoormap
    if tv_events == 4 and mommbateonspycam:
        MT "{i}Holy fuck.... It looked like Lauren was licking up cum in the lounge.{/i}"
        MT "{i}She said it was frosting from a cinnamon roll, but what if it was [ryan]'s cum?{/i}"
        MT "{i}I know that's absolutely ridiculous.... and that thought shouldn't turn me on.... but.... fuck, that's hot to imagine!{/i}"
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        MT "{i}Oh, Fuuuuuuck!!!{/i}"
        scene bg SpyCamMomBedroom12 with Dissolve(0.3)
        $ renpy.pause (2.0)
        MT "{i}Oh my God!.... I'm squirting!!{/i}"
        scene bg SpyCamMomBedroom20
        with fade
        stop sound
        MT "{i}Oh Yes!! Fucking squirted again!{/i}"
        MT "{i}What's the harm in a little imagination?{/i}"
        MT "{i}But that felt sooooo good!{/i}"
        MT "{i}What's wrong with me.{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Squirting is obviously hereditary.{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Mom's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Mom just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Mom's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Mom's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ momlibido -= 5
        if timeofdaycounter == 5:
            scene bg MomDoorNight
            with fade
            RT "{i}I should probably go get some sleep now, maybe.... {/i}"
            play music Honey
            $ screen_on = "momdoornightmap"
            call screen momdoornightmap
        else:
            scene bg MomDoor
            with fade
            RT "{i}I should run before I get caught.{/i}"
            $ screen_on = "momdoormap"
            call screen momdoormap
    if aunt_second_visit and mommbateonspycam:
        MT "{i}I can't believe I made my sister get such a sexy uniform.... I mean it serves her right!{/i}"
        MT "{i}But [ryan] and her are home all alone! Could [ryan] resist the temptation to take advantage of her?{/i}"
        MT "{i}Haha.... I know Camille would never let him.... but its still pretty sexy to imagine!{/i}"
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        MT "{i}Oh, Fuuuuuuck!!!{/i}"
        scene bg SpyCamMomBedroom12 with Dissolve(0.3)
        $ renpy.pause (2.0)
        MT "{i}Oh my God!.... I'm squirting!!{/i}"
        scene bg SpyCamMomBedroom20
        with fade
        stop sound
        MT "{i}Oh Yes!! Fucking squirted again!{/i}"
        MT "{i}And that time, I thought of [ryan] fucking Camille.{/i}"
        MT "{i}What's the harm in a little imagination. He would never really do that.{/i}"
        MT "{i}But that felt sooooo good!{/i}"
        MT "{i}What's wrong with me.{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Squirting is obviously hereditary.{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Mom's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Mom just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Mom's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Mom's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ momlibido -= 5
        if timeofdaycounter == 5:
            scene bg MomDoorNight
            with fade
            RT "{i}I should probably go get some sleep now, maybe.... {/i}"
            play music Honey
            $ screen_on = "momdoornightmap"
            call screen momdoornightmap
        else:
            scene bg MomDoor
            with fade
            RT "{i}I should run before I get caught.{/i}"
            $ screen_on = "momdoormap"
            call screen momdoormap
    if jr_watched and mommbateonspycam:
        MT "{i}Oh how have I let those stupid computer games let me get so out of control?{/i}"
        MT "{i}[ryan] and I fucking watched each other masturbate!{/i}"
        MT "{i}I can't believe the size of that kids cock.{/i}"
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        MT "{i}Oh, Fuuuuuuck!!!{/i}"
        scene bg SpyCamMomBedroom12 with Dissolve(0.3)
        $ renpy.pause (2.0)
        MT "{i}Oh my God!.... I'm squirting!!{/i}"
        scene bg SpyCamMomBedroom20
        with fade
        stop sound
        MT "{i}Oh Yes!! Fucking squirted again!{/i}"
        MT "{i}And that time, I thought of [ryan] fucking me on purpose.{/i}"
        MT "{i}What's the harm in a little imagination. I would never really do that.{/i}"
        MT "{i}But that just felt sooooo good!{/i}"
        MT "{i}What's wrong with me.{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Squirting is obviously hereditary.{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Mom's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Mom just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Mom's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Mom's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ momlibido -= 5
        if timeofdaycounter == 5:
            scene bg MomDoorNight
            with fade
            RT "{i}I should probably go get some sleep now, maybe.... {/i}"
            play music Honey
            $ screen_on = "momdoornightmap"
            call screen momdoornightmap
        else:
            scene bg MomDoor
            with fade
            RT "{i}I should run before I get caught.{/i}"
            $ screen_on = "momdoormap"
            call screen momdoormap
    if fixed_washer >= 1 and mommbateonspycam:
        MT "{i}Was [ryan] really just trying to fix the washing machine, or was he dry humping my ass on purpose?{/i}"
        MT "{i}I swear I could feel his huge cock hot dogging my ass cheeks as he tried to fix those belts.{/i}"
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        MT "{i}Oh, Fuuuuuuck!!!{/i}"
        scene bg SpyCamMomBedroom12 with Dissolve(0.3)
        $ renpy.pause (2.0)
        MT "{i}Oh my God!.... I'm squirting!!{/i}"
        scene bg SpyCamMomBedroom20
        with fade
        stop sound
        MT "{i}Oh Yes!! Fucking squirted again!{/i}"
        MT "{i}And that time, I thought of [ryan] fucking me on purpose.{/i}"
        MT "{i}What's the harm in a little imagination. I would never really do that.{/i}"
        MT "{i}But that just felt sooooo good!{/i}"
        MT "{i}What's wrong with me.{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Squirting is obviously hereditary.{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Mom's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Mom just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Mom's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Mom's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ momlibido -= 5
        if timeofdaycounter == 5:
            scene bg MomDoorNight
            with fade
            RT "{i}I should probably go get some sleep now, maybe.... {/i}"
            play music Honey
            $ screen_on = "momdoornightmap"
            call screen momdoornightmap
        else:
            scene bg MomDoor
            with fade
            RT "{i}I should run before I get caught.{/i}"
            $ screen_on = "momdoormap"
            call screen momdoormap
    if lectureprogress <= 4 and mompictureprogress >= 5 and mommbateonspycam:
        MT "{i}I can't believe I let [ryan] show me those types of games in my office.{/i}"
        MT "{i}I wonder if they make him imagine those same scenarios with me.{/i}"
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        MT "{i}Oh, Fuuuuuuck!!!{/i}"
        scene bg SpyCamMomBedroom12 with Dissolve(0.3)
        $ renpy.pause (2.0)
        MT "{i}Oh my God!.... I'm squirting!!{/i}"
        scene bg SpyCamMomBedroom20
        with fade
        stop sound
        MT "{i}Oh Yes!! Fucking squirted again!{/i}"
        MT "{i}And that time, I thought of [ryan] fucking me on purpose.{/i}"
        MT "{i}What's the harm in a little imagination. I would never really do that.{/i}"
        MT "{i}But that just felt sooooo good!{/i}"
        MT "{i}What's wrong with me.{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Squirting is obviously hereditary.{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Mom's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Mom just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Mom's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Mom's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ momlibido -= 5
        if timeofdaycounter == 5:
            scene bg MomDoorNight
            with fade
            RT "{i}I should probably go get some sleep now, maybe.... {/i}"
            play music Honey
            $ screen_on = "momdoornightmap"
            call screen momdoornightmap
        else:
            scene bg MomDoor
            with fade
            RT "{i}I should run before I get caught.{/i}"
            $ screen_on = "momdoormap"
            call screen momdoormap
    else:
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom11 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        if mommbateonspycam == False:
            $ familyofsquirters += 1
            $ mommbateonspycam = True
            if ntrcontent == True:
                MT "{i}I can't believe how much I need to have both of my holes filled.{/i}"
                MT "{i}How would it be to fuck two men at the same time?{/i}"
            else:
                MT "{i}I can't believe how much I enjoy anal now.{/i}"
            scene bg SpyCamMomBedroom11 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom10 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom11 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom10 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom11 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom10 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom11 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom10 with Dissolve(0.3)
            $ renpy.pause (0.2)
            if ntrcontent == True:
                MT "{i}[dad_name] would never let that happen, but now that [dad_name] is gone.... {/i}"
                MT "{i}I can't let myself think that way.... {/i}"
                MT "{i}But still.... what two guys would I even want to fuck me besides my husband?{/i}"
            else:
                MT "{i}I wonder how long [dad_name] will be gone. I can't live without a real fucking for long!{/i}"
                MT "{i}If he's there for years, could I be celibate the whole time he's gone?{/i}"
                MT "{i}Who would I even fuck, if not my husband?{/i}"
            scene bg SpyCamMomBedroom11 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom10 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom11 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom10 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom11 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom10 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom11 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom10 with Dissolve(0.3)
            $ renpy.pause (0.2)
            if ntrcontent == True:
                MT "{i}Thanks to [dad_name]'s jealousy, there really aren't many men in my life.{/i}"
                MT "{i}There's a few students I could imagine being with, and then there's Joey DeCapo and his goons.{/i}"
                MT "{i}I still can't believe that asshole allows my son into his club whenever he feels like it.{/i}"
                MT "{i}Now that boy has a big penis. I don't know if I'd be able to fit him in either of my holes.{/i}"
            else:
                MT "{i}With [dad_name] being so jealous there really aren't many men in my life.{/i}"
                MT "{i}All I can really think of is stupid Joey DeCapo.... that asshole who let's my son into his club whenever he wants.{/i}"
                MT "{i}Now that boy has a big penis. I don't know if I'd be able to fit him in either of my holes.{/i}"
            scene bg SpyCamMomBedroom11 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom10 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom11 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom10 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom11 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom10 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom11 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom10 with Dissolve(0.3)
            $ renpy.pause (0.2)
            MT "{i}Oh, God!.... Why am I thinking about my son right now?{/i}"
            scene bg SpyCamMomBedroom11 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom10 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamMomBedroom11 with Dissolve(0.3)
            $ renpy.pause (0.2)
        else:
            pass
        scene bg SpyCamMomBedroom10 with Dissolve(0.3)
        $ renpy.pause (0.2)
        MT "{i}Oh, Fuuuuuuck!!!{/i}"
        scene bg SpyCamMomBedroom12 with Dissolve(0.3)
        $ renpy.pause (2.0)
        MT "{i}Oh my God!.... I'm squirting!!{/i}"
        scene bg SpyCamMomBedroom20
        with fade
        stop sound
        if mommbateonspycam == False:
            MT "{i}It's been so long since I've squirted!{/i}"
            MT "{i}I haven't done that since before I married [dad_name].{/i}"
            MT "{i}Shit, shit, shit.... I think I might have been imagining [ryan] fucking me with his huge dick.{/i}"
            MT "{i}Dammit! Having him spy on me at the club has really messed me up.{/i}"
            MT "{i}I've always been turned on by taboo things.{/i}"
            MT "{i}But I know the difference between fantasy and real life. I would never really do that.{/i}"
        else:
            MT "{i}Oh Yes!! Fucking squirted again!{/i}"
            MT "{i}And that time, I thought of [ryan] fucking me on purpose.{/i}"
            MT "{i}What's the harm in a little imagination. I would never really do that.{/i}"
        MT "{i}But that just felt sooooo good!{/i}"
        MT "{i}What's wrong with me.{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Squirting is obviously hereditary.{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Mom's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Mom just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Mom's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Mom's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ momlibido -= 5
        $ persistent.gal_mom_4 = True
        if timeofdaycounter == 5:
            scene bg MomDoorNight
            with fade
            RT "{i}I should probably go get some sleep now, maybe.... {/i}"
            play music Honey
            $ screen_on = "momdoornightmap"
            call screen momdoornightmap
        else:
            scene bg MomDoor
            with fade
            RT "{i}I should run before I get caught.{/i}"
            $ screen_on = "momdoormap"
            call screen momdoormap

label momspycamroommad:
    if timeofdaycounter == 5:
        scene bg SpyCamMomBedroom21
        with dissolve
        $ renpy.pause ()
        scene bg SpyCamMomBedroom19
        with fade
        RT "{i}Well.... not a lot of action going on right here. I should probably just go to sleep myself.{/i}"
        scene bg MomDoorNight
        with fade
        $ screen_on = "momdoornightmap"
        call screen momdoornightmap
    else:
        scene bg SpyCamMomBedroom17
        RT "{i}Looks like she's trying to blow off some steam with a little yoga.{/i}"
        scene bg SpyCamMomBedroom01
        with fade
        $ renpy.pause ()
        scene bg SpyCamMomBedroom02
        with dissolve
        RT "{i}Well.... she could be doing this for a while. I should go get ready for the day myself.{/i}"
        scene bg MomDoor
        with fade
        $ screen_on = "momdoormap"
        call screen momdoormap

label mominbedwithsidney:
    scene bg SleepWithSidney05
    with fade
    ST "{i}Mom did say I could sleep with her as long as I don't do anything weird to her in her sleep.{/i}"
    ST "{i}Oh God, I hope I don't keep doing weird stuff in my sleep.{/i}"
    scene bg SleepBlack
    with fade
    "{i}\"15 minutes later\"{/i}"
    scene bg SleepWithSidney06
    with fade
    play music SexMusic
    RT "{i}Well, they both seem to be sleeping pretty deeply. Hopefully the melatonin is still in their systems.{/i}"
    RT "{i}Mom did say that she would give Sidney only one chance, so what's it going to be?{/i}"
    RT "{i}Pussy or ass?{/i}"
    RT "{i}No, Mom's pussy and ass are mine, let's go with the titties.{/i}"
    scene bg SleepWithSidney07
    with fade
    RT "{i}Ok, so we'll just pull her undershirt down, place Sidney's hand into place,{/i}"
    RT "{i}.... and now time for a pinch to wake Mom up. I'd better run to my room after this, if things work like I hope, Sidney will be joining me in just a few minutes.{/i}"
    RT "{i}Ok.... how about one right on the nipple.{/i}"
    menu:
        "Pinch.":
            scene bg SleepWithSidney08
            with fade
            M "What in the world?.... Sidney wake up! What are you doing in my room?"
            S "Huh.... what's going on?"
            M "Sidney, I told you that you could only sleep with me if you didn't grope me like you did your sister."
            S "Oh, no! What did I do this time?"
            M "You pulled my shirt down and pinched my nipple!"
            S "Really? I did it again? Goddammit!"
            M "Language, honey!"
            S "Sorry..."
            M "I need you to go back out there and sleep on the couch."
            S "But Mom, I heard creepy noises out there, and so did [ryan]!"
            scene bg SleepWithSidney09
            with dissolve
            M "Oh, you're just imagining things. The doors and windows are locked. You're perfectly safe."
            M "Now, get out!"
            S "But, Mom!"
            M "Go!"
            scene bg SleepWithSidney10
            with dissolve
            MT "{i}Shit, what is wrong with that girl?{/i}"
            MT "{i}She cannot keep her hands to herself in her sleep.{/i}"
            M "I mean, I guess I can't complain too much, at least her finger wasn't in my ass."
            MT "{i}.... although I do like things in my ass.... {/i}"
            "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
            $ momlibido += 1
            play music Honey
            jump sidneysleepswithryan

##############  LAUREN'S ROOM  ###################################################  LAUREN'S ROOM  ###############################################  LAUREN'S ROOM  #######################################################################################

label spycamlaurenroom:
    scene bg LaurenRoom01
    with fade
    menu:
        "Set up new spy-cam.":
            scene bg SpyCamLaurenBedroom17
            with fade
            RT "{i}So, the instructions on the spy-cam say that I can link my phone to the live video feed.{/i}"
            RT "{i}It doesn't actually record video, I can only see what's going on live.{/i}"
            RT "{i}But it does have the option for me to snap pictures when I'm watching a live stream.{/i}"
            RT "{i}Ok, let's get this baby set up.{/i}"
            scene bg SpyCamLaurenBedroom18
            with fade
            RT "{i}Ok, I just need to get this vanity stool moved over here.... {/i}"
            RT "{i}And use this screwdriver to open this vent.... {/i}"
            RT "{i}Dammit!.... That hurt!.... {/i}"
            RT "{i}You cock nosed boner face! Open up.{/i}"
            RT "{i}You filthy sons of horkers! Son of a bitch mother fucker!{/i}"
            RT "{i}Finally!.... Ok, just place it so it can see between the grates.... {/i}"
            RT "{i}And turn it on!{/i}"
            scene bg SpyCamLaurenBedroom19
            with dissolve
            RT "{i}Ok, perfect.... It should be streaming to my phone now.{/i}"
            scene bg SpyCamLaurenBedroom12
            with fade
            RT "{i}All right, just a slight adjustment so I have a good view of the bed and in front of the mirror,{/i}"
            RT "{i}.... and now I should be able to see live streams of whatever it is the girls do in here.{/i}"
            RT "{i}I can't wait! It's amazingly convenient that the girls all have predictable daily schedules.... hmmmm.{/i}"
            $ spycaminlaurenroom = True
            scene bg LaurenRoom01
            with fade
            $ inventory.drop(spycam)
            $ screen_on = "laurenmap"
            call screen laurenmap
        "Not right now.":
            $ screen_on = "laurenmap"
            call screen laurenmap

label laurenspycamroom:
    scene bg LaurenDoor
    with fade
    RT "{i}Lauren must be getting dressed, the door's locked. Not like that's going to stop me anymore.{/i}"
    menu:
        "Peek through spy-cam.":
            play music SexMusic
            scene bg SpyCamLaurenBedroom21
            with dissolve
            RT "{i}Yep, she's getting dressed alright, with no idea I'm watching her.{/i}"
            scene bg SpyCamLaurenBedroom20
            with fade
            RT "{i}Come on, do something. Is the camera frozen? She's just staring at her tits in the mirror.{/i}"
            RT "{i}Well, to be fair, I think I would do the same if I had those cute little mosquito bites.{/i}"
            RT "{i}Well, I think I'll check back later sometime to see if she's doing anything more interesting.{/i}"
            play music Honey
            scene bg LaurenDoor
            with fade
            $ screen_on = "laurendoormap"
            call screen laurendoormap
        "Not now.":
            scene bg LaurenDoor
            with dissolve
            $ screen_on = "laurendoormap"
            call screen laurendoormap

label laurenspycamroommad:
    if timeofdaycounter == 5:
        scene bg SpyCamLaurenBedroom15
        with dissolve
        RT "{i}It's pretty late, probably not much going on in there.{/i}"
        scene bg SpyCamLaurenBedroom14
        with fade
        RT "{i}Yeah, no reason to sit here and stare, I just need to get her to forgive me so she won't lock her door at night.{/i}"
        scene bg LaurenDoorNight
        with fade
        $ screen_on = "laurendoornightmap"
        call screen laurendoornightmap
    else:
        scene bg SpyCamLaurenBedroom10
        with dissolve
        RT "{i}I don't know what I expected, it looks like she's just snapping selfies on her bed.{/i}"
        scene bg SpyCamLaurenBedroom01
        with fade
        RT "(mocking voice in head) {i}\"Felt kinda cute, don't know, might delete later\"{/i}"
        RT "{i}We were much better friends before she got that stupid phone. Now I've constantly got to compete for her attention.{/i}"
        RT "{i}Well, if I'm going to win this competition, I've got to get her to be completely reliant on me. Then when she needs something, I can ask for something in return.{/i}"
        scene bg LaurenDoor
        with fade
        $ screen_on = "laurendoormap"
        call screen laurendoormap

label laurenspycamroomhorny:
    if timeofdaycounter == 5:
        scene bg SpyCamLaurenBedroom11
        with dissolve
        play music SexMusic
        RT "{i}Oh, thank you, thank you spy-cam, before I could only imagine what was going on in here.{/i}"
    else:
        scene bg SpyCamLaurenBedroom13
        with dissolve
        RT "{i}Oh, thank you, thank you spy-cam, before I could only imagine what was going on in here.{/i}"
    scene bg SpyCamLaurenBedroom02
    with fade
    RT "{i}Oh yeah, look at her go. What an ass!{/i}"
    stop sound
    scene bg SpyCamLaurenBedroom04
    with fade
    if laurenmbateonspycam == False:
        RT "{i}What is she doing with Mr. Snuggles?{/i}"
        RT "{i}Is that a strap-on?{/i}"
    else:
        RT "{i}Oh, she's pulling out Mr. Snuggles again.{/i}"
        RT "{i}Some dudes just get all the luck.{/i}"
    scene bg SpyCamLaurenBedroom05
    with fade
    play sound Lauren01 loop
    RT "{i}I gave her that stuffy as a gift for her birthday 1 year ago.{/i}"
    RT "{i}Could that mean she's thinking about me?{/i}"
    RT "{i}I guess it could also mean she's into furrys.{/i}"
    RT "{i}Oh God, please don't let that be so.{/i}"
    scene bg SpyCamLaurenBedroom06
    with fade
    if tv_events >= 5 and laurenmbateonspycam:
        LT "{i}I can't believe what [ryan] and I have been doing in the lounge, right in front of Sidney, and Mom right behind the next door!{/i}"
        LT "{i}Oh God.... I can remember what [ryan]'s cock tasted like.{/i}"
        LT "{i}And as good as this feels, it will never feel as good as the orgasm [ryan] gave me when he was fingering my pussy and ass!{/i}"
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        LT "{i}Oh SHIIIIIT!!!{/i}"
        scene bg SpyCamLaurenBedroom09 with Dissolve(0.3)
        $ renpy.pause (2.0)
        LT "{i}Oh my God!.... I'm squirting!!{/i}"
        LT "{i}I can't control it!, I'm squirting!{/i}"
        scene bg SpyCamLaurenBedroom22
        with dissolve
        stop sound
        LT "{i}Oh my God, I squirted again!{/i}"
        LT "{i}I've got to stop thinking of [ryan] when I masturbate!{/i}"
        LT "{i}But that just felt sooooo good!{/i}"
        LT "{i}What's wrong with me.{/i}"
        LT "{i}Maybe I should stop watching \"Game of Thots.\"{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Is it something Mom's feeding them?{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Lauren's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Lauren just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Lauren's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Lauren's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ laurenlibido -= 5
        if timeofdaycounter == 5:
            scene bg SpyCamLaurenBedroom16
            with fade
            $ sawlaurensquirt = True
            RT "{i}Guess it's time for lights out, ohhhhh and she's cuddling the very soggy Mr. Snuggles. How cute!{/i}"
            scene bg LaurenDoorNight
            with dissolve
            play music Honey
            $ screen_on = "laurendoornightmap"
            call screen laurendoornightmap
        else:
            scene bg LaurenDoor
            with fade
            RT "{i}I should run before I get caught.{/i}"
            play music Honey
            $ screen_on = "laurendoormap"
            call screen laurendoormap
    if first_lauren_grind and laurenmbateonspycam:
        LT "{i}[ryan] was so heroic how he defended me from Agent Diaz!{/i}"
        LT "{i}I could tell it turned him on as much as it did me!{/i}"
        LT "{i}The only thing keeping his cock from penetrating me was my soaking wet panties!{/i}"
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        LT "{i}Oh SHIIIIIT!!!{/i}"
        scene bg SpyCamLaurenBedroom09 with Dissolve(0.3)
        $ renpy.pause (2.0)
        LT "{i}Oh my God!.... I'm squirting!!{/i}"
        LT "{i}I can't control it!, I'm squirting!{/i}"
        scene bg SpyCamLaurenBedroom22
        with dissolve
        stop sound
        LT "{i}Oh my God, I squirted again!{/i}"
        LT "{i}I've got to stop thinking of [ryan] when I masturbate!{/i}"
        LT "{i}But that just felt sooooo good!{/i}"
        LT "{i}What's wrong with me.{/i}"
        LT "{i}Maybe I should stop watching \"Game of Thots.\"{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Is it something Mom's feeding them?{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Lauren's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Lauren just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Lauren's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Lauren's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ laurenlibido -= 5
        if timeofdaycounter == 5:
            scene bg SpyCamLaurenBedroom16
            with fade
            $ sawlaurensquirt = True
            RT "{i}Guess it's time for lights out, ohhhhh and she's cuddling the very soggy Mr. Snuggles. How cute!{/i}"
            scene bg LaurenDoorNight
            with dissolve
            play music Honey
            $ screen_on = "laurendoornightmap"
            call screen laurendoornightmap
        else:
            scene bg LaurenDoor
            with fade
            RT "{i}I should run before I get caught.{/i}"
            play music Honey
            $ screen_on = "laurendoormap"
            call screen laurendoormap
    if first_diaz_dance and laurenmbateonspycam:
        LT "{i}I can't believe that pervert Diaz!{/i}"
        LT "{i}Making me dance in that outft?.... Spanking my almost bare ass!{/i}"
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        LT "{i}Oh SHIIIIIT!!!{/i}"
        scene bg SpyCamLaurenBedroom09 with Dissolve(0.3)
        $ renpy.pause (2.0)
        LT "{i}Oh my God!.... I'm squirting!!{/i}"
        LT "{i}I can't control it!, I'm squirting!{/i}"
        scene bg SpyCamLaurenBedroom22
        with dissolve
        stop sound
        LT "{i}Oh my God, I squirted again!{/i}"
        LT "{i}Shit! And I did it thinking about a girl!{/i}"
        LT "{i}But that just felt sooooo good!{/i}"
        LT "{i}What's wrong with me.{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Is it something Mom's feeding them?{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Lauren's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Lauren just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Lauren's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Lauren's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ laurenlibido -= 5
        if timeofdaycounter == 5:
            scene bg SpyCamLaurenBedroom16
            with fade
            $ sawlaurensquirt = True
            RT "{i}Guess it's time for lights out, ohhhhh and she's cuddling the very soggy Mr. Snuggles. How cute!{/i}"
            scene bg LaurenDoorNight
            with dissolve
            play music Honey
            $ screen_on = "laurendoornightmap"
            call screen laurendoornightmap
        else:
            scene bg LaurenDoor
            with fade
            RT "{i}I should run before I get caught.{/i}"
            play music Honey
            $ screen_on = "laurendoormap"
            call screen laurendoormap
    if finished_htbyd_shoot and laurenmbateonspycam:
        LT "{i}I can't believe I dry humped [ryan] after the photoshoot!{/i}"
        LT "{i}His cock was so hard!{/i}"
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        LT "{i}Oh SHIIIIIT!!!{/i}"
        scene bg SpyCamLaurenBedroom09 with Dissolve(0.3)
        $ renpy.pause (2.0)
        LT "{i}Oh my God!.... I'm squirting!!{/i}"
        LT "{i}I can't control it!, I'm squirting!{/i}"
        scene bg SpyCamLaurenBedroom22
        with dissolve
        stop sound
        LT "{i}Oh my God, I squirted again!{/i}"
        LT "{i}I've got to stop thinking of [ryan] when I masturbate!{/i}"
        LT "{i}But that just felt sooooo good!{/i}"
        LT "{i}What's wrong with me.{/i}"
        LT "{i}Maybe I should stop watching \"Game of Thots.\"{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Is it something Mom's feeding them?{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Lauren's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Lauren just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Lauren's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Lauren's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ laurenlibido -= 5
        if timeofdaycounter == 5:
            scene bg SpyCamLaurenBedroom16
            with fade
            $ sawlaurensquirt = True
            RT "{i}Guess it's time for lights out, ohhhhh and she's cuddling the very soggy Mr. Snuggles. How cute!{/i}"
            scene bg LaurenDoorNight
            with dissolve
            play music Honey
            $ screen_on = "laurendoornightmap"
            call screen laurendoornightmap
        else:
            scene bg LaurenDoor
            with fade
            RT "{i}I should run before I get caught.{/i}"
            play music Honey
            $ screen_on = "laurendoormap"
            call screen laurendoormap
    elif photoshoot_1 and laurenmbateonspycam:
        LT "{i}I can't believe we asked [ryan] to take those pictures of us when we were dressed so slutty!{/i}"
        LT "{i}I could tell he was loving it from the enormous bulge in his pants!{/i}"
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        LT "{i}Oh SHIIIIIT!!!{/i}"
        scene bg SpyCamLaurenBedroom09 with Dissolve(0.3)
        $ renpy.pause (2.0)
        LT "{i}Oh my God!.... I'm squirting!!{/i}"
        LT "{i}I can't control it!, I'm squirting!{/i}"
        scene bg SpyCamLaurenBedroom22
        with dissolve
        stop sound
        LT "{i}Oh my God, I squirted again!{/i}"
        LT "{i}I've got to stop thinking of [ryan] when I masturbate!{/i}"
        LT "{i}But that just felt sooooo good!{/i}"
        LT "{i}What's wrong with me.{/i}"
        LT "{i}Maybe I should stop watching \"Game of Thots.\"{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Is it something Mom's feeding them?{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Lauren's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Lauren just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Lauren's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Lauren's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ laurenlibido -= 5
        if timeofdaycounter == 5:
            scene bg SpyCamLaurenBedroom16
            with fade
            $ sawlaurensquirt = True
            RT "{i}Guess it's time for lights out, ohhhhh and she's cuddling the very soggy Mr. Snuggles. How cute!{/i}"
            scene bg LaurenDoorNight
            with dissolve
            play music Honey
            $ screen_on = "laurendoornightmap"
            call screen laurendoornightmap
        else:
            scene bg LaurenDoor
            with fade
            RT "{i}I should run before I get caught.{/i}"
            play music Honey
            $ screen_on = "laurendoormap"
            call screen laurendoormap
    else:
        LT "{i}Oh God Tanning Chatum, fuck my tight little pussy!{/i}"
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        if laurenmbateonspycam == False:
            $ familyofsquirters += 1
            $ laurenmbateonspycam = True
            LT "{i}I wonder if Tanning is as big as my brother?{/i}"
            scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
            $ renpy.pause (0.2)
            LT "{i} I don't even think his dick would fit in my pussy.{/i}"
            scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
            $ renpy.pause (0.2)
            LT "{i}Oh, God!.... He'd probably rip me in half.{/i}"
            scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
            $ renpy.pause (0.2)
            LT "{i}Oh, God!.... Why am I thinking about my brother?{/i}"
            RT "{i}I've got to get a picture of this!{/i}"
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            play sound Lauren01 loop
            scene bg SpyCamLaurenBedroom06
            $ renpy.pause ()
            scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom08 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamLaurenBedroom07 with Dissolve(0.3)
            $ renpy.pause (0.2)
        else:
            pass
        scene bg SpyCamLaurenBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        LT "{i}Oh SHIIIIIT!!!{/i}"
        scene bg SpyCamLaurenBedroom09 with Dissolve(0.3)
        $ renpy.pause (2.0)
        LT "{i}Oh my God!.... I'm squirting!!{/i}"
        LT "{i}I can't control it!, I'm squirting!{/i}"
        scene bg SpyCamLaurenBedroom22
        with dissolve
        stop sound
        if laurenmbateonspycam == False:
            LT "{i}I've never squirted before!{/i}"
            LT "{i}Did thinking of [ryan] do that to me?{/i}"
            LT "{i}I'd better never think of him again when I masturbate!{/i}"
        else:
            LT "{i}Oh my God, I squirted again!{/i}"
            LT "{i}I've got to stop switching my thoughts to [ryan] when I masturbate!{/i}"
        LT "{i}But that just felt sooooo good!{/i}"
        LT "{i}What's wrong with me.{/i}"
        LT "{i}Maybe I should stop watching \"Game of Thots.\"{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Is it something Mom's feeding them?{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Lauren's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Lauren just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Lauren's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Lauren's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ laurenlibido -= 5
        $ persistent.gal_Lauren_4 = True
        if timeofdaycounter == 5:
            scene bg SpyCamLaurenBedroom16
            with fade
            $ sawlaurensquirt = True
            RT "{i}Guess it's time for lights out, ohhhhh and she's cuddling the very soggy Mr. Snuggles. How cute!{/i}"
            scene bg LaurenDoorNight
            with dissolve
            play music Honey
            $ screen_on = "laurendoornightmap"
            call screen laurendoornightmap
        else:
            scene bg LaurenDoor
            with fade
            RT "{i}I should run before I get caught.{/i}"
            play music Honey
            $ screen_on = "laurendoormap"
            call screen laurendoormap

label sidneyspycamroom:
    scene bg LaurenDoor
    with fade
    if sidneyanger >= 1:
        RT "{i}I wonder what she does in her room when she's pissed off at me.{/i}"
    else:
        RT "{i}She now locks her door when she changes. Little does she know I've got an Ace in the hole. Hahaha.... In her hole soon I hope.{/i}"
    menu:
        "Look through spy-cam":
            scene bg SpyCamSidneyBedroom08
            with dissolve
            play music SexMusic
            RT "{i}Looks like she's working on some fashion designs. I wonder if it's something for Lauren.{/i}"
            scene bg SpyCamSidneyBedroom01
            with fade
            RT "{i}Well, all my suspicions are confirmed, girls go around topless whenever they're alone.{/i}"
            RT "{i}Nothing more to see, if she's working, she could stay in that position for hours.{/i}"
            scene bg LaurenDoor
            with fade
            play music Honey
            $ screen_on = "laurendoormap"
            call screen laurendoormap
        "Never mind":
            $ screen_on = "laurendoormap"
            call screen laurendoormap

label sidneyspycamroomhorny:
    scene bg SpyCamSidneyBedroom09
    with dissolve
    play music SexMusic
    RT "{i}Oh life must have been so much harder for pervs in the past. Thank you technology!{/i}"
    scene bg SpyCamSidneyBedroom02
    with fade
    RT "{i}The spy cams of the past were peepholes drilled into the wall.{/i}"
    RT "{i}If I had lived back then, I might have been desperate enough to try it.{/i}"
    scene bg SpyCamSidneyBedroom03
    with fade
    RT "{i}Oh yeah, Sidney work those sweet little mini melons.{/i}"
    RT "{i}Those tanlined little molehills.{/i}"
    scene bg SpyCamSidneyBedroom04
    with dissolve
    RT "{i}Nooieeesh!.... She's going for it!{/i}"
    if sidneymbateonspycam == False:
        RT "{i}I've got to get a picture of this.{/i}"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg SpyCamSidneyBedroom04
        $ renpy.pause ()
        play sound Sidney01 loop
    else:
        pass
    RT "{i}I wonder what Sidney thinks about when she's buttering her muffin?{/i}"
    scene bg SpyCamSidneyBedroom05
    with fade
    if club_fun_counter >= 1 and sidneymbateonspycam:
        ST "{i}Shit!.... Now I'm giving [ryan] blowjobs at work!{/i}"
        ST "{i}I can't believe no ones caught us yet.{/i}"
        ST "{i}We're practically in plain sight.{/i}"
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom07 with Dissolve(0.3)
        $ renpy.pause (2.0)
        ST "{i}Oh my God!.... What's happening?!!{/i}"
        ST "{i}Can't control.... can't stop.... {/i}"
        scene bg SpyCamSidneyBedroom10
        with dissolve
        stop sound
        ST "{i}Oh my God, I squirted again!{/i}"
        ST "{i}And that felt sooooo good!{/i}"
        ST "{i}What's wrong with me.{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Is it something Mom's feeding them?{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Sidney's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Sidney just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Sidney's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ sidneylibido -= 5
        scene bg LaurenDoor
        with fade
        RT "{i}I should run before I get caught.{/i}"
        play music Honey
        $ screen_on = "laurendoormap"
        call screen laurendoormap
    if cop_block and sidneymbateonspycam:
        ST "{i}How did I get so perverted?{/i}"
        ST "{i}I can't believe doing naughty things in the park with [ryan] turns me on so bad.{/i}"
        ST "{i}I can't believe the possibility that people may be watching me gets me so hot.{/i}"
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom07 with Dissolve(0.3)
        $ renpy.pause (2.0)
        ST "{i}Oh my God!.... What's happening?!!{/i}"
        ST "{i}Can't control.... can't stop.... {/i}"
        scene bg SpyCamSidneyBedroom10
        with dissolve
        stop sound
        ST "{i}Oh my God, I squirted again!{/i}"
        ST "{i}And that felt sooooo good!{/i}"
        ST "{i}What's wrong with me.{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Is it something Mom's feeding them?{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Sidney's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Sidney just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Sidney's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ sidneylibido -= 5
        scene bg LaurenDoor
        with fade
        RT "{i}I should run before I get caught.{/i}"
        play music Honey
        $ screen_on = "laurendoormap"
        call screen laurendoormap
    if first_sixtynine and sidneymbateonspycam:
        ST "{i}How are things moving so fast? We fucking sixty-nined!{/i}"
        ST "{i}He was so good with his tongue! He's the first guy to ever make me squirt!{/i}"
        ST "{i}And the way he plastered me with cum!{/i}"
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom07 with Dissolve(0.3)
        $ renpy.pause (2.0)
        ST "{i}Oh my God!.... What's happening?!!{/i}"
        ST "{i}Can't control.... can't stop.... {/i}"
        scene bg SpyCamSidneyBedroom10
        with dissolve
        stop sound
        ST "{i}Oh my God, I squirted again!{/i}"
        ST "{i}And that felt sooooo good!{/i}"
        ST "{i}What's wrong with me.{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Is it something Mom's feeding them?{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Sidney's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Sidney just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Sidney's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ sidneylibido -= 5
        scene bg LaurenDoor
        with fade
        RT "{i}I should run before I get caught.{/i}"
        play music Honey
        $ screen_on = "laurendoormap"
        call screen laurendoormap
    elif finished_wr_shoot and sidneymbateonspycam:
        ST "{i}I can't believe I sucked [ryan]'s cock!'{/i}"
        ST "{i}I couldn't even swallow all the cum.... there was just so much, and it just shot out so fast.... It came out my nose!{/i}"
        ST "{i}I can still taste it!{/i}"
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom07 with Dissolve(0.3)
        $ renpy.pause (2.0)
        ST "{i}Oh my God!.... What's happening?!!{/i}"
        ST "{i}Can't control.... can't stop.... {/i}"
        scene bg SpyCamSidneyBedroom10
        with dissolve
        stop sound
        ST "{i}Oh my God, I squirted again!{/i}"
        ST "{i}And that felt sooooo good!{/i}"
        ST "{i}What's wrong with me.{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Is it something Mom's feeding them?{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Sidney's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Sidney just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Sidney's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ sidneylibido -= 5
        scene bg LaurenDoor
        with fade
        RT "{i}I should run before I get caught.{/i}"
        play music Honey
        $ screen_on = "laurendoormap"
        call screen laurendoormap
    elif sidneyfingerlaurenprogress >= 7 and sidneyfingerlaurenprogress <= 9 and sidneymbateonspycam:
        ST "{i}Did I really jack off [ryan] in his sleep?{/i}"
        ST "{i}His dick was just so big.... so hard.... {/i}"
        if sidneyfingerlaurenprogress == 7:
            ST "{i}I'm so glad he slept through it!.... It would have been so humiliating if he saw me plastered in his cum!{/i}"
        else:
            ST "{i}I can't believe I used my own panties to catch the cum!{/i}"
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom07 with Dissolve(0.3)
        $ renpy.pause (2.0)
        ST "{i}Oh my God!.... What's happening?!!{/i}"
        ST "{i}Can't control.... can't stop.... {/i}"
        scene bg SpyCamSidneyBedroom10
        with dissolve
        stop sound
        ST "{i}Oh my God, I squirted again!{/i}"
        ST "{i}And that felt sooooo good!{/i}"
        ST "{i}What's wrong with me.{/i}"
        ST "{i}It doesn't help that I'm sharing his bed.{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Is it something Mom's feeding them?{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Sidney's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Sidney just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Sidney's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ sidneylibido -= 5
        scene bg LaurenDoor
        with fade
        RT "{i}I should run before I get caught.{/i}"
        play music Honey
        $ screen_on = "laurendoormap"
        call screen laurendoormap
    else:
        ST "{i}What is wrong with me lately.{/i}"
        ST "{i}I'm just so horny all the time.{/i}"
        ST "{i}So horny that I'm subconciously molesting anyone that I sleep next to.{/i}"
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
        $ renpy.pause (0.2)
        scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
        $ renpy.pause (0.2)
        if sidneymbateonspycam == False:
            $ familyofsquirters += 1
            $ sidneymbateonspycam = True
            ST "{i}If I'm not fingering my sister's ass, I'm grabbing my brother's cock.{/i}"
            scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
            $ renpy.pause (0.2)
            ST "{i}And what I did to my own mother! What has come over me?{/i}" #s_upd2_5
            scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
            $ renpy.pause (0.2)
            ST "{i}I don't even know which one turns me on more.{/i}"
            ST "{i}I think [ryan]'s cock!{/i}"
            scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamSidneyBedroom06 with Dissolve(0.3)
            $ renpy.pause (0.2)
            scene bg SpyCamSidneyBedroom05 with Dissolve(0.3)
            $ renpy.pause (0.2)
            ST "{i}It's just so big, what would it feel like to be impaled on that pole?{/i}"
            ST "{i}Aaaaah.... shit!.... That did it!{/i}"
        else:
            pass
        scene bg SpyCamSidneyBedroom07 with Dissolve(0.3)
        $ renpy.pause (2.0)
        ST "{i}Oh my God!.... What's happening?!!{/i}"
        ST "{i}Can't control.... can't stop.... {/i}"
        scene bg SpyCamSidneyBedroom10
        with dissolve
        stop sound
        if sidneymbateonspycam == False:
            ST "{i}What was that? Did I just piss myself? Was that a real squirt?{/i}"
            ST "{i}I've never done that before!{/i}"
            ST "{i}Shit! Thinking of [ryan]'s dick just gave me the best orgasm of my life!{/i}"
            ST "{i}It's just fantasy Sidney, that little twerp better never try anything at all on me.{/i}"
            ST "{i}Why would I even think he would? Am I worried that I'd like it?{/i}"
        else:
            ST "{i}Oh my God, I squirted again!{/i}"
            ST "{i}It's just harmless fantasy. It's just harmless fantasy. It's just harmless fantasy.{/i}"
        ST "{i}And that felt sooooo good!{/i}"
        ST "{i}What's wrong with me.{/i}"
        ST "{i}It doesn't help that I'm sharing his bed.{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Is it something Mom's feeding them?{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Sidney's a squirter too.{/i}"
            RT "{i}Maybe it's a family thing.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh my God! Sidney just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Sidney's a real squirter!{/i}"
        RT "{i}Just.... wow!{/i}"
        "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ sidneylibido -= 5
        scene bg LaurenDoor
        with fade
        RT "{i}I should run before I get caught.{/i}"
        $ persistent.gal_Sidney_3 = True
        play music Honey
        $ screen_on = "laurendoormap"
        call screen laurendoormap

##############  SCHOOL  ########################################  SCHOOL  ################################################  SCHOOL  #################################################  SCHOOL  #################################################  SCHOOL  #####

##############  CLASSROOM  #####################################  CLASSROOM  ##############################################  CLASSROOM  ############################################  CLASSROOM  ##############################################  CLASSROOM  ############

label invitemomtooffice:
    if forcedntrevents >= 1 and lectureprogress >= 5:
        jump jacky_caught_office
    elif firstclubvisit == True and lectureprogress >= 5:
        jump jacky_caught_office
    if lectureprogress >= 3 and ntrcontent == True:
        scene bg NewClassroom02
        with fade
        R "Hey Matt, hey Megan, Miss [mom_name]? Do you have a minute to go over a few things with my Oedipus assignment with me?"
        M "Ok [ryan], go to my office and I'll be right there."
        R "Mom!"
        M "I mean [ryan], go to my office and I'll be right there."
        scene bg SleepBlack
        with fade
        jump momsoffice
    if lectureprogress >= 3:
        scene bg NewClassroom03
        with fade
        R "Hi Megan, Miss [mom_name]? Do you have a minute to go over a few things with my Oedipus assignment with me?"
        M "Ok, Ok, [ryan], go to my office and I'll be right there."
        R "Mom!"
        M "I mean [ryan], go to my office and I'll be right there."
        scene bg SleepBlack
        with fade
        jump momsoffice
    if ntrcontent == True:
        scene bg NewClassroom02
        with fade
        M "Oh, hi honey."
        R "Mom, remember? I don't want you to call me honey at school."
        M "Oh right, I'm sorry I forgot, [ryan]."
        M "But if I can't call you honey, you have to call me Miss [mom_name]."
        R "Ok Miss [mom_name]."
        M "We were all actually just talking about you."
        R "Really? What about?"
        MG "Oh, haha.... really Miss [mom_name] just overheard our conversation about the hottest couple for the yearbook."
        MG "This year it's not from existing couples, but who would make the cutest couples."
        MG "And your name is on the top of the chart."
        M "But I'm dying to know what girl you should be coupled with."
        M "They were just about to tell me."
        MB "Actually, Miss [mom_name], you were the one the students wanted to see [ryan] coupled up with."
        scene bg NewClassroom04
        with dissolve
        M "What?"
        M "Matt, that isn't funny!"
        MB "I'm serious!"
        MB "Tabboo stuff is kind of in right now."
        MB "And think about it. You're the hottest woman in this school!"
        MG "Yeah, and [ryan]'s quite the looker as well."
        MG "You passed down your sexiest genes Miss [mom_name]!"
        scene bg NewClassroom05
        with dissolve
        M "Oh, you two!"
        M "What am I going to do with you?"
        R "Hey Miss [mom_name], do you have a minute. I really need to meet with you about the Oedipus assignment you gave us."
        M "Ok honey, go to my office and I'll be right there."
        R "Mom!"
        M "I mean [ryan], go to my office and I'll be right there."
        scene bg SleepBlack
        with fade
        jump momsoffice
    else:
        scene bg NewClassroom03
        with fade
        M "Oh, hi honey."
        R "Mom, remember? I don't want you to call me honey at school."
        M "Oh right, I'm sorry I forgot, [ryan]."
        M "But if I can't call you honey, you have to call me Miss [mom_name]."
        R "Ok Miss [mom_name]."
        M "Did you need something?"
        R "Yeah actually, I really need to meet with you about the Oedipus assignment you gave us."
        M "Ok honey, go to my office and I'll be right there."
        R "Mom!"
        M "I mean [ryan], go to my office and I'll be right there."
        scene bg SleepBlack
        with fade
        jump momsoffice

###############  JACKY'S OFFICE  ###################################  JACKY'S OFFICE  ############################################  JACKY'S OFFICE  #############################################  JACKY'S OFFICE  ############################################  JACKY'S OFFICE  ############

label momsoffice:
    if lectureprogress >= 4:
        scene bg MomOffice01
        with fade
        M "Ok honey, so what was it that you wanted to ask me?"
        R "I was just wondering if you got a chance to play more of those games I sent you, to see if they would work for my assignment."
        M "No I haven't quite had time yet."
        R "Well, would you like to play a little bit more of them with me right now, to see if you can find a reason why they wouldn't work?"
        M "Sure, just scooch over a chair and I'll come sit by you so we can play together."
        scene bg MomOffice03
        with fade
        R "Ok, let me just look through my F95Zone downloads."
        R "Oh yes, here they are."
        play music SexMusic
        scene bg SleepBlack
        with fade
        scene bg MomOffice05
        with fade
        $ renpy.pause ()
        scene bg SleepBlack
        with fade
        scene bg MomOffice08
        with fade
        M "We keep seeing the same scenes over and over."
        R "Yeah, that's called grinding, the best games require it to build your stats."
        R "It makes each scene you unlock feel even more rewarding."
        M "That makes a lot of sense."
        scene bg MomOffice10
        with fade
        R "So, did you see anything that would disqualify these games from my assignment?"
        M "Uhhh.... no!.... Nothing obvious."
        M "I think you're on the right track. But maybe when you have some time again, come by and we can keep playing to make sure."
        M "Plus I'm dying to see what happens in the new updates."
        "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
        $ momlibido += 1
        M "Ok, I really need to get back to my class, I'll see you at home tonight."
        R "Ok Mom, see you later."
        RT "{i}Who would have thought spending quality time with Mom would mean playing these types of games with her?{/i}"
        RT "{i}She seems to have no problem with them, in fact she seems to really enjoy them.{/i}"
        $ lectureprogress = 5
        play music Honey
        scene bg CityMap01
        with fade
        $ mm_fuckedtoday = True
        $ screen_on = "citymapmap"
        call screen citymapmap
    elif lectureprogress == 3:
        scene bg MomOffice01
        with fade
        M "Ok honey, so what was it that you wanted to ask me?"
        R "I'm still struggling with this Oedipus assignment."
        R "I wanted to show you something else that I found, and see if it works for my Oedipus assignment."
        scene bg MomOffice02
        with dissolve
        R "It's another video game I found online, can you come look at it with me and see what you think."
        M "Ok just scooch over a chair and I'll come sit by you so you can show me."
        scene bg MomOffice03
        with fade
        R "Ok, let me just look through my F95Zone downloads."
        R "Oh yes, here it is."
        play music SexMusic
        scene bg MomOffice09
        with fade
        M "Milfy City, huh?"
        M "What on earth is a Milf?"
        R "Just a hot mom."
        M "Ok, well let's take a look."
        scene bg SleepBlack
        with fade
        scene bg MomOffice07
        with fade
        M "Wow! Somehow the mom kissing her son makes this so much more intimate than even the sex."
        R "Yeah, it makes you kind of understand why some people get into these types of games."
        M "Hmmmm.... yes, well keep going."
        scene bg SleepBlack
        with fade
        scene bg MomOffice08
        with fade
        M "This kid's dick is as big as yours."
        M "Wait! I shouldn't have said that.... I'm sorry if I made you uncomfortable."
        R "It's ok, it's flattering that my dick impressed you that much."
        M "Don't push it!"
        scene bg MomOffice10
        with fade
        R "So, do you think this one is good example for my paper as well?"
        R "Mom, are you alright?"
        M "Uhhh.... yes!.... Of course.... just a little flustered from that game."
        M "But yes you're right. I think you're on the right track. Send me a link to that game as well, so I can make sure it falls completely within the umbrella of this assignment."
        "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
        $ momlibido += 1
        M "Ok, I really need to get back to my class, I'll see you at home tonight."
        R "Ok, Mom, see you later."
        RT "{i}Boy, she really seemed flustered, If I can get her into these types of games, what I'm trying to do to her might not be so shocking for her when the time comes.{/i}"
        RT "{i}I'll have to show her some more of those games to see how she reacts.{/i}"
        $ lectureprogress = 4
        play music Honey
        scene bg CityMap01
        with fade
        $ mm_fuckedtoday = True
        $ screen_on = "citymapmap"
        call screen citymapmap
    else:
        scene bg MomOffice01
        with fade
        M "Ok honey, so what was it that you wanted to ask me?"
        R "I'm just kind of struggling with this Oedipus assignment."
        R "I'm supposed to find how this ancient play still is relevant in modern day life."
        R "But when I search for Oedipus stuff on the internet. I find stuff that is kind of porn-ish."
        M "Yeah, I've been worried about this assignment turning up that kind of stuff."
        M "In fact I hate this new curriculum."
        M "But I'm forced to teach it, because if I don't I'll be fired."
        R "It's not as bad as I originally thought it would be. But if you don't get to choose what you teach, who sets the curriculum?"
        M "Some pervert on the school board named Will Tylor. He's some kind of deviant from what I can tell."
        M "I just hope he gets fired before his curriculum corrupts everyone on the school board, and in the schools."
        R "Hmmmm.... sounds like an asshole."
        M "He really is."
        R "Well then, I wanted to show you something that I found on the internet, and see if it works for my Oedipus assignment."
        scene bg MomOffice02
        with dissolve
        R "It's just this video game I found online, can you come look at it with me and see what you think."
        M "Sure, just scooch over a chair and I'll come sit by you so you can show me."
        scene bg MomOffice03
        with fade
        R "Ok, let me just look through my F95Zone downloads."
        R "Oh yes, here it is."
        play music SexMusic
        scene bg MomOffice04
        with fade
        M "Big Brother, huh?"
        M "Is this like that voyeuristic television show on TV?"
        R "No this isn't nearly that lewd."
        M "Ok, well let's take a look."
        scene bg SleepBlack
        with fade
        scene bg MomOffice05
        with fade
        M "Uggghh.... are we really supposed to continue to believe that the mom is so stupid to believe she needs to jack off her son because he has carpal tunnel syndrome?"
        R "Mom, try to remember that it's just a game. It may be a bit ridiculous, but it's hard to make up situations where a mom would willingly enter a relationship with her son."
        M "Hmmmm.... well, keep going."
        scene bg SleepBlack
        with fade
        scene bg MomOffice06
        with fade
        M "And now she's a party to the corruption of her daughter?"
        M "I think that's all we should see for today."
        scene bg MomOffice10
        with fade
        R "It's just fiction Mom, but there are a lot of people into these kind of games. I think it would be a good argument in my paper."
        R "Mom, are you alright?"
        M "Uhhh.... yes!.... Of course.... just a little flustered from that game."
        M "But yes you're right. I think you're on the right track. Send me a link to that game so I can make sure it falls completely within the umbrella of this assignment."
        "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
        $ momlibido += 1
        M "Ok, I really need to get back to my class, I'll see you at home tonight."
        R "Ok Mom, see you later."
        RT "{i}Boy, she really seemed flustered, and she didn't kick me out of her office like I expected. Could she maybe have enjoyed that?{/i}"
        RT "{i}I'll have to show her some more of those games to see how she reacts.{/i}"
        $ lectureprogress = 3
        $ mompictureprogress = 5
        play music Honey
        scene bg CityMap01
        with fade
        $ mm_fuckedtoday = True
        $ screen_on = "citymapmap"
        call screen citymapmap

##############  WAREHOUSE  #####################################  WAREHOUSE  #############################################  WAREHOUSE  ##############################################  WAREHOUSE  ##############################################  WAREHOUSE  ############

label emptywarehouse:
    scene bg CosplayWarehouse01
    with fade
    $ renpy.pause ()
    scene bg CosplayWarehouse02
    with fade
    R "Well, this is it. What do you guys think?"
    MD "It's not quite as dirty as I thought it would be, but still pretty grimy."
    L "And there are windows everywhere! Any perverted warehouse worker could peek in for a free show."
    R "All problems we can take care of."
    R "I will start to clean things up a bit, and hang these old canvas tarps over the windows."
    R "You two go into that utility closet and get your outfits on."
    scene bg SleepBlack
    with fade
    "{i}\"15 minutes later\"{/i}"
    scene bg CosplayWarehouse03
    with fade
    R "There, isn't this better."
    MD "Yeah, it actually is pretty good."
    L "Not the best lighting, but the flash on your camera should help with that?"
    R "To a degree."
    R "If we take more pictures down the road, we may want to consider investing in some professional lighting, a nice backdrop, some photo equipment."
    R "That's getting way ahead of ourselves. That is assuming we make some good money."
    R "But for now, this will do just fine."
    R "I'm going to shoot each of you individually and do some photos of you together."
    R "Who wants to go first?"
    L "Oh, I do!"
    R "Ok, strike a pose and I'll start taking some pictures."
    scene bg CosplayWarehouse04
    with fade
    play music SexMusic
    R "Ok, that's cute."
    L "Cute? I was going for sexy!"
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg CosplayWarehouse04
    R "If you want sexy just turn around."
    L "Do you know how weird this is having my brother directing me to take sexy photos?"
    R "You've just got to forget that I'm your brother."
    R "Imagine you're a professional model, and I'm just some nameless photographer."
    R "Now turn around."
    L "Ok, I'll try."
    scene bg CosplayWarehouse05
    with fade
    R "There you go, now that's sexy!"
    L "Can you at least try not to make comments like that?"
    L "I can't completely forget that it's my brother taking these pictures."
    R "Ok, I'll try."
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg CosplayWarehouse05
    R "Ok, grab your prop gun and see if you can think of a sexy pose on your own."
    scene bg CosplayWarehouse06
    with fade
    L "How's this?"
    RT "{i}Oh God, don't say anything too weird!{/i}"
    R "Yeah.... that works ok."
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg CosplayWarehouse06
    RT "{i}Would it be unprofessional to pop a boner in the middle of a photoshoot?{/i}"
    R "Alright, should we turn up the heat a little more?"
    L "Ok, what do you mean?"
    menu:
        "Let's modify your outfit so it shows a little more skin.":
            scene bg CosplayWarehouse07
            with dissolve
            L "Oh my ass cheeks hanging out aren't enough skin for you?"
            R "Well, yeah, it's pretty sexy, but you're going to have to go further if you want your pictures to get the kind of attention you want them to get."
            L "Yeah, I don't think so."
            "{i}{b}\"Lauren's Anger +1\"{/b}{/i}"
            $ laurenanger += 1
            L "I'm sure I'll get plenty of attention without having to strip for you."
            R "Ok.... ok.... I don't want you to do anything you're uncomfortable with."
        "Let's get Mandy to join the shoot.":
            pass
    R "Mandy.... why don't you grab your prop gun and we'll take some pictures of you two together."
    R "Ok, now you two pose like Lauren is arresting Mandy."
    scene bg CosplayWarehouse08
    with fade
    MD "Like this?"
    R "Yeah, that's pretty good."
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg CosplayWarehouse08
    R "Ok Lauren, now you have to check her for dangerous weapons."
    R "Start with her boots, and work your way up."
    scene bg CosplayWarehouse09
    with dissolve
    $ renpy.pause ()
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg CosplayWarehouse09
    R "Ok, work your way up to her belt, and take it off."
    R "I see some dangerous weapons hanging off of it."
    scene bg CosplayWarehouse10
    with dissolve
    R "Ok, that's great."
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg CosplayWarehouse10
    R "Now just unbuckle it and throw it over here."
    R "Now you need to check the more intimate areas for weapons."
    scene bg CosplayWarehouse11
    with dissolve
    L "Are you serious right now? She's my cousin. That's just too weird."
    R "She's not your cousin. You're both professional models that are trying to take the kinds of pictures that will kick start your careers."
    R "You don't have to grope her. Just hover your hands over the area and make it look like you're groping her."
    L "You really are a pervert."
    R "No, I'm a professional photographer, who has done a fair bit of online research, so I know what kind of pictures get attention online."
    MD "Hahaha.... online research.... hahah."
    R "Now get back into character!"
    scene bg CosplayWarehouse12
    with dissolve
    R "There you go, that's perfect."
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg CosplayWarehouse12
    R "It looks like you're really groping Mandy."
    L "I kind-of am, I was just going to hover my hands, but figured the picture and Mandy's reaction would be better if I just went for it."
    R "Good job!"
    R "That's the kind of professionalism I want on my photoshoots."
    menu:
        "Ok Lauren, time to strip search her.":
            R "Ok, now you need to strip search Mandy to make sure she's not hiding anything else."
            MD "Ohhh..."
            "{i}{b}\"Mandy's Libido +2\"{/b}{/i}"
            $ cousinlibido += 2
            L "And now I'm done."
            scene bg CosplayWarehouse13
            with dissolve
            R "Wait what do you mean you're done?"
            L "You pushed it too far!"
            "{i}{b}\"Lauren's Anger +5\"{/b}{/i}"
            $ laurenanger += 5
            L "I'm not participating in your perverted fantasies anymore."
            MD "But Lauren, he's right, these are the kinds of pictures that get attention online."
            L "Well then, go ahead and take some more pics with my pervy brother. I'll just watch."
            R "Ok Lauren, your loss."
            R "Alright; Mandy, I want you to start out with an action pose. Here, use this prop."
        "Alright, let's take some pics of just Mandy.":
            R "Alright; Mandy, I want you to start out with an action pose. Here, use this prop."
    scene bg CosplayWarehouse14
    with dissolve
    MD "Like this?"
    R "Yeah Mandy, you really are a natural."
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg CosplayWarehouse14
    R "Ok, let's get into the poses that will make the money. Can you sexy up that outfit?"
    MD "Yeah, it comes apart in pieces. Here tell me what you think when I take this part off."
    scene bg CosplayWarehouse15
    with dissolve
    RT "{i}Holy shit! I think I need roomier pants.{/i}"
    R "Uhhemm.... It looks really good.... uhhh nice pose!"
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg CosplayWarehouse15
    R "Ok, let's get a sexy pic from the front."
    R "Can you modify anything in the front so that it looks sexier?"
    MD "What do you mean?"
    menu:
        "Like, does the breastplate come off?":
            MD "Yeah, it can, I'm not really sure I'm comfortable showing my nips though."
            R "Oh yeah, like I said, nothing that makes you feel uncomfortable, so you could just take off the breast plate and cover your nipples with your hands."
            scene bg CosplayWarehouse17
            with dissolve
            MD "Ok, I guess I can do that."
            "{i}{b}\"Mandy's Submission +1\"{/b}{/i}"
            $ cousinsubmission += 1
            R "Yeah, that costume kicks ass."
            R "Now, try to look sexy."
        "I don't know, you decide.":
            MD "Hmmmm.... I do want these pics to get attention."
            MD "Ok, I'll do it!"
            "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
            $ cousinlibido += 1
    scene bg CosplayWarehouse16
    with dissolve
    MD "Is this sexy enough for you?"
    RT "{i}Oh my gosh! I actually got her to do it!{/i}"
    RT "{i}That is pretty hot! I think I've found my dream career.{/i}"
    R "Uuuuhhhhhh.... gulp.... yeah, that will.... uh.... do just fine."
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg CosplayWarehouse16
    R "Ok, good job. Those pictures are going to turn out great!"
    scene bg CosplayWarehouse18
    with fade
    play music Honey
    R "I got some great pictures from both of you. Why don't you go change and put your costumes in my scooter's pizza box holder, and I'll take them home for you."
    "{i}+2 inventory items, \"Cosplay Outfits.\"{/i}"
    $ inventory.add(cosplay_outfit_space_01)
    $ inventory.add(cosplay_outfit_space_02)
    R "I'll also edit and enhance these photos and post them online for you."
    R "If all goes well, this will be the beginning of your internet fame."
    R "Be careful riding your bikes home."
    $ timeofdaycounter = 4
    scene bg SleepBlack
    with fade
    "{i}\"30 minutes later\"{/i}"
    $ photoshoot_1 = True
    $ persistent.gal_Cosplay_1 = True
    jump postingthepics

##############  STRIP CLUB  #####################################  STRIP CLUB  ###########################################  STRIP CLUB  ############################################  STRIP CLUB  ##############################################  STRIP CLUB  ##########

label ntrclub:
    scene bg WalkingBar
    with fade
    play music ClubMusic
    RT "{i}I think I remember my way to the strip pole.... {/i}"
    scene bg WalkingCasino
    with fade
    RT "{i}Past the bar, through the casino, and Bingo!{/i}"
    scene bg NTRClub01
    with fade
    RT "{i}Noish! I haven't missed anything yet!{/i}"
    RT "{i}This is a new outfit. Me likey.{/i}"
    scene bg NTRClub02
    with fade
    RT "{i}I don't know why girls dressed as bunnies are a turn on, but they are.{/i}"
    scene bg NTRClub03
    with dissolve
    RT "{i}Wow! Mom is really acrobatic and in great shape. I love how her tits just popped out of that outfit!{/i}"
    RT "{i}Nipple pasties? What a cocktease!{/i}"
    scene bg NTRClub04
    with dissolve
    RT "{i}Oh man, she looks so seductive.{/i}"
    RT "{i}I've got to get a picture.{/i}"
    $ ntr_club_pic_01 = True
    play sound CameraClick
    show CamaraFlash
    pause (0.25)
    scene bg NTRClub04
    RT "{i}That will be a nice addition to the collection.{/i}"
    scene bg NTRClub05
    with dissolve
    MT "{i}Here I am again, baring it all for total strangers.{/i}"
    MT "{i}And it's not like I'm not used to being in front of an audience every day.{/i}"
    scene bg NTRClub06
    with dissolve
    MT "{i}I just don't take off my clothes for my classes.{/i}"
    MT "{i}Although, that would be pretty exciting if I did.{/i}"
    MT "{i}I can just imagine the shocked look on all the youngsters' faces.{/i}"
    MT "{i}And the look of desire in their eyes as they all imagine fucking me.{/i}"
    MT "{i}Shit! I'm getting super horny. I'm drenching the pole again.{/i}"
    "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
    $ momlibido += 1
    scene bg NTRClub07
    with fade
    $ renpy.pause ()
    scene NTRStripVideo01
    with fade
    $ renpy.pause ()
    RT "{i}As much as I love the tail on those panties. I would love to see them come off.{/i}"
    scene NTRStripVideo02
    with fade
    $ renpy.pause ()
    scene bg NTRClub08
    with dissolve
    RT "{i}What the hell? Why did Joey stop her dance?{/i}"
    RT "{i}What the hell is he saying to her.{/i}"
    RT "{i}Shit, she looks worried.{/i}"
    scene bg NTRClub09
    with dissolve
    VOM "Next up we have a hot little cowgirl who's ready to ride the pole like you wish she'd ride your pole."
    VOM "Please welcome the sexy young Emma to the stage."
    X "Bring back the redhead! She didn't finish her dance!"
    G "Come back next week. If you're lucky she'll be here again."
    RT "{i}They're taking Mom to the back room. I'd better see if I can find out what Joey's doing to her back there.{/i}"
    if liedaboutmoney == True:
        RT "{i}Shit! Why didn't I just pay them the money for this week? Who knows what could happen to Mom back there.{/i}"
    else:
        RT "{i}Shit! Why didn't i work harder to make the money for this week's payment? Who knows what could happen to Mom back there.{/i}"
    scene bg NTRClub10
    with fade
    R "Umm.... excuse me sir, could you tell me what goes on behind that curtain?"
    scene bg NTRClub11
    with dissolve
    G "Ahh.... aren't you Ron?"
    R "It's [ryan] actually."
    G "Right, yeah, [ryan]."
    G "Joey was hoping you'd be here tonight."
    R "What? What are you talking about?"
    G "Well, Joey loves cuckolding other men, and he loves it even more when they know about it. It really gets him off."
    G "And since [dad_name] is in prison, having you around is the next best thing for him."
    scene bg NTRClub10
    with dissolve
    R "Cuckold? Does that mean he's going to fuck her in there?"
    G "Well, probably not tonight, he usually takes it a little bit slow so that he doesn't scare off the girls immediately."
    G "But if she keeps coming back, I would say yes, he'll eventually split her peach."
    R "Shit. I've got to do something."
    scene bg NTRClub11
    with dissolve
    G "Oh, no you damn well will not!"
    G "You're invited to watch, but if you do anything to interfere I will personally give you two black eyes."
    G "And maybe you'd better just peek, and don't let [mom_name] see you. If you spook her off, Joey won't be very happy, and once again, I'll have to give you two black eyes."
    R "Ok, ok, I've got it. If I ruin Joey's moment, I get two black eyes."
    G "Two black eyes."
    R "Ok, can I peek now?"
    G "Go right ahead."
    scene bg NTRClub12
    with dissolve
    $ renpy.pause ()
    scene bg NTRClub13
    with fade
    J "Now just try to feel comfortable, and if you do a good job I'll be very generous to you."
    J "Maybe take you shopping for sexy outfits?"
    RT "{i}Hey, that's what I want to do with her.{/i}"
    scene bg NTRClub14
    with fade
    J "That's right beautiful! Let me get a good feel of those tits."
    M "The customer's not supposed to touch us during private dances."
    J "Well, I'm not just any customer, am I?"
    J "Now put your leg up here."
    scene bg NTRClub15
    with dissolve
    M "Oh my God, Joey, this is so wrong!"
    M "Nobody has touched me here but [dad_name] since we've been married."
    J "Oh, but I know you love it! My fingers are getting soaked."
    M "Maybe I do just a little."
    RT "{i}Dammit! I wanted to be the first since Dad!{/i}"
    scene bg NTRClub16
    with fade
    J "Wow [mom_name], this view is incredible."
    J "You're making my cock so hard."
    J "Why don't you come down here and give me that lap-dance now."
    scene bg NTRClub18 with Dissolve(0.3)
    $ renpy.pause (0.05)
    play sound ClubGrind loop
    scene bg NTRClub19 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub20 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub21 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub22 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub17 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub18 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub19 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub20 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub21 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub22 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub17 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub18 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub19 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub20 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub21 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub22 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub17 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub18 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub19 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub20 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub21 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub22 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub17 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub18 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub19 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub20 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub21 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub22 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub17 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub18 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub19 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub20 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub21 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub22 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub17 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub18 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub19 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub20 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub23
    stop sound
    with dissolve
    M "Joey, what are you doing back there?"
    J "Just letting \"Little Joey\" get some air."
    scene bg NTRClub24
    with dissolve
    J "And getting rid of this bunny tail."
    J "It's getting in the way."
    J "Now keep going!"
    scene bg NTRClub25
    with fade
    play sound ClubGrind
    $ renpy.pause (0.05)
    scene bg NTRClub26 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub27 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub26 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub25 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub26 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub27 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub26 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub25 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub26 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub27 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub26 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub25 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub26 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub27 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub26 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub25 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub26 with Dissolve(0.3)
    $ renpy.pause (0.05)
    scene bg NTRClub27
    with dissolve
    stop sound
    J "Holy Mary!"
    scene bg BlurryWhite
    with fade
    with hpunch
    with vpunch
    scene bg NTRClub28
    with dissolve
    J "Take that!"
    scene bg NTRClub29
    with dissolve
    J "Oh yeah, [mom_name]! That was great!"
    scene bg NTRClub30
    M "Uhhh.... did you just do what I think you did?"
    J "Oh Yeah!"
    J "Why don't you run to the locker room and get yourself cleaned up."
    J "I'm sure your son Ron's waiting up for you."
    M "You mean [ryan]?"
    J "Whatever."
    scene bg NTRClub12
    with fade
    R "Shit, she's done, I'd better make myself scarce."
    $ forcedntrevents = 1
    play music Honey
    scene bg SleepBlack
    with fade
    scene bg CityMapNight
    $ persistent.gal_NTR_2 = True
    $ sawmomstripping = True
    $ screen_on = "citymapmapnight"
    call screen citymapmapnight
