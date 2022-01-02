
define audio.Blow01 = "music/Blow01.wav"
define audio.Camille01 = "music/Camille01.wav"
define audio.Mandy01 = "music/Mandy01.wav"

define SG = Character(_("SWAT Guy"), color="FF4500", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define CC = Character(_("Charlie the Chin"), color="5d4037", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define VP = Character(_("Voice on Phone"), color="263238", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define SR = Character(_("Stripper"), color="FF69B4", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define SRT = Character(_("Stripper's Thoughts"), color="263238", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define CD = Character(_("Candy"), color="FF69B4", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define CDT = Character(_("Candy's Thoughts"), color="263238", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define P1 = Character(_("Player 1"), color="2E2EFE", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define HG = Character(_("Hermione Bang'er"), color="B40404", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define HGT = Character(_("Hermione's Thoughts"), color="B40404", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define PM = Character(_("Professor McGargleCum"), color="B18904", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define PMT = Character(_("Professor McGargleCum's Thoughts"), color="2E2EFE", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define EV = Character(_("Eerie Voice"), color="81F781", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define MGT = Character(_("Megan's Thoughts"), color="99FF99", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define WTT = Character(_("Will Tylor's Thoughts"), color="9135D1", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])

define diaz_text = False
define no_more_sub = False
define lauren_mischief = 0
define lauren_door_locked = False
define most_attractive_counter = 0
define safest_truth = False
define daily_truth_counter = 0
define dare_counter = 0
define daily_dare_counter = 0
define truth_told = 0
define safe_truth = False
define s_risky_truth = False
define risky_truth = False
define v_risky_truth = False
define truth_dare_completed = False
define mandy_first_hj = False
define get_to_know_candy = False
define no_time_for_candy = False
define sidney_cum_loads_counter = 0
define blackmailed_mom_matt = False
define blackmailed_mom_megan = False
define commissioned_hp_outfit = False
define talked_about_hp = False
define ready_for_hp = False
define first_megan_breast_reveal = False
define hp_shoot_almost_finished = False
define didnt_watch = False
define mom_sucked_matt = True
define mom_sucked_ryan = True
define first_download = False
define weekly_hp_trigger = False
define finished_hp_shoot = False
define first_hp_shoot = False
define weekly_hp_complete = False
define watched_recap = False
define couldnt_resist = False
define first_aunt_exercise = False
define saw_aunt_exercise = False
define gaveauntgift = False
define gavecuzgift = False
define look_for_bathrobe = False
define found_bathrobe = False
define brobe_bfast = False
define mom_mischief = 0
define fucked_sid = False
define first_mandy_study_visit = False
define first_mandy_vgame_visit = False
define mandymbatespycam = False
define auntmbatespycam = False
define shower_scene_selector = 0
define spiedgirlsbathroom = False
define spiedmandybathroom = False
define spiedauntbathroom = False
define spycammandyshower = False
define spycammandymbatebath = False
define spycamauntshower = False
define spycamauntmbatebath = False
define had_park_sex = False
define had_br_sex = False
define had_wr_sex = False
define had_club_sex_again = False
define after_bondage_chat = False
define visited_mandy_evening = False
define move_in_bfast = False
define spied_mandy_bed = False
define played_the_game = False
define mandys_fun_night = False
define read_book1 = False
define read_book2 = False
define read_book3 = False
define passed_ph_test_1 = False
define passed_ph_test_2 = False
define passed_ph_test_3 = False
define answered_ph_wrong = False
define candy_danced = False
define diaz_came_for_mandy = False
define gave_their_asses = False
define saved_their_asses = False
define lauren_spanked = False
define mandy_spanked = False
define list_girl_characters = [ "", "_Mom", "_Lauren", "_Sidney", "_Aunt", "_Cousin" ]

default fut_ball_gag = 0
default fut_ph_book1 = 0
default fut_ph_book2 = 0
default fut_ph_book3 = 0

init:
    image DareVideo01 = Movie(play="video/DareVideo01.webm", start_image="images/DareVideo01F01.webp")
    image DareVideo02 = Movie(play="video/DareVideo02.webm", start_image="images/DareVideo02F01.webp")
    image DareVideo03 = Movie(play="video/DareVideo03.webm", start_image="images/DareVideo03F01.webp")
    image DareVideo04 = Movie(play="video/DareVideo04.webm", start_image="images/DareVideo04F01.webp")
    image LaurenMischiefVideo01 = Movie(play="video/LaurenMischiefVideo01.webm", start_image="images/LaurenMischiefVideo01F01.webp")
    image LaurenMischiefVideo02 = Movie(play="video/LaurenMischiefVideo02.webm", start_image="images/LaurenMischiefVideo02F01.webp")
    image SidFirstVideo01 = Movie(play="video/SidFirstVideo01.webm", start_image="images/SidFirstVideo01F01.webp")
    image SidFirstVideo02 = Movie(play="video/SidFirstVideo02.webm", start_image="images/SidFirstVideo02F01.webp")
    image SidFirstVideo03 = Movie(play="video/SidFirstVideo03.webm", start_image="images/SidFirstVideo03F01.webp")
    image SidFirstVideo04 = Movie(play="video/SidFirstVideo04.webm", start_image="images/SidFirstVideo04F01.webp")
    image SidFirstVideo05 = Movie(play="video/SidFirstVideo05.webm", start_image="images/SidFirstVideo05F01.webp")
    image SidFirstVideo06 = Movie(play="video/SidFirstVideo06.webm", start_image="images/SidFirstVideo06F01.webp")
    image SidFirstVideo07 = Movie(play="video/SidFirstVideo07.webm", start_image="images/SidFirstVideo07F01.webp")
    image SidFirstVideo08 = Movie(play="video/SidFirstVideo08.webm", start_image="images/SidFirstVideo08F01.webp")
    image OfficeVideo01 = Movie(play="video/OfficeVideo01.webm", start_image="images/OfficeVideo01F01.webp")
    image OfficeVideo02 = Movie(play="video/OfficeVideo02.webm", start_image="images/OfficeVideo02F01.webp")
    image OfficeVideo03 = Movie(play="video/OfficeVideo03.webm", start_image="images/OfficeVideo03F01.webp")
    image OfficeVideo04 = Movie(play="video/OfficeVideo04.webm", start_image="images/OfficeVideo04F01.webp")
    image HPCosplayVideo01 = Movie(play="video/HPCosplayVideo01.webm", start_image="images/HPCosplayVideo01F01.webp")
    image HPCosplayVideo02 = Movie(play="video/HPCosplayVideo02.webm", start_image="images/HPCosplayVideo02F01.webp")
    image HPCosplayVideo03 = Movie(play="video/HPCosplayVideo03.webm", start_image="images/HPCosplayVideo03F01.webp")
    image HPCosplayVideo04 = Movie(play="video/HPCosplayVideo04.webm", start_image="images/HPCosplayVideo04F01.webp")
    image HPCosplayVideo05 = Movie(play="video/HPCosplayVideo05.webm", start_image="images/HPCosplayVideo05F01.webp")
    image MandMastBedroomVideo01 = Movie(play="video/MandMastBedroomVideo01.webm", start_image="images/MandMastBedroomVideo01F01.webp")
    image AuntMastBedroomVideo01 = Movie(play="video/AuntMastBedroomVideo01.webm", start_image="images/AuntMastBedroomVideo01F01.webp")
    image MandyMbateShowerVideo01 = Movie(play="video/MandyMbateShowerVideo01.webm", start_image="images/MandyMbateShowerVideo01F01.webp")
    image AuntMbateShowerVideo01 = Movie(play="video/AuntMbateShowerVideo01.webm", start_image="images/AuntMbateShowerVideo01F01.webp")
    image BRSexVideo01 = Movie(play="video/BRSexVideo01.webm", start_image="images/BRSexVideo01F01.webp")
    image BRSexVideo02 = Movie(play="video/BRSexVideo02.webm", start_image="images/BRSexVideo02F01.webp")
    image RunSexVideo01 = Movie(play="video/RunSexVideo01.webm", start_image="images/RunSexVideo01F01.webp")
    image WRSexVideo01 = Movie(play="video/WRSexVideo01.webm", start_image="images/WRSexVideo01F01.webp")
    image WRSexVideo02 = Movie(play="video/WRSexVideo02.webm", start_image="images/WRSexVideo02F01.webp")
    image MFJobVideo01 = Movie(play="video/MFJobVideo01.webm", start_image="images/MFJobVideo01F01.webp")
    image MHDVideo01 = Movie(play="video/MHDVideo01.webm", start_image="images/MHDVideo01F01.webp")
    image JackOffVideo05 = Movie(play="video/JackOffVideo05.webm", start_image="images/JackOffVideo05F01.webp")
    image JOffMandyVideo01 = Movie(play="video/JOffMandyVideo01.webm", start_image="images/JOffMandyVideo01F01.webp")
    image DiazAgainVideo01 = Movie(play="video/DiazAgainVideo01.webm", start_image="images/DiazAgainVideo01F01.webp")
    image DiazAgainVideo02 = Movie(play="video/DiazAgainVideo02.webm", start_image="images/DiazAgainVideo02F01.webp")
    image DiazAgainVideo03 = Movie(play="video/DiazAgainVideo03.webm", start_image="images/DiazAgainVideo03F01.webp")
    image bg DareVideo01F01 = "DareVideo01F01.webp"
    image bg DareVideo02F01 = "DareVideo02F01.webp"
    image bg DareVideo03F01 = "DareVideo03F01.webp"
    image bg DareVideo04F01 = "DareVideo04F01.webp"
    image bg LaurenMischiefVideo01F01 = "LaurenMischiefVideo01F01.webp"
    image bg LaurenMischiefVideo02F01 = "LaurenMischiefVideo02F01.webp"
    image bg SidFirstVideo01F01 = "SidFirstVideo01F01.webp"
    image bg SidFirstVideo02F01 = "SidFirstVideo02F01.webp"
    image bg SidFirstVideo03F01 = "SidFirstVideo03F01.webp"
    image bg SidFirstVideo04F01 = "SidFirstVideo04F01.webp"
    image bg SidFirstVideo05F01 = "SidFirstVideo05F01.webp"
    image bg SidFirstVideo06F01 = "SidFirstVideo06F01.webp"
    image bg SidFirstVideo07F01 = "SidFirstVideo07F01.webp"
    image bg SidFirstVideo08F01 = "SidFirstVideo08F01.webp"
    image bg OfficeVideo01F01 = "OfficeVideo01F01.webp"
    image bg OfficeVideo02F01 = "OfficeVideo02F01.webp"
    image bg OfficeVideo03F01 = "OfficeVideo03F01.webp"
    image bg OfficeVideo04F01 = "OfficeVideo04F01.webp"
    image bg HPCosplayVideo01F01 = "HPCosplayVideo01F01.webp"
    image bg HPCosplayVideo02F01 = "HPCosplayVideo02F01.webp"
    image bg HPCosplayVideo03F01 = "HPCosplayVideo03F01.webp"
    image bg HPCosplayVideo04F01 = "HPCosplayVideo04F01.webp"
    image bg HPCosplayVideo05F01 = "HPCosplayVideo05F01.webp"
    image bg MandMastBedroomVideo01F01 = "MandMastBedroomVideo01F01.webp"
    image bg AuntMastBedroomVideo01F01 = "AuntMastBedroomVideo01F01.webp"
    image bg MandyMbateShowerVideo01F01 = "MandyMbateShowerVideo01F01.webp"
    image bg AuntMbateShowerVideo01F01 = "AuntMbateShowerVideo01F01.webp"
    image bg BRSexVideo01F01 = "BRSexVideo01F01.webp"
    image bg BRSexVideo02F01 = "BRSexVideo02F01.webp"
    image bg RunSexVideo01F01 = "RunSexVideo01F01.webp"
    image bg WRSexVideo01F01 = "WRSexVideo01F01.webp"
    image bg WRSexVideo02F01 = "WRSexVideo02F01.webp"
    image bg MFJobVideo01F01 = "MFJobVideo01F01.webp"
    image bg MHDVideo01F01 = "MHDVideo01F01.webp"
    image bg JackOffVideo05F01 = "JackOffVideo05F01.webp"
    image bg JOffMandyVideo01F01 = "JOffMandyVideo01F01.webp"
    image bg MoveInDay01 = "MoveInDay01.webp"
    image bg MoveInDay02 = "MoveInDay02.webp"
    image bg MoveInDay03 = "MoveInDay03.webp"
    image bg MoveInDay04 = "MoveInDay04.webp"
    image bg MoveInDay05 = "MoveInDay05.webp"
    image bg MoveInDay06 = "MoveInDay06.webp"
    image bg MoveInDay07 = "MoveInDay07.webp"
    image bg MoveInDay08 = "MoveInDay08.webp"
    image bg MoveInDay09 = "MoveInDay09.webp"
    image bg MoveInDay10 = "MoveInDay10.webp"
    image bg MoveInDay11 = "MoveInDay11.webp"
    image bg MoveInDay12 = "MoveInDay12.webp"
    image bg MoveInDay13 = "MoveInDay13.webp"
    image bg MoveInDay14 = "MoveInDay14.webp"
    image bg MoveInDay15 = "MoveInDay15.webp"
    image bg MoveInDay16 = "MoveInDay16.webp"
    image bg MoveInDay17 = "MoveInDay17.webp"
    image bg MoveInDay18 = "MoveInDay18.webp"
    image bg MoveInDay19 = "MoveInDay19.webp"
    image bg MoveInDay20 = "MoveInDay20.webp"
    image bg MoveInDay21 = "MoveInDay21.webp"
    image bg LaurenMischief01 = "LaurenMischief01.webp"
    image bg LaurenMischief02 = "LaurenMischief02.webp"
    image bg LaurenMischief03 = "LaurenMischief03.webp"
    image bg LaurenMischief04 = "LaurenMischief04.webp"
    image bg LaurenMischief05 = "LaurenMischief05.webp"
    image bg LaurenMischief06 = "LaurenMischief06.webp"
    image bg DiazAgainVideo01F01 = "DiazAgainVideo01F01.webp"
    image bg DiazAgainVideo02F01 = "DiazAgainVideo02F01.webp"
    image bg DiazAgainVideo03F01 = "DiazAgainVideo03F01.webp"
    image bg Dare01 = "Dare01.webp"
    image bg Dare02 = "Dare02.webp"
    image bg Dare03 = "Dare03.webp"
    image bg Dare04 = "Dare04.webp"
    image bg Dare05 = "Dare05.webp"
    image bg Dare06 = "Dare06.webp"
    image bg Dare07 = "Dare07.webp"
    image bg Dare08 = "Dare08.webp"
    image bg Dare09 = "Dare09.webp"
    image bg Dare10 = "Dare10.webp"
    image bg Dare11 = "Dare11.webp"
    image bg Dare12 = "Dare12.webp"
    image bg Dare13 = "Dare13.webp"
    image bg Dare14 = "Dare14.webp"
    image bg Dare15 = "Dare15.webp"
    image bg Dare16 = "Dare16.webp"
    image bg Dare17 = "Dare17.webp"
    image bg Dare18 = "Dare18.webp"
    image bg Dare19 = "Dare19.webp"
    image bg Dare20 = "Dare20.webp"
    image bg Dare21 = "Dare21.webp"
    image bg Dare22 = "Dare22.webp"
    image bg Dare23 = "Dare23.webp"
    image bg Dare24 = "Dare24.webp"
    image bg Dare25 = "Dare25.webp"
    image bg Dare26 = "Dare26.webp"
    image bg Dare27 = "Dare27.webp"
    image bg Dare28 = "Dare28.webp"
    image bg Dare29 = "Dare29.webp"
    image bg Dare30 = "Dare30.webp"
    image bg Dare31 = "Dare31.webp"
    image bg Dare32 = "Dare32.webp"
    image bg Dare33 = "Dare33.webp"
    image bg Dare34 = "Dare34.webp"
    image bg Dare35 = "Dare35.webp"
    image bg Dare36 = "Dare36.webp"
    image bg Dare37 = "Dare37.webp"
    image bg Dare38 = "Dare38.webp"
    image bg Dare39 = "Dare39.webp"
    image bg Dare40 = "Dare40.webp"
    image bg Dare41 = "Dare41.webp"
    image bg Dare42 = "Dare42.webp"
    image bg Dare43 = "Dare43.webp"
    image bg Dare44 = "Dare44.webp"
    image bg Dare45 = "Dare45.webp"
    image bg Dare46 = "Dare46.webp"
    image bg Dare47 = "Dare47.webp"
    image bg Dare48 = "Dare48.webp"
    image bg Dare49 = "Dare49.webp"
    image bg Dare50 = "Dare50.webp"
    image bg Dare51 = "Dare51.webp"
    image bg Dare52 = "Dare52.webp"
    image bg Dare53 = "Dare53.webp"
    image bg Dare54 = "Dare54.webp"
    image bg Dare55 = "Dare55.webp"
    image bg Dare56 = "Dare56.webp"
    image bg Dare57 = "Dare57.webp"
    image bg Dare58 = "Dare58.webp"
    image bg Dare59 = "Dare59.webp"
    image bg Dare60 = "Dare60.webp"
    image bg Dare61 = "Dare61.webp"
    image bg Dare62 = "Dare62.webp"
    image bg Dare63 = "Dare63.webp"
    image bg Dare64 = "Dare64.webp"
    image bg Dare65 = "Dare65.webp"
    image bg Dare66 = "Dare66.webp"
    image bg Dare67 = "Dare67.webp"
    image bg Dare68 = "Dare68.webp"
    image bg Dare69 = "Dare69.webp"
    image bg Dare70 = "Dare70.webp"
    image bg Dare71 = "Dare71.webp"
    image bg Dare72 = "Dare72.webp"
    image bg Dare73 = "Dare73.webp"
    image bg Dare74 = "Dare74.webp"
    image bg Dare75 = "Dare75.webp"
    image bg Dare76 = "Dare76.webp"
    image bg Dare77 = "Dare77.webp"
    image bg Dare78 = "Dare78.webp"
    image bg Dare79 = "Dare79.webp"
    image bg Dare80 = "Dare80.webp"
    image bg Dare81 = "Dare81.webp"
    image bg SidSex01 = "SidSex01.webp"
    image bg SidSex02 = "SidSex02.webp"
    image bg SidSex03 = "SidSex03.webp"
    image bg SidSex04 = "SidSex04.webp"
    image bg SidSex05 = "SidSex05.webp"
    image bg SidSex06 = "SidSex06.webp"
    image bg SidSex07 = "SidSex07.webp"
    image bg SidSex08 = "SidSex08.webp"
    image bg SidSex09 = "SidSex09.webp"
    image bg SidSex10 = "SidSex10.webp"
    image bg SidSex11 = "SidSex11.webp"
    image bg SidSex12 = "SidSex12.webp"
    image bg SidSex13 = "SidSex13.webp"
    image bg SidSex14 = "SidSex14.webp"
    image bg SidSex15 = "SidSex15.webp"
    image bg SidSex16 = "SidSex16.webp"
    image bg SidSex17 = "SidSex17.webp"
    image bg SidSex18 = "SidSex18.webp"
    image bg SidSex19 = "SidSex19.webp"
    image bg SidSex20 = "SidSex20.webp"
    image bg SidSex21 = "SidSex21.webp"
    image bg SidSex22 = "SidSex22.webp"
    image bg SidSex23 = "SidSex23.webp"
    image bg SidSex24 = "SidSex24.webp"
    image bg SidSex25 = "SidSex25.webp"
    image bg SidSex26 = "SidSex26.webp"
    image bg SidSex27 = "SidSex27.webp"
    image bg SidSex28 = "SidSex28.webp"
    image bg SidSex29 = "SidSex29.webp"
    image bg SidSex30 = "SidSex30.webp"
    image bg SidSex31 = "SidSex31.webp"
    image bg SidSex32 = "SidSex32.webp"
    image bg SidSex33 = "SidSex33.webp"
    image bg SidSex34 = "SidSex34.webp"
    image bg SidSex35 = "SidSex35.webp"
    image bg SidSex36 = "SidSex36.webp"
    image bg SidSex37 = "SidSex37.webp"
    image bg SidSex38 = "SidSex38.webp"
    image bg SidSex39 = "SidSex39.webp"
    image bg SidSex40 = "SidSex40.webp"
    image bg SidSex41 = "SidSex41.webp"
    image bg SidSex42 = "SidSex42.webp"
    image bg SidSex43 = "SidSex43.webp"
    image bg SidSex44 = "SidSex44.webp"
    image bg SidSex45 = "SidSex45.webp"
    image bg SidSex46 = "SidSex46.webp"
    image bg SidSex47 = "SidSex47.webp"
    image bg SidSex48 = "SidSex48.webp"
    image bg SidSex49 = "SidSex49.webp"
    image bg SidSex50 = "SidSex50.webp"
    image bg SidSex51 = "SidSex51.webp"
    image bg SidSex52 = "SidSex52.webp"
    image bg SidSex53 = "SidSex53.webp"
    image bg SidSex54 = "SidSex54.webp"
    image bg SidSex55 = "SidSex55.webp"
    image bg SidSex56 = "SidSex56.webp"
    image bg SidSex57 = "SidSex57.webp"
    image bg SidSex58 = "SidSex58.webp"
    image bg SidSex59 = "SidSex59.webp"
    image bg SidSex60 = "SidSex60.webp"
    image bg SidSex61 = "SidSex61.webp"
    image bg SidSex62 = "SidSex62.webp"
    image bg SidSex63 = "SidSex63.webp"
    image bg SidSex64 = "SidSex64.webp"
    image bg SidSex65 = "SidSex65.webp"
    image bg SidSex66 = "SidSex66.webp"
    image bg SidSex67 = "SidSex67.webp"
    image bg SidSex68 = "SidSex68.webp"
    image bg SidSex69 = "SidSex69.webp"
    image bg SidSex70 = "SidSex70.webp"
    image bg SidSex71 = "SidSex71.webp"
    image bg SidSex72 = "SidSex72.webp"
    image bg SidSex73 = "SidSex73.webp"
    image bg SidSex74 = "SidSex74.webp"
    image bg SidSex75 = "SidSex75.webp"
    image bg SidSex76 = "SidSex76.webp"
    image bg SidSex77 = "SidSex77.webp"
    image bg SidSex78 = "SidSex78.webp"
    image bg SidSex79 = "SidSex79.webp"
    image bg Office01 = "Office01.webp"
    image bg Office02 = "Office02.webp"
    image bg Office03 = "Office03.webp"
    image bg Office04 = "Office04.webp"
    image bg Office05 = "Office05.webp"
    image bg Office06 = "Office06.webp"
    image bg Office07 = "Office07.webp"
    image bg Office08 = "Office08.webp"
    image bg Office09 = "Office09.webp"
    image bg Office10 = "Office10.webp"
    image bg Office11 = "Office11.webp"
    image bg Office12 = "Office12.webp"
    image bg Office13 = "Office13.webp"
    image bg Office14 = "Office14.webp"
    image bg Office15 = "Office15.webp"
    image bg Office16 = "Office16.webp"
    image bg Office17 = "Office17.webp"
    image bg Office18 = "Office18.webp"
    image bg Office19 = "Office19.webp"
    image bg Office20 = "Office20.webp"
    image bg NSidneyKitchen02 = "NSidneyKitchen02.webp"
    image bg NSidneyKitchen03 = "NSidneyKitchen03.webp"
    image bg NSidneyKitchen05 = "NSidneyKitchen05.webp"
    image bg NSidneyKitchen07 = "NSidneyKitchen07.webp"
    image bg NSidneyKitchen09 = "NSidneyKitchen09.webp"
    image bg HPCosplay01 = "HPCosplay01.webp"
    image bg HPCosplay02 = "HPCosplay02.webp"
    image bg HPCosplay03 = "HPCosplay03.webp"
    image bg HPCosplay04 = "HPCosplay04.webp"
    image bg HPCosplay05 = "HPCosplay05.webp"
    image bg HPCosplay06 = "HPCosplay06.webp"
    image bg HPCosplay07 = "HPCosplay07.webp"
    image bg HPCosplay08 = "HPCosplay08.webp"
    image bg HPCosplay09 = "HPCosplay09.webp"
    image bg HPCosplay10 = "HPCosplay10.webp"
    image bg HPCosplay11 = "HPCosplay11.webp"
    image bg HPCosplay12 = "HPCosplay12.webp"
    image bg HPCosplay13 = "HPCosplay13.webp"
    image bg HPCosplay14 = "HPCosplay14.webp"
    image bg HPCosplay15 = "HPCosplay15.webp"
    image bg HPCosplay16 = "HPCosplay16.webp"
    image bg HPCosplay17 = "HPCosplay17.webp"
    image bg HPCosplay18 = "HPCosplay18.webp"
    image bg HPCosplay19 = "HPCosplay19.webp"
    image bg HPCosplay20 = "HPCosplay20.webp"
    image bg HPCosplay21 = "HPCosplay21.webp"
    image bg HPCosplay22 = "HPCosplay22.webp"
    image bg HPCosplay23 = "HPCosplay23.webp"
    image bg HPCosplay24 = "HPCosplay24.webp"
    image bg HPCosplay25 = "HPCosplay25.webp"
    image bg HPCosplay26 = "HPCosplay26.webp"
    image bg HPCosplay27 = "HPCosplay27.webp"
    image bg HPCosplay28 = "HPCosplay28.webp"
    image bg HPCosplay29 = "HPCosplay29.webp"
    image bg HPCosplay30 = "HPCosplay30.webp"
    image bg HPCosplay31 = "HPCosplay31.webp"
    image bg HPCosplay32 = "HPCosplay32.webp"
    image bg HPCosplay33 = "HPCosplay33.webp"
    image bg HPCosplay34 = "HPCosplay34.webp"
    image bg HPCosplay35 = "HPCosplay35.webp"
    image bg HPCosplay36 = "HPCosplay36.webp"
    image bg HPCosplay37 = "HPCosplay37.webp"
    image bg HPCosplay38 = "HPCosplay38.webp"
    image bg HPCosplay39 = "HPCosplay39.webp"
    image bg HPCosplay40 = "HPCosplay40.webp"
    image bg HPCosplay41 = "HPCosplay41.webp"
    image bg HPCosplay42 = "HPCosplay42.webp"
    image bg HPCosplay43 = "HPCosplay43.webp"
    image bg HPCosplay44 = "HPCosplay44.webp"
    image bg HPCosplay45 = "HPCosplay45.webp"
    image bg HPCosplay46 = "HPCosplay46.webp"
    image bg HPCosplay47 = "HPCosplay47.webp"
    image bg HPCosplay48 = "HPCosplay48.webp"
    image bg HPCosplay49 = "HPCosplay49.webp"
    image bg HPCosplay50 = "HPCosplay50.webp"
    image bg HPCosplay51 = "HPCosplay51.webp"
    image bg HPCosplay52 = "HPCosplay52.webp"
    image bg HPCosplay53 = "HPCosplay53.webp"
    image bg HPCosplay54 = "HPCosplay54.webp"
    image bg HPCosplay55 = "HPCosplay55.webp"
    image bg HPCosplay56 = "HPCosplay56.webp"
    image bg HPCosplay57 = "HPCosplay57.webp"
    image bg HPCosplay58 = "HPCosplay58.webp"
    image bg HPCosplay59 = "HPCosplay59.webp"
    image bg HPCosplay60 = "HPCosplay60.webp"
    image bg HPCosplay61 = "HPCosplay61.webp"
    image bg HPCosplay62 = "HPCosplay62.webp"
    image bg HPCosplay63 = "HPCosplay63.webp"
    image bg HPCosplay64 = "HPCosplay64.webp"
    image bg HPCosplay65 = "HPCosplay65.webp"
    image bg HPCosplay66 = "HPCosplay66.webp"
    image bg HPCosplay67 = "HPCosplay67.webp"
    image bg HPCosplay68 = "HPCosplay68.webp"
    image bg HPCosplay69 = "HPCosplay69.webp"
    image bg HPCosplay70 = "HPCosplay70.webp"
    image bg HPCosplay71 = "HPCosplay71.webp"
    image bg HPCosplay72 = "HPCosplay72.webp"
    image bg HPCosplay73 = "HPCosplay73.webp"
    image bg HPCosplay74 = "HPCosplay74.webp"
    image bg HPCosplay75 = "HPCosplay75.webp"
    image bg HPCosplay76 = "HPCosplay76.webp"
    image bg HPCosplay77 = "HPCosplay77.webp"
    image bg HPCosplay78 = "HPCosplay78.webp"
    image bg HPCosplay79 = "HPCosplay79.webp"
    image bg HPCosplay80 = "HPCosplay80.webp"
    image bg HPCosplay81 = "HPCosplay81.webp"
    image bg HPCosplay82 = "HPCosplay82.webp"
    image bg HPCosplay83 = "HPCosplay83.webp"
    image bg HPCosplay84 = "HPCosplay84.webp"
    image bg HPCosplay85 = "HPCosplay85.webp"
    image bg HPCosplay86 = "HPCosplay86.webp"
    image bg HPCosplay87 = "HPCosplay87.webp"
    image bg HPCosplay88 = "HPCosplay88.webp"
    image bg HPCosplay89 = "HPCosplay89.webp"
    image bg HPCosplay90 = "HPCosplay90.webp"
    image bg HPCosplay91 = "HPCosplay91.webp"
    image bg HPCosplay92 = "HPCosplay92.webp"
    image bg HPCosplay93 = "HPCosplay93.webp"
    image bg HPCosplay94 = "HPCosplay94.webp"
    image bg HPCosplay95 = "HPCosplay95.webp"
    image bg HPCosplay96 = "HPCosplay96.webp"
    image bg HPCosplay97 = "HPCosplay97.webp"
    image bg HPCosplay98 = "HPCosplay98.webp"
    image bg HPCosplay99 = "HPCosplay99.webp"
    image bg HPCosplay100 = "HPCosplay100.webp"
    image bg HPCosplay101 = "HPCosplay101.webp"
    image bg HPCosplay102 = "HPCosplay102.webp"
    image bg HPCosplay103 = "HPCosplay103.webp"
    image bg HPCosplay104 = "HPCosplay104.webp"
    image bg HPCosplay105 = "HPCosplay105.webp"
    image bg HPCosplay106 = "HPCosplay106.webp"
    image bg HPCosplay107 = "HPCosplay107.webp"
    image bg HPCosplay108 = "HPCosplay108.webp"
    image bg HPCosplay109 = "HPCosplay109.webp"
    image bg HPCosplay110 = "HPCosplay110.webp"
    image bg HPCosplay111 = "HPCosplay111.webp"
    image bg HPCosplay112 = "HPCosplay112.webp"
    image bg HPCosplay113 = "HPCosplay113.webp"
    image bg HPCosplay114 = "HPCosplay114.webp"
    image bg PStudioHP = "PStudioHP.webp"
    image bg AuntWorkout01 = "AuntWorkout01.webp"
    image bg AuntWorkout02 = "AuntWorkout02.webp"
    image bg AuntWorkout03 = "AuntWorkout03.webp"
    image bg AuntWorkout04 = "AuntWorkout04.webp"
    image bg AuntWorkout05 = "AuntWorkout05.webp"
    image bg AuntWorkout06 = "AuntWorkout06.webp"
    image bg AuntWorkout07 = "AuntWorkout07.webp"
    image bg AuntWorkout08 = "AuntWorkout08.webp"
    image bg AuntWorkout09 = "AuntWorkout09.webp"
    image bg AuntAngry01 = "AuntAngry01.webp"
    image bg AuntAngry02 = "AuntAngry02.webp"
    image bg AuntAngry03 = "AuntAngry03.webp"
    image bg AuntAngry04 = "AuntAngry04.webp"
    image bg SpyCamAuntAngryBedroom01 = "SpyCamAuntAngrySafeBedroom01.webp"#"SpyCamAuntAngryBedroom01.webp"
    image bg SpyCamAuntAngryBedroom02 = "SpyCamAuntAngrySafeBedroom02.webp"#"SpyCamAuntAngryBedroom02.webp"
    image bg BFast02 = "BFast02.webp"
    image bg BFast03 = "BFast03.webp"
    image bg BFast04 = "BFast04.webp"
    image bg BFast05 = "BFast05.webp"
    image bg BFast06 = "BFast06.webp"
    image bg BFast07 = "BFast07.webp"
    image bg BFast08 = "BFast08.webp"
    image bg BFast09 = "BFast09.webp"
    image bg BFast14 = "BFast14.webp"
    image bg BFast15 = "BFast15.webp"
    image bg BFast16 = "BFast16.webp"
    image bg BFast17 = "BFast17.webp"
    image bg BFast18 = "BFast18.webp"
    image bg BFast19 = "BFast19.webp"
    image bg BFast20 = "BFast20.webp"
    image bg BFast22 = "BFast22.webp"
    image bg BFast27 = "BFast27.webp"
    image bg MomSleep01 = "MomSleep01.webp"
    image bg MomSleep02 = "MomSleep02.webp"
    image bg MomSleep03 = "MomSleep03.webp"
    image bg MomSleep04 = "MomSleep04.webp"
    image bg MomSleep05 = "MomSleep05.webp"
    image bg MomSleep06 = "MomSleep06.webp"
    image bg MomSleep07 = "MomSleep07.webp"
    image bg MomSleep08 = "MomSleep08.webp"
    image bg MomSleep09 = "MomSleep09.webp"
    image bg MomSleep10 = "MomSleep10.webp"
    image bg MomSleep11 = "MomSleepSafe11.webp"#"MomSleep11.webp"
    image bg MomSleep12 = "MomSleepSafe12.webp"#"MomSleep12.webp"
    image bg MomSleep13 = "MomSleepSafe13.webp"#"MomSleep13.webp"
    image bg MomSleep14 = "MomSleepSafe14.webp"#"MomSleep14.webp"
    image bg MandyRoomMad01 = "MandyRoomMad01.webp"
    image bg MandyRoomMad02 = "MandyRoomMad02.webp"
    image bg MandyRoomMad03 = "MandyRoomMad03.webp"
    image bg MandyRoomMad04 = "MandyRoomMad04.webp"
    image bg MandyRoomMad05 = "MandyRoomMad05.webp"
    image bg MandyStudy01 = "MandyStudy01.webp"
    image bg MandyStudy02 = "MandyStudy02.webp"
    image bg MandyStudy03 = "MandyStudy03.webp"
    image bg MandyStudy04 = "MandyStudy04.webp"
    image bg MandyStudy05 = "MandyStudy05.webp"
    image bg MandyStudy06 = "MandyStudy06.webp"
    image bg SpyCamMandyBedroom01 = "SpyCamMandyBedroom01.webp"
    image bg SpyCamMandyBedroom02 = "SpyCamMandyBedroom02.webp"
    image bg SpyCamMandyBedroom03 = "SpyCamMandyBedroom03.webp"
    image bg SpyCamMandyBedroom04 = "SpyCamMandyBedroom04.webp"
    image bg MandMastBedroom01 = "MandMastBedroomSafe01.webp"#"MandMastBedroom01.webp"
    image bg MandMastBedroom02 = "MandMastBedroomSafe02.webp"#"MandMastBedroom02.webp"
    image bg MandMastBedroom03 = "MandMastBedroom03.webp"
    image bg MandMastBedroom04 = "MandMastBedroom04.webp"
    image bg MandMastBedroom05 = "MandMastBedroom05.webp"
    image bg MandMastBedroom06 = "MandMastBedroom06.webp"
    image bg MandMastBedroom07 = "MandMastBedroomSafe07.webp"#"MandMastBedroom07.webp"
    image bg MandMastBedroom08 = "MandMastBedroom08.webp"
    image bg MandMastBedroom09 = "MandMastBedroom09.webp"
    image bg MandMastBedroom10 = "MandMastBedroomSafe10.webp"#"MandMastBedroom10.webp"
    image bg MandMastBedroom11 = "MandMastBedroomSafe11.webp"#"MandMastBedroom11.webp"
    image bg AuntMastBedroom01 = "AuntMastBedroomSafe01.webp"#"AuntMastBedroom01.webp"
    image bg AuntMastBedroom02 = "AuntMastBedroomSafe02.webp"#"AuntMastBedroom02.webp"
    image bg AuntMastBedroom03 = "AuntMastBedroom03.webp"
    image bg AuntMastBedroom04 = "AuntMastBedroom04.webp"
    image bg AuntMastBedroom05 = "AuntMastBedroom05.webp"
    image bg MandyLaurenBath01 = "MandyLaurenBath01.webp"
    image bg MandyLaurenBath02 = "MandyLaurenBath02.webp"
    image bg MandyLaurenBath03 = "MandyLaurenBath03.webp"
    image bg MandyLaurenBath04 = "MandyLaurenBath04.webp"
    image bg MandyLaurenBath05 = "MandyLaurenBath05.webp"
    image bg MandyLaurenBath06 = "MandyLaurenBath06.webp"
    image bg MandyLaurenBath07 = "MandyLaurenBath07.webp"
    image bg MandyShower01 = "MandyShower01.webp"
    image bg MandyShower02 = "MandyShower02.webp"
    image bg MandyShower03 = "MandyShower03.webp"
    image bg MandyMBateShower01 = "MandyMbateShower01.webp"
    image bg MandyMBateShower02 = "MandyMbateShower02.webp"
    image bg MandyMBateShower03 = "MandyMBateShower03.webp"
    image bg MandySleepIn = "MandySleepIn.webp"
    image bg AuntMbateShower01 = "AuntMbateShower01.webp"
    image bg AuntMbateShower02 = "AuntMbateShower02.webp"
    image bg AuntMbateShower03 = "AuntMbateShower03.webp"
    image bg AuntMbateShower04 = "AuntMbateShower04.webp"
    image bg AuntShower01 = "AuntShower01.webp"
    image bg AuntShower02 = "AuntShower02.webp"
    image bg AuntShower03 = "AuntShower03.webp"
    image bg BRSex01 = "BRSex01.webp"
    image bg BRSex02 = "BRSex02.webp"
    image bg BRSex03 = "BRSex03.webp"
    image bg BRSex04 = "BRSex04.webp"
    image bg BRSex05 = "BRSex05.webp"
    image bg BRSex06 = "BRSex06.webp"
    image bg BRSex07 = "BRSex07.webp"
    image bg BRSex08 = "BRSex08.webp"
    image bg BRSex09 = "BRSex09.webp"
    image bg RunSex01 = "RunSex01.webp"
    image bg RunSex02 = "RunSex02.webp"
    image bg RunSex03 = "RunSex03.webp"
    image bg RunSex04 = "RunSex04.webp"
    image bg RunSex05 = "RunSex05.webp"
    image bg RunSex06 = "RunSex06.webp"
    image bg WRSex01 = "WRSex01.webp"
    image bg WRSex02 = "WRSex02.webp"
    image bg WRSex03 = "WRSex03.webp"
    image bg WRSex04 = "WRSex04.webp"
    image bg WRSex05 = "WRSex05.webp"
    image bg WRSex06 = "WRSex06.webp"
    image bg WRSex07 = "WRSex07.webp"
    image bg WRSex08 = "WRSex08.webp"
    image bg WRSex09 = "WRSex09.webp"
    image bg WRSex10 = "WRSex10.webp"
    image bg MandysPictures01 = "MandysPictures01.webp"
    image bg JackOffMandy05 = "JackOffMandy05.webp"
    image bg JackOffMandy06 = "JackOffMandy06.webp"
    image bg ImageMapCasino = "ImageMapCasino.webp"
    image bg ImageMapCasinoWSidney = "ImageMapCasinoWSidney.webp"
    image bg PHRead01 = "PHRead01.webp"
    image bg PHRead02 = "PHRead02.webp"
    image bg PHRead03 = "PHRead03.webp"
    image bg PHRead04 = "PHRead04.webp"
    image bg PHRead05 = "PHRead05.webp"
    image bg PHRead06 = "PHRead06.webp"
    image bg PHRead07 = "PHRead07.webp"
    image bg PHRead08 = "PHRead08.webp"
    image bg PHRead09 = "PHRead09.webp"
    image bg PHRead10 = "PHRead10.webp"
    image bg PHRead11 = "PHRead11.webp"
    image bg PHRead12 = "PHRead12.webp"
    image bg PHRead13 = "PHRead13.webp"
    image bg PHRead14 = "PHRead14.webp"
    image bg PHRead15 = "PHRead15.webp"
    image bg PHRead16 = "PHRead16.webp"
    image bg PHRead17 = "PHRead17.webp"
    image bg PHRead18 = "PHRead18.webp"
    image bg PHRead19 = "PHRead19.webp"
    image bg PHRead20 = "PHRead20.webp"
    image bg DiazAgain01 = "DiazAgain01.webp"
    image bg DiazAgain02 = "DiazAgain02.webp"
    image bg DiazAgain03 = "DiazAgain03.webp"
    image bg DiazAgain04 = "DiazAgain04.webp"
    image bg DiazAgain05 = "DiazAgain05.webp"
    image bg DiazAgain06 = "DiazAgain06.webp"
    image bg DiazAgain07 = "DiazAgain07.webp"
    image bg DiazAgain08 = "DiazAgain08.webp"
    image bg DiazAgain09 = "DiazAgain09.webp"
    image bg DiazAgain10 = "DiazAgain10.webp"
    image bg DiazAgain11 = "DiazAgain11.webp"
    image bg DiazAgain12 = "DiazAgain12.webp"
    image bg DiazAgain13 = "DiazAgain13.webp"
    image bg DiazAgain14 = "DiazAgain14.webp"
    image bg DiazAgain15 = "DiazAgain15.webp"
    image bg DiazAgain16 = "DiazAgain16.webp"
    image bg DiazAgain17 = "DiazAgain17.webp"
    image bg DiazAgain18 = "DiazAgain18.webp"
    image bg DiazAgain19 = "DiazAgain19.webp"
    image bg DiazAgain20 = "DiazAgain20.webp"
    image bg DiazAgain21 = "DiazAgain21.webp"
    image bg DiazAgain22 = "DiazAgain22.webp"
    image bg DiazAgain23 = "DiazAgain23.webp"
    image bg DiazAgain24 = "DiazAgain24.webp"
    image bg DiazAgain25 = "DiazAgain25.webp"
    image bg DiazAgain26 = "DiazAgain26.webp"
    image bg DiazAgain27 = "DiazAgain27.webp"
    image bg DiazAgain28 = "DiazAgain28.webp"
    image bg DiazAgain29 = "DiazAgain29.webp"
    image bg DiazAgain30 = "DiazAgain30.webp"
    image bg DiazAgain31 = "DiazAgain31.webp"
    image bg NDiazVisit40 = "NDiazVisit40.webp"
    image bg NDiazVisit42 = "NDiazVisit42.webp"
    image bg NDiazVisit43 = "NDiazVisit43.webp"

    image Brobe = "Brobe.webp"
    image Meme21 = "Meme21.webp"
    image Meme22 = "Meme22.webp"
    image Meme23 = "Meme23.webp"
    image Meme24 = "Meme24.webp"

    image bg Casino = "ImageMapCasino.webp"
    image bg CasinoWSidney = "ImageMapCasinoWSidney.webp"

#############  RYAN'S ROOM  #################################  RYAN'S ROOM  ####################################################

label move_in_day:
    scene bg SleepBlack
    with fade
    $ renpy.pause (1.0)
    scene bg RyanHomework01
    with fade
    RT "{i}I... think I slept in... What time is it?{/i}"
    scene bg RyansRoom01
    with fade
    RT "{i}It looks like Sidney already left to go running.{/i}"
    RT "{i}Isn't today Sunday? I should probably go see if Mom needs any help with the \"honey-do list\".{/i}"
    "{b}Ding Dong!{/b}"
    RT "{i}Who could that be?{/i}"
    scene bg SleepBlack
    with fade
    scene bg DiazVisit47
    with fade
    RT "{i}Why am I the only one in the house who ever answers the door?{/i}"
    scene bg MoveInDay01
    with dissolve
    AD "Well, there's the little twerp himself."
    R "The... bitch is back."
    RT "{i}Shit... That just sounded lame.{/i}"
    AD "Ok?...."
    R "Why are you here? It's not Thursday."
    R "Wait!... Is that a SWAT van in front of the house?"
    AD "You're very observant, [ryan]."
    R "Shit!... Are we in trouble?"
    scene bg MoveInDay02
    with dissolve
    AD "Why don't you tell me?"
    AD "What have you been up to lately?"
    R "Uhhhh...."
    RT "{i}What the fuck?... What the hell did I do?{/i}"
    scene bg MoveInDay01
    with dissolve
    AD "Hahaha... Relax... They're just helping me move a few things... hahaha... you should see the look on your face!"
    SG "Hey, Diaz!"
    scene bg MoveInDay03
    with dissolve
    AD "What?"
    SG "You gonna come help us unload all of this shit, or what?"
    AD "No! Why do you think I brought all of you strong guys along?"
    scene bg MoveInDay04
    with dissolve
    SG "Well, don't forget our deal!"
    SG "The Chief wouldn't be happy if he knew we were using our training time to help you."
    AD "Well, I'm making it worth your time."
    SG "O'Brien said you promised us each ten minutes, and if we can last that long, we all get a go at you at the same time."
    AD "Would you shut the hell up? Can't you see we're in front of a little boy?"
    R "Hey!... I'm 19!"
    AD "Just go throw all this stuff in the entryway and tell the other boys to do the same! We'll settle up later in the van."
    RT "{i}Holy fuck!... Did I understand that exchange right?{/i}"
    scene bg MoveInDay05
    with dissolve
    AD "Would you please do me a favor and go get your mom?"
    R "What's going on?"
    AD "You'll find out in just a few minutes, now will you please go get [mom_name]?"
    menu:
        "If I can watch what happens in the van later, I will.":
            AD "If you make a suggestion like that to me again, you'll be taking my place in the van!"
            R "Gross!"
            $ diaz_text = True
        "Alright... anything to get that image of Diaz in the van out of my head.":
            RT "{i}Gross!{/i}"
    scene bg SleepBlack
    with fade
    scene bg HoneyDoList03
    with fade
    $ renpy.pause ()
    RT "Hey, Mom."
    scene bg HoneyDoList06
    with fade
    M "Hey, honey! Who was at the door?"
    R "It's Agent Diaz of the FBI.  She wants to talk to you."
    M "Is it good news about your father?"
    R "I don't know.  But they are bringing in a bunch of luggage."
    M "Oh, maybe it's [dad_name]'s stuff!"
    M "Please stay here and finish sweeping for me."
    R "What? I want to see what's going on."
    scene bg HoneyDoList12
    with dissolve
    M "Please, [ryan]!..."
    R "Ok..."
    scene bg SleepBlack
    with fade
    "{i}\"A few minutes later\"{/i}"
    R "Finally finished, now I can go see what's going on."
    scene bg MoveInDay07
    with fade
    AD "So the nerds at the FBI noticed that all of Camille's bills were still getting paid, even though Uncle Bobby cleaned out all of his bank accounts."
    AD "They wanted to put you and Mandy in a tiny apartment in a dangerous part of town to make sure they could more easily monitor your transactions, but I convinced them that they should move you in with family instead."
    AD "That way, I can keep a close eye on Camille's finances and movements, since I'm already in charge of monitoring this household."
    C "I think we'd rather stay in the tiny apartment. There's only one bathroom in this house!"
    M "Well, go to the apartment then! No one's keeping you here."
    AD "Well, actually the FBI will be keeping you here."
    AD "And trust me, this place is much better.  Everyone we send to those apartments ends up getting bedbugs."
    C "Well... I wish that my Mandy didn't have to stay in the same house as that pervert, [ryan]!"
    M "He's no more perverted than any other young adult his age!"
    RT "{i}It's amazing how little my own mother knows me.{/i}"
    MT "{i}That's the biggest lie I've told this week.{/i}"
    scene bg MoveInDay06
    with dissolve
    MD "Mom! I'm 18 yrs old. I can take care of myself."
    C "Mandy...."
    MD "....[ryan]!"
    scene bg MoveInDay08
    with dissolve
    "{i}Smooch{/i}"
    scene bg MoveInDay10
    with dissolve
    MD "It's so good to see you! I've pretty much been locked up in my house since Mom found that picture!"
    MD "I'm sorry for all the shit she's put you through because of that! I tried to tell her it was our idea."
    R "I figured... it's good to see you too!"
    scene bg MoveInDay09
    with dissolve
    MD "{i}(whispering){/i} Does my mom look mad?"
    R "{i}(whispering){/i} Yeah..."
    MD "{i}(whispering){/i} Good! I love pissing her off!"
    MD "{i}(whispering){/i} I don't know what you did to her, but she really hates you!"
    scene bg MoveInDay10
    with dissolve
    MD "It's going to be so fun living here! I'm going to run and find Lauren."
    scene bg MoveInDay11
    with dissolve
    M "How long have you been standing there?"
    C "I don't care if he heard what I said. He already knows how I feel about him."
    M "Honey, will you go tell your sisters and cousin to meet in the lounge for a family meeting?"
    AD "Actually, I need to meet with [ryan] first."
    scene bg MoveInDay07
    with dissolve
    C "Is he in trouble?"
    AD "No, I just need to help show him how to declare his extra income with the FBI."
    C "Damn!"
    scene bg MoveInDay11
    with dissolve
    M "Alright [ryan]... When you're done, we'll meet you in the lounge."
    scene bg MoveInDay05
    with dissolve
    R "...."
    AD "Well?"
    R "Well, what?"
    AD "Aren't you going to thank me?"
    R "Thank you? For what?"
    AD "Well, for starters, I had to do some pretty creative technical cartwheels to keep your income, and your payments from Uncle Bobby hidden when the forensic accounting team started poking around."
    AD "They could tell there was money coming from somewhere, I just kept them from figuring out from where."
    AD "You'd be looking at a cell next to your dad if they had figured it out."
    R "Really? Just for trying to make money to take care of my family?"
    AD "Ahh... That would be a minor charge, the greater crime would be for giving a lot of that money to a suspected organized crime syndicate."
    R "But I have no choice!"
    AD "Yeah, that's what you call being stuck between a rock and a hard place."
    AD "And then the next thing you should be thanking me for, is for delivering two more playthings to live in your house of perversion."
    R "What?"
    AD "Oh, I've seen what you've been making your aunt do."
    AD "And, I've got to ask..."
    AD "How the hell have you been able to make your aunt wear that skimpy maid outfit without your mom finding out?"
    R "Well... she knows... it was kind of her idea."
    AD "Ha!... I knew your mom was a freak!"
    AD "You better keep her out of that club, cuz it won't be long until she's willingly giving her pussy to every customer that gives her a couple dollars."
    R "Shut up! She's not like that!"
    AD "You better hope she is if you want a shot at her."
    AD "And besides, as an FBI profiler, I'm pretty good at reading people."
    AD "You're just going to have to be really skillful in manipulating her into seeing you as her only option."
    AD "But from what I've seen, you should have no problems."
    RT "{i}Am I really that manipulative?{/i}"
    AD "Alright, I'm outta here!"
    scene bg MoveInDay02
    with dissolve
    AD "But when you're enjoying your time with your aunt and cousin, don't forget who hooked you up!"
    AD "And maybe you'll be willing to let me in on some of the fun sometime in the future."
    AD "Now I've got a whole SWAT team that are expecting to get paid for their help today."
    R "Are you really going to fuck them all?"
    scene bg MoveInDay01
    with dissolve
    AD "Haha... What do you think?"
    AD "Ya know, you and I aren't too different."
    AD "You earn money to gain influence and buy sex."
    AD "I use sex to gain influence and get money."
    R "We aren't the same at all!"
    AD "Think about it... I'm sure you'll eventually realize that I'm right."
    AD "See you Thursday!"
    scene bg DiazVisit47
    with dissolve
    RT "{i}I'm not anything like that bitch!... Am I?{/i}"
    RT "...."
    RT "{i}I'd better head to the lounge for the family meeting.{/i}"
    scene bg SleepBlack
    with fade
    scene bg MoveInDay12
    with fade
    M "Oh good, [ryan], you're here. Please sit down."
    scene bg MoveInDay14
    with fade
    M "As if our lives weren't crazy enough, we've had another new development."
    M "The FBI has decided that your Aunt Camille and Mandy should come live with us, since Uncle Bobby has taken all their money and they can't afford a place to live."
    M "They also want to keep an eye on them for various reasons, and since we're already being watched, they thought it just made sense to make 5 people live in a three bedroom, one bathroom house."
    scene bg MoveInDay13
    with fade
    R "I volunteer to share my bed with Aunt Camille."
    C "Yeah right, pervert! Mandy and I will be staying as far away from your room as possible."
    MD "I'll share your bed with you, [ryan]!"
    C "Oh, no you will not!"
    scene bg MoveInDay14
    with dissolve
    M "Relax, Camille"
    M "They're just teasing you."
    M "Nobody will be sharing [ryan]'s bed!"
    M "A teenage boy's bed is no place for any woman."
    scene bg MoveInDay16
    with fade
    ST "{i}That's right ho's! Only I get to sleep in [ryan]'s bed.{/i}"
    M "We'll have Mandy sleep with Lauren, and Camille will sleep with me."
    MD "Yay! Girl time!"
    scene bg MoveInDay15
    with dissolve
    C "What about the bathroom and showers?"
    M "Mandy will have to share the bathroom with Lauren in the {b}early morning{/b} before they both go to school."
    M "Camille, you can shower in the {b}afternoon{/b} after you're done working out with me, and done cleaning the house."
    C "I'm still the maid, huh?"
    M "Yeah, now you need to pull your weight more than ever."
    scene bg MoveInDay16
    with dissolve
    MD "I want to pull my weight too.  Is there anything I can do to help?"
    M "Hmmm... Do you know how to do any yard work?"
    M "I've had a hard time keeping on top of the yard, now that we cant afford a landscaper."
    MD "Sure... At least, I think I can figure it out."
    M "Well, maybe [ryan] can help you with anything you're unsure of."
    MD "All right, I can do the yardwork in the {b}evenings{/b} after I get home from school."
    scene bg MoveInDay14
    with fade
    M "Will you be changing schools?"
    C "Not yet.  Mandy's tuition has already been paid until the end of this semester."
    MD "This semester is almost over though, and then I'll probably have to go to public school, since we can't afford the private school you teach at."
    M "Well, let me talk to a few people, they might make an exception since you're my niece."
    MT "{i}Hopefully school board member Will Tylor won't want anything in exchange.{/i}"
    MD "Oh, I hope so! I'd love to go to school with Lauren and [ryan]!"
    M "Alright, I'll see what I can do."
    if diaz_text:
        play sound PhoneVibrate
        RT "{i}Huh?... Oh that's my phone.{/i}"
        scene bg MoveInDay17
        with dissolve
        RT "{i}text from a blocked number?{/i}"
        RT "{i}I wonder what this could be?{/i}"
        scene bg MoveInDay18
        with fade
        RT "{i}Do I dare click on the image to download it?{/i}"
        scene bg MoveInDay19
        with fade
        RT "{i}Oh, my God!{/i}"
        RT "{i}Is that Agent Diaz?{/i}"
        scene bg MoveInDay20
        with fade
        $ renpy.pause ()
        RT "{i}Wow! What a whore!{/i}"
        RT "{i}At least I have some photo evidence to blackmail her now.{/i}"
        scene bg MoveInDay21
        with dissolve
        RT "{i}What? Photo deleted?{/i}"
        RT "{i}Shit! Of course she's hacked my phone!{/i}"
        scene bg MoveInDay17
        with fade
        M "[ryan]?... Is that more important than our meeting?"
        R "What?... Oh sorry, no... I'm putting it away."
    else:
        pass
    scene bg MoveInDay13
    with dissolve
    M "Is there anything else we need to talk about?"
    L "If you can make it, we have a family breakfast every morning."
    scene bg MoveInDay14
    M "Yep, that's right. First thing in the morning."
    C "Mandy and I usually skip breakfast, so don't wait for us if we don't show up."
    M "Ok... Well, I think that's all we have."
    M "I know this living situation isn't ideal, but hopefully we can all get along and make the most of it."
    M "This experience can either bring us all closer together, or tear us apart."
    M "I'm begging all of you to put aside former grudges and differences, and try your best to get along!"
    scene bg MoveInDay16
    with fade
    S "Ok, Mom."
    L "Sure thing, Mom."
    MD "You got it, Aunt [mom_name]."
    menu:
        "I'm in!":
            "{i}{b}\"Mom's Respect +1\"{/b}{/i}"
            $ momrespect += 1
        "Only if Aunt Cami does.":
            M "That's not a very good attitude!"
            M "Please don't make your attitude conditional on her!"
            "{i}{b}\"Mom's Respect -1\"{/b}{/i}"
            $ momrespect -= 1
    C "...."
    M "...Camille?"
    C "...."
    scene bg MoveInDay15
    with dissolve
    C "Ok... I'll try my best."
    M "Great! Thank you eveyone for being patient and sitting through this little meeting."
    scene bg MoveInDay14
    with fade
    M "Let's help Aunt Camille and Mandy unpack their bags, and then get back to our normal routines."
    $ progress = 15
    $ timeofdaycounter += 1
    scene bg FamilyRoom01
    with fade
    $ screen_on = "loungemap"
    call screen loungemap

label posting_ph_pics:
    scene bg SleepBlack
    with fade
    play music Honey
    scene bg CosplayWarehouse20
    with fade
    RT "{i}I finally finished the Zad 3D work and photo editing.{/i}"
    RT "{i}They turned out pretty damn hot if I do say so myself.{/i}"
    RT "{i}Uploading the pictures now... and click submit... and now we just wait to see if anyone likes them.{/i}"
    scene bg SleepBlack
    with fade
    if not first_download:
        scene bg HPCosplay108
        with fade
        KT "{i}Oh, my God! Is that Miss [mom_name] posing with Megan!?{/i}"
        KT "{i}I've got to have this!{/i}"
        scene bg HPCosplay114
        with fade
        $ renpy.pause ()
        scene bg SleepBlack
        with fade
        scene bg HPCosplay109
        with fade
        J "Well... If it isn't the lovely, lovely [mom_name]"
        scene bg HPCosplay114
        with fade
        $ renpy.pause ()
        scene bg SleepBlack
        with fade
        scene bg HPCosplay110
        with fade
        S "Oh, my God!"
        L "He really did get Mom to do the photo shoot!"
        MD "Hahaha...."
        scene bg HPCosplay114
        with fade
        $ renpy.pause ()
        scene bg SleepBlack
        with fade
        scene bg HPCosplay111
        with fade
        AD "Haha... That manipulative son of a bitch got [mom_name] to do a photo shoot?"
        AD "This kid's going places."
        scene bg HPCosplay114
        with fade
        $ renpy.pause ()
        scene bg HPCosplay112
        with fade
        B "Oh... No way! How'd that fucker get my sister-in-law to pose for pics like that?"
        B "These pics are going into my \"Wank_Later\" folder."
        scene bg HPCosplay114
        with fade
        $ renpy.pause ()
        scene bg SleepBlack
        with fade
        scene bg HPCosplay113
        with fade
        WTT "{i}Well, well, well, one of our teachers is taking pictures with one of her students...{/i}"
        WTT "{i}I sincerely hope that student is an adult.{/i}"
        WTT "{i}I'd hate for there to be a hearing in front of the schoolboard.{/i}"
        WTT "{i}This is the kind of teacher that this district needs more of.{/i}"
        WTT "{i}The kind of teacher that goes out of her way to help a student persue extracurricular activities.{/i}"
        WTT "{i}I'll do whatever I can to defend a teacher like this.{/i}"
        scene bg HPCosplay114
        with fade
        $ renpy.pause ()
        $ first_download = True
        scene bg SleepBlack
        with fade
        jump myroom
    else:
        scene bg HPCosplay108
        with fade
        KT "{i}More pics of Megan and Miss [mom_name]?{/i}"
        KT "{i}I've got to have this!{/i}"
        scene bg HPCosplay114
        with fade
        $ renpy.pause ()
        scene bg SleepBlack
        with fade
        scene bg HPCosplay109
        with fade
        J "Ahh... Glad to see [mom_name]'s still at it."
        scene bg HPCosplay114
        with fade
        $ renpy.pause ()
        scene bg SleepBlack
        with fade
        scene bg HPCosplay110
        with fade
        S "Not again!"
        L "He got her to go back to the studio?!"
        MD "Hahaha...."
        scene bg HPCosplay114
        with fade
        $ renpy.pause ()
        scene bg SleepBlack
        with fade
        scene bg HPCosplay111
        with fade
        AD "Haha... More pics of the lovely [mom_name] with that skinny goddess?"
        AD "I love this kid!"
        scene bg HPCosplay114
        with fade
        $ renpy.pause ()
        scene bg HPCosplay112
        with fade
        B "YES!... Just what I was hoping for today!"
        B "These pics are going into my \"Wank_Later\" folder."
        scene bg HPCosplay114
        with fade
        $ renpy.pause ()
        scene bg SleepBlack
        with fade
        scene bg HPCosplay113
        with fade
        WTT "{i}How lovely! More pics of our lovely teacher [mom_name] and the beautiful Megan.{/i}"
        WTT "{i}I was so glad to find that Megan is an adult.{/i}"
        WTT "{i}Now we won't need to do any kind of investigation and Megan is free to pursue her desired extracurricular activities.{/i}"
        WTT "{i}I hope I get to meet this dedicated teacher soon.{/i}"
        WTT "{i}She might be in line for some kind of promotion soon.{/i}"
        WTT "{i}Maybe she can help me identify other great teachers in the district who can help our school progress out of the tired old ways of the past.{/i}"
        scene bg HPCosplay114
        with fade
        $ renpy.pause ()
        scene bg SleepBlack
        with fade
        jump myroom

label fapmandy:
    play music SexMusic
    scene JackOffVideo05
    with fade
    $ renpy.pause ()
    scene bg BlurryWhite
    with fade
    scene JOffMandyVideo01
    with fade
    $ renpy.pause ()
    scene bg BlurryWhite
    with fade
    play sound Ejaculate
    scene bg JackOffMandy05
    with fade
    with vpunch
    with hpunch
    $ renpy.pause ()
    scene bg JackOffMandy06
    with dissolve
    RT "{i}What is wrong with me?{/i}"
    $ timeofdaycounter += 1
    play music Honey
    jump myroom

label sidney_bed_sex:
    scene bg MyRoomNightWSidney
    with fade
    menu:
        "Mess around.":
            if sidneylibido >= 8:
                scene bg SleepWithSidney12
                with fade
                R "Psssssst... {i}(whispering){/i} Hey, Sidney... are you awake?"
                scene bg RyanRoomOral01
                with dissolve
                S "Yeah, I just laid down about 10 minutes ago, so I haven't fallen asleep yet... everything ok?"
                scene bg RyanRoomOral02
                with dissolve
                R "Yeah... I was just wondering if you wanted to..."
                scene bg RyanRoomOral01
                with dissolve
                S "Mess around?"
                R "Yeah... exactly."
                S "Well... what exactly are you thinking we should do?"
                menu:
                    "Sixty nine.":
                        R "Oh... nothing too crazy. But I do think we'd both benefit from some oral action."
                        S "Ok... I'm in, let's get this sixty-nine thing going."
                        play music SexMusic
                        scene bg SleepBlack
                        with fade
                        S "So, should I be on the bottom or top?"
                        S "Ouch! You kneeled on my hand..."
                        R "Sorry, I just can't see very well in the dark."
                        R "Ok, now just open really wide."
                        scene bg RyanRoomOral03
                        with fade
                        R "Oh, my God!... I'm still amazed you can get your mouth around that!"
                        S "Hrmph... gurrrccchh..."
                        R "Haha... never mind!"
                        play sound Blow03 loop
                        scene bg RyanRoomOral04
                        scene bg RyanRoomOral04
                        with fade
                        S "Mmmmpphhh..."
                        scene bg RyanRoomOral05 with Dissolve(0.3)
                        $ renpy.pause (0.2)
                        scene bg RyanRoomOral06 with Dissolve(0.3)
                        $ renpy.pause (0.2)
                        scene bg RyanRoomOral05 with Dissolve(0.3)
                        $ renpy.pause (0.02)
                        scene bg RyanRoomOral06 with Dissolve(0.3)
                        $ renpy.pause (0.2)
                        scene bg RyanRoomOral05 with Dissolve(0.3)
                        $ renpy.pause (0.02)
                        scene bg RyanRoomOral06 with Dissolve(0.3)
                        $ renpy.pause (0.2)
                        scene bg SleepBlack
                        with fade
                        scene bg RyanRoomOral13
                        with fade
                        RT "{i}Oh, my God!... I'll never get sick of the taste of this pussy.{/i}"
                        scene bg SleepBlack
                        with fade
                        scene bg RyanRoomOral07 with Dissolve(0.3)
                        $ renpy.pause (0.2)
                        scene bg RyanRoomOral08 with Dissolve(0.3)
                        $ renpy.pause (0.2)
                        scene bg RyanRoomOral07 with Dissolve(0.3)
                        $ renpy.pause (0.02)
                        scene bg RyanRoomOral08 with Dissolve(0.3)
                        $ renpy.pause (0.2)
                        ST "{i}Oh, my God!... I can't believe we're just doing this without any kind of pretense anymore.{/i}"
                        scene bg RyanRoomOral07 with Dissolve(0.3)
                        $ renpy.pause (0.02)
                        scene bg RyanRoomOral08 with Dissolve(0.3)
                        $ renpy.pause (0.2)
                        scene bg RyanRoomOral07 with Dissolve(0.3)
                        $ renpy.pause (0.02)
                        scene bg RyanRoomOral08 with Dissolve(0.3)
                        $ renpy.pause (0.2)
                        ST "{i}Ahhhh, [ryan]!... That tongue!{/i}"
                        scene bg RyanRoomOral09 with Dissolve(0.3)
                        $ renpy.pause (0.2)
                        scene bg RyanRoomOral10 with Dissolve(0.3)
                        $ renpy.pause (0.2)
                        scene bg RyanRoomOral09 with Dissolve(0.3)
                        $ renpy.pause (0.02)
                        scene bg RyanRoomOral10 with Dissolve(0.3)
                        $ renpy.pause (0.2)
                        ST "{i}[ryan]'s cock is destroying my throat!... Ah... ah... ah... [ryan]!{/i}"
                        scene bg RyanRoomOral09 with Dissolve(0.3)
                        $ renpy.pause (0.2)
                        scene bg RyanRoomOral10 with Dissolve(0.3)
                        $ renpy.pause (0.2)
                        scene bg RyanRoomOral09 with Dissolve(0.3)
                        $ renpy.pause (0.02)
                        scene bg RyanRoomOral10 with Dissolve(0.3)
                        $ renpy.pause (0.2)
                        ST "{i}I'M CUMMING!!!!!!!!!!!!!!!!!{/i}"
                        scene bg RyanRoomOral13
                        with fade
                        RT "{i}Holy hell, I love when she shakes like this!{/i}"
                        scene bg BlurryWhite
                        with fade
                        with vpunch
                        with hpunch
                        stop sound
                        scene bg RyanRoomOral14
                        with fade
                        RT "{i}Oh, my God!... She just squirted like crazy! That's so hot!!... I better pull out fast, I'm going to lose it!!!{/i}"
                        scene bg BlurryWhite
                        with fade
                        with vpunch
                        with hpunch
                        play sound Ejaculate
                        scene bg RyanRoomOral11
                        with fade
                        $ renpy.pause ()
                        play sound Ejaculate
                        scene bg RyanRoomOral12
                        with dissolve
                        $ renpy.pause ()
                        scene bg SleepBlack
                        with fade
                        $ renpy.pause ()
                        scene bg RyanRoomOral16
                        with fade
                        R "So, how was that?"
                        scene bg RyanRoomOral15
                        with dissolve
                        S "You did good... and you keep getting better!"
                        S "What did you think of my performance?"
                        R "Wow!... That thing you were doing with your tongue."
                        S "You noticed!..."
                        scene bg RyanRoomOral16
                        with dissolve
                        R "How could I not?"
                        R "I can't wait until the next time we do it!"
                        S "[ryan]?"
                        R "Yeah?..."
                        scene bg RyanRoomOral15
                        S "Do you think what we're doing is wrong?"
                        R "Oh, fuck yeah!... That's why it's so fun!"
                        S "I know... right?"
                        S "Well..."
                        S "Goodnight, [ryan]!"
                        R "Goodnight, Sidney."
                        "{i}\"Sidney Libido -5\"{/i}"
                        $ sidneylibido -= 5
                        play music Honey
                        $ sixty_nined_last_night = True
                        $ sixty_nined_bfast = 1
                        jump sleep
                    "Have sex!":
                        R "Ohh... just my favorite activity in the whole world."
                        S "Alright... I'll go get the strap-on dildo... are you sure your ass is up for it tonight?"
                        scene bg RyanRoomOral02
                        with dissolve
                        R "{i}(sarcastically){/i} Oh, ha... ha..."
                        R "When did you become such a comedian?"
                        R "You know what I meant."
                        scene bg RyanRoomOral01
                        with dissolve
                        S "Of course I do, dipshit..."
                        S "And even though I know we shouldn't... I was still hoping you'd ask."
                        scene bg SleepBlack
                        with fade
                        scene bg BRSex01
                        with dissolve
                        play music SexMusic
                        S "I don't know if I'll ever be satisfied with a smaller dick than yours again."
                        S "The way it just fills me... and hits every spot!"
                        S "I can't believe I can even take it at all."
                        R "Speaking of taking it all..."
                        S "Yeah?"
                        menu:
                            "Ask for anal sex.":
                                R "How would you feel about trying some butt stuff?"
                                scene bg BRSex02
                                with dissolve
                                S "Really, [ryan]?"
                                S "We're fucking brother and sister!... We shouldn't even be fucking at all!"
                                S "And still you're not satisfied?"
                                S "You've got to try and push this to the limits of depravity?"
                                S "Why don't you try shoving something as big as your dick up your own ass!"
                                S "When you can take it all, then we can maybe talk about it."
                                S "But for now... I'm just not in the mood anymore..."
                                "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
                                $ sidneylibido -= 5
                                scene bg SleepBlack
                                with fade
                                RT "{i}Well, shit! That didn't go over very well... but she's right... I'm not satisfied!{/i}"
                                RT "{i}I need to fuck that sexy ass!{/i}"
                                WT "Sorry, [ryan]... Not in this update.  But hopefully soon!"
                                RT "{i}Damnit!{/i}"
                                jump sleep
                            "Never mind, I better not":
                                R "Never mind... forget about it."
                                S "What?"
                                R "No... it's nothing."
                                S "Ok..."
                                R "Let's just have some fun."
                                scene bg SleepBlack
                                with fade
                                S "So, should I be on the bottom or top?"
                                S "Ouch! You kneeled on my hand..."
                                R "Sorry, I just can't see very well in the dark."
                                R "No... just... straddle me."
                                S "Oh, yeah!... Right there!"
                                scene BRSexVideo01
                                with fade
                                play sound Sidney01 loop
                                $ renpy.pause ()
                                S "Fuck, [ryan]! I have to get used to the size of that cock every time!"
                                R "Sorry!... I can't make it smaller."
                                S "No... it's great!... It just never fails to surprise me."
                                S "In fact... it's starting to feel... really goOOOOooodd!"
                                scene BRSexVideo02
                                with fade
                                $ renpy.pause ()
                                R "Oh fuck, Sidney!"
                                R "Your pussy feels so good!"
                                R "I love your mouth too... but this is just... wow!"
                                scene BRSexVideo01
                                with fade
                                $ renpy.pause ()
                                S "Aaahhh... [ryan]!... I think I'm going to..."
                                stop sound
                                play sound Ejaculate
                                scene bg BRSex07
                                with fade
                                $ renpy.pause ()
                                play sound Sidney01
                                S "Fuuuuuuuck!..."
                                R "Holy shit, Sidney! You're soaking the bed!"
                                S "I... can't... fuuuuck!"
                                S "Ahhhh! Give me that cock!"
                                scene BRSexVideo01
                                with fade
                                $ renpy.pause ()
                                R "Wow!... Sidney, that was amazing!..."
                                R "But don't forget Mom and Lauren are just across the hall."
                                RT "{i}Luckily they're sleeping pretty deeply, thanks to the tea.{/i}"
                                RT "{i}Sidney's obviously stopped drinking it.{/i}"
                                if progress >= 15:
                                    RT "{i}And Mandy doesn't drink it, but I'm not sure about Aunt Cami.{/i}"
                                else:
                                    pass
                                scene BRSexVideo02
                                with fade
                                $ renpy.pause ()
                                R "Ohhh... yeah... Sidney, that's starting to feel really good!"
                                R "Oohhhh... I'm really close!"
                                menu:
                                    "Cum inside.":
                                        R "Sidney... I'm going to..."
                                        scene bg BRSexVideo02F01
                                        with dissolve
                                        stop sound
                                        $ renpy.pause ()
                                        play sound Ejaculate
                                        scene bg BRSex03
                                        with fade
                                        with hpunch
                                        S "Oh, God! You're fucking filling my womb!"
                                        "{i}\"[ryan]'s cumloads in Sidney's pussy +1\"{/i}"
                                        $ sidney_cum_loads_counter += 1
                                        "{i}\"Total loads of [ryan]'s cum in Sidney's pussy = ([sidney_cum_loads_counter])\"{/i}"
                                        scene bg SleepBlack
                                        with fade
                                        $ renpy.pause ()
                                        jump sidney_bed_sex_end
                                    "Cum on her ass and back.":
                                        stop sound
                                        play sound Ejaculate
                                        scene bg BRSex04
                                        with fade
                                        with hpunch
                                        R "Fuuuuck!..."
                                        play sound Ejaculate
                                        scene bg BRSex05
                                        with dissolve
                                        with vpunch
                                        R "I'm cuuummmiing!"
                                        scene bg BRSex06
                                        with dissolve
                                        S "Oh my God, [ryan]!"
                                        S "You covered me!"
                                        scene bg SleepBlack
                                        with fade
                                        $ renpy.pause ()
                                        jump sidney_bed_sex_end
            else:
                scene bg SleepWithSidney12
                with fade
                R "Psssssst... {i}(whispering){/i} Hey, Sidney... are you awake?"
                scene bg RyanRoomOral01
                with dissolve
                S "Yeah, I just laid down about 10 minutes ago, so I haven't fallen asleep yet... everything ok?"
                scene bg RyanRoomOral02
                with dissolve
                R "Yeah... I was just wondering if you needed to... you know..."
                scene bg RyanRoomOral17
                with dissolve
                S "No..."
                R "What!?... why?"
                S "[ryan]! Do you even care that we're fucking brother and sister?"
                R "Sometimes..."
                R "Then I start thinking about how wrong the things we're doing are, and how naughty we are to give in to our sexual urges so easily..."
                R "That's when the guilt and shame start making it seem more forbidden... and the more forbidden it is... the more I want it."
                S "That's just stupid!"
                ST "{i}Stupid [ryan]!... Only thinking with his stupid cock!... His big... fat... veiny... cock.{/i}"
                scene bg RyanRoomOral02
                with dissolve
                "{i}{b}\"Sidney's Libido +3\"{/b}{/i}"
                $ sidneylibido += 3
                S "Maybe another night."
                "{i}\"Sidney's Libido needs to be at least 8 points at the beginning of their conversation to want to mess around.\"{/i}"
                S "Good night, [ryan]."
                R "Good night, Sidney."
                $ sixty_nined_last_night = False
                jump sleep
        "Go to sleep.":
            $ sixty_nined_last_night = False
            jump sleep
        "Never mind.":
            jump myroom

label sidney_bed_sex_end:
    scene bg BRSex09
    with fade
    R "So, how was that?"
    scene bg BRSex08
    with dissolve
    S "You did good... and you keep getting better!"
    S "What did you think of my performance?"
    R "Wow!... The way your pussy would just squeeze my cock!"
    S "You noticed!... I've been working on my kegel muscles."
    R "Your what muscles?"
    S "You know... my pussy muscles."
    R "Ohh... yeah... I could totally tell!"
    scene bg BRSex09
    with dissolve
    R "I can't wait until the next time we do it!"
    S "[ryan]?"
    R "Yeah?..."
    scene bg BRSex08
    with dissolve
    S "Do you think what we're doing is wrong?"
    R "Oh, fuck yeah!... That's why it's so fun!"
    S "I know... right?"
    S "Well..."
    S "Goodnight, [ryan]!"
    R "Goodnight, Sidney."
    "{i}\"Sidney Libido -5\"{/i}"
    $ persistent.gal_Sidney_10 = True
    $ sidneylibido -= 5
    play music Honey
    $ sixty_nined_last_night = False
    $ had_br_sex = True
    jump sleep

label ph_reading_time:
    scene bg RyansRoom01
    with fade
    if read_book2 and inventory.has_item(ph_book3):
        RT "{i}I'm actually pretty excited to read the next Perry Hotter book... I don't even mind if it takes me the rest of the night.{/i}"
        RT "{i}I can't ever admit that to Mom, though. Should I take the time to read right now?{/i}"
        menu:
            "Yes":
                scene bg SleepBlack
                with fade
                scene bg PHRead03
                with fade
                RT "{i}Perry Hotter and the prisoner of Moldevort's Dungeon.{/i}"
                RT "{i}The books seem to progress in age content with the reader, but this one looks like it's going to be more like \"37 Shades of Grey\".{/i}"
                RT "{i}I can't wait to get into it!{/i}"
                scene bg PHRead04
                with fade
                RT "{i}([ryan] reading in head) Perry Hotter was a highly unusual boy in many ways...{/i}"
                scene bg SleepBlack
                with fade
                "{i}\"Some time later.\"{/i}"
                scene bg PHRead04
                with fade
                RT "{i}([ryan] still reading in head) Perry stepped out of the way. Thin cords shot from Lewdin’s wand this time, and next moment, Peckergrew was wriggling on the floor, bound and gagged...{/i}"
                scene bg PHRead05
                with dissolve
                M "Oh, hey. Just passing by from the shower to my room, and I thought you might be reading again!"
                R "Hey, Mom. Come on in."
                scene bg PHRead06
                with fade
                M "Holy cow! I can't believe you're on the third book already!"
                M "I told you those books are really addictive!"
                R "I'm not addicted!... I just want to get through them so we can finish the photoshoot."
                M "Ok... sure..."
                R "What?... You don't believe me?"
                M "...."
                R "Fine, I don't care."
                M "How far into it are you?"
                R "Well... Perry and Hermione are watching Sirius Wack and Lewdin confront Peckergrew for the second time."
                M "Oh... so they've already gone back in time?"
                R "Yeah... but some of this doesn't make any sense."
                scene bg PHRead07
                with dissolve
                M "Oh?... Like what?"
                R "Like why don't they just use the time turner to go kill baby Moldevort?"
                M "You can't kill a baby! Plus, you can't travel that far back in time with it."
                R "Well then, why didn't Duffledore use it in the past to stop Moldevort from killing Perry's parents?"
                scene bg PHRead06
                with dissolve
                M "Because he knew the only person who could stop Moldevort was Perry, plus he didn't have one at the time since the Ministry keeps them locked up."
                M "Besides they need to use the time turner to save Blackbeak!"
                R "That stupid bird?"
                M "He's not stupid!... He and Hermione have a very special relationship!"
                R "What!?"
                scene bg PHRead07
                with dissolve
                M "Whoops!... Sorry! I didn't mean to spoil it!"
                R "Please don't tell me they get romantically involved!"
                M "Welllll..."
                R "Fuck!"
                M "Language, [ryan]! Plus, it's just a short fling, Hermione moves on in the next book."
                R "Uuurrgghh... Here's why I have a problem with that!..."
                MT "{i}Wow!... He's pretty upset over this Blackbeak/\Hermione relationship.{/i}"
                R "...It's just bullshit and poor writing when an interspecies relationship has to bring together the whole plot at the..."
                M "[ryan]... [ryan]!"
                R "...when there are so many better things they could have used that time turner for, and..."
                M "[ryan]!"
                MT "{i}He won't shut up!... How do I get him to calm down?{/i}"
                MT "{i}I mean... I guess I could distract him.{/i}"
                MT "{i}Haha... I know exactly how to shut him up!{/i}"
                R "and furthermore, that stupid Dungeon of Moldevort's was hardly even mentioned in the..."
                scene bg PHRead15
                with dissolve
                M "[ryan]! Calm down, it's just a book!"
                scene bg PHRead20
                with dissolve
                R "And not to menti..."
                MT "{i}Perfect, exactly like I planned... now to act shocked!{/i}"
                scene bg PHRead16
                with dissolve
                MT "{i}Wait! I just exposed my entire body to my son on purpose!{/i}"
                MT "{i}What the fuck is wrong with me?{/i}"
                scene bg PHRead17
                with dissolve
                RT "{i}Oh... my... God!{/i}"
                scene bg PHRead18
                with dissolve
                M "I'm so sorry!... I forgot I was wearing a towel for a second."
                MT "{i}I'm going to hell!{/i}"
                R "Uhhh... no... it's ok... I mean, I've seen it before..."
                R "At least the top half."
                M "Oh, God!"
                scene bg PHRead19
                with dissolve
                RT "{i}Wow!... That was amazing!{/i}"
                RT "{i}But I kind of feel bad seeing her so embarrassed.{/i}"
                RT "{i}It was kind of cute at the same time though...{/i}"
                RT "{i}Haha... that's a memory I'll enjoy forever!{/i}"
                RT "{i}Plus, I'm sure she's fine...{/i}"
                RT "..."
                RT "{i}Back to my book I guess.{/i}"
                scene bg SleepBlack
                with fade
                "{i}\Much later\"{/i}"
                scene bg PHRead04
                with fade
                RT "{i}(reading in head) Grinning broadly at the look of horror on Uncle’s face, Perry set off toward the station exit, Headswig rattling along in front of him, for what looked like a much better summer than the last.  THE END!{/i}"
                RT "{i}Yes! I finished! Now I can get Mom to do a photoshoot!{/i}"
                RT "{i}Oh... look... there's a preview for the first chapters of the next book...{/i}"
                RT "{i}I'll just take a little look... if... I can... stay... awake...{/i}"
                scene bg SleepBlack
                with fade
                $ persistent.gal_mom_9 = True
                $ read_book3 = True
                $ renpy.pause ()
                $ timeofdaycounter = 5
                jump sleep
            "No":
                $ screen_on = "ryanmap"
                call screen ryanmap
    if read_book2 and third_book_owned:
        RT "{i}I'm actually pretty excited to read the next Perry Hotter book... I don't even mind if it takes me the rest of the night.{/i}"
        RT "{i}I can't ever admit that to [mom_name], though. Should I take the time to read right now?{/i}"
        menu:
            "Yes":
                scene bg SleepBlack
                with fade
                scene bg PHRead03
                with fade
                RT "{i}Perry Hotter and the prisoner of Moldevort's Dungeon.{/i}"
                RT "{i}The books seem to progress in age content with the reader, but this one looks like it's going to be more like \"37 Shades of Grey\".{/i}"
                RT "{i}I can't wait to get into it!{/i}"
                scene bg PHRead04
                with fade
                RT "{i}([ryan] reading in head) Perry Hotter was a highly unusual boy in many ways...{/i}"
                scene bg SleepBlack
                with fade
                "{i}\"Some time later.\"{/i}"
                scene bg PHRead04
                with fade
                RT "{i}([ryan] still reading in head) Perry stepped out of the way. Thin cords shot from Lewdin’s wand this time, and next moment, Peckergrew was wriggling on the floor, bound and gagged...{/i}"
                scene bg PHRead05
                with dissolve
                M "Oh, hey. Just passing by from the shower to my room, and I thought you might be reading again!"
                R "Hey, Mom. Come on in."
                scene bg PHRead06
                with fade
                M "Holy cow! I can't believe you're on the third book already!"
                M "I told you those books are really addictive!"
                R "I'm not addicted!... I just want to get through them so we can finish the photoshoot."
                M "Ok... sure..."
                R "What?... You don't believe me?"
                M "...."
                R "Fine, I don't care."
                M "How far into it are you?"
                R "Well... Perry and Hermione are watching Sirius Wack and Lewdin confront Peckergrew for the second time."
                M "Oh... so they've already gone back in time?"
                R "Yeah... but some of this doesn't make any sense."
                scene bg PHRead07
                with dissolve
                M "Oh?... Like what?"
                R "Like why don't they just use the time turner to go kill baby Moldevort?"
                M "You can't kill a baby! Plus, you can't travel that far back in time with it."
                R "Well then, why didn't Duffledore use it in the past to stop Moldevort from killing Perry's parents?"
                scene bg PHRead06
                with dissolve
                M "Because he knew the only person who could stop Moldevort was Perry, plus he didn't have one at the time since the Ministry keeps them locked up."
                M "Besides they need to use the time turner to save Blackbeak!"
                R "That stupid bird?"
                M "He's not stupid!... He and Hermione have a very special relationship!"
                R "What!?"
                scene bg PHRead07
                with dissolve
                M "Whoops!... Sorry! I didn't mean to spoil it!"
                R "Please don't tell me they get romantically involved!"
                M "Welllll..."
                R "Fuck!"
                M "Language, [ryan]! Plus, it's just a short fling, Hermione moves on in the next book."
                R "Uuurrgghh... Here's why I have a problem with that!..."
                MT "{i}Wow!... He's pretty upset over this Blackbeak/\Hermione relationship.{/i}"
                R "...It's just bullshit and poor writing when an interspecies relationship has to bring together the whole plot at the..."
                M "[ryan]... [ryan]!"
                R "...when there are so many better things they could have used that time turner for, and..."
                M "[ryan]!"
                MT "{i}He won't shut up!... How do I get him to calm down?{/i}"
                MT "{i}I mean... I guess I could distract him.{/i}"
                MT "{i}Haha... I know exactly how to shut him up!{/i}"
                R "and furthermore, that stupid Dungeon of Moldevort's was hardly even mentioned in the..."
                scene bg PHRead15
                with dissolve
                M "[ryan]! Calm down, it's just a book!"
                scene bg PHRead20
                with dissolve
                R "And not to menti..."
                MT "{i}Perfect, exactly like I planned... now to act shocked!{/i}"
                scene bg PHRead16
                with dissolve
                MT "{i}Wait! I just exposed my entire body to my son on purpose!{/i}"
                MT "{i}What the fuck is wrong with me?{/i}"
                scene bg PHRead17
                with dissolve
                RT "{i}Oh... my... God!{/i}"
                scene bg PHRead18
                with dissolve
                M "I'm so sorry!... I forgot I was wearing a towel for a second."
                MT "{i}I'm going to hell!{/i}"
                R "Uhhh... no... it's ok... I mean, I've seen it before..."
                R "At least the top half."
                M "Oh, God!"
                scene bg PHRead19
                with dissolve
                RT "{i}Wow!... That was amazing!{/i}"
                RT "{i}But I kind of feel bad seeing her so embarrassed.{/i}"
                RT "{i}It was kind of cute at the same time though...{/i}"
                RT "{i}Haha... that's a memory I'll enjoy forever!{/i}"
                RT "{i}Plus, I'm sure she's fine...{/i}"
                RT "..."
                RT "{i}Back to my book I guess.{/i}"
                scene bg SleepBlack
                with fade
                "{i}\Much later\"{/i}"
                scene bg PHRead04
                with fade
                RT "{i}(reading in head) Grinning broadly at the look of horror on Uncle’s face, Perry set off toward the station exit, Headswig rattling along in front of him, for what looked like a much better summer than the last.  THE END!{/i}"
                RT "{i}Yes! I finished! Now I can get Mom to do a photoshoot!{/i}"
                RT "{i}Oh... look... there's a preview for the first chapters of the next book...{/i}"
                RT "{i}I'll just take a little look... if... I can... stay... awake...{/i}"
                scene bg SleepBlack
                with fade
                $ persistent.gal_mom_9 = True
                $ read_book3 = True
                $ renpy.pause ()
                $ timeofdaycounter = 5
                jump sleep
            "No":
                $ screen_on = "ryanmap"
                call screen ryanmap
    if read_book2 and not inventory.has_item(ph_book3):
        RT "{i}Now would be a great time to read the next Perry Hotter book... too bad I haven't bought the third one yet.{/i}"
        $ screen_on = "ryanmap"
        call screen ryanmap
    if read_book2 and not third_book_owned:
        RT "{i}Now would be a great time to read the next Perry Hotter book... too bad I haven't bought the third one yet.{/i}"
        $ screen_on = "ryanmap"
        call screen ryanmap
    if inventory.has_item(ph_book2) and not read_book2:
        RT "{i}I've got to admit, the first Perry Hotter book was alright... too bad it took the whole rest of the day to finish... should I read the second book now?{/i}"
        menu:
            "Yes":
                scene bg SleepBlack
                with fade
                scene bg PHRead02
                with fade
                RT "{i}Perry Hotter and her Chambers of Secrets.{/i}"
                RT "{i}Who is \"her?\"{/i}"
                RT "{i}And could her \"Chambers of Secrets\" be what I think they are?{/i}"
                RT "{i}I can't wait to read and find out!{/i}"
                scene bg PHRead04
                with fade
                RT "{i}([ryan] reading in head) Not for the first time, an argument had broken out over breakfast at number five, Pecker Drive...{/i}"
                scene bg SleepBlack
                with fade
                "{i}\"Some time later.\"{/i}"
                scene bg PHRead04
                with fade
                RT "{i}([ryan] still reading in head) \"What have we found out, I’d like to know?\"\"That Hargrid never entered her Chambers of Secrets,\" said Perry, throwing the cloak over Rod and prodding him in the arm to make him walk. \"She's still innocent.\"{/i}"
                scene bg PHRead05
                with dissolve
                M "Oh, hey. Just passing by from the shower to my room, and I thought you might be reading again!"
                R "Hey, Mom. Come on in."
                scene bg PHRead06
                with fade
                M "You are such a fast reader."
                M "I can't believe you are already on the second book."
                R "Yeah, speed reading comes pretty easy to me."
                R "Especially when I'm motivated."
                MT "{i}Does he mean what I think he means?{/i}"
                M "So how far into the book are you?"
                R "They just found out that Hargrid didn't enter that underaged wizard's chambers of secrets after being chased by those giant spiders."
                M "That's such an exciting part!"
                R "Yeah well, there's one thing about this book that's been bothering me?"
                R "So these are considered children's books right?"
                M "Of course..."
                R "Well aren't the so called \"Chambers of Secrets\" Just a metaphor for a girl's... you know..."
                scene bg PHRead07
                with dissolve
                M "Of course not! At least I don't think so. They are a physical location in the book."
                R "Are you sure?"
                M "Of course I'm sure, you just haven't reached that part yet."
                M "Though if you pay attention, you will understand that the purpose of the Chambers of Secrets are to help a wizard awaken their sexuality in their teen years."
                R "And you don't think it's a metaphor for a girl's vagina and asshole?"
                M "No..."
                R "Well, the reason I think it might be..."
                MT "{i}Does [ryan] ever think of anything besides sex?{/i}"
                MT "{i}I wonder how much he's been thinking about the last time I visited him in his room and flashed him my nipple.{/i}"
                MT "{i}He still seems pretty comfortable around me.{/i}"
                MT "{i}Maybe I need to test him again.{/i}"
                MT "{i}I mean... I need to know how bad his Oedipal complex is... right?{/i}"
                R "And, if you really pay attention to what Duffledore says when Perry gets a glimpse into his past..."
                scene bg PHRead12
                with dissolve
                R "...."
                RT "{i}Holy shit! Both her boobs fell out of her towel this time!{/i}"
                RT "{i}Fuck! I just lost my train of thought!{/i}"
                RT "{i}Does she really not notice?{/i}"
                RT "{i}What do I do?{/i}"
                menu:
                    "Stare at those breasts!":
                        scene bg PHRead13
                        with fade
                        MT "{i}Filthy pervert! He can't look away...{/i}"
                        MT "{i}Looks like we've still got some major work to do!{/i}"
                        "{i}{b}\"Mom's Respect -1\"{/b}{/i}"
                        $ momrespect -= 1
                        MT "{i}Look at him!... He's practically drooling?{/i}"
                        scene bg PHRead14
                        with fade
                        MT "{i}Still... I haven't had anyone stare at my breasts like that for a long time!{/i}"
                        "{i}{b}\"Mom's Libido +2\"{/b}{/i}"
                        $ momlibido += 2
                        scene bg PHRead12
                        with dissolve
                        MT "{i}Fuck! What is wrong with me... I've got to get the hell out of here!{/i}"
                        M "Uhhh... I've got to run... I think... I heard Sidney calling for me."
                        scene bg PHRead19
                        with dissolve
                        RT "{i}Whoa... that got weird fast!...{/i}"
                        RT "{i}Does she keep flashing me on purpose?{/i}"
                        RT "{i}No way!... She probably just noticed her breasts were hanging out... and got super embarrassed.{/i}"
                    "Let her know her breasts are showing.":
                        R "Oh! Hey, Mom?"
                        R "Just to let you know... uhhmmm... your towel slipped down and now your breasts are hanging out."
                        scene bg PHRead18
                        with dissolve
                        M "Oh, my God! I'm so sorry that happened!... I'm so embarrassed!"
                        MT "{i}Maybe his complex is getting better off after all.{/i}"
                        MT "{i}Good for him!{/i}"
                        "{i}{b}\"Mom's Respect +1\"{/b}{/i}"
                        $ momrespect += 1
                        M "I'm just going to leave, so you can get back to your book."
                        scene bg PHRead19
                        with dissolve
                        RT "{i}Whoa... that got weird fast!...{/i}"
                        RT "{i}Did she flash me on purpose?{/i}"
                        RT "{i}No way!... She just got super embarrassed.{/i}"
                RT "..."
                RT "{i}Back to my book, I guess.{/i}"
                scene bg SleepBlack
                with fade
                "{i}\Much later\"{/i}"
                scene bg PHRead04
                with fade
                RT "{i}(reading in head) And together they walked back through the gateway to the Muddle world... THE END!{/i}"
                RT "{i}Yes! I finished! Now I can get Mom to do a photoshoot!{/i}"
                RT "{i}Oh... Look... There's a preview for the first chapters of the next book...{/i}"
                RT "{i}I'll just take a little look... if... I can... stay... awake...{/i}"
                scene bg SleepBlack
                with fade
                $ read_book2 = True
                $ renpy.pause ()
                $ timeofdaycounter = 5
                jump sleep
            "NO":
                $ screen_on = "ryanmap"
                call screen ryanmap
    if second_book_owned and not read_book2:
        RT "{i}I've got to admit, the first Perry Hotter book was alright... too bad it took the whole rest of the day to finish... should I read the second book now?{/i}"
        menu:
            "Yes":
                scene bg SleepBlack
                with fade
                scene bg PHRead02
                with fade
                RT "{i}Perry Hotter and her Chambers of Secrets.{/i}"
                RT "{i}Who is \"her?\"{/i}"
                RT "{i}And could her \"Chambers of Secrets\" be what I think they are?{/i}"
                RT "{i}I can't wait to read and find out!{/i}"
                scene bg PHRead04
                with fade
                RT "{i}([ryan] reading in head) Not for the first time, an argument had broken out over breakfast at number five, Pecker Drive...{/i}"
                scene bg SleepBlack
                with fade
                "{i}\"Some time later.\"{/i}"
                scene bg PHRead04
                with fade
                RT "{i}([ryan] still reading in head) \"What have we found out, I’d like to know?\"\"That Hargrid never entered her Chambers of Secrets,\" said Perry, throwing the cloak over Rod and prodding him in the arm to make him walk. \"She's still innocent.\"{/i}"
                scene bg PHRead05
                with dissolve
                M "Oh, hey. Just passing by from the shower to my room, and I thought you might be reading again!"
                R "Hey, Mom. Come on in."
                scene bg PHRead06
                with fade
                M "You are such a fast reader."
                M "I can't believe you are already on the second book."
                R "Yeah, speed reading comes pretty easy to me."
                R "Especially when I'm motivated."
                MT "{i}Does he mean what I think he means?{/i}"
                M "So how far into the book are you?"
                R "They just found out that Hargrid didn't enter that underaged wizard's chambers of secrets after being chased by those giant spiders."
                M "That's such an exciting part!"
                R "Yeah well, there's one thing about this book that's been bothering me?"
                R "So these are considered children's books right?"
                M "Of course..."
                R "Well aren't the so called \"Chambers of Secrets\" Just a metaphor for a girl's... you know..."
                scene bg PHRead07
                with dissolve
                M "Of course not! At least I don't think so. They are a physical location in the book."
                R "Are you sure?"
                M "Of course I'm sure, you just haven't reached that part yet."
                M "Though if you pay attention, you will understand that the purpose of the Chambers of Secrets are to help a wizard awaken their sexuality in their teen years."
                R "And you don't think it's a metaphor for a girl's vagina and asshole?"
                M "No..."
                R "Well, the reason I think it might be..."
                MT "{i}Does [ryan] ever think of anything besides sex?{/i}"
                MT "{i}I wonder how much he's been thinking about the last time I visited him in his room and flashed him my nipple.{/i}"
                MT "{i}He still seems pretty comfortable around me.{/i}"
                MT "{i}Maybe I need to test him again.{/i}"
                MT "{i}I mean... I need to know how bad his Oedipal complex is... right?{/i}"
                R "And, if you really pay attention to what Duffledore says when Perry gets a glimpse into his past..."
                scene bg PHRead12
                with dissolve
                R "...."
                RT "{i}Holy shit! Both her boobs fell out of her towel this time!{/i}"
                RT "{i}Fuck! I just lost my train of thought!{/i}"
                RT "{i}Does she really not notice?{/i}"
                RT "{i}What do I do?{/i}"
                menu:
                    "Stare at those breasts!":
                        scene bg PHRead13
                        with fade
                        MT "{i}Filthy pervert! He can't look away...{/i}"
                        MT "{i}Looks like we've still got some major work to do!{/i}"
                        "{i}{b}\"Mom's Respect -1\"{/b}{/i}"
                        $ momrespect -= 1
                        MT "{i}Look at him!... He's practically drooling?{/i}"
                        scene bg PHRead14
                        with fade
                        MT "{i}Still... I haven't had anyone stare at my breasts like that for a long time!{/i}"
                        "{i}{b}\"Mom's Libido +2\"{/b}{/i}"
                        $ momlibido += 2
                        scene bg PHRead12
                        with dissolve
                        MT "{i}Fuck! What is wrong with me... I've got to get the hell out of here!{/i}"
                        M "Uhhh... I've got to run... I think... I heard Sidney calling for me."
                        scene bg PHRead19
                        with dissolve
                        RT "{i}Whoa... that got weird fast!...{/i}"
                        RT "{i}Does she keep flashing me on purpose?{/i}"
                        RT "{i}No way!... She probably just noticed her breasts were hanging out... and got super embarrassed.{/i}"
                    "Let her know her breasts are showing.":
                        R "Oh! Hey, Mom?"
                        R "Just to let you know... uhhmmm... your towel slipped down and now your breasts are hanging out."
                        scene bg PHRead18
                        with dissolve
                        M "Oh, my God! I'm so sorry that happened!... I'm so embarrassed!"
                        MT "{i}Maybe his complex is getting better off after all.{/i}"
                        MT "{i}Good for him!{/i}"
                        "{i}{b}\"Mom's Respect +1\"{/b}{/i}"
                        $ momrespect += 1
                        M "I'm just going to leave, so you can get back to your book."
                        scene bg PHRead19
                        with dissolve
                        RT "{i}Whoa... that got weird fast!...{/i}"
                        RT "{i}Did she flash me on purpose?{/i}"
                        RT "{i}No way!... She just got super embarrassed.{/i}"
                RT "..."
                RT "{i}Back to my book, I guess.{/i}"
                scene bg SleepBlack
                with fade
                "{i}\Much later\"{/i}"
                scene bg PHRead04
                with fade
                RT "{i}(reading in head) And together they walked back through the gateway to the Muddle world... THE END!{/i}"
                RT "{i}Yes! I finished! Now I can get Mom to do a photoshoot!{/i}"
                RT "{i}Oh... Look... There's a preview for the first chapters of the next book...{/i}"
                RT "{i}I'll just take a little look... if... I can... stay... awake...{/i}"
                scene bg SleepBlack
                with fade
                $ read_book2 = True
                $ renpy.pause ()
                $ timeofdaycounter = 5
                jump sleep
            "NO":
                $ screen_on = "ryanmap"
                call screen ryanmap
    if read_book1 and not inventory.has_item(ph_book2):
        RT "{i}Now would be a great time to read the next Perry Hotter book... too bad I haven't bought the second one yet.{/i}"
        $ screen_on = "ryanmap"
        call screen ryanmap
    if read_book1 and not second_book_owned:
        RT "{i}Now would be a great time to read the next Perry Hotter book... too bad I haven't bought the second one yet.{/i}"
        $ screen_on = "ryanmap"
        call screen ryanmap
    else:
        RT "{i}Mom said she won't do a Perry Hotter photoshoot unless I read the Perry Hotter books.{/i}"
        RT "{i}Now seems as good a time as any.{/i}"
        RT "{i}Should I read the first Perry Hotter book right now?{/i}"
        menu:
            "Yes":
                scene bg SleepBlack
                with fade
                scene bg PHRead01
                with fade
                RT "{i}Perry Hotter and the Sorceror's Bone...{/i}"
                RT "{i}Uggghh...{/i}"
                RT "{i}I've avoided reading this series for as long as I could.{/i}"
                RT "{i}I always thought being a Perry Hotter nerd would keep me from getting laid.{/i}"
                RT "{i}Now, it seems like it's the best path to getting laid.{/i}"
                RT "{i}Ok... I can do this...{/i}"
                scene bg PHRead04
                with fade
                RT "{i}([ryan] reading in head) Mr. and Mrs. Bursley, of number five Pecker Drive, were proud to say they were immaculately normal, thank you very much...{/i}"
                scene bg SleepBlack
                with fade
                "{i}\"Some time later.\"{/i}"
                scene bg PHRead04
                with fade
                RT "{i}([ryan] still reading in head) It's tonight, said Perry, once he was sure Professor McGargleCum was out of earshot.{/i}"
                scene bg PHRead05
                with dissolve
                M "Oh, hey!"
                R "Oh, hi Mom."
                M "Sorry to interrupt you... I was on my way to my bedroom after my shower, and saw your light on... I was going to turn it off... but now I see you're in here."
                scene bg PHRead06
                with fade
                M "Oh, hey!... Is that Perry Hotter you're reading?"
                R "Yeah... I decided to finally bite the bullet."
                M "Don't you just love it?"
                R "It's ok... but there's one thing that's been bugging me... he's got a terrible nickname."
                scene bg PHRead07
                with dissolve
                M "Oh, really? You don't like it?"
                R "You do?... Really?... You wouldn't mind being called \"The boy with the golden snatch?\""
                R "You do know what a snatch is slang for, right?"
                M "No... the author is British, I don't think it means that in British English..."
                R "I'm pretty sure it does."
                scene bg PHRead06
                with dissolve
                M "Well... it doesn't mean that in the Perry Hotter world."
                M "In the magic world, a snatch is a beautiful spherical object that they have to chase, and when they catch it... they win their game."
                M "And since Perry caught the snatch in his mouth, they gave him that nickname."
                R "And that doesn't sound like a metaphor to you?"
                scene bg PHRead07
                with dissolve
                M "Hmmm... I don't think there's any hidden meaning there."
                MT "{i}Is there?{/i}"
                R "And all of these sexual innuendos? I think that..."
                MT "{i}I can't believe how far [ryan]'s read in that book in one night, at this pace he'll be done before he goes to sleep tonight.{/i}"
                MT "{i}Is he really that excited to get me to do his little photoshoot?{/i}"
                MT "{i}That can't be a good sign for his Oedipal complex... I'd better do a little experiment... I'll guage by his reaction just how serious his complex is.{/i}"
                R "And another thing..."
                play music SexMusic
                scene bg PHRead08
                with dissolve
                R "All the charact..."
                M "Yes?"
                RT "{i}Holy shit! Her nipple fell out of her towel!{/i}"
                RT "{i}Fuck! I just lost my train of thought!{/i}"
                RT "{i}What do I do?{/i}"
                menu:
                    "Stare at her nipple":
                        scene bg PHRead09
                        with fade
                        MT "{i}That little horndog!...{/i}"
                        MT "{i}Looks like we've still got some major work to do!{/i}"
                        "{i}{b}\"Mom's Respect -1\"{/b}{/i}"
                        $ momrespect -= 1
                        MT "{i}Look at him!... He's practically drooling?{/i}"
                        scene bg PHRead10
                        with fade
                        MT "{i}I haven't had anyone stare at my breasts like that for a long time!{/i}"
                        "{i}{b}\"Mom's Libido +2\"{/b}{/i}"
                        $ momlibido += 2
                        scene bg PHRead08
                        with dissolve
                        MT "{i}Fuck! What is wrong with me... I've got to get the hell out of here!{/i}"
                        M "Uhhh... I've got to run... I think I left the oven on."
                        scene bg PHRead19
                        with dissolve
                        RT "{i}Whoa... That got weird fast!...{/i}"
                        RT "{i}Did she flash me on purpose?{/i}"
                        RT "{i}No way!... She probably just noticed her nipple was hanging out... And got super embarrassed.{/i}"
                    "Let her know her nipple slipped.":
                        R "Oh! Hey, Mom?"
                        R "Just to let you know... uhhmmm... your nipple slipped out of your towel."
                        scene bg PHRead18
                        with dissolve
                        M "Oh my God! I'm so sorry that happened!... I'm so embarrassed!"
                        MT "{i}Maybe his complex is getting better off after all.{/i}"
                        MT "{i}Good for him!{/i}"
                        "{i}{b}\"Mom's Respect +1\"{/b}{/i}"
                        $ momrespect += 1
                        M "I'm just going to leave, so you can get back to your book."
                        scene bg PHRead19
                        with dissolve
                        RT "{i}Whoa... That got weird fast!...{/i}"
                        RT "{i}Did she flash me on purpose?{/i}"
                        RT "{i}No way!... She just got super embarrassed.{/i}"
                RT "..."
                RT "{i}Back to my book I guess.{/i}"
                scene bg SleepBlack
                with fade
                "{i}\Much later\"{/i}"
                scene bg PHRead04
                with fade
                RT "{i}(reading in head) I'm going to have a lot of fun with Pudgeley this summer... THE END!{/i}"
                RT "{i}Yes! I finished! Now I can get Mom to do a photoshoot!{/i}"
                RT "{i}Oh... look... there's a preview for the first chapters of the next book...{/i}"
                RT "{i}I'll just take a little look... if... I can... stay... awake...{/i}"
                scene bg SleepBlack
                with fade
                $ read_book1 = True
                $ renpy.pause ()
                $ timeofdaycounter = 5
                jump sleep
            "No":
                $ screen_on = "ryanmap"
                call screen ryanmap

#############  BATH  ########################################  BATH  ###########################################################

label sharing_shower:
    if spiedgirlsbathroom:
        scene bg BathroomDoor
        RT "{i}They've already showered, and will be coming out that door any second. I don't want to be creeping around when they do.{/i}"
        $ screen_on = "bathdoormap"
        call screen bathdoormap
    if spycaminbath:
        scene bg BathroomDoor
        with fade
        RT "{i}I'm excited about Mandy and Lauren sharing a shower in the morning... imagine the possibilities!{/i}"
        menu:
            "Take a peek.":
                $ shower_scene_selector = renpy.random.randint(1, 4)
                if shower_scene_selector == 1:
                    scene bg MandyLaurenBath06
                    with dissolve
                    RT "{i}Let's just see what those two are up to.{/i}"
                    scene bg MandyLaurenBath01
                    with fade
                    RT "{i}Whoops, I caught Lauren on the toilet...{/i}"
                    RT "{i}It's still a great view of her ass, but I probably should go in case something comes out of it...{/i}"
                    RT "{i}I doubt she'd do that with Mandy in there with her, but I'm not sticking around to take that chance.{/i}"
                    RT "{i}I've been surprised at how open I am to a lot of kinks, but I'll never be comfortable with that one.{/i}"
                    scene bg BathroomDoor
                    with fade
                    $ spiedgirlsbathroom = True
                    $ screen_on = "bathdoormap"
                    call screen bathdoormap
                else:
                    scene bg MandyLaurenBath07
                    with dissolve
                    RT "{i}Let's just see what those two are up to.{/i}"
                    RT "{i}Yes! I caught them in the shower together.{/i}"
                    scene bg MandyLaurenBath02
                    with fade
                    RT "{i}Haha... it looks like Mandy's sneaking peeks at Lauren when she bends over to shave her legs.{/i}"
                    RT "{i}Is... she the female version of me?{/i}"
                    scene bg MandyLaurenBath03
                    with fade
                    RT "{i}Mandy is such a tease!{/i}"
                    scene bg MandyLaurenBath04
                    with dissolve
                    RT "{i}Haha... Lauren isn't letting her get away with that.{/i}"
                    scene bg SleepBlack
                    with fade
                    scene bg MandyLaurenBath05
                    with fade
                    RT "{i}Now what are they doing?{/i}"
                    RT "{i}I'm not really sure, but I think they're comparing breast size?{/i}"
                    scene bg SleepBlack
                    RT "{i}Oh... I've stayed too long... I'd better run before I get caught.{/i}"
                    scene bg BathroomDoor
                    with fade
                    $ spiedgirlsbathroom = True
                    $ screen_on = "bathdoormap"
                    call screen bathdoormap
            "Never mind.":
                $ screen_on = "bathdoormap"
                call screen bathdoormap
    else:
        scene bg BathroomDoor
        with fade
        RT "{i}The door's locked... oh yeah, it's Mandy's and Lauren't shower time.{/i}"
        RT "{i}I'm excited about Mandy and Lauren sharing a shower in the morning... imagine the possibilities!{/i}"
        RT "{i}Damn... what a wasted opportunity... I've got to figure out a way to spy on them... maybe I can find something on the online store.{/i}"
        $ screen_on = "bathdoormap"
        call screen bathdoormap

label mandybathspycam:
    if spycaminbath:
        scene bg BathroomDoor
        with fade
        RT "{i}It sounds like Mandy is taking advantage of the weekend by getting the shower to herself.{/i}"
        menu:
            "Take a peek.":
                if spiedmandybathroom == True:
                    scene bg BathroomDoor
                    RT "{i}She's already showered, she'll be coming out that door any second. I don't want to be creeping around when she does.{/i}"
                    $ screen_on = "bathdoormap"
                    call screen bathdoormap
                else:
                    scene bg MandyShower03
                    with dissolve
                    play music SexMusic
                    $ renpy.pause ()
                    scene bg MandyShower01
                    with fade
                    RT "{i}And I think I'll zoom in a little bit.{/i}"
                    scene bg MandyShower02
                    with fade
                    RT "{i}Oh, I love those mosquito bite titties!{/i}"
                    if spycammandyshower == False:
                        RT "{i}I've got to get a picture.{/i}"
                        play sound CameraClick
                        show CamaraFlash
                        pause (0.25)
                        scene bg MandyShower02
                        $ spycammandyshower = True
                        $ renpy.pause ()
                    RT "{i}Aaauhh... I've been here too long, I'd better go before I'm caught.{/i}"
                    $ spiedmandybathroom = True
                    $ spycammandyshower = True
                    play music Honey
                    scene bg BathroomDoor
                    with fade
                    $ screen_on = "bathdoormap"
                    call screen bathdoormap
            "Never mind.":
                $ screen_on = "bathdoormap"
                call screen bathdoormap
    else:
        scene bg BathroomDoor
        with fade
        RT "{i}The door is locked... sounds like somebody is showering...{/i}"
        RT "{i}Since I can't see through doors, I have no idea who's in there.{/i}"
        RT "{i}Nothing a little spycam wouldn't solve though.{/i}"
        RT "{i}I should check the online store.{/i}"
        $ screen_on = "bathdoormap"
        call screen bathdoormap

label mandyhornybathroom:
    if spycaminbath == True:
        scene bg BathroomDoor
        with fade
        play sound Mandy01 loop
        RT "{i}I think Mandy is taking an early morning shower. Wait... did I just hear some moaning? I've got to see this!{/i}"
        menu:
            "Look.":
                jump mandyfingerselfbath
            "Never mind.":
                scene bg BathroomDoor
                "{i}{b}\"Mandy's Libido -5\"{/b}{/i}"
                $ cousinlibido -= 5
                stop sound fadeout 1.0
                $ screen_on = "bathdoormap"
                call screen bathdoormap
    else:
        scene bg BathroomDoor
        with fade
        play sound Mandy01 loop
        RT "{i}Mandy is taking an early morning shower. Wait... did I just hear some moaning? Uggh, I've got to find a way to see what's going on in there!{/i}"
        "{i}{b}\"Mandy's Libido -5\"{/b}{/i}"
        $ cousinlibido -= 5
        stop sound fadeout 1.0
        $ screen_on = "bathdoormap"
        call screen bathdoormap

label mandyfingerselfbath:
    if spiedmandybathroom == True:
        scene bg BathroomDoor
        RT "{i}She's already showered, she'll be coming out that door any second. I don't want to be creeping around when she does.{/i}"
        $ screen_on = "bathdoormap"
        call screen bathdoormap
    else:
        scene bg MandyMBateShower01
        with dissolve
        play music SexMusic
        RT "{i}Thank you technology!{/i}"
        scene bg MandyMBateShower02
        with fade
        RT "{i}Oh my God, yes! This is so awesome!{/i}"
        RT "{i}And thanks to modern technology I can watch it all.{/i}"
        scene MandyMbateShowerVideo01
        with fade
        $ renpy.pause ()
        RT "{i}I'm amazed such a small ass can fit that shampoo bottle.{/i}"
        RT "{i}Wow!{/i}"
        RT "{i}I love how unashamed Mandy is about being a sexual person.{/i}"
        RT "{i}If everyone were as open and honest as her, we'd all have a lot more fun.{/i}"
        RT "{i}I guess I'm not all that honest or open, but if I were, I'd get called a pervert and be sent to jail.{/i}"
        if spycammandymbatebath == False:
            RT "{i}I have to capture this moment. ok, just double tapping the screen while watching a livefeed should take a pic.{/i}"
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            hide CamaraFlash
            play sound Mandy01 loop
            $ renpy.pause ()
            RT "{i}Perfect! That beautiful image will be on my computer next time I check it.{/i}"
        RT "{i}Look at that tiny ass stretch!{/i}"
        RT "{i}I need to sneak a bigger shampoo bottle in the bathroom... help all the girls get ready for me.{/i}"
        stop sound
        play sound Ejaculate
        scene bg MandyMBateShower03
        with dissolve
        $ renpy.pause ()
        RT "{i}Oh damn!... What a cute little squirt!{/i}"
        RT "{i}And now I've been here too long... I'd better take off before someone sees me just staring at my phone in front of the bathroom door.{/i}"
        RT "{i}Great show, Mandy!{/i}"
        "{i}{b}\"Mandy's Libido -5\"{/b}{/i}"
        $ persistent.gal_Mandy_1 = True
        $ spiedmandybathroom = True
        $ cousinlibido -= 5
        $ timeofdaycounter += 1
        $ spycammandymbatebath = True
        play music Honey
        scene bg BathroomDoor
        with fade
        $ screen_on = "bathdoormap"
        call screen bathdoormap

label auntbathspycam:
    if spycaminbath:
        scene bg BathroomDoor
        with fade
        RT "{i}It sounds like Aunt Cami's taking her afternoon shower.{/i}"
        menu:
            "Take a peek.":
                if spiedauntbathroom == True:
                    scene bg BathroomDoor
                    RT "{i}She's already showered, she'll be coming out that door any second. I don't want to be creeping around when she does.{/i}"
                    $ screen_on = "bathdoormap"
                    call screen bathdoormap
                else:
                    scene bg AuntShower01
                    with dissolve
                    play music SexMusic
                    $ renpy.pause ()
                    scene bg AuntShower02
                    with fade
                    RT "{i}And I think I'll zoom in a little bit.{/i}"
                    scene bg AuntShower03
                    with fade
                    RT "{i}Just when I think I like smaller titties, I get a good look at those!{/i}"
                    RT "{i}I guess I just love all sizes of tits equally.{/i}"
                    if spycamauntshower == False:
                        RT "{i}I've got to get a picture.{/i}"
                        play sound CameraClick
                        show CamaraFlash
                        pause (0.25)
                        scene bg AuntShower03
                        $ spycamauntshower = True
                        $ renpy.pause ()
                    RT "{i}Aaauhh... I've been here too long, I'd better go before I'm caught.{/i}"
                    $ spiedauntbathroom = True
                    play music Honey
                    scene bg BathroomDoor
                    with fade
                    $ screen_on = "bathdoormap"
                    call screen bathdoormap
            "Never mind.":
                $ screen_on = "bathdoormap"
                call screen bathdoormap
    else:
        scene bg BathroomDoor
        with fade
        RT "{i}The door is locked... Aunt Cami must be taking her afternoon shower...{/i}"
        RT "{i}I'd love to see those huge boobies all wet and soaped up!{/i}"
        RT "{i}I should put a spycam in there or something.{/i}"
        RT "{i}I should check the online store.{/i}"
        $ screen_on = "bathdoormap"
        call screen bathdoormap

label aunthornybathroom:
    if spycaminbath == True:
        scene bg BathroomDoor
        with fade
        play sound Camille01 loop
        RT "{i}Door's locked, it looks like Aunt Cami's taking her afternoon shower.. Wait... did I just hear some moaning? I've got to see this!{/i}"
        menu:
            "Look.":
                jump auntfingerselfbath
            "Never mind.":
                scene bg BathroomDoor
                "{i}\"Aunt Camille's Libido -5\"{/i}"
                $ auntlibido -= 5
                stop sound fadeout 1.0
                $ screen_on = "bathdoormap"
                call screen bathdoormap
    else:
        scene bg BathroomDoor
        with fade
        play sound Camille01 loop
        RT "{i}Door's locked, it looks like Aunt Cami's taking her afternoon shower.. Wait... did I just hear some moaning?{/i}"
        RT "{i}Uuuurrrggghhhh... if only I had a way to see in there!{/i}"
        "{i}\"Aunt Camille's' Libido -5\"{/i}"
        $ auntlibido -= 5
        stop sound fadeout 1.0
        $ screen_on = "bathdoormap"
        call screen bathdoormap

label auntfingerselfbath:
    if spiedauntbathroom == True:
        scene bg BathroomDoor
        RT "{i}She's already showered, she'll be coming out that door any second. I don't want to be creeping around when she does.{/i}"
        $ screen_on = "bathdoormap"
        call screen bathdoormap
    else:
        scene bg AuntMbateShower01
        with dissolve
        play music SexMusic
        RT "{i}Good old trusty spycam!{/i}"
        scene bg AuntMbateShower02
        with fade
        RT "{i}I really should have tried to find spycams that record video!{/i}"
        RT "{i}Oh well, at least it takes pictures.{/i}"
        RT "{i}Time to zoom in a little closer.{/i}"
        scene AuntMbateShowerVideo01
        with fade
        $ renpy.pause ()
        RT "{i}I can't believe so many girls in my family are into anal.{/i}"
        RT "{i}I always thought girls that liked anal were just a myth... that they only exist in porn and crappy h-games.{/i}"
        RT "{i}What if my life is just a simulation... and I only exist in some pervert's porn game!...{/i}"
        RT "{i}Haha... that's ridiculous... if I were in a porn game, my dick would be twice as big.{/i}"
        RT "{i}I should really just concentrate on what's going on in front of me...{/i}"
        RT "{i}Wow!{/i}"
        if spycamauntmbatebath == False:
            RT "{i}I have to capture this moment. ok, just double tapping the screen while watching a livefeed should take a pic.{/i}"
            play sound CameraClick
            show CamaraFlash
            pause (0.25)
            hide CamaraFlash
            play sound Camille01 loop
            $ renpy.pause ()
            RT "{i}Perfect! That beautiful image will be on my computer next time I check it.{/i}"
        RT "{i}I could watch this all day!{/i}"
        stop sound
        play sound Ejaculate
        scene bg AuntMbateShower04
        with dissolve
        $ renpy.pause ()
        RT "{i}Holy fuck!... That's a huge squirt!{/i}"
        RT "{i}She's gonna have to take another shower!{/i}"
        RT "{i}I mean besides the two she just took.{/i}"
        "{i}\"Aunt Camille's Libido -5\"{/i}"
        $ persistent.gal_auntie_2 = True
        $ spiedauntbathroom = True
        $ auntlibido -= 5
        $ timeofdaycounter += 1
        $ spycamauntmbatebath = True
        play music Honey
        scene bg BathroomDoor
        with fade
        $ screen_on = "bathdoormap"
        call screen bathdoormap

#############  Kitchen  #####################################  Kitchen  ########################################################

label commission_ph_outfit:             #### Edited ####
    if talked_about_hp:
        scene bg SidneyKitchen01
        with fade
        S "Well look who's back!"
        scene bg NSidneyKitchen03
        with dissolve
        S "I'm guessing you've got some money for me?"
        menu:
            "Peek up her skirt.":
                scene bg NSidneyKitchen05
                with fade
                R "Ummm..."
                S "Haha... My eyes are up here [ryan]."
                "{i}\"Sidney Libido +1\"{/i}"
                $ sidneylibido += 1
                scene bg NSidneyKitchen03
                with fade
                $ renpy.pause ()
                scene bg NSidneyKitchen09
                with dissolve
                $ renpy.pause (0.3)
                scene bg NSidneyKitchen03
                with dissolve
            "Better Not.":
                RT "{i}Maybe I'd better not be so obvious.{/i}"
                ST "{i}Haha... I can tell he's really trying not to peek.{/i}"
                ST "{i}Good for him for showing some self-control.{/i}"
                "{i}{b}\"Sidney's Respect +1\"{/b}{/i}"
                $ sidneyrespect += 1
        S "I hope it's enough to pay the Mafia debt this week, and buy the costumes."
        menu:
            "I have enough money for both." if money >= 1800:
                R "I've been working really hard lately, and I should have enough to pay for both outfits and the weekly Mafia debt."
                "{i}{b}\"Sidney's Respect +1\"{/b}{/i}"
                $ sidneyrespect += 1
                S "Good for you, [ryan]! Keep it up and maybe we will be able to get along without Dad."
                "{i}\"Money - $1000\"{/i}"
                $ money -= 1000
            "Mom can just work it off at the club this week.":
                R "Why should I be the one responsible to pay off the debt every week, Mom can help out too."
                S "Yeah, well I guess it's your money. You earned it. If you'd rather pay me for a sexy costumes for Mom and your school girlfriend, than keeping Mom safe from the Mafia, that's up to you."
                R "Oh please, Mom's not in any danger."
                "{i}\"Money - $1000\"{/i}"
                $ money -= 1000
            "You're right, I should save up a little more money first.":
                scene bg SidneyInKitchen
                with fade
                $ screen_on = "sidneykitchenmap"
                call screen sidneykitchenmap
        R "So, how long will it take to finish?"
        S "Give me a couple days and then I'll have it ready for fitting on Mom and the other girl, what's her name?"
        R "Megan."
        S "Ok... I'll get it done."
        $ sidneymakingcosplay = True
        $ commissioned_hp_outfit = True
        R "Awesome, I can't wait!"
        scene bg NSidneyKitchen02
        with dissolve
        S "Haha, I'll bet you can't."
        R "What's that supposed to mean?"
        scene bg NSidneyKitchen03
        with dissolve
        S "Oh, I think you know."
        R "Whatever... I'll just check back in a few days to see if you're done."
        scene bg SidneyInKitchen
        with fade
        $ screen_on = "sidneykitchenmap"
        call screen sidneykitchenmap
    else:
        scene bg SidneyKitchen01
        with fade
        S "Hey [ryan], what can I do for you?"
        R "I need a couple more cosplay outfits made."
        scene bg NSidneyKitchen03
        with dissolve
        S "Two of them? Really?"
        S "Who are the two unlucky girls?"
        R "A girl from my school named Megan..."
        R "And... Mom."
        scene bg NSidneyKitchen02
        with dissolve
        S "Hahahahah... You're such a tease!"
        S "Hahahaha..."
        scene bg NSidneyKitchen03
        with dissolve
        S "...."
        scene bg NSidneyKitchen07
        with dissolve
        S "Oh, my God! You're serious!"
        scene bg NSidneyKitchen03
        with dissolve
        S "How in the hell did you pull that one off?"
        R "It wasn't really me, it was all..."
        scene bg NSidneyKitchen05
        with fade
        R "Oh my God, Sidney, you're not wearing any panties!"
        scene bg NSidneyKitchen02
        with fade
        S "Hahaha... Shhhhhh..."
        S "I don't want the whole house to hear."
        scene bg NSidneyKitchen03
        with dissolve
        S "I thought you might enjoy that!"
        S "I've just been waiting for you to come talk to me, and I knew you'd try to peek up my skirt."
        S "Make sure you get a good look."
        scene bg NSidneyKitchen05
        with fade
        $ renpy.pause ()
        R "Wow!"
        R "I can't believe you're the same sister that I grew up with."
        scene bg NSidneyKitchen03
        with fade
        S "Well... In a lot of ways I'm not."
        S "Now, you were saying something about needing some cosplay outfits?"
        S "For Mom?"
        S "I still can't believe that!"
        R "Yeah, it's a long story. I'll tell you some other time."
        RT "{i}I'll just have to censor most of the important details.{/i}"
        S "You'd better! I'm dying to know."
        S "So what kind of outfits do you need?"
        R "Have you ever seen any of the Perry Hotter movies?"
        S "Of course, several times each, thought it's been a while."
        RT "{i}Why is everyone so infatuated with that dumb story?{/i}"
        R "Well I need an outfit for a student and a teacher."
        S "Easy..."
        R "So I'm thinking a conservative costume, that turns into a sexy costume."
        S "You mean like every other outfit I've made?"
        R "Yep, just continue the good work."
        S "Alright, that will just cost you one thousand dollars."
        R "One thousand dollars?!"
        S "Yep... I told you I wouldn't do any more costumes for less than $500."
        R "I thought you were just being bitchy at the time."
        scene bg NSidneyKitchen07
        with dissolve
        S "I was... but still... you're making more money these days, and I need the money pretty badly myself."
        R "Maybe I can do something special for you tonight in the bedroom to bring that price down."
        scene bg NSidneyKitchen02
        with dissolve
        S "Hahahaha..."
        scene bg NSidneyKitchen03
        with dissolve
        S "that was a joke... right?"
        RT "{i}No... Why is that so funny?{/i}"
        R "Of course it was a joke."
        S "You're such a tease!"
        S "So do you have enough money to keep Mom from having to strip in the club this weekend, and enough for the costumes?"
        $ talked_about_hp = True
        menu:
            "I have enough money for both." if money >= 1800:
                R "I've been working really hard lately, and I should have enough to pay for both outfits and the weekly Mafia debt."
                "{i}{b}\"Sidney's Respect +1\"{/b}{/i}"
                $ sidneyrespect += 1
                S "Good for you [ryan]! Keep it up and maybe we will be able to get along without Dad."
                "{i}\"Money - $1000\"{/i}"
                $ money -= 1000
            "Mom can just work it off at the club this week.":
                R "Why should I be the one responsible to pay off the debt every week, Mom can help out too."
                S "Yeah, well I guess it's your money. You earned it. If you'd rather pay me for a sexy costumes for Mom and your school girlfriend, then keeping Mom safe from the Mafia, that's up to you."
                R "Oh please, Mom's not in any danger."
                "{i}\"Money - $1000\"{/i}"
                $ money -= 1000
            "You're right, I should save up a little more money first.":
                scene bg SidneyInKitchen
                with fade
                $ screen_on = "sidneykitchenmap"
                call screen sidneykitchenmap
        R "So, how long will it take to finish?"
        S "Give me a couple days and then I'll have it ready for fitting on Mom and the other girl, what's her name?"
        R "Megan."
        S "Ok... I'll get it done."
        $ sidneymakingcosplay = True
        $ commissioned_hp_outfit = True
        R "Awesome, I can't wait!"
        scene bg NSidneyKitchen02
        with dissolve
        S "Haha, I'll bet you can't."
        R "What's that supposed to mean?"
        scene bg NSidneyKitchen03
        with dissolve
        S "Oh, I think you know."
        R "Whatever... I'll just check back in a few days to see if you're done."
        scene bg SidneyInKitchen
        with fade
        $ screen_on = "sidneykitchenmap"
        call screen sidneykitchenmap

label ph_cosplayfitting:                #### Edited 9-1-2020 ####
    scene bg HPCosplay01
    with fade
    MG "Hey, [ryan]!"
    R "Megan! I didn't know you were here."
    M "I brought her home from school with me after Sidney texted me that the costumes were ready for fitting."
    R "Nice! I wish you'd tell me though. I don't ever want to miss a costume fitting."
    MG "Why? What don't you want to miss?"
    scene bg HPCosplay02
    with dissolve
    $ renpy.pause (1.0)
    scene bg HPCosplay01
    with dissolve
    RT "{i}Oh man, Megan is trouble... I love to get into trouble!{/i}"
    R "Oh... I just like to be part of the process."
    scene bg HPCosplay03
    with dissolve
    S "Alright, [ryan]... what do you think?"
    R "They look really authentic!"
    R "I feel like I'm looking at actual costumes from the set of the movie, but I can't wait to see the sexy versions of them."
    scene bg HPCosplay04
    with dissolve
    S "I couldn't really do a sexy version of Mom's, so I made a whole other outfit for her to change into."
    S "At no extra charge, I might add."
    R "Wow! Thank you."
    S "I'll also let you use the wands and fake broom that we picked up from Perry Hotter Land from our California vacation a couple years ago."
    R "That's a great idea!"
    R "So, can I see the sexy versions of the costumes?"
    M "You don't need to see them until the shoot."
    R "Well I kind of do, that way I know what kind of digital background I need to start putting together."
    R "What kind of poses to start planning."
    M "Uuurrgghh... I don't like this... but I get what your're saying."
    M "Let's go change, Megan."
    MG "I don't mind changing right here."
    M "No... you can change in the bathroom."
    MG "Haha... ok, we'll be right back."
    scene bg HPCosplay05
    with dissolve
    S "Oh my God, [ryan]!"
    S "Thank you for letting me be part of this."
    S "I've never seen Mom so uncomfortable, it's been hilarious!"
    S "You still haven't told me how you convinced her to do a photoshoot."
    S "And to do it with one of her students?"
    S "... you never cease to amaze me."
    R "Well, like I said, I had much less to do with it than you think..."
    S "Oop... here comes Mom. We'll talk later."
    scene bg HPCosplay06
    with dissolve
    MG "Don't you love them!?"
    MT "{i}My God! I can't believe I'm dressed like this in front of my kids.{/i}"
    MT "{i}I feel even more exposed than I did on the stage at the stripclub.{/i}"
    R "Wow!"
    R "Another win for Sidney!"
    R "If the girls in Perry Hotter had dressed like that, I would have liked the movies way more!"
    scene bg HPCosplay07
    with dissolve
    M "[ryan]! Don't forget that your mother is standing right here in front of you."
    R "Oh, I can see you very well!"
    MG "Look how good mine looks from behind!"
    scene bg HPCosplay08
    with dissolve
    S "{i}(Whispering){/i} See what I mean about Mom being so uncomfortable?"
    M "{i}(quiet voice){/i} You shouldn't be so eager to show off your body... if you want men to respect you... {i}(trailing off){/i}"
    scene bg HPCosplay09
    with dissolve
    M "Ok, [ryan]. You've seen the costumes. I think you should go now."
    R "Ok, but when can we start shooting?"
    S "I'll finish the costumes tonight, so you could probably start as early as tomorrow."
    M "I'm only available in the {b}evenings{/b} after school. And I refuse to do it on weekends."
    MG "That works for me, too."
    R "Ok, I'll get the studio ready, and then I'll give you both a call sometime on a {b}weekday{/b} in the {b}evening{/b}."
    M "Alright, now get out of here."
    $ sidneymakingcosplay = False
    $ cosplayoutfitcounter = 0
    $ timeofdaycounter += 1
    $ ready_for_hp = True
    scene bg SleepBlack
    with fade
    jump myroom

label update_six_bfasts:                #### Edited 9-1-2020 ####
    if found_bathrobe and not brobe_bfast:
        scene bg Kitchen01
        with fade
        RT "{i}It smells good in here. Should I join everybody for breakfast?{/i}"
        menu:
            "Yes":
                scene bg SleepBlack
                with fade
                MT "{i}Oh, God!... Here it goes... what will they say about me having breakfast in nothing but my underwear?{/i}"
                MT "{i}Will [ryan] be turned on by it?{/i}"
                MT "{i}I hope not... that would be unfair to him.{/i}"
                MT "{i}It's pretty tame compared to how he saw me at the club, though...{/i}"
                scene bg BFast27
                with fade
                $ renpy.pause ()
                S "Thanks, Mom... Mom!... Why are you in just your underwear?"
                L "Yeah, whoa... holy shit!"
                M "Please watch your language, Lauren!"
                R "Says the almost nude woman pretending to be Mom."
                M "{i}(sarcastically){/i} Oh, haha!"
                scene bg BFast05
                with fade
                M "It's the weirdest thing..."
                M "My bathrobe just disappeared out of thin air."
                M "It should have been in my underwear drawer."
                M "Have any of you seen it?"
                scene bg Breakfast10
                with fade
                L "No."
                S "No."
                R "No... what... bathrobe was it?"
                M "The only bathrobe I have numbskul!"
                R "It... it probably got lost in the wash like my socks always do."
                scene bg Breakfast11
                with dissolve
                S "You mean your cum socks?... Try looking under your bed."
                M "Sidney! That wasn't funny, and it was very gross!"
                MT "{i}Don't think about [ryan] masturbating!{/i}"
                scene bg Breakfast12
                with dissolve
                S "Well, Mom?... The real question is, why didn't you wear something else to breakfast?"
                M "What am I going to wear, Sidney?"
                M "My workout clothes are sweaty and gross. It would be unsanitary to cook in them."
                scene bg BFast09
                with fade
                M "I don't want to wear my school clothes to make breakfast. The bacon smoke will make me smell like bacon all day."
                M "I don't own any pajamas, since I like to sleep in my robe and underwear."
                M "I can't buy new clothes because the freaking FBI won't let me spend our money how I want..."
                M "Not to mention, our washing machine is acting up, so I'm trying to do as little laundry as possible."
                scene bg BFast08
                with dissolve
                M "[ryan]?... Is me being at breakfast like this going to be a problem? Because if it is, I'll figure out something else."
                R "No, Mom... it might be distracting if you were someone else, but you're my mother, so..."
                scene bg BFast07
                with dissolve
                M "Alright, well make sure you tell me if it becomes a problem."
                R "Ok, Mom."
                RT "{i}I should do fine as long as she doesn't start doing random boner testing.{/i}"
                S "You've got more trust in the little pervert than I do."
                scene bg BFast04
                with dissolve
                L "Lay off of [ryan]. He hasn't done anything to deserve all of your abuse this morning."
                S "Whatever."
                R "Thanks, Lauren!"
                scene bg BFast07
                with dissolve
                M "Ok, let's just pretend that everything is as it should be, act normal, and let's eat our breakfast."
                R "Yeah, ok Mom."
                RT "{i}I hope so much that Mom dressed like that \"is\" the new normal!{/i}"
                $ brobe_bfast = True
                menu:
                    "Tease Mom":
                        play music SexMusic
                        R "Would you mind pouring more maple syrup on my pancakes?"
                        M "I can pass it to you, and you can pour it yourself."
                        R "But I always pour too much, and it ruins my pancakes."
                        R "You always do it just right."
                        M "Ok... I guess I can do that."
                        if brobe_bfast:
                            scene bg BFast16
                            with dissolve
                        else:
                            scene bg Breakfast16
                            with dissolve
                        M "There... how's that?"
                        if brobe_bfast:
                            scene bg BFast17
                            with fade
                        else:
                            scene bg Breakfast17
                            with fade
                        R "They're perfect... I mean the syrup's perfect!"
                        if brobe_bfast:
                            scene bg BFast18
                            with fade
                        else:
                            scene bg Breakfast18
                            with fade
                        MT "{i}You bold cheeky bastard!... I know what that was about.{/i}"
                        MT "{i}So, why did you do it for him?{/i}"
                        if brobe_bfast:
                            scene bg BFast19
                            with dissolve
                        else:
                            scene bg Breakfast19
                            with dissolve
                        MT "{i}Shit!... I need to get laid, so I'm not always so horny around [ryan] and the girls!{/i}"
                        MT "{i}When are they going to let my fucking husband out of prison?{/i}"
                        "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                        $ momlibido += 1
                        R "Thanks, Mom!"
                        if brobe_bfast:
                            RT "{i}It almost seems like she knows I'm staring at her breasts, and just doesn't care. Is it possible she's showing them off for me on purpose?{/i}"
                        else:
                            RT "{i}Oh, she doesn't seem in any hurry to close that robe! Is it possible she's showing them off for me on purpose?{/i}"
                        if brobe_bfast:
                            scene bg BFast20
                            with dissolve
                        else:
                            scene bg Breakfast20
                            with dissolve
                        $ renpy.pause ()
                        scene bg SleepBlack
                        with fade
                        play music Honey
                        $ timeofdaycounter += 1
                        jump kitchen
                    "Tease Lauren" if finished_htbyd_shoot:
                        play music SexMusic
                        if brobe_bfast:
                            scene bg BFast02
                            with fade
                        else:
                            scene bg Breakfast02
                            with fade
                        RT "{i}Look at that sexy redhead, just blabbering on about her social life.{/i}"
                        RT "{i}I wonder what she'd do if I teased her a little. Hopefully she won't kill me now that we've messed around a little.{/i}"
                        if brobe_bfast:
                            scene bg BFast14
                            with fade
                        else:
                            scene bg Breakfast14
                            with fade
                        L "And so I said to Kenzie..."
                        if brobe_bfast:
                            scene bg BFast15
                            with dissolve
                        else:
                            scene bg Breakfast15
                            with dissolve
                        L "..."
                        S "What?... What did you say to Kenzie?"
                        L "Never mind... it was a stupid story."
                        if brobe_bfast:
                            scene bg BFast06
                            with fade
                        else:
                            scene bg Breakfast06
                            with fade
                        LT "{i}I can't believe [ryan] is doing this in front of everybody!{/i}"
                        LT "{i}Ohhh... but his toes do feel good!{/i}"
                        M "You ok, Lauren? You're being unusually quiet."
                        L "Uhhh... yeah... I'm great!..."
                        "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                        $ laurenlibido += 1
                        scene bg SleepBlack
                        with fade
                        play music Honey
                        $ timeofdaycounter += 1
                        jump kitchen
                    "Tease Sidney" if finished_wr_shoot:
                        play music SexMusic
                        scene bg Breakfast12
                        with fade
                        RT "{i}Man, Sidney is hella beautiful, but my brain just shuts down when she starts talking about design college.{/i}"
                        RT "{i}I need to liven things up a little or I'm going to fall asleep.{/i}"
                        scene bg Breakfast25
                        with fade
                        S "So, I had to start over from scratch, and when I finally got the new outfit put together according to his specifications..."
                        S "... do you know what he said to me?..."
                        scene bg Breakfast26
                        with dissolve
                        S "..."
                        M "What?..."
                        S "Huhhh?..."
                        M "What did your professor say?"
                        S "Oh... uhh... \"Nice outfit.\""
                        M "Huh..."
                        M "No offense Sidney, but that story was a bit anticlimactic."
                        S "Uhhh... yeah... sorry."
                        scene bg Breakfast13
                        with fade
                        ST "{i}Ohhhh... I should kill that little shit!...{/i}"
                        ST "{i}Mmmm... but it does feel really good.{/i}"
                        "{i}{b}\"Sidney's Libido +1\"{/b}{/i}"
                        $ sidneylibido += 1
                        scene bg SleepBlack
                        with fade
                        play music Honey
                        $ timeofdaycounter += 1
                        jump kitchen
            "No":
                $ screen_on = "kitchenmap"
                call screen kitchenmap
    else:
        scene bg Kitchen01
        with fade
        RT "{i}It smells good in here. Should I join everybody for breakfast?{/i}"
        menu:
            "Yes":
                if brobe_bfast:
                    scene bg BFast02
                    with fade
                else:
                    scene bg Breakfast02
                    with fade
                $ renpy.pause ()
                scene bg Breakfast10
                R "So, will Mandy and Aunt Cami ever be joining us for breakfast?"
                M "Maybe, but probably very rarely... I think they feel like they're intruding in our home."
                M "And in such a small house, It's hard to get privacy, so they probably just use this time to get some alone time."
                L "I wish I could skip breakfast and have alone time too."
                if brobe_bfast:
                    scene bg BFast05
                    with fade
                else:
                    scene bg Breakfast05
                    with fade
                M "Well, too bad! You're a part of this family, and studies show that families that have at least one meal together every day are much closer."
                ST "{i}Some of us have become closer than you would probably ever approve of.{/i}"
                LT "{i}Is that why [ryan] and I have become so close?{/i}"
                M "Now, let's eat our breakfast before we're late for school."
                $ move_in_bfast = True
                menu:
                    "Tease Mom":
                        play music SexMusic
                        R "Would you mind pouring more maple syrup on my pancakes?"
                        M "I can pass it to you, and you can pour it yourself."
                        R "But I always pour too much, and it ruins my pancakes."
                        R "You always do it just right."
                        M "Ok... I guess I can do that."
                        if brobe_bfast:
                            scene bg BFast16
                            with dissolve
                        else:
                            scene bg Breakfast16
                            with dissolve
                        M "There... how's that?"
                        if brobe_bfast:
                            scene bg BFast17
                            with fade
                        else:
                            scene bg Breakfast17
                            with fade
                        R "They're perfect... I mean the syrup's perfect!"
                        if brobe_bfast:
                            scene bg BFast18
                            with fade
                        else:
                            scene bg Breakfast18
                            with fade
                        MT "{i}You bold cheeky bastard!... I know what that was about.{/i}"
                        MT "{i}So, why did you do it for him?{/i}"
                        if brobe_bfast:
                            scene bg BFast19
                            with dissolve
                        else:
                            scene bg Breakfast19
                            with dissolve
                        MT "{i}Shit!... I need to get laid, so I'm not always so horny around [ryan] and the girls!{/i}"
                        MT "{i}When are they going to let my fucking husband out of prison?{/i}"
                        "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                        $ momlibido += 1
                        R "Thanks, Mom!"
                        if brobe_bfast:
                            RT "{i}It almost seems like she knows I'm staring at her breasts, and just doesn't care. Is it possible she's showing them off for me on purpose?{/i}"
                        else:
                            RT "{i}Oh, she doesn't seem in any hurry to close that robe! Is it possible she's showing them off for me on purpose?{/i}"
                        if brobe_bfast:
                            scene bg BFast20
                            with dissolve
                        else:
                            scene bg Breakfast20
                            with dissolve
                        $ renpy.pause ()
                        scene bg SleepBlack
                        with fade
                        play music Honey
                        $ timeofdaycounter += 1
                        jump kitchen
                    "Tease Lauren" if finished_htbyd_shoot:
                        play music SexMusic
                        if brobe_bfast:
                            scene bg BFast02
                            with fade
                        else:
                            scene bg Breakfast02
                            with fade
                        RT "{i}Look at that sexy redhead, just blabbering on about her social life.{/i}"
                        RT "{i}I wonder what she'd do if I teased her a little. Hopefully she won't kill me now that we've messed around a little.{/i}"
                        if brobe_bfast:
                            scene bg BFast14
                            with fade
                        else:
                            scene bg Breakfast14
                            with fade
                        L "And so I said to Kenzie..."
                        if brobe_bfast:
                            scene bg BFast15
                            with dissolve
                        else:
                            scene bg Breakfast15
                            with dissolve
                        L "..."
                        S "What?... What did you say to Kenzie?"
                        L "Never mind... it was a stupid story."
                        if brobe_bfast:
                            scene bg BFast06
                            with fade
                        else:
                            scene bg Breakfast06
                            with fade
                        LT "{i}I can't believe [ryan] is doing this in front of everybody!{/i}"
                        LT "{i}Ohhh... but his toes do feel good!{/i}"
                        M "You ok, Lauren? You're being unusually quiet."
                        L "Uhhh... yeah... I'm great!..."
                        "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                        $ laurenlibido += 1
                        scene bg SleepBlack
                        with fade
                        play music Honey
                        $ timeofdaycounter += 1
                        jump kitchen
                    "Tease Sidney" if finished_wr_shoot:
                        play music SexMusic
                        scene bg Breakfast12
                        with fade
                        RT "{i}Man, Sidney is hella beautiful, but my brain just shuts down when she starts talking about design college.{/i}"
                        RT "{i}I need to liven things up a little or I'm going to fall asleep.{/i}"
                        scene bg Breakfast25
                        with fade
                        S "So, I had to start over from scratch, and when I finally got the new outfit put together according to his specifications..."
                        S "... do you know what he said to me?..."
                        scene bg Breakfast26
                        with dissolve
                        S "..."
                        M "What?..."
                        S "Huhhh?..."
                        M "What did your professor say?"
                        S "Oh... uhh... \"Nice outfit.\""
                        M "Huh..."
                        M "No offense Sidney, but that story was a bit anticlimactic."
                        S "Uhhh... yeah... sorry."
                        scene bg Breakfast13
                        with fade
                        ST "{i}Ohhhh... I should kill that little shit!...{/i}"
                        ST "{i}Mmmm... but it does feel really good.{/i}"
                        "{i}{b}\"Sidney's Libido +1\"{/b}{/i}"
                        $ sidneylibido += 1
                        scene bg SleepBlack
                        with fade
                        play music Honey
                        $ timeofdaycounter += 1
                        jump kitchen
            "No":
                $ screen_on = "kitchenmap"
                call screen kitchenmap

#############  JACKY'S ROOM  ################################  JACKY'S ROOM  ###################################################

label camille_workout:                  #### Edited 9-1-2020 ####
    if auntanger >= 1:
        jump aunt_angry
    if auntlibido == 10:
        jump aunthornybedroom
    if saw_aunt_exercise:
        scene bg MomDoor
        with fade
        if couldnt_resist:
            RT "{i}I'm not going back in there... she was pissed!{/i}"
            $ screen_on = "momdoormap"
            call screen momdoormap
        else:
            RT "{i}No reason to go back in there, I already know that Aunt Cami's exercising.{/i}"
            $ screen_on = "momdoormap"
            call screen momdoormap
    if first_aunt_exercise:
        scene bg AuntWorkout07
        with fade
        RT "{i}She's exercising again. I could sit and watch all day...{/i}"
        RT "{i}I don't know if that's a good idea though, last time she got kind of angry.{/i}"
        scene bg AuntWorkout01
        with fade
        RT "What should I do?"
        menu:
            "Stay and watch.":
                "Yeah, it's worth the risk, and her wrath."
                scene bg AuntWorkout08
                with fade
                CT "{i}I can feel that perverted little mother fucker's eyes staring at my ass.{/i}"
                CT "{i}I wonder if he's getting a hard-on from watching me?{/i}"
                "{i}{b}\"Aunt Camille's Libido +1\"{/b}{/i}"
                $ auntlibido += 1
                scene bg AuntWorkout09
                with dissolve
                RT "{i}Ohhh... this is giving me the biggest boner!{/i}"
                CT "{i}Alright, now I'm starting to feel uncomfortable.{/i}"
                CT "{i}What does he think this is... a free show?{/i}"
                scene bg AuntWorkout06
                with fade
                C "Would you stop staring at my ass and let me work out in peace?"
                C "This is starting to get a little creepy."
                R "I wasn't..."
                scene bg AuntWorkout03
                C "Yeah right... do you think I'm an idiot?"
                C "Now get out of here... I'm not turning around again until you do!"
                R "That shirt gives plenty to look at from the front too."
                scene bg AuntWorkout06
                with dissolve
                C "Go!"
                "{i}{b}\"Aunt Camille's Anger +2\"{/b}{/i}"
                $ auntanger += 2
                $ couldnt_resist = True
                $ saw_aunt_exercise = True
                scene bg MomDoor
                with fade
                $ screen_on = "momdoormap"
                call screen momdoormap
            "I should leave.":
                RT "{i}I'd love to stick around and watch that show, but she gets pretty mad when she catches me.{/i}"
                RT "{i}I think I'll just play it safe this time.{/i}"
                $ saw_aunt_exercise = True
                scene bg MomDoor
                with fade
                $ screen_on = "momdoormap"
                call screen momdoormap
    else:
        scene bg AuntWorkout01
        with fade
        RT "{i}Oh Nice!... I thought Aunt Cami did yoga this morning. I guess she wanted to squeeze another workout in today.{/i}"
        RT "{i}Should I enjoy the view for a little bit before I announce my arrival?{/i}"
        menu:
            "look closer":
                scene bg AuntWorkout08
                with fade
                RT "{i}She does have one fine ass.{/i}"
                scene bg AuntWorkout02
                with fade
                $ couldnt_resist = True
            "Resist and say hi":
                R "Hey Aunt Cami. How's the workout going?"
                play sound WomanBreath
                scene bg AuntWorkout02
                with dissolve
        C "Oh... it's you..."
        C "You scared me!"
        scene bg AuntWorkout03
        with dissolve
        C "What do you want, twerp?"
        R "Oh... not much... I was just wondering why you're working out again today."
        R "Didn't you work out with Mom This morning?"
        scene bg AuntWorkout04
        with dissolve
        C "What?... The yoga?"
        C "Sure... it helps tone my body and improves my balance, but I've got to do other types of workouts to build my muscles."
        C "And now that I can't afford a gym membership, here I am."
        R "Is that the outfit you wear to the gym?"
        scene bg AuntWorkout05
        with dissolve
        C "Yeah... as well as many others... Why, do you like it?"
        R "Pfff... yeah!... There's not a straight red blooded male out there that wouldn't."
        C "I guess I do get a lot of guys staring at me."
        R "You're lucky that's all they do to you."
        scene bg AuntWorkout06
        with dissolve
        C "Ohhh, I see! You're one of those men that think women get what they deserve for dressing slutty."
        R "I didn't say that!"
        scene bg AuntWorkout03
        with dissolve
        C "So what do I deserve for the maid outfit you make me wear to clean the house?"
        R "It's not me who makes you wear the outfit... you know it's because you pissed Mom off, so you need to stop blaming me."
        C "Well... you're the only one around to enforce it. When you're not here, I don't have to wear it."
        R "You're right... I need to get on Sidney to make sure she's enforcing your dress code when I'm not around."
        scene bg AuntWorkout06
        with dissolve
        $ renpy.pause ()
        scene bg AuntWorkout03
        with dissolve
        C "Was there something you needed?"
        R "No... I just had a question for Mom, and thought I'd find her in here."
        C "She's always taking a shower right now, dumbass!"
        if couldnt_resist:
            C "From how long you lingered at the door staring at my ass, I would have guessed \"that\" must have been the purpose of your visit."
            CT "{i}I must be looking pretty good if even my own nephew can't keep his eyes off of me.{/i}"
            "{i}{b}\"Aunt Camille's Libido +1\"{/b}{/i}"
            $ auntlibido += 1
            C "Now if you'll excuse me, I need to get back to my workout."
        else:
            C "And since she's not here, why don't you run along so I can get back to my workout."
        scene bg AuntWorkout07
        with fade
        RT "{i}How can I leave when she's putting on such a good show?{/i}"
        if couldnt_resist:
            C "[ryan]! Stop staring at my ass and get out of here!"
            "{i}{b}\"Aunt Camille's Anger +2\"{/b}{/i}"
            $ auntanger += 2
        else:
            RT "{i}But... if I stare too long, she's going to notice.{/i}"
        scene bg SleepBlack
        with fade
        $ first_aunt_exercise = True
        $ saw_aunt_exercise = True
        scene bg MomDoor
        with fade
        $ screen_on = "momdoormap"
        call screen momdoormap

label aunt_angry:                       #### Edited 9-2-2020 ####
    if timeofdaycounter == 5:
        while spycaminmomroom == True:
            scene bg MomDoorNight
            with fade
            RT "{i}Aunt Cami locked the door like always. I wonder if she's still mad at me?{/i}"
            RT "{i}Then again, when isn't she?{/i}"
            menu:
                "Take a peek.":
                    jump auntspycamroommad
                "Never mind.":
                    $ screen_on = "momdoornightmap"
                    call screen momdoornightmap
        if timeofdaycounter == 5:
            scene bg MomDoorNight
            with fade
            RT "{i}Aunt Cami locked the door like always. I wonder if she's still mad at me?{/i}"
            RT "{i}Then again, when isn't she?{/i}"
            $ screen_on = "momdoornightmap"
            call screen momdoornightmap
    else:
        scene bg MomDoor
        RT "{i}Aunt Cami Actaully locked the door this time!... Probably because she's mad at me.{/i}"
        RT "{i}Should I see if I can smooth things over?{/i}"
        menu:
            "Knock":
                scene bg AuntAngry01
                with fade
                R "Hey Aunt Cami, workin out?"
                C "What do you want twerp? I really don't want to talk to you right now!"
                menu:
                    "Give her a gift":
                        if gaveauntgift == False:
                            scene bg AuntAngry02
                            with dissolve
                            C "You bought me a gift?"
                            menu:
                                "Give her a chocolate bar" if inventory.inv_amount(chocolate) >= 1:
                                    scene bg AuntAngry03
                                    with dissolve
                                    C "What? Am I too skinny for you!?"
                                    "{i}{b}\"Aunt Camille's Anger +1\"{/b}{/i}"
                                    $ auntanger += 1
                                    $ inventory.drop(chocolate)
                                    $ gaveauntgift = True
                                    C "Maybe one of my stalkers at the gym will want it."
                                    scene bg MomDoor
                                    with fade
                                    $ screen_on = "momdoormap"
                                    call screen momdoormap
                                "Give her Hardnlong gift card" if inventory.inv_amount(giftcard) >= 1:
                                    scene bg AuntAngry04
                                    with dissolve
                                    C "Really?... No strings attached?... I don't have to show you my boobs or anything?"
                                    C "Thanks!"
                                    "{i}{b}\"Aunt Camille's Anger -3\"{/b}{/i}"
                                    $ auntanger -= 3
                                    $ inventory.drop(giftcard)
                                    $ gaveauntgift = True
                                    if auntanger >= 1:
                                        scene bg AuntAngry01
                                        with dissolve
                                        C "But don't think that I've forgiven you yet. I still think you're a perverted degenerate, and your actions were completely inappropriate."
                                        scene bg MomDoor
                                        with fade
                                        $ screen_on = "momdoormap"
                                        call screen momdoormap
                                    else:
                                        scene bg AuntAngry02
                                        with dissolve
                                        C "Thank you, [ryan]! I guess you're not horrible all of the time."
                                        scene bg MomDoor
                                        with fade
                                        $ screen_on = "momdoormap"
                                        call screen momdoormap
                                "Give her flowers" if inventory.inv_amount(flowers) >= 1:
                                    $ inventory.drop(flowers)
                                    scene bg AuntAngry03
                                    with dissolve
                                    $ gaveauntgift = True
                                    C "[ryan], what the fuck? I'm not your girlfriend!"
                                    "{i}\"Throws them in the trash\"{/i}"
                                    C "You've got some weird boundary issues."
                                    C "Maybe next time try to think of something a little less creepy."
                                    "{i}{b}\"Aunt Camille's Affection -1\"{/b}{/i}"
                                    "{i}{b}\"Aunt Camille's Anger +2\"{/b}{/i}"
                                    $ auntanger += 2
                                    $ auntaffection -= 1
                                    scene bg MomDoor
                                    with fade
                                    $ screen_on = "momdoormap"
                                    call screen momdoormap
                                "Never mind":
                                    scene bg AuntAngry03
                                    with dissolve
                                    C "Did you just come to stare at me, twerp? I'm trying to work out. Don't bother me anymore!"
                                    "{i}{b}\"Aunt Camille's Anger +1\"{/b}{/i}"
                                    $ auntanger += 1
                                    scene bg MomDoor
                                    with fade
                                    $ screen_on = "momdoormap"
                                    call screen momdoormap
                        else:
                            scene bg AuntAngry01
                            with dissolve
                            C "You already gave me a gift [ryan]. Stop being such a needy simp!"
                            $ auntanger += 1
                            "{i}{b}\"Aunt Camille's Anger +1\"{/b}{/i}"
                            scene bg MomDoor
                            with fade
                            $ screen_on = "momdoormap"
                            call screen momdoormap
                    "I just wanted to apologize":
                        scene bg AuntAngry03
                        with dissolve
                        C "Well actions speak louder than words, so stop being who you are, and maybe I'll forgive you!"
                        RT "{i}I guess I better give her some time, or maybe I can get her a present so she won't be so mad.{/i}"
                        scene bg MomDoor
                        with fade
                        $ screen_on = "momdoormap"
                        call screen momdoormap
            "Peek through spy-cam" if spycaminmomroom == True:
                jump auntspycamroommad
            "I'm just going to give her some time to cool down":
                $ screen_on = "momdoormap"
                call screen momdoormap

label auntspycamroommad:                #### Edited 9-2-2020 ####
    if timeofdaycounter == 5:
        scene bg MomSleep14
        with dissolve
        $ renpy.pause ()
        scene bg MomSleep11
        with fade
        RT "{i}Not much going on... I guess I should have suspected that.{/i}"
        scene bg MomDoorNight
        with fade
        $ screen_on = "momdoornightmap"
        call screen momdoornightmap
    else:
        scene bg SpyCamAuntAngryBedroom02
        RT "{i}Working out again? That woman has some body issues.{/i}"
        RT "{i}Probably didn't help when her husband took off with the nanny.{/i}"
        scene bg SpyCamAuntAngryBedroom01
        with fade
        RT "{i}I don't know what else I expected her to be doing.{/i}"
        scene bg MomDoor
        with fade
        $ screen_on = "momdoormap"
        call screen momdoormap

label naughty_pranks_on_mom:            #### Edited 9-2-2020 ####
    if momnight:
        scene bg MomDoorNight
        with fade
        RT "{i}I shouldn't push my luck... that's enough for tonight.{/i}"
        $ screen_on = "momdoornightmap"
        call screen momdoornightmap
    if mom_mischief >= 2:
        scene bg MomSleep01
        with fade
        RT "{i}Should I make a visit to Mom's bedside tonight?{/i}"
        menu:
            "Yes.":
                play music SexMusic
                RT "{i}I'm getting addicted to Mom's body... I can't wait until she gives it to me willingly.{/i}"
                RT "{i}So what whould I choose tonight?{/i}"
                menu:
                    "Footjob.":
                        RT "{i}I've gotta take off that bra so I have some goods to look at while her feet are caressing my cock.{/i}"
                        scene bg SleepBlack
                        with fade
                        scene bg MomSleep03
                        with fade
                        RT "{i}I can't wait to cum all over them!{/i}"
                        scene MFJobVideo01
                        with fade
                        $ renpy.pause ()
                        RT "{i}Oh, fuck! That feels so good!{/i}"
                        RT "{i}And the view can't be beat.{/i}"
                        $ renpy.pause ()
                        RT "{i}Oh, yeah! I'm about to cum!{/i}"
                        RT "{i}And I get to cum all over Mom's tits!{/i}"
                        RT "{i}This was such a good idea!{/i}"
                        RT "{i}Hhhnnnnggghhhh!...{/i}"
                        play sound Ejaculate
                        scene bg MomSleep04
                        with fade
                        with hpunch
                        $ renpy.pause ()
                        play sound Ejaculate
                        scene bg MomSleep05
                        with dissolve
                        with vpunch
                        $ renpy.pause ()
                        scene bg MomSleep06
                        with dissolve
                        RT "{i}Fuck yeah... I covered her.{/i}"
                        RT "{i}Now to hide the evidence and rub it all in. This extra moisturizer should make her skin even more radiant.{/i}"
                        scene bg SleepBlack
                        with fade
                        scene bg MomDoorNight
                        with fade
                        play music Honey
                        if mom_mischief == 2:
                            $ mom_mischief = 3
                        $ momnight = True
                        $ screen_on = "momdoornightmap"
                        call screen momdoornightmap
                    "Hotdog her ass.":
                        RT "{i}First I've got to get those tiny panties off and turn her on her stomach.{/i}"
                        scene bg SleepBlack
                        with fade
                        scene bg MomSleep07
                        with fade
                        RT "{i}I'm going to cum all over that ass!{/i}"
                        scene MHDVideo01
                        with fade
                        $ renpy.pause ()
                        RT "{i}Oh, wow! This is where my dick belongs!{/i}"
                        $ renpy.pause ()
                        RT "{i}Ohhh... I'm gonna cum!{/i}"
                        RT "{i}Mom... I'm gonna cum all over your ass!{/i}"
                        RT "{i}Hnnnggghhh!...{/i}"
                        play sound Ejaculate
                        scene bg MomSleep08
                        with fade
                        with hpunch
                        $ renpy.pause ()
                        play sound Ejaculate
                        scene bg MomSleep09
                        with dissolve
                        $ renpy.pause ()
                        scene bg MomSleep10
                        with dissolve
                        RT "{i}Oh, yeah... she's fucking covered!{/i}"
                        RT "{i}Now to wipe that moisturizing goodness into her skin, and say goodbye until next time.{/i}"
                        scene bg SleepBlack
                        with fade
                        scene bg MomDoorNight
                        with fade
                        play music Honey
                        if mom_mischief == 2:
                            $ mom_mischief = 3
                        $ momnight = True
                        $ screen_on = "momdoornightmap"
                        call screen momdoornightmap
            "No.":
                scene bg MomDoorNight
                with fade
                $ screen_on = "momdoornightmap"
                call screen momdoornightmap
    if mom_mischief >= 1:
        scene bg MomSleep01
        with fade
        RT "{i}Should I make a visit to Mom's bedside tonight?{/i}"
        menu:
            "Yes.":
                play music SexMusic
                RT "{i}Thank God! She's still wearing her sexy underwear to sleep.{/i}"
                scene bg MomSleep02
                with fade
                RT "{i}Now, what can I get away with, without waking her up?{/i}"
                menu:
                    "Take off her panties.":
                        "{i}Why should I just look at her boobs? With Mom in this state, I can have a look at whatever I want.{/i}"
                        scene bg SleepBlack
                        with fade
                        RT "{i}I'll just slide these tiny panties down and onto the floor.{/i}"
                        RT "{i}And let's see if I can roll her onto her stomach so I can get a better view.{/i}"
                        scene bg MomSleep07
                        with fade
                        RT "{i}That is one firm ass... and that pussy and butthole!... I'm going to jizz in my pants!{/i}"
                        RT "{i}I'd better hold back... I've got bigger plans than jizzing in my pants.{/i}"
                        menu:
                            "Hotdog her ass.":
                                RT "{i}This is going to be risky... We'll see just how deep of a sleep she's in.{/i}"
                                scene bg SleepBlack
                                with fade
                                scene MHDVideo01
                                $ renpy.pause ()
                                RT "{i}Oh, my God!... I'm actually sliding my dick between Mom's ass cheeks!{/i}"
                                RT "{i}If I angled my dick down just a little, I could fully penetrate her.{/i}"
                                RT "{i}That might wake her up though, not to mention, I want her to be fully awake and willing the first time I penetrate her.{/i}"
                                $ renpy.pause ()
                                RT "{i}Ohhh... I'm gonna cum!{/i}"
                                RT "{i}Mom... I'm gonna cum all over your ass!{/i}"
                                RT "{i}Hnnnggghhh!...{/i}"
                                play sound Ejaculate
                                scene bg MomSleep08
                                with fade
                                with hpunch
                                $ renpy.pause ()
                                play sound Ejaculate
                                scene bg MomSleep09
                                with dissolve
                                $ renpy.pause ()
                                scene bg MomSleep10
                                with dissolve
                                RT "{i}Oh, yeah... she's fucking covered!{/i}"
                                RT "{i}Now to wipe that moisturizing goodness into her skin, and say goodbye until next time.{/i}"
                                scene bg SleepBlack
                                with fade
                                scene bg MomDoorNight
                                with fade
                                play music Honey
                                $ mom_mischief = 2
                                $ momnight = True
                                $ screen_on = "momdoornightmap"
                                call screen momdoornightmap
            "No.":
                scene bg MomDoorNight
                with fade
                $ screen_on = "momdoornightmap"
                call screen momdoornightmap
    else:
        scene bg MomSleep01
        with fade
        RT "{i}Should I make a visit to Mom's bedside tonight?{/i}"
        menu:
            "Yes.":
                play music SexMusic
                RT "{i}Yes!... I was worried Mom was going to start sleeping in sweats or something when her robe disappeared.{/i}"
                RT "{i}God, I love her sexy underwear!{/i}"
                scene bg MomSleep02
                with fade
                RT "{i}And now that her pesky robe is out of the way, I can start to have some fun.{/i}"
                RT "{i}Now, what can I get away with, without waking her up?{/i}"
                menu:
                    "Take off her bra.":
                        RT "{i}How about I start out with a view of Mom's boobs.{/i}"
                        scene bg SleepBlack
                        with fade
                        RT "{i}I just need to unclasp... bring it around her shoulders... roll her onto her back... and pull the bra off her arms.{/i}"
                        scene bg MomSleep03
                        with fade
                        RT "{i}Wow!... To think I used to suck on those every day!{/i}"
                        RT "{i}I'm going to cum all over them...{/i}"
                        RT "{i}But why jack off when I can think of something even more fun?{/i}"
                        menu:
                            "How about a foot job?":
                                if lauren_mischief >= 2:
                                    RT "{i}Using Lauren's feet felt incredible, I think I'll start with that.{/i}"
                                else:
                                    RT "{i}I know a lot of guys are into feet. Let's see what all the hype is about.{/i}"
                                scene bg SleepBlack
                                with fade
                                scene MFJobVideo01
                                with fade
                                $ renpy.pause ()
                                RT "{i}Oh, fuck! That feels so good!{/i}"
                                RT "{i}And the view can't be beat.{/i}"
                                $ renpy.pause ()
                                RT "{i}Oh, yeah! I'm about to cum!{/i}"
                                RT "{i}And I get to cum all over Mom's tits!{/i}"
                                RT "{i}This was such a good idea!{/i}"
                                RT "{i}Hhhnnnnggghhhh!...{/i}"
                                play sound Ejaculate
                                scene bg MomSleep04
                                with fade
                                with hpunch
                                $ renpy.pause ()
                                play sound Ejaculate
                                scene bg MomSleep05
                                with dissolve
                                with vpunch
                                $ renpy.pause ()
                                scene bg MomSleep06
                                with dissolve
                                RT "{i}Fuck yeah... I covered her.{/i}"
                                RT "{i}Now to hide the evidence and rub it all in. This extra moisturizer should make her skin even more radiant.{/i}"
                                scene bg SleepBlack
                                with fade
                                scene bg MomDoorNight
                                with fade
                                play music Honey
                                $ mom_mischief = 1
                                $ momnight = True
                                $ screen_on = "momdoornightmap"
                                call screen momdoornightmap
            "No.":
                scene bg MomDoorNight
                with fade
                $ screen_on = "momdoornightmap"
                call screen momdoornightmap

label no_more_night_fun_with_mom:       #### Edited 9-2-2020 ####
    if momatclub:
        scene bg MomRoomNight
        with fade
        RT "{i}Mom's at the club tonight, but where's Aunt Cami?{/i}"
        RT "{i}Is it possible she followed Mom to the club?{/i}"
        $ screen_on = "momsmapnight"
        call screen momsmapnight
    else:
        scene bg MomDoorNight
        with fade
        RT "{i}What the fuck? The door is locked!... This is Aunt Cami's doing for sure!{/i}"
        RT "{i}Mom never locks the door!{/i}"
        RT "{i}What could be going on in there?{/i}"
        menu:
            "Check spycam.":
                scene bg MomSleep14
                with fade
                $ renpy.pause ()
                scene bg MomSleep11
                with fade
                RT "{i}Why did I expect anything else?{/i}"
                scene bg MomDoorNight
                with fade
                $ screen_on = "momdoornightmap"
                call screen momdoornightmap
            "Who cares?":
                $ screen_on = "momdoornightmap"
                call screen momdoornightmap

label aunthornybedroom:                 #### Edited 9-2-2020 ####
    if spycaminmomroom == True:
        scene bg MomDoor
        with fade
        RT "{i}Hmmm... door's locked... I don't think she's any more pissed off at me than usual.{/i}"
        RT "{i}I wonder what she's doing?{/i}"
        menu:
            "Use spy-cam.":
                jump auntspycamroomhorny
            "Not right now.":
                RT "{i}On second thought... I don't really care about what Aunt Cami's doing in Mom's room.'{/i}"
                $ screen_on = "momdoormap"
                call screen momdoormap
    else:
        scene bg MomDoor
        with fade
        play sound Camille01 loop
        RT "{i}Hmmm... door's locked... I don't think she's any more pissed off at me than usual.{/i}"
        RT "{i}Wait! What is that moaning noise?{/i}"
        RT "{i}Sound's like she's getting a different type of workout in today.{/i}"
        RT "{i}I wish I could see what's going on... I've got to figure out a way to spy on her.{/i}"
        "{i}{b}\"Aunt Camille's Libido -5\"{/b}{/i}"
        $ auntlibido -= 5
        stop sound
        $ screen_on = "momdoormap"
        call screen momdoormap

label auntspycamroomhorny:              #### Edited 9-2-2020 ####
    scene bg AuntMastBedroom01
    with dissolve
    RT "{i}Alright, Aunt Cami, let's see what you're up to.{/i}"
    scene bg AuntMastBedroom02
    with fade
    play music SexMusic
    RT "{i}Oh, nice! Great timing once again!{/i}"
    RT "{i}These cameras have been worth every penny.{/i}"
    RT "{i}She's got her dildo out, and it looks like she found Mom's butt plug!{/i}"
    RT "{i}Maybe I'm wrong, but it seems like a butt plug should be a personal item.{/i}"
    if not auntmbatespycam:
        CT "{i}I always knew my sister had a slutty side... but a butt plug?{/i}"
        CT "{i}Hmmm... I do wonder though...{/i}"
        scene bg AuntMastBedroom03
        with fade
        CT "{i}If my sister can get this thing in her ass, then so... can... I...{/i}"
        CT "{i}There!{/i}"
    else:
        CT "{i}I can't believe I enjoyed using that butt plug so much last time!...{/i}"
        CT "{i}Am I becoming as big of a slut as my sister?{/i}"
        CT "{i}I really do want to cum as hard as I did last time though...{/i}"
        scene bg AuntMastBedroom03
        with fade
        CT "{i}Hopefully... it will... go... In easier... this time...{/i}"
        CT "{i}There!{/i}"
    scene AuntMastBedroomVideo01
    with fade
    play sound Camille01 loop
    $ renpy.pause ()
    if auntmbatespycam:
        CT "{i}God, I hope [ryan] pays me to see my breasts again!{/i}"
        CT "{i}And when is he going to pay me to take it even further?{/i}"
        CT "{i}To give him a handjob, maybe?{/i}"
        C "Ohhh..."
        CT "{i}Maybe a blowjob?{/i}"
        CT "{i}Would he want to fuck my ass like this butt plug?{/i}"
        CT "{i}Whoah... hold on there, Camille!... That's escalating things way too quickly.{/i}"
        CT "{i}It's just that this fucking plug in my ass is making me think these dirty things...{/i}"
        CT "{i}This dirty butt plug of my sister's...{/i}"
        C "Aaahhh..."
        CT "{i}Why does the fact that the plug belongs to [mom_name] turn me on even more?{/i}"
    else:
        CT "{i}Why do I keep lying to myself?... Trying to tell myself I'm not a whore like my sister...{/i}"
        CT "{i}When the facts don't lie. The facts say that I'm just a dirty slut like she is...{/i}"
        C "Ooohhh..."
        CT "{i}Even dirtier, probably!{/i}"
        CT "{i}For fuck's sake! I let my own nephew bribe me into showing him my tits!{/i}"
        CT "{i}And it's not about the money... like I've been trying to tell myself...{/i}"
        CT "{i}It just feels so good to have someone desire me sexually again.{/i}"
        C "Aaahh..."
        CT "{i}Bobby seemed bored of me just a couple years after being married... about the same time we hired that homewrecker, Cindy.{/i}"
        CT "{i}So, I started dressing like a whore at the gym... because I needed the guys to stare...{/i}"
        CT "{i}To undress me with their eyes!{/i}"
        CT "{i}To fuck me in their minds!{/i}"
        C "MMMMmmm..."
        CT "{i}And now we can't even afford a fucking gym membership!{/i}"
        CT "{i}And although I hate fucking [ryan]...{/i}"
        CT "{i}I need his hungry eyes on my breasts!{/i}"
        CT "{i}I love the fact that he's probably jacking off to thoughts of me.{/i}"
        RT "{i}I've got to get a picture of this to jack off to!{/i}"
        stop sound
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        hide CamaraFlash
        play sound Camille01 loop
        C "Aaaahhh..."
        CT "{i}I need to see his massive cock again!{/i}"
    $ renpy.pause ()
    CT "{i}Oh, fuck! I'm almost there!{/i}"
    $ renpy.pause ()
    CT "{i}Oh, fuck! Oh, fuck! I'm coming!{/i}"
    stop sound
    play sound Ejaculate
    scene bg AuntMastBedroom04
    with fade
    CT "{i}Oh, God! Oh, fuck!{/i}"
    C "Aaaahhhhhh!"
    RT "{i}Another huge squirter!... I fucking live in a porn video... or at least I'm going to soon!{/i}"
    scene bg AuntMastBedroom05
    with dissolve
    if auntmbatespycam:
        CT "{i}I'm never masturbating without a butt plug again!{/i}"
    else:
        CT "{i}Oh, God! I haven't squirted like that since I was in my twenties!{/i}"
        CT "{i}Was it because of the butt plug?{/i}"
        $ auntmbatespycam = True
    "{i}{b}\"Aunt Camille's Libido -5\"{/b}{/i}"
    $ auntlibido -= 5
    RT "{i}Just... wow!{/i}"
    RT "{i}Now I'd better get out of here before someone else comes along.{/i}"
    $ persistent.gal_auntie_3 = True
    play music Honey
    $ screen_on = "momdoormap"
    call screen momdoormap

label moms_update_six_mbate_thoughts:   #### Edited 9-2-2020 ####
    if blackmailed_mom_megan:
        MT "{i}Did I really give [ryan] a blowjob?...{/i}"
        MT "{i}What kind of mother does that to her son?{/i}"
        MT "{i}But it's not fair... I've never seen a cock like that!{/i}"
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
        MT "{i}Oh, fuuuuuuck!!!{/i}"
        scene bg SpyCamMomBedroom12 with Dissolve(0.3)
        $ renpy.pause (2.0)
        MT "{i}Oh, my God!... I'm squirting!!{/i}"
        scene bg SpyCamMomBedroom20
        with fade
        stop sound
        MT "{i}Oh, yes!! Fucking squirted again!{/i}"
        MT "{i}I've got to stop thinking about these kinds of things!...{/i}"
        MT "{i}But what's the harm in a little imagination?{/i}"
        MT "{i}That felt sooooo good!{/i}"
        MT "{i}What's wrong with me?{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry, with all these women squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Is it something in the girl's diets?{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Mom's a squirter too.{/i}"
            RT "{i}Maybe there's something in the water.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh, my God! Mom just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Mom's a real squirter!{/i}"
        RT "{i}Just... wow!{/i}"
        "{i}{b}\"Mom's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ momlibido -= 5
        if timeofdaycounter == 5:
            scene bg MomDoorNight
            with fade
            RT "{i}I should probably go get some sleep now, maybe...{/i}"
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
        MT "{i}Did I really give Matt a blowjob?...{/i}"
        MT "{i}What kind of teacher does that to their student?{/i}"
        MT "{i}But I've never seen a student with a cock like that!{/i}"
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
        MT "{i}Oh, fuuuuuuck!!!{/i}"
        scene bg SpyCamMomBedroom12 with Dissolve(0.3)
        $ renpy.pause (2.0)
        MT "{i}Oh, my God!... I'm squirting!!{/i}"
        scene bg SpyCamMomBedroom20
        with fade
        stop sound
        MT "{i}Oh, yes!! Fucking squirted again!{/i}"
        MT "{i}I've got to stop thinking about these kinds of things!...{/i}"
        MT "{i}But what's the harm in a little imagination?{/i}"
        MT "{i}That felt sooooo good!{/i}"
        MT "{i}What's wrong with me?{/i}"
        if familyofsquirters == 4:
            RT "{i}Mom must be doing a lot of extra laundry with all these women squirting all over their beds.{/i}"
            RT "{i}Not to mention what I do in mine.{/i}"
        elif familyofsquirters == 3:
            RT "{i}And that makes 3 for 3.{/i}"
            RT "{i}Is it something in the girl's diets?{/i}"
        elif familyofsquirters == 2:
            RT "{i}Wow! Mom's a squirter too.{/i}"
            RT "{i}Maybe there's something in the water.{/i}"
        elif familyofsquirters == 1:
            RT "{i}Oh, my God! Mom just squirted all over her bed!{/i}"
            RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
            RT "{i}Wow, Mom's a real squirter!{/i}"
        RT "{i}Just... wow!{/i}"
        "{i}{b}\"Mom's Libido -5\"{/b}{/i}"
        RT "{i}I might need to go back to my room to take care of something myself.{/i}"
        $ momlibido -= 5
        if timeofdaycounter == 5:
            scene bg MomDoorNight
            with fade
            RT "{i}I should probably go get some sleep now, maybe...{/i}"
            play music Honey
            $ screen_on = "momdoornightmap"
            call screen momdoornightmap
        else:
            scene bg MomDoor
            with fade
            RT "{i}I should run before I get caught.{/i}"
            $ screen_on = "momdoormap"
            call screen momdoormap

label update_six_momspycamroommad:      #### Edited 9-2-2020 ####
    if timeofdaycounter == 5 and progress >= 15:
        scene bg MomSleep14
        with dissolve
        $ renpy.pause ()
        scene bg MomSleep11
        with fade
        RT "{i}Well... not a lot of action going on here. I should probably just go to sleep myself.{/i}"
        scene bg MomDoorNight
        with fade
        $ screen_on = "momdoornightmap"
        call screen momdoornightmap
    if timeofdaycounter == 5 and found_bathrobe:
        scene bg MomSleep13
        with dissolve
        $ renpy.pause ()
        scene bg MomSleep12
        with fade
        RT "{i}Well... not a lot of action going on here. I should probably just go to sleep myself.{/i}"
        scene bg MomDoorNight
        with fade
        $ screen_on = "momdoornightmap"
        call screen momdoornightmap

#############  Lauren's Room  ###############################  Lauren's Room  ###################################################

label lauren_night:                     #### Edited ####
    if cousinanger >= 1 and progress >= 15:
        jump mandy_angry
    if played_the_game:
        scene bg LaurenDoorNight
        with fade
        RT "{i}I've already kept Mandy up super late. I should just let them sleep.{/i}"
        $ screen_on = "laurendoornightmap"
        call screen laurendoornightmap
    if truth_dare_completed and lauren_door_locked == False:
        scene bg LaurenDoorNight
        with fade
        RT "{i}I wonder if Mandy will be up for continuing our game of \"Truth, or Dare\".{/i}"
        RT "{i}Should I knock and find out?{/i}"
        menu:
            "Knock.":
                $ played_the_game = True
                L "Who is it?"
                R "It's me...."
                L "Come in."
                play music SexMusic
                scene bg Dare02
                with fade
                MD "Oh hey, [ryan]. Did you come to hang out with us again?"
                R "Yeah, I thought I'd see what you're doing."
                L "We're just doing girl time again, but we can make you an honorary girl again for the night."
                R "Do I need to flash you again?"
                L "Oh God, no!"
                LT "{i}I don't need wet panties right now.{/i}"
                L "Just come sit down."
                scene bg Dare05
                with fade
                L "I can't believe I slept through truth or dare again!"
                L "I think you're right, [ryan]... I must be going through a growth spurt."
                L "Even if I don't get taller, I hope my boobs get bigger."
                R "I like small boobs."
                R "So hopefully they don't get much bigger."
                L "So, let's play before I fall asleep again."
                L "I'll go first."
                L "[ryan], you get to choose what I do."
                R "Ok... Truth or ..."
                scene bg Dare75
                with dissolve
                MD "Well, there she goes again."
                R "So are you ready to play with just the two of us again?"
                MD "You know what? I think we can skip the whole truth or dare game this time, and just jump to the good stuff."
                R "Really?..."
                if mandy_first_hj == False:
                    MD "Yeah, I can't get the image of you shooting your load all over your sister out of my head."
                    MD "I was hoping maybe I could maybe be a part of it this time."
                    R "What kind of part do you want?"
                    MD "I've never touched a cock before... Do you mind if I give you a handjob?"
                    R "Holy shit! Are you serious?"
                    MD "As serious as I can possibly be!"
                    MD "Please... Please... Please let me!"
                else:
                    MD "I can't stop thinking about the last handjob I gave you!"
                    MD "I really want to do it again!"
                R "How can I say no to that?"
                scene bg Dare77
                with fade
                MD "Yay!"
                MD "Ok, get your clothes off, and then help me get Lauren's off."
                R "Why do we need to take Lauren's clothes off?"
                MD "Because I want you to cum all over her again."
                R "Wow, Mandy!... If you weren't my cousin, I think I'd be in love with you."
                MD "Yeah well, clearly depravity runs in our blood."
                MD "Now get your clothes off."
                scene bg SleepBlack
                with fade
                "{i}\"A few moments later.\"{/i}"
                scene bg Dare36
                with fade
                MD "I think we're all ready... Let's get into position."
                scene bg Dare70
                with fade
                if mandy_first_hj == False:
                    MD "Oh, my God! I can't believe I'm jacking off a cock for the first time!"
                    MD "And it's such a big one!"
                    MD "Ohhh... And it's so soft!"
                    MD "Shit! I think it's getting harder!"
                    MD "Can I start stroking it now?"
                else:
                    MD "Oh, it feels just as good in my hand as it did the first time!"
                    MD "I don't think I'll ever get over how big it is."
                    MD "Haha... it's getting harder again!"
                    MD "Can I stroke it now?"
                R "Oh, God! Please!"
                scene DareVideo04
                with fade
                $ renpy.pause ()
                MD "How am I doing?"
                R "Ooohhh..."
                MD "Haha... That's what I thought."
                $ mandys_fun_night = True
                menu:
                    "Fuck Lauren's thighs":
                        jump t_d_thighs
                    "Cum":
                        jump cum_hj
            "Not tonight.":
                RT "{i}I don't feel like it tonight.{/i}"
                $ screen_on = "laurendoornightmap"
                call screen laurendoornightmap
    if lauren_mischief == 5 and lauren_door_locked == False:
        scene bg LaurenDoorNight
        with fade
        RT "{i}I wonder if Mandy will be up for continuing our game of \"Truth, or Dare\".{/i}"
        RT "{i}Should I knock and find out?{/i}"
        menu:
            "Knock.":
                $ played_the_game = True
                L "Who is it?"
                R "It's me...."
                L "Come in."
                scene bg Dare02
                with fade
                MD "Oh hey, [ryan]. Did you come to hang out with us again?"
                R "Yeah, I thought I'd see what you're doing."
                L "We're just doing girl time again, but we can make you an honorary girl again for the night."
                R "Do I need to flash you again?"
                L "Oh, God no!"
                LT "{i}I don't need wet panties right now.{/i}"
                L "Just come sit down."
                scene bg Dare05
                with fade
                L "I can't believe I slept through truth or dare again!"
                L "I don't know why I can't stay up very late anymore."
                L "I hope I'm not getting mono like you did, [ryan]."
                R "Nah... You'd be tired all the time, and have other symptoms too."
                R "You're probably just going through a growth spurt."
                L "Oh, I hope so. I'd love to get taller."
                L "It wouldn't take much for me to get taller than you, [ryan]."
                R "You'd better not! I don't want to be the shortest in the family."
                scene bg Dare06
                with dissolve
                MD "Well, with all the sleep Lauren's getting, I think you better buy some platform shoes."
                L "So, let's play before I fall asleep again."
                L "I'll go first."
                L "[ryan], you get to choose what I do."
                R "Ok... Truth or ..."
                scene bg Dare75
                with dissolve
                MD "Well, there she goes again."
                MD "Looks like it's down to just us two."
                MD "And since you're older, you get to go first."
                R "Gee... Thanks."
                show screen Points_screen_Cuz_dare
                play music SexMusic
                MD "Don't mention it... Do you want truth, or dare?"
                jump truth_dare_menus
            "Not tonight.":
                RT "{i}I don't feel like it tonight.{/i}"
                $ screen_on = "laurendoornightmap"
                call screen laurendoornightmap
    if lauren_mischief == 4 and lauren_door_locked == False:
        scene bg LaurenDoorNight
        with fade
        RT "{i}Should I tell Mandy the truth?... Should I lie?....{/i}"
        RT "{i}I need to do something, or things are just going to get awkward.{/i}"
        RT "{i}And if I lie, Mandy might ask her mom about it.{/i}"
        RT "{i}Maybe I should just come clean.{/i}"
        menu:
            "Knock.":
                $ played_the_game = True
                RT "{i}Alright, here goes nothing.{/i}"
                L "Who is it?"
                R "It's me...."
                L "Come in."
                scene bg Dare02
                with fade
                MD "Oh hey, [ryan]. Did you come to hang out with us again?"
                R "Yeah, I thought I'd see what you're doing."
                L "We're just doing girl time again, but we can make you an honorary girl again for the night."
                R "Do I need to flash you again?"
                L "Oh, God no!"
                LT "{i}I don't need wet panties right now.{/i}"
                L "Just come sit down."
                scene bg Dare05
                with fade
                L "Mandy said you guys played truth or dare last time."
                L "I want to play with you guys this time."
                scene bg Dare06
                with dissolve
                MD "Well, if you can stay awake for longer than five minutes, maybe you can."
                RT "{i}I wouldn't bet on it.{/i}"
                L "Well, since I missed out last time, I'll go first."
                MD "Alright Lauren, do you want truth or dare?"
                play music SexMusic
                show screen Points_screen_Cuz_dare
                L "Ok... I'll pick dare."
                MD "Hmmmm... Let me think of a good one."
                MD "...."
                MD "I dare you to...."
                scene bg Dare07
                with dissolve
                MD "Oh, my God!... She went down again."
                scene bg Dare75
                MD "Do you think she might have narcolepsy?"
                R "Maybe."
                R "But she doesn't fall asleep like this in the day."
                MD "Maybe she should get tested."
                RT "{i}The last thing I want is a doctor discovering higher amounts of melatonin in her than is normal.{/i}"
                R "I'm sure she's fine."
                R "She's always been this way."
                R "Let's keep playing."
                MD "Ok... if you're sure."
                MD "...."
                MD "Now if we're going to play this, you know you have to pick truth right now, right?"
                R "Ok... I'll pick truth."
                MD "Awesome"
                scene bg Dare08
                with dissolve
                MD "Now, what is the worst thing you have ever done to my mom?"
                R "Alright... I'm going to tell you, but promise you won't get mad."
                MD "I can't promise that."
                R "...."
                R "Ok...."
                R "Well, the first thing you have to understand is that I'm only a man, and a really horny one at that."
                R "And watching your mom clean our house everyday in that skimpy outfit, made me think things that might not be appropriate for a nephew to think about his aunt."
                MD "Go on...."
                R "So one day, I offered her money and a day off if she would flash me her tits."
                scene bg Dare11
                with dissolve
                MD "Oh, my God! You did not!"
                R "Yeah...."
                MD "Wow! Did she kick you in the nuts?"
                R "No... She flashed me."
                scene bg Dare10
                with dissolve
                $ renpy.pause ()
                MD "...."
                RT "{i}Oh shit, I'm dead.{/i}"
                scene bg Dare09
                with dissolve
                MD "Oh, my God!... That is so awesome!"
                "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
                $ cousinlibido += 1
                R "Wait!... What?"
                MD "You have no idea how happy this makes me!"
                R "I'm confused... How can this make you happy?"
                scene bg Dare75
                with dissolve
                MD "Do you have any idea how many times my mom has ridden my ass for kissing a boy, or dressing too slutty, or looking at dirty pictures?"
                MD "She's been trying to make me lead the life of a nun, and acting like the biggest prude..."
                MD "And now I find out, she's been flashing you her tits for money, and to get out of having to do a few chores?"
                MD "This is too perfect!"
                MD "Now she has no moral high ground."
                MD "You've just given me the best leverage against her I could ever ask for."
                MD "The next time she tries to force her puritanistic ways on me... Oh, I'll be able to shut her down so hard!"
                MD "And the ironic thing is that making me repress all of my urges, has just made me want to do naughty stuff all the more."
                R "Yeah, well, I also think overactive libidos run in the family."
                MD "Oh, I can't wait to use this on her!"
                R "Oh, great! Now she's really going to hate me."
                MD "Oh, yes she is!"
                MD "...."
                MD "Well... I guess it's my turn."
                R "Oh right... Truth, or dare?"
                MD "I'll pick... dare."
                R "Ok... Well let's help you get some of that sexual repression out..."
                R "I'd love to see you kiss Lauren again."
                MD "You make it so easy!"
                "{i}{b}\"Mandy's Submission +1\"{/b}{/i}"
                $ cousinsubmission += 1
                scene bg Dare12
                with fade
                $ renpy.pause ()
                RT "{i}Why do girls kissing turn me on so much?{/i}"
                RT "{i}And the fact that they're cousins makes it so much sexier!{/i}"
                scene bg Dare08
                with fade
                MD "Mmmm... I think Lauren is wearing cherry chapstick."
                MD "Your turn... Do you want truth, or dare?"
                $ lauren_mischief = 5
                jump truth_dare_menus
            "Not tonight.":
                RT "{i}I'm not ready...{/i}"
                $ screen_on = "laurendoornightmap"
                call screen laurendoornightmap
    if lauren_mischief == 3 and lauren_door_locked == False:
        scene bg LaurenDoorNight
        with fade
        RT "{i}Alright, should I invade girl time?{/i}"
        menu:
            "knock":
                $ played_the_game = True
                L "Who is it?"
                R "It's me...."
                L "Come in."
                scene bg Dare02
                with fade
                L "What do you want?"
                R "Just came to see if I can hang out with you girls."
                scene bg Dare03
                with dissolve
                MD "What do you think Lauren? Should we make [ryan] an honorary girl for the night?"
                R "Honorary girl?... Does an honorary girl have a package like this?"
                menu:
                    "Flash them.":
                        scene bg Dare02
                        with dissolve
                        L "Aaahhh... [ryan]! Put that away!"
                        MD "Haha... Or leave it out... it will help us remember that you're no lady."
                        L "Absolutley not! Put it away, or go away!"
                        RT "{i}Mandy's a pretty wild girl.{/i}"
                        RT "{i}It doesn't seem to bother her at all that I'm her cousin.{/i}"
                        RT "{i}She might actually be a lot of fun.{/i}"
                        R "Alright, alright, it's going back in my shorts."
                        L "Good, and don't pull it out again!"
                        R "Ahhh... you're no fun!"
                        MD "Come sit down and gossip with us."
                        scene bg Dare04
                        with fade
                        MD "So... What I want to know is, what in the hell did you do to make my mom hate you so much?"
                        L "You mean besides making her wear that skimpy maid outfit when she cleans the house?"
                        scene bg Dare05
                        with dissolve
                        R "That was actually Mom's idea, not mine."
                        R "I just enforce her rule when I'm here."
                        scene bg Dare04
                        with dissolve
                        MD "She probably hates the manual labor more than having to wear the skimpy outfit, so I don't think that's it."
                        RT "{i}I can't let them know how I've manipulated Aunt Cami into flashing me several times.{/i}"
                        scene bg Dare05
                        with dissolve
                        R "I'm pretty sure she just blames me for that photoshoot with you and Lauren.  She thinks I'm a pervert who's trying to exploit you."
                        MD "pfff... I've told her over and over that the photoshoot was our idea."
                        scene bg Dare06
                        with dissolve
                        L "Well, you did push us to make the pics more sexy."
                        R "I just know what cosplay fans like to see."
                        scene bg Dare04
                        with dissolve
                        MD "By the way, I'm sorry for telling her you were the one taking the pictures.  I don't know how it happened, it just accidentally slipped out."
                        R "It's ok, I'm sure she would have figured it out eventually."
                        L "The way she...."
                        scene bg Dare75
                        with dissolve
                        R "... What the hell?"
                        scene bg Dare07
                        with dissolve
                        MD "Oh, my God!... She did this last night too."
                        MD "I almost called 911, but she seemed to be breathing and healthy... Just... in a really deep sleep."
                        R "I know she sleeps deep, but I've never seen her collapse mid-sentence before."
                        R "Haha... She'll be gone till morning."
                        scene bg Dare75
                        with dissolve
                        MD "That's too bad..."
                        MD "I was hoping for some bonding time tonight.  I didn't get any with her last night either, since she checked out early yesterday too."
                        R "What do you two do to bond?"
                        MD "I don't know, maybe play a game together, or something."
                        R "What kind of game?"
                        MD "Something like... Truth or Dare."
                        R "Well... That doesn't mean that we can't play it."
                        MD "Are you serious?"
                        R "Yeah, why not?"
                        MD "Hmmmm...."
                        scene bg Dare08
                        with dissolve
                        MD "I guess... and Lauren can play too. Even if she doesn't know she's playing."
                        R "Haha... I like the sound of that."
                        MD "And the first rule is that you can't do two truth's in a row.  You can do as many dare's as you want, but you can only choose one truth in between."
                        R "Ok... and what happens if one of us is too chicken to tell the truth, or do the dare?"
                        MD "hmmm... I don't know... Let's just say that if you're too chicken to continue the game, then the game ends, and you have \"the big gay\"."
                        R "That doesn't sound very motivating."
                        MD "That sounds like something someone with \"the big gay\" would say."
                        R "I'm not gay!"
                        MD "Then prove it. You go first."
                        R "Alright, I'm ready."
                        $ reverse_cuz = True
                        show screen Points_screen_Cuz_dare
                        play music SexMusic
                        MD "Ok... Truth or Dare?"
                        menu:
                            "Truth":
                                MD "Hmmm... Ok, I have one.  Present company excluded, which member of your family do you think is the most sexy?"
                                R "Of my family?... I don't find anyone in my family sexy!"
                                RT "{i}Great cover, [ryan]! She'll never expect the truth!{/i}"
                                scene bg Dare75
                                with dissolve
                                MD "I'm calling bullshit.  You're surrounded by drop-dead sexy girls, and you haven't noticed? Yeah, that's bullshit!"
                                MD "So spill it."
                                R "Fine..."
                                $ safest_truth = True
                                RT "{i}Hmmm... Who do I find the most attractive?{/i}"
                                menu:
                                    "Mom":
                                        $ most_attractive_counter = 1
                                    "Sidney":
                                        $ most_attractive_counter = 2
                                    "Lauren":
                                        $ most_attractive_counter = 3
                                    "Aunt Cami":
                                        $ most_attractive_counter = 4
                                    "Uncle Bobby":
                                        scene bg Dare09
                                        with dissolve
                                        MD "Hahaha... You smartass!"
                                        MD "Now, tell the truth!"
                                        with dissolve
                                        menu:
                                            "Mom":
                                                $ most_attractive_counter = 1
                                            "Sidney":
                                                $ most_attractive_counter = 2
                                            "Lauren":
                                                $ most_attractive_counter = 3
                                            "Aunt Cami":
                                                $ most_attractive_counter = 4
                                scene bg Dare08
                                with dissolve
                                if most_attractive_counter == 1:
                                    MD "Your own mother, huh?..."
                                    MD "So you like your women more mature?"
                                    R "I just like her natural curves. She may be a little bit older, but she's aged really well."
                                    MD "She is really hot... More of a natural beauty, where my mom has a lot of plastic improvements."
                                    "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
                                    $ cousinlibido += 1
                                    R "Your mom is hot too, though."
                                    scene bg Dare10
                                    with dissolve
                                    MD "Eeuuww... You just called your aunt hot!"
                                    scene bg Dare08
                                    with dissolve
                                    R "But you..."
                                    MD "Alright, it's my turn."
                                if most_attractive_counter == 2:
                                    MD "Sidney, huh?..."
                                    MD "It's her ass, isn't it?"
                                    R "Well, it is pretty firm."
                                    R "She runs almost everyday.  She's in great shape."
                                    MD "I wish I had a bigger ass."
                                    R "What? No, your ass works great for your body type."
                                    MD "You like my ass?"
                                    R "Ummm... Is there a safe way to answer this question?"
                                    scene bg Dare09
                                    with dissolve
                                    MD "Haha... You like your cousin's ass!"
                                    "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
                                    $ cousinlibido += 1
                                    scene bg Dare08
                                    with dissolve
                                    MD "Pervert!"
                                    R "But, you..."
                                    MD "Alright, it's my turn."
                                if most_attractive_counter == 3:
                                    MD "Lauren, huh?..."
                                    MD "You don't mind the itty-bitty titties?"
                                    R "No... I like a nice big set of breasts as much as the next guy, but there's something about little titties that really turns me on."
                                    MD "So you think my little mole hills are ok?"
                                    R "Yeah!... They're sexy as hell."
                                    scene bg Dare09
                                    with dissolve
                                    MD "Haha... I'm your cousin, you pervert."
                                    "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
                                    $ cousinlibido += 1
                                    scene bg Dare08
                                    with dissolve
                                    R "But, you..."
                                    MD "Alright, it's my turn."
                                if most_attractive_counter == 4:
                                    scene bg Dare10
                                    with dissolve
                                    MD "Eeuuww... Really?... My mom?"
                                    MD "But she's all plastic."
                                    R "I don't mind. The plastic surgeon did a great job."
                                    R "Plus, she keeps herself in really great shape."
                                    scene bg Dare75
                                    with dissolve
                                    MD "Yeah, but I think she only does that because her self-esteem is so low."
                                    MD "I think she's really craving some attention since my dad left."
                                    RT "{i}Duly noted.{/i}"
                                    MD "I've never really thought of my mom as hot, but I guess I can see it."
                                    "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
                                    $ cousinlibido += 1
                                    MD "Alright, it's my turn."
                                R "Ok, what do you want? Truth or dare?"
                            "Dare":
                                MD "Let me think... Ok...."
                                MD "How about you bend down and give your sister a little kiss on the ass."
                                R "What?... But she's my sister!"
                                MD "Oh, don't pretend like you don't want to."
                                MD "You've been sneaking peeks at her ass since she fell asleep."
                                R "No, I haven't!"
                                RT "{i}Shit, she noticed.{/i}"
                                MD "Don't worry, it doesn't bother me... I think her ass is hard not to look at, too."
                                MD "It makes me really jealous actually.  I've got such a small ass."
                                R "You've got a great ass."
                                MD "No, I don't."
                                R "For your tiny build... Your ass is perfect."
                                MD "Thanks!... but you really shouldn't be complimenting your cousin's ass."
                                R "Uhhh...."
                                scene bg Dare75
                                with dissolve
                                MD "Haha... Relax... I'm just teasing."
                                MD "Now are you going to kiss Lauren's ass, or do you give up and have \"the big gay\"?"
                                R "Ok... I'll do it."
                                scene bg Dare14
                                with fade
                                R "Nope! Put your phone away! There can't be any photo evidence of this."
                                MD "Haha... Fine!"
                                MD "Now kiss her ass!"
                                R "Ok... Here I go."
                                scene bg Dare13
                                with dissolve
                                $ renpy.pause ()
                                MD "Haha!... You're kissing your own sister's ass!"
                                MD "It's actually kind of cute!"
                                MDT "{i}Fucking hot, actually.{/i}"
                                "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
                                $ cousinlibido += 1
                                scene bg Dare14
                                with dissolve
                                R "Alright, it's your turn."
                                scene bg Dare75
                                with fade
                                $ dare_counter = 1
                                R "So what do you want?"
                                R "Truth, or dare?"
                        MD "....I'll take dare."
                        R "Ok, hmmm...."
                        if dare_counter == 1:
                            R "Since you made me kiss Lauren's ass... Why don't you..."
                        else:
                            pass
                        R "Kiss Lauren on the lips."
                        MD "Haha... easy!"
                        MD "We sometimes kiss each other on the lips just when we greet each other."
                        R "Well, then I want you to...."
                        MD "Too late! You've already said it."
                        R "Well, then do it already."
                        MD "Fine!"
                        "{i}{b}\"Mandy's Submission +1\"{/b}{/i}"
                        $ cousinsubmission += 1
                        scene bg Dare12
                        with fade
                        $ renpy.pause ()
                        MDT "{i}Her lips are so soft.{/i}"
                        "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
                        $ cousinlibido += 1
                        RT "{i}That's pretty hot!{/i}"
                        scene bg Dare75
                        with fade
                        MD "Next time, think of a challenging dare."
                        R "I thought having you kiss your cousin on the lips would be challenging."
                        MD "Nah... That's just a thing girls do normally all the time."
                        MD "Ususally when boys aren't looking, cuz they always say something inappropriate."
                        R "Well, you have permission to kiss in front of me whenever you want."
                        MD "Yep, something inappropriate like that."
                        R "Sorry."
                        MD "...."
                        MD "Ok, it's your turn again."
                        MD "Truth, or dare?"
                        menu:
                            "Truth":
                                scene bg Dare75
                                with dissolve
                                MD "Ok... I want to know why my mom really hates you so bad, so my question is, what is the worst thing you've ever done to my mom?"
                                RT "{i}Oh shit! Was it the time I had her press her boobs on the shower glass{/i}?"
                                if lounge_boobs:
                                    RT "{i}Was it the time I had her flash me on the coffee table?{/i}"
                                if kitchen_boobs:
                                    RT "{i}Maybe, it was when I had her present her tits on a platter?{/i}"
                                R "Hmmm...."
                                RT "{i}I can't answer that!... She'll know what a huge pervert I am...{/i}"
                                R "I'm afraid to answer that...."
                                MD "Hah!... I knew you did something more to her."
                                MD "Tell me, tell me, tell me!"
                                R "I can't."
                                scene bg Dare08
                                with dissolve
                                MD "Really?"
                                MD "Well, that was the shortest game of Truth or Dare I've ever played. it looks like you have \"the big gay\" after all."
                                R "Shit! I guess so."
                            "Dare":
                                scene bg Dare75
                                with dissolve
                                MD "Ok... I want to know why my mom really hates you so bad, so I dare you to tell me what is the worst thing you've ever done to my mom?"
                                R "You can't do that.  That's a truth."
                                MD "Yes, you can do that.  You can use a dare to make someone tell the truth, you just can't use a truth to make somebody do a dare."
                                R "Hmmm... That doesn't seem fair."
                                MD "Maybe so, but thems the rules."
                                MD "So what is the worst thing you've done to my mom?"
                                RT "{i}Oh shit! Was it the time I had her press her boobs on the shower glass{/i}?"
                                if lounge_boobs:
                                    RT "{i}Was it the time I had her flash me on the coffee table?{/i}"
                                if kitchen_boobs:
                                    RT "{i}Maybe, it was when I had her present her tits on a platter?{/i}"
                                R "Hmmm...."
                                RT "{i}I can't answer that!... She'll know what a huge pervert I am...{/i}"
                                R "I'm afraid to answer that...."
                                MD "Hah!... I knew you did something more to her."
                                MD "Tell me, tell me, tell me!"
                                R "I can't."
                                scene bg Dare08
                                with dissolve
                                MD "Really?"
                                MD "Well, it looks like you have \"the big gay\" after all."
                                R "Shit! I guess so."
                        scene bg Dare08
                        with dissolve
                        hide screen Points_screen_Cuz_dare
                        MD "I guess we should call it a night then."
                        play music Honey
                        MD "If you ever want to play truth or dare with Lauren and I again, you know where to find us."
                        MD "But just so you know, If you want to play with us, you'll have to answer that question about my mom."
                        R "Oh, come on! Don't be like that."
                        MD "I can't help it, now that I know there's something to her hate for you, I'm dying to know what it is."
                        MD "So bring your A game next time, or don't come at all."
                        scene bg SleepBlack
                        with fade
                        scene bg LaurenDoorNight
                        with fade
                        RT "{i}What the fuck just happened?... I inadvertently let Mandy know that I did something to Aunt Cami... her own mother!{/i}"
                        RT "{i}Now she's not going to let me hang out with them at night until I'm willing to tell her.{/i}"
                        RT "{i}How is she going to react when I tell her I manipulated her mom to flash me by appealing to her weakness of shopping?{/i}"
                        RT "{i}Wow! When I think about it like that, it does sound pretty fucked up!{/i}"
                        RT "{i}I didn't mean to be such a manipulative bastard, I was just horny and wanted to see some tits.{/i}"
                        RT "{i}Shit!... Maybe I inherited the tendency to be a manipulative bastard from my father.{/i}"
                        RT "{i}I suppose I'm going to have to come clean to Mandy if I want to hang out with her anymore.{/i}"
                        RT "{i}I'll have to think of a way to make it not sound so bad.{/i}"
                        $ lauren_door_locked = True
                        $ lauren_mischief = 4
                        $ screen_on = "laurendoornightmap"
                        call screen laurendoornightmap
            "Leave them alone tonight.":
                RT "{i}Never mind, they will probably just talk about boys, or other dumb girl stuff.{/i}"
                $ screen_on = "laurendoornightmap"
                call screen laurendoornightmap
    if progress >= 15 and lauren_door_locked == False:
        scene bg LaurenDoorNight
        with fade
        RT "{i}Creeping on Lauren might be a little more challenging now that Mandy is sharing a bed with her.{/i}"
        RT "{i}It also might make things a whole lot more fun.{/i}"
        RT "{i}Please say that Mandy drank the melatonin tea as well.{/i}"
        scene bg Dare01
        with fade
        RT "{i}Oh shit!... They're both still awake!{/i}"
        scene bg Dare02
        with dissolve
        L "Don't you know how to knock?"
        L "Look... you caught us in our underwear."
        R "Being in your underwear didn't stop you two from coming into my room without knocking."
        R "And then staring at my penis, I might add."
        MD "Haha... I've still got a mental picture of that."
        MD "Can we do anything for you, [ryan]?"
        RT "{i}Shit!... what should I tell them I wanted?{/i}"
        RT "...."
        R "I was just bored.  Thought I'd come hang out with you two."
        L "We're having girl time."
        L "Go away!"
        scene bg Dare03
        with dissolve
        MD "{i}(quiet voice){/i} I don't mind if he stays and hangs out."
        L "{i}(whispering){/i} He's a pervert... He's probably just here to stare at us in our underwear."
        MD "{i}(whispering){/i} Yeah... I still don't mind if he hangs out with us."
        L "{i}(whispering){/i} Fine... But at least not tonight."
        MD "{i}(whispering){/i} Ok... I'm fine with that."
        scene bg Dare02
        with dissolve
        L "You can come hang out with us on a different night."
        MD "Yep, it's just us girls tonight."
        RT "{i}They're both awake still. They must not have drank any tea.{/i}"
        R "Ok, that's fair."
        R "I'm heading to the kitchen, do you want me to bring you back anything? Maybe a cup of tea or something?"
        L "I've already had a cup."
        MD "I hate tea!"
        R "You hate tea?"
        MD "Yeah, it tastes like some leaves farted in my water."
        MD "I despise the stuff."
        RT "{i}Well, shit!{/i}"
        R "Ok well, goodnight then."
        MD "Goodnight!"
        scene bg Dare01
        with dissolve
        $ renpy.pause ()
        scene bg LaurenDoorNight
        with fade
        RT "{i}She doesn't drink tea?{/i}"
        RT "{i}What am I gonna find to spike for Mandy?{/i}"
        RT "{i}They said I could come hang out on another night, maybe I should just come back and see what kind of fun I can have when they're awake.{/i}"
        RT "{i}Lauren had a cup of tea though, Mandy must be keeping her awake.  I'll bet she crashes really soon.{/i}"
        $ lauren_door_locked = True
        $ lauren_mischief = 3
        $ screen_on = "laurendoornightmap"
        call screen laurendoornightmap
    if lauren_door_locked:
        scene bg LaurenDoorNight
        with fade
        RT "{i}She locked her door.{/i}"
        RT "{i}I wonder if she's asleep... I can't hear anything.{/i}"
        RT "{i}I'll have to try again tomorrow night.{/i}"
        RT "{i}I guess I could take a look at the spycam to see what they're doing.{/i}"
        menu:
            "Take a look.":
                RT "{i}Yeah, my curiosity is getting the best of me.{/i}"
                scene bg Dare81
                with dissolve
                RT "{i}Damn... Mandy's still awake.{/i}"
                scene bg Dare79
                with fade
                RT "{i}Since she doesn't drink the melatonin tea, I won't be able to do any more sneaking around in there at night.{/i}"
                $ screen_on = "laurendoornightmap"
                call screen laurendoornightmap
            "I don't feel like it.":
                $ screen_on = "laurendoornightmap"
                call screen laurendoornightmap
    if laurennight:
        scene bg LaurenDoorNight
        with fade
        RT "{i}I shouldn't press my luck... That's enough for tonight.{/i}"
        $ screen_on = "laurendoornightmap"
        call screen laurendoornightmap
    if lauren_mischief == 2:
        scene bg NightLauren01
        with fade
        menu:
            "Mischief with Lauren":
                scene bg LaurenNightPeek1
                with fade
                $ renpy.pause ()
                play music SexMusic
                scene bg LaurenNightPeek3
                if tookmelatonin:
                    RT "{i}I can't believe how knocked out she is... That melatonin-laced tea is incredible.{/i}"
                else:
                    RT "{i}Luckily Lauren has always been a deep sleeper.{/i}"
                RT "{i}Now to roll her onto her back.{/i}"
                scene bg LaurenMischief01
                with fade
                RT "{i}Nice!{/i}"
                menu:
                    "Lift her shirt":
                        scene bg LaurenMischief02
                        RT "{i}Time to uncover those little mosquito bites again.{/i}"
                        RT "{i}What will it be tonight?{/i}"
                        menu:
                            "Use Lauren's hand.":
                                scene bg LaurenMischiefVideo02F01
                                with fade
                                RT "{i}Oh, God!... I love how she squeezes!{/i}"
                                RT "{i}It's like instinctual for her to have a penis in her hand..{/i}"
                                scene LaurenMischiefVideo02
                                $ renpy.pause ()
                                RT "{i}So good!{/i}"
                                $ renpy.pause ()
                                RT "{i}Oh... I'm gonna cum!{/i}"
                                $ renpy.pause ()
                                play sound Ejaculate
                                scene bg LaurenMischief05
                                with fade
                                with hpunch
                                with vpunch
                                $ renpy.pause ()
                                scene bg LaurenMischief06
                                with dissolve
                                $ renpy.pause ()
                                RT "{i}Fuck!... That is so hot!{/i}"
                                RT "{i}I'd better wipe that up and get out of here.{/i}"
                                scene bg SleepBlack
                                with fade
                                $ renpy.pause ()
                                $ laurennight = True
                                play music Honey
                                scene bg LaurenDoorNight
                                with fade
                                RT "{i}That made me pretty tired. Should I go to bed now?{/i}"
                                $ screen_on = "laurendoornightmap"
                                call screen laurendoornightmap
                            "Use Lauren's feet.":
                                RT "{i}Her feet felt pretty good before, I think I'll try them again.{/i}"
                                scene bg LaurenMischiefVideo01F01
                                with fade
                                RT "{i}The bottoms of her feet are so soft.{/i}"
                                RT "{i}I've got to say, this might just grow on me.{/i}"
                                scene LaurenMischiefVideo01
                                with fade
                                $ renpy.pause ()
                                RT "{i}That's pretty hot.{/i}"
                                $ renpy.pause()
                                RT "{i}Oh, damn!....{/i}"
                                $ renpy.pause ()
                                play sound Ejaculate
                                scene bg LaurenMischief03
                                with fade
                                with vpunch
                                with hpunch
                                $ renpy.pause ()
                                scene bg LaurenMischief04
                                with fade
                                RT "{i}Oh, yeah...{/i}"
                                RT "{i}I might just be turning into a feet guy.{/i}"
                                RT "{i}Now I'd better wipe this up and get out of here.{/i}"
                                scene bg SleepBlack
                                with fade
                                $ renpy.pause ()
                                $ laurennight = True
                                $ lauren_mischief = 2
                                play music Honey
                                scene bg LaurenDoorNight
                                with fade
                                RT "{i}That made me pretty tired. Should I go to bed now?{/i}"
                                $ screen_on = "laurendoornightmap"
                                call screen laurendoornightmap
            "Not tonight":
                $ laurennight = True
                scene bg LaurenDoorNight
                with fade
                $ screen_on = "laurendoornightmap"
                call screen laurendoornightmap
    if lauren_mischief == 1:
        scene bg NightLauren01
        with fade
        menu:
            "Mischief with Lauren":
                scene bg LaurenNightPeek1
                with fade
                $ renpy.pause ()
                play music SexMusic
                scene bg LaurenNightPeek3
                RT "{i}This went really well last time... I hope I can get as lucky a second time.{/i}"
                RT "{i}I'm just going to go ahead and roll her over again.{/i}"
                scene bg LaurenMischief01
                with fade
                RT "{i}Perfect.{/i}"
                RT "{i}Well... Almost perfect.{/i}"
                menu:
                    "lift her shirt":
                        scene bg LaurenMischief02
                        with dissolve
                        RT "{i}Yeah... Those little titties look better with my cum all over them.{/i}"
                        RT "{i}I better get to work.{/i}"
                        RT "{i}I think this time though I'll try something a little different though.{/i}"
                        menu:
                            "Use Lauren's feet.":
                                if mom_mischief >= 1:
                                    RT "{i}Using Mom's feet was surprisingly awesome, let's go for that.{/i}"
                                else:
                                    RT "{i}I know a lot of guys are into feet. Let's see what all the hype is about.{/i}"
                                scene bg LaurenMischiefVideo01F01
                                with fade
                                RT "{i}The bottoms of her feet are surprisingly soft.{/i}"
                                RT "{i}Let's see how this compares with a handy.{/i}"
                                scene LaurenMischiefVideo01
                                with fade
                                $ renpy.pause ()
                                RT "{i}That's pretty hot, actually.{/i}"
                                $ renpy.pause()
                                RT "{i}Oh, damn!....{/i}"
                                $ renpy.pause ()
                                play sound Ejaculate
                                scene bg LaurenMischief03
                                with fade
                                with vpunch
                                with hpunch
                                $ renpy.pause ()
                                scene bg LaurenMischief04
                                with fade
                                RT "{i}Oh, yeah... That was pretty good.{/i}"
                                RT "{i}I don't know if it was necessarily better than a handy, but I think I might try it again.{/i}"
                                RT "{i}Now I'd better wipe this up and get out of here.{/i}"
                                scene bg SleepBlack
                                with fade
                                $ renpy.pause ()
                                $ laurennight = True
                                $ lauren_mischief = 2
                                play music Honey
                                scene bg LaurenDoorNight
                                with fade
                                RT "{i}That made me pretty tired. Should I go to bed now?{/i}"
                                $ screen_on = "laurendoornightmap"
                                call screen laurendoornightmap
            "Not tonight":
                $ laurennight = True
                scene bg LaurenDoorNight
                with fade
                $ screen_on = "laurendoornightmap"
                call screen laurendoornightmap
    else:
        scene bg NightLauren01
        with fade
        menu:
            "Mischief with Lauren":
                scene bg LaurenNightPeek1
                with fade
                $ renpy.pause ()
                play music SexMusic
                scene bg LaurenNightPeek3
                RT "{i}She doesn't seem to be responding to the subliminal messages anymore... But that doesn't mean I can't still have some fun with her.{/i}"
                RT "{i}I don't think I'll ever get tired of looking at that ass, but I want to see her from the front too.{/i}"
                if tookmelatonin:
                    RT "{i}Let's just see if her melatonin-laced tea will keep her asleep while I'm turning her over.{/i}"
                else:
                    RT "{i}Let's just see if she if she's still a deep sleeper.{/i}"
                scene bg LaurenMischief01
                with fade
                RT "{i}Perfect.{/i}"
                RT "{i}Well... Almost perfect.{/i}"
                menu:
                    "lift her shirt":
                        RT "{i}She didn't even stir when I turned her over, so lifting her shirt shouldn't even faze her.{/i}"
                        scene bg LaurenMischief02
                        with fade
                        RT "{i}Wow!... She's so sexy!... it isn't fair that she should be off-limits just because she's my sister.{/i}"
                        RT "{i}That's just bullshit! I don't care what anybody else thinks, I've just get to get her thinking more like me.{/i}"
                        RT "{i}But for now... I really just want to cum all over those tits!{/i}"
                        RT "{i}I'll just jack off and cum all over her... or....{/i}"
                        menu:
                            "Use Lauren's hand.":
                                scene bg LaurenMischiefVideo02F01
                                with fade
                                RT "{i}Oh, God!... She instinctively started squeezing!{/i}"
                                RT "{i}Ok, let's see if this will work.{/i}"
                                scene LaurenMischiefVideo02
                                $ renpy.pause ()
                                RT "{i}Even better than I expected!{/i}"
                                $ renpy.pause ()
                                RT "{i}Oh... I'm gonna cum!{/i}"
                                $ renpy.pause ()
                                play sound Ejaculate
                                scene bg LaurenMischief05
                                with fade
                                with hpunch
                                with vpunch
                                $ renpy.pause ()
                                scene bg LaurenMischief06
                                with dissolve
                                $ renpy.pause ()
                                RT "{i}Fuck!... That is so hot!{/i}"
                                RT "{i}I'd better wipe that up and get out of here.{/i}"
                                scene bg SleepBlack
                                with fade
                                $ renpy.pause ()
                                $ laurennight = True
                                $ lauren_mischief = 1
                                play music Honey
                                scene bg LaurenDoorNight
                                with fade
                                RT "{i}I can't believe that worked! Maybe those H-game scenarios aren't so unrealistic after all.{/i}"
                                $ screen_on = "laurendoornightmap"
                                call screen laurendoornightmap
            "Not tonight":
                $ laurennight = True
                scene bg LaurenDoorNight
                with fade
                $ screen_on = "laurendoornightmap"
                call screen laurendoornightmap

label truth_dare_menus:                 #### Edited ####
    menu:
        "Truth (always a safe bet)" if truth_told == 0:
            jump truth_sequence
        "Safest dare" if daily_dare_counter == 0:
            jump safest_dare_sequence
        "Safe dare ({i}Submission {b}5 {color=#0000ff}or{/color}{/b} Libido {b}8{/b}{/i} )" if daily_dare_counter <= 1:
            jump safe_dare_sequence
        "Slightly risky dare ({i}Submission {b}8 {color=#0000ff}or{/color}{/b} Libido {b}9{/b}{/i} )" if daily_dare_counter <= 2:
            jump s_risk_dare_sequence
        "Risky dare ({i}Submission {b}12{/b}{/i} )" if daily_dare_counter <=3:
            jump risky_dare_sequence
        "Very risky dare ({i}Submission {b}17{/b}{/i})":
            jump v_risky_dare_sequence
        "Let's be done for the night.":
            jump quit_dare

label truth_sequence:                   #### Edited ####
    if daily_truth_counter == 4 and v_risky_truth:
        scene bg Dare55
        with dissolve
        MD "Aaahhh... You're no fun."
        MD "Alright, let me think of one for a second..."
        scene bg Dare52
        with dissolve
        MD "Ok... When you finally get around to fucking my mom, what position do you want to fuck her in?"
        R "Shit, Mandy! I can't believe you're talking to me about fucking your mom!"
        MD "Well, you'd better make peace with it, cuz we've got a lot of work to do."
        MD "And I just want to know what position you're going to go for."
        R "Hmmm..."
        menu:
            "Missionary":
                scene bg Dare54
                with dissolve
                MD "Really? Why so boring?"
                R "Hey!"
                scene bg Dare52
                with dissolve
                MD "Alright, whatever floats your boat."
            "Doggy":
                MD "That's kind of kinky."
            "Cowgirl":
                scene bg Dare53
                with dissolve
                MD "Yeah... Make her ride you!"
                scene bg Dare52
                with dissolve
            "Doesn't matter, as long as it's anal.":
                scene bg Dare55
                with dissolve
                MD "Euwww..."
                "{i}{b}\"Mandy's Respect -1\"{/b}{/i}"
                $ cousinrespect -= 1
                MD "That's really dirty!"
                MD "I wouldn't even wish that on my mom."
                scene bg Dare52
                with dissolve
                MD "But I guess that might bring her down a few extra pegs."
        MDT "{i}I can just imagine it.{/i}"
        "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
        $ cousinlibido += 1
        R "Alright, it's your turn. Truth, or Dare?"
        MD "I'll pick truth again."
        R "Hmmm... Let me think of a good one."
        scene bg SleepBlack
        with fade
        "Several minutes later and a rather revealing truth from Mandy."
        scene bg Dare53
        with fade
        MD "Haha... And that's why I hate pineapples even more than bananas."
        R "Hahaha... No wonder... They are so much thicker and rougher than bananas."
        R "Ohhh... I won't be able to get that image out of my mind."
        scene bg Dare52
        with fade
        MD "I know, right?"
        MD "And now that I've told you that humiliating truth, I think it's your turn."
        MD "Truth, or Dare?"
        $ truth_told = 1
        $ daily_truth_counter = 5
        jump truth_dare_menus
    if daily_truth_counter == 4 and v_risky_truth == False:
        scene bg Dare55
        with dissolve
        MD "Aaahhh... You're no fun."
        MD "Alright, let me think of one for a second..."
        scene bg Dare52
        with dissolve
        MD "Ohh... I know..."
        MD "You already told me that you got my mom to flash you..."
        scene bg Dare54
        with dissolve
        MD "So what I want to know is... Are you trying to fuck my mom?"
        R "Pfff... What!?"
        scene bg Dare52
        with dissolve
        MD "No... it's an honest question... And I'm genuinely curious."
        R "I can't believe you're asking me that!"
        MD "It's a simple question."
        R "Why would you want to know that?"
        scene bg Dare54
        with dissolve
        MD "I don't know..."
        MD "Well... Actually I do."
        MD "I'm still shocked that such a prude bitch would flash you her tits for money, so if she's willing to do that, then she'd probably be willing to do more for even more money."
        MD "I haven't confronted her about flashing you yet, so I'll keep that between us. But I want to help you to make my mom into even more of a slut."
        RT "{i}Oh, my God! I think Mandy's flipped as hard as I have!{/i}"
        R "Why would you want to do that to your own mom?"
        MD "You have no idea what it was like to be raised by that so-called \"sexually pure\" woman."
        MD "She's been so protective and controlling of me my entire life."
        MD "And while her flashing you takes her down a peg, if she got fucked by her own nephew, and I had proof... that would take her down like 100 pegs, and she'd never have room to lecture or control me again."
        R "Wow! You must really hate your mom."
        MD "Actually, I really love her. But I hate living under her thumb."
        MD "And If anybody's going to bring my mom down in this way, I would feel much safer if it was you."
        RT "{i}My God! I can't belive we're having this conversation.{/i}"
        MD "So I ask you again, as part of my truth..."
        MD "Do you have any intentions of fucking my mom?"
        R "Honestly, I was just having a little fun with her before."
        R "But after what you just told me... I suppose I could put some effort into doing... that."
        scene bg Dare53
        with dissolve
        MD "Awesome!"
        scene bg Dare52
        with dissolve
        MD "But it's not going to be easy."
        MD "And it might be kind of expensive."
        R "Shit! It's not like I have a humongous Mafia debt to pay or anything."
        scene bg Dare54
        with dissolve
        MD "Hmmm... Is there any way I could help make more money?"
        R "Well... Would you be willing to be in another photoshoot?"
        R "Maybe even be willing to shoot some risqué shots with another girl?"
        scene bg Dare53
        with dissolve
        MD "YES!"
        scene bg Dare52
        with dissolve
        MD "I mean... sure... if you think it would help."
        MD "And we could use the proceeds of the shoot to buy my mom's sluttiness?"
        MDT "{i}My mom's going to be the biggest slut in the family!... Then I'll be able to get away with anything!{/i}"
        MDT "{i}Can we really get her to fuck her own nephew?{/i}"
        MDT "{i}My God! That would be crazy!{/i}"
        "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
        $ cousinlibido += 1
        R "I'll make sure those funds are used specifically for that."
        MD "I can't wait!"
        RT "{i}She's just as corrupt and manipulative as I am.{/i}"
        RT "{i}Must be a common symptom of having your life fucked up my the Mafia.{/i}"
        MD "So, it's my turn."
        MD "And I pick truth."
        R "Oh... Ok... I'm still processing our conversation... Just give me a second to think of one."
        scene bg SleepBlack
        with fade
        "Several minutes later and a rather revealing truth from Mandy."
        scene bg Dare53
        with fade
        MD "Hahah... No I swear to God, that's exactly what happened."
        R "Hahah...Wow! That is unbelievable."
        scene bg Dare52
        with dissolve
        R "No wonder you hate bananas."
        MD "Ugghh... I can't even look at them."
        MD "So now that I've told you that humiliating truth, it's your turn."
        R "Ok, but that will be a hard one to top."
        MD "So do you want truth, or dare?"
        $ truth_told = 1
        $ daily_truth_counter = 5
        $ v_risky_truth = True
        jump truth_dare_menus
    if daily_truth_counter == 3 and risky_truth:
        MD "Alright, so what I want to know is..."
        MD "When was the last time you fooled around with Lauren?"
        "{i}\"[ryan] tells Mandy the date of the last time they fooled around.\"{/i}"
        MD "Oh, damn! I should have asked what you two did to fool around."
        R "Haha... Maybe next time."
        R "So, I guess it's your turn."
        MD "Ok, I pick truth."
        R "When was the last time you used your mom's dildo?"
        MD "Just a couple days ago."
        R "Really? But where did you? I didn't see any..."
        R "Never mind."
        scene bg Dare32
        with dissolve
        MD "What do you mean?"
        MD "You're not spying on me somehow, are you?"
        R "Haha... Of course not... How would I?"
        MD "I don't know."
        scene bg Dare31
        with dissolve
        MD "Never mind, I guess."
        MD "It's your turn."
        MD "Do you want truth, or dare?"
        $ truth_told = 1
        $ daily_truth_counter = 4
        jump truth_dare_menus
    if daily_truth_counter == 3 and risky_truth == False:
        MD "Ok, this truth is like the last one..."
        MD "Have you ever fooled around with Lauren?"
        R "...."
        R "Yes."
        scene bg Dare78
        with dissolve
        MD "Damn, [ryan]!"
        MD "You do know that incest is against the law, right?"
        R "Well, it's not like I'm sleeping with any of them."
        RT "{i}yet... unless you count Sidney in my bed last night.{/i}"
        scene bg Dare31
        with dissolve
        MD "I'm just giving you a hard time."
        R "Well, I never did anything inappropriate with my sisters until my father was arrested, and all the shit hit the fan with the FBI and Mafia."
        R "Then I saw Mom stripping for the first time, and it's like a switch got turned on inside me."
        MD "I think I kinda know what you're talking about."
        scene bg Dare76
        with dissolve
        MD "When my dad left, I just started wanting to do things that kept my mind from thinking about all the shit that's going on."
        MD "Most of it was pretty rebellious."
        MD "I mean, I've always been a little bit rebellious, but before all this went down, I would never have been sitting here naked, playing truth or dare with you."
        MD "But since my dad left, I've got all this sexual frustration, and crazy strong sexual desires."
        scene bg Dare31
        with dissolve
        MD "Maybe that's what they mean when they talk about \"daddy issues\"."
        R "Huh... maybe."
        R "But, I think you're onto something."
        R "Maybe I'm just coping with everthing by pursuing things that are the most distracting."
        MD "That's how I look at it."
        R "Huh..."
        R "Well, whatever, it's your turn."
        MD "Alright, I'll take truth, too."
        R "Hmmm..."
        R "Give me an example of something rebellious you've done, as a result of your dad leaving, that's sexual in nature."
        MDT "{i}Hmmm... what can I tell him, that won't scare him too bad?... Oh, I think this one will be safe.{/i}"
        scene bg Dare76
        with dissolve
        MD "So, when I'm feeling really horny, I sneak into my mom's room and steal her dildo."
        MDT "{i}I should probably leave out the part there's an inscription on it that says it was molded to be identical to my dad's penis.{/i}"
        MD "It's something that would have grossed me out before all of this. I mean, how do I know if she cleaned it well after she used it?"
        MD "But now I don't care. Knowing she might have used it recently kind of turns me on even more now."
        MDT "{i}But not as much as knowing that it's shaped like my dad's cock.{/i}"
        R "Wow! That's pretty hot."
        scene bg Dare31
        with dissolve
        MD "Ok... I believe it's your turn again."
        MD "Do you want truth, or dare?"
        $ truth_told = 1
        $ daily_truth_counter = 4
        $ risky_truth = True
        jump truth_dare_menus
    if daily_truth_counter == 2 and s_risky_truth:
        scene bg Dare31
        with dissolve
        MD "Good, I was hoping to get this out of you."
        R "Uh Oh..."
        MD "When was the last time you and Sidney fooled around?"
        "{i}\"[ryan] tells Mandy the date of the last time they fooled around.\"{/i}"
        scene bg Dare76
        with dissolve
        MD "Holy shit! I thought maybe it had been a little while."
        MDT "{i}For all I know they could have been fucking in [ryan]'s bed last night!{/i}"
        MDT "{i}I know Sidney doesn't stay on the couch.  I'm almost positive she sneaks into [ryan]'s room.{/i}"
        MDT "{i}Could [ryan] really be fucking his own sister?{/i}"
        "{i}Mandy's Libido +1\"{/i}"
        $ cousinlibido += 1
        scene bg Dare31
        with dissolve
        MD "How do you two mess around?"
        R "Sorry, you've already used up your truth."
        MD "Yeah, you caught me. Alright, it's my turn."
        R "Truth, or dare?"
        MD "I'll take truth again."
        R "When was the last time you messed around with Lauren?"
        MD "Well, unlike you, it's been a while... probably three years ago at the last family reunion."
        R "Ok, I was just checking to see if you girls had done anything more recent."
        R "Outside of the game, since I know your truth is up, do you mind telling me what you two did to mess around?"
        MD "Yep, I mind. You'll just have to use your imagination."
        R "Are you sure, cuz my imagination is going to come up with something way crazier than anything you actually did."
        scene bg Dare78
        with dissolve
        MD "Haha... You creep!"
        MD "So, do you want truth, or dare?"
        $ truth_told = 1
        $ daily_truth_counter = 3
        jump truth_dare_menus
    if daily_truth_counter == 2 and s_risky_truth == False:
        scene bg Dare31
        with dissolve
        MD "Ok... Another truth...."
        MD "Oh... I've got one."
        MD "Have you and Sidney ever fooled around?"
        R "Wow! Why are you so interested in my relationship with my family?"
        MD "I've kind of got an idea of what kind of person I think you are, and now I'm just trying to confirm my suspicions."
        MD "So spill it, have you two ever fooled around?"
        R "Uhhh... a... a little bit."
        scene bg Dare76
        with dissolve
        MD "Yeah... I kinda figured."
        scene bg Dare31
        with dissolve
        MDT "{i}Shoot! I should have been more specific, messing around could mean touching each other in the bathtub when they were kids, to fucking each other every other night.{/i}"
        MDT "{i}I can just imagine them going at it in [ryan]'s bed.{/i}"
        "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
        $ cousinlibido += 1
        MD "So what did you two do together?"
        R "Nope, you're not fooling me this time. You've already asked me a question."
        R "Now it's my turn to ask you."
        MDT "{i}Shit!{/i}"
        R "Truth, or dare?"
        MD "I'll choose truth as well."
        RT "{i}I wonder if she's asked me that because she's messed around with someone in our family.{/i}"
        RT "{i}I wonder who it could be?... Most likely Lauren, but if it isn't I've wasted a question.{/i}"
        R "Who have you messed around with in our family?"
        scene bg Dare78
        with dissolve
        MD "You mean besides letting my cousin take semi-naked pictures of me?"
        R "Yeah... That doesn't count."
        scene bg Dare31
        with dissolve
        MD "How do you know that I have?"
        R "Well, if you haven't, just say so."
        MD "Hmmm..."
        MD "Alright... I've messed around a little bit with Lauren."
        R "Ha!... I knew it!"
        scene bg Dare78
        with dissolve
        MD "Haha... Way to go, Sherlock!"
        R "So what did you two do together?"
        MD "Ha... I'm not falling for that either. My turn is over."
        scene bg Dare31
        with dissolve
        MD "Now do you want truth, or dare?"
        $ truth_told = 1
        $ daily_truth_counter = 3
        $ s_risky_truth = True
        jump truth_dare_menus
    if safe_truth and daily_truth_counter == 1:
        if daily_dare_counter >= 2:
            scene bg Dare31
            with dissolve
        else:
            scene bg Dare26
            with dissolve
        MD "Another truth, huh? Ok..."
        MD "I can't get the image of Aunt [mom_name] out of my head, and I haven't even seen her strip."
        MD "So what I want to know is..."
        MD "When was the last time you fantasized about your mom stripping?"
        R "You sure like to get personal."
        MD "Yeah, yeah, we both know you fantasize about her, I just want to know when was the last time."
        R "Fine... I can't place the exact time, but it's been less than a week."
        MDT "{i}So, it seems like he can't get the thought of his mom stripping out of his head either... that's pretty interesting.{/i}"
        MD "Ok... Fair enough."
        MD "I guess it's my turn, and I'll pick truth as well."
        R "You mentioned that you've been picturing Mom stripping, so I'm asking you the same question.  When was the last time you fantasized about Mom?"
        MD "Same question, same answer."
        R "You mean less than a week?"
        MD "Yup."
        R "Wow! I thought you'd try to deny that you've fantasized about her."
        MD "This is truth or dare... If you're going to lie, you shouldn't play..."
        if daily_dare_counter >= 2:
            scene bg Dare32
            with dissolve
        else:
            scene bg Dare27
            with dissolve
        MD "Have you been lying?"
        R "No... Honest to God."
        if daily_dare_counter >= 2:
            scene bg Dare31
            with dissolve
        else:
            scene bg Dare26
            with dissolve
        MD "You'd better not be."
        MD "Because now it's your turn."
        MD "Truth, or dare?"
        $ daily_truth_counter = 2
        $ truth_told = 1
        jump truth_dare_menus
    if daily_truth_counter == 1 and safe_truth == False:
        if daily_dare_counter >= 2:
            scene bg Dare31
            with dissolve
        else:
            scene bg Dare26
            with dissolve
        MD "Another truth, huh? Ok..."
        MD "My mom keeps talking about how her sister got a shameful new job after her husband went to jail, but she won't tell me what it is."
        MD "So tell me what that shameful new job is."
        R "Ok... but you can't tell anyone else, or Mom will kill me."
        MD "Yeah... I promise I won't tell anyone."
        if clubcounter >= 5:
            R "I guess you could call it a second job, she's gone quite a few times now..."
        if clubcounter >= 3:
            R "Well, she's only had to a go a few times, so I don't know if I would call it a new job..."
        if clubcounter == 0:
            R "Well, it's not a new job, she's only had to do the job one time, I've been able to make enough money on the side that she hasn't had to go back..."
            if sidney_spy:
                RT "{i}Well... And the time I couldn't find my money.{/i}"
            else:
                pass
        MD "So, what's the job?"
        R "Ok... well...."
        R "The Mafia guys we owe money to, own a strip club."
        R "And if we don't have enough money to make our weekly payment to them, then they let Mom pay it off by pole dancing and stripping in their club."
        MD "Wow! And you help to pay the Mafia debt each week so [mom_name] doesn't have to strip?"
        R "I try to."
        "{i}{b}\"Mandy's Respect +1\"{/b}{/i}"
        $ cousinrespect += 1
        MD "Have you ever seen her do it?"
        MDT "{i}I can just see her swinging on that pole.{/i}"
        "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
        $ cousinlibido += 1
        R "Do what?"
        MD "Strip, of course!"
        R "Yeah, the first night she... hey! You can't ask me any additional questions until I choose truth again."
        if daily_dare_counter >= 2:
            scene bg Dare78
            with dissolve
        else:
            scene bg Dare77
            with dissolve
        MD "Haha... Fair enough..."
        MD "I guess it's my turn, and I'll pick truth as well."
        R "Alright... Are you a virgin?"
        if daily_dare_counter >= 2:
            scene bg Dare31
            with dissolve
        else:
            scene bg Dare26
            with dissolve
        MD "Yes."
        R "Really?"
        if daily_dare_counter >= 2:
            scene bg Dare32
            with dissolve
        else:
            scene bg Dare27
            with dissolve
        MD "Why do you sound so surprised?"
        R "Uhhh... I guess, I mean, you seem so sexually open."
        if daily_dare_counter >= 2:
            scene bg Dare31
            with dissolve
        else:
            scene bg Dare26
            with dissolve
        MD "Yeah well, I probably wouldn't be a virgin if my overprotective mom wasn't always clam-jamming me."
        R "Clam-jamming?"
        MD "You know, like the female version of cockblock."
        R "Haha... Never heard that one."
        MD "Well... My mom's been pretty successful at keeping me out of situations where I could possibly get my cherry popped."
        MD "But I'm hoping to remedy that very soon."
        RT "{i}Is she hinting at something?{/i}"
        MD "Alright, your turn again."
        MD "Truth, or dare?"
        $ daily_truth_counter = 2
        $ safe_truth = True
        $ truth_told = 1
        jump truth_dare_menus
    if safest_truth == True:
        if daily_dare_counter >= 2:
            scene bg Dare31
            with dissolve
        else:
            scene bg Dare75
            with dissolve
        MD "Hmmm... ok, I think I have one."
        if most_attractive_counter == 1:
            MD "You already told me that you find [mom_name] the most attractive."
        if most_attractive_counter == 2:
            MD "You already told me that you find Sidney the most attractive."
        if most_attractive_counter == 3:
            MD "You already told me that you find Lauren the most attractive."
        if most_attractive_counter == 4:
            MD "You already told me that you find my mom the most attractive."
        MD "So what I want to know is... When was the last time you jacked off while thinking of her?"
        R "How do you know that I have?"
        MD "Well, have you?"
        R "Is that your question?"
        MD "No... I'll stick to the original, since I'm pretty sure that you have."
        R "...."
        R "I can't remember exactly, but I'm pretty sure it's been less than a week."
        if daily_dare_counter >= 2:
            scene bg Dare78
            with dissolve
        else:
            scene bg Dare09
            with dissolve
        MD "Haha... You pervert!"
        "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
        $ cousinlibido += 1
        if daily_dare_counter >= 2:
            scene bg Dare31
            with dissolve
        else:
            scene bg Dare75
            with dissolve
        MD "Ok, now do me."
        RT "{i}I wish!{/i}"
        R "Alright, truth, or dare?"
        MD "I'll pick truth."
        R "Ok..."
        R "When was the last time you masturbated thinking about someone from our family?"
        if daily_dare_counter >= 2:
            scene bg Dare76
            with dissolve
        else:
            scene bg Dare08
            with dissolve
        MD "It's been less than a week."
        R "Really?... Who?"
        MD "Sorry, you've already asked your question."
        R "Dammit!"
        RT "{i}Unless she's lesbian, or bisexual, which I wouldn't put past her, she's probably masturbated to me.{/i}"
        RT "{i}She did seem to be pretty interested in my cock when she and Lauren came into my room that morning.{/i}"
        MD "Alright, it's your turn.  Do you want truth, or dare?"
        $ daily_truth_counter = 1
        $ truth_told = 1
        jump truth_dare_menus
    else:
        if daily_dare_counter >= 2:
            scene bg Dare31
            with dissolve
        else:
            scene bg Dare75
            with dissolve
        MD "Hmmm... Ok, I have one.  Present company excluded, which member of your family do you think is the most sexy?"
        R "Of my family?... I don't find anyone in my family sexy!"
        RT "{i}Great cover [ryan]! She'll never expect the truth!{/i}"
        if daily_dare_counter >= 2:
            scene bg Dare31
            with dissolve
        else:
            scene bg Dare75
            with dissolve
        MD "I'm calling bullshit.  You're surrounded by drop-dead sexy girls, and you haven't noticed? Yeah, that's bullshit!"
        MD "So, spill it."
        R "Fine..."
        $ safest_truth = True
        $ truth_told = 1
        $ daily_truth_counter = 1
        RT "{i}Hmmm... Who do I find the most attractive?{/i}"
        menu:
            "Mom":
                $ most_attractive_counter = 1
            "Sidney":
                $ most_attractive_counter = 2
            "Lauren":
                $ most_attractive_counter = 3
            "Aunt Cami":
                $ most_attractive_counter = 4
            "Uncle Bobby":
                if daily_dare_counter >= 2:
                    scene bg Dare78
                    with dissolve
                else:
                    scene bg Dare09
                    with dissolve
                MD "Hahaha... You smartass!"
                MD "Now, tell the truth!"
                with dissolve
                menu:
                    "Mom":
                        $ most_attractive_counter = 1
                    "Sidney":
                        $ most_attractive_counter = 2
                    "Lauren":
                        $ most_attractive_counter = 3
                    "Aunt Cami":
                        $ most_attractive_counter = 4
        if daily_dare_counter >= 2:
            scene bg Dare76
            with dissolve
        else:
            scene bg Dare08
            with dissolve
        if most_attractive_counter == 1:
            MD "Your own mother, huh?..."
            MD "So you like your women more mature?"
            R "I just like her natural curves. She may be a little bit older, but she's aged really well."
            MD "She is really hot... More of a natural beauty, where my mom has a lot of plastic improvements."
            "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
            $ cousinlibido += 1
            R "Your mom is hot too, though."
            if daily_dare_counter >= 2:
                scene bg Dare32
                with dissolve
            else:
                scene bg Dare10
                with dissolve
            MD "Eeuuww... You just called your aunt hot!"
            if daily_dare_counter >= 2:
                scene bg Dare76
                with dissolve
            else:
                scene bg Dare08
                with dissolve
            R "But, you..."
            MD "Alright, it's my turn."
        if most_attractive_counter == 2:
            MD "Sidney, huh?..."
            MD "It's her ass, isn't it?"
            R "Well, it is pretty firm."
            R "She runs almost everyday.  She's in great shape."
            MD "I wish I had a bigger ass."
            R "What? No, your ass works great for your body type."
            MD "You like my ass?"
            R "Ummm... Is there a safe way to answer this question?"
            if daily_dare_counter >= 2:
                scene bg Dare78
                with dissolve
            else:
                scene bg Dare09
                with dissolve
            MD "Haha... You like your cousin's ass!"
            "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
            $ cousinlibido += 1
            if daily_dare_counter >= 2:
                scene bg Dare76
                with dissolve
            else:
                scene bg Dare08
                with dissolve
            MD "Pervert!"
            R "But, you..."
            MD "Alright, it's my turn."
        if most_attractive_counter == 3:
            MD "Lauren, huh?..."
            MD "You don't mind the itty-bitty titties?"
            R "No... I like a nice big set of breasts as much as the next guy, but there's something about little titties that really turns me on."
            MD "So you think my little mole hills are ok?"
            R "Yeah!... They're sexy as hell."
            if daily_dare_counter >= 2:
                scene bg Dare78
                with dissolve
            else:
                scene bg Dare09
                with dissolve
            MD "Haha... I'm your cousin, you pervert."
            "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
            $ cousinlibido += 1
            if daily_dare_counter >= 2:
                scene bg Dare76
                with dissolve
            else:
                scene bg Dare08
                with dissolve
            R "But, you..."
            MD "Alright, it's my turn."
        if most_attractive_counter == 4:
            if daily_dare_counter >= 2:
                scene bg Dare32
                with dissolve
            else:
                scene bg Dare10
                with dissolve
            MD "Eeuuww... Really?... My mom?"
            MD "But she's all plastic."
            R "I don't mind. The plastic surgeon did a great job."
            R "Plus, she keeps herself in really great shape."
            if daily_dare_counter >= 2:
                scene bg Dare31
                with dissolve
            else:
                scene bg Dare75
                with dissolve
            MD "Yeah, but I think she only does that because her self-esteem is so low."
            MD "I think she's really craving some attention since my dad left."
            RT "{i}Duly noted.{/i}"
            MD "I've never really thought of my mom as hot, but I guess I can see it."
            "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
            $ cousinlibido += 1
            MD "Alright, it's my turn."
            R "Do you want truth, or dare?"
            MD "Since you picked truth, I'm going to pick truth too."
            R "Ok... Are you attracted to anyone in our family?"
            MD "...."
            MD "Yes."
            R "Who?"
            MD "Nope, I already told my truth."
            R "Goddammit!"
            MD "You're not very good at this, are you?"
            MD "Now do you want truth, or dare?"
            jump truth_dare_menus

label safest_dare_sequence:             #### Edited ####
    MD "Kiss your sister's ass."
    $ reverse_cuz = False
    scene bg Dare14
    with fade
    R "Ok... but we have to agree, we won't tell Lauren about any of the dares we do that involve her in any way."
    MD "Yeah, obviously."
    R "Ok, just making sure."
    scene bg Dare13
    with dissolve
    $ renpy.pause ()
    MDT "{i}He looks so cute kissing his sister's ass, and why does the fact that it's his sister kinda turn me on?{/i}"
    MDT "{i}I'll bet I can get him to do a better kiss than that.{/i}"
    scene bg Dare14
    with dissolve
    R "Was that to your liking?"
    MD "Are you kidding me? That was the wussiest ass kiss I've ever seen."
    R "Have you seen a lot of ass kisses?"
    MD "Yes, and you've got to get deeper in the crack."
    RT "{i}Is she messing with me?{/i}"
    RT "{i}I would love to kiss Lauren there, and in front of Mandy, with her approval?{/i}"
    RT "{i}I can't resist.{/i}"
    R "Ok, like this?"
    scene bg Dare15
    with dissolve
    $ renpy.pause ()
    RT "{i}Oh... That is such a sexy smell!{/i}"
    MDT "{i}Oh, my God!... This is making me so wet!{/i}"
    "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
    $ cousinlibido += 1
    scene bg Dare14
    with dissolve
    R "Was that better?"
    MD "Uhhh... Ummm... much... better."
    RT "{i}Haha... I don't think she thought I would go through with it.  But from the look on her face, I think she liked it.{/i}"
    MD "Umm... Is it my turn?"
    R "Yeah, truth, or dare?"
    $ reverse_cuz = True
    scene bg Dare08
    with fade
    MD "I pick dare."
    R "I'm going to take things up a notch... I dare you to take off Lauren's shirt."
    scene bg Dare11
    with dissolve
    MD "Really?... You don't think she'll wake up?"
    R "No way. She is out for the night."
    scene bg Dare08
    with dissolve
    MD "Alright, but if she wakes up, I'm blaming this on you."
    R "Fair enough."
    MD "Ok..."
    scene bg Dare16
    with fade
    MD "Here goes."
    $ renpy.pause ()
    MDT "{i}Please don't wake up, please don't wake up, please don't wake up.{/i}"
    "{i}{b}\"Mandy's Submission +1\"{/b}{/i}"
    $ cousinsubmission += 1
    scene bg Dare17
    with fade
    MD "Wow! She barely stirred!"
    MD "I'm starting to think we can get away with anything involving her, and with that in mind, do you want truth, or dare?"
    if dare_counter == 0:
        $ dare_counter = 1
    $ daily_dare_counter += 1
    $ truth_told = 0
    jump truth_dare_menus

label safe_dare_sequence:               #### Edited ####
    if daily_dare_counter == 0:
        MD "Well, no point in wasting any time, let's just start the game out with Lauren already topless."
        scene bg SleepBlack
        with fade
        "{i}\"A few moments later.\"{/i}"
        scene bg Dare26
        with fade
    else:
        pass
    MD "Let me see... Oh, I have a good one."
    MD "Take off her panties."
    R "And leave her bare ass naked on the bed?"
    R "How will we explain things if she wakes up?"
    MD "I don't know... maybe just convince her she's having a dream."
    MD "But, you either do it, or you lose."
    R "Alright, I'm on it."
    $ reverse_cuz = False
    scene bg Dare21
    with fade
    RT "{i}Oh, my God! I'm taking off my sister's panties, and my cousin dared me to do it... Shit, my dick is rock hard now!{/i}"
    RT "{i}It won't be easy to hide a hardon in these small shorts.{/i}"
    if cousinlibido >= 8 or cousinsubmission >= 5:
        R "What?... I don't want to see my sister naked!"
        RT "{i}Why am I even trying anymore? She knows I'm lying.{/i}"
        R "But... I'll do it because it will make the next dares easier."
        scene bg SleepBlack
        with fade
        $ reverse_cuz = True
        scene bg Dare22
        with fade
        MDT "{i}I'm glad I'm not the only one in this house with tiny tits.{/i}"
        MDT "{i}They're actually pretty sexy on Lauren, maybe my tiny tits don't look so bad either.{/i}"
        RT "{i}Fuck! My cock is so hard... I can see everything!{/i}"
        MD "So... I guess it's my turn?"
        R "Oh yeah, do you want truth, or dare?"
        MD "I don't want to be outdone, so I'll pick dare too."
        R "Nice!"
        R "Cuz I've got a great one all ready for you."
        scene bg Dare25
        with dissolve
        MD "Oh no... maybe I should have chosen truth!"
        R "Haha... too late!"
        R "I dare you to press your naked tits against Lauren's naked tits."
        MD "Oh, yeah... I should have chosen truth."
        R "Ha... So do you give up?"
        scene bg Dare24
        with dissolve
        MD "Never!"
        scene bg Dare25
        with dissolve
        MD "Just give me a second."
        scene bg Dare28
        with fade
        MDT "{i}[ryan]'s about to see my tits!{/i}"
        MDT "{i}What if he doesn't like them?{/i}"
        MDT "{i}What if he thinks they're too small, or funny shaped, or my nipples are too puffy?{/i}"
        MDT "{i}This is the first time I've ever shown them to anybody up close.{/i}"
        scene bg Dare29
        with dissolve
        MDT "{i}Moment of truth.{/i}"
        R "Wow, Mandy!"
        R "I know this may be inappropriate, so don't take this the wrong way with me being your cousin and all, but those are some great tits."
        RT "{i}I didn't think it was possible for me to get any harder, and yet...{/i}"
        MD "You don't think they're too small?"
        R "Are you kidding? I love and respect all sizes of tits equally... well... almost equally."
        R "It really depends on the body they're attached to, and I love a slim body, so I think yours are fantastic."
        R "Ummm... in a non-weird, cousin way."
        MDT "{i}I think he really likes them!{/i}"
        "{i}{b}\"Mandy's Affection +1\"{/b}{/i}"
        $ cousinaffection += 1
        MD "Ok... I'm gonna do it."
        $ reverse_cuz = False
        scene bg Dare30
        with fade
        $ renpy.pause ()
        MDT "{i}Oh, my God! My breasts are pressed against another girl's!{/i}"
        MDT "{i}Not to mention they're my cousin's breasts!{/i}"
        "{i}{b}\"Mandy's Submission +1\"{/b}{/i}"
        $ cousinsubmission += 1
        RT "{i}I've got to control my thoughts, or I'm going to be dealing with some premature ejaculation.{/i}"
        $ reverse_cuz = True
        scene bg Dare31
        with fade
        MD "Oh, wow! I did it. That gave me butterflies."
        MD "I can't wait to get you back for that one!"
        MD "Now, do you want truth, or dare?"
        $ daily_dare_counter = 2
        $ truth_told = 0
        jump truth_dare_menus
    else:
        play music Honey
        MD "Oh, my God!"
        scene bg Dare27
        with fade
        MD "You really are a disgusting pervert."
        R "But you're the one that..."
        MD "She's your sister, for God's sake!"
        R "Hey! You're the one who gave the dare!"
        MD "Yeah, because I wanted to win, I never thought you would ever take it so far with your own sister!"
        "{i}{b}\"Mandy's Anger +2\"{/b}{/i}"
        $ cousinanger += 2
        MD "Let's just call it a night."
        hide screen Points_screen_Cuz_dare
        MD "I'm not really sure if I'll be in the mood to play tomorrow night, maybe if you do something to make it up to me."
        MD "Otherwise, maybe you can come back the next night, or even later."
        MD "I think I'm just going to need a little time to get over that."
        scene bg SleepBlack
        with fade
        scene bg LaurenDoorNight
        with fade
        RT "{i}Shit! Why did I push it so far? I should have read the room better.{/i}"
        RT "{i}I need to make sure she is more submissive or horny before I try to push things that far.{/i}"
        RT "{i}I always have the option to quit the game if I think she's at her limit.{/i}"
        RT "{i}I'd better give her a few days before I come back, or I could buy her something from Hardnlong.com to cheer her up.{/i}"
        $ lauren_door_locked = True
        $ screen_on = "laurendoornightmap"
        call screen laurendoornightmap

label s_risk_dare_sequence:             #### Edited ####
    if daily_dare_counter <= 1:
        MD "Well, no point in wasting any dares, let's just jump to where we left off, with Lauren naked, and I believe I was topless?"
        R "Yeah... I think so... No complaints here."
        scene bg SleepBlack
        with fade
        "{i}\"A few moments later.\"{/i}"
        scene bg Dare31
        with fade
    else:
        pass
    MD "Good choice."
    MD "Ok, you're the only one here not showing anything, so why don't you get naked."
    RT "Shit! I was afraid of this one. I'm pitching a circus-sized tent, and now I'm going to have to reveal how horny I am."
    R "I only made you take of your top. Shouldn't I get a dare to take off just my top too?"
    MD "You're thinking of strip poker, dummy!"
    MD "In \"Truth, or dare\", you have to complete the dare you're given, or lose."
    if cousinsubmission >= 8 or cousinlibido >= 9:
        MD "But... since it's late, and because I want to get to the more interesting dares... I'll go ahead and strip my bottoms off too."
        R "Oh, my God! Are you serious?"
        MD "Pretty serious. See?"
        scene bg Dare33
        with fade
        $ renpy.pause ()
        RT "{i}Wow!... What's this girl planning for the more interesting dares?{/i}"
        scene bg Dare31
        with fade
        MD "Alright, now get your clothes off if you want to stay in this game."
        RT "{i}Goddammit. How's Mandy going to react when she realizes I'm harder than diamonds?{/i}"
        RT "{i}I Guess I'm about to find out.{/i}"
        scene bg Dare34
        with fade
        $ renpy.pause ()
        RT "{i}Moment of truth.{/i}"
        scene bg Dare35
        with fade
        MDT "{i}Holy shit!... He's huge!... That's even bigger than I remembered.{/i}"
        MDT "{i}Fuck! Why am I turned on so bad by my own cousin?{/i}"
        MDT "{i}Shit! I'm starting to get wet. I'd better not drip anything onto the bedspread... That would be as obvious as his boner.{/i}"
        scene bg Dare76
        with fade
        MD "I can't believe you're that horny from your own cousin and sister."
        R "It's not my fault, havent you ever heard of NRB's?"
        MD "No, what's that?"
        R "It stands for \"no reason boner\"."
        scene bg Dare78
        with dissolve
        MD "Well, when we're both sitting here naked, it's hard to believe there's not a reason."
        R "Well, so what if there is a reason, how the hell am I supposed to control my dick when there's two naked chicks in front of me."
        MD "Haha... Fair point."
        R "And now that we're both naked, I believe it's your turn."
        R "Do you want truth, or dare?"
        MD "Ooo... give me a good dare."
        R "A good one huh?"
        R "Alright, I dare you to suck on Lauren's titty for 10 seconds."
        scene bg Dare36
        with fade
        MD "Suck her titty? Damn, I hope she doesn't wake up."
        R "She hasn't stirred. I think as long as you don't pinch her, she'll sleep through anything."
        MD "Alright... I'm gonna do it."
        scene bg Dare40
        with fade
        MD "Don't you dare take a picture of this."
        R "Don't worry, I'm just taking mental pictures."
        MD "Haha... You pervert."
        MD "Here goes."
        scene bg Dare41
        with dissolve
        MD "Mmmmm..."
        R "Oh, do you want me to count?"
        MD "MMMmmm..."
        R "Ok,... One... Two... Three... Four... Five..."
        scene bg Dare42
        with dissolve
        L "Mmmmmmmm..."
        scene bg Dare43
        with dissolve
        MD "Oh, fuck! Did you hear that?"
        R "Haha... Yeah... I think she's enjoying it."
        MD "I can't keep sucking on her titty if she's liking it... can I?"
        R "Why not?"
        MD "I don't know."
        R "You've got five seconds left to suck, but you can always give up and declare me the winner."
        MD "No way..."
        scene bg Dare40
        with dissolve
        MD "It's just kind of weird, knowing she's asleep, but she's enjoying it."
        R "Do you think she's dreaming about you sucking on her nipples?"
        RT "{i}I hope she's dreaming that I'm the one sucking them.{/i}"
        MD "No, she's probably dreaming about this boy she likes."
        R "Who?"
        MD "I don't know, she won't tell me, which is weird, cuz usually she'll tell me those kinds of things."
        RT "{i}Huh... could she really like me?{/i}"
        MD "Ok... five more seconds."
        MD "Don't forget to count."
        scene bg Dare41
        with dissolve
        "{i}{b}\"Mandy's Submission +1\"{/b}{/i}"
        $ cousinsubmission += 1
        R "One... Two..."
        scene bg Dare42
        with dissolve
        L "MMmmmm..."
        MDT "{i}Goddammit, Lauren.{/i}"
        RT "{i}Awesome!{/i}"
        R "Three... Four... Five!"
        scene bg Dare43
        with dissolve
        MD "What a horndog!"
        R "Hahahaha..."
        scene bg Dare78
        with fade
        MD "Stop laughing!..."
        MD "It's your turn."
        MD "Truth, or dare?"
        $ daily_dare_counter = 3
        $ truth_told = 0
        jump truth_dare_menus
    else:
        R "Ok, fine."
        RT "{i}How's Mandy going to react when she realizes how horny I am?{/i}"
        scene bg SleepBlack
        with fade
        scene bg Dare34
        with fade
        $ renpy.pause ()
        RT "{i}Moment of truth.{/i}"
        scene bg Dare35
        with fade
        MDT "Oh my Lord, he's huge... And why is he so hard?"
        scene bg Dare32
        with dissolve
        play music Honey
        MD "What the fuck, [ryan]?"
        MD "Are you really that horny over your own cousin and sister?"
        MD "My God, do you have any self-control?"
        R "It's not my fault, havent you ever heard of NRB's?"
        MD "No, what's that?"
        R "It stands for \"no reason boner\"."
        MD "Well, when we're both sitting here naked, it's hard to believe there's not a reason."
        R "Well, so what if there is a reason, how the hell am I supposed to control my dick when there's two naked chicks in front of me."
        MD "You try your Goddamned best, that's how."
        MD "That's it for tonight, I can't play anymore."
        "{i}{b}\"Mandy's Anger +5\"{/b}{/i}"
        $ cousinanger += 5
        hide screen Points_screen_Cuz_dare
        MD "I'm not really sure if I'll be in the mood to play tomorrow night, maybe if you do something to make it up to me."
        MD "Otherwise, maybe you can come back the next night, or even later."
        MD "I think I'm just going to need a little time to get over that."
        scene bg SleepBlack
        with fade
        scene bg LaurenDoorNight
        with fade
        RT "{i}Shit! Why did I push it so far? I should have read the room better.{/i}"
        RT "{i}I need to make sure she is more submissive or horny before I try to push things that far.{/i}"
        RT "{i}I always have the option to quit the game if I think she's at her limit.{/i}"
        RT "{i}I'd better give her a few days before I come back, or I could buy her something from Hardnlong.com to cheer her up.{/i}"
        $ lauren_door_locked = True
        $ screen_on = "laurendoornightmap"
        call screen laurendoornightmap

label risky_dare_sequence:              #### Edited ####
    if daily_dare_counter <= 2:
        MD "Well, no point in wasting any dares, let's just jump to where we left off, we've got to strip Lauren and ourselves."
        R "Yeah... No complaints here."
        scene bg SleepBlack
        with fade
        "{i}\"A few moments later.\"{/i}"
        scene bg Dare31
        with fade
    else:
        pass
    scene bg Dare78
    with dissolve
    MD "Ok, I've got a funny one for you."
    MD "I dare you to give Lauren a penis mustache."
    R "A penis mustache?... What the hell is that?"
    MD "It's exactly what it sounds like."
    R "Ummm... Ok."
    scene bg SleepBlack
    with fade
    R "So I just put my penis under her nose like this?"
    scene bg Dare44
    with fade
    $ renpy.pause ()
    if cousinsubmission >= 12:
        MD "Kind of, but you got to really get it under her nose like this."
        scene bg Dare45
        with dissolve
        RT "{i}Oh, my God! Mandy just grabbed my cock!{/i}"
        MDT "{i}Did I really just grab his cock?{/i}"
        scene bg Dare46
        with fade
        MD "See... You're too far away.  You've really got to get it under her nose."
        MD "Like this."
        scene bg Dare47
        with dissolve
        MD "Haha... Look... Now she's got a penis mustache."
        R "You're so weird... But I've got to admit... That's kind of funny."
        RT "{i}And kind of hot that my penis is touching Lauren's lips.{/i}"
        scene bg SleepBlack
        with fade
        scene bg Dare31
        with fade
        MD "I guess it's my turn?"
        R "Yep, and let me just give you a warning about choosing dare.  You really upped the ante when you had me put my cock in my sister's face."
        scene bg Dare78
        with dissolve
        MD "Ooooo... A warning, huh?... I look at a warning as more of a challenge."
        MD "Bring on \"The Dare\"."
        R "You asked for it."
        R "I dare you to lick Lauren's pussy for ten seconds."
        scene bg Dare76
        with dissolve
        MD "What?... That's... Not even close to what I did to you."
        R "What do you mean?"
        R "You made me put my genitals in Lauren's face, and now I'm daring you to put her genitals into your face."
        MD "Yeah, but you're also making me lick them.  Genitals in the face and genitals in the mouth are very different."
        R "I'd say it's the next natural step in our game."
        MD "Hmmmm...."
        R "You can always admit defeat, and declare me the winner."
        MD "No... I can do this."
        scene bg SleepBlack
        with fade
        MD "There's not much room for me right in front of her."
        MD "I think the only way to make this work is to get under her like this."
        R "Just don't wake her."
        scene bg Dare48
        with fade
        MD "I made it... I can't believe she slept through that."
        R "Great... You're in the perfect position to give her a good licking."
        R "For ten seconds."
        scene bg Dare49
        with dissolve
        MD "What is it with you, and doing things for ten seconds?"
        R "You can lick longer if you'd like."
        scene bg Dare48
        with dissolve
        MD "You're such a smartass."
        MD "Here I go."
        MD "Oh... And don't forget to count."
        scene bg Dare50
        with dissolve
        R "One... Two... Three..."
        scene bg Dare51
        with dissolve
        L "Ooohhh..."
        scene bg Dare49
        with dissolve
        MD "{i}(whispering){/i} Fuck!... She's doing it again!"
        R "That doesn't mean you get to stop."
        R "She's not waking up, is she?"
        MD "Well... No... But...."
        R "But, nothing, get back to licking."
        R "Unless you want to concede defeat."
        MD "Fine!"
        "{i}{b}\"Mandy's Submission +1\"{/b}{/i}"
        $ cousinsubmission += 1
        scene bg Dare50
        with dissolve
        R "Four... Five..."
        scene bg Dare51
        with dissolve
        L "Ooohhh..."
        R "Six... Seven..."
        L "MMMmmmmm..."
        R "Eight... nine..."
        L "Aaaahhh..."
        R "Ten!"
        scene bg Dare53
        with dissolve
        MD "Holy shit!"
        MD "I was worried she was going to have an orgasm!"
        RT "{i}You're lucky she didn't, or you'd be soaking wet.{/i}"
        R "Haha... I wonder what she's dreaming about."
        scene bg Dare52
        with dissolve
        MD "I don't know, but I'm sure her dreams are very pleasant."
        MD "Now, you'd better choose dare, because I'm ready to get revenge on you for that one."
        R "Hmmm... Well, in that case I'd better choose..."
        $ truth_told = 0
        $ daily_dare_counter = 4
        jump truth_dare_menus
    else:
        scene bg SleepBlack
        with fade
        scene bg Dare32
        with fade
        play music Honey
        MD "Oh, my God! I can't even believe you just stuck your dick in your sister's face!"
        RT "You're the one who dared me to do it!"
        MD "Yeah... Only because I wanted to win!... I never thought you would actually do it!"
        MD "You really are a huge pervert."
        MD "So, at least you can pat yourself on the back for winning the game, but now I think you should leave."
        "{i}{b}\"Mandy's Anger +5\"{/b}{/i}"
        $ cousinanger += 5
        hide screen Points_screen_Cuz_dare
        MD "I'm not really sure if I'll be in the mood to play tomorrow night, maybe if you do something to make it up to me."
        MD "Otherwise, maybe you can come back the next night, or even later."
        MD "I think I'm just going to need a little time to get over that."
        scene bg SleepBlack
        with fade
        scene bg LaurenDoorNight
        with fade
        RT "{i}Shit! Why did I push it so far? I should have read the room better.{/i}"
        RT "{i}I need to make sure she is more submissive or horny before I try to push things that far.{/i}"
        RT "{i}I always have the option to quit the game if I think she's at her limit.{/i}"
        RT "{i}I'd better give her a few days before I come back, or I could buy her something from Hardnlong.com to cheer her up.{/i}"
        $ lauren_door_locked = True
        $ screen_on = "laurendoornightmap"
        call screen laurendoornightmap

label v_risky_dare_sequence:            #### Edited ####
    if not v_risky_truth and cousinsubmission >= 17:
        scene bg Dare76
        with fade
        MD "Before I give you this dare, there's something kind of serious I want to talk to you about."
        R "Really?"
        MD "Yeah... I was hoping you were going to pick truth so I could ask you, but you didn't, so I want to ask you this question outside of our game."
        MD "So what I want to know is... Are you trying to fuck my mom?"
        R "Pfff... What!?"
        scene bg Dare52
        with dissolve
        MD "No... it's an honest question... And I'm genuinely curious."
        R "I can't believe you're asking me that!"
        MD "It's a simple question."
        R "Why would you want to know that?"
        scene bg Dare54
        with dissolve
        MD "I don't know..."
        MD "Well... Actually I do."
        MD "I'm still shocked that such a prude bitch would flash you her tits for money, so if she's willing to do that, then she'd probably be willing to do more for even more money."
        MD "I haven't confronted her about flashing you yet, so I'll keep that between us. But I want to help you to make my mom into even more of a slut."
        RT "{i}Oh, my God! I think Mandy's flipped as hard as I have!{/i}"
        R "Why would you want to do that to your own mom?"
        MD "You have no idea what it was like to be raised by that so-called \"sexually pure\" woman."
        MD "She's been so protective and controlling of me my entire life."
        MD "And while her flashing you takes her down a peg, if she got fucked by her own nephew, and I had proof... that would take her down like 100 pegs, and she'd never have room to lecture or control me again."
        R "Wow! You must really hate your mom."
        MD "Actually, I really love her. But I hate living under her thumb."
        MD "And If anybody's going to bring my mom down in this way, I would feel much safer if it was you."
        RT "{i}My God! I can't belive we're having this conversation.{/i}"
        MD "So I ask you again, aside from this game..."
        MD "Do you have any intentions of fucking my mom?"
        R "Honestly, I was just having a little fun with her before."
        R "But after what you just told me... I suppose I could put some effort into doing... that."
        scene bg Dare53
        with dissolve
        MD "Awesome!"
        scene bg Dare52
        with dissolve
        MD "But, it's not going to be easy."
        MD "And it might be kind of expensive."
        R "Shit! It's not like I have a humongous Mafia debt to pay or anything."
        scene bg Dare54
        with dissolve
        MD "Hmmm... Is there any way I could help make more money?"
        R "Well... Would you be willing to be in another photoshoot?"
        R "Maybe even be willing to shoot some risqué shots with another girl?"
        scene bg Dare53
        with dissolve
        MD "YES!"
        scene bg Dare52
        with dissolve
        MD "I mean... sure... if you think it would help."
        MD "And we could use the proceeds of the shoot to buy my mom's sluttiness?"
        MDT "{i}My mom's going to be the biggest slut in the family!... Then I'll be able to get away with anything!{/i}"
        MDT "{i}Can we really get her to fuck her own nephew?{/i}"
        MDT "{i}My God! That would be crazy!{/i}"
        "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
        $ cousinlibido += 1
        R "I'll make sure those funds are used specifically for that."
        MD "I can't wait!"
        RT "{i}She's just as corrupt and manipulative as I am.{/i}"
        RT "{i}Must be a common symptom of having your life fucked up my the Mafia.{/i}"
        MD "Ok... We can get back to the game."
        scene bg Dare31
        with dissolve
        $ v_risky_truth = True
    else:
        pass
    if daily_truth_counter == 5:
        scene bg Dare52
        with fade
    else:
        scene bg Dare31
        with fade
    MD "Alright, this one is going to be a doozy."
    MD "I dare you to rub your cock on Lauren's pussy."
    R "What?... You weren't kidding... That is a doozy."
    MD "Yeah, I'd say we are about to that part in our game."
    MD "So are you going to do it? Or are you going to chicken out?"
    R "...."
    R "Ok... I'm gonna go for it."
    hide screen Points_screen_Cuz_dare
    scene bg Dare56
    with fade
    R "Do you mean like this?"
    if cousinsubmission >= 17:
        MD "Exactly!... Now you've got to rub your cock back and forth on her pussy."
        R "Like this?"
        scene DareVideo01
        with fade
        $ renpy.pause ()
        MD "I actually meant for you to rub it forward and back."
        scene DareVideo02
        with fade
        $ renpy.pause ()
        R "Is this better?"
        MD "Exactly..."
        R "For how long?"
        MD "I don't know... Until it feels good."
        R "...."
        MD "Wait... I've got a really good idea."
        scene bg Dare57
        with dissolve
        MD "How does it feel when I hold her legs together like this?"
        R "Holy shit! It feels so good."
        R "If I keep rubbing, I'm going to cum."
        MD "Go for it!"
        R "What?"
        MD "Just keep rubbing until you cum."
        R "Are you kidding me?"
        MD "You know you want to."
        R "Yeah but, I can't cum on my sister."
        MD "I'm not going to tell her..."
        MD "And if you don't tell her, it will be our little secret."
        MD "I know you want to."
        RT "{i}Of course I want to... but I need to at least pretend I dont... don't I?{/i}"
        R "Ok... You make a good argument."
        scene DareVideo03
        with fade
        $ renpy.pause ()
        MDT "{i}Fuck, that's hot!{/i}"
        "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
        $ cousinlibido += 1
        play sound Lauren01 loop
        MD "Does it feel like you're really fucking her?"
        R "Uhhh... I don't know... it feels really good though..."
        MD "Haha... Lauren sounds like she's getting into it."
        MD "Are you about to cum?"
        R "Yes..."
        MD "Just go for it!"
        R "Fuck!"
        stop sound
        play sound Ejaculate
        scene bg Dare58
        with dissolve
        with vpunch
        with hpunch
        $ renpy.pause ()
        play sound Ejaculate
        scene bg Dare59
        with dissolve
        with vpunch
        with hpunch
        $ renpy.pause ()
        scene bg Dare60
        with dissolve
        MD "Oh, my God!"
        scene bg Dare61
        with fade
        MD "That is so much cum!"
        MD "I mean I've watched a good amount of porn lately, but I've never seen anybody cum this much."
        R "Thanks?... I guess..."
        scene bg Dare62
        with dissolve
        MD "It would probably really turn me on if I weren't your cousin."
        "{i}{b}\"Mandy's Libido +1\"{/b}{/i}"
        $ cousinlibido += 1
        R "Yeah, I'd better clean that up."
        MD "No, you'd better get out of here. She was doing quite a bit of moaning. She might wake up any minute."
        R "But..."
        MD "Don't worry. I'll clean it all up."
        R "And our game?"
        MD "Congratulations! You won."
        MD "Now get your clothes on, and hurry and get out of here!"
        R "Alright... I'm going."
        scene bg SleepBlack
        with fade
        scene bg LaurenDoorNight
        with fade
        RT "{i}Mandy was in a little too much of a hurry to get me out of there... Something seems fishy.{/i}"
        RT "{i}I think I'll just take a quick peek to see if something's up.{/i}"
        scene bg Dare80
        with dissolve
        RT "{i}Fuck! Is Mandy on top of Lauren?{/i}"
        scene bg Dare74
        with fade
        RT "{i}What in the hell is she doing?{/i}"
        scene bg Dare63
        with fade
        MDT "{i}Well look at you, Lauren!{/i}"
        MDT "{i}All covered in your brother's cum!... What a naughty girl...{/i}"
        MDT "{i}This is the first time I've ever seen cum!{/i}"
        MDT "{i}The girls on porn always eat it.{/i}"
        MDT "{i}I wonder if it's any good.{/i}"
        scene bg Dare64
        with fade
        MDT "{i}Oh, my God! I'm eating cum... {/i}"
        scene bg Dare65
        with fade
        MDT "{i}Uuugghh... I don't like the taste of that at all.{/i}"
        MDT "{i}I'm not eating any more of that... I better run to the bathroom to get some toilet paper to finish cleaning it up.{/i}"
        RT "{i}Shit! She's coming out... I've got to book it!{/i}"
        scene bg SleepBlack
        with fade
        RT "{i}Holy shit, that was close.  I'm glad I was able to find my way to my room so quickly in the dark.{/i}"
        RT "{i}I can't believe Mandy licked up some of my cum!{/i}"
        RT "{i}I can't believe anything that happened in that room!{/i}"
        RT "{i}And for once it wasn't just me pushing things to happen.{/i}"
        RT "{i}I think Mandy is my female counterpart.{/i}"
        RT "{i}I'll have to go back and see if she'll push it even farther next time.{/i}"
        $ persistent.gal_harem_3 = True
        $ truth_dare_completed = True
        play music Honey
        jump myroom
    else:
        scene bg Dare32
        with fade
        MD "Dude, [ryan]! What the hell?"
        R "Huh?..."
        play music Honey
        MD "I can't believe you were rubbing your dick on your own sister's pussy!"
        R "But... You dared me to do it!"
        MD "Yeah... Only because I wanted to win!... I never thought you would actually do it!"
        MD "You really are a huge pervert."
        MD "So, at least you can pat yourself on the back for winning the game, but now I think you should leave."
        "{i}{b}\"Mandy's Anger +5\"{/b}{/i}"
        $ cousinanger += 5
        hide screen Points_screen_Cuz_dare
        MD "I'm not really sure if I'll be in the mood to play tomorrow night, maybe if you do something to make it up to me."
        MD "Otherwise, maybe you can come back the next night, or even later."
        MD "I think I'm just going to need a little time to get over that."
        scene bg SleepBlack
        with fade
        scene bg LaurenDoorNight
        with fade
        RT "{i}Shit! Why did I push it so far? I should have read the room better.{/i}"
        RT "{i}I need to make sure she is more submissive or horny before I try to push things that far.{/i}"
        RT "{i}I always have the option to quit the game if I think she's at her limit.{/i}"
        RT "{i}I'd better give her a few days before I come back, or I could buy her something from Hardnlong.com to cheer her up.{/i}"
        $ lauren_door_locked = True
        $ screen_on = "laurendoornightmap"
        call screen laurendoornightmap

label quit_dare:                        #### Edited ####
    if daily_dare_counter >= 2:
        scene bg Dare31
        with dissolve
    else:
        scene bg Dare26
        with dissolve
    R "Actually, I'm going to have to call it for the night."
    hide screen Points_screen_Cuz_dare
    MD "What?... Why?"
    R "Well, I've got to be up early in the morning, and I've got a pretty full day."
    R "But mostly, I think that neither of us are ready for where this game is going next."
    R "So I hereby declare you the winner."
    MD "Alright, you're watching out for both of us... I can respect that."
    "{i}{b}\"Mandy's Respect +1\"{/b}{/i}"
    $ cousinrespect += 1
    MD "But if you want a rematch, I'll be waiting here every night."
    MD "And maybe one of these times, we can get Lauren to be a conscious, willing participant."
    R "Haha... I wouldn't bet on it."
    RT "{i}At least until that tea runs out.{/i}"
    R "Alright, goodnight Mandy."
    MD "Goodnight [ryan]."
    scene bg SleepBlack
    with fade
    play music Honey
    $ lauren_door_locked = True
    $ screen_on = "laurendoornightmap"
    call screen laurendoornightmap

label t_d_thighs:                       #### Edited ####
    play sound Lauren01 loop
    scene DareVideo03
    with fade
    $ renpy.pause ()
    MD "Are you sure my hand doesn't feel better?"
    menu:
        "Mandy Handjob":
            stop sound
            jump t_d_hj
        "Cum":
            jump cum_thighs

label t_d_hj:                           #### Edited ####
    scene DareVideo04
    with fade
    $ renpy.pause ()
    MD "Cum all over your sister!"
    menu:
        "Fuck Lauren's thighs":
            jump t_d_thighs
        "Cum":
            jump cum_hj

label cum_hj:                           #### Edited ####
    R "Oh, God! Here I go!"
    play sound Ejaculate
    scene bg Dare71
    with dissolve
    with vpunch
    with hpunch
    $ renpy.pause ()
    play sound Ejaculate
    scene bg Dare72
    with dissolve
    with vpunch
    with hpunch
    $ renpy.pause ()
    scene bg Dare73
    with dissolve
    MD "You dirty boy! You just came all over your sister!"
    MD "You came so... so... much!"
    R "Yeah... I'd better get it cleaned up."
    MD "You'd better get out of here quickly before she wakes up."
    MD "That much cum to the chest could wake up anyone."
    MD "Don't worry about anything.  I'll get her all cleaned up."
    R "Are you sure?"
    MD "Yes... Positive... Now hurry and get out of here."
    MDT "{i}While your cum is still warm.{/i}"
    scene bg SleepBlack
    with fade
    scene bg LaurenDoorNight
    with fade
    RT "{i}Mandy was in a hurry to get me out of there... Is she going to eat my cum again?{/i}"
    RT "{i}I think I'll just take a quick peek to see if something's up.{/i}"
    scene bg Dare80
    with dissolve
    RT "{i}Mandy's on top of Lauren again.{/i}"
    scene bg Dare74
    with fade
    RT "{i}She must have enjoyed it last time.{/i}"
    scene bg Dare63
    with fade
    MDT "{i}Well look at you, Lauren!{/i}"
    MDT "{i}All covered in your brother's cum!... What a naughty girl...{/i}"
    MDT "{i}Look at it glistening all over her chest!{/i}"
    MDT "{i}The girls on porn must acquire a taste for it.{/i}"
    MDT "{i}I wonder if I could?{/i}"
    scene bg Dare64
    with fade
    MDT "{i}Oh, my God! I'm eating [ryan]'s cum again!... {/i}"
    "{i}\"Mandy's Lidido +3\"{/i}"
    $ cousinlibido += 3
    scene bg Dare66
    with fade
    if mandy_first_hj == False:
        MDT "{i}Hmmmm... it doesn't seem too bad the second time around.{/i}"
        MDT "{i}I think I just needed to get over the yuk factor.{/i}"
        scene bg Dare67
        with dissolve
        MDT "{i}I swallowed it!{/i}"
    else:
        MDT "{i}Yeah... I think I'm acquiring a taste for it.{/i}"
        scene bg Dare67
        with dissolve
        MDT "{i}It was even smooth going down.{/i}"
    MDT "{i}I might as well finish it.{/i}"
    scene bg Dare68
    with dissolve
    $ renpy.pause ()
    scene bg Dare69
    with dissolve
    MDT "{i}I got it all!{/i}"
    MDT "{i}I'm becoming a real cumslut!{/i}"
    scene bg SleepBlack
    with fade
    RT "{i}I can't believe Mandy licked up all of my cum!{/i}"
    RT "{i}What a cumslut!{/i}"
    RT "{i}I'll have to go back again very soon!{/i}"
    play music Honey
    $ mandy_first_hj = True
    jump myroom

label cum_thighs:                       #### Edited ####
    R "Oh, God! Here I go!"
    stop sound
    play sound Ejaculate
    scene bg Dare58
    with dissolve
    with vpunch
    with hpunch
    $ renpy.pause ()
    play sound Ejaculate
    scene bg Dare59
    with dissolve
    with vpunch
    with hpunch
    $ renpy.pause ()
    scene bg Dare60
    with dissolve
    MD "You dirty boy! You just came all over your sister!"
    MD "You came so... so... much!"
    R "Yeah... I'd better get it cleaned up."
    MD "You'd better get out of here quickly before she wakes up."
    MD "That much cum to the chest could wake up anyone."
    MD "Don't worry about anything.  I'll get her all cleaned up."
    R "Are you sure?"
    MD "Yes... Positive... Now hurry and get out of here."
    MDT "{i}While your cum is still warm.{/i}"
    scene bg SleepBlack
    with fade
    scene bg LaurenDoorNight
    with fade
    RT "{i}Mandy was in a hurry to get me out of there... Is she going to eat my cum again?{/i}"
    RT "{i}I think I'll just take a quick peek to see if something's up.{/i}"
    scene bg Dare80
    with dissolve
    RT "{i}Mandy's on top of Lauren again.{/i}"
    scene bg Dare74
    with fade
    RT "{i}She must have enjoyed it last time.{/i}"
    scene bg Dare63
    with fade
    MDT "{i}Well look at you, Lauren!{/i}"
    MDT "{i}All covered in your brother's cum!... What a naughty girl...{/i}"
    MDT "{i}Look at it glistening all over her chest!{/i}"
    MDT "{i}The girls on porn must acquire a taste for it.{/i}"
    MDT "{i}I wonder if I could.{/i}"
    scene bg Dare64
    with fade
    MDT "{i}Oh, my God! I'm eating cum again!... {/i}"
    scene bg Dare66
    with fade
    if mandy_first_hj == False:
        MDT "{i}Hmmmm... it doesn't seem too bad the second time around.{/i}"
        MDT "{i}I think I just needed to get over the yuk factor.{/i}"
        scene bg Dare67
        with dissolve
        MDT "{i}I swallowed it!{/i}"
    else:
        MDT "{i}Yeah... I think I'm acquiring a taste for it.{/i}"
        scene bg Dare67
        with dissolve
        MDT "{i}It was even smooth going down.{/i}"
    MDT "{i}I might as well finish it.{/i}"
    scene bg Dare68
    with dissolve
    $ renpy.pause ()
    scene bg Dare69
    with dissolve
    MDT "I got it all!"
    MDT "I'm becoming a real cumslut!"
    "{i}\"Mandy's Lidido +3\"{/i}"
    $ cousinlibido += 3
    scene bg SleepBlack
    with fade
    RT "{i}I can't believe Mandy licked up all of my cum!{/i}"
    RT "{i}What a cumslut!{/i}"
    RT "{i}I'll have to go back again very soon!{/i}"
    play music Honey
    $ mandy_first_hj = True
    jump myroom

label mandy_angry:                      #### Edited 9-2-2020 ####
    if timeofdaycounter == 5:
        while spycaminlaurenroom == True:
            scene bg LaurenDoorNight
            with fade
            RT "{i}The door is locked! Mandy must still be pissed off.{/i}"
            menu:
                "Take a peek.":
                    jump mandyspycamroommad
                "Never mind.":
                    $ screen_on = "laurendoornightmap"
                    call screen laurendoornightmap
        if timeofdaycounter == 5:
            scene bg LaurenDoorNight
            with fade
            RT "{i}She locked her door! Mandy must still be pissed off. I guess I better just let them sleep.{/i}"
            $ screen_on = "laurendoornightmap"
            call screen laurendoornightmap
    else:
        scene bg LaurenDoor
        RT "{i}The door's locked. Mandy's pretty pissed off at me.{/i}"
        menu:
            "Knock":
                scene bg MandyRoomMad01
                with fade
                MD "What do you want, jerk?"
                menu:
                    "Give her a gift":
                        if gavecuzgift == False:
                            scene bg MandyRoomMad02
                            with dissolve
                            MD "You have something for me?"
                            menu:
                                "Give her a chocolate bar" if inventory.inv_amount(chocolate) >= 1:
                                    scene bg MandyRoomMad04
                                    with dissolve
                                    MD "Thank you, I love chocolate!"
                                    "{i}{b}\"Mandy's Anger -2\"{/b}{/i}"
                                    $ cousinanger -= 2
                                    $ inventory.drop(chocolate)
                                    $ gavecuzgift = True
                                    if cousinanger >= 1:
                                        scene bg MandyRoomMad03
                                        with dissolve
                                        MD "But this doesn't mean I'm not mad at you anymore. You acted like a jerk, and it's going to take me some more time to forgive you."
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap
                                    else:
                                        scene bg MandyRoomMad04
                                        MD "Thank you, [ryan]! It's hard to stay mad for very long at someone as sweet as you!"
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap
                                "Give her Hardnlong gift card" if inventory.inv_amount(giftcard) >= 1:
                                    scene bg MandyRoomMad04
                                    with dissolve
                                    MD "Thank you! I'm going to use it right now!"
                                    "{i}{b}\"Mandy's Anger -5\"{/b}{/i}"
                                    $ cousinanger -= 5
                                    $ inventory.drop(giftcard)
                                    $ gavecuzgift = True
                                    if cousinanger >= 1:
                                        scene bg MandyRoomMad03
                                        with dissolve
                                        MD "But this doesn't mean I'm not mad at you anymore. You acted like a jerk, and it's going to take me some more time to forgive you."
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap
                                    else:
                                        scene bg MandyRoomMad04
                                        MD "Thank you, [ryan]! It's hard to stay mad for very long at someone as sweet as you!"
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap
                                "Give her flowers" if inventory.inv_amount(flowers) >= 1:
                                    $ inventory.drop(flowers)
                                    if cousinaffection <= 50:
                                        scene bg MandyRoomMad03
                                        with dissolve
                                        MD "What the hell are you thinking? I'm not your girlfriend!"
                                        "{i}\"Throws them in the trash\"{/i}"
                                        MD "You're so weird sometimes!"
                                        MD "Maybe next time, try to think of something a little less creepy."
                                        "{i}{b}\"Mandy's Affection -1\"{/b}{/i}"
                                        "{i}{b}\"Mandy's Anger +2\"{/b}{/i}"
                                        "{i}\"You need higher affection to gift flowers.\"{/i}"
                                        $ cousinanger += 1
                                        $ cousinaffection -= 1
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap
                                    else:
                                        scene bg MandyRoomMad04
                                        with dissolve
                                        MD "Oh my gosh! I love them!"
                                        MD "You're so sweet!"
                                        MD "If I didn't know any better, I would think you were trying to put the moves on me!"
                                        $ cousinanger = 0
                                        $ cousinaffection += 1
                                        "{i}{b}\"Mandy's Anger -10\"{/b}{/i}"
                                        "{i}{b}\"Mandy's Affection +1\"{/b}{/i}"
                                        scene bg MandyRoomMad05
                                        MD "Thank you so much!"
                                        RT "{i}Oh, wow.{/i}"
                                        $ screen_on = "laurendoormap"
                                        call screen laurendoormap
                                "Never mind":
                                    scene bg MandyRoomMad03
                                    with dissolve
                                    MD "OMG! You made me get up for that."
                                    "{i}{b}\"Mandy's Anger +1\"{/b}{/i}"
                                    $ cousinanger += 1
                                    $ screen_on = "laurendoormap"
                                    call screen laurendoormap
                        else:
                            scene bg MandyRoomMad03
                            with dissolve
                            L "You already gave me a gift. Stop being creepy!"
                            $ cousinanger += 1
                            "{i}{b}\"Mandy's Anger +1\"{/b}{/i}"
                            $ screen_on = "laurendoormap"
                            call screen laurendoormap
                    "I just wanted to apologize":
                        scene bg MandyRoomMad03
                        with dissolve
                        MD "Well, it's going to take more than just words for me to forgive you for what you did!"
                        RT "{i}I guess I better give her some time, or maybe I can get her a present so she won't be so mad.{/i}"
                        $ screen_on = "laurendoormap"
                        call screen laurendoormap
            "Let's just take a peek at what she's doing." if spycaminlaurenroom == True:
                jump mandyspycamroommad
            "I'm just going to give her some time to cool down":
                $ screen_on = "laurendoormap"
                call screen laurendoormap

label mandyspycamroommad:               #### Edited 9-2-2020 ####
    if timeofdaycounter == 5:
        scene bg Dare81
        with dissolve
        $ renpy.pause ()
        scene bg Dare79
        with fade
        RT "{i}Not much going on... I guess I should have suspected that.{/i}"
        scene bg LaurenDoorNight
        with fade
        $ screen_on = "laurendoornightmap"
        call screen laurendoornightmap
    else:
        if daycounter <= 5:
            scene bg SpyCamMandyBedroom03
            with dissolve
            $ renpy.pause ()
            scene bg SpyCamMandyBedroom01
            with fade
            RT "{i}Looks like she's just doing her homework, I don't know why expected anything else.{/i}"
        else:
            scene bg SpyCamMandyBedroom04
            with dissolve
            $ renpy.pause ()
            scene bg SpyCamMandyBedroom02
            with fade
            RT "{i}Looks like she's just doing homework, or playing a computer game, or something boring. I don't know why I expected anything else.{/i}"
        scene bg LaurenDoor
        with fade
        $ screen_on = "laurendoormap"
        call screen laurendoormap

label mandy_study:                      #### Edited 9-2-2020 ####
    if spied_mandy_bed:
        scene bg LaurenDoor
        with fade
        RT "{i}It's locked... Mandy's probably still changing after dildoing herself in Mom's room.{/i}"
        menu:
            "Take a peek.":
                scene bg SpyCamMandyBedroom04
                with dissolve
                $ renpy.pause ()
                scene bg SpyCamMandyBedroom02
                with fade
                RT "{i}Look's like she's just doing her homework or something... I guess it was too much to ask for to get two shows today.{/i}"
                scene bg LaurenDoor
                with fade
                $ screen_on = "laurendoormap"
                call screen laurendoormap
            "Never mind.":
                RT "{i}I've already invaded her privacy enough for today.{/i}"
                $ screen_on = "laurendoormap"
                call screen laurendoormap
    if cousinanger >= 1:
        jump mandy_angry
    if cousinlibido == 10:
        jump mandyhornybedroom
    if visited_mandy_evening:
        scene bg LaurenDoor
        with fade
        if daycounter <= 5:
            RT "{i}I just went and talked with her... She'll think I'm creepy if I keep going in there to stare up her skirt.{/i}"
        else:
            RT "{i}I just went and talked to her... She'll get really annoyed if I keep interrupting her Womb Raider game.{/i}"
        $ screen_on = "laurendoormap"
        call screen laurendoormap
    if daycounter >= 6:
        scene bg LaurenDoor
        with fade
        RT "{i}Let's see if anything is going on in Lauren's room.{/i}"
        scene bg MandyStudy03
        with fade
        if not first_mandy_vgame_visit:
            RT "{i}Damn!... It looks like Mandy is having to do homework over the week... No. That's not homework.{/i}"
            R "Hey, Mandy, what's up?"
            scene bg MandyStudy04
            with dissolve
            MD "Oh! Hey, [ryan]!... I didn't hear you come in."
            MD "I'm just playing some computer games."
            R "Oh, yeah? Whatcha playin'?"
            MD "I'm actually really into the latest \"Womb Raider\" game."
            MD "Seeing the pictures you took of Sidney made me really want to play it."
            MD "Though, after seeing your version, this game seems a bit tame."
            MD "You need to be hired to make the next one more exciting and interesting."
            R "I'd love a job as a game developer, but like a real game developer. Not one that makes crappy renpy adult H-games."
            MD "Oh, yeah! Those perverts need to do something better with their time!"
            "...."
            MD "The weird thing about playing Womb Raider now though, is I keep picturing Sidney as Lauren Craft."
            R "Haha... weird."
            R "Oh!... If you do want to make the game more interesting, I can send you a link to a mod site where there are quite a few mods you can add to the game to make it a little more lewd."
            R "But, maybe that would be weird if you're picturing Sidney as Lauren Craft."
            MDT "{i}That would be awesome!{/i}"
            MD "Send me the link!"
            MD "I mean... If you have some time, and you remember, I'd be interested in seeing what kind of mods there are."
            R "Ok, I'll send it right now from my phone."
            R "...."
            R "And... it's sent."
            MD "Thanks!"
        else:
            RT "{i}Looks like Mandy's playing Womb Raider again.{/i}"
            R "Hey, Mandy."
            scene bg MandyStudy04
            with dissolve
            MD "Oh! Hey, [ryan]."
            R "How's your game coming along?"
            R "Did you download any more of those mods from the site I showed you?"
            MD "Yeah, I downloaded a few more sexy outfits for Lauren."
            MD "There's a few others I want to try out still."
            MDT "{i}I don't think I'll tell him about the mod I installed that makes Sidney... I mean Lauren Craft, get fucked by her aggressor when she gets defeated.{/i}"
            MDT "{i}I've never enjoyed getting defeated so much in my life.{/i}"
            R "Alright, I didn't want to inturrupt your fun, so I'll just show myself out."
        MD "Oh... if you're not doing anything, you should stop by our room again tonight."
        if truth_dare_completed:
            MDT "{i}I'd love to get that cock in my hands again!{/i}"
        if lauren_mischief >= 3:
            MDT "{i}I can't wait to see where our truth or dare game goes next!{/i}"
        else:
            MD "Maybe we can play a game or something."
        R "Sounds fun! I'll try to be there."
        MD "Awesome!... Now I've got to get back to my game."
        scene bg MandyStudy03
        with dissolve
        if not first_mandy_vgame_visit:
            MDT "{i}I've got to find that damn wolf that keeps sneaking up on me.!{/i}"
            $ first_mandy_vgame_visit = True
        else:
            MDT "{i}Now where's a really big bad guy that can fuck the shit out of Sidney... I mean Lauren Craft.{/i}"
        RT "{i}Dang, I was hoping to hang out, but she's pretty into that game.{/i}"
        $ visited_mandy_evening = True
        scene bg LaurenDoor
        $ screen_on = "laurendoormap"
        call screen laurendoormap
    else:
        scene bg LaurenDoor
        with fade
        RT "{i}Let's see if anything is going on in Lauren's room.{/i}"
        scene bg MandyStudy01
        with fade
        if not first_mandy_study_visit:
            RT "{i}Oh, looks like Mandy is doing some homework or something... Holy shit!{/i}"
            RT "{i}She's not wearing any panties!{/i}"
            RT "{i}I've got to get a picture of this!{/i}"
            scene bg MandyStudy05
            with dissolve
            $ renpy.pause ()
            play sound CameraClick
            $ renpy.pause ()
            scene bg MandyStudy01
            with dissolve
        else:
            RT "{i}I guess she's just more comfortable without her panties.{/i}"
            menu:
                "Take a closer look.":
                    scene bg MandyStudy06
                    with fade
                    RT "{i}Thank you, Jesus! I can see everything!{/i}"
                    RT "{i}I'd better back off before she catches me.{/i}"
                    scene bg MandyStudy01
                    with fade
        RT "I guess I should probably let her know I'm here."
        R "Hey, Mandy. What's up?"
        scene bg MandyStudy02
        with dissolve
        MD "Oh! Hey, [ryan]... I didn't hear you come in."
        RT "{i}Thank God!{/i}"
        if not first_mandy_study_visit:
            R "What are you working on?"
            MD "Some homework for my economics class."
            MD "There's so much work, and it's so boring!"
            R "Well, if you're bored, why don't we do something?"
            MD "Uugghh... I wish I could... but I've got to get this done."
            MD "Hey... Maybe if I'm able to get this done, you can stop by the room tonight?"
            MD "Then you can hang out with both Lauren and me."
            R "Yeah... Maybe I'll stop by."
            $ first_mandy_study_visit = True
        else:
            R "Still doing econ homework?"
            MD "Unfortunately."
            R "No time for a break?"
            MD "No..."
            MD "But stop by tonight, and hang out with Lauren and me."
            if truth_dare_completed:
                MDT "{i}I'd love to get that cock in my hands again!{/i}"
            if lauren_mischief >= 3:
                MDT "{i}I can't wait to see where our truth or dare game goes next!{/i}"
            else:
                MD "Maybe we can play a game or something."
            R "Sounds fun! I'll try to be there."
            MD "Awesome!... Now I've got to get back to my homework."
            scene bg MandyStudy01
            with dissolve
            MDT "{i}I wonder if he noticed I'm not wearing panties{/i}"
            RT "{i}Ok, [ryan]! Peel your eyes away before she notices you staring.{/i}"
        scene bg LaurenDoor
        with fade
        $ visited_mandy_evening = True
        $ screen_on = "laurendoormap"
        call screen laurendoormap

label mandyhornybedroom:                #### Edited 9-2-2020 ####
    if spycaminmomroom == True:
        scene bg LaurenRoom01
        with fade
        RT "{i}Hmmm... where's Mandy?... She's usually here in the evenings.{/i}"
        RT "{i}I guess I'll go check on Aunt Cami.{/i}"
        RT "{i}I love watching that ass when she's working out.{/i}"
        scene bg SleepBlack
        with fade
        scene bg MomDoor
        with fade
        RT "{i}What the hell? Why is the door locked? I don't think Aunt Cami's mad at me...{/i}"
        RT "{i}Or... any madder than usual, I should say.{/i}"
        RT "{i}Should I put my camera to good use?{/i}"
        menu:
            "Use spy-cam.":
                jump mandyspycamroomhorny
            "Not right now.":
                RT "{i}On second thought... I don't really care about what Aunt Cami's doing in that room.'{/i}"
                $ screen_on = "momdoormap"
                call screen momdoormap
    else:
        scene bg LaurenRoom01
        with fade
        RT "{i}Hmmm... where's Mandy?... She's usually here in the evenings.{/i}"
        RT "{i}I guess I'll go check on Aunt Cami.{/i}"
        RT "{i}I love watching that ass when she's working out.{/i}"
        scene bg SleepBlack
        with fade
        scene bg MomDoor
        with fade
        RT "{i}What the hell? Why is the door locked? I don't think Aunt Cami's mad at me...{/i}"
        RT "{i}Or... any madder than usual, I should say.{/i}"
        RT "{i}I've got to figure out a way to spy on her.{/i}"
        $ screen_on = "momdoormap"
        call screen momdoormap

label mandyspycamroomhorny:             #### Edited 9-2-2020 ####
    RT "{i}What will happen to me if the girls ever find out I'm using cameras to spy on them?{/i}"
    scene bg MandMastBedroom11
    with dissolve
    play music SexMusic
    $ renpy.pause ()
    if not mandymbatespycam:
        scene bg MandMastBedroom01
        with fade
        RT "{i}Mandy's in Mom's room?{/i}"
        scene bg MandMastBedroom02
        with dissolve
        RT "{i}What the hell is she looking for?{/i}"
        RT "{i}Whatever it is... she'd better hurry before Mom or Aunt Cami come back.{/i}"
    scene bg SleepBlack
    with fade
    scene bg MandMastBedroom03
    with fade
    if mandymbatespycam:
        MDT "{i}Found it! It was just under the bed.{/i}"
    else:
        MDT "{i}It's time again to take care of that itch.{/i}"
    scene bg MandMastBedroom04
    with fade
    MDT "{i}I'm glad Mom still keeps her key to the lockbox in her old running shoes in the closet.{/i}"
    scene bg MandMastBedroom05
    with fade
    MDT "{i}The forbidden dildo!{/i}"
    scene bg MandMastBedroom06
    with fade
    MDT "{i}(Reading in her head) ...So your pussy doesn't miss me. An exact replica of my dick. Love, Bobby.{/i}"
    if not mandymbatespycam:
        MDT "{i}What an egotistical bastard! I can't believe he had this made... I hope Mom doesn't use this!... But why else would she keep it if she doesn't?{/i}"
        MDT "{i}More importantly... why do I want to use it so badly?{/i}"
        MDT "{i}Goddamned prick! Leaving our family to fend for ourselves!{/i}"
        MDT "{i}Goddamned daddy issues!{/i}"
    else:
        MDT "{i}Why do I need to go to such lengths to get off anymore?{/i}"
        MDT "{i}Goddamned daddy issues!{/i}"
    scene bg SleepBlack
    with fade
    scene bg MandMastBedroom07
    with fade
    RT "{i}That's a big dildo for such a small girl!{/i}"
    scene bg MandMastBedroom08
    with fade
    if not mandymbatespycam:
        RT "{i}Oh, God... that's pretty fucking hot!{/i}"
        RT "{i}I need to get a picture.{/i}"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg MandMastBedroom08
        $ renpy.pause ()
    else:
        RT "{i}I can't believe she can actually take it!{/i}"
        RT "{i}At least she'll be ready for me when the time comes.{/i}"
    scene MandMastBedroomVideo01
    with fade
    play sound Mandy01 loop
    $ renpy.pause ()
    MDT "{i}God, yes! I needed this!{/i}"
    if mandymbatespycam and truth_dare_completed:
        MDT "{i}I can't believe the things I've been doing with my own cousins!{/i}"
        MDT "{i}Why do I love having [ryan]'s cock in my hands?{/i}"
        MDT "{i}Why do I enjoy licking his cum off of Lauren when it's all over?{/i}"
        MDT "{i}Daddy leaving has really fucked me up!{/i}"
    else:
        MDT "{i}Oh, I need to punish this little pussy!{/i}"
        MDT "{i}Why are you so naughty lately?{/i}"
        MDT "{i}Why do you keep making me think of my dad while I'm punishing you?{/i}"
        $ renpy.pause ()
    MDT "{i}Oh, fuck!... I'm gonna cum!{/i}"
    stop sound
    play sound Ejaculate
    scene bg MandMastBedroom09
    with fade
    if not mandymbatespycam:
        RT "{i}Oh, holy shit! She squirts as much as the rest of the family!... It definitely comes from my mom's side of the family then.{/i}"
        $ mandymbatespycam = True
    else:
        RT "{i}She's like a fucking firehose!{/i}"
    "{i}{b}\"Mandy's Libido -5\"{/b}{/i}"
    $ cousinlibido -= 5
    scene bg MandMastBedroom10
    with fade
    RT "{i}Look at her enjoying that after-orgasm feeling!{/i}"
    RT "{i}I hope the bedspread dries before Mom and Aunt Cami come back!{/i}"
    RT "{i}And she'd better dress and get out of there before she's caught.{/i}"
    RT "{i}Speaking of which... I'd better get out of here before I'm caught.{/i}"
    $ persistent.gal_Mandy_2 = True
    scene bg MomDoor
    with fade
    $ spied_mandy_bed = True
    play music Honey
    $ screen_on = "momdoormap"
    call screen momdoormap

label mandy_sleep_in:                   #### Edited 9-2-2020 ####
    scene bg SleepBlack
    with fade
    scene bg MandySleepIn
    with fade
    RT "{i}Mandy's taking full advantage of the weekend by sleeping in... I'm surprised that Lauren isn't here too... could she be in the bathroom?{/i}"
    RT "{i}Oh, well... I should sneak out so I don't wake Mandy.{/i}"
    scene bg LaurenDoor
    with fade
    $ screen_on = "laurendoormap"
    call screen laurendoormap

label lauren_sleep_in:                  #### Edited 9-2-2020 ####
    scene bg SleepBlack
    with fade
    scene bg LaurenSleepIn
    with fade
    RT "{i}Lauren's taking full advantage of the weekend by sleeping in... I'm surprised that Mandy isn't here too... could she be in the bathroom?{/i}"
    RT "{i}Oh, well... I should sneak out so I don't wake Lauren.{/i}"
    scene bg LaurenDoor
    with fade
    $ screen_on = "laurendoormap"
    call screen laurendoormap

label update_six_sidneyspycamroomhorny: #### Edited 9-2-2020 ####
    ST "{i}Holy fuck!... I actually fucked my own brother!{/i}"
    ST "{i}And I did it because I wanted to fuck him!{/i}"
    ST "{i}I wasn't imagining anybody else.{/i}"
    ST "{i}If I'm being honest with myself, I stopped thinking about other guys a long time ago.{/i}"
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
    ST "{i}Oh, my God!... What's happening?!!{/i}"
    ST "{i}Can't control... can't stop... {/i}"
    scene bg SpyCamSidneyBedroom10
    with dissolve
    stop sound
    ST "{i}Oh, my God, I squirted again!{/i}"
    ST "{i}And that felt sooooo good!{/i}"
    ST "{i}What's wrong with me?{/i}"
    if familyofsquirters == 4:
        RT "{i}Mom must be doing a lot of extra laundry with all the girls squirting all over their beds.{/i}"
        RT "{i}Not to mention what I do in mine.{/i}"
    elif familyofsquirters == 3:
        RT "{i}And that makes 3 for 3.{/i}"
        RT "{i}Is it something Mom's feeding them?{/i}"
    elif familyofsquirters == 2:
        RT "{i}Wow! Sidney's a squirter too.{/i}"
        RT "{i}Maybe there's something in the water.{/i}"
    elif familyofsquirters == 1:
        RT "{i}Oh, my God! Sidney just squirted all over her bed!{/i}"
        RT "{i}I thought that was just some kinky porn gimmick where the girls just piss all over.{/i}"
        RT "{i}Wow, Sidney's a real squirter!{/i}"
    RT "{i}Just... wow!{/i}"
    "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
    RT "{i}I might need to go back to my room to take care of something myself.{/i}"
    $ sidneylibido -= 5
    scene bg LaurenDoor
    with fade
    RT "{i}I should run before I get caught.{/i}"
    play music Honey
    $ screen_on = "laurendoormap"
    call screen laurendoormap

label diaz_is_back:
    if diaz_came_for_mandy:
        scene bg SleepBlack
        with fade
        "{b}DING DONG!{/b}"
        scene bg BlurryWhite
        with fade
        scene bg SleepBlack
        with fade
        "{b}DING DONG!{/b}"
        scene bg BlurryWhite
        with fade
        scene bg SleepBlack
        with fade
        R "Shit!.... I know who that is..."
        scene bg RyanHomework01
        with fade
        R "Looks like Sidney already went running."
        R "Not like anyone but me ever answers the door anyways."
        "It's time for the weekly Agent Diaz event, would you like to skip it this week?"
        menu:
            "Yes":
                "Ok... I get it... you've got other events to complete."
                "But are you going to protect Lauren and Mandy by paying the $1,000 this week, or will you let them pay Diaz in favors?"
                menu:
                    "Of course I'll protect them!" if money >= 1000:
                        "{i}\"Money -$1,000\"{/i}"
                        $ money -= 1000
                        "{i}\"Lauren and Mandy's Affection +1\"{/i}"
                        $ laurenaffection += 1
                        $ cousinaffection += 1
                        "{i}\"Lauren and Mandy's Libido +3\"{/i}"
                        $ laurenlibido += 3
                        $ cousinlibido += 3
                        $ timeofdaycounter += 1
                        jump myroom
                    "Shit!.... I don't have the money to protect them this week!" if money <= 999:
                        "That's ok, but somebody is going to have to get spanked."
                        "Who do you choose?"
                        menu:
                            "Lauren":
                                "{i}{b}\"Lauren's Affection -1\"{/b}{/i}"
                                $ laurenaffection -= 1
                                "{i}{b}\"Mandy's Affection +1\"{/b}{/i}"
                                $ cousinaffection += 1
                                "{i}\"Lauren and Mandy's Libido +1\"{/i}"
                                $ laurenlibido += 1
                                $ cousinlibido += 1
                                "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                                $ laurensubmission += 1
                                $ timeofdaycounter += 1
                                jump myroom
                            "Mandy":
                                "{i}{b}\"Mandy's Affection -1\"{/b}{/i}"
                                $ cousinaffection -= 1
                                "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                                $ laurenaffection += 1
                                "{i}\"Lauren and Mandy's Libido +1\"{/i}"
                                $ laurenlibido += 1
                                $ cousinlibido += 1
                                "{i}{b}\"Mandy's Submission +1\"{/b}{/i}"
                                $ cousinsubmission += 1
                                $ timeofdaycounter += 1
                                jump myroom
                    "I need that money elsewhere.... their asses will have to pay the bill this week." if money >= 1000:
                        "You perverted degenerate!"
                        "You want them to get spanked!... Well, only one of them this week. So, who do you choose?"
                        "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                        menu:
                            "Lauren":
                                "{i}{b}\"Lauren's Affection -1\"{/b}{/i}"
                                $ laurenaffection -= 1
                                "{i}{b}\"Mandy's Affection +1\"{/b}{/i}"
                                $ cousinaffection += 1
                                "{i}\"Lauren and Mandy's Libido +1\"{/i}"
                                $ laurenlibido += 1
                                $ cousinlibido += 1
                                "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                                $ laurensubmission += 1
                                $ timeofdaycounter += 1
                                jump myroom
                            "Mandy":
                                "{i}{b}\"Mandy's Affection -1\"{/b}{/i}"
                                $ cousinaffection -= 1
                                "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                                $ laurenaffection += 1
                                "{i}\"Lauren and Mandy's Libido +1\"{/i}"
                                $ laurenlibido += 1
                                $ cousinlibido += 1
                                "{i}{b}\"Mandy's Submission +1\"{/b}{/i}"
                                $ cousinsubmission += 1
                                $ timeofdaycounter += 1
                                jump myroom
            "No":
                pass
        if money >= 1000:
            RT "{i}I better grab my cash in case I need it.{/i}"
        else:
            RT "{i}Shit, I'm short on cash this week.{/i}"
            RT "{i}I hope Lauren and Mandy are ready to do their duty.{/i}"
        scene bg SleepBlack
        with fade
        scene bg DiazVisit02
        with fade
        AD "Well, good morning, [ryan]!"
        R "Chipper as always, I see?"
        AD "Yep, the prospect of money or entertainment just puts me in a good mood."
        AD "So, what's it going to be this week?"
        menu:
            "Pay her $1,000." if money >= 1000:
                R "Here, just take your money and get out of here."
                "{i}\"Money -$1,000\"{/i}"
                $ money -= 1000
                scene bg DiazVisit01
                with dissolve
                AD "Now don't be like that..."
                AD "I'm going to be a big part of your family's lives here in the near future. So, let's try to keep things civil."
                scene bg DiazVisit02
                with dissolve
                AD "For now, let me just say that I hope you enjoy your week."
                R "..."
                AD "Well?"
                R "{i}(muttering){/i} I hope you enjoy your week, too."
                AD "Well, thank you! I'll see you next Thursday, bright and early!"
                play sound CloseDoor
                scene bg DiazVisit47
                with dissolve
                RT "{i}Oh, how do I get her out of our lives?{/i}"
                L "{i}(Shouting){/i} [ryan]! Was that who I think it was?"
                R "Yeah! But she's gone now!"
                MD "You mean you paid her!?"
                R "I did!"
                L "Will you please come to our room?"
                scene bg SleepBlack
                with fade
                R "What is it?"
                play music SexMusic
                jump ryan_lauren_and_mandy
            "Let Lauren and Mandy pay in favors":
                if money <= 999:
                    R "Uuuuugghhh.... I don't have enough money this week."
                    AD "You've got to learn to manage your money better!"
                    AD "Lucky for you, your sister and cousin can cover your ass, by using theirs."
                    R "You sadist!"
                else:
                    R "I need my money for other things this week."
                    R "I'm just going to have to let Lauren and Mandy take one for the team."
                    AD "Haha, I like that attitude!"
                    AD "Why put your ass on the line, when you can use theirs?"
                    R "You sadist!"
                scene bg DiazVisit02
                with dissolve
                AD "Why, thank you!..."
                AD "And don't worry about the long-term effects of punishing the girls."
                AD "If you could see their search history and digital journals you'd see that we're just helping them realize their desires."
                scene bg DiazVisit02
                with dissolve
                AD "Would you kindly escort me to their room?"
                scene bg SleepBlack
                with fade
                $ renpy.pause ()
                play music SexMusic
                jump diaz_lauren_and_mandy
    else:
        scene bg SleepBlack
        with fade
        "{i}\"DING DONG\"{/i}"
        RT "{i}Huh?...{/i}"
        scene bg BlurryWhite
        with fade
        scene bg SleepBlack
        with fade
        "{i}\"DING DONG\"{/i}"
        scene bg BlurryWhite
        with fade
        scene bg SleepBlack
        with fade
        RT "{i}Where is that bell coming from?{/i}"
        RT "{i}Oh yeah, probably from the...{/i}"
        RT "...."
        $ renpy.pause ()
        scene bg DiazVisit47
        with fade
        ADT "{i}What the hell? Where is everyone?{/i}"
        ADT "{i}I guess I'll just use my key and let myself in.{/i}"
        scene bg DiazAgain31
        with dissolve
        AD "Hello!... Is anybody home?"
        ADT "{i}I know [mom_name] left this morning to talk to her lawyer, and I saw Sidney go running.{/i}"
        ADT "{i}The rest of them have got to be here.{/i}"
        ADT "{i}I'll just show myself into Lauren's room, then.{/i}"
        ADT "{i}From what I've seen on [ryan]'s little spycams, I'd say it's about time for Mandy to join in on the fun.{/i}"
        scene bg SleepBlack
        with fade
        scene bg DiazAgain01
        with fade
        ADT "{i}Ohhh... how adorable is that?{/i}"
        ADT "{i}I almost hate to wake them.{/i}"
        ADT "{i}But I didn't break into their house for nothing!{/i}"
        scene bg DiazAgain03
        with dissolve
        play music SexMusic
        AD "Good morning, girls!"
        MD "What the fuck?"
        L "Oh, shit!"
        L "What the hell are you doing here?"
        scene bg DiazAgain04
        with dissolve
        AD "What do you mean, what am I doing here?"
        AD "You know we have a long-standing appointment."
        L "You mean [ryan] didn't pay you?"
        MD "Pay you... what the hell are you two taking about?... What the hell is going on?"
        AD "Lauren, would you take a few minutes to fill Mandy in about what's going on?"
        scene bg SleepBlack
        with fade
        "{i}\"A few minutes later.\"{/i}"
        scene bg DiazAgain04
        with fade
        MD "Oh, fuck no! You're not doing anything like that to me."
        AD "Is that right?"
        AD "And why do you think you get to even live here at your aunt's house?"
        AD "It's all because of me."
        AD "One word from me, and the FBI will happily move you and your mom into a shit-hole appartment in the projects."
        AD "Do you know how much crime there is there? Do you know what happens to cute little white girls like you in a place like that?"
        MD "You couldn't do that... could you?"
        AD "All it would take is one word from me."
        MD "Fuck!"
        AD "Haha... i knew you'd see it my way."
        scene bg DiazAgain06
        with dissolve
        AD "And now that we have that resolved... let me show you a few things I brought with me to make our game today even more fun."
        scene bg DiazAgain08
        with fade
        AD "With these, as well as the rope I brought, and my sexy little costume, we are going to have so much fun!"
        AD "I'd say it's time for you two to get your uniforms on and make sure you sexy them up."
        L "No... wait! Shouldn't you check with [ryan] first, and make sure he doesn't have the money to pay you this week?"
        AD "Sorry, I'm pretty sure he left you on your own this morning... I haven't seen or heard from him."
        L "Well, let me just run to his bedroom and..."
        AD "Nope! He's already had his chance to..."
        L "{i}(yelling){/i} [ryan]!"
        AD "You idiot! Are you trying to bring Camille in here?"
        AD "Do that again and our deal's off."
        AD "Mandy can go live in the projects, and you can go to a nice little women's prison for being complicit to your brother's many crimes involving the Mafia."
        L "I'm sorry! I won't..."
        AD "That's right you won't, now lets get changed and have some fun."
        scene bg SleepBlack
        with fade
        "{i}\"Meanwhile, back in [ryan]'s room.\"{/i}"
        scene bg RyanHomework01
        with fade
        RT "{i}What the hell?...{/i}"
        RT "{i}Did I sleep in?{/i}"
        RT "{i}I thought I heard someone call my name.{/i}"
        RT "{i}It sounded like Lauren, I should go and check on her.{/i}"
        scene bg SleepBlack
        with fade
        $ renpy.pause ()
        scene bg LaurenDoor
        with fade
        RT "{i}Lauren and Mandy could be dressing or something... I should probably knock.{/i}"
        menu:
            "Knock":
                RT "{i}Nobody answered.{/i}"
                R "Mandy? Lauren? Are you there?"
                X "{i}(whispering){/i} Oh, thank God... it's just [ryan]."
                X "Come in."
                RT "{i}That didn't sound like Mandy or Lauren... that sounded like...{/i}"
                scene bg DiazAgain09
                with fade
                R "Diaz!..."
                "...."
                R "What the hell is going on here?"
                AD "Well there you are, [ryan]. So nice of you to finally join us."
                R "Why is Lauren all tied up?"
                play sound Muffled
                L "Mmmmpphhhh..."
                stop sound
                scene bg DiazAgain11
                with dissolve
                MD "[ryan]! Thank God you finally came."
                MD "Agent Diaz said we have to pay her in favors today, since you didn't show up with the money."
                R "Well... nobody woke me up."
                AD "Is that my job now too? Your own personal wake up service?"
                AD "I rang the doorbell like I do every Thursday."
                AD "Why did you fail to answer the door this morning?"
                R "I didn't hear..."
                MD "She's going to make me spank Lauren!"
                MD "Please say you're going to pay her now, so I don't have to."
                play sound Muffled
                scene bg DiazAgain09
                with dissolve
                L "Mmmmpphhh!"
                stop sound
                R "Alright Diaz, let me run and see if I've got the five hundred in my bedroom."
                AD "Five hundred? You're rescuing two girls now... the price has doubled."
                R "A thousand dollars?!"
                $ persistent.gal_harem_4 = True
                menu:
                    "Fine! Let me get your money." if money >= 500:
                        AD "Alright, I'll just untie Lauren and get changed, while you grab the money."
                        R "Yeah, why are you dressed like that?"
                        AD "It's my sexy police girl costume. Dressing up makes everything more fun."
                        AD "And now that you've seen me in it, are you sure you want to pay the money?"
                        RT "{i}She is damn hot in that costume...{/i}"
                        RT "{i}No!... The girls are depending on me!{/i}"
                        R "I'll be right back."
                        scene bg SleepBlack
                        with fade
                        "{i}\"A few minutes later.\"{/i}"
                        scene bg DiazAgain13
                        with fade
                        R "Here's your money."
                        "{i}\"Money -$1,000\"{/i}"
                        $ money -= 1000
                        R "I thought you were going to change while I was gone."
                        AD "Well... you weren't gone very long, and I thought you might want one more look on what you're missing out on."
                        AD "You sure this is what you want?"
                        R "I'm sure, so why don't you get your ass off our property."
                        AD "Alright, no need to be so rude. I'll just show myself out."
                        ADT "{i}Jerk... I'll fucking change in my car.{/i}"
                        scene bg DiazAgain14
                        with dissolve
                        R "Are you two ok?"
                        scene bg DiazAgain15
                        with dissolve
                        MD "Holy fuck, [ryan]! I can't believe that just happened!"
                        R "Yeah... this happens every week."
                        MD "I know! Diaz had Lauren fill me in."
                        L "I guess we're just getting used to it."
                        scene bg DiazAgain16
                        with dissolve
                        MD "I thought I was really going to have to spank your ass!"
                        MD "What a kinky bitch!"
                        L "Yeah, that's some messed-up shit."
                        LT "{i}Why does the thought of getting spanked by Mandy kind of turn me on?{/i}"
                        MDT "{i}I could have been slapping Lauren's sexy ass if [ryan] hadn't shown up.{/i}"
                        "{i}\"Lauren and Mandy's Libido +1\"{/i}"
                        $ laurenlibido += 1
                        $ cousinlibido += 1
                        scene bg DiazAgain17
                        with dissolve
                        MD "Thank you for rescuing us!"
                        L "Yeah!.. Our hero!"
                        "{i}\"Lauren's and Mandy's Affection +1{/i}"
                        $ laurenaffection += 1
                        $ cousinaffection += 1
                        scene bg DiazAgain16
                        with dissolve
                        MD "Shit, Lauren. We'd better get in the shower. We're going to be late for school!"
                        L "I'll just skip the shower this morning. I need to talk to [ryan] about something."
                        MD "Alright, see you after my shower."
                        scene bg SleepBlack
                        with fade
                        scene bg DiazAgain18
                        with fade
                        L "Well, [ryan]. Once again, you've come to my rescue."
                        R "Ohh... it was nothing. I couldn't watch that bitch do that to my sister this..."
                        scene bg DiazAgain19
                        with dissolve
                        L "Now it's time for me to reward my hero."
                        scene bg DiazAgain20
                        with dissolve
                        MD "I forgot my tow..."
                        MD "Oh, my God!"
                        scene bg DiazAgain21
                        with dissolve
                        MD "Haha!... I knew there was something going on with you two!"
                        MD "So, this is the boy you wouldn't tell me about?"
                        L "Mandy, shut up!"
                        L "And, this isn't what you think it is."
                        MD "Well, please explain."
                        L "It's just something I like to do for [ryan] to show him my gratitude for paying Diaz off."
                        L "I just kind of grind him a bit. Just through our clothes... nothing more."
                        R "It's becoming kind of our ritual."
                        MD "Oh?... And there's nothing else to this ritual?"
                        L "No... well, I guess I usually dance in my sexy schoolgirl uniform too."
                        MD "Now that sounds fun! I want in on this ritual."
                        L "What!?"
                        MD "Yeah, let me just put some music on my phone and we'll do some dancing for [ryan]."
                        L "Really?!"
                        MD "Yeah, I want to thank him too. And this sounds like a pretty fun ritual you've already got established. No need to change it."
                        RT "{i}Now, Lauren gets to see just how much fun Mandy can be!{/i}"
                        play music ClubMusic
                        scene bg SleepBlack
                        with fade
                        scene bg DiazAgain22
                        with fade
                        RT "{i}Holy shit! Look at those two go at it! This is sexy as hell!{/i}"
                        RT "{i}Mandy grinding up against Lauren's sexy ass!... Fuck, I'm hard as a rock!{/i}"
                        scene bg DiazAgain23
                        with dissolve
                        RT "{i}Oh, God!... I want both of those asses!{/i}"
                        RT "{i}Lauren's soft, curvy ass, and Mandy's skinny, muscular ass.{/i}"
                        RT "{i}As much as I detest Diaz... this wouldn't be possible without her.{/i}"
                        play music SexMusic
                        scene bg DiazAgain24
                        with dissolve
                        MD "And now, it's time for the other part of the ritual."
                        MD "Did you say you two do some top-of-the-clothes grinding?"
                        L "Yeah, I guess we could take turns."
                        R "There's no way I'll be able to last long enough for both of you to grind me."
                        MD "Hmmm... then we'll have to try something different."
                        MD "But it's going to require at least one of us to take off their underwear."
                        R "Who?"
                        MD "You, stupid."
                        RT "{i}Oh, God!{/i}"
                        scene bg SleepBlack
                        with fade
                        scene bg DiazAgain25
                        with fade
                        L "Holy fuck, [ryan], you're so hard!"
                        MD "More like, \"Holy fuck, [ryan], you're so huge!\""
                        MD "I can't get over the size of this porn-sized cock!"
                        L "So... how are we going to do this?"
                        MD "Just take off your skirt, and follow my lead."
                        scene bg SleepBlack
                        with fade
                        scene bg DiazVisit38
                        with fade
                        ADT "{i}Finally! It's such a fucking pain to change clothes in the car.{/i}"
                        scene bg DiazVisit39
                        with fade
                        ADT "{i}I hope I didn't take too long.{/i}"
                        ADT "{i}I would hate to miss out on their after-Diaz visit ritual.{/i}"
                        scene bg NDiazVisit40
                        with dissolve
                        ADT "{i}Oh, well now.... this is interesting!{/i}"
                        ADT "{i}I didn't think he'd be able to get Mandy involved this quickly!{/i}"
                        ADT "{i}What could he have said to them to make this happen?{/i}"
                        ADT "{i}I'm starting to respect this kid's game!{/i}"
                        scene bg DiazAgain26
                        with fade
                        ADT "{i}That's fucking hot!{/i}"
                        scene bg NDiazVisit42 with Dissolve (0.5)
                        $ renpy.pause (1.0)
                        scene bg NDiazVisit43 with Dissolve (0.5)
                        $ renpy.pause (1.0)
                        play sound Diaz01 loop
                        scene bg NDiazVisit42 with Dissolve (0.5)
                        $ renpy.pause (1.0)
                        scene bg NDiazVisit43 with Dissolve (0.5)
                        $ renpy.pause (1.0)
                        scene bg NDiazVisit42 with Dissolve (0.5)
                        $ renpy.pause (1.0)
                        scene bg NDiazVisit43 with Dissolve (0.5)
                        $ renpy.pause (1.0)
                        scene bg NDiazVisit42 with Dissolve (0.5)
                        $ renpy.pause (1.0)
                        scene bg NDiazVisit43 with Dissolve (0.5)
                        $ renpy.pause (1.0)
                        scene bg NDiazVisit42 with Dissolve (0.5)
                        $ renpy.pause (1.0)
                        scene bg NDiazVisit43 with Dissolve (0.5)
                        $ renpy.pause (1.0)
                        stop sound fadeout 1.0
                        scene bg SleepBlack
                        with fade
                        scene DiazAgainVideo03
                        with fade
                        $ renpy.pause ()
                        RT "{i}Oh, God!... This might be the best day of my life!{/i}"
                        RT "{i}Both my sister and my cousin, at the same time?!{/i}"
                        RT "{i}How could this get any better?{/i}"
                        RT "{i}Oh... right... I could be fucking them.{/i}"
                        RT "{i}Soon!{/i}"
                        $ renpy.pause ()
                        LT "{i}Oh, my God! My brother's huge cock is sliding up and down against my pussy and ass!{/i}"
                        LT "{i}And my ass is rubbing against my cousin's skinny ass cheeks!{/i}"
                        LT "{i}This is the hottest thing that's ever happened to me!{/i}"
                        "{i}{b}\"Lauren's Libido +5\"{/b}{/i}"
                        $ laurenlibido += 5
                        $ renpy.pause ()
                        MDT "{i}God, yes! Finally I've got a cock rubbing against my virgin pussy and ass!{/i}"
                        MDT "{i}If Mom could see me now! Haha!.. She'd cut [ryan]'s balls off!{/i}"
                        MDT "{i}Self-righteous slut.{/i}"
                        "{i}{b}\"Mandy's Libido +5\"{/b}{/i}"
                        $ cousinlibido += 5
                        $ renpy.pause ()
                        R "Oh, fuck!... This feels incredible!"
                        R "I'm gonna cum!"
                        MD "Let it out. You deserve it."
                        R "Oh, God!"
                        play sound Ejaculate
                        scene bg DiazAgain27
                        with dissolve
                        with hpunch
                        $ renpy.pause ()
                        play sound Ejaculate
                        scene bg DiazAgain28
                        with dissolve
                        with vpunch
                        $ renpy.pause ()
                        scene bg DiazAgain29
                        with dissolve
                        MD "That... is a lot of cum!"
                        L "Yeah, it's running down my back, into my panties."
                        MD "I dare you to wear those panties to school."
                        L "Euw... that's gross... they'll be all smelly and crusty."
                        MD "Chicken."
                        L "Fine... I will if you do."
                        MD "Deal."
                        R "You two are too much!"
                        "{i}\"Girls giggling\"{/i}"
                        scene bg DiazAgain30
                        with dissolve
                        play music Honey
                        MD "[ryan], really, thank you so much for rescuing us from that sadistic bitch."
                        L "Yeah... we know another thousand dollars a week is expensive, but we'll keep rewarding you like this if you'll keep paying to keep us safe."
                        R "I'll try my hardest."
                        MD "Hehehe... that's pretty hard."
                        L "Now we've really got to get ready for school."
                        L "Do you think I'll see you there today?"
                        R "Maybe."
                        if not mandy_at_school:
                            MD "I hope I can get transferred to your school soon. It would be so fun being there with you two."
                            L "Oh my God, that would be so fun!"
                        else:
                            pass
                        R "Alright, I'd better run and get ready myself."
                        MD "Maybe we'll see you tonight."
                        scene bg RyansRoom01
                        with fade
                        $ diaz_came_for_mandy = True
                        $ saved_their_asses = True
                        $ timeofdaycounter += 1
                        jump myroom
                    "I cant pay that!":
                        R "A thousand dollars? I can't spare that much money right now."
                        AD "Well then... let's get started. We don't have all morning."
                        AD "I'll tell you what though. I'll let you watch this time, and I'll even let you choose who gets spanked."
                        AD "And we'll let the other one do the spanking."
                        R "I can't choose that... I don't want to have any part of this."
                        AD "Well, if you don't choose, than I'll spank them both myself. And I'm a pretty hard spanker."
                        MD "No, [ryan]! Please, just choose."
                        MD "I would rather be spanked by Lauren than by Agent Diaz."
                        play sound Muffled
                        L "MMMpphhhhh..."
                        stop sound
                        R "But how will I decide?"
                        R "Hmmm... who should I choose to get spanked?"
                        menu:
                            "Lauren":
                                $ lauren_spanked = True
                                R "Sorry Lauren, but you're already tied up and ready for it."
                                R "I choose you to be spanked."
                                "{i}{b}\"Mandy's Affection +1\"{/b}{/i}"
                                "{i}{b}\"Lauren's Affection -1\"{/b}{/i}"
                                $ cousinaffection += 1
                                $ laurenaffection -= 1
                                AD "Alright girls, you heard the man. Lauren, head down, ass up."
                                AD "Mandy, prepare yourself to spank your cousin."
                                AD "Now, let's all imagine that I'm your school resource officer."
                                AD "Mandy saw Lauren smoking in the school bathroom, and came to me to tattle."
                                AD "As a reward for squealing on her peer, I gave her the option to help me punish her."
                                AD "And Mandy enthusiastically accepted!"
                                scene bg SleepBlack
                                with fade
                                scene bg DiazAgainVideo02F01
                                with fade
                                MD "Do I really have to do this?"
                                AD "No, but if you want to keep living here you do."
                                AD "And make sure you do it hard enough to hurt."
                                AD "If you're too pussy about it, I'll spank you both."
                                MD "Fine... I'm sorry, Lauren!"
                                scene DiazAgainVideo02
                                with fade
                                play sound Muffled loop
                                $ renpy.pause ()
                                MD "When can I stop?"
                                AD "Keep going until I tell you."
                                RT "{i}Diaz is such a sadistic bitch!{/i}"
                                RT "{i}This is so messed up!{/i}"
                                RT "{i}So, why is it making me so hard?{/i}"
                                $ renpy.pause ()
                                LT "{i}Oww... my ass is so sensitive!{/i}"
                                LT "{i}This really hurts!...{/i}"
                                LT "{i}So why do I kind of like it?{/i}"
                                LT "...."
                                LT "{i}This is starting to make me wet!{/i}"
                                LT "{i}Fuck! Mandy is going to notice!{/i}"
                                "{i}{b}\"Lauren's Libido +3\"{/b}{/i}"
                                $ laurenlibido += 3
                                $ renpy.pause ()
                                MDT "{i}As if my life couldn't get any weirder, now I'm being forced to spank my cousins!{/i}"
                                MDT "{i}I'm being blackmailed by an authoritative, dominatrix-like woman! Could this get any kinkier?{/i}"
                                MDT "...."
                                MDT "{i}OH MY GOD!! Are Lauren's panties starting to get wet?{/i}"
                                MDT "{i}Could she really be getting this turned on? Or is her bladder leaking from fright?{/i}"
                                MDT "{i}Is Lauren into this?{/i}"
                                MDT "{i}If she's enjoying my hand slapping her ass cheeks... Fuck!... Now I'm super turned on!{/i}"
                                MDT "{i}At least nobody can see my panties.{/i}"
                                "{i}{b}\"Mandy's Libido +3\"{/b}{/i}"
                                $ cousinlibido += 3
                                $ renpy.pause ()
                                ADT "{i}I love this job!{/i}"
                                ADT "{i}I wouldn't be able to get away with this with most people...{/i}"
                                ADT "{i}But after reading their digital journals and seeing their browser histories, I know I'm just helping them fulfill their deepest and most secret desires.{/i}"
                                $ renpy.pause ()
                                AD "Alright... I think Lauren's probably had enough fun for today."
                                AD "You can stop, Mandy."
                                stop sound
                                scene bg DiazAgain11
                                with fade
                                AD "I think Lauren has learned her lesson."
                                AD "Are you ever going to smoke in the girl's bathroom again?"
                                play sound Muffled
                                L "Mmmmpphhh!"
                                stop sound
                                "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                                $ laurensubmission += 1
                            "Mandy":
                                $ mandy_spanked = True
                                R "Sorry Mandy, but Lauren's already been terrorized by Agent Diaz too much."
                                R "I choose you to be spanked."
                                L "Fuck..."
                                "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
                                "{i}{b}\"Mandy's Affection -1\"{/b}{/i}"
                                $ cousinaffection -= 1
                                $ laurenaffection += 1
                                AD "Alright girls, you heard the man. Mandy, let's get you tied up and gagged."
                                scene bg SleepBlack
                                with fade
                                $ renpy.pause ()
                                scene bg DiazAgain10
                                with fade
                                AD "Lauren, prepare yourself to spank your cousin."
                                AD "Now, let's all imagine that I'm your school resource officer."
                                AD "Lauren saw Mandy smoking in the school bathroom, and came to me to tattle."
                                AD "As a reward for squealing on her peer, I gave her the option to help me punish her."
                                AD "And Lauren enthusiastically accepted!"
                                scene bg SleepBlack
                                with fade
                                scene bg DiazAgainVideo01F01
                                with fade
                                L "Do I really have to do this?"
                                AD "No, but if you want to stay out of jail, you do."
                                AD "And make sure you do it hard enough to hurt."
                                AD "If you're too pussy about it, I'll spank you both."
                                L "Fine... I'm sorry, Mandy!"
                                scene DiazAgainVideo01
                                with fade
                                play sound Muffled loop
                                $ renpy.pause ()
                                L "When can I stop?"
                                AD "Keep going until I tell you."
                                RT "{i}Diaz is such a sadistic bitch!{/i}"
                                RT "{i}This is so messed up!{/i}"
                                RT "{i}So, why is it making me so hard?{/i}"
                                $ renpy.pause ()
                                MDT "{i}Oww... my ass is so sensitive!{/i}"
                                MDT "{i}This really hurts!...{/i}"
                                MDT "{i}So why do I kind of like it?{/i}"
                                MDT "...."
                                MDT "{i}This is starting to make me wet!{/i}"
                                MDT "{i}Fuck! Lauren is going to notice!{/i}"
                                "{i}{b}\"Mandy's Libido +3\"{/b}{/i}"
                                $ cousinlibido += 3
                                $ renpy.pause ()
                                LT "{i}As if my life couldn't get any weirder, now I'm being forced to spank my cousin!{/i}"
                                LT "{i}I'm being blackmailed by an authoritative, dominatrix-like woman! Could this get any kinkier?{/i}"
                                LT "...."
                                LT "{i}OH MY GOD!! Are Mandy's panties starting to get wet?{/i}"
                                LT "{i}Could she really be getting this turned on? Or is her bladder leaking from fright?{/i}"
                                LT "{i}Is Mandy into this?{/i}"
                                LT "{i}If she's enjoying my hand slapping her ass cheeks... Fuck!... Now I'm super turned on!{/i}"
                                LT "{i}At least nobody can see my panties.{/i}"
                                "{i}{b}\"Lauren's Libido +3\"{/b}{/i}"
                                $ laurenlibido += 3
                                $ renpy.pause ()
                                ADT "{i}I love this job!{/i}"
                                ADT "{i}It's a rare thing to find a family that's this perverted.{/i}"
                                ADT "{i}I wouldn't be able to get away with this with most people...{/i}"
                                ADT "{i}But after reading their digital journals and seeing their browser histories, I know I'm just helping them fulfill their deepest and most secret desires.{/i}"
                                $ renpy.pause ()
                                AD "Alright... I think Mandy's probably had enough fun for today."
                                AD "You can stop, Lauren."
                                stop sound
                                scene bg DiazAgain12
                                with fade
                                AD "I think Mandy has learned her lesson."
                                AD "Are you ever going to smoke in the girl's bathroom again?"
                                play sound Muffled
                                MD "Mmmmpphhh!"
                                stop sound
                                "{i}{b}\"Mandy's Submission +1\"{/b}{/i}"
                                $ cousinsubmission += 1
                        AD "Haha... that's what I thought."
                        scene bg SleepBlack
                        with fade
                        $ renpy.pause ()
                        scene bg DiazAgain13
                        with fade
                        AD "Wow!... That got me all worked up."
                        AD "{i}(whispering to [ryan]){/i} I'm going to go take care of myself in my car."
                        AD "{i}(whispering){/i} And don't feel too bad. I've seen their browser histories... they're totally into this."
                        scene bg DiazAgain14
                        with dissolve
                        RT "{i}Holy shit!... Is Agent Diaz right?  Did they secretly enjoy that?{/i}"
                        R "Are you girls ok?"
                        scene bg DiazAgain15
                        with dissolve
                        if lauren_spanked:
                            L "Well, besides the fact that I was tied up, gagged, and was spanked raw by my cousin, who was blackmailed into it... {i}(sarcastic tone){/i} Yeah, I'm great!"
                            LT "{i}Shit!... Why did I like that? What is wrong with me?... I wonder if Mandy noticed that my panties were soaked.{/i}"

                        else:
                            MD "Well, besides the fact that I was tied up, gagged, and was spanked raw by my cousins, who was blackmailed into it... {i}(sarcastic tone){/i} Yeah, I'm great!"
                            MDT "{i}Shit!... Why did I like that? What is wrong with me?... I wonder if Lauren noticed that my panties were soaked.{/i}"
                        scene bg DiazAgain16
                        with dissolve
                        if lauren_spanked:
                            MD "I'm so sorry! I really didn't want to do that."
                            MDT "{i}Fuck, why was spanking Lauren so fun?{/i}"
                            MDT "{i}I really need to rub one out now.{/i}"
                            L "I know... it was fucking Agent Diaz!"
                        else:
                            L "I'm so sorry! I really didn't want to do that."
                            LT "{i}Fuck, why was spanking Mandy so fun?{/i}"
                            LT "{i}I really need to rub one out now.{/i}"
                            MD "I know... it was fucking Agent Diaz!"
                        scene bg DiazAgain15
                        with dissolve
                        if lauren_spanked:
                            L "And [ryan], for choosing to have me spanked!"
                        else:
                            MD "And [ryan], for choosing to have me spanked!"
                        R "I'm sorry, but I had to choose one of you!"
                        R "I didn't have the money to spare this week, but I'll try as hard as I can next week."
                        scene bg DiazAgain17
                        with dissolve
                        L "Oh, please do!"
                        LT "{i}I can't let this new fetish get any stronger!{/i}"
                        MD "Yes, please try your hardest!"
                        MDT "{i}Or don't... we've got to save that money to corrupt my mom!{/i}"
                        MDT "{i}And I wouldn't mind doing that again!{/i}"
                        R "Alright... well, I'll let you finish getting ready for school.  I'm going to try to make some more money to save your asses next week."
                        scene bg LaurenDoor
                        with fade
                        RT "{i}I'm not sure... they didn't seem to enjoy that... and even if they did... do I really want them to become corrupted in that way?{/i}"
                        $ timeofdaycounter += 1
                        $ diaz_came_for_mandy = True
                        $ gave_their_asses = True
                        play music Honey
                        jump myroom

label ryan_lauren_and_mandy:
    if not saved_their_asses:
        scene bg DiazAgain17
        with dissolve
        MD "Thank you so much for saving us this week!"
        L "Yes! Neither of us were up to getting our asses slapped today."
        MD "Yeah, that's some messed-up shit."
        LT "{i}Why does the thought of getting spanked by Mandy kind of turn me on?{/i}"
        LT "{i}It would even be fun to slap her ass!{/i}"
        MDT "{i}I could have been slapping Lauren's sexy ass if [ryan] hadn't shown up.{/i}"
        MDT "{i}Or better yet, she could have been slapping mine!{/i}"
        "{i}\"Lauren and Mandy's Libido +1\"{/i}"
        $ laurenlibido += 1
        $ cousinlibido += 1
        scene bg DiazAgain17
        with dissolve
        MD "Thank you for rescuing us!"
        L "Yeah!... Our hero!"
        "{i}\"Lauren and Mandy's Affection +1\"{/i}"
        $ laurenaffection += 1
        $ cousinaffection += 1
        scene bg DiazAgain16
        with dissolve
        MD "Shit, Lauren. We'd better get in the shower. We're both going to be late for school!"
        L "I'll just skip the shower this morning. I need to talk to [ryan] about something."
        MD "Alright, see you after my shower."
        scene bg SleepBlack
        with fade
        scene bg DiazAgain18
        with fade
        L "Well, [ryan]. Once again, you've come to my rescue."
        R "Ohh... it was nothing. I couldn't watch that bitch do that to my sister this..."
        scene bg DiazAgain19
        with dissolve
        L "Now it's time for me to reward me hero."
        scene bg DiazAgain20
        with dissolve
        MD "I forgot my tow..."
        MD "Oh, my God!"
        scene bg DiazAgain21
        with dissolve
        MD "Haha!... I knew there was something going on with you two!"
        MD "So, this is the boy you wouldn't tell me about?"
        L "Mandy, shut up!"
        L "And, this isn't what you think it is."
        MD "Well, please explain."
        L "It's just something I like to do for [ryan] to show him my gratitude for paying Diaz off."
        L "I just kind of grind him a bit. Just through our clothes... nothing more."
        R "It's becoming kind of our ritual."
        MD "Oh?... And there's nothing else to this ritual?"
        L "No... well, I guess I usually dance in my sexy schoolgirl uniform too."
        MD "Now that sounds fun! I want in on this ritual."
        L "What!?"
        MD "Yeah, let me just put some music on my phone and we'll do some dancing for [ryan]."
        L "Really?!"
        MD "Yeah, I want to thank him too. And this sounds like a pretty fun ritual you've already got established. No need to change it."
        RT "{i}Now, Lauren gets to see just how much fun Mandy can be!{/i}"
        play music ClubMusic
        scene bg SleepBlack
        with fade
        scene bg DiazAgain22
        with fade
        RT "{i}Holy shit! Look at those two go at it! This is sexy as hell!{/i}"
        RT "{i}Mandy grinding up against Lauren's sexy ass!... Fuck, I'm hard as a rock!{/i}"
        scene bg DiazAgain23
        with dissolve
        RT "{i}Oh, God!... I want both of those asses!{/i}"
        RT "{i}Lauren's soft, curvy ass, and Mandy's skinny, muscular ass.{/i}"
        RT "{i}As much as I detest Diaz... this wouldn't be possible without her.{/i}"
        play music SexMusic
        scene bg DiazAgain24
        with dissolve
        MD "And now, it's time for the other part of the ritual."
        MD "Did you say you two do some top-of-the-clothes grinding?"
        L "Yeah, I guess we could take turns."
        R "There's no way I'll be able to last long enough for both of you to grind me."
        MD "Hmmm... then we'll have to try something different."
        MD "But it's going to require at least one of us to take off their underwear."
        R "Who?"
        MD "You, stupid."
        RT "{i}Oh, God!{/i}"
        scene bg SleepBlack
        with fade
        scene bg DiazAgain25
        with fade
        L "Holy fuck, [ryan], you're so hard!"
        MD "More like, \"Holy fuck, [ryan], you're so huge!\""
        MD "I can't get over the size of this porn-sized cock!"
        L "So... how are we going to do this?"
        MD "Just take off your skirt, and follow my lead."
        scene bg SleepBlack
        with fade
        scene bg DiazVisit38
        with fade
        ADT "{i}Finally! It's such a fucking pain to change clothes in the car.{/i}"
        scene bg DiazVisit39
        with fade
        ADT "{i}I hope I didn't take too long.{/i}"
        ADT "{i}I would hate to miss out on their after-Diaz visit ritual.{/i}"
        scene bg NDiazVisit40
        with dissolve
        ADT "{i}Oh, well now.... this is interesting!{/i}"
        ADT "{i}I didn't think he'd be able to get Mandy involved this quickly!{/i}"
        ADT "{i}What could he have said to them to make this happen?{/i}"
        ADT "{i}I'm starting to respect this kid's game!{/i}"
        scene bg DiazAgain26
        with fade
        ADT "{i}That's fucking hot!{/i}"
        scene bg NDiazVisit42 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg NDiazVisit43 with Dissolve (0.5)
        $ renpy.pause (1.0)
        play sound Diaz01 loop
        scene bg NDiazVisit42 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg NDiazVisit43 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg NDiazVisit42 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg NDiazVisit43 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg NDiazVisit42 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg NDiazVisit43 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg NDiazVisit42 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg NDiazVisit43 with Dissolve (0.5)
        $ renpy.pause (1.0)
        stop sound fadeout 1.0
        scene bg SleepBlack
        with fade
        scene DiazAgainVideo03
        with fade
        $ renpy.pause ()
        RT "{i}Oh, God!... This might be the best day of my life!{/i}"
        RT "{i}Both my sister and my cousin, at the same time?!{/i}"
        RT "{i}How could this get any better?{/i}"
        RT "{i}Oh... right... I could be fucking them.{/i}"
        RT "{i}Soon!{/i}"
        $ renpy.pause ()
        LT "{i}Oh, my God! My brother's huge cock is sliding up and down against my pussy and ass!{/i}"
        LT "{i}And my ass is rubbing against my cousin's skinny ass cheeks!{/i}"
        LT "{i}This is the hottest thing that's ever happened to me!{/i}"
        "{i}{b}\"Lauren's Libido +5\"{/b}{/i}"
        $ laurenlibido += 5
        $ renpy.pause ()
        MDT "{i}God, yes! Finally I've got a cock rubbing against my virgin pussy and ass!{/i}"
        MDT "{i}If Mom could see me now! Haha!.. She'd cut [ryan]'s balls off!{/i}"
        MDT "{i}Self-righteous slut.{/i}"
        "{i}{b}\"Mandy's Libido +5\"{/b}{/i}"
        $ cousinlibido += 5
        $ renpy.pause ()
        R "Oh, fuck!... This feels incredible!"
        R "I'm gonna cum!"
        MD "Let it out. You deserve it."
        R "Oh, God!"
        play sound Ejaculate
        scene bg DiazAgain27
        with dissolve
        with hpunch
        $ renpy.pause ()
        play sound Ejaculate
        scene bg DiazAgain28
        with dissolve
        with vpunch
        $ renpy.pause ()
        scene bg DiazAgain29
        with dissolve
        MD "That... is a lot of cum!"
        L "Yeah, it's running down my back, into my panties."
        MD "I dare you to wear those panties to school."
        L "Euw... that's gross... they'll be all smelly and crusty."
        MD "Chicken."
        L "Fine... I will if you do."
        MD "Deal."
        R "You two are too much!"
        "{i}\"Girls giggling\"{/i}"
        scene bg DiazAgain30
        with dissolve
        play music Honey
        MD "[ryan], really, thank you so much for rescuing us from that sadistic bitch."
        L "Yeah... we know another thousand dollars a week is expensive, but we'll keep rewarding you like this if you'll keep paying to keep us safe."
        R "I'll try my hardest."
        MD "Hehehe... that's pretty hard."
        L "Now we've really got to get ready for school."
        L "Do you think I'll see you there today?"
        R "Maybe."
        if not mandy_at_school:
            MD "I hope I can get transferred to your school soon. It would be so fun being there with you two."
            L "Oh my God, that would be so fun!"
        else:
            pass
        R "Alright, I'd better run and get ready myself."
        MD "Maybe we'll see you tonight."
        scene bg RyansRoom01
        with fade
        $ saved_their_asses = True
        $ timeofdaycounter += 1
        jump myroom
    else:
        scene bg DiazAgain17
        with fade
        R "Oh, wow! You're already in your sexy schoolgirl outfits!"
        L "Well of course, we want to thank you, silly."
        R "Thank me how?"
        MD "Come sit on the bed and we'll show you."
        scene bg SleepBlack
        with fade
        MD "I'll get the music."
        play music ClubMusic
        scene bg DiazAgain22
        with fade
        RT "{i}Holy shit! Look at those two go at it! This is sexy as hell!{/i}"
        RT "{i}Mandy grinding up against Lauren's sexy ass again!... Fuck, I'm hard as a rock!{/i}"
        scene bg DiazAgain23
        with dissolve
        RT "{i}Oh, God!... I want both of those asses!{/i}"
        RT "{i}Lauren's soft, curvy ass, and Mandy's skinny, muscular ass.{/i}"
        RT "{i}Thank you Diaz, for making this possible!{/i}"
        play music SexMusic
        scene bg DiazAgain24
        with dissolve
        MD "And now it's time for the other part of your reward."
        L "[ryan], go on and take off your underwear."
        RT "{i}Oh, God!{/i}"
        scene bg SleepBlack
        with fade
        scene bg DiazAgain25
        with fade
        L "Holy fuck, [ryan], you're so hard!"
        MD "More like, \"Holy fuck, [ryan], you're so huge!\""
        MD "I still can't get over the size of this porn-sized cock!"
        L "I can't wait any longer. Let's just take off our skirts already."
        scene bg SleepBlack
        with fade
        scene bg DiazVisit38
        with fade
        $ renpy.pause ()
        scene bg DiazVisit39
        with fade
        ADT "{i}I hope I didn't take too long.{/i}"
        ADT "{i}I would hate to miss out on their after-Diaz visit ritual.{/i}"
        scene bg NDiazVisit40
        with dissolve
        ADT "{i}Haha... I'd say my visit is an aphrodisiac!{/i}"
        scene bg DiazAgain26
        with fade
        ADT "{i}That's fucking hot!{/i}"
        scene bg NDiazVisit42 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg NDiazVisit43 with Dissolve (0.5)
        $ renpy.pause (1.0)
        play sound Diaz01 loop
        scene bg NDiazVisit42 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg NDiazVisit43 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg NDiazVisit42 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg NDiazVisit43 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg NDiazVisit42 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg NDiazVisit43 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg NDiazVisit42 with Dissolve (0.5)
        $ renpy.pause (1.0)
        scene bg NDiazVisit43 with Dissolve (0.5)
        $ renpy.pause (1.0)
        stop sound fadeout 1.0
        scene bg SleepBlack
        with fade
        scene DiazAgainVideo03
        with fade
        $ renpy.pause ()
        RT "{i}Oh, God!... This feels so good!{/i}"
        RT "{i}Both my sister and my cousin, at the same time?!{/i}"
        RT "{i}How could this get any better?{/i}"
        RT "{i}Oh... right... I could be fucking them.{/i}"
        RT "{i}Soon!{/i}"
        $ renpy.pause ()
        LT "{i}Oh, my God! My brother's huge cock is sliding up and down against my pussy and ass!{/i}"
        LT "{i}And my ass is rubbing against my cousin's skinny ass cheeks!{/i}"
        LT "{i}This is the hottest thing that's ever happened to me!{/i}"
        "{i}{b}\"Lauren's Libido +3\"{/b}{/i}"
        $ laurenlibido += 3
        $ renpy.pause ()
        MDT "{i}God, yes! Finally I've got a cock rubbing against my virgin pussy and ass!{/i}"
        MDT "{i}If Mom could see me now! Haha!.. She'd cut [ryan]'s balls off!{/i}"
        MDT "{i}Self-righteous slut.{/i}"
        "{i}{b}\"Mandy's Libido +3\"{/b}{/i}"
        $ cousinlibido += 3
        $ renpy.pause ()
        R "Oh, fuck!... This feels incredible!"
        R "I'm gonna cum!"
        MD "Let it out. You deserve it."
        R "Oh, God!"
        play sound Ejaculate
        scene bg DiazAgain27
        with dissolve
        with hpunch
        $ renpy.pause ()
        play sound Ejaculate
        scene bg DiazAgain28
        with dissolve
        with vpunch
        $ renpy.pause ()
        scene bg DiazAgain29
        with dissolve
        MD "That... is a lot of cum!"
        L "Yeah, it's running down my back, into my panties."
        MD "I dare you to wear those panties to school again."
        L "Haha... ok, it wasn't so bad last time."
        L "Are you going to do it again, too?"
        MD "If you are, definitely."
        R "You two are too much!"
        "{i}\"Girls giggling\"{/i}"
        scene bg DiazAgain30
        with dissolve
        play music Honey
        MD "[ryan], really, thank you so much for rescuing us from that sadistic bitch again."
        L "Yeah... we know a thousand dollars a week is expensive, but we'll keep rewarding you like this if you'll keep paying to keep us safe."
        R "I'll try my hardest."
        MD "Hehehe... that's pretty hard."
        L "Now we've really got to get ready for school."
        L "Do you think I'll see you there today?"
        R "Maybe."
        if not mandy_at_school:
            MD "I hope I can get transferred to your school soon. It would be so fun being there with you two."
            L "Oh my God, that would be so fun!"
        else:
            pass
        R "Alright, I'd better run and get ready myself."
        MD "Maybe we'll see you tonight."
        scene bg RyansRoom01
        with fade
        $ timeofdaycounter += 1
        jump myroom

label diaz_lauren_and_mandy:
    scene bg DiazAgain01
    with fade
    AD "Look how sweet those two look when they're asleep."
    scene bg DiazAgain02
    with dissolve
    AD "Almost like two lesbian lovers."
    if not gave_their_asses:
        R "They're not lesbians!"
        AD "Haha... how do you know?"
        R "Trust me... I know."
    else:
        R "I told you... they're not lesbians!"
        AD "Haha... I know you think so... I'm just fucking with you."
    scene bg DiazAgain01
    with dissolve
    if not gave_their_asses:
        AD "Well, trust me, a girl can change her mind."
        AD "Or just decide to swing both ways."
    else:
        pass
    AD "Do you want to wake them up, or should I?"
    R "I'll give you the honors."
    AD "Good morning, ladies!"
    scene bg DiazAgain03
    with dissolve
    MD "Oh, fuck! Look who's back."
    L "No... it's not really Thursday... is it?"
    scene bg DiazAgain04
    with dissolve
    AD "I'm afraid so... and I've got to commend you on your fake dissapointment."
    L "We're not faking!"
    LT "{i}Shit, am I really that easy to read?{/i}"
    MDT "{i}How could she tell?{/i}"
    if not gave_their_asses:
        L "Did you wake up [ryan]?... Maybe he'll pay your extortion fee this week."
        AD "He's already sold your asses to me for the morning."
    else:
        L "Fuck! [ryan] sold our asses to you again this week?"
        AD "I guess he didn't try hard enough to get the money together."
    scene bg DiazAgain05
    with dissolve
    AD "Isn't that right, [ryan]?"
    R "I'm sorry, girls! I just don't have the money to spare this week."
    scene bg DiazAgain04
    with dissolve
    RT "{i}I think Diaz is wrong, they really do seem dissapointed...{/i}"
    if money >= 1000:
        RT "{i}Shit!... Maybe I should have just paid Diaz.{/i}"
    else:
        RT "{i}Damnit!... Why wasn't I better with my money this week?{/i}"
    AD "Now the only question is, who do you want to see spanked this week?"
    if not gave_their_asses:
        R "I don't want to choose."
        AD "Well either you choose, or I spank both of them as hard as I can, for twice the amount of time."
    else:
        R "You're making me choose again?"
        AD "Either choose, or you know what happens."
        R "Fine."
    AD "So who's it going to be?"
    menu:
        "Lauren":
            $ lauren_spanked = True
            R "Sorry, Lauren."
            R "I choose you to be spanked."
            LT "{i}He chose me!?... Not that I mind being spanked so much... fuck, I kinda like it... but why would he choose me?{/i}"
            "{i}{b}\"Mandy's Affection +1\"{/b}{/i}"
            "{i}{b}\"Lauren's Affection -1\"{/b}{/i}"
            $ cousinaffection += 1
            $ laurenaffection -= 1
            AD "Alright! [ryan], why don't you step out while we get changed and get Lauren all tied up."
            scene bg SleepBlack
            with fade
            $ renpy.pause ()
            AD "Alright [ryan], you can come in."
            scene bg DiazAgain09
            with fade
            AD "Doesn't your sister look crazy sexy, all tied up?"
            RT "{i}She really does!{/i}"
            AD "Nothing to say?... Alright, let's get started."
            if not gave_their_asses:
                AD "Now, let's all imagine that I'm your school resource officer."
                AD "Mandy saw Lauren smoking in the school bathroom, and came to me to tattle."
            else:
                AD "Ok... same scenario as last time. I'm your school resource officer."
                AD "Mandy saw Lauren smoking in the school bathroom again, and came to me to tattle."
            AD "As a reward for squealing on her peer, I gave her the option to help me punish her."
            AD "And Mandy enthusiastically accepted!"
            AD "Mandy, stay at the foot of the bed, and Lauren... head down, ass up."
            scene bg SleepBlack
            with fade
            scene bg DiazAgainVideo02F01
            with fade
            MD "Do I really have to do this?"
            AD "No, but if you want to keep living here you do."
            AD "And make sure you do it hard enough to hurt."
            AD "If you're too pussy about it, I'll spank you both."
            MD "Fine... I'm sorry, Lauren!"
            scene DiazAgainVideo02
            with fade
            play sound Muffled loop
            $ renpy.pause ()
            MD "When can I stop?"
            AD "Keep going until I tell you."
            RT "{i}Diaz is such a sadistic bitch!{/i}"
            if not gave_their_asses:
                RT "{i}This is so messed up!{/i}"
                RT "{i}So, why is it making me so hard?{/i}"
            else:
                RT "{i}But I'm the one who let it happen.{/i}"
                RT "{i}And my dick's harder than diamonds... maybe I'm a sadist too?{/i}"
            $ renpy.pause ()
            LT "{i}Oww... my ass is so sensitive!{/i}"
            LT "{i}This really hurts!...{/i}"
            LT "{i}So why do I kind of like it?{/i}"
            LT "...."
            LT "{i}This is starting to make me wet!{/i}"
            LT "{i}Fuck! Mandy is going to notice!{/i}"
            "{i}{b}\"Lauren's Libido +3\"{/b}{/i}"
            $ laurenlibido += 3
            $ renpy.pause ()
            MDT "{i}As if my life couldn't get any weirder, now I'm being forced to spank my cousins!{/i}"
            MDT "{i}I'm being blackmailed by an authoritative, dominatrix-like woman! Could this get any kinkier?{/i}"
            MDT "...."
            if not gave_their_asses:
                MDT "{i}OH MY GOD!! Are Lauren's panties starting to get wet?{/i}"
            else:
                MDT "{i}OH MY GOD!! Are Lauren's panties getting wet again?{/i}"
            MDT "{i}Could she really be getting this turned on? Or is her bladder leaking from fright?{/i}"
            MDT "{i}Is Lauren into this?{/i}"
            MDT "{i}If she's enjoying my hand slapping her ass cheeks... Fuck!... Now I'm super turned on!{/i}"
            MDT "{i}At least nobody can see my panties.{/i}"
            "{i}{b}\"Mandy's Libido +3\"{/b}{/i}"
            $ cousinlibido += 3
            $ renpy.pause ()
            ADT "{i}I love this job!{/i}"
            ADT "{i}It's a rare thing to find a family that's this perverted.{/i}"
            if not gave_their_asses:
                ADT "{i}I wouldn't be able to get away with this with most people...{/i}"
                ADT "{i}But after reading their digital journals and seeing their browser histories, I know I'm just helping them fulfill their deepest and most secret desires.{/i}"
            else:
                ADT "{i}And they've let me do this multiple times now!{/i}"
                ADT "{i}They're so into this!{/i}"
            $ renpy.pause ()
            AD "Alright... I think Lauren's probably had enough fun for today."
            AD "You can stop, Mandy."
            stop sound
            scene bg DiazAgain11
            with fade
            AD "I think Lauren has learned her lesson."
            AD "Are you ever going to smoke in the girl's bathroom again?"
            play sound Muffled
            L "Mmmmpphhh!"
            stop sound
            "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
            $ laurensubmission += 1
        "Mandy":
            $ mandy_spanked = True
            R "Sorry, Mandy."
            R "I choose you to be spanked."
            MDT "{i}He chose me!?... That fucker has got a soft spot in his heart for his sister...{/i}"
            "{i}{b}\"Mandy's Affection -1\"{/b}{/i}"
            "{i}{b}\"Lauren's Affection +1\"{/b}{/i}"
            $ cousinaffection -= 1
            $ laurenaffection += 1
            AD "Alright! [ryan], why don't you step out while we get changed and get Mandy all tied up."
            scene bg SleepBlack
            with fade
            $ renpy.pause ()
            AD "Alright [ryan], you can come in."
            scene bg DiazAgain10
            with fade
            AD "Doesn't your cousin look crazy sexy, all tied up?"
            RT "{i}She really does!{/i}"
            AD "Nothing to say?... Alright, let's get started."
            if not gave_their_asses:
                AD "Now, let's all imagine that I'm your school resource officer."
                AD "Lauren saw Mandy smoking in the school bathroom, and came to me to tattle."
            else:
                AD "Ok... same scenario as last time. I'm your school resource officer."
                AD "Lauren saw Mandy smoking in the school bathroom again, and came to me to tattle."
            AD "As a reward for squealing on her peer, I gave her the option to help me punish her."
            AD "And Lauren enthusiastically accepted!"
            AD "Lauren, stay at the foot of the bed, and Mandy... head down, ass up."
            scene bg SleepBlack
            with fade
            scene bg DiazAgainVideo01F01
            with fade
            L "Do I really have to do this?"
            AD "No, but if you want to stay out of jail, you do."
            AD "And make sure you do it hard enough to hurt."
            AD "If you're too pussy about it, I'll spank you both."
            L "Fine... I'm sorry, Mandy!"
            scene DiazAgainVideo01
            with fade
            play sound Muffled loop
            $ renpy.pause ()
            L "When can I stop?"
            AD "Keep going until I tell you."
            RT "{i}Diaz is such a sadistic bitch!{/i}"
            if not gave_their_asses:
                RT "{i}This is so messed up!{/i}"
                RT "{i}So, why is it making me so hard?{/i}"
            else:
                RT "{i}But I'm the one who let it happen.{/i}"
                RT "{i}And my dick's harder than diamonds... maybe I'm a sadist too?{/i}"
            $ renpy.pause ()
            MDT "{i}Oww... my ass is so sensitive!{/i}"
            MDT "{i}This really hurts!...{/i}"
            MDT "{i}So why do I kind of like it?{/i}"
            MDT "...."
            MDT "{i}This is starting to make me wet!{/i}"
            MDT "{i}Fuck! Lauren is going to notice!{/i}"
            "{i}{b}\"Mandy's Libido +3\"{/b}{/i}"
            $ cousinlibido += 3
            $ renpy.pause ()
            LT "{i}As if my life couldn't get any weirder, now I'm being forced to spank my cousin!{/i}"
            LT "{i}I'm being blackmailed by an authoritative, dominatrix-like woman! Could this get any kinkier?{/i}"
            LT "...."
            if not gave_their_asses:
                LT "{i}OH MY GOD!! Are Mandy's panties starting to get wet?{/i}"
            else:
                LT "{i}OH MY GOD!! Are Mandy's panties getting wet again?{/i}"
            LT "{i}Could she really be getting this turned on? Or is her bladder leaking from fright?{/i}"
            LT "{i}Is Mandy into this?{/i}"
            LT "{i}If she's enjoying my hand slapping her ass cheeks... Fuck!... Now I'm super turned on!{/i}"
            LT "{i}At least nobody can see my panties.{/i}"
            "{i}{b}\"Lauren's Libido +3\"{/b}{/i}"
            $ laurenlibido += 3
            $ renpy.pause ()
            ADT "{i}I love this job!{/i}"
            ADT "{i}It's a rare thing to find a family that's this perverted.{/i}"
            if not gave_their_asses:
                ADT "{i}I wouldn't be able to get away with this with most people...{/i}"
                ADT "{i}But after reading their digital journals and seeing their browser histories, I know I'm just helping them fulfill their deepest and most secret desires.{/i}"
            else:
                ADT "{i}And they've let me do this multiple times now!{/i}"
                ADT "{i}They're so into this!{/i}"
            $ renpy.pause ()
            AD "Alright... I think Mandy's probably had enough fun for today."
            AD "You can stop, Lauren."
            stop sound
            scene bg DiazAgain11
            with fade
            AD "I think Mandy has learned her lesson."
            AD "Are you ever going to smoke in the girl's bathroom again?"
            play sound Muffled
            MD "Mmmmpphhh!"
            stop sound
            "{i}{b}\"Mandy's Submission +1\"{/b}{/i}"
            $ cousinsubmission += 1
    AD "Haha... that's what I thought."
    scene bg SleepBlack
    with fade
    $ renpy.pause ()
    scene bg DiazAgain13
    with fade
    AD "Wow!... That got me all worked up."
    AD "{i}(whispering to [ryan]){/i} I'm going to go take care of myself in my car."
    if not gave_their_asses:
        AD "{i}(whispering){/i} And don't feel too bad. I've seen their browser histories... they're totally into this."
    else:
        AD "{i}(whispering){/i} I'm not lying to you. They're way into this... they both looked up BDSM porn like crazy after the last time we did this."
    scene bg DiazAgain14
    with dissolve
    RT "{i}Holy shit!... Is Agent Diaz right?  Did they secretly enjoy that?{/i}"
    R "Are you girls ok?"
    scene bg DiazAgain15
    with dissolve
    if lauren_spanked:
        L "Well, besides the fact that I was tied up, gagged, and was spanked raw by my cousin, who was blackmailed into it... {i}(sarcastic tone){/i} Yeah, I'm great!"
        LT "{i}Shit!... Why did I like that? What is wrong with me?... I wonder if Mandy noticed that my panties were soaked.{/i}"
    else:
        MD "Well, besides the fact that I was tied up, gagged, and was spanked raw by my cousins, who was blackmailed into it... {i}(sarcastic tone){/i} Yeah, I'm great!"
        MDT "{i}Shit!... Why did I like that? What is wrong with me?... I wonder if Lauren noticed that my panties were soaked.{/i}"
    scene bg DiazAgain16
    with dissolve
    if lauren_spanked:
        MD "I'm so sorry! I really didn't want to do that."
        MDT "{i}Fuck, why was spanking Lauren so fun?{/i}"
        MDT "{i}I really need to rub one out now.{/i}"
        L "I know... it was fucking Agent Diaz!"
    else:
        L "I'm so sorry! I really didn't want to do that."
        LT "{i}Fuck, why was spanking Mandy so fun?{/i}"
        LT "{i}I really need to rub one out now.{/i}"
        MD "I know... it was fucking Agent Diaz!"
    scene bg DiazAgain15
    with dissolve
    if lauren_spanked:
        L "And [ryan], for choosing to have me spanked!"
    else:
        MD "And [ryan], for choosing to have me spanked!"
    R "I'm sorry, but I had to choose one of you!"
    R "I didn't have the money to spare this week, but I'll try as hard as I can next week."
    scene bg DiazAgain17
    with dissolve
    L "Oh, please do!"
    LT "{i}I can't let this new fetish get any stronger!{/i}"
    MD "Yes, please try your hardest!"
    MDT "{i}Or don't... we've got to save that money to corrupt my mom!{/i}"
    MDT "{i}And I wouldn't mind doing that again!{/i}"
    R "Alright... well, I'll let you finish getting ready for school.  I'm going to try to make some more money to save your asses next week."
    scene bg LaurenDoor
    with fade
    RT "{i}I'm not sure... they didn't seem to enjoy that... and even if they did... do I really want them to become corrupted in that way?{/i}"
    $ timeofdaycounter += 1
    $ gave_their_asses = True
    play music Honey
    jump myroom

#############  JACKY'S OFFICE  ##############################  JACKY'S OFFICE  #################################################

label both_caught:                      #### Edited 9-2-2020 ####
    if blackmailed_mom_matt == True or blackmailed_mom_megan == True:
        scene bg SleepBlack
        with fade
        RT "{i}Hmmmm... her door's shut again. I'll bet she's at it again. I'll Just take a peek.{/i}"
        scene bg MCaughtInOffice01
        with fade
        RT "{i}Haha... yep!... She must really be missing Dad to be trying to squeeze a session in before class.{/i}"
        RT "{i}Now that Mom's given me a handjob, maybe I can get her to give me one here in her office too.{/i}"
        play music SexMusic
        play sound Mom02 loop
        scene bg MCaughtInOffice02
        with dissolve
        $ renpy.pause (0.03)
        scene bg MCaughtInOffice01
        with dissolve
        $ renpy.pause (0.03)
        scene bg MCaughtInOffice02
        with dissolve
        $ renpy.pause (0.03)
        scene bg MCaughtInOffice01
        with dissolve
        $ renpy.pause (0.03)
        RT "{i}Now looks like a good time.{/i}"
        R "Uhhuuuhhemmmmm?"
        stop sound
        scene bg MCaughtInOffice03
        with dissolve
        play sound LaptopShut
        M "[ryan]!... You scared the hell out of me again!?"
        M "Why won't the school board just let us put locks on our office doors?"
        R "Probably so that you'll give your students your attention during school hours, rather than attending to personal business."
        scene bg MCaughtInOffice04
        M "Don't be a prick."
        M "And can't you just wait until I'm finished?"
        R "You know this is the only time I have to see you about school assignments."
        M "Alright, well come in, and we'll get to work."
        scene bg MCaughtInOffice05
        with fade
        M "Let's just pick up from where we left off."
        M "Maybe there's more scenes in this game that will be good to mention in your paper."
        scene bg MCaughtInOffice06
        with dissolve
        M "Darn it."
        M "I forgot to save the last time we played. We'll just have to click through the scenes quickly without reading it."
        M "Oh, and before I forget, you might as well take it out right now before you put anymore strain on the stitching of those pants, and I'll make myself comfortable too."
        R "{i}Wow, she seems to be jumping right into it this time.{/i}"
        scene bg MCaughtInOffice11
        with dissolve
        MT "{i}Uuuggghhh... why does that little motherfucker... I mean just fucker... always have to catch me when I'm horny in my office.{/i}"
        MT "{i}I'm already out of control! I've already invited him to take his dick out and pulled my skirt up to my waist.{/i}"
        MT "{i}Ok, [mom_name]!... Use a little self-control... do not look over at his cock!{/i}"
        scene bg MCaughtInOffice14
        with dissolve
        MT "{i}Shit!{/i}"
        scene OfficeVideo02
        with fade
        $ renpy.pause ()
        MT "{i}Why am I doing this?{/i}"
        MT "{i}I have so little self-control when I'm horny.{/i}"
        MT "{i}And God help me that I can't wait for my fucking son to join in.{/i}"
        scene OfficeVideo03
        with fade
        $ renpy.pause ()
        MT "{i}Damnit! Why does this turn me on so much?{/i}"
        MT "..."
        R "Mom?"
        M "Not now, [ryan]."
        R "I just wanted to ask if you'd give me a handjob."
        M "I can't even believe you would ask me that after what happened last time."
        M "Like I told you before, from now on, that's only a reward for paying the mafia debt each week."
        R "Please!"
        M "Push it, and I'll stop doing it completely."
        R "Fine!"
        RT "{i}I think the time will be right very soon to push things a little further... I'll just enjoy this for now.{/i}"
        RT "{i}Oh... fuck...{/i}"
        scene bg BlurryWhite
        with fade
        with vpunch
        with hpunch
        scene bg MCaughtInOffice20
        with fade
        scene bg BlurryWhite
        with fade
        with vpunch
        with hpunch
        scene bg MCaughtInOffice33
        with fade
        M "Haha... did you see that!?"
        M "I caught it again!"
        R "Haha... I can't believe how excited you get about that!"
        M "Yeah, well I've decided I'm happy to see you practicing good health habits."
        R "You're so cool!"
        "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
        $ momlibido += 1
        M "Now run along so I can finish taking care of myself before I go to class."
        R "Wait! Take care of yourself how?"
        M "I think you know what I mean."
        R "Can I watch?"
        MT "{i}This kid needs to get the fuck out of my office!! I don't have much time before class!{/i}"
        M "Now please hurry along... before I cut your cock off."
        R "Ok... I'm going!"
        $ mm_fuckedtoday = True
        play music Honey
        scene bg SchoolHallway01
        with fade
        jump school
    else:
        if ntrcontent:
            scene bg BlurryWhite
            with fade
            "{i}\"This is a mandatory check of the game's NTR system.\"{/i}"
            "{i}\"Currently your game settings are set to allow NTR content.\"{/i}"
            "{i}\"Unless your settings are changed, the following series of scenes will contain NTR content.\"{/i}"
            "{i}\"Would you like to take this opportunity to turn off the NTR content?]\"{/i}"
            menu:
                "Yes! I don't want to see any NTR shit!":
                    P1 "How the fuck did that get turned on?"
                    P1 "I swear I wasn't experimenting with any new kinks!"
                    "{i}\"(NTR Content turned off)\"{/i}"
                    $ ntrcontent = False
                "No, for fucks sake! Stop asking. Let me enjoy my punishment.":
                    P1 "Fucking babies, that are always complaining about NTR content..."
                    P1 "can't let a developer make a game without pasting NTR warnings everywhere!"
                    "{i}\"(NTR Content will remain turned on)\"{/i}"
            "Back at Mom's office door."
        else:
            pass
        scene bg SleepBlack
        with fade
        RT "{i}Hmmmm... her door's shut again. I'll bet she's at it again. I'll Just take a peek.{/i}"
        scene bg MCaughtInOffice01
        with fade
        RT "{i}Haha... yep!... She must really be missing Dad to be trying to squeeze a session in before class.{/i}"
        RT "{i}Now that Mom's given me a handjob, maybe I can get her to give me one here in her office too.{/i}"
        play music SexMusic
        play sound Mom02 loop
        scene bg MCaughtInOffice02
        with dissolve
        $ renpy.pause (0.03)
        scene bg MCaughtInOffice01
        with dissolve
        $ renpy.pause (0.03)
        scene bg MCaughtInOffice02
        with dissolve
        $ renpy.pause (0.03)
        scene bg MCaughtInOffice01
        with dissolve
        $ renpy.pause (0.03)
        RT "{i}Now looks like a good time.{/i}"
        R "Uhhuuuhhemmmmm?"
        stop sound
        scene bg MCaughtInOffice03
        with dissolve
        play sound LaptopShut
        M "[ryan]!... You scared the hell out of me again!?"
        M "Why won't the school board just let us put locks on our office doors?"
        R "Probably so that you'll give your students your attention during school hours, rather than attending to personal business."
        scene bg MCaughtInOffice04
        M "Don't be a prick."
        M "And can't you just wait until I'm finished?"
        R "You know this is the only time I have to see you about school assignments."
        M "Alright, well come in, and we'll get to work."
        scene bg MCaughtInOffice05
        with fade
        M "Let's just pick up from where we left off."
        M "Maybe there's more scenes in this game that will be good to mention in your paper."
        scene bg MCaughtInOffice06
        with dissolve
        M "Darn it."
        M "I forgot to save the last time we played. We'll just have to click through the scenes quickly without reading it."
        M "Oh, and before I forget, you might as well take it out right now before you put anymore strain on the stitching of those pants, and I'll make myself comfortable too."
        R "{i}Wow, she seems to be jumping right into it this time.{/i}"
        scene bg MCaughtInOffice11
        with dissolve
        MT "{i}Uuuggghhh... why does that little motherfucker... I mean just fucker... always have to catch me when I'm horny in my office.{/i}"
        MT "{i}I'm already out of control! I've already invited him to take his dick out and pulled my skirt up to my waist.{/i}"
        MT "{i}Ok, [mom_name]!... Use a little self-control... do not look over at his cock!{/i}"
        scene bg MCaughtInOffice14
        with dissolve
        MT "{i}Shit!{/i}"
        scene OfficeVideo02
        with fade
        $ renpy.pause ()
        MT "{i}Why am I doing this?{/i}"
        MT "{i}I have so little self-control when I'm horny.{/i}"
        MT "{i}And God help me that I can't wait for my fucking son to join in.{/i}"
        scene OfficeVideo03
        with fade
        $ renpy.pause ()
        MT "{i}Damnit! Why does this turn me on so much?{/i}"
        MT "..."
        R "Mom?"
        M "Not now, [ryan]."
        R "I just wanted to ask if you'd give me a handjob."
        MT "{i}Why do I want that huge cock in my hands so badly?{/i}"
        M "That's supposed to be a reward for paying the weekly Mafia debt."
        M "I don't want you to think you can have one any time you want to."
        MT "{i}If only I didn't want to give him another one right now.{/i}"
        MT "{i}If he presses, I won't be able to say no.{/i}"
        R "I know... it's just that I'm feeling really backed up, and when I take care of myself, I'm just not able to get as much out as you can."
        M "Are you trying to tell me it's a matter of your health then?"
        R "Absolutely."
        MT "{i}What a bunch of bullshit!{/i}"
        MT "{i}But at least it gives me an excuse as well.{/i}"
        M "Ok fine, but just this once."
        R "I can live with that."
        scene OfficeVideo04
        with fade
        M "You're even harder than usual."
        R "Something about doing this at school turns me on even more."
        M "Haha... you must get that from me."
        M "Even before your dad was arrested, I would sneak in a session in my office now and then."
        M "Fuck! Why did I just tell you that?"
        MT "{i}It's like I can't think straight with a huge cock in my hands.{/i}"
        R "It's ok, Mom... I love hearing how much we have in common."
        M "Please don't call me Mom in my office..."
        M "Please call me Miss [mom_name]."
        R "So you're saying doing this to your son is weird, but you're ok with doing this to your students?"
        M "No..."
        MT "{i}Maybe?{/i}"
        M "If you want me to finish, then you better stop being such a smartass."
        R "Yeah, you've got a class starting pretty soon."
        R "I'll finish sooner if you talk dirty to me."
        M "Or you won't finish at all, if I stop."
        MT "{i}I don't want to stop.{/i}"
        MT "{i}I want to see that cock shoot cum all over!{/i}"
        M "But... for your sexual health..."
        M "..."
        M "I love this massive cock!"
        R "Ohhh..."
        M "Please... I need to see it cum!"
        MT "{i}Uuugghh... I should not be talking to my son like this!{/i}"
        M "I need your cum in my mouth!"
        MT "{i}This is so wrong!{/i}"
        M "I need it all over my face!"
        MT "{i}This is so weird!{/i}"
        M "Please!... Cover me!"
        MT "{i}So... weirdly arousing!{/i}"
        R "Oh, fuck!"
        play sound Ejaculate
        scene bg Office01
        with dissolve
        with hpunch
        MT "{i}Oh, shit! He didn't give me any warning!{/i}"
        play sound Ejaculate
        scene bg Office02
        with dissolve
        MT "{i}Aaahh... he's covering me!{/i}"
        if ntrcontent:
            scene bg Office03
            with fade
            MB "Holy fuck!"
            scene bg Office04
            with dissolve
            M "Oh, my God! Matt!"
            MT "{i}Goddamned doors without locks!{/i}"
            MB "Hahaha..."
            MB "I knew there was something weird going on between the two of you."
            M "Matt! It's not what you're thinking!"
            MB "Really?... So that isn't [ryan]'s cum all over your face?"
            M "Not so loud! Get in here and shut the door! Let's talk about this!"
            scene bg SleepBlack
            with fade
            scene bg Office05
            with fade
            MB "I think you'll find that I'm pretty accepting and open to people and their sexual perversions."
            M "I wasn't lying... this really isn't what you think it is."
            scene bg Office06
            with fade
            MB "Let me guess..."
            MB "[ryan]'s got carpal tunnel syndrome, or some kind of crazy reason why he can't jerk himself off, so you're just helping him to not get too backed up?"
            scene bg Office07
            with dissolve
            M "Oh, my God... you've played \"Big Brother\" too?"
            MB "Well... yeah... those kind of games have been pretty popular with all the kids at school for a few years... Wait! You've played \"Big Brother\"?"
            M "Well, I've been doing a bunch of research so I can teach the Oedipal curriculum, and [ryan] showed me a few of those games."
            MB "Hahah... nice one, [ryan]! Classic porn game protagonist type of move!"
            scene bg Office08
            with dissolve
            MB "Respect!"
            M "Is that why you showed me those games? To groom me like a conquest in a porn game?"
            R "No!... Shut up Matt, you don't know what you're talking about."
            R "I just thought they would be a compelling piece of evidence to validate Freud's Oedipus theories. You know, for my final project."
            R "If I was trying to groom you like in a porn game, do you think I'd be stupid enough to show you how women get groomed in porn games?"
            RT "{i}That really was stupid of me.{/i}"
            scene bg Office09
            with dissolve
            M "Hmmm... that had better be the case!"
            scene bg Office10
            with dissolve
            M "So, to explain what we were doing, it's going to sound weird, expecially since it's a little bit theoretical, even though it's backed up by significant research."
            M "{b}{i}Doctor{/i}{/b} Will Tylor, a famous psychologist, who also happens to be a member of our school board, published a study about how young men can get stuck in an Oedipal phase if they aren't allowed to let it develop and go away on their own."
            scene bg Office09
            with dissolve
            M "My son has started exhibiting symptoms of a slight Oedipal complex.  Sorry to embarrass you, [ryan]."
            R "Oh, God..."
            scene bg Office10
            with dissolve
            M "So I'm trying to help him get through it by letting it take it's course naturally, rather than trying to cut it off, and make him get stuck in it."
            M "It just involves a few handjobs from time to time. And it will never go any farther than that."
            scene bg Office11
            with dissolve
            M "Isn't that right, [ryan]?"
            R "... Oh... yeah... of course..."
            scene bg Office12
            with dissolve
            $ renpy.pause ()
            scene bg Office10
            with dissolve
            M "So that's all that's going on... not as terrible as you were probably imagining."
            scene bg Office14
            with fade
            MB "No... not quite as terrible."
            M "So... I'm hoping we can keep all of this between us?"
            MB "Yeah, I have no desire to stir up any trouble, but there is just a small thing I want from you."
            M "Oh, shit! Here we go."
            MB "No! It's not as terrible as you think, either."
            MB "But it is something you probably wouldn't do, unless I had some leverage over you."
            scene bg Office07
            with fade
            M "You don't have any leverage... I could defend my position to the school board."
            M "Especially with Will Tylor there to support me with his research."
            MB "Yeah, but a school board hearing would make this all very public, and I think people's imaginations will make them believe that much more is going on between you and your son."
            MT "{i}Dammit! That could ruin both of our reputations.  We would probably have to move. But I'm sure the FBI wouldn't let us.{/i}"
            MB "Don't get too defensive until you hear what it is that I want."
            scene bg Office15
            with fade
            MB "I'm sure you're already aware, but [ryan] has a photo studio that's beginning to do fairly well."
            M "I know it's bringing in a little money each week."
            M "And I know his sisters have been posing for pictures, in outfits that Sidney has designed."
            scene bg Office14
            with dissolve
            MB "Exactly... and those shoots have started to get a good amount of attention online."
            scene bg Office10
            with dissolve
            M "Oh, really?"
            MB "Yeah, in fact my girlfriend Megan won't shut up about it."
            M "Oh, Megan's such a nice girl."
            MB "Sure, but she's been trying to get internet famous for years by posting pics and vids of her cheerleading stuff, and makeup and fashion tutorials."
            MB "But besides the occasional creepy stalker, she hasn't been able to get a very good following."
            MB "But I think [ryan]'s got a good thing going with his studio."
            MB "Cosplay is extremely popular right now."
            scene bg Office09
            with dissolve
            M "Well, I'm sure that [ryan] would be more than happy to take some pictures of Mandy in cosplay."
            M "Wouldn't you, [ryan]?"
            R "Ummm... yeah... I'd love to get another model in there."
            MB "Great, but here's the part you're not going to like, Miss [mom_name]."
            MB "I have a feeling the photoshoot will be ten times more popular if she's posing with a beautiful, sexy, more mature woman."
            scene bg Office06
            with dissolve
            M "You mean me."
            MB "Yes."
            M "There's no way!... I can't pose in sexy photos with one of my students!"
            scene bg Office07
            with dissolve
            M "That would destroy my reputation."
            MB "Destroy it? No... When I was a freshman, a video leaked of Miss Stone fucking one of her students, and now her class fills up faster than any other."
            MB "It's mostly boys, but the event only boosted her status among the students."
            MB "I was really surprised she didn't get fired."
            M "That's because the student was over 18, and the state has a law that schools can't punish teachers for that type of behavior if the student is a consenting adult."
            M "They didn't even bring it before the school board because there were no grounds for dimissal."
            M "It probably helped that she has tenure as well."
            R "You have tenure too, Miss [mom_name]."
            scene bg Office08
            with dissolve
            M "Shut up, [ryan]!"
            scene bg Office14
            with fade
            MB "[ryan] could even put the pictures behind a paywall for premium members, then probably none of your students would see the pics, since almost none of us have access to credit cards."
            scene bg Office13
            with fade
            MT "{i}Let's see... a formal investigation and scandal for incest, or taking sexy pics with a student, which probably no one will see?{/i}"
            scene bg Office14
            with dissolve
            M "Fine!... I'll do the photoshoot."
            MB "That's awesome!"
            MB "And just a few more details."
            scene bg Office15
            with dissolve
            MB "I get to direct the shoot."
            MB "[ryan], I want you to create the background with your Photochop and 3d modeling skills."
            scene bg Office10
            with fade
            MB "And Megan loves the Perry Hotter movies and books."
            MB "So I want you to get some Perry Hotter cosplay outfits."
            MB "I'm thinking a student and a teacher outfit."
            R "Really? Isn't Perry Hotter kind of juvenile?"
            scene bg Office11
            with dissolve
            M "If you had actually read the books then you'd know they appeal to all ages."
            R "Ok... sorry."
            M "You should be!"
            R "So, who's going to pay for the cosplay outfits?"
            scene bg Office09
            with dissolve
            M "Who do you think?"
            R "Me? But why am I getting stuck with the bill?"
            M "All my wages are garnished by the FBI, and I hardly think our extortioner is going to offer to pick up the bill."
            MB "You thought right."
            R "Fine!"
            R "I'll give Sidney the money the next time I see her."
            scene bg Office15
            with fade
            MB "This is so awesome! I can't wait to tell Megan the good news! Just let me know when Sidney's got the costumes all made."
            R "... fine."
            scene bg SleepBlack
            with fade
            RT "{i}Goddammit, I don't want Matt at my photo studio. That's supposed to be my place to be alone with girls. I don't need another guy competing with me in my own space!{/i}"
            RT "{i}But, I don't think there's anything I can do about it now.{/i}"
            $ mm_fuckedtoday = True
            $ blackmailed_mom_matt = True
            $ persistent.gal_NTR_4 = True
            play music Honey
            scene bg SchoolHallway01
            with fade
            jump school
        else:
            scene bg Office16
            with fade
            MG "Holy fuck!"
            scene bg Office17
            with dissolve
            M "Oh, my God! Megan!"
            MT "{i}Goddamned doors without locks!{/i}"
            MG "Hahaha..."
            MG "I knew there was something weird going on between the two of you."
            M "Megan! It's not what you're thinking!"
            MG "Really?... So that isn't [ryan]'s cum all over your face?"
            M "Not so loud! Get in here and shut the door! Let's talk about this!"
            scene bg SleepBlack
            with fade
            scene bg Office18
            with fade
            MG "I think you'll find that I'm pretty accepting and open to people and their sexual perversions."
            M "I wasn't lying... this really isn't what you think it is."
            scene bg Office06
            with fade
            MG "Let me guess..."
            MG "[ryan]'s got carpal tunnel syndrome, or some kind of crazy reason why he can't jerk himself off, so you're just helping him to not get too backed up?"
            scene bg Office07
            with dissolve
            M "Oh, my God... you've played \"Big Brother\" too?"
            MG "Well... yeah... those kind of games have been pretty popular with all the kids at school for a few years... Wait! You've played \"Big Brother\"?"
            M "Well, I've been doing a bunch of research so I can teach the Oedipal curriculum, and [ryan] showed me a few of those games."
            MG "Hahah... nice one, [ryan]! Classic porn game protagonist type of move!"
            scene bg Office08
            with dissolve
            MG "Im impressed!"
            M "Is that why you showed me those games? To groom me like a conquest in a porn game?"
            R "No!... But I can see why you two would think that."
            R "I just thought they would be a compelling piece of evidence to validate Freud's Oedipus theories. You know, for my final project."
            R "If I was trying to groom you like in a porn game, do you think I'd be stupid enough to show you how women get groomed in porn games?"
            RT "{i}That really was stupid of me.{/i}"
            scene bg Office09
            with dissolve
            M "Hmmm... that had better be the case!"
            scene bg Office10
            with dissolve
            M "So, to explain what we were doing, it's going to sound weird, expecially since it's a little bit theoretical, even though it's backed up by significant research."
            M "{b}{i}Doctor{/i}{/b} Will Tylor, a famous psychologist who also happens to be a member of our school board, published a study about how young men can get stuck in an Oedipal phase if they aren't allowed to let it develop and go away on their own."
            scene bg Office09
            with dissolve
            M "My son has started exhibiting symptoms of a slight Oedipal complex. Sorry to embarrass you, [ryan]."
            R "Oh, God..."
            scene bg Office10
            with dissolve
            M "So I'm trying to help him get through it by letting it take it's course naturally, rather than trying to cut it off, and make him get stuck in it."
            M "It just involves a few handjobs from time to time. And it will never go any farther than that."
            scene bg Office11
            with dissolve
            M "Isn't that right, [ryan]?"
            R "... Oh... yeah... of course..."
            scene bg Office12
            with dissolve
            $ renpy.pause ()
            scene bg Office10
            with dissolve
            M "So that's all that's going on... not as terrible as you were probably imagining."
            scene bg Office19
            with fade
            MG "No... not quite as terrible."
            M "So... I'm hoping we can keep all of this between us?"
            MG "Yeah, I have no desire to stir up any trouble, but there is just a small thing I want from you."
            M "Oh, shit! Here we go."
            MG "No! It's not as terrible as you think, either."
            MG "But it is something you probably wouldn't do, unless I had some leverage over you."
            scene bg Office07
            with fade
            M "You don't have any leverage... I could defend my position to the school board."
            M "Especially with Will Tylor there to support me with his research."
            MG "Yeah, but a school board hearing would make this all very public, and I think people's imaginations will make them believe that much more is going on between you and your son."
            MT "{i}Dammit! That could ruin both of our reputations.  We would probably have to move. But I'm sure the FBI wouldn't let us.{/i}"
            MG "Don't get too defensive until you hear what it is that I want."
            scene bg Office20
            with fade
            MG "I'm sure you're already aware, but [ryan] has a photo studio that's beginning to do fairly well."
            M "I know it's bringing in a little money each week."
            M "And I know his sisters have been posing for pictures, in outfits that Sidney has designed."
            scene bg Office19
            with dissolve
            MG "Exactly... and those shoots have started to get a good amount of attention online."
            scene bg Office10
            with dissolve
            M "Oh, really?"
            MG "Yeah, in fact I thought that I'd already convinced [ryan] to let me be part of a photoshoot, but I guess I wasn't persuasive enough!"
            R "I've just been busy. I kinda forgot."
            MG "Well, I've been trying to get internet famous for years by posting pics and vids of my cheerleading stuff, and makeup and fashion tutorials."
            MG "But besides the occasional creepy stalker, I havn't been able to get a very good following."
            MG "But, I think [ryan]'s got a good thing going with his studio."
            MG "Cosplay is extremely popular right now."
            scene bg Office09
            with dissolve
            M "Well, I'm sure that [ryan] would be more than happy to take some pictures of you in cosplay."
            M "Wouldn't you, [ryan]?"
            R "Ummm... yeah... I'd love to get another model in there."
            MG "Great, but here's the part you're not going to like, Miss [mom_name]."
            MG "I have a feeling the photoshoot will be ten times more popular if I'm posing with a beautiful, sexy, more mature woman."
            scene bg Office06
            with dissolve
            M "You mean me."
            MG "Yes."
            M "There's no way!... I can't pose in sexy photos with one of my students!"
            scene bg Office07
            with dissolve
            M "That would destroy my reputation."
            MG "Destroy it? No... When I was a freshman, a video leaked of Miss Stone fucking one of her students, and now her class fills up faster than any other."
            MG "It's mostly boys, but the event only boosted her status among the students."
            MG "I was really surprised she didn't get fired."
            M "That's because the student was over 18, and the state has a law that schools can't punish teachers for that type of behavior if the student is a consenting adult."
            M "They didn't even bring it before the school board because there were no grounds for dimissal."
            M "It probably helped that she has tenure as well."
            R "You have tenure too, Miss [mom_name]."
            scene bg Office08
            with dissolve
            M "Shut up, [ryan]!"
            scene bg Office19
            with fade
            MG "[ryan] could even put the pictures behind a paywall for premium members, then probably none of your students would see the pics, since almost none of us have access to credit cards."
            scene bg Office13
            with fade
            MT "{i}Let's see... a formal investigation and scandal for incest, or taking sexy pics with a student, which probably no one will see?{/i}"
            scene bg Office19
            with dissolve
            M "Fine!... I'll do the photoshoot."
            MG "Yay! That's awesome!"
            MG "And just a few more details."
            scene bg Office20
            with dissolve
            MG "[ryan], I want you to create the background with your Photochop and 3d modeling skills."
            scene bg Office10
            with fade
            MG "And I love the Perry Hotter movies and books."
            MG "So I want you to get some Perry Hotter cosplay outfits."
            MG "I'm thinking a student and a teacher outfit."
            R "Really? Isn't Perry Hotter kind of juvenile?"
            scene bg Office11
            with dissolve
            M "If you had actually read the books then you'd know they appeal to all ages."
            R "Ok... sorry."
            M "You should be!"
            R "So, who's going to pay for the cosplay outfits?"
            scene bg Office09
            with dissolve
            M "Who do you think?"
            R "Me? But why am I getting stuck with the bill?"
            M "All my wages are garnished by the FBI, and I hardly think our extortioner is going to offer to pick up the bill."
            MG "You thought right."
            R "Fine!"
            R "I'll give Sidney the money the next time I see her."
            scene bg Office20
            with fade
            MG "This is so awesome! I can't wait to see the costumes! Just let me know when Sidney's got them ready."
            R "... fine."
            scene bg SleepBlack
            with fade
            RT "{i}Well that was an interesting turn of events.  I've been trying to think of a way to get Mom in the studio, but now Megan has done it for me!{/i}"
            RT "{i}As excited as I am though, I think Megan's even more excited.{/i}"
            $ mm_fuckedtoday = True
            $ blackmailed_mom_megan = True
            $ persistent.gal_mom_8 = True
            play music Honey
            scene bg SchoolHallway01
            with fade
            jump school

#############  CLUB  ########################################  CLUB  ###########################################################

label sid_sex_event:                    #### Edited ####
    scene bg SleepBlack
    with fade
    $ renpy.pause ()
    "{i}\"As [ryan] slowly drives his manly scooter to see Sidney at work, a significant event begins to unfold in the alleyway outside the nightclub.\"{/i}"
    scene bg SidSex01
    CC "I don't know... The DeCapo's won't ever stop trying to kill me if they know I betrayed them."
    VP "Well then don't fuck this up! If you successfully pull this off, the DeCapos will be as good as finito. With Joey dead, Don DeCapo will have no one to take over his enterprise."
    VP "We'll muscle our way in, and take over his whole operation."
    VP "And while we're cleaning things up here, you'll be at our little cocoa farm in Columbia with more money than you can spend and more coke than you can possibly snort."
    VP "And when it's all taken care of, you come back home as a made man forever in the Bonatti family."
    CC "Alright, but what do I do if things go south? Will you help me get out of here?"
    VP "Sure... sure, just give us a call on your burner, and we'll come riding in to the rescue."
    CC "Ok, Joey is always alone in his office Monday nights, I'll take care of it there."
    VP "Alright, and just remember... If you get caught, if you say a single word that we were involved, we'll go after that pretty little sister of yours."
    CC "I would never..."
    VP "Make sure that you don't."
    scene bg SleepBlack
    with fade
    $ renpy.pause ()
    scene bg SidClub48
    with fade
    play music ClubMusic
    A "Wow! Not a single customer since we started."
    A "Joey asked me to do the books tonight. He and the boys had to run off suddenly on some kind of emergency. So I get to fill in tonight. I guess I'll go get started since there's no action here."
    A "Do you want to come and keep me company?"
    S "What if a customer comes?"
    A "It's unlikely since most of the customers are part of the gang, but if someone shows up, I'm sure Charlie the Chin will come and find us."
    A "He's guarding the entrance tonight."
    S "I don't know..."
    A "Oh come on... I'll do the books in Joey's office, and you can just hang out while getting paid for it."
    ST "{i}Hmmm... [ryan] did tell me to keep my eye out for anything that might help us in our situation...{/i}"
    ST "{i}I might find something really useful in his office.{/i}"
    S "Ok..."
    A "Yay!"
    scene bg SleepBlack
    with fade
    play music Honey
    scene bg SidSex02
    with fade
    S "I can't believe you're keeping the books on actual books... Why don't you use a computer?"
    A "Well, because of the nature of some of the family's sources of income, some legitimate, others not so much, my uncle doesn't want any records kept that could possibly get hacked."
    A "Well, the money they make from your family each week for instance, see it's listed right here. It's not a legitimate source of income, and so it has to be laundered through one of his legitimate companies."
    S "Isn't your uncle afraid the books might get stolen?"
    A "Not really... They're kept undet the desk here in a very heavy, very secure safe."
    ST "{i}Hmmm... I wonder if there's any way to get the combination for that safe?{/i}"
    play sound CloseDoor
    "{i}\"SLAMMM!!!\"{/i}"
    scene bg SidSex03
    with dissolve
    CC "Don Bonatti sends his regards Joey!"
    scene bg SidSex04
    with fade
    CC "Armani!"
    scene bg SidSex05
    with dissolve
    A "Charlie!... You're not supposed to be in Uncle's office!"
    A "And why the hell?..."
    CC "Shut up! Why are you here? Where's your Uncle Joey?"
    A "I wouldn't tell you if I knew!"
    A "You came here to kill him, didn't you!"
    scene bg SidSex04
    with dissolve
    CC "Tell me, or I start shooting!"
    scene bg SidSex06
    with fade
    A "Ok!... ok... I don't really know!"
    A "He just said he had some emergency business."
    A "He didn't give me any details."
    A "He told me to come and do the accounting for the eveing while he was away."
    CC "Well, why wasn't I told?"
    A "Are you kdding? They don't tell you anything."
    scene bg SidSex04
    with fade
    CC "Goddammit! Shit! Mother fucker!"
    CC "Now, what in the hell am I supposed to do with yous two... Huh?"
    S "Please... Just let me go... I'm just a waitress.  I don't have any part of this."
    A "And I don't have any information that would be helpful to you!"
    CC "Just shut up and let me think!"
    CC "Goddammit!"
    CC "...."
    scene bg SidSex06
    with fade
    CC "Ok, first thing, I need to get you two to a secure room while I hide and wait for Joey to come back."
    CC "Armani, lead the way to the interrogation room.  And if either of yous gals tries to run, or cry for help, or anything stupid like that, then I put a bullet in your heads."
    ST "{i}Oh, God!{/i}"
    ST "{i}I can't die!{/i}"
    ST "{i}I just gave my brother a blowjob! I'll go to hell for sure!{/i}"
    CC "Are you two gonna move, or do I need to start shooting?"
    A "No! We're going."
    scene bg SleepBlack
    with fade
    play music ClubMusic
    scene bg SidSex07
    with fade
    $ renpy.pause ()
    scene bg SidSex08
    with dissolve
    $ renpy.pause ()
    SRT "{i}There's Armani and the new girl... I wonder where Charlie the Chin is taking them?{/i}"
    scene bg SidSex14
    with fade
    SRT "{i}Hmmm... None of my business, I guess...{/i}"
    scene bg SleepBlack
    with fade
    play music Honey
    scene bg SidSex09
    with fade
    CC "This should be a good place to keep you until Joey gets back."
    CC "Armani, go bend yourself over the wooden pony, waitress girl, latch the cuffs around her hands and ankles."
    A "Her name is Sidney!"
    CC "I don't give a fuck."
    CC "Now do it!"
    scene bg SidSex10
    with fade
    CC "Make sure you latch those good and tight."
    CC "And when you're finished, bend over the wooden pony, and I'll latch you in as well."
    scene bg SleepBlack
    with fade
    scene bg SidSex11
    with fade
    CC "Alright, now you two keep quiet while I make a few phone calls."
    S "{i}(whispering){/i} Armani, what is this thing we're buckled into?"
    S "It seems kind of kinky."
    A "{i}(whispering){/i}Yeah, I think it's some kind of kinky sex furniture, but I guess someone figured out it's pretty good for torture and interrogation and stuff like that."
    S "{i}(whispering){/i}What is he going to do to us?"
    A "{i}(whispering){/i}He won't do anything to us if he has half a brain."
    A "....But it is Charlie the Chin... He's not known for being very intelligent."
    scene bg SleepBlack
    with fade
    $ renpy.pause ()
    play music ClubMusic
    scene bg SidSex12
    with fade
    AD "What do you mean nobody's here?"
    AD "Why isn't The Chin watching the door?"
    AD "Where's Armani and Sidney?"
    SR "I don't know... I just saw Armani and another girl, followed by Charlie going towards the back hallway where I'm not allowed to go."
    AD "Shit! Something doesn't feel right about this."
    scene bg SidSex13
    with fade
    SR "Where are you going in such a hurry?"
    AD "...."
    scene bg SidSex14
    with fade
    SRT "No business of mine, I guess."
    scene bg SleepBlack
    with fade
    $ renpy.pause ()
    play music Honey
    scene bg SidSex16
    with fade
    CC "No... it's just like I said.  Joey wasn't in his office... He's not even in the club."
    VP "Well then, do it a different night."
    CC "Well... The thing is... His niece was there... and now I've got her and another girl tied up in the interrogation room."
    CC "So I was thinking you could use his niece for a hostage, and this other girl is pretty enough to be trafficked to one of your italian brothels."
    ST "{i}Oh God, no!{/i}"
    VP "Did they see your face? Do they know who you are?"
    CC "Ummm... Yeah..."
    VP "Charlie, you dumb fuck!"
    VP "We need Joey dead, not his niece as our hostage."
    VP "Taking her hostage will cause an all-out gang war, which is exactly what we're trying to avoid by taking him out quickly and quietly in the first place."
    VP "Uuuggghhhh... You dumb fuck!"
    scene bg SidSex15
    with dissolve
    VP "...."
    VP "If you fail to kill Joey tonight, if I were you, I'd dissapear, cuz if the DeCapos catch you, they're going to torture and kill you."
    VP "And I seriously doubt you have the strength to keep quiet about us under torture."
    VP "And if you do mention our name, we'll kill you if they don't, and that pretty little sister of yours will be the one that ends up trafficked to one of our brothels."
    VP "So, you'd better kill Joey, or get out of there and make yourself impossible to find."
    CC "Can't you guys protect me?"
    VP "Only if Joey dies tonight."
    VP "But you can't leave any witnesses either."
    VP "So, if you're successful in killing him, bring us those two lovely girls, and we'll let you keep a share of their brothel earnings."
    CC "But how am I going to?...."
    "{i}\"CLICK\"{/i}"
    CC "Hello?"
    CC "Goddammit!"
    "{i}\"Sound of running footsteps\"{/i}"
    CC "Shit! Someone's coming!"
    scene bg SidSex18
    with dissolve
    AD "{i}(Muffled voice){/i} Armani?... Sidney... Can you girls hear me?"
    A "Help! We're in the interrogation room!"
    scene bg SidSex19
    with dissolve
    AD "{i}GASP!{/i} Oh, my God!"
    scene bg SidSex20
    with dissolve
    ADT "{i}Holy fuck, Diaz! Ignore those sexy asses for a minute.{/i}"
    AD "Where's Charlie the Chin?... Did he do this to you?"
    A "{i}(Panicked voice){/i} I'm not sure where he is, but I think he's still in the room!"
    play sound CloseDoor
    scene bg SidSex21
    with dissolve
    CC "That's right, I'm right here."
    CC "Now drop your gun!"
    AD "Charlie? What in God's name are you doing?"
    AD "Are you some kind of retard?"
    scene bg SidSex22
    with fade
    CC "I said to drop it!"
    AD "What the hell do you think you're doing?"
    CC "Shut up bitch! I've got a gun, so I don't have to tell you anything."
    A "He said he's here to kill my uncle!"
    AD "You have got to be the dumbest son of a bitch. You do realize you've just dug your own grave, right?"
    CC "Not if I succeed, and I turn you all into drugged up sex slaves that can't tell anyone about it."
    AD "You're not smart enough, nor do you have the resources to succeed with that."
    A "He's got help from someone!"
    CC "If you don't shut your mouth, I'm going to put something in it!"
    CC "How would you like to get a little practice for your new profession?"
    A "{i}(Timid voice){/i} I'll be quiet!"
    CC "You'd better."
    CC "And as for you, Diaz, drop your gun and strip, so I can make sure you're not hiding more weapons."
    scene bg SleepBlack
    with fade
    scene bg SidSex23
    with fade
    AD "There, as you can see I'm not hiding any more weapons."
    CC "Good... Now bend over that wooden pony, I need to detain you so I can go wait for Joey."
    scene bg SleepBlack
    with fade
    "{i}\"Meanwhile...{/i}\""
    scene bg SidSex25
    with fade
    R "Huh... I've never seen the entrance without a guard before..."
    play music ClubMusic
    scene bg WalkingCasino
    with fade
    R "I know Mondays are slow... but where is everyone?"
    scene bg WalkingBar
    with fade
    R "Sidney and Armani aren't here either."
    scene bg SidSex26
    with fade
    RT "{i}Oh, good!... I was beginning to think the DeCapos had packed up and left town... Actually that would probably be a good thing.{/i}"
    SR "Oh, finally! A customer!"
    scene bg SidSex27
    with fade
    R "Oh no... Actually... I'm just looking for my sister, Sidney."
    R "Have you seen her? She's always waitressing here on Mondays?"
    scene bg SidSex28
    with dissolve
    SR "Ohhh... You're the waitress's little brother. I've heard of you."
    R "Oh, really? From who?"
    SR "Emma... One of the other dancers."
    R "Yeah... I know who that is... I hope she said good things."
    SR "She was telling all of us about the waitress's younger brother, who looks far too young to be in a strip club, who sits there with a raging hard-on, and never gives any tips."
    R "Ouch..."
    SR "You're not just here to waste my time are you?"
    R "Well... kind of, I guess... I'm just here to find my sister."
    scene bg SidSex29
    with dissolve
    SR "I'll tell you what... I'm having a terrible night... And I really need to make some money."
    SR "If you'll pay me double for a lapdance... I'll tell you where your sister and Armani went."
    SR "I'll also let the girls know what a good customer and tipper you are, and maybe raise your status here at the club a little bit."
    R "How much is a lapdance?"
    SR "Nomally twenty five dollars, but I really need at least fifty tonight."
    SR "What do you say?"
    menu:
        "You have a deal! ($50)" if money >= 50:
            jump candy_strip_show
        "Please... I don't have time for this!" if money >= 50:
            $ no_time_for_candy == True
            jump find_sidney
        "I don't have enough money." if money <= 49:
            $ no_time_for_candy == True
            jump find_sidney
        "Tell me about yourself first.":
            jump candy_story

label candy_story:                      #### Edited ####
    scene bg SidSex28
    with dissolve
    SR "You want to know about me?"
    R "Yeah... I'm just curious what your story is."
    SR "You mean, do I have an interesting backstory like your mom does?"
    R "Yeah... kind of... I guess..."
    scene bg SidSex27
    with dissolve
    SR "Well, it turns out that I do."
    SR "My name is Candy, by the way."
    R "Candy?... How sweet!"
    scene bg SidSex28
    with dissolve
    CD "I've never heard that one before."
    R "Sorry."
    CD "So, my story starts on my honeymoon, with my new husband, Jack."
    CD "We were spending it in Vegas, when somehow, Jack got invited to a high-stakes poker game."
    scene bg SidSex29
    with dissolve
    CD "During the game Jack got what he called an \"unbeatable hand\"."
    CD "He had a straight flush."
    CD "So, he bet way more than he could afford."
    CD "Well... More than we could ever afford, in both our lifetimes."
    CD "And guess what?..."
    R "He lost?"
    scene bg SidSex28
    with dissolve
    CD "Yep... That motherfucker lost to Joey DeCapo, who had a royal flush."
    CD "Long story short, I ended up spending my honeymoon with Joey, and now I have to work here once a week to pay off my loser husband's poker debt."
    CD "On top of that, Joey has me entertain important clients doing things you can only imagine in the VIP room."
    CD "Jack took me to Vegas, and made me a whore!"
    R "Wow! That sounds like it could be the plot of a movie!"
    CD "Yeah, well, I have yet to see the happy ending for this one."
    CD "Although I've given many men a happy ending."
    $ get_to_know_candy = True
    scene bg SidSex27
    with dissolve
    CD "So you can see why I need that money tonight..."
    CD "So, will you pay me for a lapdance?"
    menu:
        "You have a deal! ($50)" if money >= 50:
            jump candy_strip_show
        "Please... I've got to run!" if money >= 50:
            jump find_sidney
        "I don't have enough money." if money <= 49:
            jump find_sidney

label candy_strip_show:                 #### Edited ####
    "{i}\"Money -$50\"{/i}"
    $ money -= 50
    scene bg SidSex27
    with dissolve
    if get_to_know_candy == False:
        SR "My name is Candy, by the way! Just thought you should know the name of the dancer that's grinding on your dick."
        R "Candy?... How sweet!"
        scene bg SidSex28
        with dissolve
        CD "I've never heard that one before."
        R "Sorry."
        scene bg SidSex27
        with dissolve
    else:
        pass
    CD "Thank you so much for buying a lapdance!"
    CD "You won't be dissapointed!"
    scene bg SleepBlack
    with fade
    scene bg SidSex30
    with fade
    CD "Wow... I can tell you're packing quite a unit."
    CD "I'll make sure all the dancers hear about that too."
    scene SidFirstVideo06
    with fade
    $ renpy.pause ()
    R "Oh God, you can really move those hips!"
    CD "Haha... You like that?"
    R "I love it!"
    CD "For a little tip, I'll give you some more!"
    if money >= 20:
        RT "{i}I only have twenty dollar bills on me!{/i}"
        RT "{i}Is it really worth it?{/i}"
    else:
        RT "{i}Shit! I don't have the money!{/i}"
    menu:
        "I'm out of cash" if money <= 19:
            R "I'd love to pay you more, but your lapdance took all the money I had."
            CD "That's alright, honey. I really appreciate you buying a dance in the first place. Now my night wasn't a complete waste of time."
            scene bg SleepBlack
            $ candy_danced = True
            with fade
            jump find_sidney
        "I'm not paying this bitch any more money.":
            R "I'd love to, but I think I'd better go find my sister now."
            CD "That's alright, honey. I really appreciate you buying a dance in the first place. Now my night wasn't a complete waste of time."
            scene bg SleepBlack
            $ candy_danced = True
            with fade
            jump find_sidney
        "Tip $20." if money >= 20:
            "{i}\"Money -$20\"{/i}"
            $ money -= 20
            scene bg SidSex30
            with fade
            CD "Twenty dollars! Now that's a great tip!"
            scene bg SidSex31
            with dissolve
            CD "Let me show you something even sweeter than my name."
            scene bg SidSex32
            with dissolve
            R "Oh, my God!"
            CD "Wow! Your dick twitch almost lifted me up an inch."
            scene SidFirstVideo07
            with fade
            $ renpy.pause ()
            R "Can I touch them?... Or even better, could I taste them?"
            CD "Sorry, the rules are to keep your hands to yourself."
            R "That's a terrible rule!"
            CD "If you spend enough money here, you can become a VIP, then those kind of rules won't apply to you."
            R "How much money?"
            CD "I don't even know... You have to work it out with the boss."
            RT "{i}Hmmm... maybe I will.{/i}"
            CD "If you like what you see, you can give me another tip and I'll let you see even more."
            if money >= 20:
                RT "{i}I'd love to see more.{/i}"
                RT "{i}But is it worth another twenty bucks?{/i}"
            else:
                RT "{i}Shit! I don't have the money!{/i}"
            menu:
                "I'm out of cash" if money <= 19:
                    R "I'd love to pay you more, but your lapdance took all the money I had."
                    CD "That's alright, honey. I really appreciate you buying a dance in the first place. Now my night wasn't a complete waste of time."
                    scene bg SleepBlack
                    with fade
                    $ candy_danced = True
                    jump find_sidney
                "I'm not paying this bitch any more money.":
                    R "I'd love to, but I think I'd better go find my sister now."
                    CD "That's alright, honey. I really appreciate you buying a dance in the first place. Now my night wasn't a complete waste of time."
                    scene bg SleepBlack
                    $ candy_danced = True
                    with fade
                    jump find_sidney
                "Tip $20." if money >= 20:
                    "{i}\"Money -$20\"{/i}"
                    $ money -= 20
                    scene bg SidSex32
                    with fade
                    CD "Oh, my God! Another twenty dollars? Thank you so much!"
                    CD "If you think your dick is hard now..."
                    scene bg SidSex33
                    with dissolve
                    CD "Wait until you see my sugary little funnel cake."
                    R "Funnel cake? I've never heard that one before. What does it mean?"
                    CD "You'll see."
                    scene bg SidSex34
                    with dissolve
                    R "Oh, God! That is a sweet looking funnel cake."
                    scene SidFirstVideo08
                    with fade
                    $ renpy.pause ()
                    R "And you really know how to shake it."
                    R "I need some release!"
                    CD "Don't you dare touch yourself!"
                    CD "That's definitely not allowed here."
                    R "Oh, God! What a cocktease! I've really got to get me a VIP membership!"
                    RT "{i}I've really got to keep Mom out of here, so she doesn't have to start servicing VIP clients.{/i}"
                    RT "{i}Although... If I were the client...{/i}"
                    CD "Alright, the dance is over!"
                    scene bg SleepBlack
                    with fade
                    scene bg SidSex27
                    with fade
                    CD "Thank you for making my night so much better!"
                    CD "I really hope you do become a VIP member. I can tell that cock is so much bigger than my husband Jack's."
                    $ candy_danced = True
                    jump find_sidney

label find_sidney:                      #### Edited ####
    if no_time_for_candy:
        scene bg SidSex29
        with dissolve
        SR "Urrggghh... Fine!... it was worth a try."
        SR "This is the worst fucking night ever."
        SR "I saw your sister go down the hallway that leads to the VIP room."
        SR "She was with Armani and tonight's guard Charlie."
        SR "There must have been some sort of staff meeting or something."
        SR "And the fuckers must not have thought I was important enough to attend."
        R "So just down the hallway, behind the stage, and to the right?"
        SR "Yeah, but be careful. I've been warned that I'm not allowed to go any further down that hallway than the VIP room."
        R "Alright, thanks! I'd better run."
    elif candy_danced == False:
        scene bg SidSex29
        with dissolve
        CD "Urrggghh... Fine!... it was worth a try."
        CD "This is the worst fucking night ever."
        SR "I saw your sister go down the hallway that leads to the VIP room."
        CD "She was with Armani and tonight's guard, Charlie."
        CD "There must have been some sort of staff meeting or something."
        CD "And the fuckers must not have thought I was important enough to attend."
        R "So just down the hallway, behind the stage, and to the right?"
        CD "Yeah, but be careful. I've been warned that I'm not allowed to go any further down that hallway than the VIP room."
        R "Alright, thanks! I'd better run."
    else:
        scene bg SidSex29
        with dissolve
        CD "Alright, a deal's a deal."
        SR "I saw your sister go down the hallway that leads to the VIP room."
        CD "She was with Armani and tonight's guard, Charlie."
        CD "There must have been some sort of staff meeting or something."
        CD "And the fuckers must not have thought I was important enough to attend."
        R "So just down the hallway, behind the stage, and to the right?"
        CD "Yeah, but be careful. I've been warned that I'm not allowed to go any further down that hallway than the VIP room."
        R "Alright, thanks! I'd better run."
    RT "{i}I hope everything's alright.{/i}"
    scene bg SleepBlack
    with fade
    $ renpy.pause ()
    play music Honey
    scene bg SidSex24
    with fade
    AD "Ouch! Not so tight, you moron!"
    AD "You think you're going to get away with this?"
    AD "You really are dumber than a box of rocks!"
    CC "If you don't shut your trap, you're really going to regret it!"
    AD "Oh, am I?... What are you going to put me in my place with, your incredible wit?"
    CC "Don't insult my intelligence!"
    AD "Why? Do you actually think you have some?"
    A "Agent Diaz, maybe you should be quiet!"
    AD "If only your mom had swallowed you instead."
    CC "That's it! Now you're going to get it!"
    scene bg SidSex35
    with fade
    AD "Don't you dare!"
    scene bg SidSex36
    with dissolve
    AD "You sick, perverted fucker! Pull my panties back up!"
    CC "Not until I teach you some respect."
    AD "If you stick your dick in me, I swear I'll..."
    CC "I wouldn't stick my dick in that community jizz hole!"
    AD "Oh... So you're gay!"
    scene bg SidSex37
    with dissolve
    CC "Damnit Diaz! I'm going to fuck your ass with a wrench!"
    scene bg SidSex38
    with fade
    AD "You wouldn't dare!"
    if not no_time_for_candy:
        scene bg SidSex39
        with dissolve
        AD "Oh, fuck!"
        scene SidFirstVideo01
        with fade
        $ renpy.pause ()
        CC "Haha... That shut your big mouth!"
        A "Oh, my God! Did he really stick a wrench in your ass?"
        scene bg SidSex39
        with dissolve
        S "Oh, my God, oh my God, oh my God!"
        scene bg SidSex40
        with dissolve
        $ renpy.pause ()
        A "Holy fuck! Diaz, you aren't enjoying it, are you?"
        AD "...I... I cant... help it!..."
        scene SidFirstVideo01
        with fade
        $ renpy.pause ()
        A "Oh, my God! How depraved are you?"
        AD "It's just... I'm kind of into... anal..."
        AD "And bondage... situations... really turn me on!..."
        AD "Fuck!"
        CC "Haha!... You really are a slut!"
        CC "Are you going to cum?"
        scene bg SidSex40
        with fade
        S "No! Don't give him the satisfaction of making you cum!"
        scene bg SidSex39
        with dissolve
        AD "I'm fucking trying! Ok?"
        scene bg SidSex41
        with fade
        RT "{i}What's behind this doo...{/i}"
    else:
        scene bg SidSex42
        with fade
        RT "{i}What's behind this doo...{/i}"
    scene bg SidSex43
    with dissolve
    RT "{i}Holy shit!{/i}"
    if not no_time_for_candy:
        scene bg SidSex44
        with fade
        RT "{i}Is that Sidny and Armani in the tights?{/i}"
        RT "{i}And who the hell is that guy fucking in the ass with a wrench?{/i}"
    else:
        RT "{i}Is that Sidny and Armani in the tights?{/i}"
        RT "{i}And who is that with her panties down, and what is he about to do with that wrench?{/i}"
    RT "{i}I have to do something!{/i}"
    scene bg SidSex45
    with fade
    RT "{i}He hasn't noticed me yet... And there's his gun on the floor!{/i}"
    RT "{i}I don't think I can do this!{/i}"
    RT "{i}For fuck's sake, [ryan]! You don't have a choice!... Find your balls!{/i}"
    RT "{i}I think they've retreated into my stomach!{/i}"
    RT "{i}I don't even know how to use a gun!{/i}"
    RT "{i}He doesn't know that though...{/i}"
    RT "{i}Here goes nothing!{/i}"
    if not no_time_for_candy:
        scene bg SidSex46
        with fade
        R "Drop that wrench, you perverted son of a bitch!"
        scene bg SidSex47
        with fade
        CC "Whoa... Hey... Hey... Please, don't shoot!"
        A "Who's that?"
        R "Don't worry, girls... I'm here!"
        S "Is that [ryan]!?"
        R "Yeah, it's me!"
        S "Oh, [ryan]! Thank God!"
        AD "Hey, [ryan]?"
        R "Yeah?... Is that you, Agent Diaz?"
        AD "Yes... and can you hurry up and detain this guy, and kindly get the wrench out of my ass?"
        RT "{i}Haha... That wrench is just sticking out of her ass!{/i}"
        R "Ummm... yeah..."
        R "Let those girls out of those shackles before I put a bullet in your head!"
    else:
        scene bg SidSex48
        with fade
        R "Get away from those girls, you perverted son of a bitch!"
        CC "Whoa... Hey... Hey... don't shoot!"
        A "Who's that?"
        R "Don't worry girls... I'm here!"
        S "Is that [ryan]!?"
        R "Yeah, it's me!"
        S "Oh, [ryan]! Thank God!"
        AD "Hey, [ryan]?"
        R "Yeah? Is that you, Agent Diaz?"
        AD "Yes... and can you hurry up and detain this guy and get us out of these shackles, so I can pull my panties back up?"
        R "Ummm... yeah..."
        R "Let those girls out of those shackles before I put a bullet in your head!"
    scene bg SleepBlack
    with fade
    scene bg SidSex49
    with fade
    if not no_time_for_candy:
        AD "So you think it's ok to shove things up someone's ass?"
        CC "You liked it, you slut."
        AD "Yeah well, we'll see how you like it when they are interrogating you. I'm going to request that they shove a pineapple up your ass."
        AD "You're going to wish [ryan] had pulled the trigger."
        CC "Bitch!"
        AD "Come on, I'm taking your treacherous ass to the DeCapo boys!"
        AD "They can decide what to do with you."
    else:
        AD "You're lucky [ryan] never gave you a chance to stick that wrench up my ass."
        CC "Yeah, you would have liked it, you slut."
        AD "Yeah well, we'll see how you like it when they are interrogating you. I'm going to request that they shove a pineapple up your ass."
        AD "You're going to wish [ryan] had pulled the trigger."
        CC "Bitch!"
        AD "Come on, I'm taking your treacherous ass to the DeCapo boys!"
        AD "They can decide what to do with you."
    scene bg SleepBlack
    with fade
    scene bg SidSex50
    with fade
    A "Are you doing ok, Sidney?"
    S "Yeah, I'm surprisingly calm."
    S "I was scared while it was happening, but now I feel almost a rush."
    A "Aahh... like after a scary movie, right?"
    S "Yeah... Kinda..."
    A "There are very few people that get a thrill from such intense situations."
    A "Maybe this type of life is suited for you."
    A "Anyways, I hope this experience won't make you quit working here."
    A "I love having your company at work."
    S "No... I think I'm ok... I'll be back next Monday... Maybe even sooner."
    A "Yay! I'm so happy you're going to stay!"
    scene bg SidSex51
    with fade
    A "And thank you so much for saving us, [ryan]!"
    A "Who knows what would have happened to us if he'd succeeded in killing my uncle."
    R "He was after your uncle?"
    A "Yes, and because of you, we're all safe!"
    RT "{i}Damnit! Why couldn't I have saved them after he'd killed her uncle.{/i}"
    RT "{i}No uncle, no debt.{/i}"
    scene bg SidSex52
    with dissolve
    $ renpy.pause (0.3)
    scene bg SidSex51
    with dissolve
    R "Wow!... Thanks!"
    A "No... Thank you!"
    A "And now I've got to run help Diaz find my uncle."
    A "Make sure Sidney's ok for me, will you?"
    R "Yeah, of course."
    scene bg SidSex54
    with dissolve
    R "Wow! What a day!"
    R "I'm so glad you're safe!"
    scene bg SidSex55
    with fade
    S "I'm only safe thanks to you."
    scene bg SidSex57
    with dissolve
    S "You're my hero!"
    R "I was just lucky to be there at the right time."
    scene bg SidSex55
    with dissolve
    S "No!... Don't sell yourself short!"
    S "What you did took incredible courage."
    S "I don't think I'd have had the courage to..."
    scene bg SidSex56
    with dissolve
    S "Wow! Your dick is as hard as a rock!"
    R "Oh... I'm sorry! I didn't even notice, with everything else going on... I guess it's just a weird reaction to all the excitement."
    S "No it's ok... Actually..."
    scene bg SidSex54
    with fade
    S "I'm kinda hoping that you're hard because you were hugging me."
    R "Really?!"
    S "Yeah..."
    scene bg SidSex53
    with dissolve
    S "I know this is really weird... But my thoughts and emotions are doing all kinds of somersaults."
    S "I'm both shook up, and weirdly calm.  I'm feeling timid, and brave. I'm scared, but I've also feeling a rush like I just rode a rollercoaster."
    S "But the strongest of all these feelings is that I need to get as close as I can to the guy who saved my life!"
    scene bg SidSex55
    with fade
    S "And I know this is so wrong, but I just don't care anymore!"
    scene bg SidSex57
    with dissolve
    S "I neeeed you inside me!"
    play music SexMusic
    scene bg SleepBlack
    with fade
    $ renpy.pause ()
    scene bg SidSex58
    with fade
    RT "{i}Oh, my God!{/i}"
    RT "{i}Is this really going to happen?{/i}"
    RT "{i}I mean it took a lot of work to get here, but I never would have thought I'd get her to the point where she would initiate our first time having sex!{/i}"
    RT "{i}Wow! My first time having sex is going to be with my sister, Sidney!{/i}"
    play sound Blow02 loop
    scene SidFirstVideo02
    with fade
    $ renpy.pause ()
    ST "{i}Oh, my God! What's come over me?{/i}"
    ST "{i}Am I really going to let my own brother fuck my needy pussy?{/i}"
    ST "{i}But it is such a needy pussy right now.{/i}"
    ST "{i}It seems that I need a good dicking down when my adrenaline gets so high.{/i}"
    ST "{i}God, I hope a good dicking down will satisfy this itch!{/i}"
    stop sound
    scene SidFirstVideo03
    with dissolve
    play sound Blow03 loop
    $ renpy.pause ()
    if ntrcontent:
        ST "{i}It's not like I need my brother's cock... I just need any cock right now... His is just the most convenient and willing.{/i}"
        ST "{i}Not to mention the biggest around.{/i}"
        ST "{i}How could I have allowed myself to get so wanton?{/i}"
    else:
        ST "{i}But it's not like any cock will scratch this itch... I really just need my brother's cock.{/i}"
        ST "{i}How could I have let things go so far between us?{/i}"
    stop sound
    scene bg SleepBlack
    with fade
    S "Ok, I think we're both ready. Lay down."
    scene bg SidSex59
    with fade
    R "Wait!"
    S "Oh no... What is it?"
    R "I just wanted to let you know that I'm giving my virginity to you."
    scene bg SidSex60
    with dissolve
    S "Oh, my God... I didn't realize... I mean I've never seen you real cozy around any other girls, but your virginity?"
    R "Yeah, yeah, I know I'm not real smooth with the ladies."
    S "No wonder you're so perverted, all that pent-up sexual energy..."
    S "but... are you sure you want to lose your virginity to your sister?"
    R "I can't think of anyone better."
    RT "{i}Well maybe Mom, or Lauren.{/i}"
    S "That's so sweet."
    S "So are you ready? I'm dying to get that huge cock in my pussy!"
    R "Hahah... Yeah... I'm ready."
    play sound Ejaculate
    scene bg SidSex61
    with dissolve
    RT "{i}Oh, fuck!{/i}"
    scene bg SidSex62
    with dissolve
    S "God, [ryan]! I've never felt so filled!"
    scene SidFirstVideo04
    with fade
    play sound Sidney01 loop
    $ renpy.pause ()
    ST "{i}It's happening!... I'm fucking my brother!... God, that's so wrong!... but fuck, it's so hot!{/i}"
    S "It's so tight in there! Look how my pussy lips grip your cock!"
    S "I've never had anything this big in there!"
    scene bg SidSex62
    with fade
    S "It's too long! I can't even get it very deep!"
    scene SidFirstVideo04
    with fade
    $ renpy.pause ()
    S "I wonder... if... we try... another... position..."
    scene bg SidSex63
    with dissolve
    stop sound
    S "Wow!... I know that feels good, but I want to see if I can take you any deeper. I wonder if it will work better if you fuck me from behind."
    R "Yeah... Let's try it."
    scene bg SleepBlack
    with fade
    play sound Sidney01 loop
    scene SidFirstVideo05
    with fade
    $ renpy.pause ()
    S "Shit, that's much deeper..."
    S "You're pounding my cervix!"
    R "Your what now?"
    S "The entrance of my womb!"
    RT "{i}Her womb! Holy fuck! I didn't even think about how I could get her pregnant!{/i}"
    RT "{i}She's probably on birth control. Should I ask her?... Nah... That would ruin the moment.{/i}"
    RT "{i}Oh fuck, I'm getting close though!{/i}"
    $ renpy.pause ()
    RT "{i}Hnnnggghhh... I'm getting really close!{/i}"
    R "Sidney! I'm gonna cum!"
    if sidneyaffection >= 10:
        S "Please!... Fill my pussy!"
        R "Fill your pussy? Are you on birth control?"
        S "No!... But I don't care! I need your cum deep in my pussy!"
        RT "{i}Shit! Do I risk getting her pregnant?{/i}"
        menu:
            "Fill her pussy! {i}(Best if Sidney's affection is 10 or greater.){/i}":
                scene bg SidSex64
                with fade
                $ renpy.pause ()
                stop sound
                $ renpy.pause ()
                R "Hnnnnggghhh!..."
                play sound Ejaculate
                scene bg SidSex65
                with dissolve
                with hpunch
                $ renpy.pause ()
                play sound Ejaculate
                "{i}\"[ryan]'s cum loads in Sidney's pussy +1\"{/i}"
                $ sidney_cum_loads_counter += 1
                "{i}\"Total loads of [ryan]'s cum in Sidney's pussy = ([sidney_cum_loads_counter])\"{/i}"
                "{i}{b}\"Sidney's Libido +5\"{/b}{/i}"
                $ sidneylibido += 5
                "{i}\"Sidney's Submission +1\"{/i}"
                $ sidneysubmission += 1
                scene bg SleepBlack
                with fade
                scene bg SidSex71
                with fade
                S "Wow, [ryan]! That was amazing!"
                S "I can't believe you lasted so long for your first time!"
                scene bg SidSex69
                with dissolve
                S "And ohhh... God! There's so much cum in my pussy!"
                S "I'll be dripping for days!"
                RT "{i}Shit! Did I just knock up my sister?{/i}"
                R "Maybe you should take one of those..."
                "{i}\"(Sound of door opening)\"{/i}"
            "Don't risk it!":
                stop sound
                R "I'm sorry! It's just too risky!"
                R "Hnnnggghhh!..."
                play sound Ejaculate
                scene bg SidSex66
                with fade
                with hpunch
                $ renpy.pause ()
                play sound Ejaculate
                scene bg SidSex67
                with dissolve
                with hpunch
                $ renpy.pause ()
                scene bg SidSex68
                with dissolve
                S "Fuck, [ryan]! I think that's the most I've ever seen you cum!"
                scene bg SleepBlack
                with fade
                scene bg SidSex71
                with fade
                S "Sorry I got so carried away while you were fucking me. Not cumming inside me was a really good call."
                scene bg SidSex69
                S "Ohh... But now it's dripping down the back of my legs!"
                S "I'll just rub it into my skin for now."
                "{i}\"(Sound of door opening)\"{/i}"
    else:
        S "I'm not on birth control!"
        S "Please! Don't cum in my pussy!"
        RT "{i}It's not like she really has a choice here, but should I risk gettting her pregnant?{/i}"
        menu:
            "Fill her pussy! {i}(Best if Sidney's affection is 10 or greater.){/i}":
                scene bg SidSex64
                with fade
                $ renpy.pause ()
                stop sound
                $ renpy.pause ()
                R "Hnnnnggghhh!..."
                play sound Ejaculate
                scene bg SidSex65
                with dissolve
                with hpunch
                $ renpy.pause ()
                play sound Ejaculate
                "{i}\"[ryan]'s cum loads in Sidney's pussy +1\"{/i}"
                $ sidney_cum_loads_counter += 1
                "{i}\"Total loads of [ryan]'s cum in Sidney's pussy = ([sidney_cum_loads_counter])\"{/i}"
                "{i}{b}\"Sidney's Anger +5\"{/b}{/i}"
                $ sidneyanger += 5
                scene bg SleepBlack
                with fade
                scene bg SidSex70
                with fade
                S "What the hell?... I told you not to cum in my pussy!"
                scene bg SidSex69
                S "God! And you came so much!"
                S "I'm going to be dripping for days."
                S "I'd better go get one of those..."
                "{i}\"(Sound of door opening)\"{/i}"
            "Don't risk it!":
                stop sound
                R "Hnnnggghhh!..."
                play sound Ejaculate
                scene bg SidSex66
                with fade
                with hpunch
                $ renpy.pause ()
                play sound Ejaculate
                scene bg SidSex67
                with dissolve
                with hpunch
                $ renpy.pause ()
                scene bg SidSex68
                with dissolve
                S "Fuck, [ryan]! I think that's the most I've ever seen you cum!"
                scene bg SleepBlack
                with fade
                scene bg SidSex71
                with fade
                S "Thank you so much for resisting the urge to cum in my pussy!"
                scene bg SidSex69
                S "Ohh... But now it's dripping down the back of my legs!"
                S "I'll just rub it into my skin for now."
                "{i}\"(Sound of door opening)\"{/i}"
    scene bg SidSex72
    with fade
    play music Honey
    A "Fuck! What are you two doing?"
    S "It's not what it looks like!"
    S "Its..."
    A "It doesn't matter right now. You two need to hurry and get your pants back on. My uncle is back, and he's looking for both of you."
    A "I'll run and tell him you're still here, and in the meantime, get those pants back on."
    scene bg SleepBlack
    with fade
    scene bg SidSex73
    with fade
    $ renpy.pause ()
    scene bg SidSex75
    with dissolve
    J "I'm so glad you two are still here."
    J "I was really hoping I'd get a chance to talk to you before you went home tonight."
    J "Mostly [ryan], I want to thank you for stopping Charlie the Chin from hurting my niece and possibly killing me."
    RT "{i}Fuck! What does Armani think we were up to?... Is there any way she could mistake what we were doing?{/i}"
    scene bg SidSex76
    with dissolve
    J "Though it's unlikely he would have ever succeeded."
    RT "{i}Nope... Looks like she understood exactly what we were doing.{/i}"
    J "That idiot doesn't have two brain cells to rub together."
    J "But it still takes a lot of courage to stand up to a Mafia goon, there's no way you could have known he's not the sharpest tool in the shed."
    scene bg SidSex77
    with dissolve
    J "Sidney, I'm so embarrassed that you were put in danger at your place of employment."
    RT "{i}At least Armani doesn't seem very disturbed by it all.{/i}"
    J "I would hate to lose your help over this incident, so please consider continued employment with us."
    J "I'd love to give you a little pay bonus for the inconvenience."
    "{i}\"Sidney's College fund + $1,000\"{/i}"
    $ sidney_money += 1000
    scene bg SidSex75
    with dissolve
    J "Also, as a token of my appreciation, I'm going to take twenty thousand dollars off of your family's debt to us."
    R "Wow! That's a lot!"
    J "Well, it won't affect any weekly payments or anything, but it will take a lot off the final balloon payment that's due at the end of the payment period."
    R "How much debt do we still owe you, and when does the payment period end?"
    J "Sorry, I don't have the numbers memorised.  I'll look into it, and get back to you through Agent Diaz."
    J "But anyways, thank you so much, and if there's anything else we can do for you within reason, let me know."
    J "I'll give you a few minutes to collect yourselves, and then I'm going to need that room back.  I've got a certain former disgruntled employee that I've got to do an exit interview with in that room."
    R "Understood."
    scene bg SidSex74
    with dissolve
    A "Holy fuck!... I can't even believe you two!"
    A "Sidney! Why didn't you tell me you were fucking your brother?"
    S "I wasn't... Until tonight..."
    S "I was just so overwhelmed with emotions, I acted on instinct, instead of using my brain."
    A "Shit! That's awesome! Usually our instincts are right, and we just screw things up with our brains."
    A "Just to be clear though, you don't have any time to fuck here again.  They are literally hauling Charlie's broken ass to this room as we speak."
    A "I hope I get to see you two around again very soon!"
    A "And thank you again, [ryan]! You're my hero!"
    play sound CloseDoor
    scene bg SidSex73
    with dissolve
    S "Wow!... I can't believe how cool Armani was with what just happened."
    scene bg SidSex78
    with dissolve
    S "I'm sorry our night had to end this way."
    S "You'd better run home."
    S "I need to collect all my stuff, and then I'll meet you there."
    scene bg SleepBlack
    with fade
    $ renpy.pause ()
    $ persistent.gal_sidney_7 = True
    $ progress = 16
    $ fucked_sid = True
    $ visited_sid = True
    $ timeofdaycounter = 5
    jump citymap

label post_bondage_chat:                #### Edited 9-2-2020 ####
    A "I just can't tell you how happy I am that our experience didn't scare you off!"
    S "Yeah... it's weird... it's like I never felt so alive!"
    S "And that's why I..."
    A "Nope!... You don't have to explain a thing!"
    A "I'll admit I was a little shocked at first..."
    A "But I totally see why you would be into that."
    A "Especially when I saw how hung your brother is!"
    S "You didn't even see him fully erect!"
    A "Shit! That's true!"
    A "We've got to figure out a way to get a peek!..."
    S "Hehehehe..."
    A "Hehehehe..."
    scene bg SidClub49
    with fade
    R "What's so funny?"
    A "Oh, hey [ryan]!"
    A "We were just talking about... potatoes."
    R "Potatoes?"
    A "Weren't we?"
    scene bg SidClub50
    with fade
    S "Ummm... yeah..."
    S "You know... how they use potatos to make vodka!"
    A "Right!... Vodka... like how we have vodka at the bar."
    A "{i}(Whispering to Sidney){/i} Nice cover!"
    A "Anyways, I've got to run and fill out an order form for the booze we're getting short on."
    A "Sidney, watch the bar for me while I'm gone."
    S "You got it!"
    $ visited_sid = True
    $ after_bondage_chat = True
    S "So, was there something you wanted to talk to me about?"
    menu:
        "Working for the Mafia":
            jump mafia_chat
        "Are you making good money?":
            jump money_chat
        "Can we?... You know....":
            jump club_fun

label club_sex:                         #### Edited 9-2-2020 ####
    $ club_fun_counter = 1
    S "Well... we are pretty slow... but we can't fuck in our usual blowjob spot, too high a risk of getting caught."
    R "Then let's go fuck in the same room where we fucked for the first time."
    S "I still can't believe our first time was in a Mafia torture room!"
    R "Yeah... not very romantic..."
    S "Fuck romance! It was as exciting as hell!"
    RT "{i}What have I turned her into?{/i}"
    S "So yeah, let's go to our special room... I just hope it's not occupied by a Mafia prisoner."
    scene bg SleepBlack
    with fade
    $ renpy.pause ()
    scene bg SidSex58
    with fade
    play music SexMusic
    R "Ohh... Sidney! You're too good to me!"
    ST "{i}I'm glad he's grateful!... That's actually pretty sweet!{/i}"
    ST "{i}But I don't need sweet!... I need hard... dirty... SEX!{/i}"
    play sound Blow02 loop
    scene SidFirstVideo02
    R "Oh, my God!"
    R "Your hands are so soft!"
    stop sound
    play sound Blow03 loop
    scene SidFirstVideo03
    with fade
    $ renpy.pause ()
    R "Aaahhh..."
    R "Your head game is getting stronger!"
    ST "{i}You bet your ass it is.{/i}"
    ST "{i}Now, it's time for my brother to help me with my itch!{/i}"
    ST "{i}God, I hope a good dicking down will satisfy this itch!{/i}"
    stop sound
    scene bg SleepBlack
    with fade
    S "Ok, I think we're both ready. Lay down."
    scene bg SidSex59
    with fade
    $ renpy.pause ()
    scene bg SidSex60
    with dissolve
    $ renpy.pause ()
    scene bg SidSex61
    with dissolve
    RT "{i}Oh, fuck!{/i}"
    scene bg SidSex62
    with dissolve
    S "God, [ryan]! You're splitting me in two!"
    scene SidFirstVideo04
    with fade
    play sound Sidney01 loop
    $ renpy.pause ()
    ST "{i}It's happening again!... I'm fucking my brother!... God, that's so wrong!... but fuck, it's so hot!{/i}"
    S "It's so tight in there! Look how my pussy lips grip your cock!"
    scene bg SidSex62
    with fade
    S "It's too long! I can't even get it very deep!"
    scene SidFirstVideo04
    with fade
    $ renpy.pause ()
    S "Let's try... another... position..."
    scene bg SidSex63
    with dissolve
    stop sound
    S "Wow!... I know that feels good, but I want to see if I can take you any deeper. Try fucking me from behind again."
    R "Oh, yeah... I love this position!"
    scene bg SleepBlack
    with fade
    play sound Sidney01 loop
    scene SidFirstVideo05
    with fade
    $ renpy.pause ()
    S "Shit, that's much deeper..."
    S "You're pounding my cervix!"
    ST "{i}He's knocking on my womb again! Holy, fuck... that's so hot!{/i}"
    ST "{i}Oh, fuck, I'm gonna cum!{/i}"
    $ renpy.pause ()
    ST "{i}[ryan]! I'm cumming!{/i}"
    stop sound
    play sound Ejaculate
    scene bg SidSex79
    with fade
    S "FUUUUUuuuuck!"
    R "Holy hell, Sidney!"
    R "You must drink like, fifty cups of water every day!"
    S "Hnnnggghhh..."
    S "Now, stick that cock back inside me! I need your cum, now!"
    scene SidFirstVideo05
    with dissolve
    play sound Sidney01
    $ renpy.pause ()
    RT "{i}Ooooo... I'm getting really close!{/i}"
    R "Sidney! I'm gonna cum!"
    $ had_club_sex_again = True
    if sidneyaffection >= 10:
        S "Please!... Fill my pussy!"
        R "Fill your pussy? Are you on birth control?"
        S "No!... But I don't care! I need your cum deep in my pussy!"
        RT "{i}Shit! Do I risk getting her pregnant?{/i}"
        menu:
            "Fill her pussy!":
                scene bg SidSex64
                with fade
                $ renpy.pause ()
                stop sound
                $ renpy.pause ()
                R "Hnnnnggghhh!..."
                play sound Ejaculate
                scene bg SidSex65
                with dissolve
                with hpunch
                $ renpy.pause ()
                play sound Ejaculate
                "{i}\"[ryan]'s cum loads in Sidney's pussy +1\"{/i}"
                $ sidney_cum_loads_counter += 1
                "{i}\"Total loads of [ryan]'s cum in Sidney's pussy = ([sidney_cum_loads_counter])\"{/i}"
                "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
                $ sidneylibido -= 5
                scene bg SleepBlack
                with fade
                scene bg SidSex71
                with fade
                S "Wow, [ryan]! That was amazing!"
                S "I can't believe you lasted so long!"
                scene bg SidSex69
                with dissolve
                S "And, ohhh... God! There's so much cum in my pussy!"
                S "I'll be dripping for days!"
                RT "{i}Shit! Did I just knock up my sister?{/i}"
                R "Maybe you should take one of those..."
                scene bg SidSex71
                with dissolve
                S "Yeah... I'll try to remember to pick one up at the pharmacy tomorrow."
                S "That was amazing!"
                S "But, now I {i}really{/i} have to get back to work!"
                scene bg SleepBlack
                with fade
                $ renpy.pause ()
                scene bg SidClub50
                with dissolve
                play music ClubMusic
                S "Thanks for the distraction from work, [ryan]!"
                S "Before you go... was there anything else you wanted to talk to me about?"
                menu:
                    "Working for the Mafia.":
                        jump mafia_chat
                    "Are you making good money?":
                        jump money_chat
                    "That's all for tonight.":
                        scene bg ImageMapCasinoWSidney
                        with fade
                        $ screen_on = "casinosidneymap"
                        call screen casinosidneymap
            "Don't risk it!":
                stop sound
                R "I'm sorry! It's just too risky!"
                R "Hnnnggghhh!..."
                play sound Ejaculate
                scene bg SidSex66
                with fade
                with hpunch
                $ renpy.pause ()
                play sound Ejaculate
                scene bg SidSex67
                with dissolve
                with hpunch
                $ renpy.pause ()
                scene bg SidSex68
                with dissolve
                S "Fuck, [ryan]! That is so... much... cum!"
                scene bg SleepBlack
                with fade
                scene bg SidSex71
                with fade
                S "Sorry I got so carried away while you were fucking me. Not cumming inside me was a really good call."
                scene bg SidSex69
                S "Ohh... but now it's dripping down the back of my legs!"
                S "I'll just rub it into my skin for now."
                scene bg SidSex70
                with dissolve
                R "Yeah... I hear it's supposed to be good for your skin."
                S "I don't even want to know where you heard that."
                R "No... I read it on..."
                S "Stop! I said I don't want to know."
                S "And now, I {i}really{/i} have to get back to work!"
                scene bg SleepBlack
                with fade
                $ renpy.pause ()
                scene bg SidClub50
                with dissolve
                play music ClubMusic
                S "Thanks for the distraction from work, [ryan]!"
                S "Before you go... Was there anything else you wanted to talk to me about?"
                menu:
                    "Working for the Mafia.":
                        jump mafia_chat
                    "Are you making good money?":
                        jump money_chat
                    "That's all for tonight.":
                        scene bg ImageMapCasinoWSidney
                        with fade
                        $ screen_on = "casinosidneymap"
                        call screen casinosidneymap
    else:
        S "I'm not on birth control!"
        S "Please! Don't cum in my pussy!"
        RT "{i}It's not like she really has a choice here, but should I risk gettting her pregnant?{/i}"
        menu:
            "Fill her pussy!":
                scene bg SidSex64
                with fade
                $ renpy.pause ()
                stop sound
                $ renpy.pause ()
                R "Hnnnnggghhh!..."
                play sound Ejaculate
                scene bg SidSex65
                with dissolve
                with hpunch
                $ renpy.pause ()
                play sound Ejaculate
                "{i}\"[ryan]'s cum loads in Sidney's pussy +1\"{/i}"
                $ sidney_cum_loads_counter += 1
                "{i}\"Total loads of [ryan]'s cum in Sidney's pussy = ([sidney_cum_loads_counter])\"{/i}"
                "{i}{b}\"Sidney's Anger +5\"{/b}{/i}"
                $ sidneyanger += 5
                "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
                $ sidneylibido -= 5
                scene bg SleepBlack
                with fade
                scene bg SidSex70
                with fade
                S "What the hell?... I told you not to cum in my pussy!"
                scene bg SidSex69
                S "God! And you came so much!"
                S "I'm going to be dripping for days."
                S "I'd better go get one of those morning-after pills"
                S "I'll try to remember to pick one up at the pharmacy tomorrow."
                S "Thanks a lot, you jerk!"
                S "And now, I {i}really{/i} have to get back to work!"
                scene bg SleepBlack
                with fade
                $ renpy.pause ()
                scene bg SidClub50
                with dissolve
                play music ClubMusic
                S "Before you go... was there anything else you wanted to talk to me about?"
                menu:
                    "Working for the Mafia.":
                        jump mafia_chat
                    "Are you making good money?":
                        jump money_chat
                    "That's all for tonight.":
                        scene bg ImageMapCasinoWSidney
                        with fade
                        $ screen_on = "casinosidneymap"
                        call screen casinosidneymap
            "Don't risk it!":
                stop sound
                R "Hnnnggghhh!..."
                play sound Ejaculate
                scene bg SidSex66
                with fade
                with hpunch
                $ renpy.pause ()
                play sound Ejaculate
                scene bg SidSex67
                with dissolve
                with hpunch
                $ renpy.pause ()
                scene bg SidSex68
                with dissolve
                S "Fuck, [ryan]! That's so much cum!"
                scene bg SleepBlack
                with fade
                scene bg SidSex71
                with fade
                S "Thank you so much for resisting the urge to cum in my pussy!"
                scene bg SidSex69
                S "Ohh... but now it's dripping down the back of my legs!"
                S "I'll just rub it into my skin for now."
                scene bg SidSex70
                with dissolve
                R "Yeah... I hear it's supposed to be good for your skin."
                S "I don't even want to know where you heard that."
                R "No... I read it on..."
                S "Stop! I said I don't want to know."
                S "And now, I {i}really{/i} have to get back to work!"
                scene bg SleepBlack
                with fade
                $ renpy.pause ()
                scene bg SidClub50
                with dissolve
                play music ClubMusic
                S "Thanks for the distraction from work, [ryan]!"
                S "Before you go... was there anything else you wanted to talk to me about?"
                menu:
                    "Working for the Mafia.":
                        jump mafia_chat
                    "Are you making good money?":
                        jump money_chat
                    "That's all for tonight.":
                        scene bg ImageMapCasinoWSidney
                        with fade
                        $ screen_on = "casinosidneymap"
                        call screen casinosidneymap

label club_casino:                      #### Edited 9-2-2020 ####
    scene bg SleepBlack
    with fade
    scene bg SidClub11
    with fade
    R "Hey Lurch, how's it hanging?"
    R "Are you just gonna leave me hanging?"
    "...."
    R "Alright, I'll just find Mom on my own."
    scene bg SleepBlack
    with fade
    play music ClubMusic
    $ screen_on = "casinomap"
    call screen casinomap

label club_casino_with_sid:             #### Edited 9-2-2020 ####
    scene bg SleepBlack
    with fade
    scene bg SidClub11
    with fade
    R "Hey Lurch, how's it hanging?"
    R "Are you just gonna leave me hanging?"
    "...."
    R "Alright, I'll just find Sidney on my own."
    scene bg SleepBlack
    with fade
    play music ClubMusic
    $ screen_on = "casinosidneymap"
    call screen casinosidneymap

label stripper_stage:                   #### Edited 9-2-2020 ####
    if progress >= 16:
        scene bg SleepBlack
        with fade
        scene bg SidSex26
        with fade
        CD "Oh, good! You're back!"
        CD "I'm having such a slow night!... I was hoping someone would come!"
        scene bg SidSex27
        with fade
        if get_to_know_candy:
            R "Hi, Candy, how's your husband Jack?"
            scene bg SidSex28
            with dissolve
            CD "Uuugghh... Don't even talk to me about that tiny-dicked loser."
            CD "After all the dick I get here at the club, I can barely even tell when he tries to penetrate me."
            CD "I need a real big dick to grind up against tonight."
            CD "Speaking of which... I really hope you're here for a lapdance!"
        else:
            R "Hi, Candy."
            CD "Please tell me you're here for a lapdance!"
        menu:
            "Buy a lapdance. ($50)" if money >= 50:
                jump candy_danced_again
            "I'm too poor!" if money <= 49:
                R "Shit, I'd love too, but I'm don't have enough money for a lapdance."
                R "I was hoping I might see some of your moves on the pole though."
                CD "Sorry, If you don't have the money for a lapdance, I know you don't have enough to tip me."
                CD "You'll just have to wait around and hope some higher rollers show up."
                RT "{i}I don't have time to wait for that.{/i}"
                R "Alright... I'm outta here."
                scene bg SleepBlack
                with fade
                $ screen_on = "casinosidneymap"
                call screen casinosidneymap
            "Sorry, not today." if money >= 50:
                R "Yeah... I'm not really feeling it for a lapdance today."
                R "I was hoping I could just see some of your moves on the pole."
                CD "Sorry, buddy... If you're not willing to spend the money for a lapdance, with your reputation, I'm sure you wouldn't tip me either."
                CD "You'll just have to wait around and hope some higher rollers show up."
                RT "{i}I don't have time to wait for that.{/i}"
                R "Alright... I'm outta here."
                scene bg SleepBlack
                with fade
                $ screen_on = "casinosidneymap"
                call screen casinosidneymap
            "Get to know Candy." if not get_to_know_candy:
                jump candy_story_again
    else:
        scene bg ImageMapCasinoWSidney
        RT "{i}Looks like there aren't any girls on stage right now.{/i}"
        RT "{i}Hopefully there will be some girls dancing later.{/i}"
        $ screen_on = "casinosidneymap"
        call screen casinosidneymap

label candy_story_again:                #### Edited 9-2-2020 ####
    scene bg SidSex28
    with dissolve
    SR "You want to know about me?"
    R "Yeah... I'm just curious what your story is."
    SR "You mean, do I have an interesting backstory like your mom does?"
    R "Yeah... kind of... I guess..."
    scene bg SidSex27
    with dissolve
    SR "Well, it turns out that I do."
    scene bg SidSex28
    with dissolve
    CD "So, my story starts on my honeymoon, with my new husband, Jack."
    CD "We were spending it in Vegas, when somehow, Jack got invited to a high-stakes poker game."
    scene bg SidSex29
    with dissolve
    CD "During the game Jack got what he called an \"unbeatable hand\"."
    CD "He had a straight flush."
    CD "So, he bet way more than he could afford."
    CD "Well... More than we could ever afford, in both our lifetimes."
    CD "And guess what?..."
    R "He lost?"
    scene bg SidSex28
    with dissolve
    CD "Yep... That motherfucker lost to Joey DeCapo, who had a royal flush."
    CD "Long story short, I ended up spending my honeymoon with Joey, and now I have to work here once a week to pay off my loser husband's poker debt."
    CD "On top of that, Joey has me entertain important clients doing things you can only imagine in the VIP room."
    CD "Jack took me to Vegas, and made me a whore!"
    R "Wow! That sounds like it could be the plot of a movie!"
    CD "Yeah, well, I have yet to see the happy ending for this one."
    CD "Although I've given many men a happy ending."
    $ get_to_know_candy = True
    scene bg SidSex27
    with dissolve
    CD "So you can see why I need that money tonight..."
    CD "So, will you pay me for a lapdance?"
    menu:
        "Buy a lapdance. ($50)" if money >= 50:
            jump candy_danced_again
        "I'm too poor!" if money <= 49:
            R "Shit, I'd love too, but I'm don't have enough money for a lapdance."
            R "I was hoping I might see some of your moves on the pole though."
            CD "Sorry, If you don't have the money for a lapdance, I know you don't have enough to tip me."
            CD "You'll just have to wait around and hope some higher rollers show up."
            RT "{i}I don't have time to wait for that.{/i}"
            R "Alright... I'm outta here."
            scene bg SleepBlack
            with fade
            $ screen_on = "casinosidneymap"
            call screen casinosidneymap
        "Sorry, not today." if money >= 50:
            R "Yeah... I'm not really feeling it for a lapdance today."
            R "I was hoping I could just see some of your moves on the pole."
            CD "Sorry, buddy... If you're not willing to spend the money for a lapdance, with your reputation, I'm sure you wouldn't tip me either."
            CD "You'll just have to wait around and hope some higher rollers show up."
            RT "{i}I don't have time to wait for that.{/i}"
            R "Alright... I'm outta here."
            scene bg SleepBlack
            with fade
            $ screen_on = "casinosidneymap"
            call screen casinosidneymap

label candy_danced_again:               #### Edited 9-2-2020 ####
    "{i}\"Money -$50\"{/i}"
    $ money -= 50
    scene bg SidSex27
    with dissolve
    CD "Thank you so much for buying a lapdance!"
    CD "You won't be dissapointed!"
    scene bg SleepBlack
    with fade
    scene bg SidSex30
    with fade
    CD "Wow... I hope I get to see that unit up close one day."
    R "Well... Why not now?"
    CD "Oh, no!... It's against the club rules. You'd have to be a VIP card holder to get those kind of benefits."
    R "Well?... How the hell do I get one of those VIP cards?"
    CD "I don't know... I think maybe Joey gives them out."
    CD "You'd have to talk to him."
    scene SidFirstVideo06
    with fade
    $ renpy.pause ()
    R "Oh God, you can really move those hips!"
    CD "Haha... You like that?"
    R "I love it!"
    CD "For a little tip, I'll give you some more!"
    if money >= 20:
        RT "{i}I only have twenty dollar bills on me!{/i}"
        RT "{i}Is it really worth it?{/i}"
    else:
        RT "{i}Shit! I don't have the money!{/i}"
    menu:
        "I'm out of cash" if money <= 19:
            R "I'd love to pay you more, but your lapdance took all the money I had."
            CD "That's alright, honey. I really appreciate you buying a dance in the first place. Now my night wasn't a complete waste of time."
            scene bg SleepBlack
            with fade
            scene bg ImageMapCasinoWSidney
            with fade
            $ screen_on = "casinosidneymap"
            call screen casinosidneymap
        "I'm not paying this bitch any more money.":
            R "I'd love to, but I think I'd better not spend any more money tonight."
            CD "That's alright, honey. I really appreciate you buying a dance in the first place. Now my night wasn't a complete waste of time."
            scene bg SleepBlack
            with fade
            scene bg ImageMapCasinoWSidney
            with fade
            $ screen_on = "casinosidneymap"
            call screen casinosidneymap
        "Tip $20." if money >= 20:
            "{i}\"Money -$20\"{/i}"
            $ money -= 20
            scene bg SidSex30
            with fade
            CD "Twenty dollars! Now that's a great tip!"
            scene bg SidSex31
            with dissolve
            CD "Let me show you something even sweeter than my name."
            scene bg SidSex32
            with dissolve
            R "Oh, my God!"
            CD "Wow! Your dick twitch almost lifted me up an inch."
            scene SidFirstVideo07
            with fade
            $ renpy.pause ()
            R "Can I touch them?... Or even better, could I taste them?"
            CD "Sorry, the rules are to keep your hands to yourself."
            R "That's a terrible rule!"
            CD "If you spend enough money here, you might be able to become a VIP, then those kind of rules won't apply to you."
            R "How much money?"
            CD "I don't even know... You have to work it out with the boss."
            RT "{i}Hmmm... maybe I will.{/i}"
            CD "If you like what you see, you can give me another tip and I'll let you see even more."
            if money >= 20:
                RT "{i}I'd love to see more.{/i}"
                RT "{i}But is it worth another twenty bucks?{/i}"
            else:
                RT "{i}Shit! I don't have the money!{/i}"
            menu:
                "I'm out of cash" if money <= 19:
                    R "I'd love to pay you more, but your lapdance took all the money I had."
                    CD "That's alright, honey. I really appreciate you buying a dance in the first place. Now my night wasn't a complete waste of time."
                    scene bg SleepBlack
                    with fade
                    scene bg ImageMapCasinoWSidney
                    with fade
                    $ screen_on = "casinosidneymap"
                    call screen casinosidneymap
                "I'm not paying this bitch any more money.":
                    R "I'd love to, but I think I'd better not spend any more money tonight."
                    CD "That's alright, honey. I really appreciate you buying a dance in the first place. Now my night wasn't a complete waste of time."
                    scene bg SleepBlack
                    with fade
                    scene bg ImageMapCasinoWSidney
                    with fade
                    $ screen_on = "casinosidneymap"
                    call screen casinosidneymap
                "Tip $20." if money >= 20:
                    "{i}\"Money -$20\"{/i}"
                    $ money -= 20
                    scene bg SidSex32
                    with fade
                    CD "Oh, my God! Another twenty dollars? Thank you so much!"
                    CD "If you think your dick is hard now..."
                    scene bg SidSex33
                    with dissolve
                    CD "Wait until you see my sugary little funnel cake."
                    scene bg SidSex34
                    with dissolve
                    R "Oh, God! That is a sweet looking funnel cake."
                    scene SidFirstVideo08
                    with fade
                    $ renpy.pause ()
                    R "And you really know how to shake it."
                    R "I need some release!"
                    CD "Don't you dare touch yourself!"
                    CD "That's definitely not allowed here."
                    R "Oh, God! What a cocktease! I've really got to get me a VIP membership!"
                    RT "{i}I've really got to keep Mom out of here, so she doesn't have to start servicing VIP clients.{/i}"
                    RT "{i}Although... If I were the client...{/i}"
                    CD "Alright, the dance is over!"
                    scene bg SleepBlack
                    with fade
                    scene bg SidSex27
                    with fade
                    CD "Thank you for making my night so much better!"
                    CD "I really hope you do become a VIP member. I can tell that cock is so much bigger than my husband Jack's."
                    R "Thanks, Candy! I'll do everything I can to get that VIP membership card!"
                    CD "Oooo... I can't wait!"
                    CDT "{i}I can definitely wait!{/i}"
                    scene bg SleepBlack
                    with fade
                    $ screen_on = "casinosidneymap"
                    call screen casinosidneymap

label casino_exit:                      #### Edited 9-2-2020 ####
    if screen_on == "casinomap":
        scene bg Casino
    elif screen_on == "casinosidneymap":
        scene bg CasinoWSidney
    RT "{i}This place is dangerous... I shouldn't spend any more time here.{/i}"
    scene bg SleepBlack
    with fade
    play music Honey
    $ visited_sid = True
    jump citymap

label gamble_end:                       #### Edited 9-2-2020 ####
    if sidneys_working:
        scene bg ImageMapCasinoWSidney
        with fade
        $ screen_on = "casinosidneymap"
        call screen casinosidneymap
    else:
        scene bg ImageMapCasino
        with fade
        $ screen_on = "casinomap"
        call screen casinomap

#############  WAREHOUSE  ###################################  WAREHOUSE  ######################################################

label ph_shoot:                         #### Edited ####
    if not inventory.has_item(ball_gag) or not ball_gag_owned:
        scene bg PStudioHP
        "For some reason you can't start this photo shoot without a ball gag.  Why don't you go check the online store?"
        jump photostudio
    if timeofdaycounter != 4:
        scene bg PStudioHP
        "Mom and Megan are only available to take pictures in the evening."
        jump photostudio
    elif finished_hp_shoot:
        scene bg PStudioHP
        "You have completed this photo session with Mom and Megan entirely."
        "You can still play through the event, but you will not be able to increase Mom's stats, or be able to generate any more likes for the Cosplay Heaven website."
    elif weekly_hp_complete:
        scene bg PStudioHP
        "You have already done this photo session with Mom and Megan this week."
        "You will still be able to increase Mom's stats and progress through this scene,"
        "But only the first playthrough of this event each week will generate likes for the Cosplay Heaven website."
    else:
        pass

    scene bg PhotoStudio01
    with fade
    if answered_ph_wrong:
        RT "{i}Damnit! She won't even pick up!{/i}"
        RT "{i}I guess I'll have to try again tomorrow.{/i}"
        jump photostudio
    if passed_ph_test_3:
        R "Hey, Mom... I'm at the warehouse..."
        "..."
        R "Yes... Uh huh... I'll call Megan and see if she wants you to give her a ride."
        "..."
        R "No... I promise I'll be professional."
        "..."
        R "Don't forget to bring your cosplay outfits."
        "..."
        R "Ok... see you in 10 to 15 minutes."
    if read_book3 and not passed_ph_test_3:
        R "Hey, Mom... I'm at the warehouse..."
        M "{i}(muffled voice){/i} And?"
        R "And... I'm ready to do the photoshoot."
        M "Oh right... And I did see you reading... so..."
        M "Let's see how much you got out of your reading."
        M "Why did Hermione and Perry go back in time?"
        menu:
            "A) Obviously to kill baby Moldevort.":
                R "Then he'll never rise to power and kill Perry's parents."
                M "{i}(Angry silence){/i}"
                M "...."
                "{i}\"CLICK\"{/i}"
                RT "{i}Damnit!... I should have paid better attention.{/i}"
                $ answered_ph_wrong = True
                jump photostudio
            "B) To stop the dementors gangbang with Hermione":
                M "{i}(Angry silence){/i}"
                M "...."
                "{i}\"CLICK\"{/i}"
                RT "{i}Damnit!... I should have paid better attention.{/i}"
                $ answered_ph_wrong = True
                jump photostudio
            "C) To save Hermione's new love interest, Blackbeak.":
                M "Correct... I'll grab Megan from her cheerleading practice and we'll both be over soon."
                M "I'm really proud of what a Perry Hotter fan you've become."
                R "What!? No... I'm not!"
                M "Don't deny it."
                R "Fine... Maybe a little."
                M "Yay!... I can't wait to take you back to Perry Hotter Land!"
                R "Hmmm... That sounds fun, so... See you in 10 to 15 minutes?"
                M "See you soon!"
                $ passed_ph_test_3 = True
    if passed_ph_test_2 and not read_book3:
        R "Hey, Mom... I'm at the warehouse..."
        M "{i}(muffled voice){/i} And?"
        R "And... I'm ready to do the photoshoot."
        M "Ok... Have you read any of the third book yet?"
        R "Of course."
        M "Alright... Why did Perry's alleged sex offender uncle escape prison?"
        R "Sex offender uncle? Isn't this a children's book?"
        M "Yes... It doesn't say that exactly but it's implied."
        R "Hmmm... to... diddle his nephew?"
        "{i}\"CLICK\"{/i}"
        RT "{i}Damnit!... I've got to get reading... I could probably get some reading done in my room during the evenings.{/i}"
        scene bg SleepBlack
        with fade
        jump photostudio
    if read_book2 and not passed_ph_test_2:
        R "Hey, Mom... I'm at the warehouse..."
        M "{i}(muffled voice){/i} And?"
        R "And... I'm ready to do the photoshoot."
        M "Oh right... And I did see you reading... so..."
        M "Let's see how much you got out of your reading."
        M "What is the purpose of the chambers of secrets?"
        menu:
            "A) Secret sex dungeon?":
                M "Sorry... Wrong answer."
                "{i}\"CLICK\"{/i}"
                RT "{i}Damnit!... I should have paid better attention.{/i}"
                $ answered_ph_wrong = True
                jump photostudio
            "B) Aren't they just metephors for a girls vagina and asshole?":
                M "{i}(Angry silence){/i}"
                M "...."
                "{i}\"CLICK\"{/i}"
                RT "{i}Damnit!... I should have paid better attention.{/i}"
                $ answered_ph_wrong = True
                jump photostudio
            "C) For sexual awakening?":
                M "Correct... I'll grab Megan from her cheerleading practice and we'll both be over soon."
                M "And now that you've read the second book, make sure to read the third one before you ask us to do another photoshoot."
                R "Really?... But I already kind of know what it's about."
                M "[ryan]!..."
                R "Fine!... See you in 10 to 15 minutes."
                $ passed_ph_test_2 = True
    if passed_ph_test_1 and not read_book2:
        R "Hey, Mom... I'm at the warehouse..."
        M "{i}(muffled voice){/i} And?"
        R "And... I'm ready to do the photoshoot."
        M "Ok... Have you read any of the second book yet?"
        R "Of course."
        M "Alright... Who is the celebrity teacher that Hermione want's to Bang?"
        R "Wants to bang? Isn't this a children's book?"
        M "Yes... It doesn't say that exactly but it's implied."
        R "Hmmm... Diddledorf?"
        "{i}\"CLICK\"{/i}"
        RT "{i}Damnit!... I've got to get reading... I could probably get some reading done in my room during the evenings.{/i}"
        scene bg SleepBlack
        with fade
        jump photostudio
    if read_book1 and not passed_ph_test_1:
        R "Hey, Mom... I'm at the warehouse..."
        M "{i}(muffled voice){/i} And?"
        R "And... I'm ready to do the photoshoot."
        M "Oh right... And I did see you reading... so..."
        M "Let's see how much you got out of your reading."
        M "What nickname does Perry Hotter get after defeating Moldevort as a baby?"
        menu:
            "A) The boy who jizzed?":
                M "Sorry... Wrong answer."
                "{i}\"CLICK\"{/i}"
                RT "{i}Damnit!... I should have paid better attention.{/i}"
                $ answered_ph_wrong = True
                jump photostudio
            "B) The boy with the golden snatch?":
                M "Correct... I'll grab Megan from her cheerleading practice and we'll both be over soon."
                M "And now that you've read the first book, make sure to read the second one before you ask us to do another photoshoot."
                R "Really?... But I already kind of know what it's about."
                M "[ryan]!..."
                R "Fine!... See you in 10 to 15 minutes."
                $ passed_ph_test_1 = True
            "C) The boy who cockblocked Moldevort?":
                M "Sorry... Wrong answer."
                "{i}\"CLICK\"{/i}"
                RT "{i}Damnit!... I should have paid better attention.{/i}"
                $ answered_ph_wrong = True
                jump photostudio
    if inventory.has_item(ph_book1) and not read_book1:
        R "Hey, Mom... I'm at the warehouse..."
        M "{i}(muffled voice){/i} And?"
        R "And... I'm ready to do the photoshoot."
        M "Ok... Have you read any of the books yet?"
        R "Of course."
        M "Alright... What's the headmaster's sexual preference?"
        R "What? Isn't this a children's book?"
        "{i}\"CLICK\"{/i}"
        RT "{i}Damnit!... I've got to get reading... I could probably get some reading done in my room during the evenings.{/i}"
        scene bg SleepBlack
        with fade
        jump photostudio
    if first_book_owned and not read_book1:
        R "Hey, Mom... I'm at the warehouse..."
        M "{i}(muffled voice){/i} And?"
        R "And... I'm ready to do the photoshoot."
        M "Ok... Have you read any of the books yet?"
        R "Of course."
        M "Alright... What's the headmaster's sexual preference?"
        R "What? Isn't this a children's book?"
        "{i}\"CLICK\"{/i}"
        RT "{i}Damnit!... I've got to get reading... I could probably get some reading done in my room during the evenings.{/i}"
        scene bg SleepBlack
        with fade
        jump photostudio
    if not inventory.has_item(ph_book1):
        R "Hey, Mom... I'm at the warehouse..."
        M "{i}(muffled voice){/i} And?"
        R "And... I'm ready to do the photoshoot."
        M "Ok... Have you read any of the books yet?"
        R "Of course."
        M "Alright... What's the name of the headmaster at hagwarts?"
        R "Ummm... Merlin?"
        M "[ryan]... Have you even bought the book?"
        R "Ummm... No..."
        M "Uuuhhhh... Call me another time after you've read the first book."
        "{i}\"CLICK\"{/i}"
        RT "{i}Damnit!... I've got to get that stupid book! Hopefully I can find it in the online store.{/i}"
        scene bg SleepBlack
        with fade
        jump photostudio

    scene bg SleepBlack
    with fade
    "{i}\"10 to 15 minutes later.\"{/i}"
    if blackmailed_mom_matt and first_hp_shoot:
        scene bg HPCosplay13
        with fade
        MG "Hey guys! We're both here, and we're both excited for the photoshoot!"
        scene bg HPCosplay14
        with dissolve
        M "I can't say I'm thrilled to be here, but I've got to admit that your enthusiasm is infectious."
        MG "That's so sweet!"
        MB "Ok, girls... Why don't you both run and put on the sexy version of your outfits?"
        scene bg SleepBlack
        with fade
        $ renpy.pause ()
        scene bg HPCosplay99
        with fade
        MB "So, let's see... Where did we leave off?"
        MB "Let's do a quick recap of what we shot last time."
        MG "Ohhh... I'll do a recap!"
        MG "Since it's mostly about me."
        MG "So there I was, I mean there Hermione was... Which is me!"
        play music WizardingSchool
        if finished_hp_shoot:
            "{i}\"How would you like to see the rest of this photo shoot?\"{/i}"
            menu:
                "In story mode.":
                    jump ph_recap_beginning
                "Jump to the end.":
                    jump no_panties_shot
        if watched_recap:
            "{i}\"Would you like to watch the recap again?\"{/i}"
            menu:
                "Watch recap":
                    jump ph_recap_beginning
                "Jump to the photo shoot.":
                    jump advanced_ph_shoot
        else:
            pass
        jump ph_recap_beginning
    if blackmailed_mom_megan and first_hp_shoot:
        scene bg HPCosplay13
        with fade
        MG "Hey, [ryan]! We're both here, and we're both excited for the photoshoot!"
        scene bg HPCosplay14
        with dissolve
        M "I can't say I'm thrilled to be here, but I've got to admit that your enthusiasm is infectious."
        MG "That's so sweet!"
        R "Ok, girls... Why don't you both run and put on the sexy version of your outfits?"
        scene bg SleepBlack
        with fade
        $ renpy.pause ()
        scene bg HPCosplay99
        with fade
        R "So, let's see... Where did we leave off?"
        R "Let's do a quick recap of what we shot last time."
        MG "Ohhh... I'll do a recap!"
        MG "Since it's mostly about me."
        MG "So there I was, I mean there Hermione was... Which is me!"
        play music WizardingSchool
        if finished_hp_shoot:
            "{i}\"How would you like to see the rest of this photo shoot?\"{/i}"
            menu:
                "In story mode.":
                    jump ph_recap_beginning
                "Jump to the end.":
                    jump no_panties_shot
        if watched_recap:
            "{i}\"Would you like to watch the recap again?\"{/i}"
            menu:
                "Watch recap":
                    jump ph_recap_beginning
                "Jump to the photo shoot.":
                    jump advanced_ph_shoot
        else:
            pass
        jump ph_recap_beginning
    if blackmailed_mom_matt:
        scene bg HPCosplay10
        with fade
        MB "Damn! This place is legit!"
        MB "You've got some nice equipment."
        scene bg HPCosplay11
        with dissolve
        MB "{i}(quiet voice){/i}You could shoot porn videos here too, you know."
        MB "You only need a little more equipment, you wouldn't even have to pay me to be the dick in your films."
        MB "Haha... I'd willingly fuck your mom and sisters for free."
        R "Dude, fuck off!"
        scene bg HPCosplay12
        with fade
        M "Wow, [ryan]! I'm impressed."
        M "I'd imagined something much smaller."
        R "Well, it's not great, but it has a lot of potential."
        MG "It's so industrial!"
        MG "It reminds me of those new fusion restaurants I love!"
        scene bg HPCosplay13
        with dissolve
        R "Why don't you two go get changed into your outfits, and we'll get started."
        MB "Hey, don't forget that I'm directing this photoshoot."
        MB "You're just in charge of adding the backgrounds later."
        R "This is my photo studio."
        MB "Yeah, but that was part of the deal."
        scene bg HPCosplay14
        with dissolve
        MB "I'll tell you what... Since you're the more experienced photographer, I'll consult with you if I think I need some help."
        R "Alright, fine."
        MB "Alright ladies, you should get changed into your outfits so we can get started."
        scene bg SleepBlack
        with fade
        scene bg HPCosplay15
        with fade
        MG "This is so exciting!"
        MG "I look totally hot!"
        M "Uggghhh... I still can't believe I'm doing this."
        M "I don't know if I hate this drab outfit worse, or the one that leaves so little to the imagination."
        RT "{i}By the time we're done, we won't have to imagine anything.{/i}"
        MB "Alright, I think we should start the shoot with just Megan."
        scene bg HPCosplay16
        with fade
        MG "I've got my wand, and I'm all ready."
        MB "Great! Now, I want you to pretend you're Hermione Bang'er, walking through the library with a new book you found."
        MB "Do we have any old books?"
        R "We might have some old account books in the storage closet, just a second."
        "{i}\"A second later\"{/i}"
        R "Here's a whole bunch... How many do you need?"
        MB "Just one for now."
        MG "How's this?"
        scene bg HPCosplay17
        with dissolve
        MB "That's great! Let me get a shot."
        MB "How do I make this thing take pictures?"
        R "It's this button here."
        MB "Ok, got it."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay17
        MB "So [ryan]... Do you think you can make a nice library background?"
        R "Yeah, I think I've seen an asset in the 3d store for an old library."
        R "I can just picture it."
        play music WizardingSchool
        scene bg HPCosplay18
        with fade
        MB "Great! I can't wait to see what you come up with."
        MB "Ok Megs, or should I say Hermione... Now you stop and open the book you're carrying."
        MG "Ok..."
        scene bg HPCosplay19
        with fade
        MB "Perfect."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay19
        MB "And now something in the book startles you."
        MB "Because it's from the forbidden section of the library!"
        scene bg HPCosplay20
        with fade
        MB "Can you make some cool effects to come out of the book?"
        R "Yeah, you've read my mind."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay20
        MB "Nice!"
        MB "Now, you're under the spell of the forbidden book, so I want you to look up and give me an evil smile."
        scene bg HPCosplay21
        with dissolve
        MB "Perfect!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay21
        R "Though you still look cute!"
        MB "Shut up, [ryan]."
        MB "She's my girlfriend."
        MB "And you look hot, not cute."
        R "I'd say both."
        MB "Shut up."
        MB "Ok, so now that you're under the book's spell, you realize how prudish your school outfit is."
        MB "So now, let's take some shots that show the outfit becoming sexy."
        scene bg HPCosplay22
        with fade
        MB "Let's get rid of the sweater vest first."
        MB "[ryan], can you make the wand look like it's got magic coming out?"
        R "I've got it covered."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay22
        MB "Great, now let's get rid of the sweater vest."
        scene bg HPCosplay23
        with dissolve
        MB "Nice"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay23
        MB "And now let's make that shirt and tie look sexier."
        scene bg HPCosplay24
        with dissolve
        MB "Perfect!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay24
        MB "And last but not least, the skirt."
        MB "Hold it out with one hand like you're about to cast a spell on it."
        scene bg HPCosplay25
        with dissolve
        MB "Good."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay25
        MB "And now let's shorten it."
        scene bg HPCosplay26
        with dissolve
        MB "Now give me another evil smile..."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay26
        R "Hey, Mom!"
        M "What?"
        R "What can we do to get the dresscode at school to be more like that?"
        M "Hmmm... Let me think..."
        M "Maybe you can start by shoving that idea up your ass."
        R "Mom!... Language!"
        M "Shut up!"
        MG "Haha..."
        MB "Ok, back to the shoot."
        MB "Now Megs, I want you to use your wand to summon your broom."
        MG "Ok."
        scene bg HPCosplay27
        with fade
        MG "Accio Firebolt!"
        R "Haha... Did you make that up?"
        MB "No, you idiot, that's the real spell from the book."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay27
        MB "It's a good thing I'm directing this shoot, and not you."
        MB "Now, will you please hand Megan the broom?"
        scene bg HPCosplay28
        with dissolve
        MB "And now I need you to make a mischievous smile, since you're going to be causing some more trouble on that broom."
        MB "Perfect!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay28
        MB "Now, let's take some shots like you're flying on the broom."
        scene bg HPCosplay29
        with fade
        MG "How are we going to make it look like I'm flying on a broom?"
        MB "Huh... I'm not sure."
        MB "Any ideas, [ryan]?"
        R "Well, any way you pose, I can always just put you into the background so it looks like you're in the air."
        R "But we need to make it look like there's some wind from you flying so fast."
        R "Hmmm... Oh, I know!"
        R "There's some big industrial fans in one of the other warehouses to help keep the warehouse goods cool."
        R "Matt, will you come help me wheel one in here?"
        scene bg SleepBlack
        with fade
        scene bg HPCosplay31
        with fade
        "{i}\"A few minutes later.\"{/i}"
        R "This should do the trick."
        R "Matt, will you run and plug it in?"
        R "And Megan, grab that wooden pallet and you can use it to do a flying pose."
        scene bg HPCosplay32
        with fade
        MG "So, how does it look?"
        MB "Not very convincing."
        MB "I mean the hair and your skirt are blowing back, but it just doesn't look like you're flying."
        R "Just wait until I get the background, I think you'll be pleasantly surprised."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay32
        MB "Whatever you say, I hope you're right."
        scene bg HPCosplay33
        with fade
        MB "And now let's turn around and make it look like you're flying the other way."
        R "Really? That means we have to push the fan around to the other side."
        R "Just switch your hand on the broom, and I'll flip the image during Photochop so it looks like you're turned the other way."
        MG "Like this?"
        scene bg HPCosplay34
        with dissolve
        R "Yeah... And change the angle you're taking the pic from, Matt."
        MB "Ok, do you think this will work?"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay34
        R "Yeah, I can already see it in my head."
        MB "Great! And I want one more from the front."
        scene bg HPCosplay35
        with dissolve
        MB "Beautiful!"
        MG "Thanks, Matt!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay35
        MB "Ok... I think it's time to get Miss [mom_name] involved."
        MB "Miss [mom_name], can you come in front of the camera with an armful of books."
        M "Alright, do you still want the fan on?"
        MB "Yeah, I want it to look like Megs, or I mean Hermione is buzzing by you, and you're really annoyed by it."
        M "Ok, how's this?"
        scene bg HPCosplay36
        with fade
        MB "That works great!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay36
        MB "And [ryan]?"
        R "Yeah?"
        MB "Can you insert those pics of Megan to make it look like she's flying really close to your mom?"
        scene bg HPCosplay37
        with fade
        R "Yeah... I'll make sure to do that."
        MB "Great! Now let's make a few small adjustments so [ryan] can make it look like the wind is blowing the other way."
        scene bg HPCosplay38
        with dissolve
        MB "That will work, I think."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay38
        with dissolve
        MB "Ok, Miss [mom_name], drop the books like they were knocked or blown out of your arms."
        scene bg HPCosplay39
        with dissolve
        MB "Oh... and look like you're pissed off."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay39
        MB "That's great!"
        MB "Now you've had enough! It's time to stop this wicked witch."
        MB "So make an angry face, lift your wand, and cast a spell to knock her off her broom."
        scene bg HPCosplay40
        with fade
        M "Stupefy!"
        RT "{i}Oh, my God! Mom is such a nerd!{/i}"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay40
        MB "Ok Megs, I need you to come up here and make it look like you're getting knocked off a broom with a large blast of magic."
        scene bg HPCosplay41
        with fade
        MB "[ryan], can you?..."
        R "Yeah... I'll take care of all the magic and background and stuff."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay41
        MB "Ok, Miss [mom_name].  Walk up to her like you've defeated your nemesis."
        MB "And Megs, try to look all scared."
        scene bg HPCosplay42
        with fade
        R "That's actually kind of hot."
        MB "Damn hot!"
        MB "For the next scene I need a few tables and chairs."
        R "The warehouse has just about anything you need."
        MB "Nice, start thinking about how to render a detention hall for the next scene."
        scene bg SleepBlack
        with fade
        "{i}\"A few minutes later.\"{/i}"
        scene bg HPCosplay43
        with fade
        MB "Ok, so we've got Miss [mom_name] up front of the room in charge of detention."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay43
        MB "With Megs bored at her desk."
        scene bg HPCosplay44
        with fade
        MB "When she suddenly gets an idea."
        scene bg HPCosplay45
        with dissolve
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay45
        MB "She raises her hand to ask the teacher a question."
        scene bg HPCosplay46
        with fade
        MB "And she pulls out the evil book that put her under its spell."
        scene bg HPCosplay47
        with fade
        $ renpy.pause ()
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay47
        MB "When she opens the book, she encounters the same green light."
        MB "[ryan]?"
        R "Yes... I remember the green light from before."
        MB "Yeah, do the same one."
        RT "{i}I'm getting sick of him bossing me around.{/i}"
        scene bg HPCosplay48
        with fade
        MB "And now do an evil look, like you were just put under the book's spell."
        scene bg HPCosplay49
        with dissolve
        MB "Ooohh... Good evil look!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay49
        MB "Now you need to point your wand at your dress, since your new evil nature wants it to be a sexy dress."
        scene bg HPCosplay50
        with fade
        MB "Great... and..."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay50
        MB "Finally! It's time for you to get into your sexy outfit."
        scene bg HPCosplay98
        with fade
        M "I'm sorry, but I've got to call this... I know we're just getting to the good part, but I've got other stuff I need to get done."
        M "Another outfit change, and then more pictures... I just don't have any more time."
        R "Yeah... That's a good call... it's getting late."
        MB "Yeah, ok. [ryan], give us a call the next time you can let us into the studio."
        MB "We'll just pick up from where we left off today."
        R "Yeah... ok."
        play music Honey
        $ first_hp_shoot = True
        $ timeofdaycounter += 1
        jump citymap
    else:
        scene bg HPCosplay12
        with fade
        M "Wow, [ryan]! I'm impressed."
        M "I'd imagined something much smaller."
        R "Well, it's not great, but it has a lot of potential."
        MG "It's so industrial!"
        MG "It reminds me of those new fusion restaurants I love!"
        scene bg HPCosplay13
        with dissolve
        R "Thanks! I've been putting every last bit of extra money I have into this place."
        if clubcounter >= 3:
            M "Well, I can think of a few weeks where you should have used your money in a better way!"
            MG "What does that mean?"
            M "Don't worry about it."
        scene bg HPCosplay14
        with dissolve
        R "Alright ladies, you should get changed into your outfits so we can get started."
        scene bg SleepBlack
        with fade
        scene bg HPCosplay15
        with fade
        MG "This is so exciting!"
        MG "I look totally hot!"
        M "Uggghhh... I still can't believe I'm doing this."
        M "I don't know if I hate this drab outfit worse, or the one that leaves so little to the imagination."
        RT "{i}By the time we're done, we won't have to imagine anything.{/i}"
        R "Alright, I think we should start the shoot with just Megan."
        scene bg HPCosplay16
        with fade
        MG "I've got my wand, and I'm all ready."
        R "Great! Now, I want you to pretend you're Hermione Bang'er, walking through the library with a new book you found."
        R "Oh, wait!... I need some old books."
        R "We might have some old account books in the storage closet, just a second."
        scene bg SleepBlack
        with fade
        "{i}\"A second later\"{/i}"
        scene bg HPCosplay16
        with fade
        R "Here's a whole bunch..."
        R "Can you hold onto this one?"
        MG "How's this?"
        scene bg HPCosplay17
        with dissolve
        R "That's great! Let me get a shot."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay17
        R "I think I've seen an asset in the 3d store for an old library."
        R "I can just picture it."
        play music WizardingSchool
        scene bg HPCosplay18
        with fade
        R "Ok Megan, or should I say Hermione... Now you stop and open the book you're carrying."
        MG "Ok..."
        scene bg HPCosplay19
        with fade
        R "Perfect."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay19
        R "And now something in the book startles you."
        R "Because it's from the forbidden section of the library!"
        scene bg HPCosplay20
        with fade
        R "I'll make some cool effects to come out of the book."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay20
        R "Nice!"
        R "Now, you're under the spell of the forbidden book, so I want you to look up and give me an evil smile."
        scene bg HPCosplay21
        with dissolve
        R "Perfect!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay21
        R "That looks pretty evil, but sexy at the same time."
        R "Ok, so now that you're under the book's spell, you realize how prudish your school outfit is."
        R "So now let's take some shots that show the outfit becoming sexy."
        scene bg HPCosplay22
        with fade
        M "And here we go."
        R "Relax Mom, it's not like you didn't know it was this type of shoot."
        M "I know... I just still can't believe I'm part of it."
        R "Yeah... You've said that."
        R "So, back to you, Megan."
        R "Let's get rid of the sweater vest first."
        R "I'll add some effects to the wand."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay22
        R "Great, now let's get rid of the sweater vest."
        scene bg HPCosplay23
        with dissolve
        R "Nice"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay23
        R "And now let's make that shirt and tie look sexier."
        scene bg HPCosplay24
        with dissolve
        R "Perfect!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay24
        R "And last but not least, the skirt."
        R "Hold it out with one hand like you're about to cast a spell on it."
        scene bg HPCosplay25
        with dissolve
        R "Good."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay25
        R "And now let's shorten it."
        scene bg HPCosplay26
        with dissolve
        R "Now give me another evil smile..."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay26
        R "Hey, Mom!"
        M "What?"
        R "What can we do to get the dresscode at school to be more like that?"
        M "Hmmm... Let me think..."
        M "Maybe you can start by shoving that idea up your ass."
        R "Mom!... Language!"
        M "Shut up!"
        MG "Haha..."
        R "Ok, back to the shoot."
        R "Now Megan, I want you to use your wand to summon your broom."
        MG "Ok."
        scene bg HPCosplay27
        with fade
        MG "Accio Firebolt!"
        R "Haha... Did you make that up?"
        M "No you idiot, that's the real spell from the book."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay27
        M "I wish someone who knew Perry Hotter better was directing this photoshoot."
        R "I know enough..."
        R "Now, will you please hand Megan the broom?"
        scene bg HPCosplay28
        with dissolve
        R "And now I need you to make a mischievous smile, since you're going to be causing some more trouble on that broom."
        R "Perfect!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay28
        R "Now, let's take some shots like you're flying on the broom."
        scene bg HPCosplay29
        with fade
        MG "How are we going to make it look like I'm flying on a broom?"
        R "Hmmm..."
        R "Well, any way you pose, I can always just put you into the background so it looks like you're in the air."
        R "But we need to make it look like there's some wind from you flying so fast."
        R "Hmmm... Oh, I know!"
        R "There's some big industrial fans in one of the other warehouses to help keep the warehouse goods cool."
        R "Let me run and grab one."
        scene bg SleepBlack
        with fade
        scene bg HPCosplay30
        with fade
        "{i}\"A few minutes later.\"{/i}"
        R "This should do the trick."
        R "Mom, will you run and plug it in?"
        R "And Megan, grab that wooden pallet and you can use it to do a flying pose."
        scene bg HPCosplay32
        with fade
        MG "So, how does it look?"
        R "The hair and your skirt are blowing back, so I think I can make it look pretty convincing."
        R "Just wait until I get the background, I think you'll be pleasantly surprised."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay32
        R "Yeah, this should look pretty good."
        scene bg HPCosplay33
        with fade
        R "And now I want to make it look like you've turned around and are flying the other way."
        MG "Really? Does that mean we have to push the fan around to the other side?"
        R "Just switch your hand on the broom, and I'll flip the image during Photochop so it looks like you're turned the other way."
        MG "Like this?"
        scene bg HPCosplay34
        with dissolve
        R "Yeah... And I'll change the angle that I'm taking the pic from."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay34
        R "Yeah, I can already see it in my head."
        R "Great! And I want one more from the front."
        scene bg HPCosplay35
        with dissolve
        R "Beautiful!"
        MG "Thanks, [ryan]!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay35
        R "Ok... I think it's time to get Mom involved."
        R "Mom, can you come in front of the camera with an armful of books."
        M "Alright, do you still want the fan on?"
        R "Yeah, I want it to look like Megan, or I mean Hermione, is buzzing by you, and you're really annoyed by it."
        M "Ok, how's this?"
        scene bg HPCosplay36
        with fade
        R "That works great!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay36
        R "And I'll just insert those pics I just took of Megan into the pic so it looks like she's buzzing past you on her broom."
        scene bg HPCosplay37
        with fade
        R "Yeah... That'll look good."
        R "Great! Now let's make a few small adjustments so we can make it look like the wind is blowing the other way."
        scene bg HPCosplay38
        with dissolve
        R "That will work, I think."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay38
        with dissolve
        R "Ok Mom, drop the books like they were knocked or blown out of your arms."
        scene bg HPCosplay39
        with dissolve
        R "Oh... and look like you're pissed off."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay39
        R "That's great!"
        R "Now you've had enough! It's time to stop this wicked witch."
        R "So make an angry face, lift your wand, and cast a spell to knock her off her broom."
        scene bg HPCosplay40
        with fade
        M "Stupefy!"
        RT "{i}Oh, my God! Mom is such a nerd!{/i}"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay40
        R "Ok Megan, I need you to come up here and make it look like you're getting knocked off a broom with a large blast of magic."
        scene bg HPCosplay41
        with fade
        R "I'll take care of all the magic and background and stuff."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay41
        R "Ok, Mom.  Walk up to her like you've defeated your nemesis."
        R "And Megan, try to look all scared."
        scene bg HPCosplay42
        with fade
        R "That's actually kind of hot."
        R "For the next scene I need a few tables and chairs."
        R "The warehouse has just about anything I need."
        R "I can start thinking about how to render a detention hall for the next scene while I'm looking for some."
        scene bg SleepBlack
        with fade
        "{i}\"A few minutes later.\"{/i}"
        scene bg HPCosplay43
        with fade
        R "Ok, so we've got Mom up front of the room in charge of detention."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay43
        R "With Megan bored at her desk."
        scene bg HPCosplay44
        with fade
        R "When she suddenly gets an idea."
        scene bg HPCosplay45
        with dissolve
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay45
        R "She raises her hand to ask the teacher a question."
        scene bg HPCosplay46
        with fade
        R "And she pulls out the evil book that put her under its spell."
        scene bg HPCosplay47
        with fade
        $ renpy.pause ()
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay47
        R "When she opens the book, she encounters the same green light."
        scene bg HPCosplay48
        with fade
        R "And now do an evil look, like you were just put under the book's spell."
        scene bg HPCosplay49
        with dissolve
        R "Ooohh... Good evil look!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay49
        R "Now you need to point your wand at your dress, since your new evil nature wants it to be a sexy dress."
        scene bg HPCosplay50
        with fade
        R "Great... And..."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay50
        R "Finally, Mom! It's time for you to get into your sexy outfit."
        scene bg HPCosplay98
        with fade
        M "I'm sorry, but I've got to call this... I know we're just getting to the good part, but I've got other stuff I need to get done."
        M "Another outfit change, and then more pictures... I just don't have any more time."
        R "Yeah... That's a good call... it's getting late."
        R "I'll give you both a call another evening to see if your both available."
        R "We'll just pick up from where we left off today."
        MG "Yeah... ok."
        M "{i}(sarcastically){/i} I can't wait."
        play music Honey
        $ first_hp_shoot = True
        $ timeofdaycounter += 1
        jump citymap

label ph_recap_beginning:               #### Edited ####
    scene bg SleepBlack
    with fade
    $ renpy.pause ()
    scene bg HPCosplay18
    HGT "{i}Oh, Merlin's saggy left testicle! That was close!{/i}"
    HGT "{i}If I'd been caught in the forbidden section of the library, I would have cost our house over three hundred points!{/i}"
    HGT "{i}I think Ron Tiddle's diary will help Perry defeat \"He who must not be kink-shamed!\"{/i}"
    "...."
    HGT "{i}Did I just hear a noise come from the diary?{/i}"
    scene bg HPCosplay19
    with fade
    HGT "{i}I can't read this. Is this Latin?{/i}"
    HGT "{i}Perdidi nasum, sed penis maior possedi?{/i}"
    scene bg HPCosplay20
    with fade
    EV "{i}(Rasping){/i} Perdidi nasum, sed penis maior possedi!"
    scene bg HPCosplay21
    with dissolve
    HG "Yes master, but until I see it, I will cause mischief in your name."
    scene bg HPCosplay22
    with fade
    HGT "{i}First I need to do something about these drabby clothes.{/i}"
    scene bg HPCosplay23
    with dissolve
    $ renpy.pause ()
    scene bg HPCosplay24
    with dissolve
    $ renpy.pause ()
    scene bg HPCosplay25
    with dissolve
    $ renpy.pause ()
    scene bg HPCosplay26
    with dissolve
    HGT "{i}Haha... That's better! Now how should I cause trouble?{/i}"
    HGT "{i}I know!{/i}"
    scene bg HPCosplay27
    with fade
    HG "Accio Firebolt!"
    scene bg HPCosplay28
    with dissolve
    HGT "{i}And now for some fun.{/i}"
    scene bg SleepBlack
    with fade
    scene bg HPCosplay33
    with fade
    $ renpy.pause ()
    scene bg SleepBlack
    with fade
    scene bg HPCosplay34
    with fade
    $ renpy.pause ()
    scene bg SleepBlack
    with fade
    scene bg HPCosplay35
    with fade
    HGT "{i}Hahaha... There's Professor McGargleCum!{/i}"
    HGT "{i}Let's make some mischief for her.{/i}"
    scene bg HPCosplay37
    with fade
    PM "Hermione Bang'er! Get back here at once!"
    scene bg HPCosplay38
    with fade
    PM "What has gotten into you!"
    scene bg HPCosplay39
    with dissolve
    PM "That is it!"
    scene bg HPCosplay40
    with fade
    PM "Stupify!"
    scene bg HPCosplay41
    with fade
    HG "OOOHHFFF!"
    scene bg HPCosplay42
    with fade
    PM "Well, well, well..."
    PM "Miss Bang'er."
    PM "I never thought I'd see the day! What has come over you!"
    PM "One hundred points from Griffendor for causing mischief, and another one hundred points for dressing like a common Slytherin whore."
    PM "You will now follow me to detention for the next two hours."
    scene bg SleepBlack
    with fade
    $ renpy.pause ()
    scene bg HPCosplay43
    with fade
    HGT "{i}Uuucchhh... How am I supposed to cause mischief in detention?{/i}"
    scene bg HPCosplay44
    with fade
    EV "{i}(Raspy whisper){/i} Perdidi nasum, sed penis maior possedi!"
    scene bg HPCosplay45
    with dissolve
    HGT "{i}That's it!{/i}"
    scene bg HPCosplay46
    with dissolve
    HG "Professor McGargleCum, can you help me with something I read in this book that I don't understand."
    PM "It it homework for a class?"
    HG "Yes, it's something I was hoping to use in my paper for my history of Hagwarts class."
    scene bg HPCosplay47
    PM "Ron Tiddles diary? But where did you find that?"
    scene bg HPCosplay48
    with fade
    PM "Oh no!..."
    EV "{i}(Raspy growl){/i} Perdidi nasum, sed penis maior possedi!"
    scene bg HPCosplay49
    with dissolve
    PM "Yes master, but until I see it, I will cause mischief in your name."
    scene bg HPCosplay50
    with fade
    PM "But why am I in such a prudish dress?"
    $ watched_recap = True
    jump advanced_ph_shoot

label advanced_ph_shoot:                #### Edited ####
    $ timeofdaycounter += 1
    if hp_shoot_almost_finished:
        "{i}\"How would you like to see the rest of this photo shoot?\"{/i}"
        menu:
            "Stay in story mode.":
                jump ph_recap_end
            "In photo shoot mode.":
                jump advanced_ph_shoot_continued
            "Skip to the end." if finished_hp_shoot:
                jump no_panties_shot
    else:
        jump advanced_ph_shoot_continued

label advanced_ph_shoot_continued:      #### Edited ####
    scene bg SleepBlack
    with fade
    $ renpy.pause ()
    scene bg HPCosplay99
    with fade
    if blackmailed_mom_matt:
        MG "And that's where we left off."
        R "Wow! You're a great storyteller. I felt like I was in the story."
        R "And I have a feeling I'm going to like the rest of this Perry Hotter story much better then any of the others."
        R "We'll call it \"Perry Hotter and The Order of Moldy's Prostitutes.\""
        MB "Haha... or \"Perry Hotter and The Golden Snatches.\""
        R "Hahaha..."
        "...."
        M "If you're done, we've got places we need to go after this."
        MB "Oh right! Let's set up the props and begin the shoot."
        scene bg SleepBlack
        with fade
        show screen Points_screen_Mom_cosplay
        MB "Miss [mom_name], in the last pic we took of you..."
        scene bg HPCosplay50
        with fade
        MB "You were just about to make your drabby dress turn into a sexy one."
        MB "So you pointed your wand at the dress, and magic came out of your wand, and now..."
        scene bg HPCosplay51
        MB "You're in your sexy dress.  Let's get a sexy face with that pose."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay51
        MB "Perfect."
        MB "Now, you're going to show Hermione who's boss, since you're both Moldevort's slaves, one of you has to be in charge."
        MB "And Miss [mom_name], that's going to be you."
        MB "So stand aggressively in front of Megan, like she's really in trouble now, but with a look on your face like you're going to enjoy this."
        scene bg HPCosplay52
        with fade
        MB "Oh, yeah... that's scary hot!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay52
        MB "I've got to admit that I'm at a loss for creativity all of the sudden."
        MB "[ryan], I think I'm going to let you decide where to take this next, since you're more experienced."
        MB "What kind of pose should the girls do now?"
        RT "{i}What a coward... He's afraid of how Mom will react if he pushes it any farther.{/i}"
        RT "{i}So now he's putting it all on me.{/i}"
        RT "{i}Alright, I'll take control.{/i}"
        RT "{i}He is right about me having more experience.{/i}"
        R "Ok... I think..."
    else:
        MG "And that's where we left off."
        R "Wow! You're a great storyteller. I felt like I was in the story."
        R "And I have a feeling I'm going to like the rest of this Perry Hotter story much better then any of the others."
        R "We'll call it \"Perry Hotter and The Order of Moldy's Prostitutes.\""
        R "Haha... or \"Perry Hotter and The Golden Snatches.\""
        R "Hahaha..."
        "...."
        M "If you're done, we've got places we need to go after this."
        R "Oh right! Let's set up the props and begin the shoot."
        scene bg SleepBlack
        with fade
        show screen Points_screen_Mom_cosplay
        R "Mom, in the last pic we took of you..."
        scene bg HPCosplay50
        with fade
        R "You were just about to make your drabby dress turn into a sexy one."
        R "So you pointed your wand at the dress, and magic came out of your wand, and now..."
        scene bg HPCosplay51
        R "You're in your sexy dress.  Let's get a sexy face with that pose."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay51
        R "Perfect."
        R "Now, you're going to show Hermione who's boss, since you're both Moldevort's slaves, one of you has to be in charge."
        R "And Mom, that's going to be you."
        R "So stand aggressively in front of Megan, like she's really in trouble now, but with a look on your face like you're going to enjoy this."
        scene bg HPCosplay52
        with fade
        R "Oh, yeah... that's scary hot!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay52
        R "Ok... Next I think we should..."
    menu:
        "Have Megan lick Mom's boot. {i}(submission 5+ {b}{color=#0000ff}or{/color}{/b} libido 9+){/i}":
            if momsubmission >= 5 or momlibido >= 9:
                jump lick_boots
            else:
                if blackmailed_mom_matt:
                    R "Ok, I think Professor McGargleCum needs to establish dominance by first making Hermione lick her boots."
                    MB "Yeah... what better way to show dominance than humiliation."
                else:
                    R "Ok, I think Professor McGargleCum needs to establish dominance by first making Hermione lick her boots."
                    R "What better way to show dominance than humiliation?"
                scene bg HPCosplay53
                with fade
                M "Wait! That sounds really demeaning! I don't thing Megan wants to be captured on film forever doing something like that."
                MG "I don't mind."
                MG "Come on Miss [mom_name], I think most people can tell a photo shoot from reality. Plus, it's kind of hot."
                M "You think it's hot to lick a boot?"
                MG "When it's an older sexy woman dressed like you are, I do."
                M "Oh, God!"
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +1\"{/i}"
                $ momanger += 1
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to let Megan lick her boot, you need her submission points at 5 or her libido points at 9."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Have Mom rip open Megan's shirt. {i}(submission 7+ {b}{color=#0000ff}or{/color}{/b} libido 9+){/i}":
            if momsubmission >= 7 or momlibido >= 9:
                if blackmailed_mom_matt:
                    R "Ok, I think Professor MCGargleCum needs to establish dominance quickly by ripping open Hermione's shirt."
                    MB "Yeah... what better way to show dominance than humiliation."
                    scene bg HPCosplay53
                    with fade
                    M "Wait! What?"
                    R "You know... exposing Megan's breasts."
                    if first_megan_breast_reveal == False:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "We're not even asking you to get nude for this shot... You just have to be in a shot with another nude female."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Ok, I think Professor MCGargleCum needs to establish dominance quickly by ripping open Hermione's shirt."
                    R "What better way to show dominance than humiliation?"
                    scene bg HPCosplay53
                    with fade
                    M "Wait! What?"
                    R "You know... exposing Megan's breasts."
                    if first_megan_breast_reveal == False:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "We're not even asking you to get nude for this shot... You just have to be in a shot with another nude female."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                scene bg HPCosplay59
                with dissolve
                M "Yeah, I know..."
                if blackmailed_mom_matt:
                    MT "{i}I can't expose my career, let alone [ryan]'s reputation if Matt were to get us investigated.{/i}"
                else:
                    MT "{i}I can't expose my career, let alone [ryan]'s reputation if Megan were to get us investigated.{/i}"
                M "I don't like this at all, but let's do the scene."
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                    $ momsubmission += 1
                if finished_hp_shoot == False and weekly_hp_complete == False:
                    $ photoshoot_kinky += 1
                R "Great, let's just have Megan standing right here, when you just come over and rip her shirt open."
                jump megans_shirt
            else:
                if blackmailed_mom_matt:
                    R "Ok, I think Professor MCGargleCum needs to establish dominance quickly by ripping open Hermione's shirt."
                    MB "Yeah... what better way to show dominance than humiliation."
                    scene bg HPCosplay53
                    with fade
                    M "Wait! What?"
                    R "You know... exposing Megan's breasts."
                    if first_megan_breast_reveal == False:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "We're not even asking you to get nude for this shot... You just have to be in a shot with another nude female."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Ok, I think Professor MCGargleCum needs to establish dominance quickly by ripping open Hermione's shirt."
                    R "What better way to show dominance than humiliation?"
                    scene bg HPCosplay53
                    with fade
                    M "Wait! What?"
                    R "You know... exposing Megan's breasts."
                    if first_megan_breast_reveal == False:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "We're not even asking you to get nude for this shot... You just have to be in a shot with another nude female."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +1\"{/i}"
                $ momanger += 1
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to expose Megan's breasts, you need her submission points at 7 or her libido points at 9."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Have Mom tie Megan up and humiliate her. {i}(submission 10+ {b}{color=#0000ff}or{/color}{/b} libido 10){/i}":
            if momsubmission >= 10 or momlibido >= 10:
                if blackmailed_mom_matt:
                    R "Ok, I think Professor MCGargleCum needs to establish dominance quickly by exposing Hermione's breasts, tying her arms behind her back, and giving her some kind of punishment that a teacher would give a schoolgirl."
                    MB "Yeah... like making her write lines, like I had to do when I was in second grade."
                    R "That's a good idea, but her hands will be tied... I know, she can use her wand, and it's in her mouth."
                    R "That would really humiliate her."
                    scene bg HPCosplay53
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Exposing her breasts?... Tying her hands?..."
                    M "Trying to humiliate her?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "We're not even asking you to get nude for this shot... You just have to be in a shot with another nude female."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Ok, I think Professor MCGargleCum needs to establish dominance quickly by exposing Hermione's breasts, tying her arms behind her back, and giving her some kind of punishment that a teacher would give a schoolgirl."
                    R "Like making her write lines, like I had to do when I was in second grade."
                    R "Hmmm... but her hands will be tied... I know, she can use her wand, and it's in her mouth."
                    R "That would really humiliate her."
                    scene bg HPCosplay53
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Exposing her breasts?... Tying her hands?..."
                    M "Trying to humiliate her?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "We're not even asking you to get nude for this shot... You just have to be in a shot with another nude female."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                scene bg HPCosplay59
                with dissolve
                M "Yeah, I know..."
                MT "{i}I can't expose my career, let alone [ryan]'s reputation if Matt were to get us investigated.{/i}"
                M "I don't like this at all, but let's do the scene."
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                    $ momsubmission += 1
                if finished_hp_shoot == False and weekly_hp_complete == False:
                    $ photoshoot_kinky += 1
                R "Great, let's have Megan pull out her breasts, I'll tie her hands, and then Mom will point her wand at the knots to look like she tied the knot with magic."
                jump megan_tied
            else:
                if blackmailed_mom_matt:
                    R "Ok, I think Professor MCGargleCum needs to establish dominance quickly by exposing Hermione's breasts, tying her arms behind her back, and giving her some kind of punishment that a teacher would give a schoolgirl."
                    MB "Yeah... like making her write lines, like I had to do when I was in second grade."
                    R "That's a good idea, but her hands will be tied... I know, she can use her wand, and it's in her mouth."
                    R "That would really humiliate her."
                    scene bg HPCosplay53
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Exposing her breasts?... Tying her hands?..."
                    M "Trying to humiliate her?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "We're not even asking you to get nude for this shot... You just have to be in a shot with another nude female."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Ok, I think Professor MCGargleCum needs to establish dominance quickly by exposing Hermione's breasts, tying her arms behind her back, and giving her some kind of punishment that a teacher would give a schoolgirl."
                    R "Like making her write lines, like I had to do when I was in second grade."
                    R "Hmmm... but her hands will be tied... I know, she can use her wand, and it's in her mouth."
                    R "That would really humiliate her."
                    scene bg HPCosplay53
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Exposing her breasts?... Tying her hands?..."
                    M "Trying to humiliate her?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "We're not even asking you to get nude for this shot... You just have to be in a shot with another nude female."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +1\"{/i}"
                $ momanger += 1
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to tie up and humiliate Megan, you need her submission points at 10 or her libido points at 10."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Have Mom expose her breasts and gag Megan. {i}(submission 14+){/i}":
            if momsubmission >= 14:
                if blackmailed_mom_matt:
                    R "Ok, I think Professor MCGargleCum needs to establish dominance quickly by exposing both of their breasts and silencing Hermione with a ball gag."
                    MB "My God! Do you have a ball gag?"
                    R "I just so happen to have one."
                    RT "{i}Ha... I knew this would come in handy.{/i}"
                    scene bg HPCosplay53
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Exposing our breasts?... A ball gag!?..."
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "It's just some light nudity and a ball gag... It's pretty tame for most cosplay photo shoots these days."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Ok, I think Professor MCGargleCum needs to establish dominance quickly by exposing both of their breasts and silencing Hermione with a ball gag."
                    MB "My God! Do you have a ball gag?"
                    R "I just so happen to have one."
                    RT "Ha... I knew this would come in handy."
                    scene bg HPCosplay53
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Exposing our breasts?... A ball gag!?..."
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "It's just some light nudity and a ball gag... It's pretty tame for most cosplay photo shoots these days."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                scene bg HPCosplay59
                with dissolve
                M "Yeah, I know..."
                MT "{i}I can't expose my career, let alone [ryan]'s reputation if Matt were to get us investigated.{/i}"
                M "I don't like this at all, but let's do the scene."
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                    $ momsubmission += 1
                if finished_hp_shoot == False and weekly_hp_complete == False:
                    $ photoshoot_kinky += 1
                R "Great, let's just have Megan look like she's yelling at you, challenging your authority... That's when you'll need to use the ball gag."
                jump ball_gagged
            else:
                if blackmailed_mom_matt:
                    R "Ok, I think Professor MCGargleCum needs to establish dominance quickly by exposing both of their breasts and silencing Hermione with a ball gag."
                    MB "My God! Do you have a ball gag?"
                    R "I just so happen to have one."
                    RT "{i}Ha... I knew this would come in handy.{/i}"
                    scene bg HPCosplay53
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Exposing our breasts?... A ball gag!?..."
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "It's just some light nudity and a ball gag... It's pretty tame for most cosplay photo shoots these days."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Ok, I think Professor MCGargleCum needs to establish dominance quickly by exposing both of their breasts and silencing Hermione with a ball gag."
                    MB "My God! Do you have a ball gag?"
                    R "I just so happen to have one."
                    RT "{i}Ha... I knew this would come in handy.{/i}"
                    scene bg HPCosplay53
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Exposing our breasts?... A ball gag!?..."
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "It's just some light nudity and a ball gag... It's pretty tame for most cosplay photo shoots these days."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +1\"{/i}"
                $ momanger += 1
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to ball gag Megan, you need her submission points at 14."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Have Mom remove Megan's panties and spank her. {i}(submission 19+){/i}":
            if momsubmission >= 19:
                if blackmailed_mom_matt:
                    R "Ok, I think Professor MCGargleCum needs to establish dominance quickly by giving Hermione a good old-fashioned spanking."
                    R "After she's removed Hermione's panties and exposed both of their breasts, of course."
                    MB "Oh yeah, nothing establishes dominance like a good spanking."
                    MB "Let's go ahead and do that."
                    scene bg HPCosplay53
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Taking off Megan's panties and spanking her with the wand?... Exposing our breasts?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "It's just some light nudity on your part, and Megan is totally comfortable with showing a little more.  It's actaully pretty tame compared to some of the other cosplay stuff on the internet."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Ok, I think Professor MCGargleCum needs to establish dominance quickly by giving Hermione a good old-fashioned spanking."
                    R "After she's removed Hermione's panties and exposed both of their breasts, of course."
                    R "Nothing establishes dominance like a good spanking."
                    M "Whoa, whoa, whoa, hold up."
                    M "Taking off Megan's panties and spanking her with the wand?... Exposing our breasts?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "It's just some light nudity on your part, and Megan is totally comfortable with showing a little more.  It's actaully pretty tame compared to some of the other cosplay stuff on the internet."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                scene bg HPCosplay59
                with dissolve
                M "Yeah, I know..."
                MT "{i}I can't expose my career, let alone [ryan]'s reputation if Matt were to get us investigated.{/i}"
                M "I don't like this at all, but let's do the scene."
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                    $ momsubmission += 1
                if finished_hp_shoot == False and weekly_hp_complete == False:
                    $ photoshoot_kinky += 1
                R "Great, you two just let the girls breathe, and let's have Megan bend over that table, I mean \"desk\", to get ready for her spanking."
                R "Oh... and just to make it even more hot, Megan will be wearing this ball gag."
                M "Where'd you get a ball gag?"
                R "That's not important, let's take some pics!"
                jump megan_spanked
            else:
                if blackmailed_mom_matt:
                    R "Ok, I think Professor MCGargleCum needs to establish dominance quickly by giving Hermione a good old-fashioned spanking."
                    R "After she's removed Hermione's panties and exposed both of their breasts, of course."
                    MB "Oh yeah, nothing establishes dominance like a good spanking."
                    MB "Let's go ahead and do that."
                    scene bg HPCosplay53
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Taking off Megan's panties and spanking her with the wand?... Exposing our breasts?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "It's just some light nudity on your part, and Megan is totally comfortable with showing a little more.  It's actaully pretty tame compared to some of the other cosplay stuff on the internet."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Ok, I think Professor MCGargleCum needs to establish dominance quickly by giving Hermione a good old-fashioned spanking."
                    R "After she's removed Hermione's panties and exposed both of their breasts, of course."
                    R "Nothing establishes dominance like a good spanking."
                    M "Whoa, whoa, whoa, hold up."
                    M "Taking off Megan's panties and spanking her with the wand?... Exposing our breasts?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "It's just some light nudity on your part, and Megan is totally comfortable with showing a little more.  It's actaully pretty tame compared to some of the other cosplay stuff on the internet."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +1\"{/i}"
                $ momanger += 1
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to spank Megan, you need her submission points at 19."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Have Mom remove her panties and pose with Megan. {i}(submission 25+){/i}":
            if momsubmission >= 25:
                if blackmailed_mom_matt:
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    MB "Huh?... I kind of thought we'd build up to that."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    MB "Alright, you heard him, ladies."
                    scene bg HPCosplay53
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Removing both our tops and bottoms?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "I'm only asking you to do what every other photographer asks their models to do."
                    M "But I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    scene bg HPCosplay53
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Removing both our tops and bottoms?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "I'm only asking you to do what every other photographer asks their models to do."
                    M "But I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                scene bg HPCosplay59
                with dissolve
                M "Yeah, I know..."
                MT "{i}I can't expose my career, let alone [ryan]'s reputation if Matt were to get us investigated.{/i}"
                M "I don't like this at all, but let's do the scene."
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                    $ momsubmission += 1
                if finished_hp_shoot == False and weekly_hp_complete == False:
                    $ photoshoot_kinky += 1
                R "How about a pose where Megan is on all fours with her skirt up so we can see that she's not wearing any panties, and Mom will be dominating her by sitting on her."
                R "Oh... and just to make it even more hot, Megan will be wearing this ball gag."
                M "Where'd you get a ball gag?"
                R "That's not important, let's take some pics!"
                jump no_panties_shot
            else:
                if blackmailed_mom_matt:
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    MB "Huh?... I kind of thought we'd build up to that."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    MB "Alright, you heard him, ladies."
                    scene bg HPCosplay53
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Removing both our tops and bottoms?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "I'm only asking you to do what every other photographer asks their models to do."
                    M "But I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    scene bg HPCosplay53
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Removing both our tops and bottoms?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "I'm only asking you to do what every other photographer asks their models to do."
                    M "But I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +5\"{/i}"
                $ momanger += 5
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to pose naked with Megan, you need her submission points at 25."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Maybe we should end the shoot for today.":
            if blackmailed_mom_matt:
                scene bg HPCosplay56
                with fade
                R "I don't think we need to take any more pics today."
                MB "Really? We haven't taken very many."
                R "Yeah, but the ones we have are really good, and the only way they could be better is if we pushed the girls into something they might not be comfortable with."
                scene bg HPCosplay58
                with dissolve
                M "Oh, [ryan]! You really do act like a professional photographer."
                M "And that wasn't nearly as bad as I thought it would be!"
                M "And even though I'm being coerced into this, you both helped me feel pretty comfortable!"
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Mom's Libido +5\"{/b}{/i}"
                    $ momaffection += 1
                    $ momlibido += 5
                M "The next photo shoot might not make me feel so uneasy now."
                M "I might be even more daring, and be willing to show a little more skin... maybe..."
                MB "Great! I can't wait!"
                RT "{i}Ugghh... I wish Matt wasn't going to be there.{/i}"
            else:
                scene bg HPCosplay56
                with fade
                R "I don't think we need to take any more pics today."
                MG "Really? We haven't taken very many."
                R "Yeah, but the ones we have are really good, and the only way they could be better is if we pushed the girls into something they might not be comfortable with."
                scene bg HPCosplay58
                with dissolve
                M "Oh, [ryan]! You really do act like a professional photographer."
                M "And that wasn't nearly as bad as I thought it would be!"
                M "And even though I'm being coerced into this, you both helped me feel pretty comfortable!"
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Mom's Libido +5\"{/b}{/i}"
                    $ momaffection += 1
                    $ momlibido += 5
                M "The next photo shoot might not make me feel so uneasy now."
                M "I might be even more daring, and be willing to show a little more skin... maybe..."
                MG "Great! I can't wait!"
                RT "{i}Neither can I... I just need to be careful about pushing Mom too hard, and too fast... That's what she said.{/i}"
            R "You can get changed and I'll see you back home."
            hide screen Points_screen_Mom_cosplay
            jump posting_the_wr_pics

label lick_boots:                       #### Edited ####
    if blackmailed_mom_matt:
        R "Ok, I think Professor McGargleCum needs to establish dominance by first making Hermione lick her boots."
        MB "Yeah... what better way to show dominance than humiliation."
        scene bg HPCosplay53
        with fade
        M "Wait! That sounds really demeaning! I don't thing Megan wants to be captured on film forever doing something like that."
        MG "I don't mind."
        MG "Come on Miss [mom_name], I think most people can tell a photo shoot from reality. Plus, it's kind of hot."
        M "You think it's hot to lick a boot?"
        MG "When it's an older sexy woman dressed like you are, I do."
        M "Oh, God!"
        if not finished_hp_shoot:
            "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
            $ momsubmission += 1
        if finished_hp_shoot == False and weekly_hp_complete == False:
            $ photoshoot_kinky += 1
        MB "Ok... let's set the scene..."
        MB "Miss [mom_name], you go sit in that chair by where your desk would be, and Megan get on all fours and lick Miss [mom_name]'s boot."
        MB "And Miss [mom_name]?"
        M "Yeah?"
        MB "Try to look happy about it, and evil at the same time."
        scene bg HPCosplay54
        with fade
        R "This is great! I love the upskirt shot of Megan!"
        M "[ryan]!"
        R "Sorry, I can't help it."
        MB "Yeah, this is pretty hot."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay54
        R "Especially picturing this situation with the right background."
        scene bg HPCosplay55
        with fade
        R "Oh, yeah... I can see the whole situation in the Hagwarts detention room."
        MB "I can't wait to see what you come up with!"
        MG "Me either!"
        M "I dread it."
        scene bg SleepBlack
        with fade
        scene bg HPCosplay101
        with fade
        R "Oh come on Mom, try to loosen up and have more fun."
        R "I know you always wanted to be a model."
        M "Yeah, but not like this."
        MB "I'm sure you'll warm up to all this."
        MB "So that ended up pretty dang hot"
        MB "Any ideas for what should come next?"
    else:
        R "Ok, I think Professor McGargleCum needs to establish dominance by first making Hermione lick her boots."
        R "What better way to show dominance than humiliation?"
        scene bg HPCosplay53
        with fade
        M "Wait! That sounds really demeaning! I don't thing Megan wants to be captured on film forever doing something like that."
        MG "I don't mind."
        MG "Come on Miss [mom_name], I think most people can tell a photo shoot from reality. Plus, it's kind of hot."
        M "You think it's hot to lick a boot?"
        MG "When it's an older sexy woman dressed like you are, I do."
        M "Oh, God!"
        if not finished_hp_shoot:
            "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
            $ momsubmission += 1
        if finished_hp_shoot == False and weekly_hp_complete == False:
            $ photoshoot_kinky += 1
        R "Ok... let's set the scene..."
        R "Mom, you go sit in that chair by where your desk would be, and Megan get on all fours and lick Mom's boot."
        R "And Mom?"
        M "Yeah?"
        R "Try to look happy about it, and evil at the same time."
        scene bg HPCosplay54
        with fade
        R "This is great! I love the upskirt shot of Megan!"
        M "[ryan]!"
        R "Sorry, I can't help it."
        R "This is pretty hot."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay54
        R "Especially picturing this situation with the right background."
        scene bg HPCosplay55
        with fade
        R "Oh, yeah... I can see the whole situation in the Hagwarts detention room."
        MG "I can't wait to see what you come up with!"
        M "I dread it."
        scene bg SleepBlack
        with fade
        scene bg HPCosplay101
        with fade
        R "Oh come on Mom, try to loosen up and have more fun."
        R "I know you always wanted to be a model."
        M "Yeah, but not like this."
        R "I'm sure you'll warm up to all this."
        R "So... What should we have you two do next?"
    R "Maybe..."
    menu:
        "Have Mom rip open Megan's shirt. {i}(submission 7+ {b}{color=#0000ff}or{/color}{/b} libido 9+){/i}":
            if momsubmission >= 7 or momlibido >= 9:
                if blackmailed_mom_matt:
                    R "We should have Mom pull open Megan's shirt."
                    MB "Yeah, that would definitely be more humiliating than licking her boot."
                    scene bg HPCosplay56
                    with fade
                    M "Wait! What?"
                    R "You know... exposing Megan's breasts."
                    if first_megan_breast_reveal == False:
                        scene bg HPCosplay57
                        with dissolve
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        scene bg HPCosplay57
                        with dissolve
                        M "I still can't believe you're asking me to do this."
                    R "We're not even asking you to get nude for this shot... You just have to be in a shot with another nude female."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Mom, you should pull open Megan's shirt."
                    R "That would definitely be more humiliating than licking her boot."
                    scene bg HPCosplay56
                    with fade
                    M "Wait! What?"
                    R "You know... exposing Megan's breasts."
                    if first_megan_breast_reveal == False:
                        scene bg HPCosplay57
                        with dissolve
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        scene bg HPCosplay57
                        with dissolve
                        M "I still can't believe you're asking me to do this."
                    R "We're not even asking you to get nude for this shot... You just have to be in a shot with another nude female."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                scene bg HPCosplay59
                with dissolve
                M "Yeah, I know..."
                MT "{i}I can't expose my career, let alone [ryan]'s reputation if Matt were to get us investigated.{/i}"
                M "I don't like this at all, but let's do the scene."
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                    $ momsubmission += 1
                if finished_hp_shoot == False and weekly_hp_complete == False:
                    $ photoshoot_kinky += 1
                R "Great, let's just have Megan standing right here, when you just come over and rip her shirt open."
                jump megans_shirt
            else:
                if blackmailed_mom_matt:
                    R "We should have Mom pull open Megan's shirt."
                    MB "Yeah, that would definitely be more humiliating than licking her boot."
                    scene bg HPCosplay56
                    with fade
                    M "Wait! What?"
                    R "You know... exposing Megan's breasts."
                    if first_megan_breast_reveal == False:
                        scene bg HPCosplay57
                        with dissolve
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        scene bg HPCosplay57
                        with dissolve
                        M "I still can't believe you're asking me to do this."
                    R "We're not even asking you to get nude for this shot... You just have to be in a shot with another nude female."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Mom, you should pull open Megan's shirt."
                    R "That would definitely be more humiliating than licking her boot."
                    scene bg HPCosplay56
                    with fade
                    M "Wait! What?"
                    R "You know... exposing Megan's breasts."
                    if first_megan_breast_reveal == False:
                        scene bg HPCosplay57
                        with dissolve
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        scene bg HPCosplay57
                        with dissolve
                        M "I still can't believe you're asking me to do this."
                    R "We're not even asking you to get nude for this shot... You just have to be in a shot with another nude female."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                scene bg HPCosplay56
                with dissolve
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +1\"{/i}"
                $ momanger += 1
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to expose Megan's breasts, you need her submission points at 7 or her libido points at 9."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Have Mom tie Megan up and humiliate her. {i}(submission 10+ {b}{color=#0000ff}or{/color}{/b} libido 10){/i}":
            if momsubmission >= 10 or momlibido >= 10:
                if blackmailed_mom_matt:
                    R "Ok, I think Professor MCGargleCum needs to continue her push for dominance by exposing Hermione's breasts, tying her arms behind her back, and giving her some kind of punishment that a teacher would give a schoolgirl."
                    MB "Yeah... like making her write lines, like I had to do when I was in second grade."
                    R "That's a good idea, but her hands will be tied... I know, she can use her wand, and it's in her mouth."
                    R "That would really humiliate her."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Exposing her breasts?... Tying her hands?..."
                    M "Trying to humiliate her?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "We're not even asking you to get nude for this shot... You just have to be in a shot with another nude female."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Ok, I think Professor MCGargleCum needs to continue her push for dominance by exposing Hermione's breasts, tying her arms behind her back, and giving her some kind of punishment that a teacher would give a schoolgirl."
                    R "Like making her write lines, like I had to do when I was in second grade."
                    R "Hmmm... but her hands will be tied... I know, she can use her wand, and it's in her mouth."
                    R "That would really humiliate her."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Exposing her breasts?... Tying her hands?..."
                    M "Trying to humiliate her?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "We're not even asking you to get nude for this shot... You just have to be in a shot with another nude female."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                scene bg HPCosplay59
                with dissolve
                M "Yeah, I know..."
                MT "{i}I can't expose my career, let alone [ryan]'s reputation if Matt were to get us investigated.{/i}"
                M "I don't like this at all, but let's do the scene."
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                    $ momsubmission += 1
                if finished_hp_shoot == False and weekly_hp_complete == False:
                    $ photoshoot_kinky += 1
                R "Great, let's have Megan pull out her breasts, I'll tie her hands, and then Mom will point her wand at the knots to look like she tied the knot with magic."
                jump megan_tied
            else:
                if blackmailed_mom_matt:
                    R "Ok, I think Professor MCGargleCum needs to continue her push for dominance by exposing Hermione's breasts, tying her arms behind her back, and giving her some kind of punishment that a teacher would give a schoolgirl."
                    MB "Yeah... like making her write lines, like I had to do when I was in second grade."
                    R "That's a good idea, but her hands will be tied... I know, she can use her wand, and it's in her mouth."
                    R "That would really humiliate her."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Exposing her breasts?... Tying her hands?..."
                    M "Trying to humiliate her?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "We're not even asking you to get nude for this shot... You just have to be in a shot with another nude female."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Ok, I think Professor MCGargleCum needs to continue her push for dominance by exposing Hermione's breasts, tying her arms behind her back, and giving her some kind of punishment that a teacher would give a schoolgirl."
                    R "Like making her write lines, like I had to do when I was in second grade."
                    R "Hmmm... but her hands will be tied... I know, she can use her wand, and it's in her mouth."
                    R "That would really humiliate her."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Exposing her breasts?... Tying her hands?..."
                    M "Trying to humiliate her?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "We're not even asking you to get nude for this shot... You just have to be in a shot with another nude female."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +1\"{/i}"
                $ momanger += 1
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to tie up and humiliate Megan, you need her submission or libido points at 10."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Have Mom expose her breasts and gag Megan. {i}(submission 14+){/i}":
            if momsubmission >= 14:
                if blackmailed_mom_matt:
                    R "Ok, I think Professor MCGargleCum needs to continue her push for dominance by exposing both of their breasts and silencing Hermione with a ball gag."
                    MB "My God! Do you have a ball gag?"
                    R "I just so happen to have one."
                    RT "{i}Ha... I knew this would come in handy.{/i}"
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Exposing our breasts?... A ball gag!?..."
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "It's just some light nudity and a ball gag... It's pretty tame for most cosplay photo shoots these days."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Ok, I think Professor MCGargleCum needs to continue her push for dominance by exposing both of their breasts and silencing Hermione with a ball gag."
                    MB "My God! Do you have a ball gag?"
                    R "I just so happen to have one."
                    RT "{i}Ha... I knew this would come in handy.{/i}"
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Exposing our breasts?... A ball gag!?..."
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "It's just some light nudity and a ball gag... It's pretty tame for most cosplay photo shoots these days."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                scene bg HPCosplay59
                with dissolve
                M "Yeah, I know..."
                MT "{i}I can't expose my career, let alone [ryan]'s reputation if Matt were to get us investigated.{/i}"
                M "I don't like this at all, but let's do the scene."
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                    $ momsubmission += 1
                if finished_hp_shoot == False and weekly_hp_complete == False:
                    $ photoshoot_kinky += 1
                R "Great, let's just have Megan look like she's yelling at you, challenging your authority... That's when you'll need to use the ball gag."
                jump ball_gagged
            else:
                if blackmailed_mom_matt:
                    R "Ok, I think Professor MCGargleCum needs to continue her push for dominance by exposing both of their breasts and silencing Hermione with a ball gag."
                    MB "My God! Do you have a ball gag?"
                    R "I just so happen to have one."
                    RT "{i}Ha... I knew this would come in handy.{/i}"
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Exposing our breasts?... A ball gag!?..."
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "It's just some light nudity and a ball gag... It's pretty tame for most cosplay photo shoots these days."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Ok, I think Professor MCGargleCum needs to continue her push for dominance by exposing both of their breasts and silencing Hermione with a ball gag."
                    MB "My God! Do you have a ball gag?"
                    R "I just so happen to have one."
                    RT "{i}Ha... I knew this would come in handy.{/i}"
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Exposing our breasts?... A ball gag!?..."
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "It's just some light nudity and a ball gag... It's pretty tame for most cosplay photo shoots these days."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +1\"{/i}"
                $ momanger += 1
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to ball gag Megan, you need her submission points at 14."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Have Mom remove Megan's panties and spank her. {i}(submission 19+){/i}":
            if momsubmission >= 19:
                if blackmailed_mom_matt:
                    R "Ok, I think Professor MCGargleCum needs to continue her push for dominance by giving Hermione a good old-fashioned spanking."
                    R "After she's removed Hermione's panties and exposed both of their breasts, of course."
                    MB "Oh yeah, nothing establishes dominance like a good spanking."
                    MB "Let's go ahead and do that."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Taking off Megan's panties and spanking her with the wand?... Exposing our breasts?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "It's just some light nudity on your part, and Megan is totally comfortable with showing a little more.  It's actaully pretty tame compared to some of the other cosplay stuff on the internet."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Ok, I think Professor MCGargleCum needs to continue her push for dominance by giving Hermione a good old-fashioned spanking."
                    R "After she's removed Hermione's panties and exposed both of their breasts, of course."
                    R "Nothing establishes dominance like a good spanking."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Taking off Megan's panties and spanking her with the wand?... Exposing our breasts?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "It's just some light nudity on your part, and Megan is totally comfortable with showing a little more.  It's actaully pretty tame compared to some of the other cosplay stuff on the internet."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                scene bg HPCosplay59
                with dissolve
                M "Yeah, I know..."
                MT "{i}I can't expose my career, let alone [ryan]'s reputation if Matt were to get us investigated.{/i}"
                M "I don't like this at all, but let's do the scene."
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                    $ momsubmission += 1
                if finished_hp_shoot == False and weekly_hp_complete == False:
                    $ photoshoot_kinky += 1
                R "Great, you two just let the girls breathe, and let's have Megan bend over that table, I mean \"desk\", to get ready for her spanking."
                R "Oh... and just to make it even more hot, Megan will be wearing this ball gag."
                M "Where'd you get a ball gag?"
                R "That's not important, let's take some pics!"
                jump megan_spanked
            else:
                if blackmailed_mom_matt:
                    R "Ok, I think Professor MCGargleCum needs to continue her push for dominance by giving Hermione a good old-fashioned spanking."
                    R "After she's removed Hermione's panties and exposed both of their breasts, of course."
                    MB "Oh yeah, nothing establishes dominance like a good spanking."
                    MB "Let's go ahead and do that."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Taking off Megan's panties and spanking her with the wand?... Exposing our breasts?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "It's just some light nudity on your part, and Megan is totally comfortable with showing a little more.  It's actaully pretty tame compared to some of the other cosplay stuff on the internet."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Ok, I think Professor MCGargleCum needs to continue her push for dominance by giving Hermione a good old-fashioned spanking."
                    R "After she's removed Hermione's panties and exposed both of their breasts, of course."
                    R "Nothing establishes dominance like a good spanking."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Taking off Megan's panties and spanking her with the wand?... Exposing our breasts?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "It's just some light nudity on your part, and Megan is totally comfortable with showing a little more.  It's actaully pretty tame compared to some of the other cosplay stuff on the internet."
                    M "I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +1\"{/i}"
                $ momanger += 1
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to spank Megan, you need her submission points at 19."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Have Mom remove her panties and pose with Megan. {i}(submission 25+){/i}":
            if momsubmission >= 25:
                if blackmailed_mom_matt:
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    MB "Huh?... I kind of thought we'd build up to that."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    MB "Alright, you heard him, ladies."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Removing both our tops and bottoms?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "I'm only asking you to do what every other photographer asks their models to do."
                    M "But I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Removing both our tops and bottoms?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "I'm only asking you to do what every other photographer asks their models to do."
                    M "But I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                scene bg HPCosplay59
                with dissolve
                M "Yeah, I know..."
                MT "{i}I can't expose my career, let alone [ryan]'s reputation if Matt were to get us investigated.{/i}"
                M "I don't like this at all, but let's do the scene."
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                    $ momsubmission += 1
                if finished_hp_shoot == False and weekly_hp_complete == False:
                    $ photoshoot_kinky += 1
                R "How about a pose where Megan is on all fours with her skirt up so we can see that she's not wearing any panties, and Mom will be dominating her by sitting on her."
                R "Oh... and just to make it even more hot, Megan will be wearing this ball gag."
                M "Where'd you get a ball gag?"
                R "That's not important, let's take some pics!"
                jump no_panties_shot
            else:
                if blackmailed_mom_matt:
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    MB "Huh?... I kind of thought we'd build up to that."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    MB "Alright, you heard him, ladies."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Removing both our tops and bottoms?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "I'm only asking you to do what every other photographer asks their models to do."
                    M "But I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Removing both our tops and bottoms?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think we're going to do nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "I'm only asking you to do what every other photographer asks their models to do."
                    M "But I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +5\"{/i}"
                $ momanger += 5
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to pose naked with Megan, you need her submission points at 25."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Maybe we should end the shoot for today.":
            if blackmailed_mom_matt:
                scene bg HPCosplay56
                with fade
                R "I don't think we need to take any more pics today."
                MB "Really? We haven't taken very many."
                R "Yeah, but the ones we have are really good, and the only way they could be better is if we pushed the girls into something they might not be comfortable with."
                scene bg HPCosplay58
                with dissolve
                M "Oh, [ryan]! You really do act like a professional photographer."
                M "And that wasn't nearly as bad as I thought it would be!"
                M "And even though I'm being coerced into this, you both helped me feel pretty comfortable!"
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Mom's Libido +5\"{/b}{/i}"
                    $ momaffection += 1
                    $ momlibido += 5
                M "The next photo shoot might not make me feel so uneasy now."
                M "I might be even more daring, and be willing to show a little more skin... maybe..."
                MB "Great! I can't wait!"
                RT "{i}Ugghh... I wish Matt wasn't going to be there.{/i}"
            else:
                scene bg HPCosplay56
                with fade
                R "I don't think we need to take any more pics today."
                MG "Really? We haven't taken very many."
                R "Yeah, but the ones we have are really good, and the only way they could be better is if we pushed the girls into something they might not be comfortable with."
                scene bg HPCosplay58
                with dissolve
                M "Oh, [ryan]! You really do act like a professional photographer."
                M "And that wasn't nearly as bad as I thought it would be!"
                M "And even though I'm being coerced into this, you both helped me feel pretty comfortable!"
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Mom's Libido +5\"{/b}{/i}"
                    $ momaffection += 1
                    $ momlibido += 5
                M "The next photo shoot might not make me feel so uneasy now."
                M "I might be even more daring, and be willing to show a little more skin... maybe..."
                MG "Great! I can't wait!"
                RT "{i}Neither can I... I just need to be careful about pushing Mom too hard, and too fast... That's what she said.{/i}"
            R "You can get changed and I'll see you back home."
            hide screen Points_screen_Mom_cosplay
            jump posting_the_wr_pics

label megans_shirt:                     #### Edited ####
    scene bg HPCosplay56
    with dissolve
    MT "{i}I can't believe I'm going to do this!{/i}"
    MT "{i}I've never done anything like this to another woman.{/i}"
    MT "{i}I would never have imagined doing this to one of my students.{/i}"
    MT "{i}Then again, I've been forced into a situation that I never thought in a million years I'd find myself in.{/i}"
    MG "Ok, Miss [mom_name], I'm ready."
    scene bg HPCosplay60
    with fade
    if blackmailed_mom_matt:
        MB "Now Megan, try to look really surprised that she did that!"
        MB "That's perfect!"
        MB "Hold that pose."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay60
        R "Really sexy!"
        M "[ryan], would you stop commenting on everything I do as being sexy?"
        M "It's just kind of weird."
        MT "{i}Even weirder that it's true!{/i}"
        MT "{i}Look at how cute her little breasts are.{/i}"
        MT "{i}And somehow, that look of surprise on her face makes the situation even hotter.{/i}"
        if not finished_hp_shoot:
            "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
            $ momlibido += 1
        MB "Really good job, both of you!"
        MB "[ryan], have you got any other good ideas for which poses we should have the girls do next?"
    else:
        R "Now Megan, try to look really surprised that she did that!"
        R "That's perfect!"
        R "Hold that pose."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay60
        R "Really sexy!"
        M "[ryan], would you stop commenting on everything I do as being sexy?"
        M "It's just kind of weird."
        MT "{i}Even weirder that it's true!{/i}"
        MT "{i}Look at how cute her little breasts are.{/i}"
        MT "{i}And somehow, that look of surprise on her face makes the situation even hotter.{/i}"
        if not finished_hp_shoot:
            "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
            $ momlibido += 1
        R "Really good job, both of you!"
        scene bg HPCosplay102
        RT "{i}OK... What should I have the girls do next{/i}?"
    menu:
        "Have Mom tie Megan up and humiliate her. {i}(submission 10+ {b}{color=#0000ff}or{/color}{/b} libido 10){/i}":
            if momsubmission >= 10 or momlibido >= 10:
                if blackmailed_mom_matt:
                    R "Since this shoot is detention themed, we need to have Professor McGargleCum force her to do something that usually happens in detention."
                    MB "Like writing lines?"
                    R "Yeah, but how do we make writing lines sexy?..."
                    R "Oh, wait!... I have an idea."
                    R "What if Professor McGargleCum uses magic to tie Hermione's hands behing her back, and then makes her put the chalk in her mouth to write lines?"
                    R "Then she has to bend over to do it."
                    MB "Better yet, she has to use her wand to write lines. You know, to make it more magic themed."
                    R "Yeah, I could make that work with some 3d stuff and Photochop!"
                    scene bg HPCosplay59
                    with fade
                    M "Well, at least no more clothes are coming off, and I guess it's not any worse than the last thing you just made us do."
                    M "So, if Megan's up for it..."
                    MG "I'm up for anything."
                    MT "{i}I'm starting to realize just how open and free Megan is with her sexuality.{/i}"
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    MB "Alright, let's set the scene."
                    MB "[ryan], would you mind tying Megan's wrists?"
                    R "I'm on it."
                    RT "{i}Tying up one of the hottest girls in the school, how could I say no?{/i}"
                    MB "And now Miss [mom_name], could you please point your wand at the knots to make it look like you tied them with magic?"
                else:
                    R "Since this shoot is detention themed, we need to have Professor McGargleCum force her to do something that usually happens in detention."
                    R "Like writing lines or something."
                    R "But, how do we make writing lines sexy?..."
                    R "Oh, wait!... I have an idea."
                    R "What if Professor McGargleCum uses magic to tie Hermione's hands behing her back, and then makes her put the chalk in her mouth to write lines?"
                    R "Then she has to bend over to do it."
                    R "Better yet, she has to use her wand to write lines. You know, to make it more magic themed."
                    R "Yeah, I could make that work with some 3d stuff and Photochop!"
                    scene bg HPCosplay59
                    with fade
                    M "Well, at least no more clothes are coming off, and I guess it's not any worse than the last thing you just made us do."
                    M "So, if Megan's up for it..."
                    MG "I'm up for anything."
                    MT "{i}I'm starting to realize just how open and free Megan is with her sexuality.{/i}"
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    R "Alright, let's set the scene."
                    R "I'll tie Megan's wrists."
                    RT "{i}Tying up one of the hottest girls in the school, how could I resist?{/i}"
                    R "Then Mom, could you point your wand at the knots to make it look like you tied them with magic?"
                jump megan_tied
            else:
                if blackmailed_mom_matt:
                    R "Since this shoot is detention themed, we need to have Professor McGargleCum force her to do something that usually happens in detention."
                    MB "Like writing lines?"
                    R "Yeah, but how do we make writing lines sexy?..."
                    R "Oh, wait!... I have an idea."
                    R "What if Professor McGargleCum uses magic to tie Hermione's hands behing her back, and then makes her put the chalk in her mouth to write lines?"
                    R "Then she has to bend over to do it."
                    MB "Better yet, she has to use her wand to write lines. You know, to make it more magic themed."
                    R "Yeah, I could make that work with some 3d stuff and Photochop!"
                else:
                    R "Since this shoot is detention themed, we need to have Professor McGargleCum force her to do something that usually happens in detention."
                    R "Like writing lines or something."
                    R "But, how do we make writing lines sexy?..."
                    R "Oh, wait!... I have an idea."
                    R "What if Professor McGargleCum uses magic to tie Hermione's hands behing her back, and then makes her put the chalk in her mouth to write lines?"
                    R "Then she has to bend over to do it."
                    R "Better yet, she has to use her wand to write lines. You know, to make it more magic themed."
                    R "Yeah, I could make that work with some 3d stuff and Photochop!"
                scene bg HPCosplay57
                with dissolve
                M "Now hold on just a second!"
                M "I'm not ok with this!"
                R "Why? Neither of you have to remove any more clothing."
                M "I can't participate in any violence against women!"
                M "It sends a dangerous message!"
                R "For one thing, it's not real, and anyone looking at the pics will know that, and for another thing, it's woman on woman violence, so... doesn't seem as bad."
                scene bg HPCosplay59
                with dissolve
                M "Hmmm... maybe it isn't as bad as man on woman violence..."
                scene bg HPCosplay56
                with dissolve
                M "But I'm still not comfortable with this."
                M "Especially to appear to be tying up my own student!"
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +1\"{/i}"
                $ momanger += 1
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to tie Megan's arms, you need her submission or libidio points at 10."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Have Mom expose her breasts and gag Megan. {i}(submission 14+){/i}":
            if momsubmission >= 14:
                if blackmailed_mom_matt:
                    R "I'm thinking that if Professor McGargleCum is being such a dom, that Hermione is going to try to fight back a bit."
                    R "At least get mad and try to yell at her."
                    MB "And Professor McGargleCum won't be able to allow any kind of defiance."
                    R "Exactly... So using her magic, she'll magic a ball gag into Hermione's mouth..."
                    R "And then we'll finish the scene with a pic of Professor McGargleCum sitting with her breasts out, triumphant over Hermione."
                    MB "Wow! That sounds awesome!"
                    MB "Do you have a ball gag?"
                    R "I do just so happen to have a ball gag."
                    MB "Yes! Let's set this up!"
                    scene bg HPCosplay56
                    with fade
                    M "Wait just a second!... Now you want me to expose my breasts?"
                    R "Well, you had to know this was coming."
                    scene bg HPCosplay57
                    with dissolve
                    M "Well... That may be... but it still doesn't mean I'm actually ready for it."
                    M "And what about the whole issue with violence against women?"
                    M "It sends a dangerous message!"
                    R "For one thing, it's not real, and anyone looking at the pics will know that, and for another thing, it's woman on woman violence, so... doesn't seem as bad."
                    scene bg HPCosplay59
                    with dissolve
                    M "Hmmm... maybe it isn't as bad as man on woman violence..."
                    R "Right, {i}(whispering){/i} And, it's not like you haven't shown off your breasts before?"
                    scene bg HPCosplay57
                    with dissolve
                    M "{i}(whispering){/i} Ix-nay on the ipping-stray!"
                    R "{i}(whispering){/i} I won't say a word if you'll do this."
                    MB "{i}(whispering){/i} What are you two whispering about?"
                    scene bg HPCosplay59
                    with dissolve
                    M "Fine! I'll do it!"
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    MB "Awesome! Let's set up the scene."
                    MB "Megan, take a stance and make a face like you're yelling at Miss [mom_name]."
                    MB "Miss [mom_name], just stand there like you're patiently waiting for her to finish."
                else:
                    R "I'm thinking that if Professor McGargleCum is being such a dom, that Hermione is going to try to fight back a bit."
                    R "At least get mad and try to yell at her."
                    R "So, Professor McGargleCum won't be able to allow any kind of defiance."
                    R "And using her magic, she'll magic a ball gag into Hermione's mouth..."
                    R "And then we'll finish the scene with a pic of Professor McGargleCum sitting with her breasts out, triumphant over Hermione."
                    MG "Wow! That sounds awesome!"
                    MG "Do you have a ball gag?"
                    R "I do just so happen to have a ball gag."
                    MG "Yes! Let's set this up!"
                    scene bg HPCosplay56
                    with fade
                    M "Wait just a second!... Now you want me to expose my breasts?"
                    R "Well, you had to know this was coming."
                    scene bg HPCosplay57
                    with dissolve
                    M "Well... That may be... but it still doesn't mean I'm actually ready for it."
                    M "And what about the whole issue with violence against women?"
                    M "It sends a dangerous message!"
                    R "For one thing, it's not real, and anyone looking at the pics will know that, and for another thing, it's woman on woman violence, so... doesn't seem as bad."
                    scene bg HPCosplay59
                    with dissolve
                    M "Hmmm... maybe it isn't as bad as man on woman violence..."
                    R "Right, {i}(whispering){/i} And, it's not like you haven't shown off your breasts before?"
                    scene bg HPCosplay57
                    with dissolve
                    M "{i}(whispering){/i} Ix-nay on the ipping-stray!"
                    R "{i}(whispering){/i} I won't say a word if you'll do this."
                    MG "{i}(whispering){/i} What are you two whispering about?"
                    scene bg HPCosplay59
                    with dissolve
                    M "Fine! I'll do it!"
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    MG "Awesome! Let's set up the scene."
                    R "Megan, take a stance and make a face like you're yelling at Miss [mom_name]."
                    R "Miss [mom_name], just stand there like you're patiently waiting for her to finish."
                jump ball_gagged
            else:
                if blackmailed_mom_matt:
                    R "I'm thinking that if Professor McGargleCum is being such a dom, that Hermione is going to try to fight back a bit."
                    R "At least get mad and try to yell at her."
                    MB "And Professor McGargleCum won't be able to allow any kind of defiance."
                    R "Exactly... So using her magic, she'll magic a ball gag into Hermione's mouth..."
                    R "And then we'll finish the scene with a pic of Professor McGargleCum sitting with her breasts out, triumphant over Hermione."
                    MB "Wow! That sounds awesome!"
                    MB "Do you have a ball gag?"
                    R "I do just so happen to have a ball gag."
                    MB "Yes! Let's set this up!"
                else:
                    R "I'm thinking that if Professor McGargleCum is being such a dom, that Hermione is going to try to fight back a bit."
                    R "At least get mad and try to yell at her."
                    R "So, Professor McGargleCum won't be able to allow any kind of defiance."
                    R "And using her magic, she'll magic a ball gag into Hermione's mouth..."
                    R "And then we'll finish the scene with a pic of Professor McGargleCum sitting with her breasts out, triumphant over Hermione."
                    MG "Wow! That sounds awesome!"
                    MG "Do you have a ball gag?"
                    R "I do just so happen to have a ball gag."
                    MG "Yes! Let's set this up!"
                scene bg HPCosplay56
                with fade
                M "Wait just a second!... Now you want me to expose my breasts?"
                R "Well, you had to know this was coming."
                scene bg HPCosplay57
                with dissolve
                M "Well... That may be... but it still doesn't mean I'm actually ready for it."
                M "And what about the whole issue with violence against women?"
                M "It sends a dangerous message!"
                R "For one thing, it's not real, and anyone looking at the pics will know that, and for another thing, it's woman on woman violence, so... doesn't seem as bad."
                scene bg HPCosplay59
                with dissolve
                M "Hmmm... maybe it isn't as bad as man on woman violence..."
                R "Right, {i}(whispering){/i} And, it's not like you haven't shown off your breasts before?"
                scene bg HPCosplay57
                with dissolve
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +1\"{/i}"
                $ momanger += 1
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to expose her breasts and gag Megan, you need her submission points at 14."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Have Mom remove Megan's panties and spank her. {i}(submission 19+){/i}":
            if momsubmission >= 19:
                if blackmailed_mom_matt:
                    R "So, here's what I'm thinking."
                    R "Professor McGargleCum needs to further dominate Hermione by showing how much bigger her naked breasts are."
                    R "Then she needs to bend her over her desk, remove her panties, and spank her with her wand."
                    MB "Oh, yeah... Total power move!"
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa!"
                    M "Did you just say I need to bare my breasts?"
                    M "Take off Megan's panties?"
                    M "And then spank her with my wand?"
                    R "Yep, in exactly that order."
                    scene bg HPCosplay57
                    with dissolve
                    M "Why did you think I'd be willing to expose my breasts in a photo shoot?"
                    R "Well, you had to know this was coming."
                    scene bg HPCosplay57
                    with dissolve
                    M "Well... That may be... but it still doesn't mean I'm actually ready for it."
                    M "And what about the whole issue with violence against women?"
                    M "It sends a dangerous message!"
                    R "For one thing, it's not real, and anyone looking at the pics will know that, and for another thing, it's woman on woman violence, so... doesn't seem as bad."
                    scene bg HPCosplay59
                    with dissolve
                    M "Hmmm... maybe it isn't as bad as man on woman violence..."
                    R "Right, {i}(whispering){/i} And, it's not like you haven't shown off your breasts before?"
                    scene bg HPCosplay57
                    with dissolve
                    M "{i}(whispering){/i} Ix-nay on the ipping-stray!"
                    R "{i}(whispering){/i} I won't say a word if you'll do this."
                    MB "{i}(whispering){/i} What are you two whispering about?"
                    scene bg HPCosplay59
                    with dissolve
                    M "Fine! I'll do it!"
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    MB "Awesome! Let's set up the scene."
                    MB "Wait... Is there a reason she's being punished?"
                    R "Hmmm... Yeah... because she has such a dirty mouth.  First, Professor McGargleCum puts a ball gag in it..."
                    MB "Do you have a ball gag?"
                else:
                    R "So, here's what I'm thinking."
                    R "Professor McGargleCum needs to further dominate Hermione by showing how much bigger her naked breasts are."
                    R "Then she needs to bend her over her desk, remove her panties, and spank her with her wand."
                    MG "Oh, yeah... Total power move!"
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa!"
                    M "Did you just say I need to bare my breasts?"
                    M "Take off Megan's panties?"
                    M "And then spank her with my wand?"
                    R "Yep, in exactly that order."
                    scene bg HPCosplay57
                    with dissolve
                    M "Why did you think I'd be willing to expose my breasts in a photo shoot?"
                    R "Well, you had to know this was coming."
                    scene bg HPCosplay57
                    with dissolve
                    M "Well... That may be... but it still doesn't mean I'm actually ready for it."
                    M "And what about the whole issue with violence against women?"
                    M "It sends a dangerous message!"
                    R "For one thing, it's not real, and anyone looking at the pics will know that, and for another thing, it's woman on woman violence, so... doesn't seem as bad."
                    scene bg HPCosplay59
                    with dissolve
                    M "Hmmm... maybe it isn't as bad as man on woman violence..."
                    R "Right, {i}(whispering){/i} And, it's not like you haven't shown off your breasts before?"
                    scene bg HPCosplay57
                    with dissolve
                    M "{i}(whispering){/i} Ix-nay on the ipping-stray!"
                    R "{i}(whispering){/i} I won't say a word if you'll do this."
                    MG "{i}(whispering){/i} What are you two whispering about?"
                    scene bg HPCosplay59
                    with dissolve
                    M "Fine! I'll do it!"
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    MG "Awesome! Let's set up the scene."
                    MG "Wait... Is there a reason she's being punished?"
                    R "Hmmm... Yeah... because she has such a dirty mouth.  First, Professor McGargleCum puts a ball gag in it..."
                    MB "Do you have a ball gag?"
                R "I just so happen to have one."
                M "Oh, my God!"
                R "Then, she bends her over the desk."
                R "And that's where we should start shooting the scene."
                jump megan_spanked
            else:
                if blackmailed_mom_matt:
                    R "So, here's what I'm thinking."
                    R "Professor McGargleCum needs to further dominate Hermione by showing how much bigger her naked breasts are."
                    R "Then she needs to bend her over her desk, remove her panties, and spank her with her wand."
                    MB "Oh, yeah... Total power move!"
                else:
                    R "So, here's what I'm thinking."
                    R "Professor McGargleCum needs to further dominate Hermione by showing how much bigger her naked breasts are."
                    R "Then she needs to bend her over her desk, remove her panties, and spank her with her wand."
                    MG "Oh, yeah... Total power move!"
                scene bg HPCosplay56
                with fade
                M "Whoa, whoa, whoa!"
                M "Did you just say I need to bare my breasts?"
                M "Take off Megan's panties?"
                M "And then spank her with my wand?"
                R "Yep, in exactly that order."
                scene bg HPCosplay57
                with dissolve
                M "Why did you think I'd be willing to expose my breasts in a photo shoot?"
                R "Well, you had to know this was coming."
                scene bg HPCosplay57
                with dissolve
                M "Well... That may be... but it still doesn't mean I'm actually ready for it."
                M "And what about the whole issue with violence against women?"
                M "It sends a dangerous message!"
                R "For one thing, it's not real, and anyone looking at the pics will know that, and for another thing, it's woman on woman violence, so... doesn't seem as bad."
                scene bg HPCosplay59
                with dissolve
                M "Hmmm... maybe it isn't as bad as man on woman violence..."
                R "Right, {i}(whispering){/i} And, it's not like you haven't shown off your breasts before?"
                scene bg HPCosplay57
                with dissolve
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +1\"{/i}"
                $ momanger += 1
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to spank Megan, you need her submission points at 19."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Have Mom remove her panties and pose with Megan. {i}(submission 25+){/i}":
            if momsubmission >= 25:
                if blackmailed_mom_matt:
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    MB "Huh?... I kind of thought we'd build up to that."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    MB "Alright, you heard him, ladies."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Removing both our tops and bottoms?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think I'm going to do full nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "I'm only asking you to do what every other photographer asks their models to do."
                    M "But I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Removing both our tops and bottoms?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think I'm going to do full nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "I'm only asking you to do what every other photographer asks their models to do."
                    M "But I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                scene bg HPCosplay59
                with dissolve
                M "Yeah, I know..."
                MT "{i}I can't expose my career, let alone [ryan]'s reputation if Matt were to get us investigated.{/i}"
                M "I don't like this at all, but let's do the scene."
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                    $ momsubmission += 1
                if finished_hp_shoot == False and weekly_hp_complete == False:
                    $ photoshoot_kinky += 1
                R "How about a pose where Megan is on all fours with her skirt up so we can see that she's not wearing any panties, and Mom will be dominating her by sitting on her."
                R "Oh... and just to make it even more hot, Megan will be wearing this ball gag."
                M "Where'd you get a ball gag?"
                R "That's not important, let's take some pics!"
                jump no_panties_shot
            else:
                if blackmailed_mom_matt:
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    MB "Huh?... I kind of thought we'd build up to that."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    MB "Alright, you heard him, ladies."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Removing both our tops and bottoms?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think I'm going to do full nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "I'm only asking you to do what every other photographer asks their models to do."
                    M "But I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Removing both our tops and bottoms?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think I'm going to do full nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "I'm only asking you to do what every other photographer asks their models to do."
                    M "But I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +5\"{/i}"
                $ momanger += 5
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to pose fully naked with Megan, you need her submission points at 25."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Maybe we should end the shoot for today.":
            if blackmailed_mom_matt:
                scene bg HPCosplay56
                with fade
                R "I don't think we need to take any more pics today."
                MB "Really? We haven't taken very many."
                R "Yeah, but the ones we have are really good, and the only way they could be better is if we pushed the girls into something they might not be comfortable with."
                scene bg HPCosplay58
                with dissolve
                M "Oh, [ryan]! You really do act like a professional photographer."
                M "And that wasn't nearly as bad as I thought it would be!"
                M "And even though I'm being coerced into this, you both helped me feel pretty comfortable!"
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Mom's Libido +5\"{/b}{/i}"
                    $ momaffection += 1
                    $ momlibido += 5
                M "The next photo shoot might not make me feel so uneasy now."
                M "I might be even more daring, and be willing to show a little more skin... maybe..."
                MB "Great! I can't wait!"
                RT "{i}Ugghh... I wish Matt wasn't going to be there.{/i}"
            else:
                scene bg HPCosplay56
                with fade
                R "I don't think we need to take any more pics today."
                MG "Really? We haven't taken very many."
                R "Yeah, but the ones we have are really good, and the only way they could be better is if we pushed the girls into something they might not be comfortable with."
                scene bg HPCosplay58
                with dissolve
                M "Oh, [ryan]! You really do act like a professional photographer."
                M "And that wasn't nearly as bad as I thought it would be!"
                M "And even though I'm being coerced into this, you both helped me feel pretty comfortable!"
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Mom's Libido +5\"{/b}{/i}"
                    $ momaffection += 1
                    $ momlibido += 5
                M "The next photo shoot might not make me feel so uneasy now."
                M "I might be even more daring, and be willing to show a little more skin... maybe..."
                MG "Great! I can't wait!"
                RT "{i}Neither can I... I just need to be careful about pushing Mom too hard, and too fast... That's what she said.{/i}"
            R "You can get changed and I'll see you back home."
            hide screen Points_screen_Mom_cosplay
            jump posting_the_wr_pics

label megan_tied:                       #### Edited ####
    if blackmailed_mom_matt:
        scene bg SleepBlack
        with fade
        scene bg HPCosplay61
        with fade
        MB "Alright, I've just about got the camera ready... and..."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay61
        MB "Got it!"
        MB "Now, I need Miss [mom_name] to put the wand in Megan's mouth..."
        MB "Then Megan, you bend over like you're shooting magic out of your wand and onto our imaginary chalkboard."
        MB "And Miss [mom_name], why don't you look down like you're staring at her ass."
        scene bg HPCosplay62
        with fade
        MG "Hrowrs hriss?"
        R "What?"
        M "I think she said, \"How's this?\""
        MG "Mrmm Hrmm..."
        MB "It looks sexy as hell."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay62
        MB "Now let me come around here a little bit, and Miss [mom_name], why don't you flip up Megan's skirt?"
        MT "{i}Well, it's not like they haven't gotten pictures of her panties already.{/i}"
        M "Alright..."
        scene bg HPCosplay63
        with fade
        MB "And Megan, look back at her like you're surprised."
        MB "And... Nice!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay63
        MB "Got it."
        scene bg SleepBlack
        with fade
        scene bg HPCosplay102
        with fade
        MB "These pics are gonna turn out awesome!"
        MB "Let's see though, where should we go from here, [ryan]?"
    else:
        scene bg SleepBlack
        with fade
        scene bg HPCosplay61
        with fade
        R "Alright, I've just about got the camera ready... and..."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay61
        R "Got it!"
        R "Now, I need Mom to put the wand in Megan's mouth..."
        R "Then Megan, you bend over like you're shooting magic out of your wand and onto our imaginary chalkboard."
        R "And Mom, why don't you look down like you're staring at her ass."
        scene bg HPCosplay62
        with fade
        MG "Hrowrs hriss?"
        R "What?"
        M "I think she said, \"How's this?\""
        MG "Mrmm Hrmm..."
        R "It looks sexy as hell."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay62
        R "Now let me come around here a little bit, and Mom, why don't you flip up Megan's skirt?"
        MT "{i}Well, it's not like he hasn't gotten pictures of her panties already.{/i}"
        M "Alright..."
        scene bg HPCosplay63
        with fade
        R "And Megan, look back at her like you're surprised."
        R "And... Nice!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay63
        R "Got it."
        scene bg SleepBlack
        with fade
        scene bg HPCosplay102
        with fade
        R "These pics are gonna turn out awesome!"
        R "Let's see though, where should we go from here?"
    R "Let me think."
    menu:
        "Megan needs a gag in her mouth. {i}(submission 14+){/i}":
            if momsubmission >= 14:
                if blackmailed_mom_matt:
                    R "I'm thinking that if Professor McGargleCum is being such a dom, that Hermione is going to try to fight back a bit."
                    R "She'll be really mad that McGargleCum flipped up her skirt, so she's going to really yell back at her."
                    MB "And Professor McGargleCum won't be able to allow any kind of defiance."
                    R "Exactly... So using her magic, she'll magic a ball gag into Hermione's mouth..."
                    R "And then we'll finish the scene with a pic of Professor McGargleCum sitting with her breasts out, triumphant over Hermione."
                    MB "Wow! That sounds awesome!"
                    MB "Do you have a ball gag?"
                    R "I do just so happen to have a ball gag."
                    MB "Yes! Let's set this up!"
                    scene bg HPCosplay56
                    with fade
                    M "Wait just a second!... Now you want me to expose my breasts?"
                    R "Well, you had to know this was coming."
                    scene bg HPCosplay57
                    with dissolve
                    M "Well... That may be... but it still doesn't mean I'm actually ready for it."
                    M "And what about the whole issue with violence against women?"
                    M "It sends a dangerous message!"
                    R "For one thing, it's not real, and anyone looking at the pics will know that, and for another thing, it's woman on woman violence, so... doesn't seem as bad."
                    scene bg HPCosplay59
                    with dissolve
                    M "Hmmm... maybe it isn't as bad as man on woman violence..."
                    R "Right, {i}(whispering){/i} And, it's not like you haven't shown off your breasts before?"
                    scene bg HPCosplay57
                    with dissolve
                    M "{i}(whispering){/i} Ix-nay on the ipping-stray!"
                    R "{i}(whispering){/i} I won't say a word if you'll do this."
                    MB "{i}(whispering){/i} What are you two whispering about?"
                    scene bg HPCosplay59
                    with dissolve
                    M "Fine! I'll do it!"
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    MB "Awesome! Let's set up the scene."
                    MB "Megan, take a stance and make a face like you're yelling at Miss [mom_name]."
                    MB "Miss [mom_name], just stand there like you're patiently waiting for her to finish."
                else:
                    R "I'm thinking that if Professor McGargleCum is being such a dom, that Hermione is going to try to fight back a bit."
                    R "At least get mad and try to yell at her."
                    R "So, Professor McGargleCum won't be able to allow any kind of defiance."
                    R "And using her magic, she'll magic a ball gag into Hermione's mouth..."
                    R "And then we'll finish the scene with a pic of Professor McGargleCum sitting with her breasts out, triumphant over Hermione."
                    MG "Wow! That sounds awesome!"
                    MG "Do you have a ball gag?"
                    R "I do just so happen to have a ball gag."
                    MG "Yes! Let's set this up!"
                    scene bg HPCosplay56
                    with fade
                    M "Wait just a second!... Now you want me to expose my breasts?"
                    R "Well, you had to know this was coming."
                    scene bg HPCosplay57
                    with dissolve
                    M "Well... That may be... but it still doesn't mean I'm actually ready for it."
                    M "And what about the whole issue with violence against women?"
                    M "It sends a dangerous message!"
                    R "For one thing, it's not real, and anyone looking at the pics will know that, and for another thing, it's woman on woman violence, so... doesn't seem as bad."
                    scene bg HPCosplay59
                    with dissolve
                    M "Hmmm... maybe it isn't as bad as man on woman violence..."
                    R "Right, {i}(whispering){/i} And, it's not like you haven't shown off your breasts before?"
                    scene bg HPCosplay57
                    with dissolve
                    M "{i}(whispering){/i} Ix-nay on the ipping-stray!"
                    R "{i}(whispering){/i} I won't say a word if you'll do this."
                    MG "{i}(whispering){/i} What are you two whispering about?"
                    scene bg HPCosplay59
                    with dissolve
                    M "Fine! I'll do it!"
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    MG "Awesome! Let's set up the scene."
                    R "Megan, take a stance and make a face like you're yelling at Miss [mom_name]."
                    R "Miss [mom_name], just stand there like you're patiently waiting for her to finish."
                jump ball_gagged
            else:
                if blackmailed_mom_matt:
                    R "I'm thinking that if Professor McGargleCum is being such a dom, that Hermione is going to try to fight back a bit."
                    R "At least get mad and try to yell at her."
                    MB "And Professor McGargleCum won't be able to allow any kind of defiance."
                    R "Exactly... So using her magic, she'll magic a ball gag into Hermione's mouth..."
                    R "And then we'll finish the scene with a pic of Professor McGargleCum sitting with her breasts out, triumphant over Hermione."
                    MB "Wow! That sounds awesome!"
                    MB "Do you have a ball gag?"
                    R "I do just so happen to have a ball gag."
                    MB "Yes! Let's set this up!"
                else:
                    R "I'm thinking that if Professor McGargleCum is being such a dom, that Hermione is going to try to fight back a bit."
                    R "At least get mad and try to yell at her."
                    R "So, Professor McGargleCum won't be able to allow any kind of defiance."
                    R "And using her magic, she'll magic a ball gag into Hermione's mouth..."
                    R "And then we'll finish the scene with a pic of Professor McGargleCum sitting with her breasts out, triumphant over Hermione."
                    MG "Wow! That sounds awesome!"
                    MG "Do you have a ball gag?"
                    R "I do just so happen to have a ball gag."
                    MG "Yes! Let's set this up!"
                scene bg HPCosplay56
                with fade
                M "Wait just a second!... Now you want me to expose my breasts?"
                R "Well, you had to know this was coming."
                scene bg HPCosplay57
                with dissolve
                M "Well... That may be... but it still doesn't mean I'm actually ready for it."
                M "And what about the whole issue with violence against women?"
                M "It sends a dangerous message!"
                R "For one thing, it's not real, and anyone looking at the pics will know that, and for another thing, it's woman on woman violence, so... doesn't seem as bad."
                scene bg HPCosplay59
                with dissolve
                M "Hmmm... maybe it isn't as bad as man on woman violence..."
                R "Right, {i}(whispering){/i} And, it's not like you haven't shown off your breasts before?"
                scene bg HPCosplay57
                with dissolve
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +1\"{/i}"
                $ momanger += 1
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to expose her breasts and gag Megan, you need her submission points at 14."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Megan needs her bare ass spanked. {i}(submission 19+){/i}":
            if momsubmission >= 19:
                if blackmailed_mom_matt:
                    R "So, here's what I'm thinking."
                    R "Professor McGargleCum needs to further dominate Hermione by showing how much bigger her naked breasts are."
                    R "Then she needs to bend her over her desk, remove her panties, and spank her with her wand."
                    MB "Oh, yeah... Total power move!"
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa!"
                    M "Did you just say I need to bare my breasts?"
                    M "Take off Megan's panties?"
                    M "And then spank her with my wand?"
                    R "Yep, in exactly that order."
                    scene bg HPCosplay57
                    with dissolve
                    M "Why did you think I'd be willing to expose my breasts in a photo shoot?"
                    R "Well, you had to know this was coming."
                    scene bg HPCosplay57
                    with dissolve
                    M "Well... That may be... but it still doesn't mean I'm actually ready for it."
                    M "And what about the whole issue with violence against women?"
                    M "It sends a dangerous message!"
                    R "For one thing, it's not real, and anyone looking at the pics will know that, and for another thing, it's woman on woman violence, so... doesn't seem as bad."
                    scene bg HPCosplay59
                    with dissolve
                    M "Hmmm... maybe it isn't as bad as man on woman violence..."
                    R "Right, {i}(whispering){/i} And, it's not like you haven't shown off your breasts before?"
                    scene bg HPCosplay57
                    with dissolve
                    M "{i}(whispering){/i} Ix-nay on the ipping-stray!"
                    R "{i}(whispering){/i} I won't say a word if you'll do this."
                    MB "{i}(whispering){/i} What are you two whispering about?"
                    scene bg HPCosplay59
                    with dissolve
                    M "Fine! I'll do it!"
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    MB "Awesome! Let's set up the scene."
                    MB "Wait... Is there a reason she's being punished?"
                    R "Hmmm... Yeah... because she has such a dirty mouth.  First, Professor McGargleCum puts a ball gag in it..."
                    MB "Do you have a ball gag?"
                else:
                    R "So, here's what I'm thinking."
                    R "Professor McGargleCum needs to further dominate Hermione by showing how much bigger her naked breasts are."
                    R "Then she needs to bend her over her desk, remove her panties, and spank her with her wand."
                    MG "Oh, yeah... Total power move!"
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa!"
                    M "Did you just say I need to bare my breasts?"
                    M "Take off Megan's panties?"
                    M "And then spank her with my wand?"
                    R "Yep, in exactly that order."
                    scene bg HPCosplay57
                    with dissolve
                    M "Why did you think I'd be willing to expose my breasts in a photo shoot?"
                    R "Well, you had to know this was coming."
                    scene bg HPCosplay57
                    with dissolve
                    M "Well... That may be... but it still doesn't mean I'm actually ready for it."
                    M "And what about the whole issue with violence against women?"
                    M "It sends a dangerous message!"
                    R "For one thing, it's not real, and anyone looking at the pics will know that, and for another thing, it's woman on woman violence, so... doesn't seem as bad."
                    scene bg HPCosplay59
                    with dissolve
                    M "Hmmm... maybe it isn't as bad as man on woman violence..."
                    R "Right, {i}(whispering){/i} And, it's not like you haven't shown off your breasts before?"
                    scene bg HPCosplay57
                    with dissolve
                    M "{i}(whispering){/i} Ix-nay on the ipping-stray!"
                    R "{i}(whispering){/i} I won't say a word if you'll do this."
                    MG "{i}(whispering){/i} What are you two whispering about?"
                    scene bg HPCosplay59
                    with dissolve
                    M "Fine! I'll do it!"
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    MG "Awesome! Let's set up the scene."
                    MG "Wait... Is there a reason she's being punished?"
                    R "Hmmm... Yeah... because she has such a dirty mouth.  First, Professor McGargleCum puts a ball gag in it..."
                    MB "Do you have a ball gag?"
                R "I just so happen to have one."
                M "Oh, my God!"
                R "Then, she bends her over the desk."
                R "And that's where we should start shooting the scene."
                jump megan_spanked
            else:
                if blackmailed_mom_matt:
                    R "So, here's what I'm thinking."
                    R "Professor McGargleCum needs to further dominate Hermione by showing how much bigger her naked breasts are."
                    R "Then she needs to bend her over her desk, remove her panties, and spank her with her wand."
                    MB "Oh, yeah... Total power move!"
                else:
                    R "So, here's what I'm thinking."
                    R "Professor McGargleCum needs to further dominate Hermione by showing how much bigger her naked breasts are."
                    R "Then she needs to bend her over her desk, remove her panties, and spank her with her wand."
                    MG "Oh, yeah... Total power move!"
                scene bg HPCosplay56
                with fade
                M "Whoa, whoa, whoa!"
                M "Did you just say I need to bare my breasts?"
                M "Take off Megan's panties?"
                M "And then spank her with my wand?"
                R "Yep, in exactly that order."
                scene bg HPCosplay57
                with dissolve
                M "Why did you think I'd be willing to expose my breasts in a photo shoot?"
                R "Well, you had to know this was coming."
                scene bg HPCosplay57
                with dissolve
                M "Well... That may be... but it still doesn't mean I'm actually ready for it."
                M "And what about the whole issue with violence against women?"
                M "It sends a dangerous message!"
                R "For one thing, it's not real, and anyone looking at the pics will know that, and for another thing, it's woman on woman violence, so... doesn't seem as bad."
                scene bg HPCosplay59
                with dissolve
                M "Hmmm... maybe it isn't as bad as man on woman violence..."
                R "Right, {i}(whispering){/i} And, it's not like you haven't shown off your breasts before?"
                scene bg HPCosplay57
                with dissolve
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +1\"{/i}"
                $ momanger += 1
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to spank Megan, you need her submission points at 19."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "We need a really good full nudity pose. {i}(submission 25+){/i}":
            if momsubmission >= 25:
                if blackmailed_mom_matt:
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    MB "Huh?... I kind of thought we'd build up to that."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    MB "Alright, you heard him, ladies."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Removing both our tops and bottoms?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think I'm going to do full nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "I'm only asking you to do what every other photographer asks their models to do."
                    M "But I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Removing both our tops and bottoms?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think I'm going to do full nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "I'm only asking you to do what every other photographer asks their models to do."
                    M "But I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                scene bg HPCosplay59
                with dissolve
                M "Yeah, I know..."
                MT "{i}I can't expose my career, let alone [ryan]'s reputation if Matt were to get us investigated.{/i}"
                M "I don't like this at all, but let's do the scene."
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                    $ momsubmission += 1
                if finished_hp_shoot == False and weekly_hp_complete == False:
                    $ photoshoot_kinky += 1
                R "How about a pose where Megan is on all fours with her skirt up so we can see that she's not wearing any panties, and Mom will be dominating her by sitting on her."
                R "Oh... and just to make it even more hot, Megan will be wearing this ball gag."
                M "Where'd you get a ball gag?"
                R "That's not important, let's take some pics!"
                jump no_panties_shot
            else:
                if blackmailed_mom_matt:
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    MB "Huh?... I kind of thought we'd build up to that."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    MB "Alright, you heard him, ladies."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Removing both our tops and bottoms?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think I'm going to do full nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MB "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "I'm only asking you to do what every other photographer asks their models to do."
                    M "But I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                    MB "I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                else:
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    scene bg HPCosplay56
                    with fade
                    M "Whoa, whoa, whoa, hold up."
                    M "Removing both our tops and bottoms?"
                    if first_megan_breast_reveal:
                        scene bg HPCosplay57
                        with fade
                        M "Are you fucking crazy? You think I'm going to do full nudity?"
                        MG "I'm ok with it."
                        M "You, be quiet."
                        R "Oh, come on, Mom... You wanted to be a model when you were younger..."
                        R "You had to know that a model doesn't make it very far without doing some nudity."
                        R "I mean, look at the profession you chose to prepare yourself for modeling."
                        MG "What profession is that?"
                        M "None of your business!"
                        $ first_megan_breast_reveal = True
                    else:
                        R "Yeah Mom, just like last time."
                        scene bg HPCosplay57
                        with fade
                        M "I still can't believe you're asking me to do this."
                    R "I'm only asking you to do what every other photographer asks their models to do."
                    M "But I don't think I can do that with one of my students!"
                    MG "I really want to finish this photo shoot, Miss [mom_name]... I need this to boost my online fame!"
                MG "So, I hate to play this card, but you know what happens if you don't finish the photo shoot?"
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son and students can be so comfortable with such perversion."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +5\"{/i}"
                $ momanger += 5
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to pose fully naked with Megan, you need her submission points at 25."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Maybe we should end the shoot for today.":
            if blackmailed_mom_matt:
                scene bg HPCosplay56
                with fade
                R "I don't think we need to take any more pics today."
                MB "Really? We haven't taken very many."
                R "Yeah, but the ones we have are really good, and the only way they could be better is if we pushed the girls into something they might not be comfortable with."
                scene bg HPCosplay58
                with dissolve
                M "Oh, [ryan]! You really do act like a professional photographer."
                M "And that wasn't nearly as bad as I thought it would be!"
                M "And even though I'm being coerced into this, you both helped me feel pretty comfortable!"
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Mom's Libido +5\"{/b}{/i}"
                    $ momaffection += 1
                    $ momlibido += 5
                M "The next photo shoot might not make me feel so uneasy now."
                M "I might be even more daring, and be willing to show a little more skin... maybe..."
                MB "Great! I can't wait!"
                RT "{i}Ugghh... I wish Matt wasn't going to be there.{/i}"
            else:
                scene bg HPCosplay56
                with fade
                R "I don't think we need to take any more pics today."
                MG "Really? We haven't taken very many."
                R "Yeah, but the ones we have are really good, and the only way they could be better is if we pushed the girls into something they might not be comfortable with."
                scene bg HPCosplay58
                with dissolve
                M "Oh, [ryan]! You really do act like a professional photographer."
                M "And that wasn't nearly as bad as I thought it would be!"
                M "And even though I'm being coerced into this, you both helped me feel pretty comfortable!"
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Mom's Libido +5\"{/b}{/i}"
                    $ momaffection += 1
                    $ momlibido += 5
                M "The next photo shoot might not make me feel so uneasy now."
                M "I might be even more daring, and be willing to show a little more skin... maybe..."
                MG "Great! I can't wait!"
                RT "{i}Neither can I... I just need to be careful about pushing Mom too hard, and too fast... That's what she said.{/i}"
            R "You can get changed and I'll see you back home."
            hide screen Points_screen_Mom_cosplay
            jump posting_the_wr_pics

label ball_gagged:                      #### Edited ####
    if blackmailed_mom_matt:
        scene bg HPCosplay64
        with fade
        MB "Really great yelling face, Megan."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay64
        MB "And now we need a picture of Miss [mom_name], pointing her wand at Megan's mouth."
        MB "And [ryan] can make it look like it's shooting magic into her mouth."
        scene bg HPCosplay65
        with fade
        MB "That just looks funny."
        R "Don't worry, it will look really cool once I get done with it."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay65
        MB "Ok, [ryan]... I need you to put the ball gag on Megan, and then Megan you'll try to look stunned because it just appeared in your mouth."
        R "All right, I've never put a ball gag on anybody, give me just a bit to figure this thing out."
        scene bg SleepBlack
        R "No, Megan, you've got to open wider... No, wider!... and this buckle goes right here... and..."
        scene bg HPCosplay66
        with fade
        RT "{i}Oh, God! I've never done any kind of kinky stuff like this before... it's really turning me on!{/i}"
        RT "{i}I'm as hard as a rock!{/i}"
        MT "{i}Oh, damn!... I didn't like that stupid \"37 Shades of Grey\" book, but this is actually kind of hot in real life.{/i}"
        MB "Wow!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay66
        MB "Now, Miss [mom_name]... it's time for you to pull down your dress, and go pose in that chair, with a triumphant look on your face."
        MT "{i}Oh, God! Can I really expose my breasts to my students?{/i}"
        MT "{i}Oh, my God! Did my [ryan] talk his sisters into showing their breasts!?... He wouldn't do that to his own sisters... Would he?{/i}"
        M "Is this part really necessary for the photo shoot to be successful?"
        R "Oh man! My studio's followers and subscribers wouldn't just be dissapointed, but they'd probably be pissed if you didn't show your breasts.  I'll bet I'd lose a lot of subscribers, and a lot of money."
        M "Ohhh... ok..."
        MT "{i}He probably did get the girls to show their breasts.{/i}"
        MT "{i}Knowing Lauren... She probably did it willingly... But how would he get Sidney to do that?{/i}"
        M "Alright, let me get into the pose first... Then I'll pull my dress down."
        MB "Alright, now Megan go sit at the foot of Miss [mom_name]'s chair... And do your best defeated look."
        scene bg SleepBlack
        with fade
        MB "Oh, that looks amazing!... But Miss [mom_name]... You still haven't pulled down your shirt?"
        MT "{i}Oh, sweet Jesus... This is so wrong!... it's so... hot?... Why does this feeling of embarrassment make me feel so turned on at the same time?{/i}"
        MT "{i}Ok... Just like at the club... I can do this!...{/i}"
        scene bg HPCosplay67
        with fade
        R "Wow! If there was a cover for this Perry Hotter movie, this pose would be it."
        MB "Great job... both of you!"
        MT "{i}Oh, my God! Matt's dick is about to rip out of his pants!{/i}"
        MT "{i}Look how hard he is!... and how big he is!{/i}"
        MT "{i}Amazing... he's even bigger than [ryan]!{/i}"
        MT "{i}I wish I could see it!{/i}"
        if not finished_hp_shoot:
            "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
            $ momlibido += 1
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay67
        MT "{i}Oh, fuck! What's wrong with me! I can't think of one of my students like that! He's too young! I'm married! Fucking shit, [mom_name]! Get control of your thoughts!{/i}"
        MB "I'm really pleased with how well this turned out."
        MB "Really good idea, [ryan]!"
        MB "So... Do you have any other good ideas?"
    else:
        scene bg HPCosplay64
        with fade
        R "Really great yelling face, Megan."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay64
        R "And now, we need a picture of Mom pointing her wand at Megan's mouth."
        R "And of course, I'll make it look like it's shooting magic into her mouth."
        scene bg HPCosplay65
        with fade
        MG "That just looks funny."
        R "Don't worry, it will look really cool once I get done with it."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay65
        R "Ok, I'll put the ball gag on Megan, and then Megan you'll try to look stunned because it just appeared in your mouth."
        R "All right, I've never put a ball gag on anybody, give me just a bit to figure this thing out."
        scene bg SleepBlack
        R "No, Megan, you've got to open wider... No, wider!... and this buckle goes right here... and..."
        scene bg HPCosplay66
        with fade
        play sound Muffled
        $ renpy.pause (2.0)
        stop sound
        RT "{i}Oh, God! I've never done any kind of kinky stuff like this before... it's really turning me on!{/i}"
        RT "{i}I'm as hard as a rock!{/i}"
        MT "{i}Oh, damn!... I didn't like that stupid \"37 Shades of Grey\" book, but this is actually kind of hot in real life.{/i}"
        R "Wow!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay66
        R "Now, Mom... it's time for you to pull down your dress, and go pose in that chair with a triumphant look on your face."
        MT "{i}Oh, God! Can I really expose my breasts to my students?{/i}"
        M "Is this part really necessary for the photo shoot to be successful?"
        R "Oh man! My studio's followers and subscribers wouldn't just be dissapointed, but they'd probably be pissed if you didn't show your breasts.  I'll bet I'd lose a lot of subscribers, and a lot of money."
        M "Ohhh... ok..."
        M "Alright, let me get into the pose first... Then I'll pull my dress down."
        R "Alright, now Megan, go sit at the foot of Miss [mom_name]'s chair... And do your best defeated look."
        scene bg SleepBlack
        with fade
        R "Oh, that looks amazing!... but Mom... you still haven't pulled down your shirt?"
        MT "{i}Oh, sweet Jesus... This is so wrong!... it's so... hot?... Why does this feeling of embarrassment make me feel so turned on at the same time?{/i}"
        MT "{i}Ok... Just like at the club... I can do this!...{/i}"
        scene bg HPCosplay67
        with fade
        R "Wow! If there was a cover for this Perry Hotter movie, this pose would be it."
        R "Great job... both of you!"
        MT "{i}Oh, my God! [ryan]'s dick is about to rip out of his pants!{/i}"
        MT "{i}Look how hard he is!... and how big he is!{/i}"
        MT "{i}I can still feel that dick in my hands!{/i}"
        MT "{i}And his cum on my face!{/i}"
        MT "{i}I wish I could see it right now!{/i}"
        if not finished_hp_shoot:
            "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
            $ momlibido += 1
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay67
        MT "{i}Oh, fuck! What's wrong with me! I can't think of my son like that! Fucking shit [mom_name]! Get control of your thoughts!{/i}"
        R "I'm really pleased with how well this turned out."
        R "So... Now I need an equally good idea."
    R "Hmmm... let's see..."
    menu:
        "Megan needs her bare ass spanked. {i}(submission 19+){/i}":
            if momsubmission >= 19:
                if blackmailed_mom_matt:
                    scene bg HPCosplay103
                    with fade
                    R "It would be a crime to do a whole school discipline shoot, and not have a spanking scene."
                    MB "Oh my God, you're right!... How did we forget a spanking scene?"
                    R "But we need to heat this photo shoot up... So... Megan's panties will need to come off."
                    scene bg HPCosplay56
                    with fade
                    M "Wait! This isn't just a topless photo shoot!?"
                    scene bg HPCosplay57
                    with fade
                    M "[ryan]!! Did you make Lauren and Sidney expose themselves completely in their photo shoots!?"
                    R "Absolutely not!..."
                    scene bg HPCosplay59
                    with fade
                    MT "{i}Oh... Thank God!{/i}"
                    R "... They did it willingly by themselves."
                    scene bg HPCosplay57
                    with dissolve
                    M "[ryan]!! I'm going to castrate you when we get home!"
                    R "Now hold on just a minute!"
                    scene bg HPCosplay56
                    with dissolve
                    MT "{i}Since when does [ryan] dare talk back to me?{/i}"
                    R "Lauren and Sidney are both adults!"
                    R "They are perfectly capable of making their own decisions."
                    R "I mean for God's sake! You were working in a strip club when you were Sidney's age!"
                    scene bg HPCosplay57
                    with dissolve
                    M "Damnit, [ryan]! I didn't want anybody else to know about that!"
                    MB "We won't say a word."
                    MB "Right Megan?"
                    play sound Muffled
                    $ renpy.pause (2.0)
                    stop sound
                    MG "Mrrmmmm..Hrmmm..."
                    R "Well, you say it like it's a bad thing... Why are you so ashamed of it?"
                    M "Because society says..."
                    R "Fuck society."
                    R "You had a dream... You needed to pay for it!"
                    R "Working at McDoogles wouldn't make enough to pay for your dream."
                    R "So you did what you needed to do."
                    R "Were the other strippers you worked with terrible people?"
                    scene bg HPCosplay56
                    with dissolve
                    M "No... Actually, I wish I was still friends with most of them."
                    R "Then stop worrying about what everyone else thinks, and let your daughters be empowered to make their own decisions... Just like you did at their age."
                    R "They wanted to do it to help with the weekly finances... To pay off the \"you know who\"."
                    MB "Who?"
                    M "Don't pry!... You already know too much about us."
                    M "But, they did that for me?"
                    R "Yes, and for all of us."
                    scene bg HPCosplay59
                    with dissolve
                    MT "{i}I really don't want to pose with Megan's bare ass... And I'm sure mine will be next... But I don't want Matt to go to the principal about what he saw in my office.{/i}"
                    MT "{i}So this is the least I can do for our family.{/i}"
                    scene bg HPCosplay58
                    with dissolve
                    MT "{i}[ryan] is a champion bullshitter!{/i}"
                    MT "{i}But I guess I can't argue with anything he just said.{/i}"
                    scene bg HPCosplay59
                    with dissolve
                    M "Fine! I'll do it."
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    MB "Wow! Good speech, [ryan]!"
                    MB "Alright, well let's set up the scene."
                    MB "Megan, bend over the table, or should I say desk..."
                    MB "And Miss [mom_name], stand behind her, staring at her ass."
                else:
                    scene bg HPCosplay103
                    with fade
                    R "It would be a crime to do a whole school discipline shoot, and not have a spanking scene."
                    R "But we need to heat this photo shoot up... So... Megan's panties will need to come off."
                    scene bg HPCosplay56
                    with fade
                    M "Wait! This isn't just a topless photo shoot!?"
                    scene bg HPCosplay57
                    with fade
                    M "[ryan]!! Did you make Lauren and Sidney expose themselves completely in their photo shoots!?"
                    R "Absolutely not!..."
                    scene bg HPCosplay59
                    with fade
                    MT "{i}Oh... Thank God!{/i}"
                    R "... They did it willingly by themselves."
                    scene bg HPCosplay57
                    with dissolve
                    M "[ryan]!! I'm going to castrate you when we get home!"
                    R "Now hold on just a minute!"
                    scene bg HPCosplay56
                    with dissolve
                    MT "{i}Since when does [ryan] dare talk back to me?{/i}"
                    R "Lauren and Sidney are both adults!"
                    R "They are perfectly capable of making their own decisions."
                    R "I mean for God's sake! You were working in a strip club when you were Sidney's age!"
                    scene bg HPCosplay57
                    with dissolve
                    M "Damnit, [ryan]! I didn't want anybody else to know about that!"
                    R "Megan won't say a word..."
                    R "Right Megan?"
                    play sound Muffled
                    $ renpy.pause (2.0)
                    stop sound
                    MG "Mrrmmmm..Hrmmm..."
                    RT "{i}Yeah right... Megan loves to gossip.{/i}"
                    R "Well, you say it like it's a bad thing... Why are you so ashamed of it?"
                    M "Because society says..."
                    R "Fuck society."
                    R "You had a dream... You needed to pay for it!"
                    R "Working at McDoogles wouldn't make enough to pay for your dream."
                    R "So you did what you needed to do."
                    R "Were the other strippers you worked with terrible people?"
                    scene bg HPCosplay56
                    with dissolve
                    M "No... Actually, I wish I was still friends with most of them."
                    R "Then stop worrying about what everyone else thinks, and let your daughters be empowered to make their own decisions... Just like you did at their age."
                    R "They wanted to do it to help with the weekly finances... To pay off \"you know who\"."
                    MG "Mrrhoo?"
                    M "Don't pry!... You already know too much about us."
                    M "But, they did that for me?"
                    R "Yes, and for all of us."
                    scene bg HPCosplay59
                    with dissolve
                    MT "{i}I really don't want to pose with Megan's bare ass... And I'm sure mine will be next... But I don't want Megan to go to the principal about what she saw in my office.{/i}"
                    MT "{i}So this is the least I can do for our family.{/i}"
                    scene bg HPCosplay58
                    with dissolve
                    MT "{i}[ryan] is a champion bullshitter!{/i}"
                    MT "{i}But I guess I can't argue with anything he just said.{/i}"
                    scene bg HPCosplay59
                    with dissolve
                    M "Fine! I'll do it."
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    R "Great!... Let's set up the scene."
                    R "Megan, bend over the table, or should I say desk..."
                    R "And Mom, stand behind her, staring at her ass."
                jump megan_spanked
            else:
                if blackmailed_mom_matt:
                    scene bg HPCosplay103
                    with fade
                    R "It would be a crime to do a whole school discipline shoot, and not have a spanking scene."
                    MB "Oh my God, you're right!... How did we forget a spanking scene?"
                    R "But we need to heat this photo shoot up... So... Megan's panties will need to come off."
                    scene bg HPCosplay56
                    with fade
                    M "Wait! This isn't just a topless photo shoot!?"
                    scene bg HPCosplay57
                    with fade
                    M "[ryan]!! Did you make Lauren and Sidney expose themselves completely in their photo shoots!?"
                    R "Absolutely not!..."
                    scene bg HPCosplay59
                    with fade
                    MT "{i}Oh... Thank God!{/i}"
                    R "... They did it willingly by themselves."
                    scene bg HPCosplay57
                    with dissolve
                    M "[ryan]!! I'm going to castrate you when we get home!"
                    R "Now hold on just a minute!"
                else:
                    scene bg HPCosplay103
                    with fade
                    R "It would be a crime to do a whole school discipline shoot, and not have a spanking scene."
                    R "But we need to heat this photo shoot up... So... Megan's panties will need to come off."
                    scene bg HPCosplay56
                    with fade
                    M "Wait! This isn't just a topless photo shoot!?"
                    scene bg HPCosplay57
                    with fade
                    M "[ryan]!! Did you make Lauren and Sidney expose themselves completely in their photo shoots!?"
                    R "Absolutely not!..."
                    scene bg HPCosplay59
                    with fade
                    MT "{i}Oh... Thank God!{/i}"
                    R "... They did it willingly by themselves."
                    scene bg HPCosplay57
                    with dissolve
                    M "[ryan]!! I'm going to castrate you when we get home!"
                    R "Now hold on just a minute!"
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son could do that to his own sisters."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +5\"{/i}"
                $ momanger += 5
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to spank Megan, you need her submission points at 19."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "We need a really good full nudity pose. {i}(submission 25+){/i}":
            if momsubmission >= 25:
                if blackmailed_mom_matt:
                    scene bg HPCosplay103
                    with fade
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    MB "Huh?... I kind of thought we'd build up to that more."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    MB "Alright, you heard him, ladies."
                    scene bg HPCosplay56
                    with fade
                    M "Wait! This isn't just a topless photo shoot!?"
                    scene bg HPCosplay57
                    with fade
                    M "[ryan]!! Did you make Lauren and Sidney expose themselves completely in their photo shoots!?"
                    R "Absolutely not!..."
                    scene bg HPCosplay59
                    with fade
                    MT "{i}Oh... Thank God!{/i}"
                    R "... They did it willingly by themselves."
                    scene bg HPCosplay57
                    with dissolve
                    M "[ryan]!! I'm going to castrate you when we get home!"
                    R "Now hold on just a minute!"
                    scene bg HPCosplay56
                    with dissolve
                    MT "{i}Since when does [ryan] dare talk back to me?{/i}"
                    R "Lauren and Sidney are both adults!"
                    R "They are perfectly capable of making their own decisions."
                    R "I mean for God's sake! You were working in a strip club when you were Sidney's age!"
                    scene bg HPCosplay57
                    with dissolve
                    M "Damnit, [ryan]! I didn't want anybody else to know about that!"
                    MB "We won't say a word."
                    MB "Right Megan?"
                    play sound Muffled
                    $ renpy.pause (2.0)
                    stop sound
                    MG "Mrrmmmm..Hrmmm..."
                    R "Well, you say it like it's a bad thing... Why are you so ashamed of it?"
                    M "Because society says..."
                    R "Fuck society."
                    R "You had a dream... You needed to pay for it!"
                    R "Working at McDoogles wouldn't make enough to pay for your dream."
                    R "So you did what you needed to do."
                    R "Were the other strippers you worked with terrible people?"
                    scene bg HPCosplay56
                    with dissolve
                    M "No... Actually, I wish I was still friends with most of them."
                    R "Then stop worrying about what everyone else thinks, and let your daughters be empowered to make their own decisions... Just like you did at their age."
                    R "They wanted to do it to help with the weekly finances... To pay off \"you know who\"."
                    MB "Who?"
                    M "Don't pry!... You already know too much about us."
                    M "But, they did that for me?"
                    R "Yes, and for all of us."
                    scene bg HPCosplay59
                    with dissolve
                    MT "{i}I really don't want to show my pussy... But I don't want Matt to go to the principal about what he saw in my office.{/i}"
                    MT "{i}So this is the least I can do for our family.{/i}"
                    scene bg HPCosplay58
                    with dissolve
                    MT "{i}[ryan] is a champion bullshitter!{/i}"
                    MT "{i}But I guess I can't argue with anything he just said.{/i}"
                    scene bg HPCosplay59
                    with dissolve
                    M "Fine! I'll do it."
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    MB "Wow! Good speech, [ryan]!"
                    MB "Alright, well let's set up the scene."
                    MB "Megan, get on your knees again with your ass facing towards us."
                    MB "And Miss [mom_name], take off your panties and sit right on top of her ass."
                else:
                    scene bg HPCosplay103
                    with fade
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    MB "Huh?... I kind of thought we'd build up to that more."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    MB "Alright, you heard him, ladies."
                    scene bg HPCosplay56
                    with fade
                    M "Wait! This isn't just a topless photo shoot!?"
                    scene bg HPCosplay57
                    with fade
                    M "[ryan]!! Did you make Lauren and Sidney expose themselves completely in their photo shoots!?"
                    R "Absolutely not!..."
                    scene bg HPCosplay59
                    with fade
                    MT "{i}Oh... Thank God!{/i}"
                    R "... They did it willingly by themselves."
                    scene bg HPCosplay57
                    with dissolve
                    M "[ryan]!! I'm going to castrate you when we get home!"
                    R "Now hold on just a minute!"
                    scene bg HPCosplay56
                    with dissolve
                    MT "{i}Since when does [ryan] dare talk back to me?{/i}"
                    R "Lauren and Sidney are both adults!"
                    R "They are perfectly capable of making their own decisions."
                    R "I mean for God's sake! You were working in a strip club when you were Sidney's age!"
                    scene bg HPCosplay57
                    with dissolve
                    M "Damnit, [ryan]! I didn't want anybody else to know about that!"
                    R "Megan won't say a word... right Megan?"
                    play sound Muffled
                    $ renpy.pause (2.0)
                    stop sound
                    MG "Mrrmmmm..Hrmmm..."
                    RT "{i}Yeah right... Megan loves to gossip.{/i}"
                    R "Well, you say it like it's a bad thing... Why are you so ashamed of it?"
                    M "Because society says..."
                    R "Fuck society."
                    R "You had a dream... You needed to pay for it!"
                    R "Working at McDoogles wouldn't make enough to pay for your dream."
                    R "So you did what you needed to do."
                    R "Were the other strippers you worked with terrible people?"
                    scene bg HPCosplay56
                    with dissolve
                    M "No... Actually, I wish I was still friends with most of them."
                    R "Then stop worrying about what everyone else thinks, and let your daughters be empowered to make their own decisions... Just like you did at their age."
                    R "They wanted to do it to help with the weekly finances... To pay off \"you know who\"."
                    MG "Mmrrho?"
                    M "Don't pry!... You already know too much about us."
                    M "But, they did that for me?"
                    R "Yes, and for all of us."
                    scene bg HPCosplay59
                    with dissolve
                    MT "{i}I really don't want to show my pussy... But I don't want Megan to go to the principal about what she saw in my office.{/i}"
                    MT "{i}So this is the least I can do for our family.{/i}"
                    scene bg HPCosplay58
                    with dissolve
                    MT "{i}[ryan] is a champion bullshitter!{/i}"
                    MT "{i}But I guess I can't argue with anything he just said.{/i}"
                    scene bg HPCosplay59
                    with dissolve
                    M "Fine! I'll do it."
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    MG "Wow! Good speech, [ryan]!"
                    R "Alright, well let's set up the scene."
                    R "Megan, get on your knees again with your ass facing towards us."
                    R "And Miss [mom_name], take off your panties and sit right on top of her ass."
                jump no_panties_shot
            else:
                if blackmailed_mom_matt:
                    scene bg HPCosplay103
                    with fade
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    MB "Huh?... I kind of thought we'd build up to that more."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    MB "Alright, you heard him, ladies."
                    scene bg HPCosplay56
                    with fade
                    M "Wait! This isn't just a topless photo shoot!?"
                    scene bg HPCosplay57
                    with fade
                    M "[ryan]!! Did you make Lauren and Sidney expose themselves completely in their photo shoots!?"
                    R "Absolutely not!..."
                    scene bg HPCosplay59
                    with fade
                    MT "{i}Oh... Thank God!{/i}"
                    R "... They did it willingly by themselves."
                    scene bg HPCosplay57
                    with dissolve
                    M "[ryan]!! I'm going to castrate you when we get home!"
                    R "Now hold on just a minute!"
                else:
                    scene bg HPCosplay103
                    with fade
                    R "Let's just go for it, and have them do a really sexy pose without their tops or panties."
                    MB "Huh?... I kind of thought we'd build up to that more."
                    R "Well, we all know that that's where this is going, so let's not beat around the bush."
                    MB "Alright, you heard him, ladies."
                    scene bg HPCosplay56
                    with fade
                    M "Wait! This isn't just a topless photo shoot!?"
                    scene bg HPCosplay57
                    with fade
                    M "[ryan]!! Did you make Lauren and Sidney expose themselves completely in their photo shoots!?"
                    R "Absolutely not!..."
                    scene bg HPCosplay59
                    with fade
                    MT "{i}Oh... Thank God!{/i}"
                    R "... They did it willingly by themselves."
                    scene bg HPCosplay57
                    with dissolve
                    M "[ryan]!! I'm going to castrate you when we get home!"
                    R "Now hold on just a minute!"
                M "Ok... I just realized this is too much for me right now."
                M "I think I need to take the rest of the day and wrap my head around how my own son could do that to his own sisters."
                R "Wait! Mom, are you ok?"
                M "No, I need to get out of here, I'm going to go and change."
                "{i}\"Mom's Anger +5\"{/i}"
                $ momanger += 5
                M "Maybe I'll be ok to shoot again on another day after I've processed this and calmed down."
                scene bg SleepBlack
                with fade
                "To get Mom to spank Megan, you need her submission points at 19."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Maybe we should end the shoot for today.":
            if blackmailed_mom_matt:
                scene bg HPCosplay56
                with fade
                R "I don't think we need to take any more pics today."
                MB "Really? We haven't taken very many."
                R "Yeah, but the ones we have are really good, and the only way they could be better is if we pushed the girls into something they might not be comfortable with."
                scene bg HPCosplay58
                with dissolve
                M "Oh, [ryan]! You really do act like a professional photographer."
                M "And that wasn't nearly as bad as I thought it would be!"
                M "And even though I'm being coerced into this, you both helped me feel pretty comfortable!"
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Mom's Libido +5\"{/b}{/i}"
                    $ momaffection += 1
                    $ momlibido += 5
                M "The next photo shoot might not make me feel so uneasy now."
                M "I might be even more daring, and be willing to show a little more skin... maybe..."
                MB "Great! I can't wait!"
                RT "{i}Ugghh... I wish Matt wasn't going to be there.{/i}"
            else:
                scene bg HPCosplay56
                with fade
                R "I don't think we need to take any more pics today."
                MG "Really? We haven't taken very many."
                R "Yeah, but the ones we have are really good, and the only way they could be better is if we pushed the girls into something they might not be comfortable with."
                scene bg HPCosplay58
                with dissolve
                M "Oh, [ryan]! You really do act like a professional photographer."
                M "And that wasn't nearly as bad as I thought it would be!"
                M "And even though I'm being coerced into this, you both helped me feel pretty comfortable!"
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Mom's Libido +5\"{/b}{/i}"
                    $ momaffection += 1
                    $ momlibido += 5
                M "The next photo shoot might not make me feel so uneasy now."
                M "I might be even more daring, and be willing to show a little more skin... maybe..."
                MG "Great! I can't wait!"
                RT "{i}Neither can I... I just need to be careful about pushing Mom too hard, and too fast... That's what she said.{/i}"
            R "You can get changed and I'll see you back home."
            hide screen Points_screen_Mom_cosplay
            jump posting_the_wr_pics

label megan_spanked:                    #### Edited ####
    if blackmailed_mom_matt:
        scene bg HPCosplay68
        with fade
        MB "Now Miss [mom_name], take a dominant stance and stare at her ass."
        MB "Megan, try to look distressed."
        MG "MMmmmrrrhhhmmm..."
        MB "...Yeah, just like that!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay68
        MB "Ok... Miss [mom_name], now you decide her panties need to come off, so squat down and reach up her skirt like you're about to take them off."
        scene bg HPCosplay69
        with fade
        MB "Really good."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay69
        MB "Now, let me come around to get a closeup, and you just pull those panties down."
        MT "{i}Am I really going to pull down one of my student's panties?{/i}"
        scene bg HPCosplay70
        with fade
        MT "{i}Oh, God!... I've never done this to another woman before... Or ever looked at a girl this intimately!{/i}"
        MT "{i}What a cute little ass Megan has... Oh, fuck! Did that thought really just come into my mind?{/i}"
        "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
        $ momlibido += 1
        MT "{i}Christ, [mom_name]! What is wrong with you lately!{/i}"
        MB "Wow Megan, you're sure you don't mind letting the whole world see this side of you?"
        MG "Not at all. It's my body, and I'm not ashamed of it."
        R "How are you talking?"
        MG "I got the gag out and onto my chin."
        MG "But what I was saying is, what an old fashioned idea that I should only be able to show it to someone who I'm intimate with."
        MT "{i}I used to think more like that when I was her age...{/i}"
        MT "{i}Which explains why I became a stripper.{/i}"
        MT "{i}Did I really let [dad_name] change me that much?{/i}"
        MB "Ok, Megan... Put your gag back in."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay70
        RT "{i}Just... Wow!{/i}"
        MB "Ok, Miss [mom_name], stand up and hold your wand up, like you're about to spank Megan."
        MB "And Megan... look scared."
        scene bg HPCosplay71
        with fade
        MB "Great job, both of you."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay71
        MB "Ok, Miss [mom_name]."
        MB "I want you to really spank Megan hard with your wand."
        M "Wait, what?"
        play sound Muffled
        $ renpy.pause (3.0)
        stop sound
        MG "Hhhrrrmmmm...?"
        MB "I'm going to be ready with the camera to take the picture the second the wand strikes Megan's ass."
        MB "I want Megan's reaction to be genuine, so I want you to really let her have it."
        play sound Muffled
        $ renpy.pause (3.0)
        stop sound
        play sound Slap
        scene bg HPCosplay72
        with dissolve
        MG "MMMMMMMRrrrmmmmmm!!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay72
        MB "Perfect! Great performance, Megan!"
        play sound Muffled
        $ renpy.pause (3.0)
        stop sound
        MB "Ok... Now we need another pose where Professor McGargleCum is triumphant and Hermione is showing her willingness to submit."
        MB "So Megan... Get on your knees...look up at Miss [mom_name]... and Miss [mom_name],... Grab her by the chin, and look sweetly into her eyes."
        MB "Ohh... And Miss [mom_name],... it would look really good if you took the dress all the way off."
        MT "{i}Well... I am wearing panties, so it's not like they'll see much more of me...{/i}"
        MT "{i}I can do that.{/i}"
        M "Ok..."
        RT "{i}What a relief... She's finally doing something without me having to convince her... I'm almost out of bullshit.{/i}"
        scene bg HPCosplay73
        with fade
        MB "Oh, wow! That's great you two!"
        R "Yeah,... it's sweet, and intimate, and super sexy, all at the same time!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay73
        MB "Super sexy!"
        MB "This might be my favorite pose so far."
        MB "Unless you have an even better one in mind, [ryan]?"
        R "Hmmm... yeah... Should we have them do one more?"
    else:
        scene bg HPCosplay68
        with fade
        R "Now Mom, take a dominant stance and stare at her ass."
        R "Megan, try to look distressed."
        MG "MMmmmrrrhhhmmm..."
        R "...Yeah, just like that!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay68
        R "Ok... Mom, now you decide her panties need to come off, so squat down and reach up her skirt like you're about to take them off."
        scene bg HPCosplay69
        with fade
        R "Really good."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay69
        R "Now, let me come around to get a closeup, and you just pull those panties down."
        MT "{i}Am I really going to pull down one of my student's panties?{/i}"
        scene bg HPCosplay70
        with fade
        MT "{i}Oh, God!... I've never done this to another woman before... Or ever looked at a girl this intimately!{/i}"
        MT "{i}What a cute little ass Megan has... Oh, fuck! Did that thought really just come into my mind?{/i}"
        "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
        $ momlibido += 1
        MT "{i}Christ, [mom_name]! What is wrong with you lately!{/i}"
        R "Wow Megan, you're sure you don't mind letting the whole world see this side of you?"
        MG "Not at all. It's my body, and I'm not ashamed of it."
        R "How are you talking?"
        MG "I got the gag out and onto my chin."
        MG "But what I was saying is, what an old fashioned idea that I should only be able to show it to someone who I'm intimate with."
        MT "{i}I used to think more like that when I was her age...{/i}"
        MT "{i}Which explains why I became a stripper.{/i}"
        MT "{i}Did I really let [dad_name] change me that much?{/i}"
        R "Ok, Megan... Put your gag back in."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay70
        RT "{i}Just... Wow!{/i}"
        R "Ok Mom, stand up and hold your wand up, like you're about to spank Megan."
        R "And Megan... look scared."
        scene bg HPCosplay71
        with fade
        R "Great job, both of you."
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay71
        R "Ok Mom."
        R "I want you to really spank Megan hard with your wand."
        M "Wait, what?"
        play sound Muffled
        $ renpy.pause (3.0)
        stop sound
        MG "Hhhrrrmmmm...?"
        R "I'm going to be ready with the camera to take the picture the second the wand strikes Megan's ass."
        R "I want Megan's reaction to be genuine, so I want you to really let her have it."
        play sound Muffled
        $ renpy.pause (3.0)
        stop sound
        play sound Slap
        scene bg HPCosplay72
        with dissolve
        MG "MMMMMMMRrrrmmmmmm!!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay72
        R "Perfect! Great performance, Megan!"
        play sound Muffled
        $ renpy.pause (3.0)
        stop sound
        R "Ok... Now we need another pose where Professor McGargleCum is triumphant and Hermione is showing her willingness to submit."
        R "So Megan... Get on your knees...look up at Miss [mom_name]... and Mom...Grab her by the chin, and look sweetly into her eyes."
        R "Ohh... And Mom,... it would look really good if you took the dress all the way off."
        MT "{i}Well... I am wearing panties, so it's not like they'll see much more of me...{/i}"
        MT "{i}I can do that.{/i}"
        M "Ok..."
        RT "{i}What a relief... She's finally doing something without me having to convince her... I'm almost out of bullshit.{/i}"
        scene bg HPCosplay73
        with fade
        R "Oh, wow! That's great you two!"
        R "It's sweet, and intimate, and sexy, all at the same time!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay73
        R "Super sexy!"
        R "This might be my favorite pose so far."
        R "But I think we might be able to top it."
        R "Hmmm... yeah... Should we have you two do one more?"
        scene bg HPCosplay104
        with fade
    $ hp_shoot_almost_finished = True
    R "Hmmmm... last one... what should we have you do?"
    menu:
        "We need a really good full nudity shot. {i}(submission 25+){/i}":
            if momsubmission >= 25:
                if blackmailed_mom_matt:
                    R "The only type of shot we're missing now, is a shot with both of you completely naked."
                    R "Mom? Do you think you're ready for a full nudity shot?"
                    M "Yeah... Anything to end this photo shoot and do what I need to protect our family."
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    M "Is this really our last pose?"
                    MB "Yeah... Unless you want to do more."
                    M "God, no!"
                    MB "Haha... Then after this, I promise we'll be done."
                    MB "So, for this shot I want Megan to get on her knees, with her ass pointing towards the camera."
                    MB "Then Miss [mom_name], I want you to lose your panties, and then go ahead and sit on Megan's ass. That we we get a good shot of both your goods."
                    M "Our goods?"
                    MB "Or... Whatever you want to call them."
                else:
                    R "The only type of shot we're missing now, is a shot with both of you completely naked."
                    R "Mom? Do you think you're ready for a full nudity shot?"
                    M "Yeah... Anything to end this photo shoot and do what I need to protect our family."
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    M "Is this really our last pose?"
                    R "Yeah... Unless you want to do more."
                    M "God, no!"
                    R "Haha... Then after this, I promise we'll be done."
                    R "So, for this shot I want Megan to get on her knees, with her ass pointing towards the camera."
                    R "Then Mom, I want you to lose your panties, and then go ahead and sit on Megan's ass. That we we get a good shot of both your goods."
                    M "Our goods?"
                    R "Or... Whatever you want to call them."
                M "... I guess goods is fine."
                jump no_panties_shot
            else:
                R "The only type of shot we're missing now, is a shot with both of you completely naked."
                R "Mom? Are you ready for a full nudity shot?"
                M "I'm sorry... I just can't."
                R "Really? We're so close to finishing the photo shoot. We just need one more shot."
                M "I'm not in the mood, [ryan]!"
                R "Come on... Let's just get it over with really quick and then we can all be done."
                M "[ryan]! If you push any harder, then I'm not ever coming back to finish it ever!"
                "{i}{b}\"Mom's Anger +5\"{/b}{/i}"
                $ momanger += 5
                RT "{i}Damnit! We're so close! I guess we'll just have to come back one more time.{/i}"
                scene bg SleepBlack
                with fade
                "To get Mom to pose totally nude with Megan, you need her submission points at 25."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Maybe we should end the shoot for today.":
            if blackmailed_mom_matt:
                scene bg HPCosplay56
                with fade
                R "I don't think we need to take any more pics today."
                MB "Really? We haven't taken very many."
                R "Yeah, but the ones we have are really good, and the only way they could be better is if we pushed the girls into something they might not be comfortable with."
                scene bg HPCosplay58
                with dissolve
                M "Oh, [ryan]! You really do act like a professional photographer."
                M "And that wasn't nearly as bad as I thought it would be!"
                M "And even though I'm being coerced into this, you both helped me feel pretty comfortable!"
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Mom's Libido +5\"{/b}{/i}"
                    $ momaffection += 1
                    $ momlibido += 5
                M "The next photo shoot might not make me feel so uneasy now."
                M "I might be even more daring, and be willing to show a little more skin... maybe..."
                MB "Great! I can't wait!"
                RT "{i}Ugghh... I wish Matt wasn't going to be there.{/i}"
            else:
                scene bg HPCosplay56
                with fade
                R "I don't think we need to take any more pics today."
                MG "Really? We haven't taken very many."
                R "Yeah, but the ones we have are really good, and the only way they could be better is if we pushed the girls into something they might not be comfortable with."
                scene bg HPCosplay58
                with dissolve
                M "Oh, [ryan]! You really do act like a professional photographer."
                M "And that wasn't nearly as bad as I thought it would be!"
                M "And even though I'm being coerced into this, you both helped me feel pretty comfortable!"
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Mom's Libido +5\"{/b}{/i}"
                    $ momaffection += 1
                    $ momlibido += 5
                M "The next photo shoot might not make me feel so uneasy now."
                M "I might be even more daring, and be willing to show a little more skin... maybe..."
                MG "Great! I can't wait!"
                RT "{i}Neither can I... I just need to be careful about pushing Mom too hard, and too fast... That's what she said.{/i}"
            R "You can get changed and I'll see you back home."
            hide screen Points_screen_Mom_cosplay
            jump posting_the_wr_pics

label no_panties_shot:                  #### Edited ####
    if blackmailed_mom_matt and not finished_hp_shoot:
        scene bg HPCosplay74
        with fade
        MB "Oh, my God! This is going to be my favorite picture."
        hide screen Points_screen_Mom_cosplay
        MT "{i}Haha... He's not kidding! Look how hard his dick is! It's so big, there's no possible way to hide it.{/i}"
        MT "{i}Poor boy... Those pants are so tight... it must be uncomfortable.{/i}"
        MT "{i}I'll bet when he takes these pics home, he's going to spend all night jacking off to them.{/i}"
        MT "{i}Poor boy needs some relief!{/i}"
        MT "{i}I suppose I could help him out.{/i}"
        MT "{i}It wouldn't be much different than helping my own son...{/i}"
        MT "{i}Matt needs to practice good sexual health too.{/i}"
        if not finished_hp_shoot:
            "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
            $ momlibido += 1
        MT "{i}Holy shit, [mom_name]! Listen to yourself!{/i}"
        MT "{i}That makes no sense!{/i}"
        MT "{i}My horny brain is trying to justify any kind of sexual deviancy!{/i}"
        MT "{i}Fight it, [mom_name]!{/i}"
        MT "...."
        MT "{i}Still...{/i}"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay74
        MB "And one quick close-up shot."
        scene bg HPCosplay100
        with fade
        MB "Wow!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay100
        MB "And that's it!"
        MB "That was amazing, you two!"
        scene bg SleepBlack
        with fade
        scene bg HPCosplay80
        with fade
        M "Well Matt, I want to compliment you on keeping things so professional."
        M "I don't think I've ever had a student mature enough to be in a situation like this without making inappropriate or crass comments."
        MB "Thanks, Miss [mom_name]"
        M "I think you make a very good director and cameraman."
        R "What about me? I'm the one who came up with the ideas for most of the shots!"
        scene bg HPCosplay81
        with dissolve
        M "Yeah... And most of them were quite inappropriate! I only did them because I felt like I had no choice."
        M "Honestly! I can't believe I raised such a pervert!"
        RT "{i}Pervert!?... I guess that's fair, but look at Matt staring at Mom's pussy while she isn't looking!{/i}"
        R "I only had to come up with the poses because Matt was too chicken to do it himself.  That's not a good director."
        scene bg HPCosplay79
        with fade
        M "[ryan]! Now you're being extremely mean spirited and rude. Why don't you take Megan and go!"
        R "But I have to clean up the studio."
        M "I'll have Matt help me clean it up.  It can't be that hard, and I'll lock everything up before we leave."
        R "But why can't I?..."
        M "Because I don't want you to be here when you're being so moody!"
        M "If I didn't have to change and get ready, then I would leave, but I do, so Matt can stay here and move the tables and fans and other props to where they're supposed to be."
        M "You just take Megan and go."
        R "But Megan has to get ready too."
        MG "I'm ready! Matt, are you going to take me home?"
        MB "No Megs, [ryan] is going to take you home. I'm going to stay here and help Miss [mom_name] clean up and stuff."
        M "Go, [ryan]!"
        R "Fine... I've got some images I need to work on and upload to the internet anyways!"
        M "God, I hope nobody I know finds those pics!"
        scene bg SleepBlack
        with fade
        scene bg HPCosplay82
        with fade
        MG "What was that all about?"
        MG "Your mom seemed pissed at you."
        R "I don't know, but I think something funny is going on."
        MG "Uh-Oh... Knowing what I know about Matt, I wouldn't look back, or linger around here. You probably won't like what's going to happen next."
        scene bg SleepBlack
        with fade
        scene bg HPCosplay83
        with fade
        MG "I'm serious, [ryan]!"
        MG "Let's just go."
        MG "I need you to give me a ride."
        R "No... I've got to see this."
        MG "I'm not kidding, [ryan]! You're not going to like it!"
        menu:
            "Listen to Megan and go.":
                R "I guess you're right, I don't want to see this."
                $ didnt_watch = True
                R "Climb on the back of the scooter, and we'll go."
                scene bg SleepBlack
                with fade
                $ finished_hp_shoot = True
                jump citymap
            "Stay and watch.":
                R "I know I'm not going to like it..."
                R "But it's like a car wreck... I can't look away."
                scene bg SleepBlack
                with fade
                scene bg HPCosplay88
                with fade
                M "I hope it isn't awkward that I bring this up... But I couldn't help but notice that your penis was very erect throughout a lot of the photo shoot."
                M "Was that just because of Megan, or was it because you were watching your teacher do naughty things?"
                MB "It was because my teacher was doing naughty things with my girlfriend."
                M "Well... After something that sexually tense... I hope she'll be taking good care of you."
                MB "What, Megan?... No... She's comfortable with her body and all, but she's still a virgin, and refuses to do anything sexual with me."
                scene bg HPCosplay78
                with fade
                M "What!?"
                scene bg SleepBlack
                with fade
                scene bg HPCosplay83
                with fade
                R "{i}(whispering){/i} That's bullshit!"
                MG "{i}(Whispering even quieter){/i}Shhh... If your mom catches us spying... Matt will kick both our asses."
                R "{i}(whispering){/i} Does he hit you?"
                MG "Shhhh..."
                scene bg SleepBlack
                with fade
                scene bg HPCosplay78
                with fade
                M "Wow! I can't believe that! She has quite a reputation at school."
                MB "Yeah... Well, people like to gossip."
                MB "She actaully comes from a very conservative family and believes we should wait until marriage."
                M "So you've just been taking care of yourself?"
                MB "Taking care of myself?..."
                scene bg HPCosplay77
                with dissolve
                M "You know..."
                M "Masturbating yourself?"
                MB "Ohhh... That!..."
                MB "No... Not since I've been with Megan.  Megan thinks I need to... keep it all in, until we're married."
                scene bg HPCosplay79
                with dissolve
                M "Of all the irresponsible, ignorant ideas..."
                scene bg HPCosplay78
                with dissolve
                M "You poor boy!"
                M "That is so unhealthy!"
                MB "It is?..."
                M "Oh my gosh, yes!"
                MT "{i}God! I shouldn't be having this kind of conversation with a student!{/i}"
                MT "{i}And I shouldn't have these impure thoughts! What is wrong with me!?{/i}"
                MT "{i}But... I don't have to do anything with him... But maybe I can get a view of his cock.{/i}"
                M "You need to take care of yourself... And you should probably do it now! It's really unhealthy for a man to get so aroused without ejaculating."
                MB "Yeah... I get blue balls all the time, it really hurts!"
                M "Oh please, take care of yourself! That is so unhealthy."
                MT "{i}I need to see that cock!{/i}"
                MB "The thing is, Miss [mom_name]... I promised Megan that I wouldn't do that to myself... And I can't break that promise."
                M "Even if it's bad for your health?"
                MB "I... just... couldn't do that..."
                M "Uuurrgghhh... Those dang unhealthy religious beliefs about sexuality!"
                MT "{i}I suppose it wouldn't hurt to help him out the way I help [ryan].{/i}"
                MT "{i}Plus, I would love to get my hands around that cock.{/i}"
                MT "{i}Goddammit, [mom_name]!{/i}"
                MT "{i}Why have I lost all of my self-control?{/i}"
                scene bg HPCosplay77
                with dissolve
                M "I can't believe I'm offering this... And it's only because I'm so worried about you..."
                M "And you couldn't say a word about it to anybody!"
                MB "What are you talking about?"
                M "Well... Maybe... I could masturbate you, so that you don't have to."
                RT "{i}Oh, my God! Who is this person?{/i}"
                MB "Oh my God, Miss [mom_name]!... That is so nice of you!"
                MB "But I couldn't do it... I promised Megan that I wouldn't let anybody else jack me off either."
                M "You need to break up with this girl!"
                MB "I couldn't... I think I love her."
                scene bg HPCosplay79
                with dissolve
                M "Urrgghh... Then I'd better have a talk with her."
                MB "Please don't!... She'll feel like I betrayed her trust by telling you all of this."
                scene bg HPCosplay78
                with dissolve
                MT "{i}This girl is no good for Matt! She won't even let him or anybody else help him out with one of the most basic needs of any male.{/i}"
                MT "{i}And I know I shouldn't get involved, but I feel so close to Matt after that photo shoot, not to mention fucking [dad_name] leaving me high and dry.{/i}"
                MT "{i}Hmmm... What if?...{/i}"
                scene bg HPCosplay77
                with dissolve
                M "Did Megan make you promise that someone couldn't take care of you orally?"
                MB "What do you mean?"
                M "You know... Like a blowjob?"
                MT "{i}Did that just come out of my mouth?{/i}"
                MB "No... We didn't really ever talk about that possibility."
                MB "Are you?... Offering?... a..."
                M "Maybe?"
                scene bg SleepBlack
                with fade
                scene bg HPCosplay83
                with fade
                R "{i}(whispering){/i} Holy fuck! She'd better not!"
                MG "Ssshhh!..."
                scene bg SleepBlack
                with fade
                scene bg HPCosplay78
                with fade
                M "It's only because I'm so worried about your health... And it would only be this once... And you couldn't ever tell a soul!"
                M "But I'd feel so much better knowing you're not going home with testicular pain!"
                M "Plus, never ejaculating gives you a higher risk of prostate cancer."
                MB "So you're saying you're willing to give me a blowjob?"
                MT "{i}Am I?... to a student?...  Who is very mature... and handsome... And has a huge cock!{/i}"
                MT "{i}I'm going to hell.{/i}"
                M "Yeah... I guess I am."
                MB "Wow, Miss [mom_name]! I've never had a teacher who cares so much about me."
                MT "{i}Ohh... How sweet!{/i}"
                MT "{i}I am just being a good, caring teacher...{/i}"
                MT "...."
                MT "{i}Stop lying to yourself, you slut!{/i}"
                scene bg SleepBlack
                with fade
                play music SexMusic
                scene bg HPCosplay90
                with fade
                M "That's got to feel so much better to get your hard penis out of those tight pants."
                MB "It feels so much better! Thank you."
                M "It's my pleasure."
                M "Are you ready for some relief?"
                MB "Please, Miss [mom_name]!"
                scene HPCosplayVideo04
                with dissolve
                $ renpy.pause ()
                MB "OH... That feels so good, Miss [mom_name]."
                MB "Thank you so much!"
                MT "{i}He is so well mannered.{/i}"
                scene bg SleepBlack
                with fade
                scene bg HPCosplay83
                with fade
                R "{i}(whispering){/i} That's it! I'm going in there, and I'm going to kill him!"
                MG "{i}(whispering){/i}Oh shit! It looks like I need to take some control."
                MG "Here, let me take your mind off of all of that."
                scene bg HPCosplay84
                with fade
                R "Wait! No... Megan... that's not what I want!"
                scene HPCosplayVideo01
                with fade
                play sound Blow03 loop
                $ renpy.pause ()
                R "Aaahhh..."
                RT "{i}I'll just go stop them in a minute.{/i}"
                MB "{i}(Distantly){/i} Ohhh... Miss [mom_name]! That feels even better!"
                stop sound
                scene bg SleepBlack
                with fade
                scene HPCosplayVideo02
                with fade
                play sound Blow01 loop
                $ renpy.pause ()
                MB "Your husband is a lucky man!"
                MT "{i}Why did that fucker have to bring up my husband?{/i}"
                MT "{i}His dick isn't nearly this big.{/i}"
                MT "{i}Both [ryan] and Matt have much nicer cocks than that loser!{/i}"
                MT "{i}Fucking criminal deserves to be cheated on.{/i}"
                MB "Wow, Miss [mom_name], you're sucking even harder now!"
                stop sound
                scene bg SleepBlack
                with fade
                scene HPCosplayVideo01
                with fade
                play sound Blow03 loop
                $ renpy.pause ()
                RT "{i}Why is Mom such a slut?{/i}"
                RT "{i}Is this my fault?{/i}"
                RT "{i}Did I drive her to Matt?{/i}"
                RT "{i}Look at her just polishing Matt's knob like it's the most natural thing in the world for her!{/i}"
                RT "{i}Fucking slut!{/i}"
                stop sound
                scene bg SleepBlack
                with fade
                scene HPCosplayVideo02
                with fade
                play sound Blow01 loop
                $ renpy.pause ()
                MB "I hope you don't mind if I tell the other boys in the school that you're helping students with their sexual health?"
                M "HHRRMMMGGGHHHH!!..."
                MB "Hahaha... I'm just kidding."
                MT "{i}That fucker better be!{/i}"
                MT "{i}Although... Thinking of all those young men... surrounding me with their youthful cocks!{/i}"
                MT "{i}Taking my turn on each one of them!{/i}"
                M "HHHMMMmmmmmnnn!..."
                MT "{i}Oh, God!! I just came!... Without even fucking touching myself!... I just came!{/i}"
                MT "...."
                MB "I'm gonna cum!"
                stop sound
                play sound Ejaculate
                scene bg HPCosplay93
                with fade
                $ renpy.pause ()
                scene bg HPCosplay94
                with dissolve
                MT "{i}Oh, God! He's completely covered me!{/i}"
                "{i}\"Mom's Libido +10\"{/i}"
                $ momlibido += 10
                MT "{i}I've got to get home and take care of myself!{/i}"
                RT "{i}Urrgghhh... Look at that slut, all covered in Matt's cum!{/i}"
                R "Hnnnggghhh..."
                scene bg SleepBlack
                with fade
                play sound Ejaculate
                scene bg HPCosplay85
                with fade
                with hpunch
                MG "Bllerrrgggghhh!"
                $ renpy.pause ()
                scene bg HPCosplay86
                with fade
                MG "{i}(whispering){/i} You asshole! You could have warned me!"
                R "{i}(whispering){/i} Sorry! I was actually trying not to... but..."
                MG "You liked seeing your mom suck off Matt?"
                R "No!..."
                R "I don't think..."
                MG "Hahaha... You're well on your way to being a complete sexual deviant, just like Matt and I."
                R "I don't want to be that..."
                MG "Yeah, right..."
                MG "Now, will you fucking give me a ride home on that shitty little scooter?"
                R "Yeah... ok..."
                $ persistent.gal_NTR_5 = True
                $ mom_sucked_matt = True
                $ finished_hp_shoot = True
                play music Honey
                scene bg SleepBlack
                with fade
                jump posting_ph_pics
    if blackmailed_mom_matt:
        scene bg HPCosplay74
        with fade
        MB "Oh, my God! This is going to be my favorite picture."
        hide screen Points_screen_Mom_cosplay
        MT "{i}Haha... He's not kidding! Look how hard his dick is! It's so big, there's no possible way to hide it.{/i}"
        MT "{i}Poor boy... Those pants are so tight... it must be uncomfortable.{/i}"
        MT "{i}I'll bet when he takes these pics home, he's going to spend all night jacking off to them.{/i}"
        MT "{i}Poor boy needs some relief!{/i}"
        MT "{i}I suppose I could help him out... again!{/i}"
        MT "{i}Matt needs to continue to practice good sexual health.{/i}"
        if not finished_hp_shoot:
            "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
            $ momlibido += 1
        MT "{i}Holy shit, [mom_name]! Listen to yourself!{/i}"
        MT "{i}That was only going to be a one time thing!{/i}"
        MT "{i}Shut up, horny brain!{/i}"
        MT "{i}Fight it, [mom_name]!{/i}"
        MT "...."
        MT "{i}Still...{/i}"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay74
        MB "And one quick close-up shot."
        scene bg HPCosplay100
        with fade
        MB "Wow!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay100
        MB "And that's it!"
        MB "That was amazing, you two!"
        scene bg SleepBlack
        with fade
        scene bg HPCosplay80
        with fade
        M "Well Matt, I want to compliment you again on keeping things so professional."
        MB "Thanks, Miss [mom_name]"
        M "I think you make a very good director and cameraman."
        R "What about me? I'm the one who came up with the ideas for most of the shots!"
        scene bg HPCosplay81
        with dissolve
        M "Yeah... And most of them were quite inappropriate! I only did them because I felt like I had no choice."
        M "Honestly! I can't believe I raised such a pervert!"
        RT "{i}Pervert!?... I guess that's fair, but look at Matt staring at Mom's pussy while she isn't looking!{/i}"
        R "I only had to come up with the poses because Matt was too chicken to do it himself.  That's not a good director."
        scene bg HPCosplay79
        with fade
        M "[ryan]! Now you're being extremely mean spirited and rude again. Why don't you take Megan and go!"
        R "But I have to clean up the studio."
        M "I'll have Matt help me clean it up again, and don't worry, I'll lock everything up before we leave."
        R "But why can't I?..."
        M "Because I don't want you to be here when you're being so moody!"
        M "If I didn't have to change and get ready, then I would leave, but I do, so Matt can stay here and move the tables and fans and other props to where they're supposed to be."
        M "You just take Megan and go."
        R "But Megan has to get ready too."
        MG "I'm ready! Matt, are you going to take me home?"
        MB "No Megs, [ryan] is going to take you home again. I'm going to stay here and help Miss [mom_name] clean up and stuff."
        M "Go, [ryan]!"
        R "Fine... I've got some images I need to work on and upload to the internet anyways!"
        M "God, I hope nobody I know finds those pics!"
        scene bg SleepBlack
        with fade
        scene bg HPCosplay82
        with fade
        MG "You need to stop pissing her off!"
        R "I think she's just looking for an excuse to get rid of me at this point."
        MG "Well hopefully you're smart enough not to stick around this time... Unless you like watching, you filthy pervert."
        scene bg SleepBlack
        with fade
        scene bg HPCosplay83
        with fade
        MG "I'm serious, [ryan]!"
        MG "Let's just go."
        MG "I need you to give me a ride."
        R "No... I've got to see this."
        MG "Are you sure?"
        menu:
            "Listen to Megan and go.":
                R "I guess you're right, I don't want to see this."
                $ didnt_watch = True
                R "Climb on the back of the scooter, and we'll go."
                scene bg SleepBlack
                with fade
                jump citymap
            "Stay and watch.":
                R "I know I'm not going to like it..."
                R "But it's like a car wreck... I can't look away."
                scene bg SleepBlack
                with fade
                scene bg HPCosplay88
                with fade
                M "I hope it isn't awkward that I bring this up... But I couldn't help but notice that your penis was very erect during some of those shots again."
                M "Were you thinking about me again?"
                MB "How could I resist?"
                M "Well... After something that sexually tense... I'm thinking you're going to need another release."
                scene bg HPCosplay77
                with dissolve
                M "I can't believe I'm offering this again... And it's only because I'm so worried about you..."
                M "And you still couldn't say a word about it to anybody!"
                MB "Oh, I know..."
                MT "{i}What the hell, [mom_name]?... You're offering your student another blowjob?{/i}"
                scene bg SleepBlack
                with fade
                scene bg HPCosplay83
                with fade
                R "{i}(whispering){/i} Holy fuck! She's gonna do it again!"
                MG "Ssshhh!..."
                scene bg SleepBlack
                with fade
                scene bg HPCosplay78
                with fade
                M "It's only because I'm so worried about your health... And this would be the last time... And you couldn't ever tell a soul!"
                M "But I'd feel so much better knowing you're not going home with testicular pain!"
                M "And less of a chance of getting prostate cancer."
                MB "So you're saying you're willing to give me another blowjob?"
                MT "{i}Fuck me, I want it so bad!{/i}"
                M "Yeah... I guess I am."
                MB "Wow, Miss [mom_name]! I've never had a teacher who cares so much about me."
                MT "{i}Ohh... How sweet!{/i}"
                MT "{i}I am just being a good, caring teacher...{/i}"
                MT "...."
                MT "{i}Stop lying to yourself, you slut!{/i}"
                scene bg SleepBlack
                with fade
                play music SexMusic
                scene bg HPCosplay90
                with fade
                M "That's got to feel so much better to get your hard penis out of those tight pants."
                MB "It feels so much better! Thank you."
                M "It's my pleasure."
                M "Are you ready for some relief?"
                MB "Please, Miss [mom_name]!"
                scene HPCosplayVideo04
                with dissolve
                $ renpy.pause ()
                MB "OH... That feels so good, Miss [mom_name]."
                MB "Thank you so much!"
                MT "{i}He is so well mannered.{/i}"
                scene bg SleepBlack
                with fade
                scene bg HPCosplay83
                with fade
                R "{i}(whispering){/i} That's it! I'm going in there, and I'm going to kill him!"
                MG "{i}(whispering){/i}Oh, shit! It looks like I need to take some control again!"
                MG "Here, let me take your mind off of all of that."
                scene bg HPCosplay84
                with fade
                R "Wait! No... Megan... I'm not trying to get another blowjob!"
                scene HPCosplayVideo01
                with fade
                play sound Blow03 loop
                $ renpy.pause ()
                R "Aaahhh..."
                RT "{i}I'll just go stop them in a minute.{/i}"
                MB "{i}(Distantly){/i} Ohhh... Miss [mom_name]! That feels even better!"
                stop sound
                scene bg SleepBlack
                with fade
                scene HPCosplayVideo02
                with fade
                $ renpy.pause ()
                play sound Blow01 loop
                MB "If I was your husband I'd make you feel so good!"
                MT "{i}Why did that fucker have to bring up my husband again?{/i}"
                MB "I'd fuck you all night, and twice in the morning before you go to school."
                MT "{i}He shouldn't be talking to his teacher like that!{/i}"
                MB "I'd eat your pussy and ass like it were my last meal."
                MT "{i}Oh, fuck!... He needs to stop that! It's turning me on so much!{/i}"
                MB "Wow, Miss [mom_name], you're sucking even harder now!"
                stop sound
                scene bg SleepBlack
                with fade
                scene HPCosplayVideo01
                with fade
                play sound Blow03 loop
                $ renpy.pause ()
                RT "{i}Why is Mom such a slut?{/i}"
                RT "{i}Is this my fault?{/i}"
                RT "{i}Did I drive her to Matt?{/i}"
                RT "{i}Look at her just polishing Matt's knob like it's the most natural thing in the world for her!{/i}"
                RT "{i}Fucking slut!{/i}"
                stop sound
                scene bg SleepBlack
                with fade
                scene HPCosplayVideo02
                with fade
                play sound Blow01 loop
                $ renpy.pause ()
                MB "Are you sure you don't want me to tell the other boys in the school that you're helping students with their sexual health?"
                M "HHRRMMMGGGHHHH!!..."
                MB "Hahaha... Still kidding."
                MT "{i}That fucker better be!{/i}"
                MT "{i}Although... Thinking of all those young men... surrounding me with their youthful cocks!{/i}"
                MT "{i}Taking my turn on each one of them!{/i}"
                MT "{i}Still the thought drives me crazy!{/i}"
                M "HHHMMMmmmmmnnn!..."
                MT "{i}Oh God!! I just came again!... Without even fucking touching myself!... I just came!{/i}"
                "\"{i}Mom's Libido =0\"{/i}"
                $ momlibido = 0
                stop sound
                MB "I'm gonna cum!"
                play sound Ejaculate
                scene bg HPCosplay93
                with fade
                $ renpy.pause ()
                scene bg HPCosplay94
                with dissolve
                MT "{i}Oh, God! He's completely covered me again!{/i}"
                "{i}\"Mom's Libido +10\"{/i}"
                $ momlibido += 10
                MT "{i}I've got to get home and take care of myself!{/i}"
                RT "{i}Urrgghhh... Look at that slut, all covered in Matt's cum!{/i}"
                R "Hnnnggghhh..."
                scene bg SleepBlack
                with fade
                play sound Ejaculate
                scene bg HPCosplay85
                with fade
                with hpunch
                MG "Bllerrrgggghhh!"
                $ renpy.pause ()
                scene bg HPCosplay86
                with fade
                MG "{i}(whispering){/i} You asshole! You didn't warn me again!"
                R "{i}(whispering){/i} Sorry! I was actually trying not to... but..."
                MG "You liked seeing your mom suck off Matt again?"
                R "No!..."
                R "It pisses me off!"
                MG "Hahaha..."
                R "Shut up!..."
                MG "You shut up!..."
                MG "Now, will you fucking give me a ride home on that shitty little scooter?"
                R "Yeah... ok..."
                scene bg SleepBlack
                with fade
                play music Honey
                jump posting_ph_pics
    if blackmailed_mom_megan and not finished_hp_shoot:
        scene bg HPCosplay74
        with fade
        R "Oh, my God! This is going to be my favorite picture."
        hide screen Points_screen_Mom_cosplay
        MT "{i}Haha... He's not kidding! Look how hard his dick is! There's no possible way to hide it. I'm sure Megan's noticed.{/i}"
        MT "{i}Poor boy... Those pants are so tight... it must be uncomfortable.{/i}"
        MT "{i}I'll bet when he takes these pics home, he's going to spend all night jacking off to them.{/i}"
        MT "{i}Because of Megan, of course!... Not me... I hope... don't I?... Shut up, brain!{/i}"
        MT "{i}But, that poor boy needs some relief!{/i}"
        MT "{i}I suppose I could help him out.{/i}"
        if not finished_hp_shoot:
            "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
            $ momlibido += 1
        MT "{i}And if it helps him to get through this Oedipal phase!{/i}"
        MT "{i}Does that make sense?{/i}"
        MT "{i}Is my horny brain trying to justify any kind of sexual deviancy!{/i}"
        MT "{i}Fight it, [mom_name]!{/i}"
        MT "...."
        MT "{i}Still...{/i}"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay74
        R "And one quick close-up shot."
        scene bg HPCosplay100
        with fade
        R "Wow!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay100
        R "And that's it!"
        R "That was amazing, you two!"
        scene bg SleepBlack
        with fade
        scene bg HPCosplay75
        with fade
        M "Well, I hope that photo shoot was satisfactory for you."
        M "And I hope you won't threaten to tell the school board anything about what you saw in my office."
        MG "Yeah, and really I should be thanking you for being in this shoot with me.  I know it's going to be super successful!"
        MG "I can't wait to see my online status jump through the roof!"
        scene bg HPCosplay76
        with fade
        R "I might need you to come back a time or two to get a couple more pictures if some of them don't turn out."
        MG "We can do that."
        M "Uuuhhh... I suppose..."
        MG "And thank you [ryan], for being such a good director and cameraman."
        MG "I'd love to reward you somehow... Maybe you can meet me in the utility closet after your mom leaves?"
        M "Ok Megan, I think it's time for you to run along... [ryan] isn't going to be meeting you in the utility closet."
        MT "{i}You two-bit hussy.{/i}"
        MT "{i}I'm taking care of him on my own.{/i}"
        MG "I don't have a car, remember?... You drove me here."
        M "Take [ryan]'s scooter.  You can give it back to him at school in the morning."
        if daycounter == 5 or daycounter == 6:
            MG "But we don't have school in the morning."
            M "Well, the next time you see him then."
        else:
            pass
        M "Now, run along."
        scene bg HPCosplay78
        with fade
        R "What was that all about?"
        M "What?"
        R "You seemed really anxious to get rid of her."
        scene bg HPCosplay77
        with fade
        M "Did I?"
        scene bg HPCosplay78
        with dissolve
        M "I guess I just didn't want to leave you alone her with such a hussy."
        R "Mom! You shouldn't say that about one of your students!"
        scene bg HPCosplay79
        with dissolve
        M "Well, when she blackmails me to do such a slutty photo shoot, and then basically offers to have sex with you in the utility closet..."
        R "Is that what she was offering?"
        scene bg HPCosplay77
        with dissolve
        M "Oh... [ryan]. You can be so dense sometimes."
        R "Damnit! What if I wanted to meet her in the utility closet then?"
        R "I'm not going to lie, I'm feeling really backed up after that photo shoot."
        R "I would have loved to have Megan's help to give me some relief!"
        scene bg HPCosplay79
        with dissolve
        M "Megan's not the kind of girl that I want you getting that kind of relief from."
        R "Well, what kind of girl would you want me to get that kind of relief from?"
        scene bg HPCosplay78
        with dissolve
        M "Someone who loves you, cares about you, a girl who is kind..."
        M "If you found someone like your sisters, I would be very happy."
        RT "{i}She might just be pleasently surprised then, when she finds out.{/i}"
        R "How about someone like you?"
        scene bg HPCosplay77
        with dissolve
        M "Oh God, [ryan]!"
        M "When is this Oedipal phase going to end?"
        R "I'm not in an Oedipal phase!"
        scene bg HPCosplay78
        with dissolve
        M "Oh, really?"
        M "How do you explain all the boner hugs? How do you explain what's been going on in my office, or the bathroom, or when you were spying on me at the club?"
        R "I just take opportunities when I see them."
        M "Ahhh... So you're an opportunist."
        R "I guess."
        M "That's not a great thing to be."
        M "And since I guess you aren't in an Oedipal phase, I won't have to offer you what I was about to offer you."
        MT "{i}But how am I going to deal with my Jocasta phase?{/i}"
        R "Wait! What offer?"
        scene bg HPCosplay77
        with dissolve
        M "If you're not in a Oedipal phase, then I don't know why you need to hear it."
        MT "{i}Holy shit! I'm being super manipulative right now!{/i}"
        MT "{i}This is my son I'm talking to.{/i}"
        MT "{i}My son who just saw the most intimate parts of my body...{/i}"
        MT "{i}What is wrong with me?{/i}"
        MT "{i}Stop thinking about him staring at you with such lust in his eyes.{/i}"
        MT "{i}Goddammit!{/i}"
        "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
        $ momlibido += 1
        scene bg HPCosplay78
        with dissolve
        R "Well... Maybe I am kind of stuck in a minor Oedipal phase..."
        M "Oh... So you're saying you want to hear my offer?"
        R "Please?"
        scene bg HPCosplay77
        with dissolve
        MT "{i}Don't do it, [mom_name]!{/i}"
        M "Well... I was simply going to offer you some relief from the intense sexual situation you've been in all evening."
        MT "{i}Damnit! You did it...{/i}"
        R "What kind of relief?"
        MT "You know... Like what we do in the bathroom every Saturday, when you pay my Mafia debt."
        R "Oh... Well, I already get that taken care of when I need it..."
        R "How can I progress in my Oedipal phase if nothing else is progressing."
        scene bg HPCosplay79
        with dissolve
        M "Wait! Are you suggesting we do more?"
        M "I told you it wasn't going to go any further than a handjob!"
        R "Well, I don't want it to go much further... Just a little."
        M "And what do you mean by a little?"
        R "You know... Like use your mouth a little?"
        M "You want a blowjob!?"
        R "No!... no... just like a little bit of licking is all..."
        scene bg HPCosplay78
        with dissolve
        M "That's not just a little bit, [ryan]."
        M "Using the mouth is very intimate."
        R "Really, because the ones I've seen in pornos don't seem much more intimate than a handjob."
        R "In fact, they usually do both at the same time."
        R "Which has really left me wondering what it feels like."
        M "Hmmm... I understand..."
        MT "{i}No, you don't understand! This isn't healthy!... Don't encourage him any further.{/i}"
        M "Maybe... If it's only this once... I'll do just a little bit of licking."
        R "No way, Mom! You're the best!"
        MT "{i}God! I'm the worst!{/i}"
        MT "{i}What happened to my self-control?{/i}"
        MT "{i}It's like a horny demon has taken over my body!{/i}"
        scene bg HPCosplay79
        with dissolve
        MT "{i}Fuck you, [dad_name]! This is your fault!{/i}"
        MT "{i}How can I be expected to control myself when my very demanding sexual needs aren't being met?{/i}"
        MT "{i}You fucking criminal!{/i}"
        MT "{i}You deserve everything you get!{/i}"
        R "You ok, Mom?"
        scene bg HPCosplay77
        with dissolve
        M "I'm great! Let's do this!"
        RT "{i}Wow! That wasn't too hard.{/i}"
        play music SexMusic
        scene bg HPCosplay91
        with fade
        M "I've got to tell you that I'm really happy for you that you don't take after your dad in the dick size department."
        R "Who do I take after?"
        M "Well... you definitely got it from my dad."
        R "Grandpa's packing too?"
        M "Oh, yeah... He's the biggest I'd seen before I saw yours."
        R "So you've seen him erect?"
        M "Ummm... Yeah..."
        R "Really? I'd like to hear that story."
        M "Well... You're not going to."
        MT "{i}I'd better distract him.{/i}"
        scene HPCosplayVideo05
        with dissolve
        $ renpy.pause ()
        R "Oh, God! That feels good! What were we talking about?"
        MT "{i}Haha... I knew that would do the trick.{/i}"
        R "Wow! That feels just as good as I imagined it would."
        scene bg SleepBlack
        with fade
        scene bg HPCosplay87
        with fade
        MGT "{i}Oh, my God! I knew there was something more going on between the two of them!{/i}"
        MGT "{i}A handjob to overcome an Oedipal phase, maybe... But a blowjob! There's more than maybe either of them know.{/i}"
        MGT "{i}Ohhh... I can't keep my hand off my pussy though...{/i}"
        scene bg SleepBlack
        with fade
        play sound Blow03 loop
        scene HPCosplayVideo03
        with fade
        $ renpy.pause ()
        R "Oh my God, Mom!..."
        R "Hhhnnn..."
        R "You said you were only going to lick!"
        R "Not... That I'm... complaining."
        MT "{i}Oh, my God! I didn't even realize I did that!{/i}"
        MT "{i}My instincts just took over!{/i}"
        MT "{i}I can't tell him it was an accident, or he'll start to suspect how slutty my inner self really is.{/i}"
        R "Oh, God! This is too much! I'm gonna cum!"
        stop sound
        $ renpy.pause ()
        play sound Ejaculate
        scene bg HPCosplay92
        with fade
        $ renpy.pause ()
        scene bg HPCosplay95
        with dissolve
        $ renpy.pause ()
        scene bg SleepBlack
        with fade
        scene bg HPCosplay96
        with fade
        R "Oh my God, Mom! What was that?"
        M "I just decided that I needed to put my pride aside and do what's best for my boy..."
        M "We've got to get you out of that Oedipal phase."
        R "Wow! I was not expecting that!"
        R "Sorry I didn't last longer."
        scene bg HPCosplay97
        with dissolve
        M "Oh, don't worry about it! I don't care if you're quick when you're in my mouth."
        M "Now if you were in my pussy, that would be..."
        scene bg HPCosplay96
        with dissolve
        M "I mean!..."
        M "I think it's time to go home."
        R "Yeah... I've got to do some work on those photos before I can upload them to the intenet."
        M "God, I hope nobody I know finds those pics!"
        M "Let's hurry and clean up, and I'll meet you in the car."
        R "Oh, don't wait for me, it takes a little while to clean everything up."
        R "I'll just walk home."
        M "Are you sure?"
        R "Yeah, it's not far."
        M "Alright, I'll see you at home."
        scene bg SleepBlack
        with fade
        scene bg HPCosplay105
        with fade
        RT "{i}Oh, what a night! I can't believe Mom sucked me off.{/i}"
        scene bg HPCosplay106
        with dissolve
        MG "Boo!"
        R "AAAHHhhh! Holy shit, Megan!"
        R "You almost gave me a heart attack!"
        MG "Hahaha...."
        R "You've been waiting here this whole time?"
        scene bg HPCosplay107
        with fade
        MG "I have... And I've got to say that I saw some pretty interesting stuff."
        R "You were peeking?"
        MG "Oh, yeah... peeking and enjoying the show."
        R "Oh, God!"
        MG "Haha... Don't worry."
        MG "I was already almost positive that something like that was going on between your mom and you."
        MG "So that wasn't too surprising."
        R "Well... That there really isn't much going on... yet..."
        R "That was my first blowjob from her."
        R "And she says she's only doing it to help get me out of an Oedipal phase."
        MG "Whatevs, that was pretty hot!"
        MG "In fact, I couldn't help but enjoy myself a little while I was watching."
        MG "But I gotta say... [mom_name] was being kind of a bitch tonight."
        MG "After everything we went through together in that photo shoot, I was kind of hoping she would include me in anything you two did together."
        MG "She didn't want me touching her little boy."
        MG "So guess what?"
        MG "I'm here to touch her little boy."
        MG "I'll tell you what... Whatever you get [mom_name] to do to you... I'll do the same thing in return."
        R "Are you fucking serious?"
        MG "In fact, I'll do you one better. You get her to let me join the two of you... And I'll let you do whatever you want to me."
        MG "... So long as it doesn't put me in the hospital."
        R "I love the idea! But why would you be willing to do that?"
        MG "I don't know... I guess that kind of stuff just really pushes my buttons if you know what I mean."
        MG "Now, why don't I show you I'm serious by sucking your dick."
        MG "Assuming you can get it up again."
        MG "Pull down your pants, and let's see."
        scene bg HPCosplay84
        with fade
        MG "You're hard as a rock!"
        MG "Nice recovery time!"
        MG "I think I'll have a taste."
        scene HPCosplayVideo01
        with fade
        play sound Blow03 loop
        $ renpy.pause ()
        R "Mmmm...."
        RT "{i}I can't believe how much my life has changed!{/i}"
        RT "{i}I used to have zero luck with the ladies, and here I am getting a second blowjob for the night.{/i}"
        RT "{i}If given a choice between my old life of constant certainty and comfort, and this new life of constant fear and change.{/i}"
        RT "{i}I don't know if I'd change a thing. I've lived more since Dad went to prison, than I have in all my years up until now.{/i}"
        RT "{i}I'm beginning to crave the adventure...{/i}"
        RT "{i}And oh... This shit feels so good!{/i}"
        R "Megan! You're such a pro at this!"
        MG "Mmmmmmmm..."
        $ renpy.pause ()
        RT "{i}Ohhhh! I'm gonna cum!{/i}"
        stop sound
        $ renpy.pause ()
        play sound Ejaculate
        scene bg HPCosplay85
        with dissolve
        MG "Bllerrrgggghhh!!"
        scene bg HPCosplay86
        with fade
        MG "You asshole! You could have warned me."
        R "Sorry! I got lost in my thoughts for a little bit."
        MG "Thinking about your mom, huh?"
        R "No!... I was thinking about how crazy my life is, but still kinda good."
        MG "Is this a good part?"
        R "Yeah... it's a great part!"
        R "Thank you!"
        MG "You bet! And remember what I said about [mom_name]... I'm serious about it."
        R "Oh... I'll take you up on that!"
        MG "Haha... Ok, fellow pervert."
        MG "Let's go jump on that shitty scooter, and you can take me home."
        $ finished_hp_shoot = True
        $ mom_sucked_ryan = True
        play music Honey
        scene bg SleepBlack
        with fade
        jump posting_ph_pics
    else:
        scene bg HPCosplay74
        with fade
        R "Oh, my God! This is going to be my favorite picture."
        hide screen Points_screen_Mom_cosplay
        MT "{i}Haha... He's not kidding! Look how hard his dick is! There's no possible way to hide it. I'm sure Megan's noticed.{/i}"
        MT "{i}Poor boy... Those pants are so tight... it must be uncomfortable.{/i}"
        MT "{i}I'll bet when he takes these pics home, he's going to spend all night jacking off to them.{/i}"
        MT "{i}Because of Megan, of course!... Not me... I hope... don't I?... Shut up, brain!{/i}"
        MT "{i}But, that poor boy needs some relief!{/i}"
        MT "{i}I suppose I could help him out again.{/i}"
        if not finished_hp_shoot:
            "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
            $ momlibido += 1
        MT "{i}And if it helps him to get through this Oedipal phase!{/i}"
        MT "{i}Does that make sense?{/i}"
        MT "{i}Is my horny brain trying to justify any kind of sexual deviancy!{/i}"
        MT "{i}Fight it, [mom_name]!{/i}"
        MT "...."
        MT "{i}Still...{/i}"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay74
        R "And one quick close-up shot."
        scene bg HPCosplay100
        with fade
        R "Wow!"
        play sound CameraClick
        show CamaraFlash
        pause (0.25)
        scene bg HPCosplay100
        R "And that's it!"
        R "That was amazing, you two!"
        scene bg SleepBlack
        with fade
        scene bg HPCosplay75
        with fade
        M "Well, I hope that photo shoot was satisfactory for you."
        M "And I hope [ryan] was able to get all the shots he needed this time."
        MG "I don't mind coming back if he didn't!"
        scene bg HPCosplay76
        with fade
        MG "And thank you [ryan], for being such a good director and cameraman."
        MG "I'd love to reward you somehow... Maybe you can meet me in the utility closet and you can do me against the sink?"
        M "Ok, Megan, I see you're no longer being subtle. I think it's time for you to run along... [ryan] isn't going to be meeting you in the utility closet this time, either."
        MT "{i}You two-bit hussy.{/i}"
        MT "{i}I'll be taking care of him again.{/i}"
        MG "Can I take the scooter again?"
        R "Ummm, yeah..."
        M "Now, run along."
        scene bg HPCosplay78
        with fade
        R "You're trying to get rid of her of her again... Aren't you?"
        scene bg HPCosplay77
        with fade
        M "Am I?"
        scene bg HPCosplay78
        with dissolve
        M "I guess I just didn't want to leave you alone her with such a hussy."
        R "Mom! You shouldn't say that about one of your students!"
        scene bg HPCosplay79
        with dissolve
        M "Well, when she blackmails me to do such a slutty photo shoot, and then flat out offers to have sex with you in the utility closet..."
        R "She was just teasing."
        scene bg HPCosplay77
        with dissolve
        M "Oh... [ryan]. You can be so naive sometimes."
        R "Well, I wish she wasn't teasing, then I'd go meet her."
        R "I'm not going to lie, I'm feeling really backed up after that photo shoot."
        R "I would have loved to have Megan's help to give me some relief!"
        scene bg HPCosplay79
        with dissolve
        M "I still don't think Megan's the kind of girl that I want you getting that kind of relief from."
        R "I know! Look for girls like my sisters."
        R "Or someone like you."
        scene bg HPCosplay77
        with dissolve
        M "Oh God, [ryan]!"
        M "We've still got a lot of work to do."
        MT "{i}What are you doing? You said it was only going to be one time!{/i}"
        MT "{i}This is my son I'm talking to.{/i}"
        MT "{i}My son who just saw the most intimate parts of my body...{/i}"
        MT "{i}What is wrong with me?{/i}"
        MT "{i}Stop thinking about him staring at you with such lust in his eyes.{/i}"
        MT "{i}Goddammit!{/i}"
        "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
        $ momlibido += 1
        scene bg HPCosplay78
        with dissolve
        R "Well... I might be a little better than last time, but I am kind of stuck in a minor Oedipal phase..."
        M "Oh... So you're saying you need some more relief?"
        R "Please?"
        scene bg HPCosplay77
        with dissolve
        MT "{i}Don't do it, [mom_name]!{/i}"
        M "How could I say no to that face."
        MT "{i}Damnit! You did it...{/i}"
        MT "{i}What happened to my self-control?{/i}"
        MT "{i}It's like a horny demon has taken over my body!{/i}"
        scene bg HPCosplay79
        with dissolve
        MT "{i}Fuck you, [dad_name]! This is your fault!{/i}"
        MT "{i}How can I be expected to control myself when my very demanding sexual needs aren't being met?{/i}"
        MT "{i}You fucking criminal!{/i}"
        MT "{i}You deserve everything you get!{/i}"
        R "You ok, Mom?"
        scene bg HPCosplay77
        with dissolve
        M "I'm great! Let's do this!"
        RT "{i}Wow! Even easier this time!{/i}"
        play music SexMusic
        scene bg HPCosplay91
        with fade
        M "I know I said it before, but I'm really happy for you that you don't take after your dad in the dick size department."
        R "Are you thinking about Grandpa's package again?"
        R "I still want to hear the story about you seeing him erect."
        M "Well... You're not going to."
        MT "{i}I'd better distract him.{/i}"
        scene HPCosplayVideo05
        with dissolve
        $ renpy.pause ()
        R "Oh, God! That feels good! What were we talking about?"
        MT "{i}Haha... every time!{/i}"
        R "Wow! That feels so good."
        scene bg SleepBlack
        with fade
        scene bg HPCosplay87
        with fade
        MGT "{i}They're at it again!{/i}"
        MGT "{i}I was hoping they'd do a little more this time.{/i}"
        MGT "{i}Still... I can't complain too much.{/i}"
        MGT "{i}Ohhh... I can't keep my hand off my pussy though...{/i}"
        scene bg SleepBlack
        with fade
        play sound Blow03 loop
        scene HPCosplayVideo03
        with fade
        $ renpy.pause ()
        R "Oh my God, Mom!..."
        R "Hhhnnn..."
        R "Oh, God! This is too much! I'm gonna cum!"
        stop sound
        $ renpy.pause ()
        play sound Ejaculate
        scene bg HPCosplay92
        with fade
        $ renpy.pause ()
        scene bg HPCosplay95
        with dissolve
        $ renpy.pause ()
        scene bg SleepBlack
        with fade
        scene bg HPCosplay96
        with fade
        R "Oh my God, Mom! That was just as good as last time!"
        R "Sorry I didn't last longer."
        scene bg HPCosplay97
        with dissolve
        M "I know honey... You'll get better with time."
        scene bg HPCosplay96
        with dissolve
        M "I think it's time to go home."
        R "Yeah... I've got to do some work on those photos before I can upload them to the intenet."
        M "God, I hope nobody I know finds those pics!"
        M "Let's hurry and clean up, and I'll meet you in the car."
        R "Oh, don't wait for me, it takes a little while to clean everything up."
        R "I'll just walk home again."
        M "Are you sure?"
        R "Yeah, it's not far."
        M "Alright, I'll see you at home."
        scene bg SleepBlack
        with fade
        scene bg HPCosplay105
        with fade
        RT "{i}Oh, what a night! I can't believe Mom sucked me off again!{/i}"
        scene bg HPCosplay106
        with dissolve
        MG "Boo!"
        R "AAAHHhhh! Holy shit, Megan!"
        R "I can't believe I let you get me again!"
        MG "Hahaha...."
        R "I didn't think you'd stick around again."
        scene bg HPCosplay107
        with fade
        MG "Well... I didn't want to miss your encore performance."
        R "Oh, God!"
        MG "Haha... I know... That was cheesy."
        MG "I gotta say though, that was pretty hot!"
        MG "In fact, I couldn't help but enjoy myself a little while I was watching."
        MG "But I gotta say... [mom_name] is still acting pretty bitchy."
        MG "After everything we went through together in that photo shoot, when are you going to get her to include me?"
        R "I'm working on it."
        MG "So, a deal's a deal."
        MG "A blowjob for a blowjob."
        MG "Assuming you can get it up again."
        MG "Pull down your pants, and let's see."
        scene bg HPCosplay84
        with fade
        MG "You're hard as a rock!"
        MG "You've got a lot of stamina!"
        MG "I've got to taste it again."
        scene HPCosplayVideo01
        with fade
        play sound Blow03 loop
        $ renpy.pause ()
        R "Mmmm...."
        R "Megan! You're such a pro at this!"
        MG "Mmmmmmmm..."
        $ renpy.pause ()
        RT "{i}Ohhhh! I'm gonna cum!{/i}"
        stop sound
        $ renpy.pause ()
        play sound Ejaculate
        scene bg HPCosplay85
        with dissolve
        MG "Bllerrrgggghhh!!"
        scene bg HPCosplay86
        with fade
        MG "You asshole! You could have warned me this time!"
        R "Sorry! I got lost in my thoughts for a little bit."
        MG "Thinking about your mom, huh?"
        R "No!... maybe..."
        R "Still thinking about how even though life is hard, there's some really good parts to it."
        MG "And this is still a good part?"
        R "Yeah... it's still a great part!"
        R "Thank you!"
        MG "You bet! And remember what I said about [mom_name]... I'm still serious about it."
        R "Oh... I'll take you up on that!"
        MG "Haha... Ok, fellow pervert."
        MG "Let's go jump on that shitty scooter, and you can take me home."
        play music Honey
        scene bg SleepBlack
        with fade
        jump posting_ph_pics

label ph_recap_end:                     #### Edited ####
    scene bg HPCosplay50
    with dissolve
    PM "I've got to do something about this!"
    scene bg HPCosplay51
    with dissolve
    PM "That's better! Edgy and sexy!"
    scene bg HPCosplay52
    with fade
    PMT "{i}So she thinks she's Moldy's top minion? I'll show her.{/i}"
    PMT "{i}She won't know what hit her.{/i}"
    PM "Alright, you slutty flea-bottom mudblood!"
    PM "Get on the floor and show me some respect before I {i}Avada Kedavra{/i} you into next week."
    HG "Uhhh... Yes... Professor."
    PM "Call me Mistress, and lick those boots clean while you're down there."
    scene bg HPCosplay55
    with fade
    PMT "{i}That was easier than I thought it would be... Maybe Hermione is a natural submissive.{/i}"
    PM "That's right, get them clean!"
    PMT "{i}Now it's time to see just how obedient she will be.{/i}"
    PM "Do you really think that uniform is to standard? That slutty shirt will get you two hundred points from Griffendor."
    scene bg HPCosplay60
    with fade
    PM "You like dressing like a slut, do you?"
    PM "Then why not do it right?"
    PM "And just so the lesson sinks in..."
    scene bg HPCosplay61
    with fade
    PM "And now you will write lines until I tell you to stop."
    HG "But, how can I write lines with my hands tied?"
    scene bg SleepBlack
    with fade
    scene bg HPCosplay62
    with fade
    PM "That's right! I want you to write \"I will not dress slutty.\" one hundred times!"
    scene bg HPCosplay63
    with fade
    PM "And while you're doing that... I think I'll help myself to some eye candy."
    scene bg HPCosplay64
    with dissolve
    HG "You perverted bitch! Get your hands off my dress!"
    PM "Oh... You think it's ok to talk to your professor like that?"
    HG "I'll talk to you however I want, you STD encrusted flobberworm!"
    scene bg HPCosplay65
    with fade
    HG "You ugly... Aaahhh!"
    scene bg HPCosplay66
    with fade
    play sound Muffled
    HG "MMMmmmmmrrrmmmpphhh!..."
    stop sound
    HGT "{i}Oh, shit! What have I done?{/i}"
    PM "That's right bitch, now if you know what's good for you, you'll come sit on the floor at my feet like the bitch you are."
    scene bg HPCosplay67
    with fade
    PMT "{i}Hahaha... I think I've got her to where she'll do whatever I say.{/i}"
    PM "Let's just test your obedience my little pet bitch."
    PM "Come bend over the desk."
    scene bg HPCosplay68
    with fade
    PM "Ohhh... That is a pretty little ass."
    scene bg HPCosplay69
    with fade
    PM "But these are getting in the way."
    scene bg HPCosplay70
    with fade
    PM "Oh, my!... You've been a good little girl."
    PM "Not a single whipping mark."
    scene bg HPCosplay71
    with fade
    PM "Well, that's about to change."
    play sound Slap
    scene bg HPCosplay72
    with dissolve
    play sound Muffled
    $ renpy.pause ()
    scene bg HPCosplay71
    with dissolve
    $ renpy.pause ()
    stop sound
    play sound Slap
    scene bg HPCosplay72
    with dissolve
    play sound Muffled
    $ renpy.pause ()
    scene bg HPCosplay71
    with dissolve
    $ renpy.pause ()
    stop sound
    play sound Slap
    scene bg HPCosplay72
    with dissolve
    play sound Muffled
    $ renpy.pause ()
    stop sound
    scene bg HPCosplay73
    with fade
    PM "And now, you'll be completely obedient to your mistress, won't you?"
    scene bg SleepBlack
    with fade
    scene bg HPCosplay104
    with fade
    MG "And that's where we left off."
    R "Wow! You're a great storyteller. I felt like I was in the story."
    R "And now I think we only need one more shot."
    R "Hmmmm... last one... what should we have you do?"
    menu:
        "We need a really good full nudity shot. {i}(submission 25+){/i}":
            if momsubmission >= 25:
                if blackmailed_mom_matt:
                    R "The only type of shot we're missing now, is a shot with both of you completely naked."
                    R "Mom? Do you think you're ready for a full nudity shot?"
                    M "Yeah... Anything to end this photo shoot and do what I need to protect our family."
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    M "Is this really our last pose?"
                    MB "Yeah... Unless you want to do more."
                    M "God, no!"
                    MB "Haha... Then after this, I promise we'll be done."
                    MB "So, for this shot I want Megan to get on her knees, with her ass pointing towards the camera."
                    MB "Then Miss [mom_name], I want you to lose your panties, and then go ahead and sit on Megan's ass. That we we get a good shot of both your goods."
                    M "Our goods?"
                    MB "Or... Whatever you want to call them."
                else:
                    R "The only type of shot we're missing now, is a shot with both of you completely naked."
                    R "Mom? Do you think you're ready for a full nudity shot?"
                    M "Yeah... Anything to end this photo shoot and do what I need to protect our family."
                    if not finished_hp_shoot:
                        "{i}{b}\"Mom's Submission +1\"{/b}{/i}"
                        $ momsubmission += 1
                    if finished_hp_shoot == False and weekly_hp_complete == False:
                        $ photoshoot_kinky += 1
                    M "Is this really our last pose?"
                    R "Yeah... Unless you want to do more."
                    M "God, no!"
                    R "Haha... Then after this, I promise we'll be done."
                    R "So, for this shot I want Megan to get on her knees, with her ass pointing towards the camera."
                    R "Then Mom, I want you to lose your panties, and then go ahead and sit on Megan's ass. That we we get a good shot of both your goods."
                    M "Our goods?"
                    R "Or... Whatever you want to call them."
                M "... I guess goods is fine."
                jump no_panties_shot
            else:
                R "The only type of shot we're missing now, is a shot with both of you completely naked."
                R "Mom? Are you ready for a full nudity shot?"
                M "I'm sorry... I just can't."
                R "Really? We're so close to finishing the photo shoot. We just need one more shot."
                M "I'm not in the mood, [ryan]!"
                R "Come on... Let's just get it over with really quick and then we can all be done."
                M "[ryan]! If you push any harder, then I'm not ever coming back to finish it ever!"
                "{i}{b}\"Mom's Anger +5\"{/b}{/i}"
                $ momanger += 5
                RT "{i}Damnit! We're so close! I guess we'll just have to come back one more time.{/i}"
                scene bg SleepBlack
                with fade
                "To get Mom to pose totally nude with Megan, you need her submission points at 25."
                hide screen Points_screen_Mom_cosplay
                jump posting_the_wr_pics
        "Maybe we should end the shoot for today.":
            if blackmailed_mom_matt:
                scene bg HPCosplay56
                with fade
                R "I don't think we need to take any more pics today."
                MB "Really? We haven't taken very many."
                R "Yeah, but the ones we have are really good, and the only way they could be better is if we pushed the girls into something they might not be comfortable with."
                scene bg HPCosplay58
                with dissolve
                M "Oh, [ryan]! You really do act like a professional photographer."
                M "And that wasn't nearly as bad as I thought it would be!"
                M "And even though I'm being coerced into this, you both helped me feel pretty comfortable!"
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Mom's Libido +5\"{/b}{/i}"
                    $ momaffection += 1
                    $ momlibido += 5
                M "The next photo shoot might not make me feel so uneasy now."
                M "I might be even more daring, and be willing to show a little more skin... maybe..."
                MB "Great! I can't wait!"
                RT "{i}Ugghh... I wish Matt wasn't going to be there.{/i}"
            else:
                scene bg HPCosplay56
                with fade
                R "I don't think we need to take any more pics today."
                MG "Really? We haven't taken very many."
                R "Yeah, but the ones we have are really good, and the only way they could be better is if we pushed the girls into something they might not be comfortable with."
                scene bg HPCosplay58
                with dissolve
                M "Oh, [ryan]! You really do act like a professional photographer."
                M "And that wasn't nearly as bad as I thought it would be!"
                M "And even though I'm being coerced into this, you both helped me feel pretty comfortable!"
                if not finished_hp_shoot:
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Mom's Libido +5\"{/b}{/i}"
                    $ momaffection += 1
                    $ momlibido += 5
                M "The next photo shoot might not make me feel so uneasy now."
                M "I might be even more daring, and be willing to show a little more skin... maybe..."
                MG "Great! I can't wait!"
                RT "{i}Neither can I... I just need to be careful about pushing Mom too hard, and too fast... That's what she said.{/i}"
            R "You can get changed and I'll see you back home."
            hide screen Points_screen_Mom_cosplay
            jump posting_the_wr_pics

label wr_sex_event:                     #### Edited 9-2-2020 ####
    R "Hmmm..."
    menu:
        "Blowjob":
            R "Let's celebrate with our traditional post-photoshoot blowjob."
            S "Since when is it a tradition?"
            R "Oh, just since I decided that it would be the best tradition ever!"
            S "Hahah... [ryan], you're such a goober!"
            S "Fine, I could use some more practice anyways."
            R "Practice for whom?"
            S "Hahaha wouldn't you like to know?..."
            R "Yes!... I really would!..."
            S "..."
            R "Who, Sidney?..."
            S "..."
            scene bg SidneyWRShoot55
            with dissolve
            S "Let's just give this little guy some attention!"
            S "Oh, not little... he's big already!"
            scene bg SidneyWRShoot56
            with fade
            R "... Ohhhh... what was I saying?..."
            S "{i}Hahaha... that did the trick...{/i}"
            S "Let's see if this is any easier."
            S "My jaw's still a little tired from last time."
            scene bg SidneyWRShoot57
            with dissolve
            ST "{i}Oh, my God!... I'm getting as needy for this as [ryan]!...{/i}"
            scene bg SidneyWRShoot58 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot59 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            play sound Blow03 loop
            scene bg SidneyWRShoot60 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot61 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            S "{i}\"Bleurghch\"{/i}"
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot63 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot61 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            R "Oh my God, Sidney... this feels even better than last time! You're getting so good at this!"
            ST "{i}Oh... he's so sweet!{/i}"
            scene bg SidneyWRShoot63 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot61 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot63 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot61 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            S "{i}\"Schhhhluurrrrp\"{/i}"
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot63 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot61 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot63 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot61 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot63 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot61 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot63 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            RT "{i}I can't hold out any longer! I'm going to cum!{/i}"
            scene bg SidneyWRShoot61 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            RT "{i}I'm going to cum right down Sidney's throat again!{/i}"
            scene bg SidneyWRShoot63 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            RT "{i}That's so wrong!...{/i}"
            scene bg SidneyWRShoot61 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot62 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            RT "{i}But soooooo... hot!!... !!{/i}"
            scene bg SidneyWRShoot63 with Dissolve(0.3)
            $ renpy.pause (0.1, hard=True)
            scene bg SidneyWRShoot64
            with dissolve
            stop sound
            play sound Ejaculate
            S "Mmmmmphhhhh..."
            scene bg SidneyWRShoot65
            with dissolve
            play sound Ejaculate
            S "MMMMmmmmmmmmmmmmmmmmmphhhhhhhhhhhh!!!!!..."
            scene bg SidneyWRShoot66
            with dissolve
            play sound Ejaculate
            S "Bleeeeeeeeurghhhhhhhhhhhhhch!!!!..."
            scene bg SidneyWRShoot67
            with dissolve
            play sound Gasp
            S "[ryan]!!... Why did you force me to swallow again?!"
            play sound WomanBreath
            R "I'm sorry!... I wasn't thinking!..."
            R "It's like my brain just shuts off when I'm about to cum."
            R "And again, I just reacted without thinking..."
            R "I'm so sorry!..."
            S "{i}(pant... pant)...{/i}... well... {i}(pant... pant){/i}... you've got to figure out... {i}(pant... pant){/i}..."
            S "How to control... {i}(pant... pant){/i}... yourself... {i}(pant... pant){/i}..."
            R "I promise, I'll try to remember next time."
            S "Ohhh... you say that every time... I need to lie down and catch my breath..."
            stop sound
            scene bg SidneyWRShoot69
            with fade
            S "Wow!... I'm getting pretty good at that aren't I?..."
            "{i}{b}\"Sidney's Libido +10\"{/b}{/i}"
            $ sidneylibido += 10
            R "Holy shit, yes!..."
            S "I can't even believe how far I'm able to get that huge dick down my throat."
            R "Now you're just trying to flatter me."
            S "Haha... you dipwad!"
            R "Haha... what?..."
            scene bg SidneyWRShoot69
            with dissolve
            S "Well, I'm going to go get dressed, and head back to the house."
            R "K, and I'll stay and clean things up a bit, and I'll see you soon!"
            S "See ya later, [ryan]!"
            jump posting_the_wr_pics
        "Sex":
            R "I can't stop thinking about the last time we did it... and seeing you dressed like this... well... I've been dying to do it again!"
            S "Do what?"
            R "... ummm, have sex."
            S "Hahaha... I know, dipshit!"
            S "Hmmm... these photoshoots do get me pretty tired... but pretty turned on at the same time."
            S "Alright... I'm in!"
            scene bg SleepBlack
            with fade
            scene bg WRSex01
            with fade
            S "Let's fuck doggystyle... it really rubs my g-spot just right."
            S "Though... I suppose your dick is so big it rubs every spot inside there."
            S "I still can't believe I can even take it at all."
            R "Speaking of taking it all..."
            S "Yeah?"
            menu:
                "Ask for anal sex.":
                    R "How would you feel about trying some butt stuff?"
                    scene bg WRSex02
                    with dissolve
                    S "Really, [ryan]?"
                    S "We're fucking brother and sister!... We shouldn't even be fucking at all!"
                    S "And still you're not satisfied?"
                    S "You've got to try and push this to the limits of depravity?"
                    S "Why don't you try shoving something as big as your dick up your own ass!"
                    S "When you can take it all, then we can maybe talk about it."
                    S "But for now... I'm just going to go get dressed and head home..."
                    "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
                    $ sidneylibido -= 5
                    scene bg SleepBlack
                    with fade
                    RT "{i}Well, shit! That didn't go over very well... but she's right... I'm not satisfied!{/i}"
                    RT "{i}I need to fuck that sexy ass!{/i}"
                    WT "Sorry, [ryan]... Not in this update.  But hopefully soon!"
                    RT "{i}Damnit!{/i}"
                    jump posting_the_wr_pics
                "Never mind, I better not":
                    R "Never mind... forget about it."
                    S "What?"
                    R "No... it's nothing."
                    S "Ok..."
                    R "Let's just have some fun."
                    scene bg WRSex03
                    with fade
                    R "Your ass is so sexy, Sidney!"
                    S "Would you stop making small talk and stick it in already!"
                    scene bg WRSex04
                    with dissolve
                    S "Oh, fuck!... I meant gently!"
                    R "Sorry!"
                    S "Wow!... That dick is so big!... I'm never quite prepared for how much it's gonna stretch out my pussy."
                    R "Are you ok?"
                    S "Yeah... I'm good now... I'm ready for some proper fucking."
                    play sound Sidney01
                    scene WRSexVideo01
                    with dissolve
                    $ renpy.pause ()
                    S "Ohhh... I feel so full!"
                    S "You're stretching my pussy so much!"
                    scene WRSexVideo02
                    with fade
                    $ renpy.pause ()
                    S "Ohhh... fuck!"
                    S "I shouldn't enjoy fucking my brother so much!"
                    R "Thanks Sid... I love fucking you too!"
                    S "Shut up and keep fucking me!"
                    $ renpy.pause ()
                    S "Oh, my God! I'm gonna cum!"
                    stop sound
                    play sound Ejaculate
                    scene bg WRSex10
                    with fade
                    R "Holy shit, Sidney!"
                    S "AAAHhhhhh..."
                    scene bg WRSex09
                    with fade
                    R "You're like a fucking fire hose!"
                    S "Hhhnnnnggghhhh..."
                    S "Oh, wow!... That was!... Give me that dick!"
                    scene WRSexVideo02
                    with dissolve
                    $ renpy.pause ()
                    R "Ohhh... this feels so good!"
                    R "I love the way your pussy squeezes my cock!"
                    scene WRSexVideo01
                    with fade
                    $ renpy.pause ()
                    R "Aaaahh..."
                    R "I'm getting really close!"
                    $ renpy.pause ()
                    R "Oh, fuck! I'm gonna cum!"
                    menu:
                        "Cum inside.":
                            R "Sidney... I'm going to..."
                            stop sound
                            play sound Ejaculate
                            scene bg WRSex05
                            with fade
                            with hpunch
                            S "Oh, God! There's no room for all that cum with your dick in there!"
                            S "It's stretching my womb!"
                            "{i}\"[ryan]'s cumloads in Sidney's pussy +1\"{/i}"
                            $ sidney_cum_loads_counter += 1
                            "{i}\"Total loads of [ryan]'s cum in Sidney's pussy = ([sidney_cum_loads_counter])\"{/i}"
                            scene bg SleepBlack
                            with fade
                            "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
                            $ sidneylibido -= 5
                        "Cum on her ass and back.":
                            R "Sidney... I'm going to..."
                            stop sound
                            play sound Ejaculate
                            scene bg WRSex06
                            with fade
                            with hpunch
                            R "Fuuuuck!..."
                            play sound Ejaculate
                            scene bg WRSex07
                            with dissolve
                            with vpunch
                            R "I'm cuuummmiing!"
                            scene bg WRSex08
                            with dissolve
                            S "Oh my God, [ryan]!"
                            S "You covered me!"
                            scene bg SleepBlack
                            with fade
                            "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
                            $ sidneylibido -= 5
                    scene bg WRSex08
                    with fade
                    S "Wow!... I'm getting pretty good at that aren't I?..."
                    R "Holy shit, yes!..."
                    S "I still can't even believe how far I'm able to get that huge dick into my pussy."
                    R "Now you're just trying to flatter me."
                    S "Haha... you dipwad!"
                    R "Haha... what?..."
                    S "Well, I'm going to go get dressed, and head back to the house."
                    R "K, and I'll stay and clean things up a bit, and I'll see you soon!"
                    S "See ya later, [ryan]!"
                    $ persistent.gal_Sidney_08 = True
                    $ had_wr_sex = True
                    jump posting_the_wr_pics

#############  PARK  ########################################  PARK  ###########################################################

label park_sex:                         #### Edited 9-2-2020 ####
    play music SexMusic
    R "What if we were to... ?"
    S "What?"
    R "You know... to have..."
    S "Sex? Here in the park?"
    S "Where anybody could catch us?"
    S "Where someone we know could come walking by and see me fucking my brother?"
    S "I love it!"
    S "Hmmm... but I don't think we could get away with that one on the park bench, without someone calling the cops."
    S "Let's go to the usual spot."
    S "Follow me."
    scene bg SidneyRun86
    with fade
    R "Ok, the coast is clear. Let's go."
    scene bg SidneyRun87
    with fade
    R "What if someone walks in on us while..."
    S "Shhhh..."
    S "We'll deal with that when it happens."
    R "You mean *if* it happens."
    S "Yes... of course."
    R "But, what if it's someone we know?"
    S "Do you want to talk, or do you want to fuck me?"
    R "Uhhh... fuck you, please."
    S "Haha... that's what I thought."
    scene bg SleepBlack
    with fade
    play sound Sidney01
    $ renpy.pause ()
    scene RunSexVideo01
    with fade
    $ renpy.pause ()
    R "I can't believe we're having sex... In such a public place."
    S "Oh, fuck!... I know... Isn't it... so HOT!"
    R "Holy shit, Sidney! Your pussy is just dripping wet!"
    S "Aaahhh... I... know... I just get so... turned on by... the thought of getting... caught!"
    S "Shit!... I'm about to cum!"
    S "Aaaaahhh..."
    stop sound
    play sound Ejaculate
    scene bg RunSex05
    with fade
    $ renpy.pause ()
    R "Holy fuck, Sidney!"
    R "You just soaked my feet!"
    S "Hhhnnnnggghhhh!..."
    S "Oh, God! Put that cock back in me!"
    scene RunSexVideo01
    with fade
    $ renpy.pause ()
    R "Wow ,Sidney!..."
    R "I can't believe how turned on you are!"
    S "Just shut up and keep fucking me!"
    $ renpy.pause ()
    R "Ohhh..."
    R "Fuck!..."
    R "I'm about to..."
    menu:
        "Cum inside.":
            R "Sidney... I'm going to..."
            stop sound
            play sound Ejaculate
            scene bg RunSex01
            with fade
            with hpunch
            S "Oh, God! I can feel it expanding my womb!"
            "{i}\"[ryan]'s cumloads in Sidney's pussy +1\"{/i}"
            $ sidney_cum_loads_counter += 1
            "{i}\"Total loads of [ryan]'s cum in Sidney's pussy = ([sidney_cum_loads_counter])\"{/i}"
            scene bg SleepBlack
            with fade
            "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
            $ sidneylibido -= 5
        "Cum on her ass and back.":
            R "Sidney... I'm going to..."
            stop sound
            play sound Ejaculate
            scene bg RunSex02
            with fade
            with hpunch
            R "Fuuuuck!..."
            play sound Ejaculate
            scene bg RunSex03
            with dissolve
            with vpunch
            R "I'm cuuummmiing!"
            scene bg RunSex04
            with dissolve
            S "Oh my God, [ryan]!"
            S "You covered me!"
            scene bg SleepBlack
            with fade
            "{i}{b}\"Sidney's Libido -5\"{/b}{/i}"
            $ sidneylibido -= 5
    scene bg SidneyRun57
    with fade
    $ renpy.pause ()
    S "Guess what..."
    R "What?"
    S "Haha... every stride I take forces more cum out of my pussy, and into my shorts!"
    R "Shit, Sidney! Stop talking like that or I'm going to have to fuck you when we get home too."
    S "Hahaha... not if you can't catch me!"
    scene bg RunSex06
    with fade
    R "Damnit!"
    R "Sidney, wait!"
    scene bg SleepBlack
    with fade
    play music Honey
    $ persistent.gal_Sidney_09 = True
    $ had_park_sex = True
    $ timeofdaycounter += 1
    jump myroom
