
default Mom_e = "Mom"
default mom_e = "mom"
default Dad_e = "Dad"
default dad_e = "dad"
default uncle_e = "uncle Bobby"
default Uncle_e = "Uncle Bobby"
default Auntie_e = "Auntie"
default auntie_e = "auntie"

define in_family_photomap = False

init:

    image failed_img:
        Text([
    "You failed this event"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5)

screen event_compleated(e):
    default event_num = e['event_num']
    default progress_needed = e['progress_needed']
    default button_idle = e['button_idle']

    if progress_needed:
        text _("[event_num]:") style "events_style_label"
        imagebutton:
            idle button_idle
            pos (0.3, 0.0)
            action NullAction()
        text _("") size 10

screen event_details(e):
    default event_num = e['event_num']
    default progress_needed = e['progress_needed']
    default button_ypos = e['button_ypos']
    default new_context_call = e['new_context_call']

    if not progress_needed:
        text _("[event_num]:") style "events_style_label"
        textbutton _("???") xpos 0.1 ypos button_ypos:
            text_outlines [(3, "#E60000", 0,0)]
            action ui.callsinnewcontext(new_context_call)
        text _("") size 10

screen event_screen():

    style_prefix "stats"

    add "MobileScreen.png"
    modal True

    default event_list = [{
#EVENT 1###############################################################################################################################################
        'event_num': 'Event 1',
        'progress_needed': progress >= 1,
        'button_idle': Text([
            "Dad's in jail, shit's",
            "\nfucked up"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.08,
        'new_context_call': 'event_info',
        }, {
#EVENT 2###############################################################################################################################################
        'event_num': 'Event 2',
        'progress_needed': progress >= 2,
        'button_idle': Text([
            "Talked with",
            "\nUncle Bobby"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.11,
        'new_context_call': 'event_info_02',
        }, {
#EVENT 3###############################################################################################################################################
        'event_num': 'Event 3',
        'progress_needed': progress >= 3,
        'button_idle': Text([
            "Mom's a stripper"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.14,
        'new_context_call': 'event_info_03',
        }, {
#EVENT 4###############################################################################################################################################
        'event_num': 'Event 4',
        'progress_needed': progress >= 4,
        'button_idle': Text([
            "Comforted Mom"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.17,
        'new_context_call': 'event_info_04',
        }, {
#EVENT 5###############################################################################################################################################
        'event_num': 'Event 5',
        'progress_needed': progress >= 5,
        'button_idle': Text([
            "Helped Lauren find",
            "\nthe tv remote"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.20,
        'new_context_call': 'event_info_05',
        }, {
#EVENT 6###############################################################################################################################################
        'event_num': 'Event 6',
        'progress_needed': progress >= 6,
        'button_idle': Text([
            "Sidney came home"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.23,
        'new_context_call': 'event_info_06',
        }, {
#EVENT 7###############################################################################################################################################
        'event_num': If( ntrcontent,
            "NTR Event 7",
            "Loyalty Event 7"),
        'progress_needed': firstntrblowjob or firstloyaltyblowjob,
        'button_idle': Text([
            "Got a blowjob",
            "\nfrom Megan"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.26,
        'new_context_call': 'event_info_07',
        }, {
#EVENT 8###############################################################################################################################################
        'event_num': 'Event 8',
        'progress_needed': fixed_bulb,
        'button_idle': Text([
            "Fixed a light bulb"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.29,
        'new_context_call': 'event_info_08',
        }, {
#EVENT 9###############################################################################################################################################
        'event_num': 'Event 9',
        'progress_needed': progress >= 7,
        'button_idle': Text([
            "Separated",
            "\nLauren and Sidney"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.29,
        'new_context_call': 'event_info_09',
        }, {
#EVENT 10##############################################################################################################################################
        'event_num': 'Event 10',
        'progress_needed': fit_enough,
        'button_idle': Text([
            "Got in shape!"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.32,
        'new_context_call': 'event_info_10',
        }, {
#EVENT 11##############################################################################################################################################
        'event_num': 'Event 11',
        'progress_needed': progress >= 8,
        'button_idle': Text([
            "Photo-shoot with",
            "\nLauren and Mandy"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.32,
        'new_context_call': 'event_info_11',
        }, {
#EVENT 12##############################################################################################################################################
        'event_num': 'Event 12',
        'progress_needed': found_bathrobe,
        'button_idle': Text([
            "Hid Mom's",
            "\nbathrobe"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.32,
        'new_context_call': 'event_info_12',
        }, {
#EVENT 13##############################################################################################################################################
        'event_num': 'Event 13',
        'progress_needed': mom_mischief >= 2,
        'button_idle': Text([
            "Night mischief",
            "\nwith Mom"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.29,
        'new_context_call': 'event_info_13',
        }, {
#EVENT 14##############################################################################################################################################
        'event_num': 'Event 14',
        'progress_needed': lauren_mischief >= 2,
        'button_idle': Text([
            "Night mischief",
            "\nwith Lauren"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.32,
        'new_context_call': 'event_info_14',
        }, {
#EVENT 15##############################################################################################################################################
        'event_num': 'NTR Event 15',
        'progress_needed': forcedntrevents >= 1,
        'button_idle': Text([
            "Lap-dance",
            "\nfor Joey"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_15',
        }, {
#EVENT 16##############################################################################################################################################
        'event_num': 'Event 16',
        'progress_needed': fixed_sink >= 1,
        'button_idle': Text([
            "Fixed kitchen sink"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_16',
        }, {
#EVENT 17##############################################################################################################################################
        'event_num': 'Event 17',
        'progress_needed': spycammommbatebath,
        'button_idle': Text([
            "Mom masturbated",
            "\nin the shower"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_17',
        }, {
#EVENT 18##############################################################################################################################################
        'event_num': 'Event 18',
        'progress_needed': mommbateonspycam,
        'button_idle': Text([
            "Mom masturbated",
            "\nin her bedroom"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_18',
        }, {
#EVENT 19##############################################################################################################################################
        'event_num': 'Event 19',
        'progress_needed': spycamlaurenmbatebath,
        'button_idle': Text([
            "Lauren masturbated",
            "\nin the shower"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_19',
        }, {
#EVENT 20##############################################################################################################################################
        'event_num': 'Event 20',
        'progress_needed': laurenmbateonspycam,
        'button_idle': Text([
            "Lauren masturbated",
            "\nin her bedroom"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_20',
        }, {
#EVENT 21##############################################################################################################################################
        'event_num': 'Event 21',
        'progress_needed': spycamsidneymbatebath,
        'button_idle': Text([
            "Sidney masturbated",
            "\nin the shower"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_21',
        }, {
#EVENT 22##############################################################################################################################################
        'event_num': 'Event 22',
        'progress_needed': sidneymbateonspycam,
        'button_idle': Text([
            "Sidney masturbated",
            "\nin Lauren's bedroom"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_22',
        }, {
#EVENT 23##############################################################################################################################################
        'event_num': 'Event 23',
        'progress_needed': (inventory.inv_amount(jacky_bikini_01) == 0 and firstclubvisit) or (inventory.inv_amount(jacky_bikini_01) == 1),
        'button_idle': If(inventory.inv_amount(jacky_bikini_01) == 0 and firstclubvisit,
            Text([
                "You failed this event"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
            If(inventory.inv_amount(jacky_bikini_01) == 1,
                Text([
                    "Bought bikini"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5))),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_23',
        }, {
#EVENT 24##############################################################################################################################################
        'event_num': 'Event 24',
        'progress_needed': bikini_show_failed or bikini_show_seen,
        'button_idle': If(bikini_show_failed,
            Text([
                "You failed this event"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
            If(bikini_show_seen,
                Text([
                    "Unlocked the",
                    "\nbikini show"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5))),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_24',
        }, {
#EVENT 25##############################################################################################################################################
        'event_num': 'Event 25',
        'progress_needed': firstclubvisit,
        'button_idle': Text([
            "Pool party"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_25',
        }, {
#EVENT 26##############################################################################################################################################
        'event_num': 'Event 26',
        'progress_needed': progress >= 11,
        'button_idle': Text([
            "Unlocked the",
            "\nphoto studio"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_26',
        }, {
#EVENT 27##############################################################################################################################################
        'event_num': 'Event 27',
        'progress_needed': not first_htbyd_shoot,
        'button_idle': Text([
            "Started HTBYD",
            "\nphotoshoot"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_27',
        }, {
#EVENT 28##############################################################################################################################################
        'event_num': 'Event 28',
        'progress_needed': finished_htbyd_shoot,
        'button_idle': Text([
            "Finished HTBYD",
            "\nphotoshoot"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_28',
        }, {
#EVENT 29##############################################################################################################################################
        'event_num': 'Event 29',
        'progress_needed': first_lauren_grind or diaz_came_for_mandy,
        'button_idle': If(diaz_came_for_mandy and not first_lauren_grind,
            Text([
                "You failed this \"Loyalty\" event"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
            If(first_lauren_grind,
                Text([
                    "Pay off Diaz"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5))),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_29',
        }, {
#EVENT 30##############################################################################################################################################
        'event_num': 'NTR Event 30',
        'progress_needed': first_diaz_dance or diaz_came_for_mandy,
        'button_idle': If(diaz_came_for_mandy and not first_diaz_dance,
            Text([
                "You failed this \"NTR\" event"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
            If(first_diaz_dance,
                Text([
                    "Pay Diaz in favors"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5))),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_30',
        }, {
#EVENT 31##############################################################################################################################################
        'event_num': 'Event 31',
        'progress_needed': start_of_campaign,
        'button_idle': Text([
            "Begin Presidential",
            "\nCampaign"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_31',
        }, {
#EVENT 32##############################################################################################################################################
        'event_num': 'Event 32',
        'progress_needed': sexy_posters_approved,
        'button_idle': Text([
            "Lauren Wagers",
            "\nher Pussy"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_32',
        }, {
#EVENT 33##############################################################################################################################################
        'event_num': 'Event 33',
        'progress_needed': mm_lockerfuck,
        'button_idle': Text([
            "Caught Matt and",
            "\nMegan Fucking"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_33',
        }, {
#EVENT 34##############################################################################################################################################
        'event_num': 'Event 34',
        'progress_needed': jr_watched,
        'button_idle': Text([
            "Mom's masturbating",
            "\nin her office"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_34',
        }, {
#EVENT 35##############################################################################################################################################
        'event_num': 'Event 35',
        'progress_needed': posters_complete or campaign_finished,
        'button_idle': If(campaign_finished and not posters_complete,
            Text([
                "You failed this event"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
            If(posters_complete,
                Text([
                    "Made new posters"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5))),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_35',
        }, {
#EVENT 36##############################################################################################################################################
        'event_num': 'Event 36',
        'progress_needed': fixed_washer == 2,
        'button_idle': Text([
            "Fixed washing",
            "\nmachine"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_36',
        }, {
#EVENT 37##############################################################################################################################################
        'event_num': 'Event 37',
        'progress_needed': tv_events == 5,
        'button_idle': Text([
            "Sneaking with",
            "\nLauren in the lounge"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_37',
        }, {
#EVENT 38##############################################################################################################################################
        'event_num': 'Event 38',
        'progress_needed': not first_wr_shoot,
        'button_idle': Text([
            "Started Womb Raider",
            "\nphotoshoot"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_38',
        }, {
#EVENT 39##############################################################################################################################################
        'event_num': 'Event 39',
        'progress_needed': locker_cam_placed or campaign_finished,
        'button_idle': If(campaign_finished and not locker_cam_placed,
            Text([
                "You failed this event"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
            If(locker_cam_placed,
                Text([
                    "Locker Room Run"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5))),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_39',
        }, {
#EVENT 40##############################################################################################################################################
        'event_num': 'Event 40',
        'progress_needed': finished_wr_shoot,
        'button_idle': Text([
            "Finished Womb Raider",
            "\nphotoshoot"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_40',
        }, {
#EVENT 41##############################################################################################################################################
        'event_num': 'Event 41',
        'progress_needed': first_sixtynine,
        'button_idle': Text([
            "69 with Sidney"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_41',
        }, {
#EVENT 42##############################################################################################################################################
        'event_num': 'Event 42',
        'progress_needed': diaz_van_counter >= 4 or campaign_finished,
        'button_idle': If(campaign_finished and diaz_van_counter <= 3,
            Text([
                "You failed this event"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
            If(diaz_van_counter >= 4,
                Text([
                    "Blown by Diaz"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5))),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_42',
        }, {
#EVENT 43##############################################################################################################################################
        'event_num': 'NTR Event 43',
        'progress_needed': ntr_train or campaign_finished,
        'button_idle': If(campaign_finished and not ntr_train,
            Text([
                "You failed this \"NTR\" event"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
            If(ntr_train,
                Text([
                    "All Aboard!"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5))),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_43',
        }, {
#EVENT 44##############################################################################################################################################
        'event_num': 'Event 44',
        'progress_needed': first_bath_hjob,
        'button_idle': Text([
            "Mom gave a Handy",
            "\nin the bathroom"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_44',
        }, {
#EVENT 45##############################################################################################################################################
        'event_num': 'Event 45',
        'progress_needed': blackmailed_mom_matt or blackmailed_mom_megan,
        'button_idle': Text([
            "Mom got",
            "\nblackmailed"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_45',
        }, {
#EVENT 46##############################################################################################################################################
        'event_num': 'Event 46',
        'progress_needed': first_hp_shoot,
        'button_idle': Text([
            "Unlocked Perry",
            "\nHotter Photoshoot"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_46',
        }, {
#EVENT 47##############################################################################################################################################
        'event_num': 'Event 47',
        'progress_needed': finished_hp_shoot,
        'button_idle': Text([
            "Finished Perry",
            "\nHotter Photoshoot"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_47',
        }, {
#EVENT 48##############################################################################################################################################
        'event_num': 'Event 48',
        'progress_needed': mp_captured,
        'button_idle': Text([
            "Saved a war hero"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_48',
        }, {
#EVENT 49##############################################################################################################################################
        'event_num': 'Event 49',
        'progress_needed': sidney_spy,
        'button_idle': Text([
            "I'm not the",
            "\nonly schemer"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_49',
        }, {
#EVENT 50##############################################################################################################################################
        'event_num': 'Event 50',
        'progress_needed': more_club_bjs,
        'button_idle': Text([
            "Blowjob on",
            "\nthe job"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_50',
        }, {
#EVENT 51##############################################################################################################################################
        'event_num': 'Event 51',
        'progress_needed': bobby_says_bye,
        'button_idle': Text([
            "Bye Uncle Bobby"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_51',
        }, {
#EVENT 52##############################################################################################################################################
        'event_num': 'Event 52',
        'progress_needed': aunt_second_visit,
        'button_idle': Text([
            "Aunt Cami is our",
            "\nnew maid"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_52',
        }, {
#EVENT 53##############################################################################################################################################
        'event_num': 'Event 53',
        'progress_needed': bathroom_boobs,
        'button_idle': Text([
            "Auntie presses",
            "\nboobs on glass"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_53',
        }, {
#EVENT 54##############################################################################################################################################
        'event_num': 'Event 54',
        'progress_needed': lounge_boobs,
        'button_idle': Text([
            "Auntie flashes",
            "\nboobs in lounge"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_54',
        }, {
#EVENT 55##############################################################################################################################################
        'event_num': 'Event 55',
        'progress_needed': kitchen_boobs,
        'button_idle': Text([
            "Auntie's tits",
            "\non a platter"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_55',
        }, {
#EVENT 56##############################################################################################################################################
        'event_num': 'Event 56',
        'progress_needed': christmas_complete,
        'button_idle': Text([
            "Completed X-mas",
            "\nevent"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_56',
        }, {
#EVENT 57##############################################################################################################################################
        'event_num': 'Event 57',
        'progress_needed': park_full_menu,
        'button_idle': Text([
            "Sampled the whole",
            "\npark menu"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_57',
        }, {
#EVENT 58##############################################################################################################################################
        'event_num': 'Event 58',
        'progress_needed': progress >= 15,
        'button_idle': Text([
            "Full house"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_58',
        }, {
#EVENT 59##############################################################################################################################################
        'event_num': 'Event 59',
        'progress_needed': progress >= 16,
        'button_idle': Text([
            "lost my virginity",
            "\nto Sidney!!"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_59',
        }, {
#EVENT 60##############################################################################################################################################
        'event_num': 'NTR Event 60',
        'progress_needed': visits_to_stone >= 7 or campaign_finished and visits_to_stone <= 6,
        'button_idle': If(campaign_finished and visits_to_stone <= 6,
            Text([
                "You failed this event"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
            If(visits_to_stone >= 7,
                Text([
                    "Predatory Teacher"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5))),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_60',
        }, {
#EVENT 61##############################################################################################################################################
        'event_num': 'Event 61',
        'progress_needed': mandy_at_school,
        'button_idle': Text([
            "Mandy's at school"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_61',
        }, {
#EVENT 62##############################################################################################################################################
        'event_num': 'Event 62',
        'progress_needed': megan_told_counter >= 1 or campaign_finished and megan_told_counter == 0,
        'button_idle': If(campaign_finished and megan_told_counter == 0,
            Text([
                "You failed this event"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
            If(megan_told_counter >= 1,
                Text([
                    "Double Agent"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5))),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_62',
        }, {
#EVENT 63##############################################################################################################################################
        'event_num': 'Event 63',
        'progress_needed': spycammandymbatebath,
        'button_idle': Text([
            "Mandy masturbated",
            "\nin the shower"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_63',
        }, {
#EVENT 64##############################################################################################################################################
        'event_num': 'Event 64',
        'progress_needed': mandymbatespycam,
        'button_idle': Text([
            "Mandy masturbated",
            "\nin Mom's bedroom"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_64',
        }, {
#EVENT 65##############################################################################################################################################
        'event_num': 'Event 65',
        'progress_needed': spycamauntmbatebath,
        'button_idle': Text([
            "Auntie masturbated",
            "\nin the shower"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_65',
        }, {
#EVENT 66##############################################################################################################################################
        'event_num': 'Event 66',
        'progress_needed': auntmbatespycam,
        'button_idle': Text([
            "Auntie masturbated",
            "\nin Mom's bedroom"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_66',
        }, {
#EVENT 67##############################################################################################################################################
        'event_num': 'Event 67',
        'progress_needed': mandys_fun_night,
        'button_idle': Text([
            "Truth or Dare?"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_67',
        }, {
#EVENT 68##############################################################################################################################################
        'event_num': 'Event 68',
        'progress_needed': best_result_counter >= 4 or campaign_finished,
        'button_idle': If(campaign_finished and best_result_counter <= 3,
            Text([
                "You failed this event"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
            If(best_result_counter >= 4,
                Text([
            "Lauren's Grateful"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5))),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_68',
        }, {
#EVENT 69##############################################################################################################################################
        'event_num': 'Event 69',
        'progress_needed': saved_their_asses,
        'button_idle': Text([
            "Saved their asses"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_69',
        }, {
#EVENT 70##############################################################################################################################################
        'event_num': 'NTR Event 70',
        'progress_needed': gave_their_asses,
        'button_idle': Text([
            "Gave their asses"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_70',
        }, {
#EVENT 71##############################################################################################################################################
        'event_num': 'Event 71',
        'progress_needed': will_email_received or campaign_finished,
        'button_idle': If(campaign_finished and not will_email_received,
            Text([
                "You failed this event"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
            If(will_email_received,
                Text([
            "Date with Will"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5))),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_71',
        }, {
#EVENT 72##############################################################################################################################################
        'event_num': 'Event 72',
        'progress_needed': had_park_sex,
        'button_idle': Text([
            "Getting wet",
            "\nin the park"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_72',
        }, {
#EVENT 73##############################################################################################################################################
        'event_num': 'Event 73',
        'progress_needed': had_br_sex,
        'button_idle': Text([
            "Getting wet",
            "\nin bed"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_73',
        }, {
#EVENT 74##############################################################################################################################################
        'event_num': 'Event 74',
        'progress_needed': had_wr_sex,
        'button_idle': Text([
            "getting wet at the",
            "\nwomb raider shoot."], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_74',
        }, {
#EVENT 75##############################################################################################################################################
        'event_num': 'Event 75',
        'progress_needed': had_club_sex_again,
        'button_idle': Text([
            "Getting wet",
            "\nat the club"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_75',
        }, {
#EVENT 76##############################################################################################################################################
        'event_num': 'Event 76',
        'progress_needed': campaign_finished,
        'button_idle': Text([
            "Intern to the",
            "\nPresident"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_76',
        }, {
#EVENT 77##############################################################################################################################################
        'event_num': 'Event 77',
        'progress_needed': ma_event >= 1,
        'button_idle': Text([
            "Morning",
            "\nAnnouncements"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_77',
        }, {
#EVENT 78##############################################################################################################################################
        'event_num': 'Event 78',
        'progress_needed': got_ntred or l_lounge_fucked,
        'button_idle': Text([
            "Creamed in",
            "\nthe lounge"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_78',
        }, {
#EVENT 79##############################################################################################################################################
        'event_num': 'Event 79',
        'progress_needed': dragon_fuck or dragon_fuck_ntr,
        'button_idle': Text([
            "Breeding the",
            "\ndragon breeder"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_79',
        }, {
#EVENT 80##############################################################################################################################################
        'event_num': 'Event 80',
        'progress_needed': fucked_lauren_bath,
        'button_idle': Text([
            "Even dirtier",
            "\nafter shower"], outlines=[(1.1, "#000000", 0, 0)], text_align=0.5),
        'button_ypos': 0.35,
        'new_context_call': 'event_info_80',
        }]

    frame xalign 0.510 yalign 0.33:# at truecenter:
        background None
        has vbox

        text _("Press the \"{color=#E60000}???{/color}\" to see \n             hints!") at center:
            outlines [(3, "#000", 0,0)]

        textbutton _("Watch the tutorial again!"):
            text_outlines [(3, "#E60000", 0,0)]
            action ui.callsinnewcontext("again_tutorial")

        text _("") size 3

        text _("{color=#E60000}-------------------------------------{/color}") #at center

        side ("c"):
            area (1,0,315,400)
            viewport id "events_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                draggable True mousewheel True
                vbox:

                    text _("") size 20

                    for e in event_list:
                        use event_details(e)

                    for e in event_list:
                        use event_compleated(e)

#                    for e in event_list:
#                        if not e['progress_needed']:
#                            use event_details(e)
#                        else:
#                            use event_compleated(e)
#                        text _("") size 10

                    text _("") size 20

            #vbar value YScrollValue("events_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG


    imagebutton auto "images/interface_images/phone_screen_images/home_%s.png":
        action [ Hide("event_screen"), Show("phone_interface") ]
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

label event_info_02:
    if dadpictureprogress == 0:
        RT "{i}I should go to the family portrait first to reminisce.{/i}"
    else:
        RT "{i}I need to go talk to Uncle Bobby at the warehouse. I can get there by looking at the city map.{/i}"

    return

label event_info_03:
    if progress <= 1:
        RT "{i}I need to complete event 2 before I can even start event 3.{/i}"
    else:
        RT "{i}I need to go to my house and talk to Mom. She should be in the kitchen.{/i}"

    return

label event_info_04:
    if sawmomstripping == False:
        RT "{i}I need to complete event 3 before I can even start event 4.{/i}"
    else:
        RT "{i}I think Mom's probably pretty shook up. I should go check on her in her room.{/i}"

    return

label event_info_05:
    if progress <= 3:
        RT "{i}I need to complete event 4 before I can even start event 5.{/i}"
    else:
        RT "{i}Lauren likes to hang out in the living room in the evenings. Maybe I should go see her.{/i}"

    return

label event_info_06:
    if progress <= 4:
        RT "{i}I need to finish event 5 before I can even start event 6.{/i}"
    else:
        RT "{i}I should go to the kitchen in the evening for family dinner.{/i}"

    return

label event_info_07:
    if progress <= 3:
        RT "{i}I need to complete event 4 before I can even start event 7.{/i}"
    if schoolprogress == 0:
        RT "{i}I need to go to school in the late morning or afternoon.{/i}"
    if ntrcontent == True:
        RT "{i}I need to visit the first stall in the school bathroom in the afternoon.{/i}"
    if first_htbyd_shoot == True:
        RT "{i}Weird.... I can't finish this event until after I finish event 27.... Must be because I told Matt I didn't want his help seducing Mom.{/i}"
    else:
        RT "{i}I need to go to school and hang out in the hallway in the late morning.{/i}"

    return

label event_info_08:
    if progress <= 3:
        RT "{i}I need to complete event 4 before I can even start event 8.{/i}"
    else:
        RT "{i}Mom works really hard all week.  I should help her with jobs around the house on weekend mornings. She usually starts cleaning in the lounge.{/i}"

    return

label event_info_09:
    if progress <= 5:
        RT "{i}I need to complete event 6 before I can even start event 9.{/i}"
    if failedsneakattempt == False:
        RT "{i}I need to sneak into Lauren's room at night and see if I can use subliminal messages on the girls.{/i}"
    if failedsneakattempt == True and tookmelatonin == False:
        RT "{i}I need to buy some melatonin from the online store on my laptop in my bedroom and spike the tea in the kitchen.{/i}"
    if tookmelatonin == True and sidneyfingerlaurenprogress == 1:
        RT "{i}The girls should be sleeping deeper at night. I should go pay them another visit.{/i}"
    if sidneyfingerlaurenprogress >= 2 and sidneyfingerlaurenprogress <=3:
        RT "{i}I need to keep sneaking into the girls room at night until I complete this event.{/i}"

    return

label event_info_10:
    if physical_fitness >= 1:
        RT "{i}I should keep running with Sidney during the early morning to complete this event.{/i}"
        return
    if sidneyfingerlaurenprogress >= 5:
        RT "{i}I should go see Sidney during the early morning in the lounge and see if she needs a running buddy.{/i}"
        return
    if progress >= 5:
        RT "{i}I should see if I can scare Sidney in the lounge at night.{/i}"
        return
    else:
        RT "{i}I need to complete event 9 before I can start event 10.{/i}"
    return

label event_info_11:
    if progress == 8:
        RT "{i}I should go to sleep and talk to Lauren and Cousin Mandy in the morning.{/i}"
    if sidneymakingcosplay == True:
        RT "{i}I should keep visiting the kitchen in the evening until Sidney is done with the cosplay costumes.{/i}"
    if sidneyfingerlaurenprogress >= 2:
        RT "{i}I need to visit Sidney in the evening and commission a cosplay outfit for Lauren.{/i}"
    if sidneyfingerlaurenprogress == 1:
        RT "{i}I need to start working on event 8 before I can start working on event 11.{/i}"

    return

label event_info_12:
    if not look_for_bathrobe:
        RT "{i}I need to keep whispering subliminal messages in Mom's ear at night.{/i}"
    if not first_bfast:
        RT "{i}I should go have breakfast with my family early in the morning and see if Mom's wearing her bathrobe.{/i}"
        RT "{i}I wonder what she would wear if the bathrobe were to suddenly dissapear.{/i}"
    else:
        RT "{i}I need to find and hide Mom's bathrobe. Most likely spot would be in her room.{/i}"
    return

label event_info_13:
    if not found_bathrobe:
        RT "{i}I need to complete event 12 before I can begin working on this event.{/i}"
    else:
        RT "{i}I should keep visiting Mom at night.{/i}"

    return

label event_info_14:
    if not no_more_sub:
        RT "{i}I need to keep whispering subliminal messages in Lauren's ear at night.{/i}"
    else:
        RT "{i}I should keep visiting Lauren at night.{/i}"

    return

label event_info_15:
    if progress <= 3:
        RT "{i}I need to complete event 4 before I can begin event 15.{/i}"
        return
    if clubcounter <= 4:
        RT "{i}If I don't pay the Mafia for more than 3 weeks in a row, I might just complete this NTR event.{/i}"
        return
    else:
        RT "{i}When Mom goes to the club, I need to go check on her to see how she's doing.{/i}"

    return

label event_info_16:
    if fixed_bulb == False:
        RT "{i}I need to complete event 8 before I can begin event 16.{/i}"
        return
    if lectureprogress <= 2:
        RT "{i}I need to get mom to loosen up a little more.  Maybe I can corrupt her with our Oedipus assignment at school.{/i}"
        return
    else:
        RT "{i}Mom works really hard all week.  I should help her with jobs around the house on weekend mornings. She usually starts cleaning in the lounge.{/i}"

    return

label event_info_17:
    if spycaminbath == True:
        RT "{i}I've placed the spycam in the bathroom. Now I just need to catch Mom in there when her libido is at it's highest (10 pts).{/i}"
    if failedsneakattempt == True and spycaminbath == False:
        RT "{i}I need to buy a spy-cam and place it in the bathroom when no one is around.{/i}"
    if progress <= 6:
        RT "{i}I need to start working on event 8 before I can start working on event 17.{/i}"

    return

label event_info_18:
    if spycaminmomroom == True:
        RT "{i}I've placed the spycam in Mom's bedroom. Now I just need to catch Mom in there when her libido is at it's highest (10 pts).{/i}"
    if failedsneakattempt == True and spycaminmomroom == False:
        RT "{i}I need to buy a spy-cam and place it in Mom's bedroom when no one is around.{/i}"
    if progress <= 6:
        RT "{i}I need to start working on event 8 before I can start working on event 18.{/i}"

    return

label event_info_19:
    if spycaminbath == True:
        RT "{i}I've placed the spycam in the bathroom. Now I just need to catch Lauren in there when her libido is at it's highest (10 pts).{/i}"
    if failedsneakattempt == True and spycaminbath == False:
        RT "{i}I need to buy a spy-cam and place it in the bathroom when no one is around.{/i}"
    if progress <= 6:
        RT "{i}I need to start working on event 8 before I can start working on event 19.{/i}"

    return

label event_info_20:
    if spycaminlaurenroom == True:
        RT "{i}I've placed the spycam in Lauren's bedroom. Now I just need to catch Lauren in there when her libido is at it's highest (10 pts).{/i}"
    if failedsneakattempt == True and spycaminlaurenroom == False:
        RT "{i}I need to buy a spy-cam and place it in Lauren's bedroom when no one is around.{/i}"
    if progress <= 6 :
        RT "{i}I need to start working on event 8 before I can start working on event 20.{/i}"

    return

label event_info_21:
    if spycaminbath == True:
        RT "{i}I've placed the spycam in the bathroom. Now I just need to catch Sidney in there when her libido is at it's highest (10 pts).{/i}"
    if failedsneakattempt == True and spycaminbath == False:
        RT "{i}I need to buy a spy-cam and place it in the bathroom when no one is around.{/i}"
    if progress <= 6:
        RT "{i}I need to start working on event 8 before I can start working on event 21.{/i}"

    return

label event_info_22:
    if spycaminlaurenroom == True:
        RT "{i}I've placed the spycam in Lauren's bedroom. Now I just need to catch Sidney in there when her libido is at it's highest (10 pts).{/i}"
    if failedsneakattempt == True and spycaminlaurenroom == False:
        RT "{i}I need to buy a spy-cam and place it in Lauren's bedroom when no one is around.{/i}"
    if progress <= 6:
        RT "{i}I need to start working on event 8 before I can start working on event 22.{/i}"

    return

label event_info_23:
    if progress <= 3:
        RT "{i}I need to complete event 4 before I can begin event 23.{/i}"
    if email_alert_one == False:
        RT "{i}I need to keep Mom out of the club by paying the Mafia debt for more than 3 weeks in a row.{/i}"
    else:
        RT "{i}I got an email ad on my phone for a bikini. I better buy it as soon as I can just in case I need it before the next weekend.{/i}"

    return

label event_info_24:
    if inventory.inv_amount(jacky_bikini_01) == 0:
        RT "{i}I need to complete event 23 before I can begin event 24.{/i}"
    else:
        RT "{i}I've got the bikini now. I would be smart to make sure Mom's libido and submission are as high as possible, then maybe I can ask her to try on the swimsuit for me.{/i}"

    return

label event_info_25:
    if progress <= 3:
        RT "{i}I need to complete event 4 before I can begin event 25.{/i}"
    if firstclubvisit == False:
        RT "{i}I need to keep Mom out of the club by paying the Mafia debt for more than 3 weeks in a row. Maybe she'll reward me with some one-on-one time.{/i}"

    return

label event_info_26:
    if progress == 10 and sidneymakingcosplay == True:
        RT "{i}I should keep checking the kitchen to see when Sidney will be done with Lauren's cosplay outfit.{/i}"
    if progress == 10 and sidneymakingcosplay == False:
        RT "{i}I should go talk to Sidney about commissioning another cosplay outfit.{/i}"
    if progress <= 9:
        RT "{i}I need to complete event 11 before I can start working on event 26.{/i}"

    return

label event_info_27:
    if progress <= 11:
        RT "{i}I need to complete event 26 before I can start on event 27.{/i}"
    else:
        RT "{i}I need to go to the warehouse in the late morning to take pictures with Lauren.{/i}"

    return

label event_info_28:
    if first_htbyd_shoot:
        RT "{i}I need to complete event 27 before I can start on event 28.{/i}"
    else:
        RT "{i}I need to keep taking these \"How to Breed your Dragon\" pictures with Lauren until we've got every kind of picture we need.{/i}"

    return

label event_info_29:
    if progress <= 11:
        RT "{i}I need to complete event 27 before I can complete event 29.{/i}"
    else:
        RT "{i}I've got a visitor coming on Thursday morning, but I don't know that yet. I need to pay the visitor off when I'm given the option.{/i}"

    return

label event_info_30:
    if progress <= 11:
        RT "{i}I need to complete event 27 before I can complete event 30.{/i}"
    else:
        RT "{i}I've got a visitor coming on Thursday morning, but I don't know that yet. I need to refuse to pay them when I'm given the option.{/i}"

    return

label event_info_31:
    if not finished_htbyd_shoot:
        RT "{i}I need to complete event 28 before I can start on this event.{/i}"
        return
    if tv_events == 0:
        RT "{i}I should watch some tv with Lauren in the Lounge. Maybe the more she watches \"Game of Thots\", the more open she'll be to messing around a little.{/i}"
        return
    else:
        RT "{i}I've heard the school is going to start doing morning announcements every Monday again. They stopped when the student body officers left for New York on their mock UN trip.{/i}"
        RT "{i}I've heard they have an exciting announcement to start it off. I'd better make sure I'm in {b}Mom's class every Monday morning{/b} so I don't miss the announcements.{/i}"
        return

label event_info_32:
    if not start_of_campaign:
        RT "{i}I need to complete event 31 before I can start on this event.{/i}"
        return
    else:
        RT "{i}I've got a great idea to help Lauren win votes. I need to keep trying to convince her until she agrees.{/i}"
        return

label event_info_33:
    if progress <= 3:
        RT "{i}I need to complete event 4 before I can complete event 33.{/i}"
    if lectureprogress <= 1:
        RT "{i}I need to attend class until I have the option to \"Talk to Mom about the Oedipus assignment.\"{/i}"
    if lectureprogress >= 4:
        RT "{i}I need to keep \"Talking to Mom about the Oedipus assignment\" in her office until I have the option to look for Matt and Megan.{/i}"
        RT "{i}Once I have that option, I need to look in the girls locker room.{/i}"

    return

label event_info_34:
    if lectureprogress <= 4:
        RT "{i}I need to complete most of event 33 before I complete event 34.{/i}"
    else:
        RT "{i}I just need to choose to resist the urge to peek, instead of looking for Matt and Megan.{/i}"

    return

label event_info_35:
    if not sexy_posters_approved:
        RT "{i}I need to complete event 32 before I can start on this event.{/i}"
        return
    else:
        RT "{i}After our afternoon campaign meetings in the girls bathroom, I have the option to go see Mrs. Stone. {p}She can help me make some kick-ass posters.{/i}"
        return

label event_info_36:
    if fixed_sink == 0:
        RT "{i}I need to complete event 16 before I complete event 36.{/i}"
        return
    if jr_watched == False:
        RT "{i}I need to complete event 34 before I can complete 36.{/i}"
        return
    else:
        RT "{i}Mom works really hard all week.  I should help her with jobs around the house on weekend mornings. She usually starts cleaning in the lounge.{/i}"

    return

label event_info_37:
    if finished_htbyd_shoot == False and first_lauren_grind == False:
        RT "{i}I need to complete either event 28 or event 29 to start working on this event.{/i}"
        return
    if tv_events <= 4:
        RT "{i}I need to keep visiting Lauren in the lounge during the evening to see how much she'll do for me.{/i}"
    return

label event_info_38:
    if first_htbyd_shoot == True:
        RT "{i} I need to complete event 27 to begin working on event 38.{/i}"
    if progress <= 12:
        RT "{i}I should see if I can push Sidney any further when we sleep together at night.{/i}"
    if progress <= 13:
        RT "{i}I need to keep checking the kitchen during the evenings to see if Sidney is done with her outfit.{/i}"
    else:
        RT "{i}I need to visit the photo-studio at the warehouse during the afternoon.{/i}"

    return

label event_info_39:
    if not posters_complete:
        RT "{i}I need to complete event 35 before I can start on this event.{/i}"
        return
    if not diazfirstvisit:
        RT "{i}I need to complete event 29 or 30 before I can start on this event.{/i}"
        return
    if not strategy_set:
        RT "{i}I need to keep meeting with the campaign team in the girls bathroom in the afternoon. Lauren is sure to come up with some good strategies.{/i}"
        return
    if diaz_van_counter == 0:
        RT "{i}We decided it would be good to visit Diaz and see if she can dig up some dirt on Matt.  I can probably find her van on my map on a weekday evening.{/i}"
        return
    else:
        RT "{i}I need to put a spy camera in the girls locker room.  It would probably be best to go early in the morning before it gets crowded.{/i}"
        return

label event_info_40:
    if first_wr_shoot == True:
        RT "{i}I need to keep taking these \"Womb Raider\" pictures with Sidney until we've got every kind of picture we need.{/i}"
    else:
        RT "{i}I need to complete event 38 to begin working on event 40.{/i}"

    return

label event_info_41:
    if finished_wr_shoot == False:
        RT "{i}I need to complete event 40 to begin working on event 41.{/i}"
    else:
        RT "{i}I need to go have a visit with Sidney in my bed tonight.{/i}"

    return

label event_info_42:
    if not locker_cam_placed:
        RT "{i}I need to complete event 39 before I can start on this event.{/i}"
        return
    else:
        RT "{i}I need to keep visiting Diaz in her van until I complete this event.{/i}"
        return

label event_info_43:
    if not start_of_campaign:
        RT "{i}I need to complete event 31 before I can start on this NTR event.{/i}"
        return
    if tv_events <= 4:
        RT "{i}I need to complete event 37 before I can finish this NTR event.{/i}"
        return
    else:
        RT "{i}If I don't help Lauren do well on her weekly poll numbers, I might not like the consequences.{/i}"
        return

label event_info_44:
    if jr_watched == False:
        RT "{i}I need to complete event 34 before I can start on this event.{/i}"
        return
    if first_bath_hjob == False:
        RT "{i}Same thing every weekend.  Pay the Mafia, hug Mom, get a boner, and throw her on the floor.{/i}"
        RT "{i}Hopefully something will be different the next time I pay the Mafia debt.{/i}"
    return

label event_info_45:
    if first_bath_hjob and firstloyaltyblowjob and finished_wr_shoot:
        RT "{i}I need to keep visiting Mom in her school office.{/i}"
        return
    if first_bath_hjob and firstntrblowjob and finished_wr_shoot:
        RT "{i}I need to keep visiting Mom in her school office.{/i}"
        return
    if not first_bath_hjob or not firstloyaltyblowjob or not finished_hp_shoot:
        RT "{i}I need to complete events 7, 40, and 44 before I can start on this event.{/i}"
        return
    if not first_bath_hjob or not firstntrblowjob or not finished_wr_shoot:
        RT "{i}I need to complete events 7, 40, and 44 before I can start on this event.{/i}"

    return

label event_info_46:
    if blackmailed_mom_megan and inventory.has_item(ball_gag):
        RT "{i}I should start the photshoot with Mom and Megan by going to the warehouse on a weekday evening.{/i}"
        return
    if blackmailed_mom_matt and inventory.has_item(ball_gag):
        RT "{i}I should start the photshoot with Mom and Megan by going to the warehouse on a weekday evening.{/i}"
        return
    if blackmailed_mom_megan and not inventory.has_item(ball_gag):
        RT "{i}I need to get a ball gag from somewhere.{/i}"
        return
    if blackmailed_mom_matt and not inventory.has_item(ball_gag):
        RT "{i}I need to get a ball gag from somewhere.{/i}"
        return
    if not blackmailed_mom_matt or not blackmailed_mom_megan:
        RT "{i}I need to complete event 45 before I can start working on this event.{/i}"
    return

label event_info_47:
    if not first_hp_shoot:
        RT "{i}I need to complete event 46 before I can start working on this event.{/i}"
    else:
        RT "{i}I should keep building Mom's submission by pushing her to do new things at the photoshoot.{/i}"

    return

label event_info_48:
    if finished_wr_shoot == False and fit_enough == False:
        RT "{i}I need to complete events 10 and 40 before I can start working on event 48.{/i}"
        return
    if finished_wr_shoot == False:
        RT "{i}I need to complete event 40 before I can start working on event 48.{/i}"
        return
    if fit_enough == False:
        RT "{i}I need to complete event 10 before I can start working on event 48.{/i}"
        return
    else:
        RT "{i}I need to keep running with Sidney during the early morning in the park to complete this event.{/i}"
    return

label event_info_49:
    if finished_wr_shoot == False:
        RT "{i}I need to complete event 40 before I can start working on this event.{/i}"
        return
    if finished_wr_shoot and sidney_spy == False:
        RT "{i}Sidney was acting funny when I told her about Mom. I'd better keep an eye on her this weekend when the Mafia comes for their weekly payment.{/i}"
    return

label event_info_50:
    if sidney_spy == False:
        RT "{i}I need to finish event 48 before I can start working on this event.{/i}"
        return
    if sidney_spy and more_club_bjs == False:
        RT "{i}I need to visit Sidney while she's working at the club, maybe she'll have some time for a little more fun.{/i}"
    return

label event_info_51:
    if progress <= 8:
        RT "{i}I need to complete event 11 before I can begin working on event 51.{/i}"
    if aunt_first_visit == False:
        RT "{i}I'll bet Aunt Cami will be angry about the pictures I took of Cousin Mandy. I should just wait for her visit.{/i}"
    if bobby_send_text == False:
        RT "{i}I've heard rumor that there's been some heat on Uncle Bobby I wonder if I'll hear from him soon.{/i}"
    else:
        RT "{i}I wonder what that text was about. I should go to the warehouse to see if Uncle Bobby is ok.{/i}"

    return

label event_info_52:
    if bobby_says_bye == False:
        RT "{i}I need to complete event 51 before I can begin working on event 52.{/i}"
    else:
        RT "{i}I should keep visiting Sidney in the evenings until Aunt Cami comes to visit again.{/i}"

    return

label event_info_53:
    if aunt_second_visit == False:
        RT "{i}I need to complete event 52 before I can begin working on event 53.{/i}"
    elif aunts_new_uniform == False:
        RT "{i}I should keep visiting the lounge in the late morning until I see Aunt Cami again.{/i}"
    elif first_time_chores == False:
        RT "{i}I should keep going to the kitchen in the late morning until I can assign Aunt Cami a chore to work on.{/i}"
    else:
        RT "{i}I need to build up Aunt Cami's libido or submission so I can do something even more mischievous to her in the bathroom.{/i}"

    return

label event_info_54:
    if first_time_chores == False:
        RT "{i}I need to start working of event 53 before I can begin working on event 54.{/i}"
    else:
        RT "{i}I need to build up Aunt Cami's libido or submission so I can make a deal with her in the lounge.{/i}"

    return

label event_info_55:
    if first_time_chores == False:
        RT "{i}I need to start working of event 53 before I can begin working on event 55.{/i}"
    else:
        RT "{i}I need to build up Aunt Cami's libido or submission so I can make a deal with her in the kitchen.{/i}"

    return

label event_info_56:
    if diazfirstvisit == False and first_sixtynine == False:
        RT "{i}I need to complete either event 29 or 30 before I can start on this event.{/i}"
        RT "{i}I also need to complete event 41.{/i}"
    elif first_sixtynine == False:
        RT "{i}I need to complete event 41 before I can start this event.{/i}"
    elif diazfirstvisit == False:
        RT "{i}I need to complete either event 29 or 30 before I can start this event.{/i}"
    else:
        RT "{i}I have a strange feeling something weird is about to happen to me. Maybe the feeling will go away when I go to sleep tonight.{/i}"
    return

label event_info_57:
    if mp_captured == False:
        RT "{i}I need to complete event 48 before I can start event 56.{/i}"
        return
    else:
        RT "{i}I need to go running with Sidney in the early morning and try everything she has to offer at the park.{/i}"
    return

label event_info_58:
    if mom_mischief <= 1:
        RT "{i}I need to complete event 13 before I can start this event.{/i}"
        return
    if lauren_mischief <= 1:
        RT "{i}I need to complete event 14 before I can start this event.{/i}"
        return
    if not diazfirstvisit:
        RT "{i}I need to complete either event 29 and or 30 before I can start this event.{/i}"
        return
    if not bathroom_boobs:
        RT "{i}I need to complete event 53 before I can start on this event.{/i}"
        return
    else:
        RT "{i}Now I just need to wait for something to happen early Sunday morning.{/i}"
    return

label event_info_59:
    if not park_full_menu:
        RT "{i}I need to complete event 57 before I can start on this event.{/i}"
        return
    if progress <= 14:
        RT "{i}I need to complete event 58 before I can start on this event.{/i}"
        return
    if not first_mafia_chat or not first_money_chat or not first_club_fun:
        RT "{i}I need to visit Sidney at the club and choose all the options.{/i}"
        return
    if first_mafia_chat and first_money_chat and first_club_fun and park_full_menu:
        RT "{i}I need to visit Sidney at the club on Monday night.{/i}"
    return

label event_info_60:
    if not posters_complete:
        RT "{i}I need to complete event 35 before I can start this event.{/i}"
        return
    if not fucked_sid:
        RT "{i}I need to complete event 59 before I can finish this event.{/i}"
        return
    else:
        RT "{i}Mrs. Stone is up for almost anything... I wonder how far she'll go if I keep visiting her each week.{/i}"
    return

label event_info_61:
    if progress <= 14:
        RT "{i}I need to complete event 58 before I can start this event.{/i}"
        return
    else:
        RT "{i}I think I've heard Mandy watching TV in the lounge with Lauren in the evenings. I should go see them.{/i}"
    return

label event_info_62:
    if not locker_cam_placed:
        RT "{i}I need to complete event 39 before I can start this event.{/i}"
        return
    if not fucked_sid:
        RT "{i}I need to complete event 59 before I can finish this event.{/i}"
        return
    else:
        RT "{i}I should talk to Megan in class about what Diaz recorded in the locker room.{/i}"
    return

label event_info_63:
    if progress <= 14:
        RT "{i}I need to complete event 58 before I can start this event.{/i}"
    else:
        RT "{i}Mandy always showers with Lauren, how am I going to catch her masturbating in the shower?{/i}"
        RT "{i}Wait! Doesn't she shower alone on Sundays?... If I visit the bathroom when her libido is full...{/i}"
    return

label event_info_64:
    if progress <= 14:
        RT "{i}I need to complete event 58 before I can start this event.{/i}"
    else:
        RT "{i}Mandy's always alone in her room in the evening. I wonder what I'll see if her libido is full.{/i}"
    return

label event_info_65:
    if progress <= 14:
        RT "{i}I need to complete event 58 before I can start this event.{/i}"
    else:
        RT "{i}Aunt Cami always showers in the afternoon, I wonder what I'll see if I spy on her when her libido is full.{/i}"
    return

label event_info_66:
    if progress <= 14:
        RT "{i}I need to complete event 58 before I can start this event.{/i}"
    else:
        RT "{i}Aunt Cami's always alone in Mom's room in the evening. I wonder what I'll see if her libido is full.{/i}"
    return

label event_info_67:
    if progress <= 14:
        RT "{i}I need to complete event 58 before I can start this event.{/i}"
    else:
        RT "{i}I should just keep visiting Lauren's room at night. I want to see where it will lead.{/i}"
    return

label event_info_68:
    if not start_of_campaign:
        RT "{i}I need to complete event 31 before I can start this event.{/i}"
        return
    if not truth_dare_completed:
        RT "{i}I need to keep Lauren happy by helping her do as good as possible in the polls. I also need to complete event 66 before I can start this event.{/i}"
        return
    else:
        RT "{i}I need to keep Lauren happy by helping her do as good as possible in the polls.{/i}"
    return

label event_info_69:
    if not truth_dare_completed:
        RT "{i}I need to complete event 67 before I can start this event.{/i}"
    else:
        RT "{i}With Cousin Mandy in Lauren's room, Agent Diaz's visits could get interesting. I should still make sure to pay to keep them safe.{/i}"
    return

label event_info_70:
    if not truth_dare_completed:
        RT "{i}I need to complete event 67 before I can start this event.{/i}"
    else:
        RT "{i}With Cousin Mandy in Lauren's room, Agent Diaz's visits could get interesting. What would happen if I dont pay her off?{/i}"
    return

label event_info_71:
    if not posters_complete:
        RT "{i}I need to complete event 35 before I can start this event.{/i}"
        return
    if not diaz_van_counter >= 3:
        RT "{i}I need to complete event 42 before I can start this event.{/i}"
        return
    if megan_told_counter == 0:
        RT "{i}I need to complete event 62 before I can start this event.{/i}"
        return
    if not will_strategy:
        RT "{i}I need to keep visiting Lauren's afternoon campaign meetings in the bathroom. She's bound to have an idea that's fire.{/i}"
        return
    if will_strategy and not will_visit:
        RT "{i}I need to visit school board member Will Tylor. I can probably find his office on my map in the late morning or afternoon.{/i}"
        return
    if will_visit and not will_email_sent:
        RT "{i}Will Tylor wants a fucking date with my mom?... Should I help him out?... Changing the dress code would almost guarantee that Lauren would win.{/i}"
        RT "{i}I'd have to convince Mom to go to dinner with him though... I don't know if she would. I think she hates him... I could ask her at breakfast. She seems to be in a better mood in the morning.{/i}"
        return
    if will_email_sent:
        RT "{i}I've sent Will an email letting him know my mom is willing to meet him for dinner. Now I've just got to wait for his reply. I'm sure it won't take longer than a week. I'll bet he sends it on Saturday when he's got a little more time.{/i}"
    return

label event_info_72:
    if progress <= 15:
        RT "{i}I need to complete event 58 before I can start this event.{/i}"
    else:
        RT "{i}After what Sidney and I did in the club, I wonder if she'll be willing to go further at the park.{/i}"
    return

label event_info_73:
    if progress <= 15:
        RT "{i}I need to complete event 59 before I can start this event.{/i}"
    else:
        RT "{i}After what Sidney and I did in the club, I wonder if she'll be willing to go further in the bedroom.{/i}"
    return

label event_info_74:
    if progress <= 15:
        RT "{i}I need to complete event 59 before I can start this event.{/i}"
    else:
        RT "{i}After what Sidney and I did in the club, I wonder if she'll be willing to go further after a photoshoot.{/i}"
    return

label event_info_75:
    if progress <= 15:
        RT "{i}I need to complete event 59 before I can start this event.{/i}"
    else:
        RT "{i}After what Sidney and I did in the club, I wonder if she'll be willing to keep doing it there.{/i}"
    return

label event_info_76:
    if not fucked_sid:
        RT "{i}I need to complete event 59 before I can start this event.{/i}"
    else:
        RT "{i}The more events, and school influence I gain, the better the outcome of the election. {p}The election will start on a Friday. I just need to be in class when it begins.{/i}"
        RT "{i}I'd better be sure I've completed all my tasks before... I won't be able to do them after the election.{/i}"
    return

label event_info_77:
    if not campaign_finished:
        RT "{i}I need to complete event 76 before I can start this event.{/i}"
    else:
        RT "{i}Now that Lauren is the student body president, she gets to read the morning announcements. I should listen to a few of them on Monday mornings.{/i}"
    return

label event_info_78:
    if not campaign_finished:
        RT "{i}I need to complete event 76 before I can start this event.{/i}"
    else:
        RT "{i}I'll bet I can go even further with Lauren when we watch tv in the evenings.{/i}"
    return

label event_info_79:
    if not campaign_finished:
        RT "{i}I need to complete event 76 before I can start this event.{/i}"
    elif not dragon_bj:
        RT "{i}I think Lauren and I both feel extra horny after a photoshoot. I wonder if I can push things any further after our next photo session.{/i}"
    else:
        RT "{i}I'll bet I can breed with Lauren the dragon breeder after our next photo session.{/i}"
    return

label event_info_80:
    if not campaign_finished:
        RT "{i}I need to complete event 76 before I can start this event.{/i}"
    else:
        RT "{i}With so many people in the house, it's hard to catch Lauren alone... She usually showers alone early on Saturday. That might be a good opportunity for some more fun.{/i}"
    return

label again_tutorial:
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
    R "Testing.... Testing.... Ok.... It looks like it's recording."
    scene bg Tutorial34
    with dissolve
    R "My name is [ryan].... And if you are watching this recording, it means that I am dead."
    R "Or I guess it could mean the extremely unlikely scenario, that my computer was hacked, and now some schmuck is using my story for financial gain."
    scene bg Tutorial28
    with dissolve
    R "Because the series of events I'm going to tell you about, is so unbelievable, it would make a great movie, or tv series."
    R "But probably the kind of tv series you could only see on HBO."
    scene bg Tutorial33
    with dissolve
    R "Please God, just don't let anybody make a crappy H-game out of this."
    scene bg Tutorial38
    with dissolve
    $ renpy.pause ()
    WT "Ummm.... Hi!"
    WT "Sorry to interrupt."
    WT "My name is Will Tylor and I just wanted to take this opportunity to welcome you to our \"awesome\" H-game, \"A Family Venture!\""
    WT "Back to you [ryan]."
    scene bg Tutorial33
    with dissolve
    scene bg Tutorial28
    with dissolve
    R "I wanted to record my version of the remarkable events that have occured over the last little while."
    R "I know many wouldn't understand why I've been doing the things I'm doing, if I didn't explain myself, so this is my attempt to justify my actions."
    R "I've been acquiring many items to help me achieve my goals, of saving those I love, and helping that love to become even more realized."
    scene bg Tutorial29
    with dissolve
    WT "Thanks [ryan].  Let me do a little explaining from here."
    scene bg Tutorial01
    with fade
    WT "This is a typical in game screen.  As [ryan] mentioned, you will acquire many items in the game."
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
    WT "while this symbol show you the time of day."
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
    WT "On the game map, you can get around to many locations by using the travel buttons."
    scene bg Tutorial06
    with dissolve
    WT "This button right here will open up a map of the house, where you can pick any room you would like to go to."
    scene bg Tutorial07
    with dissolve
    WT "You can also hover your cursor over this button, to open up the quick travel options."
    WT "These buttons will take you to any room in the house, as well as the world map."
    WT "Exploring the AFV world is vitally important, as you will find that some events only happen at certain times, and in certain places."
    WT "So have fun exploring!"
    scene bg Tutorial31
    with fade
    $ renpy.pause ()
    scene bg Tutorial30
    with dissolve
    R "I never can be sure who is following me, even though I have my suspicions."
    R "Always having to watch my back, has made me grow closer to the few people I can trust."
    R "And who can I trust better than those that live right here with me?"
    "{i}\"(knock knock knock....)\"{/i}"
    M "{i}(muffled voice){/i} [ryan]?   Why is the door locked?  You're not looking at porn and masturbating again are you?"
    scene bg Tutorial32
    with dissolve
    R "No Mom!.... But I'm really busy right now!"
    M "With what?"
    R "Ummm.... Homework.... of course!"
    M "Well, ok.... But you know, you don't need to take care of yourself, right?"
    M "You know, that if you need some relief, you just need to let me know.  And If I'm too busy, I'm sure your sisters would be happy to help you out."
    scene bg Tutorial33
    with dissolve
    R "Ok!.... thanks Mom!"
    R "Please don't judge me until you've heard my side of the story."
    scene bg Tutorial34
    with dissolve
    R "It's like I said.... With so many shady characters around, tracking my movements, I've needed to grow closer to the people around me."
    scene bg Tutorial35
    with dissolve
    WT "Let me just jump in here one more time."
    scene bg Tutorial01
    with fade
    WT "To be successful, [ryan] has to influence those around him."
    WT "Relationship management is the most important part of this game."
    WT "You will need to make choices throughout the game that will influence the way the girls in your life feel about you."
    WT "So it's pretty important that you keep track of those stats."
    WT "You can access a girls stats,"
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
    WT "The angry emoji stands for a girls anger towards you.  It's hard to get them to do anything for you when they are mad."
    scene bg Tutorial25
    with dissolve
    WT "This whip icon, represents a girls submission to you."
    scene bg Tutorial26
    with dissolve
    WT "And these lips represent a girls libido."
    scene bg Tutorial01
    with dissolve
    WT "To close the stats window, just press the \"P\" on your keyboard again."
    WT "Another handy way to track a girls stats is through your phone."
    scene bg Tutorial05
    with dissolve
    WT "You can access your phone by clicking on this button."
    scene bg Tutorial11
    with dissolve
    WT "Once your phone is pulled up, you can track a girls stats,"
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
    WT "And this extremely useful button let's you move forward in time."
    scene bg Tutorial01
    with dissolve
    WT "So that's all the tips we have for you.  Everything else you will have to figure out on your own, or I guess you could always find the walkthrough, or ask for help online."
    WT "However you decide to play.  We hope you enjoy the game."
    scene bg Tutorial35
    with dissolve
    WT "Go ahead and take it from here [ryan]!"
    scene bg Tutorial34
    with dissolve
    R "I guess the best thing I can do, is tell you my story, and let whomever watches this, be the judge of my actions."
    R "And once again, hope this story gets turned into a kick ass HBO series, and not a fucking lame-ass H-game."
    scene bg Tutorial30
    with dissolve
    R ".... So, until fairly recently, I was just a normal teenage kid like everybody else."
    R "Until I was woken up really early one day, by a phone call that would change my life forever...."
    R "...."
    scene bg SleepBlack
    with fade
    "End of tutorial."
    return

style events_style_label:
    size 20
    #bold True
    color "#888888" #00589E #E60000 #ffffff
    #hover_color "#c184ff"
    outlines [(3, "#000", 0,0)]
