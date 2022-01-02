
define audio.Punch = "music/Punch.wav"
define audio.Muffled = "music/Muffled.wav"
define audio.WaterLeak = "music/WaterLeak.wav"
define audio.Gulp = "music/Gulp.wav"

define CM = Character(_("Crazy Old Man"), color="FFFAF0", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define CMT = Character(_("Crazy Old Man's Thoughts"), color="FFFAF0", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define MP = Character(_("Mr. Peterson"), color="FFFAF0", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define MPT = Character(_("Mr. Peterson's Thoughts"), color="FFFAF0", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define P = Character(_("Policeman"), color="3366FF", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define MS = Character(_("Mrs. Stone"), color="3366FF", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])
define A = Character(_("Armani"), color="FF3300", who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])

define fixed_bulb = False
define fixed_sink = 0
define fixed_washer = 0
define sink_option = 0
define first_park_run = False
define physical_fitness = 0
define sidneys_running = False
define groped_in_park = 0
define fit_enough = False
define mp_captured = False
define mp_cockblock = False
define cop_block = False
define park_finger = False
define park_hj = False
define park_pussy_eat = False
define park_bj = False
define park_full_menu = False
define club_tip = False
define club_deeper = False
define club_throat = False
define more_club_bjs = False
define sidney_took_job = False
define sidneys_working = False
define sidney_worked_late = 0
define first_bar_convo = False
define first_mafia_chat = False
define first_money_chat = False
define first_club_fun = False
define chose_joey = False
define chose_armani = False
define visited_sid = False
define club_fun_counter = 0
define watched_with_Diaz = True
define first_diaz_convo = False
define sidney_spy = False
define sidney_money = 0
define tv_events = 0
define first_bfast = False
define finger_bfast = False
define convention_bfast = False
define htbyd_bfast = False
define pool_bfast = False
define wr_bfast = False
define ntrclub_bfast = False
define sixty_nined_bfast = 0
define camille_bfast = False
define first_bath_hjob = False
define mom_CreepShot_06 = False
define monday_sid_worked = False

init:

    image SidneyRunVideo01 = Movie(play="video/SidneyRunVideo01.webm", start_image="images/SidneyRunVideo01F01.webp")
    image SidneyRunVideo02 = Movie(play="video/SidneyRunVideo02.webm", start_image="images/SidneyRunVideo02F01.webp")
    image SidneyRunVideo03 = Movie(play="video/SidneyRunVideo03.webm", start_image="images/SidneyRunVideo03F01.webp")
    image SidneyRunVideo04 = Movie(play="video/SidneyRunVideo04.webm", start_image="images/SidneyRunVideo04F01.webp")
    image SidneyRunVideo05 = Movie(play="video/SidneyRunVideo05.webm", start_image="images/SidneyRunVideo05F01.webp")
    image SidClubVideo01 = Movie(play="video/SidClubVideo01.webm", start_image="images/SidClubVideo01F01.webp")
    image SidClubVideo02 = Movie(play="video/SidClubVideo02.webm", start_image="images/SidClubVideo02F01.webp")
    image SidClubVideo03 = Movie(play="video/SidClubVideo03.webm", start_image="images/SidClubVideo03F01.webp")
    image SidClubVideo04 = Movie(play="video/SidClubVideo04.webm", start_image="images/SidClubVideo04F01.webp")
    image SidClubVideo05 = Movie(play="video/SidClubVideo05.webm", start_image="images/SidClubVideo05F01.webp")
    image SidClubVideo06 = Movie(play="video/SidClubVideo06.webm", start_image="images/SidClubVideo06F01.webp")
    image SidClubVideo07 = Movie(play="video/SidClubVideo07.webm", start_image="images/SidClubVideo07F01.webp")
    image SidClubVideo08 = Movie(play="video/SidClubVideo08.webm", start_image="images/SidClubVideo08F01.webp")
    image GOTVideo01 = Movie(play="video/GOTVideo01.webm", start_image="images/GOTVideo01F01.webp")
    image GOTVideo02 = Movie(play="video/GOTVideo02.webm", start_image="images/GOTVideo02F01.webp")
    image GOTVideo03 = Movie(play="video/GOTVideo03.webm", start_image="images/GOTVideo03F01.webp")
    image GOTVideo04 = Movie(play="video/GOTVideo04.webm", start_image="images/GOTVideo04F01.webp")
    image GOTVideo05 = Movie(play="video/GOTVideo05.webm", start_image="images/GOTVideo05F01.webp")
    image GOTVideo06 = Movie(play="video/GOTVideo06.webm", start_image="images/GOTVideo06F01.webp")
    image GOTVideo07 = Movie(play="video/GOTVideo07.webm", start_image="images/GOTVideo07F01.webp")
    image GOTVideo08 = Movie(play="video/GOTVideo08.webm", start_image="images/GOTVideo08F01.webp")
    image GOTVideo09 = Movie(play="video/GOTVideo09.webm", start_image="images/GOTVideo09F01.webp")
    image MafiaPaidVideo01 = Movie(play="video/MafiaPaidVideo01.webm", start_image="images/MafiaPaidVideo01F01.webp")
    image LaundryVideo01 = Movie(play="video/LaundryVideo01.webm", start_image="images/LaundryVideo01F01.webp")
    image ClubStripVideo01 = Movie(play="video/ClubStripVideo01.webm", start_image="images/ClubStripVideo01F01.webp")
    image ClubStripVideo02 = Movie(play="video/ClubStripVideo02.webm", start_image="images/ClubStripVideo02F01.webp")
    image NTRStripVideo01 = Movie(play="video/NTRStripVideo01.webm", start_image="images/NTRStripVideo01F01.webp")
    image NTRStripVideo02 = Movie(play="video/NTRStripVideo02.webm", start_image="images/NTRStripVideo02F01.webp")
    image TravelVideo01 = Movie(play="video/TravelVideo01.webm", start_image="images/TravelVideoF01.webp")
    image TravelVideo02 = Movie(play="video/TravelVideo02.webm", start_image="images/TravelVideoF01.webp")
    image MeganHJVideo01 = Movie(play="video/MeganHJVideo01.webm", start_image="images/MeganHJVideo01F01.webp")
    image MeganBJVideo01 = Movie(play="video/MeganBJVideo01.webm", start_image="images/MeganBJVideo01F01.webp")
    image MeganBJVideo02 = Movie(play="video/MeganBJVideo02.webm", start_image="images/MeganBJVideo01F01.webp")
    image MeganBJVideo03 = Movie(play="video/MeganBJVideo03.webm", start_image="images/MeganBJVideo03F01.webp")
    image JackOffVideo01 = Movie(play="video/JackOffVideo01.webm", start_image="images/JackOffVideo01F01.webp")
    image JoffMomVideo01 = Movie(play="video/JoffMomVideo01.webm", start_image="images/JoffMomVideo01F01.webp")
    image JackOffVideo02 = Movie(play="video/JackOffVideo02.webm", start_image="images/JackOffVideo02F01.webp")
    image JoffLaurenVideo01 = Movie(play="video/JoffLaurenVideo01.webm", start_image="images/JoffLaurenVideo01F01.webp")
    image JackOffVideo03 = Movie(play="video/JackOffVideo03.webm", start_image="images/JackOffVideo03F01.webp")
    image JoffSidneyVideo01 = Movie(play="video/JoffSidneyVideo01.webm", start_image="images/JoffSidneyVideo01F01.webp")
    image JackOffVideo04 = Movie(play="video/JackOffVideo04.webm", start_image="images/JackOffVideo04F01.webp")
    image JoffAuntVideo01 = Movie(play="video/JoffAuntVideo01.webm", start_image="images/JoffAuntVideo01F01.webp")
    image LaurenShowerVideo01 = Movie(play="video/LaurenShowerVideo01.webm", start_image="images/LaurenShowerVideo01F01.webp")
    image LaurenShowerVideo02 = Movie(play="video/LaurenShowerVideo02.webm", start_image="images/LaurenShowerVideo02F01.webp")
    image SidneyShowerVideo01 = Movie(play="video/SidneyShowerVideo01.webm", start_image="images/SidneyShowerVideo01F01.webp")
    image SidneyShowerVideo02 = Movie(play="video/SidneyShowerVideo02.webm", start_image="images/SidneyShowerVideo02F01.webp")
    image MomShowerVideo01 = Movie(play="video/MomShowerVideo01.webm", start_image="images/MomShowerVideo01F01.webp")
    image MomShowerVideo02 = Movie(play="video/MomShowerVideo02.webm", start_image="images/MomShowerVideo02F01.webp")
    image bg Meme17 = "Meme17.webp"
    image bg Meme18 = "Meme18.webp"
    image bg Meme19 = "Meme19.webp"
    image bg Meme20 = "Meme20.webp"
    image bg HoneyDoList01 = "HoneyDoList01.webp"
    image bg HoneyDoList02 = "HoneyDoList02.webp"
    image bg HoneyDoList03 = "HoneyDoList03.webp"
    image bg HoneyDoList04 = "HoneyDoList04.webp"
    image bg HoneyDoList05 = "HoneyDoList05.webp"
    image bg HoneyDoList06 = "HoneyDoList06.webp"
    image bg HoneyDoList07 = "HoneyDoList07.webp"
    image bg HoneyDoList08 = "HoneyDoList08.webp"
    image bg HoneyDoList09 = "HoneyDoList09.webp"
    image bg HoneyDoList10 = "HoneyDoList10.webp"
    image bg HoneyDoList11 = "HoneyDoList11.webp"
    image bg HoneyDoList12 = "HoneyDoList12.webp"
    image bg HoneyDoList13 = "HoneyDoList13.webp"
    image bg HoneyDoList14 = "HoneyDoList14.webp"
    image bg HoneyDoList15 = "HoneyDoList15.webp"
    image bg HoneyDoList16 = "HoneyDoList16.webp"
    image bg HoneyDoList17 = "HoneyDoList17.webp"
    image bg HoneyDoList18 = "HoneyDoList18.webp"
    image bg HoneyDoList19 = "HoneyDoList19.webp"
    image bg HoneyDoList20 = "HoneyDoList20.webp"
    image bg HoneyDoList21 = "HoneyDoList21.webp"
    image bg HoneyDoList22 = "HoneyDoList22.webp"
    image bg HoneyDoList23 = "HoneyDoList23.webp"
    image bg HoneyDoList24 = "HoneyDoList24.webp"
    image bg HoneyDoList25 = "HoneyDoList25.webp"
    image bg HoneyDoList26 = "HoneyDoList26.webp"
    image bg HoneyDoList27 = "HoneyDoList27.webp"
    image bg HoneyDoList28 = "HoneyDoList28.webp"
    image bg HoneyDoList29 = "HoneyDoList29.webp"
    image bg HoneyDoList30 = "HoneyDoList30.webp"
    image bg HoneyDoList31 = "HoneyDoList31.webp"
    image bg HoneyDoList32 = "HoneyDoList32.webp"
    image bg HoneyDoList33 = "HoneyDoList33.webp"
    image bg HoneyDoList34 = "HoneyDoList34.webp"
    image bg HoneyDoList35 = "HoneyDoList35.webp"
    image bg HoneyDoList36 = "HoneyDoList36.webp"
    image bg HoneyDoList37 = "HoneyDoList37.webp"
    image bg HoneyDoList38 = "HoneyDoList38.webp"
    image bg HoneyDoList39 = "HoneyDoList39.webp"
    image bg HoneyDoList40 = "HoneyDoList40.webp"
    image bg HoneyDoList41 = "HoneyDoList41.webp"
    image bg HoneyDoList42 = "HoneyDoList42.webp"
    image bg HoneyDoList43 = "HoneyDoList43.webp"
    image bg HoneyDoList44 = "HoneyDoList44.webp"
    image bg HoneyDoList45 = "HoneyDoList45.webp"
    image bg HoneyDoList46 = "HoneyDoList46.webp"
    image bg HoneyDoList47 = "HoneyDoList47.webp"
    image bg HoneyDoList48 = "HoneyDoList48.webp"
    image bg HoneyDoList49 = "HoneyDoList49.webp"
    image bg HoneyDoList50 = "HoneyDoList50.webp"
    image bg HoneyDoList51 = "HoneyDoList51.webp"
    image bg HoneyDoList52 = "HoneyDoList52.webp"
    image bg HoneyDoList53 = "HoneyDoList53.webp"
    image bg HoneyDoList54 = "HoneyDoList54.webp"
    image bg HoneyDoList55 = "HoneyDoList55.webp"
    image bg HoneyDoList56 = "HoneyDoList56.webp"
    image bg HoneyDoList57 = "HoneyDoList57.webp"
    image bg HoneyDoList58 = "HoneyDoList58.webp"
    image bg HoneyDoList59 = "HoneyDoList59.webp"
    image bg HoneyDoList60 = "HoneyDoList60.webp"
    image bg HoneyDoList61 = "HoneyDoList61.webp"
    image bg HoneyDoList62 = "HoneyDoList62.webp"
    image bg HoneyDoList63 = "HoneyDoList63.webp"
    image bg HoneyDoList64 = "HoneyDoList64.webp"
    image bg HoneyDoList65 = "HoneyDoList65.webp"
    image bg HoneyDoList66 = "HoneyDoList66.webp"
    image bg HoneyDoList67 = "HoneyDoList67.webp"
    image bg HoneyDoList68 = "HoneyDoList68.webp"
    image bg HoneyDoList69 = "HoneyDoList69.webp"
    image bg HoneyDoList70 = "HoneyDoList70.webp"
    image bg HoneyDoList71 = "HoneyDoList71.webp"
    image bg HoneyDoList72 = "HoneyDoList72.webp"
    image bg HoneyDoList73 = "HoneyDoList73.webp"
    image bg HoneyDoList74 = "HoneyDoList74.webp"
    image bg HoneyDoList75 = "HoneyDoList75.webp"
    image bg HoneyDoList76 = "HoneyDoList76.webp"
    image bg HoneyDoList77 = "HoneyDoList77.webp"
    image bg HoneyDoList78 = "HoneyDoList78.webp"
    image bg HoneyDoList79 = "HoneyDoList79.webp"
    image bg SidneyRun01 = "SidneyRun01.webp"
    image bg SidneyRun02 = "SidneyRun02.webp"
    image bg SidneyRun03 = "SidneyRun03.webp"
    image bg SidneyRun04 = "SidneyRun04.webp"
    image bg SidneyRun05 = "SidneyRun05.webp"
    image bg SidneyRun06 = "SidneyRun06.webp"
    image bg SidneyRun07 = "SidneyRun07.webp"
    image bg SidneyRun08 = "SidneyRun08.webp"
    image bg SidneyRun09 = "SidneyRun09.webp"
    image bg SidneyRun10 = "SidneyRun10.webp"
    image bg SidneyRun11 = "SidneyRun11.webp"
    image bg SidneyRun12 = "SidneyRun12.webp"
    image bg SidneyRun13 = "SidneyRun13.webp"
    image bg SidneyRun14 = "SidneyRun14.webp"
    image bg SidneyRun15 = "SidneyRun15.webp"
    image bg SidneyRun16 = "SidneyRun16.webp"
    image bg SidneyRun17 = "SidneyRun17.webp"
    image bg SidneyRun18 = "SidneyRun18.webp"
    image bg SidneyRun19 = "SidneyRun19.webp"
    image bg SidneyRun20 = "SidneyRun20.webp"
    image bg SidneyRun21 = "SidneyRun21.webp"
    image bg SidneyRun22 = "SidneyRun22.webp"
    image bg SidneyRun23 = "SidneyRun23.webp"
    image bg SidneyRun24 = "SidneyRun24.webp"
    image bg SidneyRun25 = "SidneyRun25.webp"
    image bg SidneyRun26 = "SidneyRun26.webp"
    image bg SidneyRun27 = "SidneyRun27.webp"
    image bg SidneyRun28 = "SidneyRun28.webp"
    image bg SidneyRun29 = "SidneyRun29.webp"
    image bg SidneyRun30 = "SidneyRun30.webp"
    image bg SidneyRun31 = "SidneyRun31.webp"
    image bg SidneyRun32 = "SidneyRun32.webp"
    image bg SidneyRun33 = "SidneyRun33.webp"
    image bg SidneyRun34 = "SidneyRun34.webp"
    image bg SidneyRun35 = "SidneyRun35.webp"
    image bg SidneyRun36 = "SidneyRun36.webp"
    image bg SidneyRun37 = "SidneyRun37.webp"
    image bg SidneyRun38 = "SidneyRun38.webp"
    image bg SidneyRun39 = "SidneyRun39.webp"
    image bg SidneyRun40 = "SidneyRun40.webp"
    image bg SidneyRun41 = "SidneyRun41.webp"
    image bg SidneyRun42 = "SidneyRun42.webp"
    image bg SidneyRun43 = "SidneyRun43.webp"
    image bg SidneyRun44 = "SidneyRun44.webp"
    image bg SidneyRun45 = "SidneyRun45.webp"
    image bg SidneyRun46 = "SidneyRun46.webp"
    image bg SidneyRun47 = "SidneyRun47.webp"
    image bg SidneyRun48 = "SidneyRun48.webp"
    image bg SidneyRun49 = "SidneyRun49.webp"
    image bg SidneyRun50 = "SidneyRun50.webp"
    image bg SidneyRun51 = "SidneyRun51.webp"
    image bg SidneyRun52 = "SidneyRun52.webp"
    image bg SidneyRun53 = "SidneyRun53.webp"
    image bg SidneyRun54 = "SidneyRun54.webp"
    image bg SidneyRun55 = "SidneyRun55.webp"
    image bg SidneyRun56 = "SidneyRun56.webp"
    image bg SidneyRun57 = "SidneyRun57.webp"
    image bg SidneyRun58 = "SidneyRun58.webp"
    image bg SidneyRun59 = "SidneyRun59.webp"
    image bg SidneyRun60 = "SidneyRun60.webp"
    image bg SidneyRun61 = "SidneyRun61.webp"
    image bg SidneyRun62 = "SidneyRun62.webp"
    image bg SidneyRun63 = "SidneyRun63.webp"
    image bg SidneyRun64 = "SidneyRun64.webp"
    image bg SidneyRun65 = "SidneyRun65.webp"
    image bg SidneyRun66 = "SidneyRun66.webp"
    image bg SidneyRun67 = "SidneyRun67.webp"
    image bg SidneyRun68 = "SidneyRun68.webp"
    image bg SidneyRun69 = "SidneyRun69.webp"
    image bg SidneyRun70 = "SidneyRun70.webp"
    image bg SidneyRun71 = "SidneyRun71.webp"
    image bg SidneyRun72 = "SidneyRun72.webp"
    image bg SidneyRun73 = "SidneyRun73.webp"
    image bg SidneyRun74 = "SidneyRun74.webp"
    image bg SidneyRun75 = "SidneyRun75.webp"
    image bg SidneyRun76 = "SidneyRun76.webp"
    image bg SidneyRun77 = "SidneyRun77.webp"
    image bg SidneyRun78 = "SidneyRun78.webp"
    image bg SidneyRun79 = "SidneyRun79.webp"
    image bg SidneyRun80 = "SidneyRun80.webp"
    image bg SidneyRun81 = "SidneyRun81.webp"
    image bg SidneyRun82 = "SidneyRun82.webp"
    image bg SidneyRun83 = "SidneyRun83.webp"
    image bg SidneyRun84 = "SidneyRun84.webp"
    image bg SidneyRun85 = "SidneyRun85.webp"
    image bg SidneyRun86 = "SidneyRun86.webp"
    image bg SidneyRun87 = "SidneyRun87.webp"
    image bg SidneyRun88 = "SidneyRun88.webp"
    image bg SidneyRun89 = "SidneyRun89.webp"
    image bg SidneyRun90 = "SidneyRun90.webp"
    image bg SidneyRun91 = "SidneyRun91.webp"
    image bg SidneyRun92 = "SidneyRun92.webp"
    image bg SidneyRun93 = "SidneyRun93.webp"
    image bg SidneyRun94 = "SidneyRun94.webp"
    image bg SidneyRun95 = "SidneyRun95.webp"
    image bg SidneyRun96 = "SidneyRun96.webp"
    image bg SidneyRun97 = "SidneyRun97.webp"
    image bg SidClub01 = "SidClub01.webp"
    image bg SidClub02 = "SidClub02.webp"
    image bg SidClub03 = "SidClub03.webp"
    image bg SidClub04 = "SidClub04.webp"
    image bg SidClub05 = "SidClub05.webp"
    image bg SidClub06 = "SidClub06.webp"
    image bg SidClub07 = "SidClub07.webp"
    image bg SidClub08 = "SidClub08.webp"
    image bg SidClub09 = "SidClub09.webp"
    image bg SidClub10 = "SidClub10.webp"
    image bg SidClub11 = "SidClub11.webp"
    image bg SidClub12 = "SidClub12.webp"
    image bg SidClub13 = "SidClub13.webp"
    image bg SidClub14 = "SidClub14.webp"
    image bg SidClub15 = "SidClub15.webp"
    image bg SidClub16 = "SidClub16.webp"
    image bg SidClub17 = "SidClub17.webp"
    image bg SidClub18 = "SidClub18.webp"
    image bg SidClub19 = "SidClub19.webp"
    image bg SidClub20 = "SidClub20.webp"
    image bg SidClub21 = "SidClub21.webp"
    image bg SidClub22 = "SidClub22.webp"
    image bg SidClub23 = "SidClub23.webp"
    image bg SidClub24 = "SidClub24.webp"
    image bg SidClub25 = "SidClub25.webp"
    image bg SidClub26 = "SidClub26.webp"
    image bg SidClub27 = "SidClub27.webp"
    image bg SidClub28 = "SidClub28.webp"
    image bg SidClub29 = "SidClub29.webp"
    image bg SidClub30 = "SidClub30.webp"
    image bg SidClub31 = "SidClub31.webp"
    image bg SidClub32 = "SidClub32.webp"
    image bg SidClub33 = "SidClub33.webp"
    image bg SidClub34 = "SidClub34.webp"
    image bg SidClub35 = "SidClub35.webp"
    image bg SidClub36 = "SidClub36.webp"
    image bg SidClub37 = "SidClub37.webp"
    image bg SidClub38 = "SidClub38.webp"
    image bg SidClub39 = "SidClub39.webp"
    image bg SidClub40 = "SidClub40.webp"
    image bg SidClub41 = "SidClub41.webp"
    image bg SidClub42 = "SidClub42.webp"
    image bg SidClub43 = "SidClub43.webp"
    image bg SidClub44 = "SidClub44.webp"
    image bg SidClub45 = "SidClub45.webp"
    image bg SidClub46 = "SidClub46.webp"
    image bg SidClub47 = "SidClub47.webp"
    image bg SidClub48 = "SidClub48.webp"
    image bg SidClub49 = "SidClub49.webp"
    image bg SidClub50 = "SidClub50.webp"
    image bg SidClub51 = "SidClub51.webp"
    image bg SidClub52 = "SidClub52.webp"
    image bg SidClub53 = "SidClub53.webp"
    image bg SidClub54 = "SidClub54.webp"
    image bg SidClub55 = "SidClub55.webp"
    image bg SidClub56 = "SidClub56.webp"
    image bg SidClub57 = "SidClub57.webp"
    image bg SidClub58 = "SidClub58.webp"
    image bg SidClub59 = "SidClub59.webp"
    image bg SidClub60 = "SidClub60.webp"
    image bg SidClub61 = "SidClub61.webp"
    image bg SidClub62 = "SidClub62.webp"
    image bg SidClub63 = "SidClub63.webp"
    image bg SidClub64 = "SidClub64.webp"
    image bg SidClub65 = "SidClub65.webp"
    image bg SidClub66 = "SidClub66.webp"
    image bg SidClub67 = "SidClub67.webp"
    image bg SidClub68 = "SidClub68.webp"
    image bg SidClub69 = "SidClub69.webp"
    image bg SidClub70 = "SidClub70.webp"
    image bg SidClub71 = "SidClub71.webp"
    image bg GOT01 = "GOT01.webp"
    image bg GOT02 = "GOT02.webp"
    image bg GOT03 = "GOT03.webp"
    image bg GOT04 = "GOT04.webp"
    image bg GOT05 = "GOT05.webp"
    image bg GOT06 = "GOT06.webp"
    image bg GOT07 = "GOT07.webp"
    image bg GOT08 = "GOT08.webp"
    image bg GOT09 = "GOT09.webp"
    image bg GOT10 = "GOT10.webp"
    image bg GOT11 = "GOT11.webp"
    image bg GOT12 = "GOT12.webp"
    image bg GOT13 = "GOT13.webp"
    image bg GOT14 = "GOT14.webp"
    image bg GOT15 = "GOT15.webp"
    image bg GOT16 = "GOT16.webp"
    image bg GOT17 = "GOT17.webp"
    image bg GOT18 = "GOT18.webp"
    image bg GOT19 = "GOT19.webp"
    image bg GOT20 = "GOT20.webp"
    image bg GOT21 = "GOT21.webp"
    image bg GOT22 = "GOT22.webp"
    image bg GOT23 = "GOT23.webp"
    image bg GOT24 = "GOT24.webp"
    image bg GOT25 = "GOT25.webp"
    image bg GOT26 = "GOT26.webp"
    image bg GOT27 = "GOT27.webp"
    image bg GOT28 = "GOT28.webp"
    image bg GOT29 = "GOT29.webp"
    image bg GOT30 = "GOT30.webp"
    image bg GOT31 = "GOT31.webp"
    image bg GOT32 = "GOT32.webp"
    image bg GOT33 = "GOT33.webp"
    image bg GOT34 = "GOT34.webp"
    image bg GOT35 = "GOT35.webp"
    image bg GOT36 = "GOT36.webp"
    image bg GOT37 = "GOT37.webp"
    image bg GOT38 = "GOT38.webp"
    image bg GOT39 = "GOT39.webp"
    image bg GOT40 = "GOT40.webp"
    image bg GOT41 = "GOT41.webp"
    image bg GOT42 = "GOT42.webp"
    image bg GOT43 = "GOT43.webp"
    image bg GOT44 = "GOT44.webp"
    image bg GOT45 = "GOT45.webp"
    image bg GOT46 = "GOT46.webp"
    image bg GOT47 = "GOT47.webp"
    image bg GOT48 = "GOT48.webp"
    image bg GOT49 = "GOT49.webp"
    image bg GOT50 = "GOT50.webp"
    image bg GOT51 = "GOT51.webp"
    image bg GOT52 = "GOT52.webp"
    image bg Breakfast01 = "Breakfast01.webp"
    image bg Breakfast02 = "Breakfast02.webp"
    image bg Breakfast03 = "Breakfast03.webp"
    image bg Breakfast04 = "Breakfast04.webp"
    image bg Breakfast05 = "Breakfast05.webp"
    image bg Breakfast06 = "Breakfast06.webp"
    image bg Breakfast07 = "Breakfast07.webp"
    image bg Breakfast08 = "Breakfast08.webp"
    image bg Breakfast09 = "Breakfast09.webp"
    image bg Breakfast10 = "Breakfast10.webp"
    image bg Breakfast11 = "Breakfast11.webp"
    image bg Breakfast12 = "Breakfast12.webp"
    image bg Breakfast13 = "Breakfast13.webp"
    image bg Breakfast14 = "Breakfast14.webp"
    image bg Breakfast15 = "Breakfast15.webp"
    image bg Breakfast16 = "Breakfast16.webp"
    image bg Breakfast17 = "Breakfast17.webp"
    image bg Breakfast18 = "Breakfast18.webp"
    image bg Breakfast19 = "Breakfast19.webp"
    image bg Breakfast20 = "Breakfast20.webp"
    image bg Breakfast21 = "Breakfast21.webp"
    image bg Breakfast22 = "Breakfast22.webp"
    image bg Breakfast23 = "Breakfast23.webp"
    image bg Breakfast24 = "Breakfast24.webp"
    image bg Breakfast25 = "Breakfast25.webp"
    image bg Breakfast26 = "Breakfast26.webp"
    image bg MafiaPaid01 = "MafiaPaid01.webp"
    image bg MafiaPaid02 = "MafiaPaid02.webp"
    image bg MafiaPaid03 = "MafiaPaid03.webp"
    image bg MafiaPaid04 = "MafiaPaid04.webp"
    image bg MafiaPaid05 = "MafiaPaid05.webp"
    image bg MafiaPaid06 = "MafiaPaid06.webp"
    image bg MafiaPaid07 = "MafiaPaid07.webp"
    image bg MafiaPaid08 = "MafiaPaid08.webp"
    image bg MafiaPaid09 = "MafiaPaid09.webp"
    image bg MafiaPaid10 = "MafiaPaid10.webp"
    image bg MafiaPaid11 = "MafiaPaid11.webp"
    image bg MafiaPaid12 = "MafiaPaid12.webp"
    image bg MafiaPaid13 = "MafiaPaid13.webp"
    image bg MafiaPaid14 = "MafiaPaid14.webp"
    image bg TravelVideoF01 = "TravelVideoF01.webp"
    image bg LaurenShowerClimax = "LaurenShowerClimax.webp"
    image bg SidneyShowerClimax = "SidneyShowerClimax.webp"
    image bg MomShowerClimax = "MomShowerClimax.webp"

    image Meme17 = "Meme17.webp"
    image Meme18 = "Meme18.webp"
    image Meme19 = "Meme19.webp"
    image Meme20 = "Meme20.webp"

#############  RYAN'S ROOM  #################################  RYAN'S ROOM  ####################################################  RYAN'S ROOM  ################################################  RYAN'S ROOM  ################################################################  RYAN'S ROOM  ###############################################################  RYAN'S ROOM  ########################

label sidneys_home_late:
    scene bg SleepBlack
    with fade
    "{i}(Soft footsteps and door creaking.){/i}"
    scene bg SidClub57
    with fade
    R "{i}(whispering){/i} Oh.... Hey Sidney."
    S "Oh.... I'm sorry I woke you.... I was trying to be as quiet as I can."
    R "It's ok. I think I just barely dozed off, so I should be able to fall right back asleep."
    scene bg SidClub58
    with fade
    S "Well, since you're awake, let me give you part of the money from work tonight. Please use it for the Mafia debt, or some other way that's good for our family."
    "{i}\"Money + $100\"{/i}"
    $ money += 100
    if daycounter == 1 and monday_sid_worked == False:
        $ sidney_money += 200
    else:
        pass
    R "Thank you so much!  This will help out a lot!"
    S "My pleasure.... Now scootch over!.... I've got to get to sleep. Work was exhausting, and I've had a cup of tea to help calm my nerves."
    scene bg SidClub59
    with dissolve
    R "Wait.... Sidney?.... Arent you going to change first?.... Your clothes smell like alcohol."
    S "{i}(light snoring){/i}"
    scene bg SidClub60
    with fade
    RT "{i}Wow! She really is tired.{/i}"
    RT "{i}And she's really going to be dead to the world after drinking that melatonin laced tea.{/i}"
    scene bg SidClub61
    with dissolve
    R "{i}(whispering loudly){/i} Sidney!.... Go change your clothes!"
    R "Pssst.... Sidney!"
    scene bg SidClub60
    with dissolve
    RT "{i}I think she'd sleep through an earthquake right now.{/i}"
    RT "{i}And those pantyhose are sexy as hell!{/i}"
    RT "{i}I'd have to be an idiot to not recognize the opportunity here.{/i}"
    RT "{i}But I am pretty tired.{/i}"
    $ sidney_worked_late = 1
    menu:
        "I'm not going to miss this opportunity.":
            play music SexMusic
            RT "{i}Alright!.... Off come my shorts.{/i}"
            scene bg SidClub62
            with fade
            RT "{i}That is one sexy ass!{/i}"
            RT "{i}I could probably get these pantyhose off, but I don't think I could get them back on without waking her.{/i}"
            scene bg SidClub63
            with dissolve
            RT "{i}This is going to be amazing anyways.{/i}"
            scene bg SidClub64
            with dissolve
            RT "{i}That is one muscular ass! All that running is paying off.{/i}"
            RT "{i}This is going to feel amazing.{/i}"
            scene SidClubVideo08
            with fade
            $ renpy.pause ()
            $ renpy.pause ()
            RT "{i}Ooohhh.... I'm almost there!{/i}"
            $ renpy.pause ()
            R "Hhhnnnnggghhhh...."
            play sound Ejaculate
            scene bg SidClub65
            with dissolve
            $ renpy.pause ()
            play sound Ejaculate
            scene bg SidClub66
            with dissolve
            $ renpy.pause ()
            scene bg SidClub67
            with fade
            RT "{i}God that felt good!.... What a mess.{/i}"
            RT "{i}Hopefully I can just rub this in, and she won't notice.{/i}"
            RT "{i}I've heard cum is good for the skin.{/i}"
            RT "{i}I'll have to ask Sidney if her back is feeling extra moisturized and vibrant later.{/i}"
            scene bg SidClub59
            with fade
            RT "{i}There.... As soon as the cum on her pantyhose dries, she won't even be able to tell.{/i}"
            RT "{i}And now, I'm going to sleep well tonight.{/i}"
            scene bg SleepBlack
            with fade
            play music Honey
            jump sleep
        "Just go to sleep.":
            scene bg SleepBlack
            with fade
            jump sleep

############# Lounge ################################# Lounge ######################################################## Lounge ####################################################### Lounge ################################################################# Lounge ############################################################## Lounge #################################

label honey_do_list:
    if jr_watched == True and fixed_sink >= 2:
        jump fix_washer
    if lectureprogress >= 3 and fixed_bulb == True:
        jump fix_sink
    else:
        jump fix_bulb

label fix_bulb:
    if fixed_bulb == True:
        scene bg HoneyDoList01
        with fade
        RT "{i}Mom's at it again.  Doing her best to keep our house functioning like a normal home should.{/i}"
        RT "{i}I've still got plenty on my plate too, but should I take some time to see if she needs help?{/i}"
        menu:
            "Help Mom.":
                R "Hey, Mom! Way to rock that broom."
                scene bg HoneyDoList04
                with fade
                M "What is it, [ryan]?  I still don't have time for your playful banter."
                R "Sorry....  I know.... I should stop trying."
                R "I was just wondering if you needed any help with the house."
                M "You still want to help me around the house?...."
                R "Well, yeah.... Dad's still gone, and your \"honey-do list\" must still be getting longer."
                scene bg HoneyDoList07
                with dissolve
                M "I guess I just didn't think you'd still want to help me after I let you fall that time."
                M "Are your knees at least feeling better?"
                R "Oh yeah, of course, and I still don't want you to feel like you're in this thing all on your own.  I want to help you whenever I can."
                scene bg HoneyDoList10
                with dissolve
                M "hmmm.... Well, that is a very sweet of you, and there are a number of things that I can't do myself around the house.  Are you still feeling pretty handy?"
                R "For sure!"
                "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                $ momaffection += 1
                scene bg HoneyDoList04
                with dissolve
                M "Alright, well, we still need to stay right here in the lounge."
                M "I have no idea how, but that same light seems to have come loose again."
                M "The flickering is starting to drive me crazy."
                M "Do you think you could climb up there again, and make sure you screw it in nice and tight?"
                RT "{i}Ha...That's what she said!{/i}"
                R "Do you promise not to let go this time.... or surprise me like you did before?"
                M "No.... Of course not.... I'm sorry.... It won't happen again.... I don't know what came over me.... "
                MT "{i}Except that a huge penis bulge was screaming for my attention, right in front of my face.{/i}"
                scene bg HoneyDoList13
                with fade
                RT "{i}Ok.... carefully.... I don't want to fall again.{/i}"
                M "Wait a second honey, let me hold onto you.  I don't want you to fall."
                scene bg HoneyDoList14
                with dissolve
                play music SexMusic
                R "Oh, right, thanks Mom."
                RT "{i}Oh, I love having her hands on me!{/i}"
                scene bg HoneyDoList15
                with fade
                M "That's right honey. That same one as last time.... Oh, please be careful!"
                scene bg HoneyDoList20
                with fade
                RT "{i}I don't want to fall, but I wouldn't mind if she touched my penis again.{/i}"
                RT "{i}I'm prepared this time.{/i}"
                scene bg HoneyDoList16
                with fade
                MT "{i}Ok [mom_name], Try not to focus on his \"you know what.\"{/i}"
                MT "{i}Why does it have to be exactly in my face?{/i}"
                scene bg HoneyDoList23
                with fade
                MT "{i}Even when he's flaccid, he's still *so* big!{/i}"
                MT "{i}For his own sake, I'm so glad he didn't inherit his father's penis.{/i}"
                MT "{i}My dad would be proud to know he passed his size down to [ryan].{/i}"
                MT "{i}But how on earth would I ever bring that up to him?{/i}"
                MT "{i}Well, at least there was one benefit to [dad_name] being on the small side.{/i}"
                MT "{i}Anal sex isn't nearly as painful as it could be....{/i}"
                MT "{i}I'm pretty sure I'd never be able to stuff [ryan]'s penis in my ass.{/i}"
                "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                $ momlibido += 1
                MT "{i}Oh God, [mom_name]!.... Get those thoughts out of your head!{/i}"
                MT "{i}What in the fuck is wrong with you?!{/i}"
                R "Ok.... I'm done.... I'm coming down."
                scene bg HoneyDoList29
                with fade
                M "So, did you screw it really good this time?"
                RT "{i}I'll screw you really good someday.{/i}"
                R "I think so.  Though I thought I got it good last time too."
                M "...."
                M "Yeah, it's weird that it won't stay in."
                RT "{i}Could she be unscrewing it on purpose, so she can look at my penis?{/i}"
                RT "{i}That's just wishful thinking.  There is no way she would do that.{/i}"
                R "Well, hopefully we took care of it for good that time."
                R "Do you need me for anything else?"
                M "Uhhh.... No.... I think we're good for today."
                R "Alright.... I'm outta here."
                scene bg HoneyDoList30
                with fade
                M "Well, thanks for your help today."
                M "Uhhh.... "
                M "And good job!"
                RT "{i}Did Mom just give me a congratulatory butt slap?{/i}"
                scene bg HoneyDoList31
                with fade
                MT "{i}Oh God, [mom_name].... Did you just slap [ryan]'s butt?....{/i}"
                MT "{i}Why am I acting so awkward around him?{/i}"
                MT "{i}Probably has to do with my dirty thoughts about his penis.{/i}"
                MT "{i}Ok, [mom_name].... Get your act back together....{/i}"
                play music Honey
                $ timeofdaycounter += 1
                jump lounge
            "Don't help Mom.":
                scene bg HoneyDoList01
                $ screen_on = "momcleanloungemap"
                call screen momcleanloungemap
    else:
        scene bg HoneyDoList01
        with fade
        RT "{i}Oh, poor Mom!  Her life's falling apart, and she still finds time to take care of the house.{/i}"
        RT "{i}I've got more than enough on my plate too, but should I take some time to see if she needs help?{/i}"
        menu:
            "Help Mom.":
                R "Hey, Mom! Working hard, or hardly working?"
                scene bg HoneyDoList04
                with fade
                M "What is it, [ryan]?  I don't have time for playful banter."
                R "Sorry....  I know.... That was stupid."
                R "I was just wondering if you needed any help with the house."
                M "You want to help me around the house?...."
                R "Well, yeah.... Now that Dad's gone, your list of things around the house for.... you know.... like, manly work, must be getting pretty long."
                scene bg HoneyDoList07
                with dissolve
                M "Are you talking about the \"honey-do list\"?"
                M "Are you hoping to become my surrogate honey while your dad's in prison?"
                R "Well, it sounds kind of weird when you put it like that, but sure, why not?"
                R "You already call me honey anyways, and there's plenty of handyman work to do around the house.  The least I can do is chip in a little."
                scene bg HoneyDoList10
                with dissolve
                M "hmmm.... Well, that is a very generous offer, and there are a number of things that I can't do myself around the house.  Do you really think you're handy enough to help me tackle them?"
                R "For sure, and anything I don't know how to do, I can just look up online."
                "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                $ momaffection += 1
                scene bg HoneyDoList04
                with dissolve
                M "Alright, well let's start out right here in the lounge."
                M "You've probably noticed that the light bulb above the tv flickers sometimes."
                M "I'd just fix it myself, but I'm afraid I would fall off the cabinet without anybody holding onto me."
                M "Do you think you could climb up there if I support you, and make sure the light bulb is screwed in nice and tight?"
                RT "{i}I'd like to screw something else in nice and tight.{/i}"
                R "Yeah.... I'm on it."
                scene bg HoneyDoList13
                with fade
                RT "{i}Not a lot of room up here.  I can see why Mom was hesitant.{/i}"
                M "Wait a second honey, let me hold onto you.  I don't want you to fall."
                scene bg HoneyDoList14
                with dissolve
                play music SexMusic
                R "Oh, right, thanks Mom."
                RT "{i}Oh, I love having her hands on me!{/i}"
                scene bg HoneyDoList15
                with fade
                M "That's right honey. That one right there.... Oh, please be careful!"
                scene bg HoneyDoList20
                with fade
                R "The lights are still on.  Won't the light bulb burn me?"
                M "Oh, don't worry.  They're LED lights, so they don't get hot."
                RT "{i}They better not.{/i}"
                scene bg HoneyDoList16
                with fade
                MT "{i}Psshhhh.... (sarcastically) Well, this is a nice view.{/i}"
                MT "{i}Oh my God!.... Is that?....{/i}"
                scene bg HoneyDoList17
                with fade
                MT "{i}Holy shit.... I think that's his dick bulge.{/i}"
                MT "{i}Or is it just a fold in the fabric of his shorts?{/i}"
                MT "{i}If that's a dick bulge, it means his dick is bulging through his underwear and shorts.{/i}"
                MT "{i}Or that he's going commando.{/i}"
                "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                $ momlibido += 1
                scene bg HoneyDoList18
                with dissolve
                MT "{i}I wonder if....{/i}"
                scene bg HoneyDoList20
                with fade
                $ renpy.pause ()
                scene bg HoneyDoList21
                with dissolve
                R "Mom!....  Don't let go please.... I'll lose my balance!"
                scene bg HoneyDoList18
                with fade
                $ renpy.pause ()
                scene bg HoneyDoList19
                with dissolve
                MT "{i}It is his penis!....{/i}"
                scene bg HoneyDoList21
                with fade
                $ renpy.pause ()
                scene bg HoneyDoList22
                with dissolve
                R "What are you?....  Watch out!.... I'm going to fall!...."
                scene bg HoneyDoList24
                with fade
                $ renpy.pause ()
                play sound Punch
                scene bg HoneyDoList25
                with fade
                R "Ohhhhoooohoooohoooo.... Oooo.... Ouch!...."
                play sound Muffled loop
                M "Mmmmpphhhh"
                R "Mom?  Are you ok?...."
                R "Oh, shit!.... Sorry!"
                stop sound
                play sound WomanBreath loop
                scene bg HoneyDoList26
                with dissolve
                R "Fuck.... Ohhh.... My knees...."
                M "Please [ryan].... Watch your language."
                R "...."
                R "Are you hurt?"
                stop sound
                scene bg HoneyDoList27
                with dissolve
                M "No, not bad, I just couldn't breathe with you tea-bagging me."
                R "...."
                R "Pffff...."
                scene bg HoneyDoList28
                with dissolve
                R "Hahaha...."
                R "I was tea-bagging you, wasn't I?"
                M "Hahahaha.... "
                M "Yeah.... hahaha.... but please don't repeat that outside of this conversation."
                M "I don't think it would sound very good out of context."
                R "...."
                R "Well, I think the light bulb will at least stop flickering."
                M "Let's hope so"
                R "Are there any more home repairs you need help with?"
                M "Not right now.... Let's call it a day."
                M "Thank you so much for being so willing to help!"
                R "Of course! Love ya, Mom.."
                M "I love you too."
                play music Honey
                $ timeofdaycounter += 1
                $ fixed_bulb = True
                jump lounge
            "Don't help Mom.":
                scene bg HoneyDoList01
                $ screen_on = "momcleanloungemap"
                call screen momcleanloungemap

label sidney_morning_jog:
    if mp_captured == True:
        scene bg SidneyRun01
        with fade
        RT "{i}Looks like Sidney's all ready to go running.{/i}"
        scene bg SidneyRun03
        with fade
        R "Hey Sid."
        S "Hey, [ryan].  Are you ready to go running?"
        menu:
            "Yes":
                R "You bet I am.  Let me run and change my clothes and I'll meet you outside."
                jump park_activities
            "No":
                R "Sorry Sid, I'm just not feeling it today."
                S "That's ok. Ever since Mr. Peterson got put back into his nursing home, I don't feel afraid to go running there all alone."
                S "But hopefully you'll be up for it next time."
                S "It's nice to not have to run alone."
                $ sidneys_running = True
                jump lounge
    if fit_enough == True:
        scene bg SidneyRun01
        with fade
        RT "{i}Sidney's about ready to go running.{/i}"
        RT "{i}I wonder if she needs my protection in the park today.{/i}"
        scene bg SidneyRun02
        with fade
        R "Hey Sid, you look like you're about ready to go jogging."
        S "Yes, your skills of observation are unmatched."
        R "Man, you're funny!"
        scene bg SidneyRun03
        with dissolve
        S "Haha.... I know it."
        S "So, are you going to come and keep me safe at the park today?"
        menu:
            "Yes.":
                R "You bet I am.  Let me run and change my clothes and I'll meet you outside."
                jump park_activities
            "No.":
                R "Sorry Sid, I'm just not feeling it today."
                S "That's ok, I'll just head to the indoor track then."
                S "But hopefully you'll be up for it next time."
                S "I'm starting to enjoy running with you."
                $ sidneys_running = True
                jump lounge
    if groped_in_park == 2:
        scene bg SidneyRun01
        with fade
        RT "{i}Sidney's about ready for another run. I've always been impressed with her ability to stick with things. Even after her experiences in the park.{/i}"
        scene bg SidneyRun03
        with fade
        R "Hey Sidney. Are you off to the indoor track?"
        S "Yep, though I really wish I could go run in the park."
        scene bg SidneyRun02
        with dissolve
        S "Please hurry up and get into shape so you can keep me safe in the park from Mr. Peterson."
        R "I'll try, but how will I know when I'm ready?"
        S "When you can make it there in 9 minutes or less."
        R "Alright, I'll let you know when I'm in good enough shape."
        R "Have a good run today."
        menu:
            "Run to the park":
                jump run_training
            "I don't feel like running today.":
                $ sidneys_running = True
                jump lounge
    if first_park_run:
        scene bg SidneyRun01
        with fade
        RT "{i}Wow! Sidney is ambitious these days. I'm used to seeing her sleep in as late as she can.{/i}"
        scene bg SidneyRun03
        with fade
        R "Hey Sid, It looks like you're off again for your morning jog."
        S "Did you figure that one out all by yourself, Captain Obvious?"
        R "Oh, hardy har."
        R "I was just wondering if you were going to risk runnning in the park again."
        scene bg SidneyRun02
        with dissolve
        S "Well, I really want to, but I'm worried about running into crazy old Mr. Peterson again."
        S "Do you think it would be too risky? Should I go running at the country club's indoor track instead?"
        menu:
            "You should go to the indoor track.":
                scene bg SidneyRun03
                with dissolve
                R "Yeah, I think maybe you should just stick to running at the indoor track until Mr. Peterson has been caught."
                S "Uurrgghh.... I think you're right, but I just hate running inside when the weather is so nice."
                S "Alright, well I'm out of here. Good luck at school, or work, or whatever you're doing today."
                R "Thanks Sid! Have a good run."
                $ sidneys_running = True
                jump lounge
            "I'll go to the park myself and see if it's safe.":
                scene bg SidneyRun03
                with dissolve
                R "Yeah, why don't you go running at the indoor track today. I'll take a jog to the park and see if I think it's safe for next time."
                S "Really?  You'd do that for me?"
                R "Yeah, of course! I need the exercise anyways."
                "{i}{b}\"Sidney's Respect +1\"{/b}{/i}"
                $ sidneyrespect += 1
                S "I'd really appreciate that."
                R "Yeah, think nothing of it."
                S "Alright, I'll see you later. Be careful at the park."
                R "I will, and enjoy your run at the club."
                jump run_training
            "Let's go jogging in the park together. I'll keep you safe. (Light NTR Warning)" if groped_in_park <= 1:
                scene bg SidneyRun03
                with dissolve
                R "Don't go to the indoor track."
                R "Mr. Peterson is harmless. Plus, I'll go with you and keep you safe."
                S "Are you sure you can keep up with me this time?"
                R "I'll try my best."
                S "Alright, run and change and I'll meet you in front of the house."
                jump not_fit_enough
    else:
        scene bg SidneyRun01
        with fade
        RT "{i}Oh wow, Sidney's actually up!{/i}"
        RT "{i}Looks like she's getting ready to go jogging.{/i}"
        scene bg SidneyRun03
        with fade
        R "Hey Sid. You're up early."
        S "Yeah, remember what I told you?"
        R "About what?"
        scene bg SidneyRun02
        with dissolve
        S "I have to get up early so that Mom and Lauren don't discover me sleeping in your bed."
        S "Mom would flip out if she knew."
        R "Oh yeah, that probably is a good precaution to take."
        S "So yeah, since I'm up early anyways, I decided it would be good for me to take an early morning run."
        S "It probably wouldn't hurt you to do some exercising as well."
        S "Do you do anything even remotely active?"
        R "I used to play basketball, but now I cant make the team anymore because I'm too short."
        scene bg SidneyRun03
        with dissolve
        S "Ohhh.... Don't worry, I'm sure you're not done growing yet."
        R "Man, I hope not."
        R "But you're right, I should do more to stay in shape. Wait for me, I'm going to go get my running shoes."
        scene bg SidneyRun02
        with dissolve
        S "No, that's not what I meant. Do you even think you could keep up with me?"
        R "I don't know, it has been a while since I did any running."
        S "Ok, well, you're welcome to come with me, but don't expect me to wait for you if you can't keep up."
        R "Awesome! Sounds fun. I'll just run and change."
        S "Ok, I'll meet you in front of the house."
        scene bg SleepBlack
        with fade
        scene bg SidneyRun04
        with fade
        S "There you are. Don't forget to stretch out a bit."
        R "Oh, I'm fine. I don't need to stretch."
        S "Ok, if you're sure."
        R "Yeah, I'm sure. Are we running over to the club to use their indoor track?"
        S "No, we're running to the park by the mall and back.  I don't want to run indoors on a beautiful day like today."
        R "Oh really? That far?"
        S "Well, you can always stay home and paint your nails if it's too far for you."
        R "It's not too far. I'll beat you there!"
        RT "{i}I hope!{/i}"
        RT "{i}I can't let a girl beat me!{/i}"
        S "Yeah right, I'll even give you a 1 minute head start."
        S "On your mark... get set... go!"
        scene bg SleepBlack
        with fade
        $ renpy.pause ()
        scene bg SidneyRun08
        with fade
        RT "{i}Oh, shit!.... I pushed it too hard, too fast.{/i}"
        RT "{i}I don't know if I can even make it to the park.{/i}"
        S "Hey, slow poke! On your right!"
        scene bg SidneyRun05
        with fade
        R "Hey wait! Don't go on without me."
        S "Yeah right, I'm not waiting for you."
        scene bg SidneyRun06
        S "{i}(yelling){/i} I'll meet you at the park!"
        RT "{i}Yeah, right!.... I'll never make it to the park.{/i}"
        scene bg SidneyRun07
        with fade
        RT "{i}Shit.... It feels like my heart is going to jump out of my throat!{/i}"
        RT "{i}I'm closer to home than I am to the park. I'm just going to turn around and go home.{/i}"
        "{i}\"[ryan]'s physical fitness +1\"{/i}"
        $ physical_fitness += 1
        scene bg SleepBlack
        with fade
        scene bg SidneyRun10
        with fade
        ST "{i}Oh yes! I beat that cocky little shit.{/i}"
        ST "{i}I'll have to rub it in his face when I get home.{/i}"
        ST "{i}Oh man!.... I really worked up a sweat.{/i}"
        scene bg SidneyRun11
        with dissolve
        ST "{i}I just need to take a minute to rest and cool down.{/i}"
        ST "{i}I can't even see [ryan]. I really kicked his ass.{/i}"
        scene bg SleepBlack
        with fade
        $ renpy.pause ()
        scene bg SidneyRun12
        with fade
        CMT "{i}Shit!....{/i}"
        CMT "{i}Fuck!....{/i}"
        CMT "{i}How did I get separated from my unit?{/i}"
        scene bg SidneyRun13
        with fade
        CMT "{i}Ok... I must have been knocked unconscious.{/i}"
        CMT "{i}Because I don't remember how I got here.{/i}"
        CMT "{i}At least I don't have any other wounds.{/i}"
        scene bg SidneyRun12
        with fade
        CMT "{i}How did I lose my rifle? Well, at least I still have my trusty sidearm.{/i}"
        CMT "{i}I just hope the other boys from the unit are ok.{/i}"
        scene bg SidneyRun13
        with fade
        CMT "{i}It looks like I'm coming up onto a clearing.{/i}"
        CMT "{i}There must be a village nearby.{/i}"
        CMT "{i}I just hope they're friendlies.{/i}"
        CMT "{i}Oh... what do we have here?{/i}"
        scene bg SidneyRun14
        with fade
        CMT "{i}Looks like the village prostitute is out peddling her wares.{/i}"
        CMT "{i}She looks like she's all alone.{/i}"
        CMT "{i}I'm going to have to go get me some of that.{/i}"
        CMT "{i}Even if she is on the enemy side, I'm sure she wouldn't say no to a few dollars.{/i}"
        scene bg SleepBlack
        with fade
        scene bg SidneyRun15
        with fade
        ST "{i}Urgggghhh.... He must have given up and gone home.{/i}"
        CM "Well, hello there pretty thing!"
        scene bg SidneyRun62
        with dissolve
        S "Who... who are you?"
        CM "Oh that doesn't matter now, does it? I'm just a paying customer."
        S "A paying customer? What.... does that mean?"
        CM "And I pay in dollars, which are a lot more valuable than your currency."
        S "What in the hell are you talking about?"
        CM "Plus, I think you'll like what I've got right down here."
        scene bg SidneyRun17
        with dissolve
        ST "{i}Oh.... my.... God!...{/i}"
        ST "{i}He's a.... a....{/i}"
        scene bg SidneyRun18
        with dissolve
        S "FLASHER!!"
        S "HELP!.... FLASHER!... HELP!"
        X "Hey you! Stay right there!"
        CMT "{i}Shit!.... It's the commies!{/i}"
        scene bg SidneyRun19
        with dissolve
        CM "You'll never catch me alive, you commie bastard!"
        S "HELP!.... FLASHER!... Please! Someone catch him!"
        scene bg SidneyRun20
        with fade
        P "Mr. Peterson!.... Please stop!.... Your family is worried about you!"
        CM "You commie bastards will thank us one day after we win this war!"
        P "No! Please stop!"
        scene bg SidneyRun22
        with fade
        S "Holy shit!....  What in the hell?.... That crazy guy flashed me his junk!"
        S "And it appears that [ryan] isn't coming!"
        S "I'm going to give him hell when I get home!"
        scene bg SleepBlack
        with fade
        $ renpy.pause ()
        scene bg SidneyRun58
        with fade
        RT "{i}I really am in bad shape.{/i}"
        RT "{i}I can't believe how badly Sidney smoked me.{/i}"
        RT "{i}She's going to rub it in my face so bad!{/i}"
        scene bg SidneyRun59
        with dissolve
        S "So there you are!"
        R "Oh, good! You made it home."
        R "Sorry I didn't meet you at the park.... My a.... ankle was acting up.... an old basketball injury."
        scene bg SidneyRun60
        with fade
        S "Don't make up excuses for being a pussy!"
        S "I waited a long time at the park for you."
        S "Long enough for a crazy old man to flash me his junk."
        R "Oh my God!  Really?"
        S "Yeah, after he confused me for a prostitute."
        S "Is my workout outfit really that revealing?"
        R "No.... It's pretty sexy though.... I wonder if it was poor old Mr. Peterson."
        scene bg SidneyRun64
        with dissolve
        S "Yeah, I think I heard the police officer yell that name while he was chasing him."
        R "Oh wow!  You should have tried to catch him."
        S ".... Are you crazy? He wanted to pay me for sex!"
        R "Oh, he's just a little confused.  He's a war hero you know."
        R "You would have been a hero too, if you had caught him."
        R "His poor family."
        scene bg SidneyRun60
        with dissolve
        S "His poor family? What about me? He flashed me his nasty old wrinkly junk."
        R "Yeah, well I'm sure he's been off of his meds for a while now."
        R "Didn't you hear about him on the news?"
        S "No.... I've been at college, I wasn't following your local news."
        R "Well, he escaped from the nursing home a few weeks ago."
        R "No one's been sure if he's dead or alive, but people keep having sightings of him."
        R "Nobody's been able to catch him either. They say his survival training from the army is probably keeping him alive."
        R "Poor Mr. Peterson."
        S "Stop feeling sorry for my flasher!"
        R "But he's...."
        S "I don't care."
        scene bg SidneyRun61
        with fade
        S "{i}(mumbling){/i} Thought I'd get a little sympathy, but he only cares about poor Mr. Peterson."
        RT "{i}Haha.... He thought Sidney was a prostitute.... I know I'd pay for a piece of that ass.{/i}"
        scene bg SidneyRun58
        RT "{i}I need to get myself into better shape though, if I want to run with Sidney every morning.{/i}"
        RT "{i}I should probably keep running in the mornings to increase my endurance and overall physical fitness.{/i}"
        $ timeofdaycounter += 1
        $ first_park_run = True
        scene bg SleepBlack
        with fade
        jump lounge

label sidney_search:
    scene bg LaurenPonieTV
    with fade
    RT "{i}Looks like Lauren's watching her ponies show again.{/i}"
    "DING DONG"
    RT "{i}That's the doorbell. I'm pretty sure I know who that is.{/i}"
    menu:
        "Go answer the door":
            scene bg FrontDoor01
            with fade
            $ persistent.gal_Sidney_6 = True
            J "Hello little boy, is your mom at home?"
            scene bg SleepBlack
            with fade
            "{i}\"A few minutes earlier.\"{/i}"
            scene bg SidClub01
            with fade
            ST "{i}I don't have much time. I've got to make this fast.{/i}"
            ST "{i}If I were [ryan], where would I hide my money?{/i}"
            scene bg SidClub02
            with dissolve
            ST "{i}It's not in his desk.{/i}"
            scene bg SidClub03
            with dissolve
            ST "{i}No shoe boxes of cash under the bed.{/i}"
            scene bg SidClub04
            with dissolve
            ST "{i}Bingo....{/i}"
            if money >= 1000:
                ST "{i}That's a lot of cash just sitting in his top drawer.{/i}"
                ST "{i}As soon as Mom's off to the club, I'll put it right back.{/i}"
            else:
                ST "{i}There's not even enough here to pay the Mafia debt this week.{/i}"
                ST "{i}I'd better take it anyways, just in case [ryan] has enough to cover the rest in his wallet.{/i}"
                ST "{i}As soon as Mom's off to the club, I'll put it right back.{/i}"
            ST "{i}I can't believe I'm doing this.{/i}"
            ST "{i}What has come over me lately?{/i}"
            ST "{i}I think it's just the fact that Mom has always been such a prude.{/i}"
            ST "{i}I can't even imaging her stripping on a stage.{/i}"
            ST "{i}I've got to see it to believe it.{/i}"
            ST "{i}And if [ryan] doesn't have the cash to pay the Mafia, than Mom's got to go work the pole.{/i}"
            ST "{i}Shit!.... Am I going too far?....{/i}"
            "DING DONG"
            ST "{i}Shit!  That's probably them.  I've got to really hurry and get my clubbing outfit on.{/i}"
            scene bg SleepBlack
            with dissolve
            $ renpy.pause ()
            scene bg FrontDoor01
            with fade
            J "Hello little boy, is your mom at home?"
            RT "{i}He knows I'm an adult by now.  What an asshole.{/i}"
            R "Just a second."
            R "Hey Mom, there's some strange men at the door for you!"
            scene bg FrontDoor02
            with dissolve
            R "Wow, Mom! Looking good as ever!"
            M "Please, [ryan].... not now."
            $ timeofdaycounter += 1
            M "Were you able to get enough money together to pay them off this week?"
            if money >= 1000:
                R "Of course, Mom, did you really doubt me?"
                scene bg FrontDoor03
                with dissolve
                R "I've just got to run to my room and get it. I'll be right back."
                scene bg SleepBlack
                with fade
                scene bg SidClub05
                with fade
                RT "{i}What in the hell?!{/i}"
                RT "{i}Where is my Goddamned money?{/i}"
                RT "{i}Shit.... What could have happened to it?{/i}"
                RT "{i}Did I leave it at the warehouse or something?{/i}"
                RT "{i}Fuck!.... The DeCapos aren't going to sit around while I look for it.{/i}"
                RT "{i}How am I going to break the news to Mom?{/i}"
                scene bg SleepBlack
                with fade
                scene bg FrontDoor02
                with fade
                R "So, it turns out that I can't find my cash."
                M "What? No that can't be.  Let me come help you look for it."
                J "I'm sorry [mom_name], but we aren't going to just hang around at your house until you find where your son Ron misplaced his cash."
                R "My name's [ryan], actually."
                J "So either you've got it, or you don't."
                scene bg FrontDoor04
                with dissolve
                J "And it looks like you don't got it."
                J "So [mom_name], Why don't we go ahead and jump in the car."
                R "I'm so sorry Mom! I really have it. I just don't have a clue where it is right now."
                M "It's ok honey. We'll find it, and at least I won't have to go next week."
                RT "{i}Shit!.... She looks so sad!{/i}"
                "{i}{b}\"Mom's Affection -5\"{/b}{/i}"
                "{i}{b}\"Mom's Respect -1\"{/b}{/i}"
                $ momaffection -= 5
                $ momrespect -= 1
            else:
                R "Sorry, Mom! I wasn't able to get enough money together this week."
                M "Oh sweety, don't worry about it. It was just too much to ask of you."
                RT "{i}Oh no! I feel like a piece of shit! Look how sad I've made her.{/i}"
                "{i}{b}\"Mom's Affection -5\"{/b}{/i}"
                "{i}{b}\"Mom's Respect -1\"{/b}{/i}"
                $ momaffection -= 5
                $ momrespect -= 1
            J "Ok, Let's get on our way."
            scene bg FrontDoor05
            with dissolve
            RT "{i}There she goes off to the club.{/i}"
            RT "{i}She seemed extra down tonight.  I'd better jump on my scooter and head down to the club to make sure she's ok.{/i}"
            scene bg SleepBlack
            with fade
            $ renpy.pause ()
            scene bg SidClub06
            with fade
            ST "{i}Hopefully Mom doesn't mind if I borrow the car.{/i}"
            ST "{i}And that must be them driving off.{/i}"
            ST "{i}Now to follow from a discreet distance.{/i}"
            scene bg SleepBlack
            with fade
            scene bg SidClub07
            with fade
            $ renpy.pause ()
            scene bg SidClub08
            with fade
            ST "{i}So, this is the Mafia's club. It's pretty well hidden.{/i}"
            ST "{i}I never could have found it on my own.{/i}"
            ST "{i}I'll just go park around the corner.{/i}"
            ST "{i}Hopefully I can get in.{/i}"
            ST "{i}Somehow [ryan] was able to get in. I'm sure I'll find a way too.{/i}"
            scene bg SleepBlack
            with fade
            scene bg SidClub09
            with fade
            S "Uhhh.... Hi.... Can I come in?"
            G "Do you know the password?"
            S "Uhh.... is it Scarface?"
            G "Is that supposed to be a joke?"
            S "Ummmm.... I don't actually know the password.... But, my mom is one of the dancers, and I was hoping to go see her."
            G "Oh really?  Which one?"
            S "Ummm.... [mom_name]."
            G "Oh yeah, [mom_name], of course! Why didn't you just say so in the first place."
            G "We are, after all, a family establishment, and we try to be very accommodating to the families of our employees."
            S "Ummm.... Thank you?"
            G "Of course.... Come on in."
            scene bg SidClub10
            with dissolve
            $ renpy.pause ()
            scene bg SleepBlack
            with fade
            play music ClubMusic
            scene bg SidClub12
            with fade
            ST "{i}Wow! This place is so much bigger than it looks from the outside.{/i}"
            ST "{i}And so many important people. I think I saw State Senator McFeely by the craps table.{/i}"
            ST "{i}And I think I recognized that creep that was making lude gestures at me from the slot machine.{/i}"
            ST "{i}I think it was that school board member that Mom hates. I think his name is Bill, or Will Tylor, or something.{/i}"
            scene bg SidClub13
            with fade
            J "Well, hello there young lady."
            S "Oh shit!.... You scared me."
            J "I'm so sorry, allow me to introduce myself."
            scene bg SidClub14
            with dissolve
            J "My name is Joey DeCapo."
            J "And you must be [mom_name]'s oldest.... Sidney.... I think?"
            S "Yes.... but how did you?...."
            J "I pay a lot of people a lot of money to make sure I know everything about everyone of interest to me."
            J "And your family has been very interesting this last little while."
            scene bg SidClub15
            with dissolve
            J "But I must say that you are much prettier in person."
            J "You don't look very much like your mother. Maybe you take after your dad's side of the family?"
            scene bg SidClub16
            with dissolve
            S "Uhhhh.... Thank you?"
            S "And you're the guy we have to pay every week to keep our mom out of the club?"
            J "A very regrettable situation, but in life, all debts must be paid."
            S "But Dad took out the loan, not us."
            J "And when he took it out, we made sure it was very clear to him that the debt would fall on his family if anything happened to him."
            J "So, he knew the risks."
            S "That asshole!"
            J "Haha.... We can arrange for him to stay in prison for as long as you like."
            S "We might just take you up on that offer."
            J "But where are my manners. Let's go sit down and have a drink."
            J "Come.... Follow me."
            scene bg SidClub17
            with fade
            J "This is the pole room, and this is our very lovely dancer Emma."
            S "She's very beautiful."
            J "Yes, she's quite popular, but not nearly as popular as your mother."
            S "Oh God!.... She's here isn't she?"
            J "Haha.... yes, she's in the dressing room, she goes on after the next dancer."
            J "Shall we take a seat?"
            scene bg SidClub18
            with dissolve
            J "I want you to know that I feel very sorry for your family's situation."
            J "And I know I'm in an awkward position to help you all out, being your creditor and all."
            J "But I have a way you can help your family make the monthly payments, and maybe get you some spending money besides."
            J "I heard how the FBI cut out your discretionary spending."
            S "I'm not becomming a stripper, if that's what you're thinking."
            J "Haha.... No of course not!  We wouldn't hire you even if you wanted to."
            S "What?.... Why not?"
            J "You don't have the dancing experience like your mother does."
            J "But I do have another decent paying job that doesn't take any experience to get into, and only requires a pretty face."
            S "What would that be?"
            J "Take a look over there."
            scene bg SidClub19
            with dissolve
            J "Do you see that girl in the tights and blue shirt serving drinks to the customers?"
            S "Yeah."
            J "Well, she wants to be a bartender, so I'm letting her help tend the bar whenever things get a little slower."
            J "So, she needs some help filling her job while she's practicing her drink mixing skills."
            J "Let me call her over here so you can meet her."
            scene bg SidClub20
            with dissolve
            J "HEY! Armani!  Can I get a couple drinks?"
            scene bg SidClub21
            with fade
            A "Hey Uncle!  Do you want the usual?"
            J "Yes darling!, and get Sidney here whatever she wants."
            S "I don't want anything. I'm actually not old enough to buy a drink."
            J "Yeah, well regular rules don't apply here."
            S "I'm really ok."
            J "Suit yourself."
            J "Armani, this is Sidney.... She's thinking about coming here sometimes to help you serve drinks."
            J "Sidney, this is my neice Armani."
            scene bg SidClub22
            with dissolve
            A "Aren't you a pretty thing?"
            S "I wasn't really thinking about serving drinks...."
            J "Not yet, you mean."
            A "Well, I would sure love to work with someone as beautiful as you, and we can make a ton in tips in one night."
            A "So, think about it."
            scene bg SidClub23
            with dissolve
            J "And you'd be under very little commitment.  I would only require you to be here on Mondays, since that's when Armani's at the bar full time."
            J "Other than that, you could come in any day you want.  Oh.... except Saturdays, since your mother might be here."
            ST "{i}That doesn't sound bad at all.{/i}"
            ST "{i}And I'd love to be able to help [ryan] out.  He's taken most of the responsibility on himself.{/i}"
            S "That's a very tempting offer."
            J "Well, then why don't you run along with Armani and she can show you the ropes. You can keep any tips you make tonight."
            S "Ok.... Thank you."
            scene bg SidClub24
            with dissolve
            J "Oh.... and Sidney! I almost forgot."
            J "It would be best if your mother didn't know that you were here. If you are inclined to peek like your brother does, just don't get caught."
            J "I don't even think my best \"Made Man\" could stop her from murdering me, if she knew you were here."
            ST "{i}Does [ryan] regularly peek at Mom when she's stripping?{/i}"
            S "Ok.... I'll be careful."
            scene bg SleepBlack
            with fade
            $ renpy.pause ()
            scene bg SidClub11
            with fade
            R "Hey Lurch, How's it hanging?"
            R "Are you just gonna leave me hanging?"
            "...."
            R "Alright, I'll just show myself in then."
            scene bg WalkingBar
            with fade
            play music ClubMusic
            if money >= 1000:
                RT "{i}Why wasn't I more careful with my money this week?  I hate how dissapointed my mom looks when I fail to pay off the mob.{/i}"
                RT "{i}I hate seeing Mom look so disappointed. And where the hell did I put that money?{/i}"
            else:
                RT "{i}Why wasn't I more careful with my money this week?  I hate how disappointed Mom looks when I fail to pay off the mob.{/i}"
                RT "{i}I hope she's ok.{/i}"
            scene bg WalkingCasino
            with fade
            RT "{i}Past the bar, through the casino, and Bingo!{/i}"
            scene bg SidClub25
            with fade
            RT "{i}Oh wow! Now I don't feel so bad!{/i}"
            RT "{i}I never would have seen her in that outfit otherwise.{/i}"
            scene bg SidClub27
            with fade
            RT "{i}I sure wish I had access to the club's wardrobe.{/i}"
            RT "{i}Mom pulls off the edgy look really well!{/i}"
            scene bg SidClub26
            with fade
            RT "{i}Oh God, but she looks even better when she's not wearing it at all.{/i}"
            RT "{i}How are her tits so perky?  Did she even breastfeed us at all? Mmmm.... I wish I could remember that.{/i}"
            RT "{i}And that's about all the self control I have.{/i}"
            scene SidClubVideo01
            with dissolve
            RT "{i}Oh and that ass is to die for!{/i}"
            $ renpy.pause ()
            scene SidClubVideo03
            with fade
            $ renpy.pause ()
            scene SidClubVideo02
            with fade
            RT "{i}One day, I'll get her moving like that in front of my camera.{/i}"
            $ renpy.pause ()
            scene bg SidClub28
            with fade
            $ renpy.pause ()
            scene bg SidClub29
            with dissolve
            ST "{i}Oh my God! Is that guy doing what I think he's doing?{/i}"
            ST "{i}That's disgusting!{/i}"
            scene bg SidClub30
            with dissolve
            S "Hey buddy! I don't think you're supposed to be...."
            ST "{i}Wait!.... I recognize that sweatshirt!{/i}"
            stop music
            play sound Scratch
            scene bg SidClub31
            with fade
            S "[ryan]!.... What the fuck?"
            play music ClubMusic
            R "Holy fuck!.... Sidney what are you wearing, and what the hell are you doing here?"
            scene bg SidClub68
            with dissolve
            S "I might ask you the same thing, but I think that's pretty obvious."
            S "I can't even believe you would do that in public. Do you have no shame?"
            R "...."
            R "It's not really about not having any shame, more just a lack of self control."
            S "Hmmm.... Yeah, I can see that."
            S "So, is it still Emma out there on the stage?"
            R "Uuuhhh.... Yeah, she's.... really doing a great job."
            S "Scoot over, I want to take a peek."
            scene bg SidClub32
            with fade
            R "Uhhh.... wait!  I don't think that's a good idea."
            S "What? Why the hell not?"
            R "Ummm.... What if you like what you see, and want to become a pole dancer yourself? I just want to protect you from that."
            S "[ryan], that is the stupidest thing I've ever heard. Now, move over!"
            R "Uhhhh.... No...."
            S "Move over, or I'll scream and draw attention to your little jack off session."
            R "Shit Sidney!.... Just.... Fine...."
            scene bg SidClub33
            with dissolve
            RT "{i}Fuck!.... She's gonna freak out, she's going to tell Mom! My life is over!{/i}"
            S "What the actual fuck, [ryan]?"
            S "You've been jacking off to Mom?"
            scene bg SidClub34
            with dissolve
            S "What the hell is wrong with you?"
            S "I mean.... Just.... Do you care to explain yourself?"
            RT "{i}Ok brain.... I need you to come through for me.  I need your bullshit capabilities like never before.{/i}"
            RT "...."
            R "Sorry.... I don't know what to say, you know?.... I guess I got a little messed up the first time I saw Mom stripping, and I can't stop coming back when I know she's going to be here."
            R "But I'm not sorry!  If that hadn't happened, I would have stayed a prude, and freaked out when you started jacking me off in your sleep."
            scene bg SidClub69
            with dissolve
            RT "{i}If there's a hell, I'm sure I'm going there for that stunt.{/i}"
            R "I would have freaked out and kicked you out, told Mom, and you probably would have been kicked out of the house. Then we wouldn't have gotten as close as we have this past little while."
            R "Which has been one of the only good things that's been going on for me amidst all the shit with Dad and the Mafia."
            R "I guess I'm just trying to tell you how much I've loved getting closer to you."
            R "...."
            scene bg SidClub35
            with dissolve
            S "That's really sweet..."
            R "Really?...."
            S "Probably eighty percent bullshit, but still sweet, nonetheless."
            S "I also would have accepted the argument that you were just really, really, horny."
            R "Excuse me?"
            S "Yeah,  I realized about halfway through your moving speech, that I have no room to be critical of you."
            S "I mean, look at the questionable decisions I've been making lately."
            S "And I feel partly responsible for the progression of your perversions, because of the.... well you know."
            S "And I get that Mom's a total babe.... I mean, she doesn't do a lot for me, but I get why a horny teenage boy would want to see more of her."
            S "Even if she's his mother."
            R "Wow.... I thought you would be disgusted in me."
            S "Well, you definitely don't have a monopoly on perversion in this family.  I mean just take a look around that corner for example."
            S "And I've been going through some stuff myself lately."
            S "We've just got to be careful not to go too far."
            S "I'm not worried too much with your little crush on Mom."
            S "It's not like anything could actually ever come of it."
            RT "{i}Well, we'll see.{/i}"
            S "And I'm sure it will pass quickly."
            RT "{i}Not likely.{/i}"
            S "The stuff we're doing together is just to help keep our hormones in check until we both have other people to do it for us."
            S "So yeah, let's just be careful."
            R "...."
            R "Hey Sid?"
            S "Yeah?"
            R "I need some hormone checking really bad right now!"
            scene bg SidClub69
            with dissolve
            S "Are you kidding me?"
            S "Right now?.... Right here?...."
            R "Yeah, I mean you kind of interrupted me in the middle of my thing...."
            S "Ok.... I'll leave and let you get back to it."
            R "No.... I mean.... I was hoping you could help me out."
            S "...."
            S ".... I guess.... I did say...."
            S "Alright.... Just this once."
            scene bg SleepBlack
            with fade
            scene bg SidClub36
            with fade
            ST "{i}Wow!.... My poor brother is so horny right now!{/i}"
            ST "{i}And the poor kid thinks it's all his fault.{/i}"
            ST "{i}When I'm the one who started doing stuff to him while he was sleeping.{/i}"
            ST "{i}I'm the one who hid his money so Mom would have to come here tonight.{/i}"
            ST "{i}This is the least I can do for him.{/i}"
            S "Hey [ryan]?"
            R "Yeah?"
            S "You need to finish in my mouth, since I don't want cum anywhere on my face or outfit."
            R "That's a sacrifice I'm willing to make."
            S "Haha.... smartass!"
            scene SidClubVideo04
            with dissolve
            $ renpy.pause ()
            play sound Blow02 loop
            RT "{i}What just happened?....{/i}"
            RT "{i}When Sidney caught me, I thought it would be game over.{/i}"
            RT "{i}And now, she's giving me a blowjob, while Mom is stripping just a few feet away.{/i}"
            RT "{i}I have to be dreaming.... I'm sure I'm going to wake up in my bed in a few minutes with sticky sheets.{/i}"
            $ renpy.pause ()
            scene bg SidClub45
            with fade
            ST "{i}Holy Shit!.... Is my life a porn movie?{/i}"
            ST "{i}Here I am, giving my own brother a blowjob in a stripclub.{/i}"
            ST "{i}Just around the corner, I can see our mom doing a strip dance for a bunch of Mafia guys.{/i}"
            ST "{i}Even when I was scheming to get Mom here, I'd have never guessed the night would end up like this.{/i}"
            scene bg SidClub44
            with fade
            stop sound
            MT "{i}Holy shit! Is that waitress giving that guy over there a blowjob in the middle of my dance?{/i}"
            MT "{i}What a couple of filthy degenerates!{/i}"
            MT "{i}I wonder what kind of mother could raise such blatantly perverted sickos.{/i}"
            MT "{i}Did watching my dance just make them so excited they couldn't control themselves?{/i}"
            MT "{i}Fuck!.... I'm getting turned on again!.... I hope I don't make the pole too slippery for the rest of my dance.{/i}"
            "{i}{b}\"Mom's Libido +3\"{/b}{/i}"
            $ momlibido += 3
            $ sidney_spy = True
            play sound Blow02
            scene SidClubVideo04
            with fade
            $ renpy.pause ()
            play sound Blow03 loop
            jump club_tip_bj

label tv_together:
    if laurenlibido <= 7:
        scene bg LaurenPonieTV
        with fade
        menu:
            "Watch TV with Lauren":
                scene bg GOT01
                with fade
                play music SexMusic
                L "Hey [ryan], do you want to watch something with me?"
                R "Ok, should we watch the next episode of \"Game of Thots\"?"
                scene bg GOT02
                with dissolve
                L "I don't know, it's getting pretty scary!"
                L "Those white walkers creep me out so bad!"
                R "You don't want to miss the rest of the show just because of the white walkers, do you?"
                L "Well.... No.... but can I at least sit really close to you in case I get too scared?"
                R "Of course!"
                scene bg GOT03
                with fade
                L "Thanks! I feel so much safer!"
                R "Me too!"
                R "Let's start the episode."
                scene bg SleepBlack
                with fade
                scene bg GOT04
                with fade
                L "Aaahhh!.... protect me, [ryan]!"
                R "Uuuggghhh.... That is just.... not right!"
                scene bg SleepBlack
                with fade
                scene bg GOT05
                with fade
                L "Holy shit!  A blowjob on every episode!"
                scene GOTVideo01
                with fade
                $ renpy.pause ()
                R "Well, at least you're clearly enjoying it?"
                L "What do you mean?"
                R "The way you're rubbing yourself."
                scene bg GOT06
                with fade
                L "Oh my God! Was I really?"
                R "Well, yeah.... You didn't notice?"
                scene bg GOT07
                with dissolve
                L "No!.... Sometimes I do it without thinking."
                R "Well.... Do you need some relief?"
                R "Do you want me to help?"
                scene bg GOT06
                with dissolve
                L "What?.... No!"
                L "I might be rubbing myself unconsciously, but I'm not desperate enough to ask you for help."
                R "Well.... Ok.... But if you ever do get desperate enough...."
                R "Don't forget what they teach us in school."
                R "You don't have to be ashamed to ask for help."
                scene bg GOT08
                with dissolve
                L "You overconfident idiot!  Can we get back to the show now?"
                R "Of course!.... I'm not the one causing interruptions."
                L "Clearly."
                scene bg GOT05
                with dissolve
                LT "{i}I can't believe [ryan] caught me rubbing myself.{/i}"
                LT "{i}I was doing it right next to him.{/i}"
                LT "{i}While watching a TV show about a woman blowing her brother.{/i}"
                LT "{i}How many blowjobs is Cersei going to give her brother this season anyways?{/i}"
                LT "{i}Where's my self-control?{/i}"
                "{i}{b}\"Lauren's Libido +2\"{/b}{/i}"
                $ laurenlibido += 2
                $ timeofdaycounter += 1
                play music Honey
                scene bg SleepBlack
                with fade
                jump lounge
            "Never mind":
                scene bg LaurenPonieTV
                $ screen_on = "laurenponietvmap"
                call screen laurenponietvmap
    if tv_events >= 4:
        scene bg LaurenPonieTV
        with fade
        menu:
            "Watch TV with Lauren":
                scene bg GOT01
                with fade
                play music SexMusic
                L "Hey [ryan], do you want to watch something with me?"
                R "Ok, let's watch the next episode of \"Game of Thots\"!"
                scene bg GOT02
                with dissolve
                L "Well.... As long as I can sit close to you again, in case I get too scared?"
                R "Of course!"
                scene bg GOT03
                with fade
                L "Thanks! I feel so much safer!"
                R "Me too!"
                R "Let's start the episode."
                scene bg SleepBlack
                with fade
                scene bg GOT04
                with fade
                L "Aaahhh!.... protect me, [ryan]!"
                R "Uuuggghhh.... That is just.... not right!"
                scene bg SleepBlack
                with fade
                scene bg GOT05
                with fade
                R "Well, we've reached the mandatory sex scene for this episode!"
                scene bg GOT08
                with fade
                L "So, does that mean you're ready for some foolin' around?"
                R "I love that you're taking the initiative now!"
                scene bg GOT07
                with dissolve
                L "Yeah, well.... We both know we can't keep doing this.... So, this has to be our last time."
                R "Ok.... It's a deal."
                RT "{i}Haha.... She can't stop now!{/i}"
                L "So, what should we do?"
                menu:
                    "Can I get a handjob?":
                        jump lounge_hj
                    "Do you want me to finger you again?":
                        jump lounge_finger
                    "How about another blowjob?":
                        jump lounge_bj
            "Never mind":
                scene bg LaurenPonieTV
                $ screen_on = "laurenponietvmap"
                call screen laurenponietvmap
    if tv_events == 3:
        scene bg LaurenPonieTV
        with fade
        menu:
            "Watch TV with Lauren":
                scene bg GOT01
                with fade
                play music SexMusic
                $ persistent.gal_Lauren_6 = True
                L "Hey [ryan], do you want to watch something with me?"
                R "Ok, let's watch the next episode of \"Game of Thots\"!"
                scene bg GOT02
                with dissolve
                L "Well.... As long as I can sit close to you again, in case I get too scared?"
                R "Of course!"
                scene bg GOT03
                with fade
                L "Thanks! I feel so much safer!"
                R "Me too!"
                R "Let's start the episode."
                scene bg SleepBlack
                with fade
                scene bg GOT04
                with fade
                L "Aaahhh!.... protect me, [ryan]!"
                R "Uuuggghhh.... That is just.... not right!"
                scene bg SleepBlack
                with fade
                scene bg GOT05
                with fade
                L "I'm amazed at how the actress who plays Cersei can get his cock all the way down her throat."
                R "Yeah, she's definitely talented."
                scene bg GOT07
                with fade
                L "How do you even think it's possible?"
                R "I don't know.... Do I look like an expert on sucking cocks?"
                scene bg GOT08
                with dissolve
                R "Don't answer that!"
                scene bg GOT07
                with dissolve
                L "I wonder if I could do it too."
                R "I guess you'd just have to take it slow, and see if you can suppress your gag reflex."
                R "I'm willing to be your guinea pig, if you want to try."
                scene bg GOT06
                with dissolve
                L "What?.... I couldn't suck my brother's dick!"
                R "Are you really pretending to be shocked by my suggestion?"
                R "You know you only brought it up because you've been wanting to try it."
                scene bg GOT08
                with dissolve
                L "Well.... when I know I shouldn't do something, but I really want to do it anyways...."
                L "Shouldn't I at least pretend I don't want to?"
                R "I guess if it makes you feel better that you're trying to talk yourself out of it."
                R "But you don't have to pretend for my sake."
                scene bg GOT07
                with dissolve
                L "Hmmmm.... well.... that gives me a lot to think about."
                L "But how about I think about it later."
                L "Right now I want to learn a new skill."
                scene bg SleepBlack
                with fade
                scene bg GOT29
                with fade
                L "I have been experimenting with a dildo, but it's not nearly as big as you."
                L "So, don't be too disappointed if I don't do a very good job."
                R "Don't worry, Lauren!  I'm going to love it just because it's you doing it!"
                L "I hope that's true."
                scene bg GOT40
                with dissolve
                play sound Blow02 loop
                R "Oh yeah, Lauren, it's already feeling great!"
                scene GOTVideo07
                with fade
                $ renpy.pause ()
                LT "{i}Wow, it's so big, I can barely get my mouth around it.{/i}"
                LT "{i}How am I going to get it down my throat?{/i}"
                $ renpy.pause ()
                R "That's great, Lauren!.... You should see if you can go a little deeper."
                menu:
                    "Deeper":
                        scene GOTVideo08
                        with dissolve
                        stop sound
                        play sound Blow03 loop
                        $ renpy.pause ()
                LT "{i}Oh my God!.... Don't gag, don't gag, don't gag!{/i}"
                R "Oh, God!...."
                $ renpy.pause ()
                R "You're doing incredible.... but are you ready to really develop your skill?"
                menu:
                    "Throat fuck":
                        scene GOTVideo09
                        with dissolve
                        $ renpy.pause ()
                LT "{i}I'm doing it?.... Holy shit, I'm swallowing his hog!{/i}"
                LT "{i}I guess all that practice with my dildo paid off.{/i}"
                R "Oh my God, Lauren!  How are you so good for your first time?"
                LT "{i}Yay!.... He likes it!{/i}"
                $ renpy.pause ()
                R "Oh fuck, Lauren! I'm getting close!"
                R "Don't be alarmed, but I'm going to shoot it down your throat!"
                L "Mmmmpphhh...."
                R "Don't worry!  You can do this!"
                L "Bllerrrgggghhh...."
                R "You have to do this! Mom will kill me if she sees any more bodily fluids in the lounge."
                $ renpy.pause ()
                R "Oh, fuck!.... Here it comes!"
                stop sound
                scene bg GOT41
                with dissolve
                $ renpy.pause ()
                play sound Ejaculate
                scene bg GOT42
                with dissolve
                $ renpy.pause ()
                play sound Ejaculate
                $ renpy.pause ()
                scene bg GOT43
                with fade
                L "Holy fuck, I did it!"
                R "You did amazing!"
                R "Are you sure that's your first time?"
                L "I promise!"
                R "Well, then an extra \"Wow!\" to you!"
                scene bg GOT44
                with fade
                L "Shit!.... Right on time! Mom's shower just turned off."
                R "Fuck!.... Help me find my shorts!"
                scene bg GOT45
                with fade
                R "Oh, thank God!.... We made it this time."
                R "Oh, wait!.... Fuck.... Lauren, you still have cum on your...."
                scene bg GOT50
                with dissolve
                M "Hey guys!.... Watching your dragon show again?"
                scene bg GOT46
                with dissolve
                L "It's not just about dragons, its...."
                M "Hey Lauren, you've got something dripping from your bottom lip."
                RT "{i}Oh, fuck!.... Lauren's the worst liar!{/i}"
                L "Do I?.... Oh.... It must be frosting from the cinnamon roll I was eating earlier."
                L "How embarassing."
                scene bg GOT47
                with dissolve
                L "Mmmmm...."
                scene bg GOT48
                with dissolve
                L "Still tastes good!"
                RT "{i}Holy shit!.... My boner's back!{/i}"
                LT "{i}Holy shit!.... I just licked up my brother's cum in front of our mom!{/i}"
                "{i}{b}\"Lauren's Libido +2\"{/b}{/i}"
                $ laurenlibido += 2
                MT "{i}Oh, fuck!.... That looked like Lauren was licking cum off her lips{/i}"
                MT "{i}Why do I have to have such a perverted imagination?{/i}"
                "{i}{b}\"Mom's Libido +10\"{/b}{/i}"
                $ momlibido += 10
                L "Did I get it?"
                M "Yep.... You two have fun! I'm going to run to my room and.... get some clothes on."
                scene bg GOT01
                with dissolve
                R "Holy fuck, Lauren!.... That was hot!"
                L "Haha.... I thought you'd like that!"
                scene bg SleepBlack
                with fade
                $ timeofdaycounter += 1
                $ tv_events = 4
                play music Honey
                jump lounge
            "Never mind":
                scene bg LaurenPonieTV
                $ screen_on = "laurenponietvmap"
                call screen laurenponietvmap
    if tv_events == 2:
        scene bg LaurenPonieTV
        with fade
        menu:
            "Watch TV with Lauren":
                scene bg GOT01
                with fade
                play music SexMusic
                L "Hey [ryan], do you want to watch something with me?"
                R "Ok, let's watch the next episode of \"Game of Thots\"!"
                scene bg GOT02
                with dissolve
                L "Well.... As long as I can sit close to you again, in case I get too scared?"
                R "Of course!"
                scene bg GOT03
                with fade
                L "Thanks! I feel so much safer!"
                R "Me too!"
                R "Let's start the episode."
                scene bg SleepBlack
                with fade
                scene bg GOT04
                with fade
                L "Aaahhh!.... protect me, [ryan]!"
                R "Uuuggghhh.... That is just.... not right!"
                scene bg SleepBlack
                with fade
                scene bg GOT05
                with fade
                L "I was just curious what you think about Cersei's and Jamie's relationship on \"Game of Thots\"."
                R "Well, if it isn't hurting anyone else, then who cares?"
                L "Well, it did hurt someone else. Jamie pushed that Bran kid out the window, so that no one would find out."
                R "Well, as bad as that is, the real crime is that their society looks so down on the way they choose to live their lives, that Jamie felt like he had to do that to protect the girl he loves."
                L "Yeah.... I never thought about it like that."
                R "People should just \"live and let live\"."
                R "If Cersei wants to suck her brother's dick, then what business is that of anybody else?"
                scene GOTVideo01
                with fade
                R "At least you clearly enjoy it."
                R "Lauren.... You're rubbing yourself again."
                L "I know.... You don't mind, do you?"
                L "\"Live and let live\", is what you said."
                R "Oh.... Hell no.... I don't mind."
                R "But I think I could do something for you that would feel even better."
                scene bg GOT07
                with fade
                L "I don't know.  you said Mom was pretty pissed about the cum all over her table the other day."
                L "Plus, you already helped me out once, and I've helped you out once too. Now we're even."
                R "Yeah, but I didn't give you an orgasm, where you clearly gave me one."
                R "Have you ever had anyone, besides yourself, give you an orgasm?"
                L "No.... I haven't."
                R "Are you sure you don't want to try?"
                scene bg GOT08
                with dissolve
                L "Well.... when you put it that way...."
                R "Awesome!"
                R "I want you to get on your hands and knees this time."
                L "What? Why?"
                R "Something I saw in a porno.... I think you'll like it."
                scene bg GOT06
                with dissolve
                L "Wait!  They do a lot of dirty, scary things in pornos."
                R "Don't worry.  I wouldn't do it, if I didn't think you'd like it."
                L "I hope not!"
                R "And risk you not wanting to ever fool around again?"
                L "Well!.... we should make it a goal never to fool around again!"
                L "We are brother and sister after all."
                scene bg GOT07
                with dissolve
                L "But let's just do it this last time."
                RT "{i}Like a broken record.{/i}"
                scene bg SleepBlack
                with fade
                scene bg GOT15
                with fade
                L "Ok.... Is this the position?"
                R "Lauren, you have no idea how amazing this position looks from my perspective!"
                L "Oh, shut up!  Are you going to leave me waiting all day?"
                R "Oh, right!.... Sorry!"
                scene bg GOT16
                with fade
                R "Ok.... brace yourself!.... Don't cry out in ecstasy!.... remember that Sidney might hear."
                L "Stop making me wait!"
                scene bg GOT17
                with fade
                L "Oh wait, oh wait, oh wait!"
                L "That's my butt-hole!"
                L "I don't think I want you going in there."
                R "Just relax!"
                R "I've read that most dirty girls love this."
                L "I'm not a dirty girl though...."
                R "Well.... we won't know until we try."
                L "I don't know!...."
                R "Don't worry!  It's just one finger."
                R "If you hate it, I'll stop."
                L "Ok, but you don't stop when I say to, I'll scream, and you can explain to Mom and Sidney what's been going on between us."
                R "Alright.... Deal!"
                scene GOTVideo04
                with dissolve
                $ renpy.pause ()
                L "Oh, wow!.... That's a different feeling!"
                L "Hnnnnggghhh...."
                $ renpy.pause ()
                L "Ok.... I'm starting to get used to it!"
                play sound Lauren01 loop
                $ renpy.pause ()
                L "Ohh.... That's starting to feel good!"
                scene GOTVideo05
                with fade
                $ renpy.pause ()
                L "Oh fuck, oh fuck, oh fuck!"
                scene bg GOT17
                with fade
                stop sound
                L "Hey, why did you stop?"
                R "I was just wondering if you're liking this."
                L "Ummmm.... well.... yeah, it does feel a lot better than I thought it would."
                R "So, should I keep going?"
                L "Yes! Hurry! We don't have much time before Mom finishes her shower!"
                R "So.... Are you a dirty girl then?"
                L "What?"
                R "You know, that thing I read, that only dirty girls enjoy this?"
                L "[ryan]! Just shut up and fuck me with those fingers!"
                R "Ok, but first you have to tell me that you're a dirty girl."
                L "What? You are so weird, [ryan]!"
                R "If you want me to continue, you have to say it."
                L "Fine!  {i}(mumbling){/i} I'm a dirty girl."
                R "Oh, come on Lauren! Like you believe it!"
                L "Now you sound like a creepy motivational speaker."
                R "...."
                L "Fine!.... I'm a dirty girl!"
                R "Ssshhhh.... Not so loud!.... Sidney will hear you!"
                L "[ryan]! I'm going to kill you!"
                R "Hahaha.... Ok, ok!"
                scene GOTVideo04
                with dissolve
                play sound Lauren01 loop
                $ renpy.pause ()
                L "Oh.... Thank God!...."
                L "That feels so good!"
                scene GOTVideo05
                with fade
                $ renpy.pause ()
                LT "{i}Holy shit! I can feel an orgasm coming on!{/i}"
                LT "{i}It's feeling like it's going to be a big one!{/i}"
                $ renpy.pause ()
                L "Ohhh.... Fuuuck!"
                stop sound
                play sound Ejaculate
                scene bg GOT18
                with fade
                $ renpy.pause ()
                RT "{i}Oh.... my.... God!....{/i}"
                scene bg GOT19
                with dissolve
                L "Holy shit, [ryan]! That's the best orgasm I have ever had!"
                "{i}{b}\"Lauren's Libido -5\"{/b}{/i}"
                $ laurenlibido -= 5
                R "Wow!.... I didn't even know it was possible for a girl to squirt so much!"
                L "Oh, God!.... I'm so embarassed!"
                R "No.... Don't be.... That was amazing!"
                scene bg GOT20
                with dissolve
                R "Oh, shit!.... Is that?...."
                L "Mom's shower stopped!"
                scene bg GOT21
                with dissolve
                R "Where are you going?"
                R "You need to clean this up!"
                L "Mom will kill me if she catches me without pants! Good luck!"
                scene bg GOT22
                with fade
                RT "{i}And how am I supposed to explain this?{/i}"
                RT "{i}Wow!.... It's still warm.{/i}"
                scene bg GOT23
                with dissolve
                M "[ryan]! What did you spill all over my couch?"
                R "Oh!.... Goddammit!  You scared the shit out of me!"
                scene bg GOT24
                with fade
                M "[ryan]? Would you please mind your language?"
                R "Sorry Mom, but you really did startle me."
                M "Sorry, I didn't mean to! I just saw that you'd spilled somthing all over my couch!"
                R "Oh.... yeah.... sorry about that!  I just knocked over a glass of water. I was about to clean it up."
                M "Where's the glass?"
                R "Oh, it.... must have rolled under the coffee table or something."
                M "Well, ok.... Just clean it up fast. Even though the couch is leather, I don't think it's good for it if liquids sit on it too long."
                menu:
                    "I'll go grab a towel.":
                        R "Alright Mom! I'll just run grab a towel!"
                        scene bg GOT25
                        with dissolve
                        M "Thanks honey, and please try to hurry before it drips between the cushions."
                        R "I'll take care of it!"
                    "Can I use your towel, then?":
                        if momaffection >= 18:
                            scene bg GOT25
                            with dissolve
                            M "Haha.... you cheeky bastard!"
                            R "Mom.... calling me a bastard is more of an insult to you than to me!"
                            M "Oh.... You're right!"
                            M "Well, stop being a smartass and get this cleaned up before it leaks between the cushions."
                            MT "{i}Where does he get the confidence to ask his own mother to borrow the towel she's covering herself with?{/i}"
                            MT "{i}I've got to give him credit for the effort.{/i}"
                            "{i}\"Mom's respect +1\"{/i}"
                            $ momrespect += 1
                            MT "{i}And for daring to use such a sexually charged suggestion.{/i}"
                            "{i}\"Mom's Libido +1\"{/i}"
                            $ momlibido += 1
                        else:
                            M "[ryan].... That wasn't funny, and it was a very inappropriate thing to say to your own mother."
                            "{i}{b}\"Mom's Anger +1\"{/b}{/i}"
                            $ momanger += 1
                            R "Ok.... sorry Mom, I'll just run grab a towel from the kitchen then."
                            M "Make sure you hurry, before it drips down between the cushions."
                            R "Yes Mom."
                scene bg SleepBlack
                with fade
                $ timeofdaycounter += 1
                $ tv_events = 3
                play music Honey
                jump lounge
            "Never mind":
                scene bg LaurenPonieTV
                $ screen_on = "laurenponietvmap"
                call screen laurenponietvmap
    if tv_events == 1:
        scene bg LaurenPonieTV
        with fade
        menu:
            "Watch TV with Lauren":
                scene bg GOT01
                with fade
                play music SexMusic
                L "Hey [ryan], do you want to watch something with me?"
                R "Ok, let's watch the next episode of \"Game of Thots\"!"
                scene bg GOT02
                with dissolve
                L "I don't know, it's getting pretty scary!"
                L "Those white walkers creep me out so bad!"
                R "You don't want to miss the rest of the show just because of the white walkers, do you?"
                L "Well.... No.... but can I at least sit really close to you again, in case I get too scared?"
                R "Of course!"
                scene bg GOT03
                with fade
                L "Thanks! I feel so much safer!"
                R "Me too!"
                R "Let's start the episode."
                scene bg SleepBlack
                with fade
                scene bg GOT04
                with fade
                L "Aaahhh!.... protect me, [ryan]!"
                R "Uuuggghhh.... That is just.... not right!"
                scene bg SleepBlack
                with fade
                scene bg GOT05
                with fade
                L "Well.... There goes Cersei, sucking on her brother's dick again."
                L "Do you think that actor got that part because his cock is so huge?"
                R "Are you saying I should get into acting?"
                L "Haha.... No! Your dick isn't that big!"
                R "What are you talking about?"
                R "You've seen it!  You know it's that big!"
                L "Yeah.... well.... not the way I remember it."
                R "That's it!  I'm proving it to you!"
                L "Wait!....  No!.... [ryan]!...."
                scene bg GOT28
                with fade
                L "Oh my God....[ryan]!.... I can't believe you just whipped him out like that!"
                L "Sidney can look over and see us anytime she feels like it."
                scene bg GOT09
                with fade
                R "Yeah.... But she can't see what's going on behind the couch."
                R "And, like I said before.... She's too involved in her design work to ever look over here."
                scene bg GOT28
                with fade
                L "Yeah.... well.... I still think the actor who plays Jamie has you beat."
                R "What? Are you serious? Hmmm.... That's just because it looks extra big next to Cersei's head."
                R "You have to get down there and compare it to your head to get an accurate comparison."
                R "And while you're down there, maybe you can repay the favor I gave you last time?"
                scene bg GOT06
                with fade
                L "Ahhh!.... You asshole!  Are you suggesting I give you a blowjob?"
                R "What?.... No!...."
                RT "{i}Not yet....{/i}"
                R "I've just never had a handy from anybody besides myself."
                RT "{i}Not true.... but she doesn't know that.{/i}"
                R "And since I helped you out when you were feeling horny, I thought you might be willing to do the same for me."
                scene bg GOT07
                with dissolve
                L "What?.... Are you suggesting that you only fingered my pussy because you expected something in return?...."
                R "Well, I.... no, but.... I was thinking...."
                scene bg GOT08
                with dissolve
                L "Haha.... Just shittin' ya.... I'm happy to do a favor for my brother!"
                scene bg GOT29
                with fade
                L "Now that I'm down here, I declare the size difference between you and Jamie Slanister to be.... inconclusive."
                L "I really can't tell.... It's too damn close to call!"
                L "You should really be proud of yourself...."
                R "Well, I try not to brag."
                R "But how bout we.... you know...."
                R "We're kind of hurried for time."
                L "Oh, yeah.... That's right!"
                scene GOTVideo06
                with dissolve
                $ renpy.pause ()
                R "Wow, Lauren!.... That feels fucking great!"
                LT "{i}Holy shit!.... I'm jacking off my brother!....{/i}"
                LT "{i}I've never even looked at a cock this close before, and now.... I'm jacking off my brother?{/i}"
                LT "{i}Well.... I hope hell is nice.{/i}"
                LT "{i}.... This might all be fucking worth it though.{/i}"
                LT "{i}I've never felt so much happiness and excitement in my whole life before [ryan] and I started messing around.{/i}"
                R "Ohh.... Shit, Lauren!.... I'm about to cum!"
                L "Ohhh, fuck yeah!...."
                LT "{i}I've only ever seen a cock cum on a porno.  I can't wait to see it in real life!{/i}"
                play sound Ejaculate
                scene bg GOT30
                with fade
                with vpunch
                $ renpy.pause ()
                LT "{i}Wow!{/i}"
                play sound Ejaculate
                scene bg GOT31
                with fade
                $ renpy.pause ()
                LT "{i}Holy shit!.... There's even more!{/i}"
                "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                $ laurenlibido += 1
                scene bg GOT32
                with fade
                L "Oh my God!.... How long has Mom's shower been off?"
                R "Oh, shit!  I don't know!.... I was too preoccupied to notice when it turned off."
                scene bg GOT33
                with fade
                L "I'm getting out of here!"
                R "Wait!.... Help me find my shorts!"
                L "Sorry! You're on your own!"
                scene bg GOT34
                with dissolve
                R "Did I kick them under the coffee table?"
                scene bg GOT35
                with dissolve
                MT "{i}What in the hell?.... Why is [ryan] completely bare-assed in my lounge?{/i}"
                M "Uhhhh.... [ryan]? Do you mind telling me what you're doing?"
                scene bg GOT36
                with dissolve
                R "Oh.... Holy fuck.... Mom, you scared me!"
                M "[ryan], please watch your language."
                M "And please answer my question."
                MT "{i}Oh my God!.... His penis is just hanging out in the open!{/i}"
                MT "{i}Why isn't he trying to cover it up!{/i}"
                MT "{i}Don't look, don't look.{/i}"
                scene bg GOT39
                with dissolve
                R "What was the question?"
                M "Where are your penis.... I mean pants.... I meant pants!?"
                M "And why don't you cover yourself?"
                R "Oh.... Well, you've already seen me.... What difference does it make?"
                scene bg GOT36
                with dissolve
                M "Yeah, well I guess you're right...."
                scene bg GOT37
                with dissolve
                M "Oh my God!.... Is that what I think it is all over my coffee table?"
                M "[ryan]!.... You've got to be fucking kidding me!"
                R "Language, Mom."
                scene bg GOT38
                with dissolve
                M "Don't be a smart-ass with me!"
                M "Why in the hell did you blow your load all over my table?"
                menu:
                    "It's not what you think.":
                        R "Are you kidding me Mom? Do you really think I'd cum all over your table?"
                        M "Well?"
                        R "It's just some sugar glaze from a box of donuts I was eating."
                        M "Where's the box?"
                        R "Outside in the trash?"
                        M "I'm not that stupid!"
                        M "That story might be easier to believe if your pants weren't off."
                        "{i}\"Mom's Anger +3\"{/i}"
                        $ momanger += 3
                        M "You were jacking off to that dragon show, weren't you?"
                        M "I heard some of the other teachers talking about how sexual it can get."
                        M "That's what happened.... isn't it?"
                        R "Yes Mom.... There was a scene....that was fairly kinky.... So, I decided to.... practice good sexual health?"
                    "I was masturbating.":
                        R "Uhhh.... Well.... There was a scene on \"Game of Thots\"."
                        R "And it was a.... fairly kinky...."
                        R "So, I decided to.... practice good sexual health?"
                scene bg GOT36
                with dissolve
                M "Well.... Honey!"
                M "Practicing good sexual health is as important to me as it should be with any other mom."
                M "But you've got to realize there is a time and place for it."
                M "Like in your your room!  When nobody else is around!"
                M "Did you even notice that Sidney is working just over there in the kitchen?"
                R "Shit.... No!.... I didn't even notice!"
                M "Well, thank God Lauren didn't come out to watch TV with you today."
                M "Now find your shorts and clean off my coffee table, Goddammit!"
                scene bg GOT35
                with dissolve
                M "Holy shit!.... That is a lot of cum!"
                M "....Just....Wow!"
                R "Thanks Mom."
                M "Shut up [ryan]!"
                "{i}\"Mom's Anger +1\"{/i}"
                "{i}\"Mom's Libido +2\"{/i}"
                $ momanger += 1
                $ momlibido += 2
                scene bg GOT34
                with dissolve
                RT "{i}Oh.... Thank God Lauren ran off when she did!{/i}"
                RT "{i}And where the fuck are my shorts?{/i}"
                $ timeofdaycounter += 1
                $ tv_events = 2
                play music Honey
                scene bg SleepBlack
                with fade
                jump lounge
            "Never mind":
                scene bg LaurenPonieTV
                $ screen_on = "laurenponietvmap"
                call screen laurenponietvmap
    else:
        scene bg LaurenPonieTV
        with fade
        menu:
            "Watch TV with Lauren":
                scene bg GOT01
                with fade
                play music SexMusic
                L "Hey [ryan], do you want to watch something with me?"
                R "Ok, should we watch the next episode of \"Game of Thots\"?"
                scene bg GOT02
                with dissolve
                L "I don't know, it's getting pretty scary!"
                L "Those white walkers creep me out so bad!"
                R "You don't want to miss the rest of the show just because of the white walkers, do you?"
                L "Well.... No.... but can I at least sit really close to you in case I get too scared?"
                R "Of course!"
                scene bg GOT03
                with fade
                L "Thanks! I feel so much safer!"
                R "Me too!"
                R "Let's start the episode."
                scene bg SleepBlack
                with fade
                scene bg GOT04
                with fade
                L "Aaahhh!.... protect me, [ryan]!"
                R "Uuuggghhh.... That is just.... not right!"
                scene bg SleepBlack
                with fade
                scene bg GOT05
                with fade
                L "Holy shit! Her brother's dick is even bigger than yours!"
                R "Do you think?"
                L "It's pretty close."
                R "I still can't believe they can get away with this incest shit!"
                R "It's not fair that independent game developers who create incest games get crapped on by major payment processors."
                R "But those same payment processors allow for millions of people to purchase incest content that's been produced by a major TV studio."
                R "Fucking hypocrites!"
                L "What are you talking about?"
                R "It's just.... nothing.... never mind."
                R "...."
                L "I just can't believe how much they can show on TV anymore."
                scene GOTVideo01
                with fade
                $ renpy.pause ()
                R "Well, at least you're clearly enjoying it?"
                L "What do you mean?"
                R "The way you're rubbing yourself."
                scene bg GOT06
                with fade
                scene bg GOT06
                with fade
                L "Oh my God! Was I really?"
                R "Well, yeah.... You didn't notice?"
                scene bg GOT07
                with dissolve
                L "No!.... Sometimes I do it without thinking."
                R "Well.... Do you need some relief?"
                R "Do you want me to help?"
                L "How in the hell would you help with that?"
                R "We can just remove your hand and replace it with mine."
                R "It will also be more effective if your shorts are off."
                scene bg GOT06
                with dissolve
                L "Holy shit, [ryan], are you serious?"
                R "Yeah.... Why not?"
                R "You've rubbed yourself on my dick to try and take care of that itch."
                L "Yeah.... but.... that was different.... and through both of our clothes."
                R "It accomplishes the same purpose."
                R "And it doesn't seem nearly as bad as grinding, since my penis isn't involved."
                L "Well...."
                scene bg GOT08
                with dissolve
                L "When you put it that way.... it doesn't seem so bad."
                L "Oh, but what about Sidney and Mom?"
                R "What about them?"
                scene bg GOT09
                with fade
                L "Well, Sidney is right there in the kitchen, and Mom is just on the other side of that door behind us, taking a shower."
                menu:
                    "You're right!":
                        R "Yeah, she's so close.... We'd better be extremely cautious!"
                        R "Sidney is usually super focused when she's making clothing designs. Hopefully she'll never even look up."
                        R "And we'll know when Mom is done with her shower, because we'll hear the water turn off."
                        L "Hmmmm.... Well, if we're super cautious.... Ok.... If you insist."
                        "{i}{b}\"Lauren's Respect +1\"{/b}{/i}"
                        $ laurenrespect += 1
                    "That doesn't worry me!":
                        R "That shouldn't concern you!  Sidney doesn't ever look up from her computer when she's working."
                        R "Even if she did, I'm sure I could talk my way out of it."
                        R "And we'll know when Mom is done with her shower, because we'll hear the water turn off."
                        L "That sounds so risky!"
                        R "You've just got to trust me."
                        "{i}{b}\"Lauren's Submission +1\"{/b}{/i}"
                        $ laurensubmission += 1
                        L "Ok.... I trust you."
                R "Great! Just take off your shorts."
                scene bg SleepBlack
                with fade
                scene bg GOT10
                with fade
                L "Hmmmm.... This feels really awkward."
                R "Well, let's replace that feeling with another one."
                L "I hope we don't get caught!"
                scene bg GOT11
                with fade
                L "Oh, God!.... [ryan], I'm feeling so self-conscious with you staring at my pussy like that!"
                R "Lauren, you've got the cutest little pussy I've ever seen."
                scene GOTVideo02
                with fade
                $ renpy.pause ()
                L "Oh, fuck!  I can't believe you're touching my pussy!"
                R "Sssshhhh.... Don't forget that Sidney is just in the kitchen."
                L "Oh, right!...."
                scene bg GOT12
                with fade
                LT "{i}My own brother is touching my pussy!{/i}"
                LT "{i}How did we ever let it get this far?{/i}"
                play sound Lauren01 loop
                scene GOTVideo03
                with fade
                $ renpy.pause ()
                L "Oh fuck, [ryan].... that feels good!"
                R "I'm looking for your G-spot.... Did I find it?"
                L "I think you need to go deeper, but this is still feeling really good!"
                scene bg GOT13
                with fade
                LT "{i}Goddamnit! Why am I so attracted to the forbidden?{/i}"
                LT "{i}I know this is wrong! But it makes me want it even more!{/i}"
                "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
                $ laurenlibido += 1
                stop sound
                scene bg GOT14
                with dissolve
                L "Oh, shit!.... Mom's shower just turned off!"
                L "Shit!.... Where are my shorts!"
                scene bg SleepBlack
                with fade
                scene bg GOT49
                with fade
                R "Shit.... Lauren!  Try not to look so nervous!"
                L "I can't help it!.... It just feels like Mom's going to know somehow!"
                R "No way.  It was the perfect crime."
                scene bg GOT27
                with dissolve
                M "Hey, you two!"
                M "What is this you're watching?"
                R "It's that HBO show everyone used to talk about, \"Game of Thots\"."
                M "Well, it looks scary! Lauren, I'm surprised you aren't cuddled up to [ryan] for protection."
                L "What?.... No!.... Why would I do that?...."
                RT "{i}Shit!.... Lauren, relax!{/i}"
                M "Well, you certainly are brave then! You two have fun! I'm going to run and get some clothes on."
                scene bg GOT49
                with dissolve
                R "Wow!.... You're a nervous wreck!"
                R "It's a good thing Mom wasn't looking at your face."
                R "You have guilty written all over."
                L "Sorry!.... I don't have as much experience hiding my sexual deviance as you!"
                R "Don't worry! I'll help you get there."
                L "Yeah, right.... We're not doing that again!"
                RT "{i}Yeah, whatever.... we'll see....{/i}"
                $ timeofdaycounter += 1
                $ tv_events = 1
                play music Honey
                scene bg SleepBlack
                with fade
                jump lounge
            "Never mind":
                scene bg LaurenPonieTV
                $ screen_on = "laurenponietvmap"
                call screen laurenponietvmap

label lounge_hj:
    L "Yeah, I'm up for that."
    scene bg SleepBlack
    with fade
    scene bg GOT29
    with fade
    L "I've been lotioning my hands to make this feel even better for you. Can you tell?"
    R "Oh yeah, feels as soft as my old fleshlight."
    L "Oh, gross!"
    R "Haha...."
    scene GOTVideo06
    with dissolve
    $ renpy.pause ()
    R "Wow, Lauren!.... That feels fucking great!"
    LT "{i}Holy shit!.... I'm jacking off my brother again!....{/i}"
    LT "{i}How can just stroking a shaft back and forth be so fun?{/i}"
    R "Ohh.... Shit, Lauren!.... I'm about to cum!"
    L "Ohhhh, fuck yeah!...."
    LT "{i}I love having a front row seat to [ryan] cumming!{/i}"
    "{i}{b}\"Lauren's Libido +1\"{/b}{/i}"
    $ laurenlibido += 1
    play sound Ejaculate
    scene bg GOT30
    with fade
    with vpunch
    $ renpy.pause ()
    LT "{i}Wow!{/i}"
    play sound Ejaculate
    scene bg GOT31
    with fade
    $ renpy.pause ()
    LT "{i}Holy shit!.... There's even more!{/i}"
    L "I'll run and get a towel to clean up this mess."
    scene bg SleepBlack
    with fade
    scene bg GOT51
    with fade
    L "So, are we still watching the same episode we watched last time?"
    R "Yeah.... For some reason we can't ever get through an entire episode."
    L "Mmmmm.... For a good reason!"
    scene bg GOT52
    with dissolve
    M "Oohhhh.... I love seeing you so close! You two haven't been this chummy in a while."
    M "You almost look like a couple."
    M "So, just make sure you don't act like that in front of anybody we know."
    L "Ok Mom, but can you just let us watch the show?"
    M "Oh.... right.... Sorry!  I'd better go get my clothes on anyways!"
    scene bg GOT51
    with fade
    L "Oh my God!.... She has no idea!"
    R "And if she did, she'd probably cut my nuts off!"
    L "Hehehe...."
    $ timeofdaycounter += 1
    $ tv_events = 5
    play music Honey
    scene bg SleepBlack
    with fade
    jump lounge

label lounge_finger:
    L "I would love to do that again!"
    R "Alright, get those pants off and get on all fours."
    scene bg SleepBlack
    with fade
    scene bg GOT15
    with fade
    L "Ok.... I'm ready!"
    scene GOTVideo04
    with dissolve
    $ renpy.pause ()
    L "Hnnnnggghhh...."
    $ renpy.pause ()
    L "Still takes.... a minute to get used to it!"
    play sound Lauren01 loop
    $ renpy.pause ()
    L "Ohh.... That's starting to feel good again!"
    scene GOTVideo05
    with fade
    $ renpy.pause ()
    L "Oh fuck, oh fuck, oh fuck!"
    scene bg GOT17
    with fade
    stop sound
    L "Hey, why did you stop?"
    R "You know what you need to say if you want me to keep going."
    L "Fuck yeah.... I'm a dirty girl!"
    scene GOTVideo04
    with dissolve
    play sound Lauren01 loop
    $ renpy.pause ()
    L "I'm a dirty girl, I'm a dirty girl, I'm a dirty girl!...."
    L "That feels so good!"
    scene GOTVideo05
    with fade
    $ renpy.pause ()
    LT "{i}Holy shit! I can feel an orgasm coming on!{/i}"
    LT "{i}It's feeling like it's going to be a big one!{/i}"
    $ renpy.pause ()
    L "Ohhh.... Fuuuck!"
    stop sound
    play sound Ejaculate
    scene bg GOT18
    with fade
    $ renpy.pause ()
    RT "{i}Oh.... my.... God!....{/i}"
    scene bg GOT19
    with dissolve
    L "Holy shit, [ryan]! I can't even believe how much I love getting fingered like that!!"
    "{i}{b}\"Lauren's Libido -5\"{/b}{/i}"
    $ laurenlibido -= 5
    R "Haha.... I'll run and get a towel to clean up this mess!"
    scene bg SleepBlack
    with fade
    scene bg GOT51
    with fade
    L "So, are we still watching the same episode we watched last time?"
    R "Yeah.... For some reason we can't ever get through an entire episode."
    L "Mmmmm.... For a good reason!"
    scene bg GOT52
    with dissolve
    M "Oohhhh.... I love seeing you so close! You two haven't been this chummy in a while."
    M "You almost look like a couple."
    M "So, just make sure you don't act like that in front of anybody we know."
    L "Ok Mom, but can you just let us watch the show?"
    M "Oh.... right.... Sorry!  I'd better go get my clothes on anyways!"
    scene bg GOT51
    with fade
    L "Oh my God!.... She has no idea!"
    R "And if she did, she'd probably cut my nuts off!"
    L "Hehehe...."
    $ timeofdaycounter += 1
    $ tv_events = 5
    play music Honey
    scene bg SleepBlack
    with fade
    jump lounge

label lounge_bj:
    L "Yeah.... I'd love to get more practice!"
    scene bg SleepBlack
    with fade
    scene bg GOT29
    with fade
    L "This one's going to feel even better than the last one!"
    R "I can't wait!"
    play sound Blow02 loop
    scene bg GOT40
    with dissolve
    $ renpy.pause ()
    scene GOTVideo07
    with fade
    $ renpy.pause ()
    LT "{i}Wow, it's so big, I can barely get my mouth around it.{/i}"
    LT "{i}I wonder if I can get it even deeper this time.{/i}"
    $ renpy.pause ()
    stop sound
    play sound Blow03
    menu:
        "Deep":
            jump lounge_deep
        "Throat fuck":
            jump lounge_throat

label lounge_tip:
    scene GOTVideo07
    with dissolve
    $ renpy.pause ()
    menu:
        "Deep":
            jump lounge_deep
        "Throat fuck":
            jump lounge_throat
        "Cum":
            jump lounge_finish

label lounge_deep:
    scene GOTVideo08
    with dissolve
    $ renpy.pause ()
    menu:
        "Just the tip":
            jump lounge_tip
        "Throat fuck":
            jump lounge_throat
        "Cum":
            jump lounge_finish

label lounge_throat:
    scene GOTVideo09
    with dissolve
    $ renpy.pause ()
    menu:
        "Just the tip":
            jump lounge_tip
        "Deep":
            jump lounge_deep
        "Cum":
            jump lounge_finish

label lounge_finish:
    R "Oh, fuck!.... Here it comes!"
    stop sound
    scene bg GOT41
    with dissolve
    $ renpy.pause ()
    play sound Ejaculate
    scene bg GOT42
    with dissolve
    $ renpy.pause ()
    play sound Ejaculate
    $ renpy.pause ()
    scene bg GOT43
    with fade
    L "Holy fuck, I did it again!"
    R "Yeah! You are definitely getting better!"
    scene bg SleepBlack
    with fade
    scene bg GOT51
    with fade
    L "So, are we still watching the same episode we watched last time?"
    R "Yeah.... For some reason we can't ever get through an entire episode."
    L "Mmmmm.... For a good reason!"
    scene bg GOT52
    with dissolve
    M "Oohhhh.... I love seeing you so close! You two haven't been this chummy in a while."
    M "You almost look like a couple."
    M "So, just make sure you don't act like that in front of anybody we know."
    L "Ok Mom, but can you just let us watch the show?"
    M "Oh.... right.... Sorry!  I'd better go get my clothes on anyways!"
    scene bg GOT51
    with dissolve
    L "Oh my God!.... She has no idea!"
    R "And if she did, she'd probably cut my nuts off!"
    L "Hehehe...."
    $ timeofdaycounter += 1
    $ tv_events = 5
    play music Honey
    scene bg SleepBlack
    with fade
    jump lounge

label reward_for_payment:
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
                    M "Oh, my little man!"
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
                    $ momanger = 0
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
                    if first_bath_hjob == False:
                        RT "{i}Oh, no.... stay down.... stay down.... stay down!.... {/i}"
                        scene bg FrontDoor09
                        with dissolve
                        RT "{i}Shit!.... {/i}"
                        RT "{i}She's going to notice any moment.... {/i}"
                        MT "{i}Oh my God! Is that what I think it is?{/i}"
                        MT "{i}I've got to act quick, or I'm going to get dumped on my ass again!{/i}"
                        scene bg MafiaPaid01
                        with fade
                        M "Wait!.... Honey, please wait!.... Don't drop me!"
                        R "Uhhh.... but...."
                        M "I know already that you have an erection, and not the runs."
                        M "Now, please gently, let me down."
                        scene bg MafiaPaid02
                        with dissolve
                        play music Honey
                        R "God!.... This is so embarrassing!"
                        M "Embarrassing, and a bit of a problem, isn't it?"
                        M "You get one every time you hug me, don't you?"
                        R "Ummmm.... Mostly, yes...."
                        M "Well, let me see how bad it is."
                        scene bg MafiaPaid03
                        with dissolve
                        R "Holy shit, Mom!.... You're grabbing my cock!"
                        M "SShhhh.... I don't want your sisters to hear!"
                        M "Just as I thought.... Hard as a rock!"
                        R "Mom!...."
                        M "Ok.... Here's what I need you to do."
                        M "Go into the bathroom, and wait for me."
                        M "I'm going to send your sisters on an errand so they're out of the house, and then I'll come find you in the bathroom."
                        R "But, what is...."
                        M "Don't argue, just do what I say."
                        R "Yes, Mom!"
                        scene bg SleepBlack
                        with fade
                        "{i}\"A few minutes later.\"{/i}"
                        scene bg MafiaPaid04
                        with fade
                        M "I'm going to lock the doors, just in case the girls come back for something."
                        R "Mom, what is going on?"
                        M "Patience, dear."
                        M "I'll explain in just a second."
                        scene bg MafiaPaid05
                        with fade
                        M "So, it looks like your erection hasn't gone down at all?"
                        R "How could it when you've left me in such uncertain anticipation?"
                        M "Yeah.... Sorry to be so vague."
                        M "I didn't dare say anything until your sisters were out of the house."
                        M "I was worried they might overhear something I'm about to talk to you about."
                        R "What is this about?"
                        scene bg MafiaPaid06
                        with dissolve
                        M "So, you know how we've been studying an Oedipus Rex centered curriculum in my literature class?"
                        R "Yeah...."
                        M "And how we've talked about Sigmund Freud and his Oedipal complex?"
                        R "Wait!.... Do you think?...."
                        scene bg MafiaPaid07
                        with dissolve
                        M "Please, don't interrupt me."
                        R "Sorry."
                        M "As part of the curriculum, one of the books that we have to read as teachers, is by a member of our school board Will Tylor."
                        R "Ohhh.... Is he that creepy school board member that sometimes visits, and walks around the halls trying to peek up girls skirts when they bend over?"
                        M "Yes, the very same."
                        M "Anyways, he wrote a book about Oedipal complexes, that at first I thought was total bullshit, but I'm starting to think he may be onto something, as it seems to be playing out between you and me."
                        R "Playing out?"
                        scene bg MafiaPaid06
                        with dissolve
                        M "You know.... Following me to a strip club and watching me dance.... Your overwhelming desire to provide for me.... The way you get erections whenever I hug you...."
                        M "Your interests in a certain genre of H-games, and what happened between us in my office as a consequence...."
                        if firstclubvisit:
                            M "....Then there's the incident at the pool...."
                            R "You were the one who...."
                            M "I'm not talking about that, I'm talking about when you grabbed my breasts to \"try and protect me\"."
                            R "Oh...."
                        else:
                            pass
                        M "Anyways.... I'm sure you won't argue that there's been an increase in these types of incidents since your father went to prison."
                        R "Yeah, I guess I can't argue with that."
                        scene bg MafiaPaid05
                        with dissolve
                        M "So, the big question is.... What do we do about it?"
                        R "I guess.... I can try to be less perverted?"
                        M "No, I mean what can we \"realistically\" do about this?"
                        R "...."
                        scene bg MafiaPaid06
                        with dissolve
                        M "So, Will Tylor theorizes that a young man can get stuck in an Oedipal phase if he's not allowed to let it run it's course."
                        M "Kind of like how children can get stuck in oral phases when you take their pacifier away, or make them stop sucking their thumbs before they are ready."
                        M "When you do that to a child, it makes them constantly want to stick things in their mouths."
                        M "So, if Will Tylor is right, if we don't let this phase run it's course, you might never get rid of these propensities."
                        R "So, what does that mean?"
                        M "I don't know.... Will Tylor doesn't elaborate, so I guess it's up to our own interpretation."
                        scene bg MafiaPaid07
                        with dissolve
                        M "I want to try killing two birds with one stone."
                        R "So, you have a plan?"
                        M "Only if you agree to it."
                        R "I'm all ears."
                        scene bg MafiaPaid05
                        with dissolve
                        M "I'm really grateful for the way you've been keeping me from having to work at the strip club, so, I really want to reward you for your selfless efforts on my behalf."
                        M "And I think I can safely give you the kind of reward that might, at the same time, help us transition you out of your Oedipal phase."
                        R "I'm still listening."
                        scene bg MafiaPaid06
                        with dissolve
                        M "What if I were to.... Oh, how do I put this delicately?.... Give you a handjob?"
                        R "...."
                        R "Are you testing me?"
                        R "Is this some sort of trap where you'll kick me out of the house if I give you the wrong answer?"
                        M "No!.... nothing like that."
                        scene bg MafiaPaid07
                        with dissolve
                        M "I'm completely serious, and I'm willing to do this for you if you can be mature about it."
                        R "Uhhhh...."
                        R "I'm shocked.... This reminds me of one of those ga...."
                        M "Don't you dare say it's like one of your H-games!"
                        M "In those games the MC gets to have sex.... That's not going to happen between us!"
                        R "Oh, gross!.... You're my mom.... I could never think about doing that with you."
                        RT "{i}Except for hundreds of times a day.{/i}"
                        M "Well, you better not have your hopes set on anything like that, because that won't happen in a million years."
                        M "And this isn't going to be erotic, this is homemade therapy because we can't afford the real kind."
                        R "Wow, Mom.... You're making this experience incredibly hot for me.... Do you teach classes on how to set the mood?"
                        M "Don't be a smartass!"
                        M "So, if you want me to do this, get your shorts off, and jump up on the vanity."
                        scene bg SleepBlack
                        with fade
                        scene bg MafiaPaid08
                        with fade
                        play music SexMusic
                        R "Like this?"
                        M "Ummm.... Yeah...."
                        MT "{i}Holy God!.... I almost forgot how big my little man is!{/i}"
                        scene bg MafiaPaid09
                        with fade
                        MT "{i}I need to see if Will Tylor has written a book about how to treat a Jocasta complex....{/i}"
                        MT "{i}....Because I am having some strong feelings about his cock right now!{/i}"
                        M "Uuummm.... So, are you ready?...."
                        R "Uuuhhh.... This is weird.... and feels kind of wrong.... but I think you're right.... we should see if this works."
                        RT "{i}Oh.... my.... God!.... I am soooo ready!!{/i}"
                        M "Ok.... Here goes nothing."
                        scene MafiaPaidVideo01
                        with dissolve
                        $ renpy.pause ()
                        MT "{i}Oh my God!.... I'm jacking off my son!{/i}"
                        MT "{i}I never would have ever thought, in a million years, that this would even be a possibility.{/i}"
                        $ renpy.pause ()
                        RT "{i}Oh.... God!.... Mom is actually choking my chicken!{/i}"
                        RT "{i}Although I want to fuck her so bad, I don't think I ever really believed I would ever get this far!{/i}"
                        RT "{i}Maybe my goal of fucking her isn't as unrealistic as I've imagined.{/i}"
                        RT "{i}I want to cum so bad!.... But I've got to enjoy this moment.... Make it last as long as possible!{/i}"
                        RT "{i}Come on [ryan]!  This is what you've been training for everyday since you started puberty!{/i}"
                        menu:
                            "Cum":
                                jump bath_hj_cum
                            "Hold the line!":
                                $ renpy.pause ()
                                scene bg MafiaPaid13
                                with fade
                                M "Is something wrong [ryan]?  I thought for sure you would have ejaculated by now!"
                                "{i}\"Mom's affection -1\"{/i}"
                                $ momaffection -= 1
                                RT "{i}Hmmmm.... Let's see if I can make this a little more enjoyable.{/i}"
                                R "I think it's just about the way we're going about this.... It's just not very sexy."
                                M "Well, I don't want it to be very sexy.... I just want you to ejaculate so we can see if this is going to help you."
                                R "Yeah.... That's what I mean.... How am I supposed to cum, when this feels more like a check-up at the doctor's office?"
                                M "[ryan], I hope you've never had a visit to the doctor's office like this."
                                R "No, I just mean, that this is cold, impersonal.... boring."
                                scene bg MafiaPaid14
                                with dissolve
                                M "Well, you're still hard."
                                R "That's how I am half of the day."
                                M "Hmmmm.... Well, what do you suggest?"
                                R "I don't know, make it sexy!"
                                R "Act like you are enjoying it."
                                R "Talk dirty to me."
                                scene bg MafiaPaid13
                                with dissolve
                                M "Ohhh.... I don't know if that's a good idea."
                                M "I'm just going to keep going the way I am if it's all the same to you."
                                R "Alright, but this could take a while!"
                                scene MafiaPaidVideo01
                                with fade
                                $ renpy.pause ()
                                MT "{i}Oh my God!.... He really wants me to talk dirty to him?{/i}"
                                MT "{i}I could talk so dirty his ears would fall off.{/i}"
                                MT "{i}But that seems like it could have some really bad consequences.{/i}"
                                $ renpy.pause ()
                                MT "{i}Shit.... This is taking too long.... The girls will be home soon, and I'll still be in here, jacking off their brother.{/i}"
                                $ renpy.pause ()
                                menu:
                                    "Cum":
                                        jump bath_hj_cum
                                    "Hold strong.... Hold strong.... Hold strong....":
                                        $ renpy.pause ()
                                        scene bg MafiaPaid13
                                        with fade
                                        M "Are you close yet?"
                                        R "Not yet!"
                                        "{i}\"Mom's Affection -1\"{/i}"
                                        $ momaffection -= 1
                                        M "Shit!.... Your sisters are going to be home soon!"
                                        R "I'm trying!.... It just feels more like pressure to perform, than fun."
                                        scene bg MafiaPaid14
                                        with dissolve
                                        M "Uuuuuuhhhhh.... Fine!...."
                                        scene MafiaPaidVideo01
                                        with fade
                                        $ renpy.pause ()
                                        M "Oh, fuck!.... I love this huge, meaty cock!"
                                        RT "{i}Oh my God!....{/i}"
                                        M "I want to take it down my throat and fill my stomach with your cum!"
                                        RT "{i}Oh, fuck!....{/i}"
                                        M "I need that cum soooo bad!"
                                        M "Please! I need my big strong boy to shoot his load all over my face!"
                                        "{i}\"Mom's Affection +5\"{/i}"
                                        "{i}\"Mom's Libido +5\"{/i}"
                                        $ momaffection += 5
                                        $ momlibido += 5
                                        R "Oh, fuck Mom! That did it!"
                                        R "Here I cuuummm!"
                                        jump bath_hj_cum
                    else:
                        RT "{i}Ohhh.... I'm so glad I don't have to worry about my boner scaring Mom anymore!{/i}"
                        scene bg FrontDoor09
                        with dissolve
                        RT "{i}Oh, yeah!.... {/i}"
                        RT "{i}She's going to notice any moment.... {/i}"
                        MT "{i}Oh my God!.... There it is again.{/i}"
                        MT "{i}Looks like I've got some work to do!{/i}"
                        scene bg MafiaPaid03
                        with dissolve
                        M "Oh, my poor boy!.... Why don't you run to the bathroom, and I'll go get rid of your sisters."
                        scene bg SleepBlack
                        with fade
                        "{i}\"A few minutes later.\"{/i}"
                        scene bg MafiaPaid04
                        with fade
                        M "The door is locked this time.... Just in case."
                        scene bg MafiaPaid05
                        with fade
                        M "So, did you masturbate this week like I asked you?"
                        R "Yeah, I did a few times."
                        M "Good boy! Way to go above and beyond."
                        scene bg MafiaPaid06
                        with dissolve
                        M "So, do you need another handy this week?"
                        menu:
                            "Yes":
                                M "Good. Hopefully it will get us closer to taking care of your extra cum production, and your Oedipal phase at the same time."
                                R "You are one efficient mom!"
                                M "It comes with being a school teacher."
                                M "Alright, get your shorts off and jump up on the vanity."
                                scene bg SleepBlack
                                with fade
                                scene bg MafiaPaid08
                                with fade
                                play music SexMusic
                                R "Like this?"
                                M "Perfect, once again...."
                                MT "{i}Holy God!.... My little man is so big!{/i}"
                                scene bg MafiaPaid09
                                with fade
                                MT "{i}I still need to find some literature about how to treat a Jocasta complex....{/i}"
                                MT "{i}....Because I am still having strong feelings about his cock right now!{/i}"
                                M "Uuummm.... So, are you ready?...."
                                R "Yeah.... I'll try to be faster this time."
                                M "Ok.... Here goes nothing."
                                scene MafiaPaidVideo01
                                with dissolve
                                $ renpy.pause ()
                                MT "{i}Oh my God!.... I'm jacking off my son again!{/i}"
                                MT "{i}The novelty just isn't going away!{/i}"
                                $ renpy.pause ()
                                R "Oh.... God!.... Mom, you have the softest hands!"
                                scene bg MafiaPaid13
                                with fade
                                M "Alright, [ryan]! This time, we don't have time to mess around!  I'm going to jump straight to the dirty talk."
                                scene MafiaPaidVideo01
                                with fade
                                $ renpy.pause ()
                                M "Oh, damn!.... I just can't get enough of that cock!"
                                RT "{i}Oh my God!....{/i}"
                                M "I want to take it down my throat and fill my stomach with your cum!"
                                RT "{i}Oh, fuck!....{/i}"
                                M "I need that cum soooo bad!"
                                MT "{i}I can't believe I'm talking to [ryan] like this!{/i}"
                                "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                                $ momlibido += 1
                                M "Please! I need my big strong boy to shoot his load all over my face!"
                                R "Oh fuck, Mom! That did it!"
                                R "Here I cuuummm!"
                                jump bath_hj_cum
                            "No":
                                scene bg MafiaPaid07
                                with dissolve
                                M "Alright, suit yourself."
                                M "But I'm glad you don't feel like you need me to do that for you this week!"
                                M "That's definitely progress!"
                                scene bg SleepBlack
                                with fade
                                $ timeofdaycounter += 1
                                play music Honey
                                jump bath
                "No (lie)" if money >= 1000:
                    $ liedaboutmoney = True
                    $ loyaltycounter = 0
                    jump momdissapointed
                "No" if money <= 999:
                    $ loyaltycounter = 0
                    jump momdissapointed

label bath_hj_cum:
    scene bg MafiaPaid10
    with fade
    play sound Ejaculate
    if first_bath_hjob:
        M "Fuck, [ryan]! That's still too much cum!"
    else:
        M "Fuck, [ryan]! That's a lot of cum!"
    scene bg MafiaPaid11
    with dissolve
    play sound Ejaculate
    M "God! There's more?"
    scene bg MafiaPaid12
    with fade
    M "[ryan], that was way more cum than you should have!"
    M "I'm worried you're not masturbating enough."
    R "But I masturbate almost every...."
    M "You should probably be masturbating at least twice a week."
    RT "{i}I was going to say almost every hour, but oh well.{/i}"
    scene bg MafiaPaid06
    with fade
    M "If you keep paying the Mafia debt, I'll take care of it once a week, and you can take care of yourself sometime in the middle of the week."
    M "Does that sound like something you can do?"
    R "Don't worry, Mom! I'm all over it."
    scene bg MafiaPaid05
    with dissolve
    M "That's a good boy!  Now clean this up before your sisters get home, and I'm going to go get ready for bed."
    R "Thanks, Mom!"
    scene bg MafiaPaid07
    with dissolve
    M "Don't mention it!"
    M "And I mean ever!"
    scene bg SleepBlack
    with fade
    $ first_bath_hjob = True
    $ timeofdaycounter += 1
    play music Honey
    jump bath

############# Kitchen ################################# Kitchen ######################################################## Kitchen ###################################################### Kitchen ########################################################### Kitchen ####################################################################### Kitchen ########################

label fix_sink:
    if fixed_sink == 2:
        scene bg HoneyDoList02
        with fade
        RT "{i}Mom's at it again.  Doing her best to keep our house functioning like a normal home should.{/i}"
        RT "{i}I've still got plenty on my plate too, but should I take some time to see if she needs help?{/i}"
        menu:
            "Help Mom.":
                R "Hey, Mom!  Way to rock that broom."
                scene bg HoneyDoList05
                with fade
                M "What is it, [ryan]?  I still don't have time for your playful banter."
                R "Sorry....  I know.... I should stop trying."
                R "I was just wondering if you needed any help with the house."
                M "You still want to help me around the house?...."
                scene bg HoneyDoList11
                with dissolve
                R "Well, yeah.... Dad's still gone, and your \"honey-do list\" must still be getting longer."
                M "Well yeah, that's true, but unfortunately we didn't even check off the last thing we had on the list."
                R "What do you mean?"
                M "The sink started leaking again."
                R "Really?.... Again?.... Well, let's go fix it."
                scene bg HoneyDoList08
                with dissolve
                M "Again?.... I don't want to end up cold and wet again."
                M "Let's just get a plumber."
                R "We're not spending money on a plumber.  They'll charge us $200 just to drive out here."
                M "Alright.... Fine!"
                scene bg SleepBlack
                with fade
                scene bg HoneyDoList36
                with fade
                play music SexMusic
                R "Alright, so we'll just do the same thing we did last time?"
                M "Wait!...."
                M "Hmmmm.... I'm just trying to decide which part of this job is the least likely to get me wet."
                R "Ok.... I'll let you choose whichever one you want to."
                M "Hmmmmmm.... I'll take...."
                $ sink_option = renpy.random.randint (1, 2)
                if sink_option == 1:
                    M "I'll climb under the sink this time."
                    scene bg HoneyDoList37
                    with dissolve
                    R "Ok.... Just let me know when you've got the coupling secured."
                    M "Ok.... I've got the wrench securing the same thing as last time. I hope it's the coupling."
                    R "Alright, well I'll just see if I can tighten it here from above.  You ready to hold it steady?"
                    M "I'm ready."
                    M "Oh.... and don't forget to turn it right this time."
                    RT "{i}And miss the chance to see you in a wet T-shirt?.... No way!{/i}"
                    R "Yeah, I remember. Here goes nothing."
                    play sound WaterLeak loop
                    scene bg HoneyDoList38
                    with dissolve
                    M "Oh, fuck!.... [ryan]!.... It's leaking all over me!.... I told you to turn it right!"
                    R "I did turn it right.... Shit!.... I think the threads must not have been aligned right, and so it just slipped out."
                    M "Well, hurry and put it back in!....  I'm soaking wet!"
                    scene bg HoneyDoList39
                    with dissolve
                    M "[ryan]!.... Hurry!.... Tighten the damn thing!"
                    stop sound
                    scene bg HoneyDoList40
                    with dissolve
                    M "Holy shit!.... You got me again, you asshole!...."
                    R "Mom?!.... You know I didn't mean to!"
                    M "Are you sure?.... because it's starting to look suspicious!"
                    R "What?.... No.... of course not!"
                    M "Uuhhggghhh.... It's ok.... I'm ok.... I'm ok.... It's just a little water."
                    scene bg HoneyDoList41
                    with fade
                    R "I can't believe that happened again....  I'm really sorry.... You've got to believe me."
                    M "It's alright....  I'm over the shock of it now.... I'm sorry for accusing you of doing it on purpose."
                    R "That's ok.... I can see why you would think that."
                    RT "{i}It's a pretty accurate observation.{/i}"
                    R "Oh.... and just so you know...."
                    scene bg HoneyDoList42
                    with dissolve
                    M "I know.... It's just part of the weekly kitchen wet T-shirt contest."
                    M "In which I'm always the only participant."
                    M "So, what's my score?"
                    R "Oh.... It's a definite 10!"
                    "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                    $ momlibido += 1
                    M "...."
                    M "Alright.... That's enough playful banter.  I'm going to get another shirt on."
                    M "Thanks again for all your help around the house."
                    R "Of course! Love ya, Mom."
                    M "I love you too."
                    play music Honey
                    $ timeofdaycounter += 1
                    jump kitchen
                else:
                    M "I'll climb up on the counter this time."
                    M "Just be careful not to break the faucet again!"
                    R "I'll try my best."
                    scene bg HoneyDoList44
                    with dissolve
                    R "Ok.... I've got the coupling braced from below.  Go ahead and turn it clockwise, and we'll see if that stops the leak."
                    M "Ok.... That's as tight as I can get it."
                    R "Perfect, now I'll just try to get a little bit of an extra turn from down here...."
                    RT "{i}Ok, how did I do that last time.{/i}"
                    RT "{i}If I bend this at the right angle, it should separate the faucet from the water line again.{/i}"
                    R "and...."
                    play sound WaterLeak loop
                    scene bg HoneyDoList45
                    with dissolve
                    M "Aaaaahhhh.... [ryan]!.... You did it again!"
                    R "What do you mean?...."
                    M "I've got water spraying me again!"
                    scene bg HoneyDoList46
                    with dissolve
                    R "Oh, shit!.... I must have bumped the faucet connection again!"
                    R "Damn thing is so fragile!"
                    M "Goddamnit, [ryan]!...."
                    M "Get your ass up here and fix it!"
                    scene bg HoneyDoList47
                    with dissolve
                    M "UUuuurrrgggghhhhh...."
                    R "I'm sorry.... There.... I've almost got it...."
                    R "...."
                    stop sound
                    scene bg HoneyDoList48
                    with fade
                    R "And.... fixed!"
                    M "[ryan]!...."
                    R "What?"
                    M "[ryan]?...."
                    R "What?"
                    M "[ryan]!?...."
                    R "WHAAT??...."
                    M "Are you fucking kidding me?"
                    R "Mom?.... language!"
                    M "I can't even believe you got me again!"
                    M "Remind me to change into a scuba suit the next time we try to fix the sink!"
                    R "Haha.... That's a good one."
                    M "Did you do that on purpose?"
                    R "What?.... of course not!...."
                    M "Well, this is getting ri-Goddamned-fucking-diculous."
                    M "If it starts leaking again, I'm calling a plumber."
                    R "What?.... You can't!.... We can't afford one right now."
                    R "Plus, I'm pretty sure we got it this time."
                    R "Oh, but ummm.... Just so you know...."
                    scene bg HoneyDoList50
                    with dissolve
                    M "I know.... It's just part of the weekly kitchen wet T-shirt contest."
                    M "In which I'm always the only participant."
                    M "So, what's my score?"
                    R "Oh.... It's a definite 10!"
                    "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                    $ momlibido += 1
                    M "...."
                    M "Alright.... That's enough playful banter.  I'm going to get another shirt on."
                    M "Thanks again for all your help around the house."
                    R "Of course! Love ya, Mom."
                    M "I love you too."
                    play music Honey
                    $ timeofdaycounter += 1
                    jump kitchen
            "Don't help Mom.":
                scene bg HoneyDoList02
                $ screen_on = "momcleanloungemap02"
                call screen momcleanloungemap02
    if fixed_sink == 1:
        scene bg HoneyDoList02
        with fade
        RT "{i}Mom's at it again.  Doing her best to keep our house functioning like a normal home should.{/i}"
        RT "{i}I've still got plenty on my plate too, but should I take some time to see if she needs help?{/i}"
        menu:
            "Help Mom.":
                R "Hey, Mom!  Way to rock that broom."
                scene bg HoneyDoList05
                with fade
                M "What is it, [ryan]?  I still don't have time for your playful banter."
                R "Sorry....  I know.... I should stop trying."
                R "I was just wondering if you needed any help with the house."
                M "You still want to help me around the house?...."
                scene bg HoneyDoList11
                with dissolve
                R "Well, yeah.... Dad's still gone, and your \"honey-do list\" must still be getting longer."
                M "Well yeah, that's true, but unfortunately we didn't even check off the last thing we had on the list."
                R "What do you mean?"
                M "The sink started leaking again."
                R "Oh nice!  I know how to fix it now.... I think I just need to torque the coupling just a little bit tighter."
                scene bg HoneyDoList08
                with dissolve
                M "Are you sure?.... I don't want to end up cold and wet again."
                M "Maybe I should just call a plumber."
                if ntrcontent:
                    "{i}I wonder if I could request a sexy one.{/i}"
                else:
                    pass
                R "Don't be silly.  I've got it this time."
                M "All right. We'll give it another shot."
                scene bg SleepBlack
                with fade
                scene bg HoneyDoList36
                with fade
                play music SexMusic
                R "Alright, so we'll just do the same thing we did last time, and...."
                M "Wait!...."
                M "I don't want to end up soaking wet this time.  Let's trade places.  I'm sure I can tighten the thingy just as tight as you."
                R "But.... It needs to be torqued really hard.  I think probably a man should do it."
                M "Oh shut up, [ryan].  I work out more than you do.  I'm sure I can get it tighter than you could."
                R "Alright.... No need to be hurtful."
                R "I'll just crawl under the sink, and you climb up onto the counter then."
                scene bg HoneyDoList44
                with dissolve
                R "Ok.... I've got the coupling braced from below.  Go ahead and turn it clockwise, and we'll see if that stops the leak."
                M "Ok.... That's as tight as I can get it."
                R "Perfect, Now I'll just try to get a little bit of an extra turn from down here...."
                R "and...."
                scene bg HoneyDoList77
                with fade
                LT "{i}I wonder where Mom is.... I need some help on my Oedipus assignment.{/i}"
                play sound WaterLeak loop
                scene bg HoneyDoList45
                with dissolve
                M "Aaaaahhhh.... [ryan]!.... What did you do?"
                R "What do you mean?...."
                M "I've got water spraying me up here!"
                scene bg HoneyDoList46
                with dissolve
                R "Oh, shit!.... I must have knocked the faucet off the main water line with my wrench!"
                M "Goddamnit [ryan]!...."
                M "Get your ass up here and fix it!"
                scene bg HoneyDoList78
                with fade
                M "[ryan]!.... What's wrong?...."
                R "I think I pinched the nipple too hard with the clamp!"
                R "Fuck!.... It just popped out!"
                M "Well, stick it back in!"
                M "God!.... You're making me so wet!"
                scene bg HoneyDoList79
                with fade
                "{i}{b}\"Lauren's Libido +5\"{/b}{/i}"
                $ laurenlibido += 5
                scene bg HoneyDoList47
                with dissolve
                M "UUuuurrrgggghhhhh.... I can't even believe you got me again!"
                R "It's not like I did this on purpose!"
                M "Well, you could have fooled me!"
                R "I'm sorry.... There.... I've almost got it...."
                R "...."
                stop sound
                scene bg HoneyDoList48
                with fade
                R "And it's fixed!...."
                M "[ryan]! You son of a bitch!"
                R "Haha.... That's insulting both of us!"
                R "And since when did you decide to start cussing like a sailor?"
                M "Just, shut up!"
                R "Ok.... ummmm.... but you've got a situation again."
                if momlibido >= 8:
                    M "Let me guess.... I'm winning the wet T-shirt contest again?"
                    R "You know it!"
                    scene bg HoneyDoList50
                    with dissolve
                    M "You really think so?.... I mean, most of the girls at the club are so much younger."
                    R "I'm telling you Mom, those torpedoes would blow all those younger girls out of the water."
                    R "And the fact that they're natural, and still so perky after nursing three babies!"
                    R "I mean.... who wouldn't want to motorboat a pair of those \"tig ol bitties\"..."
                    scene bg HoneyDoList49
                    with dissolve
                    M "Ok.... that's enough. A son shouldn't use such colorful commentary about his own mothers breasts."
                    R "Sorry.... "
                    M "No.... it's ok.... it was my fault for fishing for compliments."
                    "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    $ momlibido += 1
                    $ momaffection += 1
                    M "And I appreciate your kind words, I just need to stop you before it gets too weird."
                    R "Yeah.... I was getting carried away."
                    M "So, I think we'll call it a day, and I'm going to go change my shirt.  Thank you for your help today."
                    R "Of course! Love ya, Mom."
                    M "I love you too."
                    play music Honey
                    $ timeofdaycounter += 1
                    $ fixed_sink = 2
                    jump kitchen
                else:
                    scene bg HoneyDoList49
                    with dissolve
                    M "Oh, shit!.... You can see through my shirt again, can't you?"
                    R "Yep.... "
                    R "Not that I'm complaining."
                    M "Goddamnit [ryan]! Stop talking to your mother like that!"
                    R "Sorry.... I wasn't...."
                    M ".... No.... no need to make up excuses."
                    M "I'm grateful for your help today.  Let's hope we got the problem fixed this time."
                    M "Thank you for always being so willing to help."
                    R "Of course! Love ya, Mom."
                    M "I love you too."
                    "{i}\"This event ends slightly different with higher libido. Get Mom's libido up, (8+) and try again next week.\"{/i}"
                    play music Honey
                    $ timeofdaycounter += 1
                    $ fixed_sink = 2
                    jump kitchen
            "Don't help Mom.":
                scene bg HoneyDoList02
                $ screen_on = "momcleanloungemap02"
                call screen momcleanloungemap02
    else:
        scene bg HoneyDoList02
        with fade
        RT "{i}Shorter shorts.... Nice open tank top.... No bra!.... {/i}"
        RT "{i}Dad wouldn't have ever let Mom wear anything like that around the house.{/i}"
        RT "{i}He's such an asshole!.... I'm so glad to see Mom opening up more, and being herself.{/i}"
        RT "{i}She always had to walk on eggshells around him.{/i}"
        RT "{i}Life's definitely harder without him here to take care of us, but honestly, I'm glad he's gone.{/i}"
        RT "{i}Now I just need to keep working on getting Mom to feel the same way.{/i}"
        RT "{i}Maybe there's something else I can help her do around the house.{/i}"
        menu:
            "Help Mom.":
                R "Hey, Mom!  I'm digging the new diggs!"
                scene bg HoneyDoList05
                with fade
                M "Oh, hi [ryan].... Did you stop me from working just so you can talk about fashion?"
                R "Uhhh.... No.... Actually, I wanted to offer my handyman services to you again."
                R "Is there anything we can do to check off another item on the \"honey-do list?\""
                R "Did that lightbulb come unscrewed again?"
                M "No, thank God.  It's not flickering at all anymore."
                M "But I just noticed we are having some problems with the kitchen sink.  It seems to be leaking from somewhere underneath into the cabinet area."
                M "I've put a pan there to catch the water for now, but we really need to get it fixed."
                M "I was just going to call a plumber."
                scene bg HoneyDoList11
                with dissolve
                R "No!.... Don't do that.  I'm sure I can fix it for you."
                RT "{i}Plus I've seen too many movies about lonely housewives calling a plumber.{/i}"
                M ".... Umm.... Ok.... If you think you can."
                R "Well, yeah, of course I can.  Plus, we need to be saving money right now.  Plumbers are expensive."
                scene bg HoneyDoList08
                with dissolve
                M "Yeah, I'd thought of that.  I figured I'd need to work another night at the club to be able to pay for it."
                R "No Mom, don't do that.... I've got this."
                if ntrcontent:
                    MT "{i}Damn.... I've been getting a little bored.  Working another night in the club sounded exciting.{/i}"
                    MT "{i}Plus, I've seen some pretty good movies about plumbers and lonely housewives.{/i}"
                    MT "{i}But this seems important to [ryan], to feel like the man of the house, so I'll just let him do it.{/i}"
                else:
                    MT "{i}I love it when [ryan] tries so hard to protect me.{/i}"
                    MT "{i}He really is growing up to be a hard working little man.{/i}"
                M "Ok, Let's see if you can fix it."
                R "Awesome!  I'll meet you in the kitchen in about 10 minutes.  I'm just going to see if there's a good YourTube tutorial for fixing leaks."
                scene bg SleepBlack
                with fade
                "{i}\"One YourTube tutorial, and 10 minutes later.\"{/i}"
                scene bg HoneyDoList34
                with fade
                M "So, do you think you can fix it?"
                R "Yeah, I think I can figure it out."
                R "Do you mind helping though?  I'm going to need an extra hand."
                scene bg HoneyDoList32
                with dissolve
                M "No, I don't mind at all.  I'm just really happy that you're getting to be so handy."
                M "Just let me know what you want me to do."
                scene bg BlurryWhite
                with fade
                scene bg HoneyDoList36
                with fade
                R "Ok, so I need you to take this wrench and keep the coupling at the base of the drain pipe from turning while I try to tighten it from above."
                R "I'll fill the sink with water too, so we can see if it stops the leak."
                M "Alright, anything else?"
                R "No.... except this would probably work better with a pipe wrench, but this is all I could find in Dad's toolbox."
                R "So, if you'll crawl under the sink and try to secure the wrench on the coupling, I'll climb up on the counter and do my part from above."
                play music SexMusic
                scene bg HoneyDoList37
                with dissolve
                R "Ok.... Just let me know when you've got the coupling secured."
                M "Well.... I've got the wrench securing something, I'm not exactly sure if it's the coupling."
                R "Alright, well I'll just see if I can tighten it from up here.  You ready to hold it steady?"
                M "I'm ready."
                RT "Now do I turn it left, or right?"
                RT "I think left. Here goes nothing."
                play sound WaterLeak loop
                scene bg HoneyDoList38
                with dissolve
                M "Oh, fuck!.... [ryan]!.... It's leaking all over me!.... Turn it the other way!"
                M "Hurry!....  I'm getting soaked!"
                scene bg HoneyDoList39
                with dissolve
                M "[ryan]!.... Hurry!.... Tighten the damn thing!"
                stop sound
                scene bg HoneyDoList40
                with dissolve
                M "Holy shit!"
                M "Couldn't you have at least filled the sink with warm water!?"
                R "Oh, no! Mom, I'm so sorry!"
                M "Uuhhggghhh.... It's ok.... I'm ok.... That was just a little shocking!"
                scene bg HoneyDoList41
                with fade
                R "Are you sure?.... For someone who hates curse words, you sure cursed a lot."
                M "[ryan].... Give me a break, ok?.... You just dumped freezing water all over my chest!"
                M "And sometimes I just need you to do what I say, and not what I do...."
                R "Yeah.... Alright.... but on the bright side, I think you could win the wet T-shirt contest at the strip club."
                if momlibido >= 8:
                    scene bg HoneyDoList42
                    with dissolve
                    M "Haha.... Yeah, I was noticing that too."
                    M "But I think much younger tits than mine would win that contest."
                    R "What?!.... No way!.... Your tits are just as good as any 20 year old out there."
                    M "Well, I appreciate that [ryan], that means.... Wait.... No, I don't.... A son shouldn't compliment his mom's tits like that."
                    R "Sorry.... but I'm only telling you the truth."
                    "{i}{b}\"Mom's Affection +1\"{/b}{/i}"
                    $ momaffection += 1
                    M "Well, be that as it may, I think it's time to call it a day.  Thanks for your help today!"
                    R "Of course! Love ya, Mom."
                    M "I love you too."
                    play music Honey
                    $ timeofdaycounter += 1
                    $ fixed_sink = 1
                    jump kitchen
                else:
                    scene bg HoneyDoList43
                    with dissolve
                    M "Oh my God!.... My shirt is completely see-through!"
                    M "I can't believe you were just staring at them without saying a word."
                    R "I did say a word!.... "
                    M "Yeah, after getting a good long look."
                    M "And then suggesting I should be in a wet T-shirt contest?"
                    M "Those aren't the kinds of jokes a son should make to his mother."
                    R "Sorry Mom,.... I was just trying to make things less awkward."
                    M "...."
                    M "That's ok, I guess I am overreacting a little."
                    M "Thanks for your help today.  I'm going to run and change my shirt."
                    R "Of course! Love ya, Mom."
                    M "I love you too."
                    "{i}\"This event ends slightly different with higher libido. Get Mom's libido up, (8+) and try again next weekend.\"{/i}"
                    play music Honey
                    $ timeofdaycounter += 1
                    $ fixed_sink = 1
                    jump kitchen
            "Don't help Mom.":
                scene bg HoneyDoList02
                $ screen_on = "momcleanloungemap02"
                call screen momcleanloungemap02

label please_go_work:
    scene bg SidneyKitchen01
    with fade
    R "Hey Sidney!"
    S "Give me just one more second and...."
    if talked_about_hp:
        scene bg NSidneyKitchen03
    else:
        scene bg SidneyKitchen03
    with dissolve
    S "What can I do for you?"
    R "You know how you said that if I need help making the Mafia payment fo the week, you'd help out?"
    S "Sure I do.... Do you need me to go work at the club tonight?"
    R "Actually yeah.... That would be really helpful!"
    S "You got it!"
    S "And if you get bored tonight, you should come see me."
    R "That's pretty tempting."
    R "We'll just see."
    R "And Sidney, thanks for being so willing to help."
    S "Yeah of course! We've all got to work extra hard to keep the family together."
    R "Alright, I'm outta here.  Maybe I'll see you at the club tonight."
    if talked_about_hp:
        scene bg NSidneyKitchen07
    else:
        scene bg SidneyKitchen07
    with dissolve
    ST "{i}I sure hope everything goes ok tonight.  After [ryan]'s warnings about working for the Mafia, I do feel a little nervous.{/i}"
    ST "{i}I would sure feel better if he comes and sees me.{/i}"
    $ sidneys_working = True
    $ sidney_money += 200
    scene bg SidneyInKitchen
    with fade
    $ screen_on = "sidneykitchenmap"
    call screen sidneykitchenmap

label breakfast_events:
    if progress >= 6 and first_bfast == False:
        scene bg Kitchen01
        with fade
        RT "{i}It smells good in here. Should I join everybody for breakfast?{/i}"
        menu:
            "Yes":
                scene bg Breakfast02
                with fade
                $ renpy.pause ()
                scene bg Breakfast04
                with fade
                R "Thanks for breakfast Mom, it's really good!"
                S "Yeah Mom, although I wish I were still at college, this is a nice perk of being home."
                scene bg Breakfast07
                with dissolve
                M "Well, we do need to talk about some things while everyone is here."
                scene bg Breakfast09
                with dissolve
                M "First, welcome home, Sidney. I know this situation stinks, and you'd rather be at college with your friends, but we sure are glad to have you home!"
                M "Second, we've only got the one bathroom. So, we need to talk about a shower schedule."
                M "Lauren, you'll be early morning, Sidney can be late morning after we've left for school, and I'll take evenings after I've come home from school."
                scene bg Breakfast07
                with dissolve
                M "[ryan], you can shower at any other time that's available.  Come to think of it, why don't I ever see you shower?"
                M "And then the other thing is that I just want to encourage you all to come to breakfast as often as you can."
                M "With how busy we all are, it's just nice to have a time when we can all be together, and talk about things that are going on in our lives."
                scene bg Breakfast09
                with dissolve
                M "That's all I've got to say, so everybody eat up."
                M "Oh, [ryan] and Lauren, try to eat fast. We don't want to be late for school!"
                scene bg SleepBlack
                with fade
                $ first_bfast = True
                $ timeofdaycounter += 1
                jump kitchen
            "No":
                $ screen_on = "kitchenmap"
                call screen kitchenmap
    if found_bathrobe and not brobe_bfast:
        jump update_six_bfasts
    if sidneyfingerlaurenprogress <= 3 and sidneyfingerlaurenprogress >= 2 and finger_bfast == False and first_bfast:
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
                if brobe_bfast:
                    scene bg BFast05
                    with fade
                else:
                    scene bg Breakfast05
                    with fade
                L "Well, don't you think we should at least address it?"
                M "Now is not the time, or the place!"
                L "Well, when is a good time?"
                M "{i}(whispering){/i} Anytime that your brother isn't around!"
                scene bg Breakfast21
                with fade
                R "Wait! What's going on?"
                M "Nothing, honey.... Just eat your pancakes!"
                RT "{i}Damn, Sidney looks miserable.... Am I going too far with my night shenanigans?{/i}"
                RT "{i}I've just got to remember, the ends justify the means.{/i}"
                scene bg SleepBlack
                with fade
                $ finger_bfast = True
                $ timeofdaycounter += 1
                jump kitchen
            "No":
                $ screen_on = "kitchenmap"
                call screen kitchenmap
    if photoshoot_1 and convention_bfast == False and first_bfast:
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
                if brobe_bfast:
                    scene bg BFast05
                    with fade
                else:
                    scene bg Breakfast05
                    with fade
                M "Oh, Lauren.... I forgot to ask you how your costume convention went."
                L "It's cosplay Mom, and it was fun."
                M "I'm glad to hear it.  I wanted to ask you the next morning, but you were nowhere to be found."
                if brobe_bfast:
                    scene bg BFast03
                    with dissolve
                else:
                    scene bg Breakfast03
                    with dissolve
                L "Yeah, Mandy and I talked [ryan] into going to Dad's warehouse to take some pictures of us in our costumes."
                if brobe_bfast:
                    scene bg BFast07
                    with dissolve
                else:
                    scene bg Breakfast07
                    with dissolve
                M "Oh, good! I love pictures. [ryan], would you please email me those pictures!"
                R "Uhhhh...."
                if brobe_bfast:
                    scene bg BFast04
                    with dissolve
                else:
                    scene bg Breakfast04
                    with dissolve
                L "Yeah [ryan], Mom will be so impressed with your photography skills."
                R "Ummm.... Ok.... I'll try to remember to send them over."
                RT "{i}Oh, shoot!.... looks like the memory card in the camera is going to have to get damaged before I get a chance to download them onto my computer, and post them online.{/i}"
                RT "{i}As long as Mom isn't a closet cosplay fan, with a secret Cosplay Heaven account, I think we'll be alright.{/i}"
                scene bg SleepBlack
                with fade
                $ convention_bfast = True
                $ timeofdaycounter += 1
                jump kitchen
            "No":
                $ screen_on = "kitchenmap"
                call screen kitchenmap
    if first_htbyd_shoot == False and htbyd_bfast == False and first_bfast:
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
                if brobe_bfast:
                    scene bg BFast05
                    with fade
                else:
                    scene bg Breakfast05
                    with fade
                M "So, why exactly did you miss my class yesterday?"
                L "Oh.... I was helping [ryan]."
                M "Helping him what?"
                L "With his new business.  He's making money off his photography skills, so I was just helping him set up his studio, and modeling for a few pictures."
                if brobe_bfast:
                    scene bg BFast08
                    with dissolve
                else:
                    scene bg Breakfast08
                    with dissolve
                M "Really? How are you affording a studio?"
                R "I'm just using some empty space at Dad's warehouse."
                M "And you think you'll actually make a fair amount of money through photography?"
                R "That's the goal."
                if brobe_bfast:
                    scene bg BFast07
                    with dissolve
                else:
                    scene bg Breakfast07
                    with dissolve
                M "Well, that's very creative and ambitious of you!"
                M "But, won't the FBI make us forfeit any money you make?"
                R "Well, I'm trying to keep it secret."
                R "Hopefully if they discover it, I just get some kind of tax penalty."
                if diazfirstvisit:
                    RT "{i}Luckily Diaz said she'd help me hide my income from the FBI. That alone might be worth the $500 I'm paying her each week.{/i}"
                else:
                    pass
                M "Hmmmm.... Normally I would be very against trying to hide income from the government, but in our case.... We really don't have a choice."
                M "But I am very proud of you! That's very entrepreneurial of you!"
                "{i}\"Mom's Respect +1\"{/i}"
                $ momrespect += 1
                R "Entre pre what now?"
                M "Just means you make a good little businessman."
                R "Why did you have to throw in the \"little\" part?"
                M "Sorry, but to me you'll always be my little boy."
                RT "{i}Shit!.... She can't think of me as her little boy if I'm going to have any chance with her.  She's got to start seeing me as a man!{/i}"
                M "Don't forget to send me some of Lauren's pics, as you forgot to, last time."
                R "Ok, Mom. I'll try to remember this time."
                RT "{i}I wonder if I'd be in more trouble for the pictures, or if Sidney would be in more trouble for the costumes.{/i}"
                if brobe_bfast:
                    scene bg BFast05
                    with fade
                else:
                    scene bg Breakfast05
                    with fade
                M "And Lauren, I don't mind if you miss school once in a while to help [ryan], so long as you keep up with your homework."
                M "I can cover for you just as easily as I do for [ryan]."
                M "But, that's just until we get our money and Mafia problems sorted out."
                L "Ok, Mom."
                scene bg SleepBlack
                with fade
                $ htbyd_bfast = True
                $ timeofdaycounter += 1
                jump kitchen
            "No":
                $ screen_on = "kitchenmap"
                call screen kitchenmap
    if firstclubvisit and pool_bfast == False and first_bfast:
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
                if brobe_bfast:
                    scene bg BFast04
                    with fade
                else:
                    scene bg Breakfast04
                    with fade
                L "So, guess who my friend Kenzie saw at the pool the other day."
                R "Shamu?"
                if brobe_bfast:
                    scene bg BFast03
                    with dissolve
                else:
                    scene bg Breakfast03
                    with dissolve
                L "Why didn't I get to go?"
                if brobe_bfast:
                    scene bg BFast05
                    with fade
                else:
                    scene bg Breakfast05
                    with fade
                M "Because I wanted to do something nice for just [ryan]."
                M "He's made enough money that I haven't had to go work for the DeCapos for quite a few weeks in a row."
                if brobe_bfast:
                    scene bg BFast04
                    with dissolve
                else:
                    scene bg Breakfast04
                    with dissolve
                L "I wish I'd been there. Kenzie said there was some kind of incident with Mom when you all were playing Marco Polo."
                L "But she wouldn't tell me any details."
                LT "{i}She told me all the details, but I'd like to see Mom squirm a little.{/i}"
                if brobe_bfast:
                    scene bg BFast22
                    with dissolve
                else:
                    scene bg Breakfast22
                    with dissolve
                MT "{i}Oh, shit!.... Does the whole school know?{/i}"
                scene bg SleepBlack
                with fade
                $ pool_bfast = True
                $ timeofdaycounter += 1
                jump kitchen
            "No":
                $ screen_on = "kitchenmap"
                call screen kitchenmap
    if first_wr_shoot == False and wr_bfast == False and first_bfast:
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
                if brobe_bfast:
                    scene bg BFast09
                    with fade
                else:
                    scene bg Breakfast09
                    with fade
                M "So, I was thinking Sidney, that since you're home all the time now, maybe there's some way you can contribute to the family."
                S "What are you talking about?  I do contribute to the family?"
                M "Really? And how is that?"
                scene bg Breakfast10
                with fade
                R "She's helping me...."
                R "Yeah, my secret business wouldn't be making any money without her help."
                M "Oh, really?  That's good to hear. What is it you do to help [ryan]?"
                scene bg Breakfast12
                with dissolve
                S "I make costumes for his photoshoots and I've even started doing a little modeling in my own costumes for him."
                M "Oh, wow!.... Both of my daughters are amateur models?"
                M "I'm so proud of all of you."
                M "[ryan]! How many times do I have to remind you to send me some of their pictures! I'm dying to see their portfolios."
                scene bg Breakfast10
                with dissolve
                R "I'll try to remember, Mom."
                M "I wanted to be a model too, back when I was young like you girls."
                R "Well, it's not too late, Mom."
                R "I happen to know a guy with a photo studio."
                R "Well, kind of a photo studio."
                M "Oh, no! Nobody would want to see pictures of an old woman like me."
                R "Tell that to J-Flo, and Jennifer Yanniston, or even Elizabeth Furly."
                R "I'm serious Mom! You are every bit as hot as any of them."
                R "I'm sure I could get some really great pictures of you too."
                M "Hmmmm.... well, we'll see."
                RT "{i}I've got to get her in front of my camera!{/i}"
                scene bg SleepBlack
                with fade
                $ wr_bfast = True
                $ timeofdaycounter += 1
                jump kitchen
            "No":
                $ screen_on = "kitchenmap"
                call screen kitchenmap
    if forcedntrevents == 1 and ntrclub_bfast == False and wr_bfast and htbyd_bfast and first_bfast:
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
                if brobe_bfast:
                    scene bg BFast08
                    with fade
                else:
                    scene bg Breakfast08
                    with fade
                M "So [ryan], I'm guessing your business isn't going very well?"
                R "No.... It's going ok.... Why would you think it's not doing very well?"
                M "Well, you haven't been able to make the weekly payments to the DeCapos, so I've been having to cover the debt at the club each week."
                R "Oh, yeah.... sorry about that, Mom.... I've just been having to re-invest my money into the studio."
                if brobe_bfast:
                    scene bg BFast05
                    with fade
                else:
                    scene bg Breakfast05
                    with fade
                L "Yeah, you should see it, he's got professional lighting, and a green screen backdrop."
                L "It's starting to look like a quasi-legitimate studio."
                scene bg Breakfast12
                with fade
                S "Is serving drinks at the club once a week really that bad?"
                M "Ummm.... well it's not so much how hard the work is, it's just not a great environment."
                R "And there's the fact that you're working for the fucking Mafia!"
                M "No foul language at the table, please."
                R "Sorry Mom, and I'll try harder to make those payments each week."
                M "Please do!"
                "{i}\"Mom's Respect -1\"{/i}"
                $ momrespect -= 1
                $ ntrclub_bfast = True
                scene bg SleepBlack
                with fade
                $ timeofdaycounter += 1
                jump kitchen
            "No":
                $ screen_on = "kitchenmap"
                call screen kitchenmap
    if first_time_chores and camille_bfast == False and first_bfast:
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
                if brobe_bfast:
                    scene bg BFast04
                    with fade
                else:
                    scene bg Breakfast04
                    with fade
                R "Great breakfast again this morning, Mom!"
                if brobe_bfast:
                    scene bg BFast08
                    with dissolve
                else:
                    scene bg Breakfast08
                    with dissolve
                M "Thanks, [ryan].... And before you all finish your food and take off, I need to talk to you about something very important."
                S "What is it?"
                if brobe_bfast:
                    scene bg BFast09
                    with dissolve
                else:
                    scene bg Breakfast09
                    with dissolve
                M "Well, it appears that your Uncle Bobby has run away with their nanny, and left Aunt Camille and Mandy to take care of themselves."
                L "Oh no, that's awful!  Poor Mandy!"
                if brobe_bfast:
                    scene bg BFast08
                    with dissolve
                else:
                    scene bg Breakfast08
                    with dissolve
                M "He pretty much left them penniless, and that's why you may see her cleaning our house for some extra money.  At least, until she can find another job."
                M "There's also a possibility that they might have to move in with us."
                if brobe_bfast:
                    scene bg BFast05
                    with fade
                else:
                    scene bg Breakfast05
                    with fade
                L "What!?.... There's barely enough room for us!.... Especially with only one bathroom!"
                M "Well, we're all going to have to make even more sacrifices.... We may have to start combining shower times."
                M "Mandy will have to sleep with you, Lauren, and Camille can sleep in my bed."
                L "Is this a for sure thing?.... When would it happen?"
                scene bg Breakfast10
                with fade
                R "Their utilities are all paid up until the end of the month, and then there's still some time before the power and water companies will actually cut them off."
                M "So, they'll probably move in with us before that happens."
                M "So, I just wanted you all to be aware of that, and start preparing yourselves now."
                RT "{i}Two more women in the house.... This could get interesting.{/i}"
                $ camille_bfast = True
                scene bg SleepBlack
                with fade
                $ timeofdaycounter += 1
                jump kitchen
            "No":
                $ screen_on = "kitchenmap"
                call screen kitchenmap
    if progress >= 15 and not move_in_bfast:
        jump update_six_bfasts
    if sixty_nined_bfast == 2 and first_bfast:
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
                with fade
                R "Thanks, Mom! Breakfast is delicious as usual!"
                M "That's very sweet, honey!"
                if brobe_bfast:
                    scene bg BFast07
                    with fade
                else:
                    scene bg Breakfast07
                    with fade
                M "Does anybody have anything exciting happening today?"
                L "No"
                S "No"
                scene bg Breakfast10
                with fade
                R "Not really...."
                M "What's the matter, Sidney?"
                M "You haven't even touched your breakfast."
                S "I'm just not feeling that hungry."
                M "Are you feeling ok?"
                R "She's fine!.... I saw her gulping down a midnight snack last night."
                scene bg Breakfast21
                with dissolve
                M "Oh.... You know it's not good for you to eat that late at night."
                scene bg Breakfast24
                with dissolve
                S "Well, it was just a little snack, wasn't it [ryan]?"
                R "Oh, I don't know.... I'd say it was pretty big."
                M "Sidney.... Try not to eat so late at night.... It will give you bad dreams."
                ST "{i}I don't know.... My dreams were pretty hot.{/i}"
                scene bg Breakfast23
                with dissolve
                S "Ok Mom, I guess I just get a little extra hungry at night because of all the running I've been doing in the mornings."
                if park_full_menu:
                    S "Not to mention, all the exercises [ryan] and I do at the park together."
                    RT "{i}Haha.... She couldn't help but throw that one in.{/i}"
                else:
                    pass
                if brobe_bfast:
                    scene bg BFast09
                    with fade
                else:
                    scene bg Breakfast09
                    with fade
                M "Oh.... Ok, that makes sense."
                menu:
                    "Tease Mom":
                        play music SexMusic
                        R "Would you mind pouring more maple syrup on my pancakes?"
                        M "I can pass it to you, and you can pour it yourself."
                        R "But I always pour too much, and it ruins my pancakes."
                        R "You always do it just right."
                        M "Ok.... I guess I can do that."
                        if brobe_bfast:
                            scene bg BFast16
                            with dissolve
                        else:
                            scene bg Breakfast16
                            with dissolve
                        M "There.... How's that?"
                        if brobe_bfast:
                            scene bg BFast17
                            with fade
                        else:
                            scene bg Breakfast17
                            with fade
                        R "They're perfect.... I mean the syrup's perfect!"
                        if brobe_bfast:
                            scene bg BFast18
                            with fade
                        else:
                            scene bg Breakfast18
                            with fade
                        MT "{i}You bold cheeky bastard!.... I know what that was about.{/i}"
                        MT "{i}So, why did you do it for him?{/i}"
                        if brobe_bfast:
                            scene bg BFast19
                            with dissolve
                        else:
                            scene bg Breakfast19
                            with dissolve
                        MT "{i}Shit!.... I need to get laid, so I'm not always so horny around my family!{/i}"
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
                        RT "{i}Look at that sexy red-head. just blabbering on about her social life.{/i}"
                        RT "{i}I wonder what she'd do if I teased her a little. Hopefully she won't kill me now that we've messed around a little.{/i}"
                        if brobe_bfast:
                            scene bg BFast14
                            with fade
                        else:
                            scene bg Breakfast14
                            with fade
                        L "And so I said to Kenzie...."
                        if brobe_bfast:
                            scene bg BFast15
                            with dissolve
                        else:
                            scene bg Breakfast15
                            with dissolve
                        L "...."
                        S "What?.... What did you say to Kenzie?"
                        L "Never mind.... It was a stupid story."
                        if brobe_bfast:
                            scene bg BFast06
                            with fade
                        else:
                            scene bg Breakfast06
                            with fade
                        LT "{i}I can't believe [ryan] is doing this in front of everybody!{/i}"
                        LT "{i}Ohhh.... but his toes do feel good!{/i}"
                        M "You ok, Lauren?  You're being unusually quiet."
                        L "Uhhh.... Yeah.... I'm great!...."
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
                        RT "{i}I need to lively things up a little or I'm going to fall asleep.{/i}"
                        scene bg Breakfast25
                        with fade
                        S "So, I had to start over from scratch, and when I finally got the new outfit put together according to his specifications...."
                        S "....do you know what he said to me?...."
                        scene bg Breakfast26
                        with dissolve
                        S "...."
                        M "What?...."
                        S "Huhhh?...."
                        M "What did your professor say?"
                        S "Oh.... Uhh.... \"Nice outfit.\""
                        M "Huh...."
                        M "No offense Sidney, but that story was a bit anticlimactic."
                        S "Uhhh.... yeah.... sorry."
                        scene bg Breakfast13
                        with fade
                        ST "{i}Ohhhh.... I should kill that little shit!....{/i}"
                        ST "{i}Mmmm.... But it does feel really good.{/i}"
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
    if lectureprogress >= 3 and first_bfast:
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
                with fade
                R "Thanks, Mom! Breakfast is delicious as usual!"
                M "That's very sweet, honey!"
                if brobe_bfast:
                    scene bg BFast07
                    with fade
                else:
                    scene bg Breakfast07
                    with fade
                M "Does anybody have anything exciting happening today?"
                L "No"
                S "No"
                scene bg Breakfast10
                with fade
                R "I've got more work to do on my Oedipus project from your class."
                R "I might need to stop by your office today to get some help."
                MT "{i}Oh, God!.... That probably means more of those H-games....{/i}"
                MT "{i}Why do I look forward to him showing me more of those games?{/i}"
                if brobe_bfast:
                    scene bg BFast07
                    with fade
                else:
                    scene bg Breakfast07
                    with fade
                M "Ok, honey.... If you need to, just cum by at the usual time."
                MT "{i}Did I just say cum?.... Wait, that doesn't make any sense.{/i}"
                MT "{i}Why do I have so many of these thoughts.... Do I need to make a run to the prison for a conjugal visit?{/i}"
                MT "{i}Yyiiickk.... That sounds so dirty.{/i}"
                menu:
                    "Tease Mom":
                        play music SexMusic
                        R "Would you mind pouring more maple syrup on my pancakes?"
                        M "I can pass it to you, and you can pour it yourself."
                        R "But I always pour too much, and it ruins my pancakes."
                        R "You always do it just right."
                        M "Ok.... I guess I can do that."
                        if brobe_bfast:
                            scene bg BFast16
                            with dissolve
                        else:
                            scene bg Breakfast16
                            with dissolve
                        M "There.... How's that?"
                        if brobe_bfast:
                            scene bg BFast17
                            with fade
                        else:
                            scene bg Breakfast17
                            with fade
                        R "They're perfect.... I mean the syrup's perfect!"
                        if brobe_bfast:
                            scene bg BFast18
                            with fade
                        else:
                            scene bg Breakfast18
                            with fade
                        MT "{i}You bold cheeky bastard!.... I know what that was about.{/i}"
                        MT "{i}So, why did you do it for him?{/i}"
                        if brobe_bfast:
                            scene bg BFast19
                            with dissolve
                        else:
                            scene bg Breakfast19
                            with dissolve
                        MT "{i}Shit!.... I need to get laid, so I'm not always so horny around my family!{/i}"
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
                        RT "{i}Look at that sexy red-head. just blabbering on about her social life.{/i}"
                        RT "{i}I wonder what she'd do if I teased her a little. Hopefully she won't kill me now that we've messed around a little.{/i}"
                        if brobe_bfast:
                            scene bg BFast14
                            with fade
                        else:
                            scene bg Breakfast14
                            with fade
                        L "And so I said to Kenzie...."
                        if brobe_bfast:
                            scene bg BFast15
                            with dissolve
                        else:
                            scene bg Breakfast15
                            with dissolve
                        L "...."
                        S "What?.... What did you say to Kenzie?"
                        L "Never mind.... It was a stupid story."
                        if brobe_bfast:
                            scene bg BFast06
                            with fade
                        else:
                            scene bg Breakfast06
                            with fade
                        LT "{i}I can't believe [ryan] is doing this in front of everybody!{/i}"
                        LT "{i}Ohhh.... but his toes do feel good!{/i}"
                        M "You ok, Lauren?  You're being unusually quiet."
                        L "Uhhh.... Yeah.... I'm great!...."
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
                        S "So, I had to start over from scratch, and when I finally got the new outfit put together according to his specifications...."
                        S "....do you know what he said to me?...."
                        scene bg Breakfast26
                        with dissolve
                        S "...."
                        M "What?...."
                        S "Huhhh?...."
                        M "What did your professor say?"
                        S "Oh.... Uhh.... \"Nice outfit.\""
                        M "Huh...."
                        M "No offense Sidney, but that story was a bit anticlimactic."
                        S "Uhhh.... yeah.... sorry."
                        scene bg Breakfast13
                        with fade
                        ST "{i}Ohhhh.... I should kill that little shit!....{/i}"
                        ST "{i}Mmmm.... But it does feel really good.{/i}"
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
    if progress <= 5:
        scene bg Kitchen01
        with fade
        RT "{i}It smells good in here. Should I join everybody for breakfast?{/i}"
        menu:
            "Yes":
                scene bg Breakfast01
                with fade
                "{i}\"You enjoy an uneventful breakfast with Mom and Lauren.\"{/i}"
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
                "{i}\"You enjoy an uneventful breakfast with your family.\"{/i}"
                $ timeofdaycounter += 1
                jump kitchen
            "No":
                $ screen_on = "kitchenmap"
                call screen kitchenmap

#############  Laundry Room  #############################  Laundry Room  ########################################################  Laundry Room  #############################################  Laundry Room  #########################################################  Laundry Room  ##############################################################  Laundry Room  ####################

label fix_washer:
    if fixed_washer >= 1:
        scene bg HoneyDoList03
        with fade
        RT "{i}Mom's at it again.  Doing her best to keep our house functioning like a normal home should.{/i}"
        RT "{i}I've still got plenty on my plate too, but should I take some time to see if she needs help?{/i}"
        menu:
            "Help Mom.":
                R "Hey, Mom!  Way to rock that broom."
                scene bg HoneyDoList06
                with fade
                $ persistent.gal_mom_7 = True
                M "What is it, [ryan]?  I still don't have time for your playful banter."
                R "Sorry....  I know.... I should stop trying."
                R "I was just wondering if you needed any help with the house."
                M "You still want to help me around the house?...."
                scene bg HoneyDoList12
                with dissolve
                R "Well, yeah.... Dad's still gone, and your \"honey-do list\" must still be getting longer."
                M "Well yeah, that's true, but unfortunately we didn't even check off the last thing we had on the list."
                if fixed_washer == 2:
                    R "Oh no!.... Is the washing machine quitting mid-load again?"
                    M "It worked for a bit, then it started doing the same thing as before."
                    R "Well, the YourTube video said it's not uncommon to have to repeat the repair several times before it's completely fixed."
                    M "Oh.... and on top of that, the laundry detergent seems to be leaking."
                    RT "{i}Laundry detergent, but there wasn't even any in the machi.... Ohhhh.... I wonder if she found my cum puddle.... I meant to come back and clean that up.{/i}"
                    R "Ok.... I'll take a look at that too."
                    scene bg HoneyDoList09
                    with dissolve
                    M "I just wish there was a less awkward way to fix that stupid machine!"
                    M "Having you grind your erect penis on my ass is pretty awkward."
                    MT "{i}Plus it kind of turns me on for some fucked-up reason.{/i}"
                else:
                    R "That's because you stopped us before we could finish it"
                    scene bg HoneyDoList09
                    with dissolve
                    M "I only stopped it because you were grinding your erect penis on my ass."
                R "Well, my penis was only \"erect\" because you made the situation feel sexual."
                M "I only said what we both were thinking."
                R "Speak for yourself, I was just trying to fix the washing machine!"
                scene bg HoneyDoList06
                with dissolve
                M "Ok.... Let's go try to finish the job we started.  But we both have to be more mature about it."
                M "And I want you to try not to get an erection."
                M "Got it?"
                R "Deal!"
                scene bg SleepBlack
                with fade
                scene bg HoneyDoList51
                with fade
                RT "{i}Uugghh.... Back to the creepy basement!{/i}"
                RT "{i}But I'd still follow that ass anywhere.{/i}"
                scene bg HoneyDoList52
                with fade
                RT "{i}Oh that's beautiful!{/i}"
                scene bg HoneyDoList51
                with fade
                $ renpy.pause ()
                scene bg HoneyDoList53
                with fade
                if fixed_washer == 2:
                    M "So, the washing machine did a few loads without stopping mid-load, but then it did the same thing as before."
                    M "Do you think doing the same thing will take care of it this time?"
                    R "Yeah I think so.... but I can't guarantee that we won't need to do it one or two times after that."
                else:
                    M "So, are you sure what we were doing last time is the only way to fix this stupid machine?"
                    R "I'm afraid so."
                    M "Damnit,  I wish we had the money to just buy another, or at least be able to afford a repair man."
                    R "Yeah.... Maybe I'll be able to afford a new one soon."
                    M "I'd rather you use the money to pay down the Mafia debt."
                    R "You got it."
                    R "Let's get this machine running again!"
                R "Unfortunately, just like last time, I'm going to need your help."
                M "I know.... Just remember to try and keep control of your penis."
                R "I'll try.... "
                scene bg HoneyDoList54
                with dissolve
                R "Take this wrench again, and just do the same thing you did last time."
                scene bg HoneyDoList55
                with fade
                M "Ok, I've got the nut secured."
                RT "{i}You're going to secure a nut from me!{/i}"
                scene bg HoneyDoList56
                with dissolve
                R "Once again.... I've just got to remove this panel so I can get into where the belt is."
                MT "{i}Ok [mom_name], don't mention anything sexual!{/i}"
                R "Sorry.... but yeah.... The YourTube video said that's the only way to fix this model of washing machine."
                scene bg HoneyDoList57
                with fade
                MT "{i}Ok,.... Seems like he's doing ok so far.... {/i}"
                M "How's it coming?"
                R "OK.... I'm just trying to get my hands on the belt clear in the back."
                M "Ok.... I'm still holding back that nut."
                RT "{i}Haha.... I'll be the one trying to hold back a nut.{/i}"
                RT "{i}Once again, Mom's pretty much stuck in there.... I don't think she could turn around if she wanted to.{/i}"
                RT "{i}So, it's time to take advantage of the situation.{/i}"
                scene bg HoneyDoList58
                with dissolve
                play music SexMusic
                MT "{i}Hmmmm.... So far so good, it seems.{/i}"
                scene bg HoneyDoList59
                with fade
                R "Don't worry Mom.  My penis is as soft as can be."
                MT "{i}Is it just me? or is there something resting on my ass?.... {/i}"
                scene bg HoneyDoList60
                with dissolve
                R "Ummmm....  Shit...."
                M "Shit!.... [ryan]?.... What did we agree on?"
                scene bg HoneyDoList61
                with dissolve
                R "I didn't mean to!"
                R "It's because I started to think about last time!"
                scene bg HoneyDoList60
                with dissolve
                R "I'm sorry...."
                scene bg HoneyDoList61
                with dissolve
                M "Ghrrrrr.... You have got to be kidding me, [ryan]!"
                R "Well, it also doesn't help that I have to move around so much to crank this belt."
                scene bg HoneyDoList60
                with dissolve
                R "And I have to keep cranking this belt until it loosens up the motor bearings enough that they can turn easily on their own."
                R "So unfortunately, there's not a lot I can do at this point."
                scene bg HoneyDoList61
                with dissolve
                M "Well, I can't take this.... I'm going to come out while you're doing that!"
                R "Wait!.... No!.... You can't!...."
                M "Why?"
                R "Because if you let go of the wrench, the bearings will turn with the belt, and it won't fix the problem."
                if momlibido >= 8:
                    M "Fine.... Just try to hurry."
                    if fixed_washer == 2:
                        RT "{i}Haha.... I've already fixed it again.... but I want to get the same 5 star user experience as last time.{/i}"
                    else:
                        RT "{i}It's all fixed actually.... but I don't want this to end just yet.{/i}"
                    R "Ok Mom, I've just got to turn this belt several more times."
                    scene bg HoneyDoList62
                    with fade
                    if fixed_washer == 2:
                        RT "{i}Oh.... My.... God.... I'm hot dogging my mom's ass again!{/i}"
                    else:
                        RT "{i}Oh.... My.... God.... I'm hot dogging my own mom's ass!{/i}"
                    scene LaundryVideo01
                    with fade
                    M "Seriously [ryan]!.... You've got to be almost done!"
                    scene bg HoneyDoList62
                    with fade
                    R "Yep!.... So close!...."
                    scene LaundryVideo01
                    with fade
                    RT "{i}Oh, shit.... I'm so close!{/i}"
                    scene bg HoneyDoList64
                    with dissolve
                    $ renpy.pause ()
                    RT "{i}Hnnnngggghhhh..........{/i}"
                    scene bg BlurryWhite
                    with vpunch
                    with hpunch
                    play sound Ejaculate
                    scene bg HoneyDoList65
                    with fade
                    $ renpy.pause ()
                    play sound Ejaculate
                    scene bg HoneyDoList66
                    with dissolve
                    with vpunch
                    with hpunch
                    $ renpy.pause ()
                    MT "{i}Oh good!  I don't feel [ryan] pressing against my ass anymore.{/i}"
                    MT "{i}He must finally be done.{/i}"
                    M "I don't care if you're done or not.... My knees are killing me, and I've got to get out of here."
                    scene bg HoneyDoList76
                    with dissolve
                    R "Aaahhh...Wait just a second!"
                    M "Nuh uh.... I'm coming out now!"
                    scene bg HoneyDoList67
                    with dissolve
                    RT "{i}Shit, shit, shit!....{/i}"
                    RT "{i}I've got to get my pants back up!{/i}"
                    scene bg HoneyDoList69
                    with dissolve
                    RT "{i}Pheww.... That was close.{/i}"
                    M "[ryan]?.... How is it that you have no self control?"
                    R "I'm sorry Mom, I'm pretty sure it's just hormones."
                    M "Well, I tried my best not say anything sexual."
                    R "I know.... But I couldn't stop thinking about last time...."
                    M "Well, shit.... I seem to be making a big pile of memories, that I wish I could ask you to forget."
                    RT "{i}And I wouldn't trade those memories for the world.{/i}"
                    R "I'm sorry!.... I really did just want to fix the washing machine again."
                    M "Would it help if I wore a burka?"
                    R "Haha.... No.... You would make even a burka look sexy."
                    M "Ok.... Let's keep the awkward compliments to a minimum."
                    R "I'm sorry.... I'm not trying to make things awkward...."
                    M "Well, I blame the manufacturer of this washer for making things awkward."
                    M "I still think we should put out a hit on whoever designed that goddamn machine."
                    R "Haha.... Yeah.... Well.... I should run along then."
                    M "Sure [ryan].... Thanks for your help!"
                    R "Of course! Love ya, Mom."
                    M "I love you too."
                    scene bg SleepBlack
                    with fade
                    scene bg HoneyDoList71
                    with fade
                    MT "{i}That horny little bull-shitter!{/i}"
                    MT "{i}What am I going to do with him?{/i}"
                    MT "{i}.... \"You would make even a burka look sexy.\".... What a smooth little charmer.{/i}"
                    "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                    $ momlibido += 1
                    scene bg HoneyDoList72
                    with dissolve
                    MT "{i}Huh?.... What's this?{/i}"
                    scene bg HoneyDoList73
                    with fade
                    if fixed_washer == 2:
                        MT "{i}Oh, shit!.... I completely forgot.{/i}"
                    else:
                        MT "{i}Is that?.... Oh, shit....{/i}"
                    scene bg HoneyDoList74
                    with dissolve
                    MT "...."
                    if fixed_washer == 2:
                        MT "{i}I need to remind him to fix the leak in the washing machine.{/i}"
                    else:
                        MT "{i}I've got to remember to tell [ryan], that the washing machine is leaking laundry detergent.{/i}"
                    $ fixed_washer = 2
                    play music Honey
                    $ timeofdaycounter += 1
                    jump myroom
                else:
                    M "I don't care!.... You're literally grinding against my ass again!"
                    scene bg HoneyDoList68
                    with dissolve
                    RT "{i}I've got to get my pants back up! {/i}"
                    scene bg HoneyDoList70
                    with dissolve
                    RT "{i}Pheww.... That was close.{/i}"
                    M "[ryan]?.... How is it that you have no self control?"
                    R "I'm sorry Mom, I'm pretty sure it's just hormones."
                    M "Well, I tried my best not say anything sexual."
                    R "I know.... But I couldn't stop thinking about last time...."
                    M "Well, shit.... I seem to be making a big pile of memories, that I wish I could ask you to forget."
                    RT "{i}And I wouldn't trade those memories for the world.{/i}"
                    R "I'm sorry!.... I really did just wanted to fix a washing machine again."
                    M "Would it help if I wore a burka?"
                    R "Haha.... No.... You would make even a burka look sexy."
                    M "Ok.... Let's keep the awkward compliments to a minimum."
                    R "I'm sorry.... I'm not trying to make things awkward...."
                    M "Well, I blame the manufacturer of this washer for making things awkward."
                    M "I still think we should put out a hit on whoever designed that goddamn machine."
                    R "Haha.... Yeah.... Well.... I should run along then."
                    M "Sure [ryan].... Thanks for your help!"
                    R "Of course! Love ya, Mom."
                    M "I love you too."
                    "{i}\"The ending to this event is different if Mom's libido is higher (+8).\"{/i}"
                    "{i}\"Raise her libido and try again next weekend.\"{/i}"
                    play music Honey
                    $ timeofdaycounter += 1
                    jump myroom
            "Don't help Mom.":
                $ screen_on = "momcleanloungemap03"
                call screen momcleanloungemap03
    else:
        scene bg HoneyDoList03
        with fade
        RT "{i}Wow!  Where did she get those shorts!?.... Sexy pink crop top.... I like the direction this is going!.... {/i}"
        RT "{i}It's a good thing Dad's in prison.... He would have an aneurysm if he saw Mom dressed like this.{/i}"
        RT "{i}He's such an asshole!.... I'm so glad to see Mom opening up more, and being herself.{/i}"
        RT "{i}I've got to make her see how much better her life can be without him.{/i}"
        RT "{i}Time to show her I can take his place in her life.{/i}"
        RT "{i}Maybe there's something else I can do to help her around the house.{/i}"
        menu:
            "Help Mom.":
                R "Hey, Mom.  Lookin good today.  Love the new outfit!"
                scene bg HoneyDoList06
                with fade
                $ persistent.gal_mom_7 = True
                M "Oh hi, [ryan].... Thank you, but I only put it on because I was feeling hot."
                R "I'll say, and you're looking hot too."
                scene bg HoneyDoList09
                with dissolve
                M "I think you know that I meant temperature...."
                R "Haha.... Yeah of course, but I didn't mean it that way."
                scene bg HoneyDoList12
                M "[ryan]!.... You're not supposed to talk to your mother that way!"
                R "What?... I can't tell my mother that she looks good?"
                R "I was just trying to give you a compliment."
                M "Well.... Yeah....  Saying I look good is fine.  But saying I look hot, or sexy, that kind of stuff is creepy...."
                M "You know.... coming from my own son."
                R "Sorry.... I won't say that anymore."
                M "Thank you!"
                R "I'll just think it instead."
                scene bg HoneyDoList06
                with dissolve
                M "No.... That's not.... Never mind!...."
                M "Did you need something?  I'm kind of busy."
                R "Yeah.... I just thought I'd see if you need me to tackle another item on the \"honey-do list.\""
                M "hmmmm.... Well, the sink stopped leaking."
                R "Thank God!"
                M "You're telling me!"
                M "So, I can't really think of anything off the top of my head.... unless you think you could fix a washing machine.... Ours keeps quitting mid-load."
                R "I could try."
                M "No.... I was just kidding.... We'll need an actual repair man to fix that."
                scene bg HoneyDoList12
                with dissolve
                R "Mom.... An actual repair man costs a lot of money."
                R "Do you want to have to strip in the club this week?"
                if ntrcontent:
                    MT "{i}I have been feeling rather bored lately.... Stripping for horny men sounds kind of exciting.{/i}"
                else:
                    MT "{i}Uggghhh.... All those horny men just staring at my ass.... I don't want to go back there!{/i}"
                M "No.... of course not."
                R "Then just finish sweeping the floor, I'll run and watch some YourTube videos about how to fix washing machines, and I'll be right back."
                scene bg SleepBlack
                with fade
                "{i}\"A few YourTube videos later.\"{/i}"
                scene bg SleepBlack
                with fade
                scene bg HoneyDoList03
                with fade
                "Ok Mom I think I'm ready.  Why don't you show me what the problem is."
                scene bg HoneyDoList06
                with fade
                M "You're sure you can do this?"
                R "Well, not completely, but I can at least try."
                M "Alright.... Let's go down to the basement."
                scene bg SleepBlack
                with fade
                $ renpy.pause ()
                scene bg HoneyDoList51
                with fade
                RT "{i}Uugghh.... I've always hated this basement!{/i}"
                RT "{i}But I'd follow that ass anywhere.{/i}"
                RT "{i}In fact, now's a great opportunity to add another pic to my collection.{/i}"
                scene bg HoneyDoList75
                with dissolve
                RT "{i}I've got to make this fast.{/i}"
                scene bg HoneyDoList52
                with fade
                RT "{i}Oh, that's beautiful!{/i}"
                play sound CameraClick
                show CamaraFlash
                $ mom_CreepShot_06 = True
                pause (0.25)
                scene bg HoneyDoList52
                RT "{i}Got it!{/i}"
                scene bg HoneyDoList51
                with fade
                $ renpy.pause ()
                scene bg HoneyDoList53
                with fade
                M "So, the washing machine keeps quitting in the middle of the cycle."
                M "Did you figure out how to fix that?"
                R "Yeah I think so.... It sounds like the belt that turns the drum got too tight."
                R "To fix it, I'm going to need your help."
                M "Great.... as long as you can guarantee my shirt will stay dry.... Just tell me what to do."
                scene bg HoneyDoList54
                with dissolve
                R "Take this wrench, and inside of the washing machine, at the very back, there is a nut that you have to secure the wrench on to keep it from turning."
                M "How will I know which nut to secure?"
                R "It's the only one, and it should fit that wrench perfectly."
                R "Now climb on in there."
                scene bg HoneyDoList55
                with fade
                M "So, I see a nut.... Is it right in the middle of the drum?"
                R "Yeah, that should be it."
                M "Ok, I've got it, now what are you going to do?"
                scene bg HoneyDoList56
                with dissolve
                R "I've just got to remove this panel so I can get into where the belt is."
                M "Well, this is kind of awkward.... Do you have to kneel right exactly there?"
                R "Sorry.... but yeah.... The YourTube video said that's the only way to fix this model of washing machine."
                scene bg HoneyDoList57
                with fade
                M "Now do you really have to lean into me like that?"
                R "Yeah, it's the only way I can reach the belt clear in the back."
                M "I'll bet repair men really hate this model of washing machine."
                R "Haha....Yeah, it's probably pretty awkward for two straight men to repair this together."
                M "Yeah?.... Well, it's not much better for a mother and son."
                R "What do you mean?  What could possibly make this awkward?"
                RT "{i}Holy shit!.... Mom's pretty much stuck in there.... I don't think she could turn around if she wanted to.{/i}"
                RT "{i}How am I going to take advantage of this situation?{/i}"
                RT "{i}Oh yeah.... I have an idea.{/i}"
                scene bg HoneyDoList58
                with dissolve
                play music SexMusic
                M "Well, it would be pretty awkward if you grinding into me while you're fixing that belt gave you an erection."
                scene bg HoneyDoList59
                with fade
                R "Don't worry Mom.  My penis is as soft as can be."
                M "Well, that's good to hear."
                scene bg HoneyDoList60
                with dissolve
                R "Ummmm....  actually...."
                M "Shit!.... [ryan]?.... Did you just make things more awkward?"
                scene bg HoneyDoList61
                with dissolve
                R "I didn't mean to!"
                R "It's because you brought it up!"
                scene bg HoneyDoList60
                with dissolve
                R "If you hadn't brought it up,...."
                R "I would probably still be soft."
                scene bg HoneyDoList61
                with dissolve
                M "Ghrrrrr.... You have got to be kidding me, [ryan]!"
                M "And why are you moving around so much back there?"
                scene bg HoneyDoList60
                with dissolve
                R "I'm sorry, I have to keep cranking this belt until it loosens up the motor bearings enough that they can turn easily on their own."
                R "And I can't crank the belt without moving around."
                scene bg HoneyDoList61
                with dissolve
                M "Well, I can't take this.... I'm going to come out while you're doing that!"
                R "Wait!.... No!.... You can't!...."
                M "Why?"
                R "Because if you let go of the wrench, the bearings will turn with the belt, and it won't fix the problem."
                if momlibido >= 8:
                    M "Fine.... Just try to hurry."
                    RT "{i}It's all fixed actually.... but I don't want this to end just yet.{/i}"
                    R "Ok Mom, I've just got to turn this belt several more times."
                    scene bg HoneyDoList62
                    with fade
                    RT "{i}Oh.... My.... God.... I'm hot dogging my own mom's ass!{/i}"
                    scene LaundryVideo01
                    with fade
                    M "Seriously, [ryan]!.... You've got to be almost done!"
                    scene bg HoneyDoList62
                    with fade
                    R "Yep!.... So close!...."
                    scene LaundryVideo01
                    with fade
                    RT "{i}Oh, shit.... I'm so close!{/i}"
                    scene bg HoneyDoList64
                    with dissolve
                    $ renpy.pause ()
                    RT "{i}Hnnnngggghhhh..........{/i}"
                    scene bg BlurryWhite
                    with vpunch
                    with hpunch
                    play sound Ejaculate
                    scene bg HoneyDoList65
                    with fade
                    $ renpy.pause ()
                    play sound Ejaculate
                    scene bg HoneyDoList66
                    with dissolve
                    with vpunch
                    with hpunch
                    $ renpy.pause ()
                    MT "{i}Oh good!  I don't feel [ryan] pressing against my ass anymore.{/i}"
                    MT "{i}He must finally be done.{/i}"
                    M "I don't care if you're done, or not.... My knees are killing me, and I've got to get out of here."
                    scene bg HoneyDoList76
                    with dissolve
                    R "Aaahhh...Wait just a second!"
                    M "Nuh uh.... I'm coming out now!"
                    scene bg HoneyDoList67
                    with dissolve
                    RT "{i}Shit, shit, shit!....{/i}"
                    RT "{i}I've got to get my pants back up!{/i}"
                    scene bg HoneyDoList69
                    with dissolve
                    RT "{i}Pheww.... That was close.{/i}"
                    M "[ryan]?.... What the hell?.... Was all of that grinding really necessary?"
                    R "I'm sorry Mom, but I already told you.... I couldn't keep my body still and turn the belt at the same time!"
                    M "Yeah.... Well.... That would've been fine, if you hadn't been pitching a tent the entire time!"
                    RT "{i}Oh, good.... She didn't realize that there was no tent involved.{/i}"
                    R "Well, that was your fault for making it sexual!"
                    M "What?.... Are you kidding?"
                    R "I just wanted to fix a washing machine, but you brought up how awkward a boner would be."
                    R "You put those thoughts in my head!"
                    R "And it didn't help that you were wearing shorts that make your ass look so incredible!"
                    M "...."
                    M "Ok, [ryan].... I'm sorry if I made that awkward for you.... I may have misread the situation."
                    R "That's ok.... I understand why you thought that was awkward."
                    M "Yeah.... We should just kill whoever designed that goddamn washing machine."
                    R "Haha.... Yeah.... Well.... I should run along then."
                    M "Sure [ryan].... Thanks for your help!"
                    R "Of course! Love ya, Mom."
                    M "I love you too."
                    scene bg SleepBlack
                    with fade
                    scene bg HoneyDoList71
                    with fade
                    MT "{i}That horny little bull-shitter!{/i}"
                    MT "{i}What am I going to do with him?{/i}"
                    MT "{i}.... And why do I get butterflies when he compliments my ass?{/i}"
                    "{i}{b}\"Mom's Libido +1\"{/b}{/i}"
                    $ momlibido += 1
                    scene bg HoneyDoList72
                    with dissolve
                    MT "{i}Huh?.... What's this?{/i}"
                    scene bg HoneyDoList73
                    with fade
                    MT "{i}Is that?.... Oh, shit....{/i}"
                    scene bg HoneyDoList74
                    with dissolve
                    MT "...."
                    MT "{i}I've got to remember to tell [ryan] that the washing machine is leaking laundry detergent.{/i}"
                    $ fixed_washer = 2
                    play music Honey
                    $ timeofdaycounter += 1
                    jump myroom
                else:
                    M "I don't care!.... You're literally grinding against my ass!"
                    scene bg HoneyDoList68
                    with dissolve
                    RT "{i}I've got to get my pants back up! {/i}"
                    scene bg HoneyDoList70
                    with dissolve
                    RT "{i}Pheww.... That was close.{/i}"
                    M "[ryan]?.... What the hell?.... Was all of that grinding really necessary?"
                    R "I'm sorry Mom, but I already told you.... I couldn't keep my body still and turn the belt at the same time!"
                    M "Yeah.... Well.... That would've been fine, if you hadn't been pitching a tent the entire time!"
                    RT "{i}Oh good.... She didn't realize that there was no tent involved.{/i}"
                    R "Well, that was your fault for making it sexual!"
                    M "What?.... Are you kidding?"
                    R "I just wanted to fix a washing machine, but you brought up how awkward a boner would be."
                    R "You put those thoughts in my head!"
                    R "And it didn't help that you were wearing shorts that make your ass look so incredible!"
                    M "...."
                    M "Ok, [ryan].... I'm sorry if I made that awkward for you.... I may have misread the situation."
                    R "That's ok.... I understand why you thought that was awkward."
                    M "Yeah.... We should just kill whoever designed that goddamn washing machine."
                    R "Haha.... Yeah.... Well, I should run along then."
                    M "Sure [ryan].... Thanks for your help!"
                    R "Of course! Love ya, Mom."
                    M "I love you too."
                    "{i}\"The ending to this event is different if Mom's libido is higher (+8).\"{/i}"
                    "{i}\"Raise her libido and try again next weekend.\"{/i}"
                    $ fixed_washer = 1
                    play music Honey
                    $ timeofdaycounter += 1
                    jump myroom
            "Don't help Mom.":
                $ screen_on = "momcleanloungemap03"
                call screen momcleanloungemap03

##############  Park  ######################################  Park  ##################################################################  Park  ##################################################  Park  ##################################################################  Park  #######################################################################  Park  ######################

label run_training:
    if physical_fitness >= 3:
        scene bg SleepBlack
        with fade
        scene bg SidneyRun63
        with fade
        RT "{i}I'm feeling pretty good today. I should have no problem keeping this pace all the way to the park.{/i}"
        "{i}\"[ryan]'s physical fitness +1\"{/i}"
        $ physical_fitness += 1
        scene bg SidneyRun34
        with fade
        R "Ok, now I feel sick, pant.... pant...."
        RT "{i}Well, at least I should be able to keep up with Sidney now.{/i}"
        RT "{i}So, I should be able to bring her to the park now, without her having to be afraid of poor Mr. Peterson.{/i}"
        RT "{i}I still don't see any sign of him though.{/i}"
        RT "{i}Oh well, time to run back home.{/i}"
        scene bg SleepBlack
        with fade
        scene bg SidneyRun58
        with fade
        RT "{i}Man, I'm not in the greatest shape, but I made it there in 9 minutes. I should now be able to keep up with Sidney.{/i}"
        scene bg SidneyRun59
        with dissolve
        S "Hey, [ryan]. Any luck at the park today?"
        scene bg SidneyRun64
        with fade
        S "Any run-in's with crazy old Mr. Peterson?"
        R "No, still no sign of him."
        R "I did make it to the park in really good time though."
        R "I think I could even keep up with you now."
        S "Do you think he would leave me alone if you were there with me?"
        R "Probably, and even if he didn't, I'd really like to help catch him, then they can get him back to the nursing home and get the help he needs."
        scene bg SidneyRun60
        with dissolve
        S "I wish you weren't so concerned with the welfare of my sexual harasser!"
        R "Mr. Peterson is a stud!  Did you know he saved most of his unit by running Rambo style towards a machine gun nest, miraculously taking out the gunner and his relief gunner?"
        R "I think he ended up getting the Medal of Honor for his heroism."
        S "I really don't care how cool the crazy pervert in the park is."
        S "I just wish he'd leave!"
        R "Well, hopefully someone catches him soon."
        S "Alright, well I'm out of here."
        scene bg SidneyRun61
        with dissolve
        R "See ya, Sid."
        R "{i}I'll just watch that backside all the way out of the room.{/i}"
        $ fit_enough = True
        $ timeofdaycounter += 1
        jump lounge
    else:
        scene bg SleepBlack
        with fade
        scene bg SidneyRun08
        with fade
        RT "{i}Oh, I feel like I'm going to be sick! I've got to push on though to make sure Sidney will be safe at the park.{/i}"
        scene bg SidneyRun34
        with fade
        R "I made it.... pant.... pant...."
        "{i}\"[ryan]'s physical fitness +1\"{/i}"
        $ physical_fitness += 1
        RT "{i}And no sign of Mr. Peterson.{/i}"
        RT "{i}There's still no way I could keep up with Sidney.  I should probably keep training.{/i}"
        RT "{i}If she gets here before me, she could be at risk of running into Mr. Peterson while she's all alone.{/i}"
        RT "{i}Man, I'm tired. I think I'll just walk home.{/i}"
        scene bg SleepBlack
        with fade
        scene bg SidneyRun58
        with fade
        RT "{i}Man, I'm still in really bad shape. At least I made it to the park this time though.{/i}"
        scene bg SidneyRun59
        with dissolve
        S "Oh, hey [ryan]. How was your run in the park today?"
        scene bg SidneyRun64
        with fade
        S "Did you see crazy old Mr. Peterson?"
        R "No, but that doesn't mean he wasn't there.  The vegetation in the park is so thick, it would be almost impossible to find someone who didn't want to be found."
        S "Well, luckily for you he isn't into male prostitutes, or he probably would have popped out to flash you his wrinkly old coin purse."
        R "Don't be too hard on him.  Don't forget he's a war hero who's off his medication."
        scene bg SidneyRun60
        with dissolve
        S "Yeah, well.... Whatever!"
        S "I guess I'm never going running in that park again until the old pervert is caught, or they find his dead body."
        R "If you go with me, I'm sure you'll be fine."
        scene bg SidneyRun64
        with dissolve
        S "Yeah, well I don't want to have to run at half my pace so you can keep up with me."
        R "Don't worry, I'll be in shape soon."
        S "I hope so. Well, I'm off to take a shower."
        scene bg SidneyRun61
        with dissolve
        S "See you later!"
        R "Later, Sid!"
        $ timeofdaycounter += 1
        jump lounge

label not_fit_enough:
    if groped_in_park == 1:
        scene bg SleepBlack
        with fade
        scene bg SidneyRun04
        with fade
        $ persistent.gal_NTR_3 = True
        S "Alright! Get stretched out and we'll take off."
        S "Just let me know when you're ready."
        R "...."
        R "Ok, let's go."
        scene bg SidneyRun05
        with fade
        RT "{i}Oh, shit!.... I'm still not going to be able to keep this pace.{/i}"
        R "Hey Sid, I need to slow down a little."
        S "I really don't want to. I'm trying to get better at running not worse."
        R "Well, I'm sorry, but I'm not going to be able to keep this pace. You'll have to go on ahead of me."
        R "You should hold back, so you're not alone in the park with Mr. Peterson again."
        S "Shit!.... I know I should.... I'm just going to go for it.  I'll just try to be extra vigilant for that crazy old pervert."
        scene bg SidneyRun06
        S "{i}(yelling){/i}Try to hurry though, I feel much safer when you're there with me!"
        R "{i}(yelling){/i} I'll try, but I might need to stop for a second to take a rest."
        scene bg SidneyRun08
        with fade
        RT "{i}Uugghh.... I pushed it too hard again trying to keep up with her.{/i}"
        scene bg SidneyRun07
        with dissolve
        RT "{i}I just need to take a minute to rest.{/i}"
        scene bg SleepBlack
        with fade
        scene bg SidneyRun10
        with fade
        ST "{i}Ooofff.... I'm tired!  I made pretty good time though.{/i}"
        ST "{i}It would have been even better if [ryan] hadn't slowed me down.{/i}"
        scene bg SidneyRun11
        with dissolve
        ST "{i}Man, I am a sweaty mess.{/i}"
        scene bg SidneyRun13
        with fade
        MPT "{i}Well, would you look at that.{/i}"
        scene bg SidneyRun14
        with fade
        MPT "{i}The saucy little whore who keeps getting away from me.{/i}"
        MPT "{i}I need some pussy so bad! If I could even get a taste of it, I'd be happy.{/i}"
        MPT "{i}She must not speak English very well. She didn't seem to understand I was trying to pay her.{/i}"
        MPT "{i}She must have thought I was trying to kidnap her.{/i}"
        MPT "{i}I need to sneak in there again and take her by surprise. I think she'll understand what I'm after if I'm a little more direct.{/i}"
        scene bg SidneyRun23
        with fade
        ST "{i}Typical, [ryan]'s nowhere to be seen.  I need to rest a little more before I take off for home.{/i}"
        scene bg SidneyRun24
        with dissolve
        ST "{i}He always seems to come out of these bushes.  I think I'll try resting on the other end of the park.{/i}"
        scene bg SidneyRun37
        with fade
        ST "{i}I should be able to see him coming from here, if he pops out of his hideout in those bushes.{/i}"
        scene bg SidneyRun38
        with fade
        ST "{i}So far I don't see any sign of him.{/i}"
        scene bg SidneyRun39
        with dissolve
        ST "{i}I better just make sure he's not sneaking up behind me.{/i}"
        scene bg SidneyRun40
        with dissolve
        ST "{i}Ok, I think I should be safe to take a little rest on the grass right here. I'll just keep my eyes peeled.{/i}"
        scene bg SidneyRun41
        with fade
        $ renpy.pause ()
        scene bg SidneyRun42
        with dissolve
        $ renpy.pause ()
        scene bg SidneyRun43
        with dissolve
        S "Aaaaahhhh!...."
        MPT "{i}Oh yeah! What a sweet smelling pussy!{/i}"
        MPT "{i}It should be pretty clear to her what I'm after now.  Hopefully she'll take my money.{/i}"
        scene bg SidneyRun44
        with dissolve
        S "YOU.... DIRTY.... OLD.... PERVERT! Let go.... of my legs.... and get your face.... out of my pussy!"
        scene bg SidneyRun45
        with dissolve
        RT "{i}What the hell?{/i}"
        R "Sidney!  Are you ok?"
        S "HELP!"
        scene bg SidneyRun46
        with fade
        R "I'm coming!"
        MP "Shit!"
        scene bg SidneyRun47
        with fade
        R "Mr. Peterson! Stop!"
        scene bg SidneyRun48
        with fade
        R "{i}(gasping){/i}Holy fuck!.... I'm gonna pass out!"
        "{i}\"[ryan]'s physical fitness +1\"{/i}"
        $ physical_fitness += 1
        R "How can that old man be so fast?"
        S "Or so sneaky?"
        scene bg SidneyRun49
        with dissolve
        R "Are you ok?"
        S "I guess. Knowing he's just crazy makes me not feel so violated."
        S "But I'm not coming here again until he's caught, or until you're in good enough shape to keep up with me."
        S "He wouldn't have touched me if you had been here."
        R "Ok, I'll let you know when I'm in good enough shape."
        S "Alright, I'm going to head home."
        S "I'll see you later."
        R "Later, Sid."
        $ groped_in_park = 2
        $ timeofdaycounter += 1
        jump myroom
    else:
        scene bg SleepBlack
        with fade
        scene bg SidneyRun04
        with fade
        S "There you are. Are you going to stretch this time?"
        R "Yeah I think I will. My legs got really sore last time."
        S "Ok, just let me know when you're ready."
        R "...."
        R "Ok, let's go."
        scene bg SidneyRun05
        with fade
        RT "{i}Oh, shit!.... I'm not going to be able to keep this pace.{/i}"
        R "Hey Sid, is there any way we can slow down a little."
        S "I really don't want to. I'm trying to get better at running not worse."
        R "Well, I'm sorry, but I'm not going to be able to keep this pace. You'll have to go on ahead of me."
        scene bg SidneyRun06
        S "{i}(yelling){/i} Don't take too long. I don't want to have to wait at the park very long with that crazy old man on the loose!"
        R "{i}(yelling){/i} I'll try, but I might need to stop for a second to take a rest."
        scene bg SidneyRun08
        with fade
        RT "{i}Uugghh.... I pushed it too hard again trying to keep up with her.{/i}"
        scene bg SidneyRun07
        with dissolve
        RT "{i}I just need to take a minute to rest.{/i}"
        scene bg SleepBlack
        with fade
        scene bg SidneyRun10
        with fade
        ST "{i}Ooofff.... I'm tired!  I made pretty good time though.{/i}"
        ST "{i}It would have been even better if [ryan] hadn't slowed me down.{/i}"
        scene bg SidneyRun11
        with dissolve
        ST "{i}Man, I am a sweaty mess though.{/i}"
        scene bg SidneyRun13
        with fade
        MPT "{i}Well, would you look at that.{/i}"
        MPT "{i}That shriekin' hooker is back.{/i}"
        scene bg SidneyRun14
        with fade
        MPT "{i}She must be a hooker for the commies then.{/i}"
        MPT "{i}Why else would she have screamed like she did?{/i}"
        MPT "{i}I need to help her realize that my money is just as good as her commie compatriots, even better actually.{/i}"
        MPT "{i}I need to sneak in there without her seeing me so that she doesn't alert the commie MP's.{/i}"
        scene bg SidneyRun21
        with fade
        ST "{i}Shit! I wish [ryan] would hurry.{/i}"
        scene bg SidneyRun22
        with dissolve
        ST "{i}I just want to get out of here.{/i}"
        scene bg SidneyRun21
        with dissolve
        $ renpy.pause ()
        scene bg SidneyRun22
        with dissolve
        $ renpy.pause ()
        scene bg SidneyRun23
        with fade
        ST "{i}Fuck it. I'm going to leave just as soon as I'm rested.{/i}"
        scene bg SidneyRun24
        with dissolve
        ST "{i}There doesn't seem to be any sign of that crazy old pervert.{/i}"
        ST "{i}I'll just sit here on this bench to wait for [ryan].{/i}"
        scene bg SidneyRun25
        with dissolve
        $ renpy.pause ()
        scene bg SidneyRun26
        with dissolve
        $ renpy.pause ()
        S "What the hell?"
        MP "Hello again, beautiful."
        scene bg SidneyRun27
        with dissolve
        MP "I know I'm not one of your commie customers, but my money is worth even more, and I think you'll find my dick is twice as big."
        S "Get your hands off of me!"
        S "HELP!"
        scene bg SidneyRun28
        with fade
        S "HELP!"
        RT "{i}Holy shit!{/i}"
        RT "{i}Mr. Peterson's grabbing Sidney!{/i}"
        R "HEY!"
        scene bg SidneyRun29
        with dissolve
        MP "Damnit girl! I just wanted a taste! And now your commie friends are coming!"
        R "Mr. Peterson! Let go of her, and let's talk!"
        MP "How do you know my name? You commie spy!"
        R "No! Don't run!"
        scene bg SidneyRun30
        with fade
        R "No, Mr. Peterson! Stop!"
        scene bg SidneyRun31
        with fade
        R "Hey Sid, I'll be right back!"
        scene bg SidneyRun32
        with fade
        R "Mr. Peterson!  I just want to talk to you!"
        scene bg SidneyRun33
        with fade
        RT "{i}How in the hell is that old man so fast?{/i}"
        scene bg SidneyRun34
        with fade
        RT "{i}Holy hell! My lungs are going to explode!{/i}"
        "{i}\"[ryan]'s physical fitness +1\"{/i}"
        $ physical_fitness += 1
        RT "{i}Spritely old fucker.{/i}"
        RT "{i}I'd better go check on Sidney.{/i}"
        scene bg SidneyRun35
        with fade
        S "You let him get away?"
        R "Sorry!  I was already exhausted from running over here."
        R "Plus that old man is quick!"
        scene bg SidneyRun36
        S "I told you he was a huge pervert!"
        R "Well yeah, a guy like that's probably used to getting pussy all the time, and now that he's confused, and off his meds, he's probably hornier than usual."
        R "Did he get you very bad?"
        S "No, just groped my boob a little."
        S "I'm sure I'd feel more violated if I didn't know he was so bat-shit crazy."
        S "Fucker still thinks I'm a prostitute."
        S "Alright, well I'm going to run home."
        R "I'll see you there. I'm too tired to run anymore."
        $ timeofdaycounter += 1
        $ groped_in_park = 1
        jump myroom

label park_activities:
    scene bg SleepBlack
    with fade
    scene bg SidneyRun09
    with fade
    $ renpy.pause ()
    scene bg SidneyRun50
    with fade
    $ persistent.gal_Sidney_5 = True
    R "We made great time today!"
    S "Yeah, we seem to be improving all the time."
    scene bg SidneyRun51
    with fade
    S "I've got to get this shirt off. I'm dripping in sweat."
    R "me too, and I've got a side ache."
    S "We should take a little rest before we run back home."
    if mp_captured:
        scene bg SidneyRun53
        with fade
        S "That pesky policeman doesn't seem to be around at all anymore."
        R "I'm sure he's serving and protecting elsewhere now that Mr. Peterson is gone."
        S "So, let's do something naughty to reward ourselves, for running all the way out here."
        R "But there's other people in the park."
        S "I know. That's what makes it extra fun."
        S "Plus, they're not paying any attention to us."
        ST "{i}Yet.{/i}"
        R "So, what do you have in mind?"
        S "Whatever you want to do. You're the hero of the park."
        jump park_menu
    if cop_block:
        scene bg SidneyRun52
        with fade
        S "Do you see the policeman anywhere around?"
        R "The policeman?  I thought you were more worried about Mr. Peterson."
        S "Oh my God, yeah.... I wonder if he watched us grinding each other."
        RT "{i}Holy shit! I think some kind of switch has gone off in Sidney's brain.{/i}"
        S "So, do you see the policeman?"
        R "No, I don't see him anywhere."
        R "But I do see a few other people walking around the park."
        scene bg SidneyRun53
        with dissolve
        S "Do we know any of them?"
        R "I.... Didn't get a good look."
        S "Hmmm.... Well, let's hope not."
        R "Wow!.... So it doesn't bother you at all anymore that we're siblings?"
        S "Well no, I mean we're just helping each other out.... We're not taking it too far."
        S "I've been talking to a few of my girlfriends from college, and according to them, siblings experimenting with each other and fooling around, is pretty common."
        S "So, why don't you quit worrying, and lets...."
        X "HELP!"
        scene bg SidneyRun54
        with dissolve
        S "What in the?"
        R "Holy fuck!"
        scene bg SidneyRun65
        with fade
        S "It's Mr. Peterson!"
        R "And he's attacking my art teacher, Mrs. Stone!"
        MS "Please help me!"
        R "That's it!"
        play sound Punch
        scene bg SidneyRun66
        with fade
        S "Oooffff...."
        R "That's it, Mr. Peterson!"
        R "You're not getting away from me this time!"
        scene bg SidneyRun67
        with dissolve
        R "This is...."
        scene bg SidneyRun68
        with fade
        R "for your...."
        scene bg SidneyRun69
        with fade
        R "own good!"
        play sound Punch
        scene bg SidneyRun70
        with fade
        MP "Urrmmmppphhhh...."
        MP "...."
        R "Are you ok, Mr. Peterson?"
        MP "(groaning)"
        scene bg SidneyRun71
        with dissolve
        P "Nice tackle, kid!"
        P "And by the looks of things, I don't think you broke any of his bones."
        P "That tough son of a bitch."
        P "He's a war hero, you know!"
        R "Yeah, and a Medal of Honor recipient."
        P "His family is going to be so relieved to have him back."
        P "You're a hero!"
        R "Oh.... Just doing my civic duty."
        P "Well, I'll make sure they hear about it."
        scene bg SidneyRun72
        with fade
        P "Come on Mr. Peterson. Your family is worried sick about you."
        MP "Can that young prostitute come with us?"
        P "We'll see if she's willing to visit you in the nursing home."
        S "Ahhh...."
        scene bg SidneyRun73
        with fade
        play music SexMusic
        MS "Oh my God! [ryan]!.... You're my hero!"
        MS "Let me just help you up, and give you a great big hug!"
        scene bg SidneyRun74
        with dissolve
        R "Thanks, Mrs. Stone!"
        MS "I just can't believe how brave you were!"
        scene bg SidneyRun75
        with fade
        MS "Not only did you rescue me, but you also helped that poor old man."
        MS "The poor thing's been surviving off of the land for weeks."
        scene bg SidneyRun74
        with fade
        MS "I sure hope they give you some kind of medal."
        R "Oh, don't be silly. I don't deserve a medal."
        MS "Oh, and you're so humble."
        scene bg SidneyRun76
        with dissolve
        play music Honey
        S "Sorry to interrupt, but shouldn't we be getting home?"
        ST "{i}This bitch better back off my brother.{/i}"
        scene bg SidneyRun78
        with dissolve
        MS "And who might this be?"
        R "Oh, no one.... I mean.... this is my sister Sidney."
        scene bg SidneyRun77
        with dissolve
        MS "Sister?.... But didn't I see her climbing up on your lap right before I got grabbed by Mr. Peterson?"
        R "Oh, she was just giving me a purely platonic, sisterly hug."
        scene bg SidneyRun78
        with dissolve
        MS "Oh.... So that's how white folks show their siblings affection?"
        S "As a matter of fact, yeah, that's how it is."
        scene bg SidneyRun77
        with dissolve
        MS "Well, it's none of my business anyhow."
        MS "And I've got to get to school before my first class starts."
        scene bg SidneyRun76
        with dissolve
        MS "Thank you so much again for saving me today!"
        MS "If the city doesn't give you a reward, I'm sure I can think up a good one to give you."
        ST "{i}She better not be implying what I think she's implying!{/i}"
        RT "{i}Holy shit! Is she implying what I think she's implying?{/i}"
        S "And I think I'm going to be sick. [ryan], let's go home."
        MS "Goodbye, my savior!"
        scene bg SleepBlack
        with fade
        scene bg SidneyRun57
        with fade
        S "You did it! No more crazy pervert to worry about at the park."
        R "Yeah, now you'll be able to go there any time you like."
        S "And what about Mrs. Stone?"
        R "What about her?"
        S "She was all over you."
        R "Oh, she was just super grateful that I saved her."
        S "Seemed like more than that to me."
        R "Hmmmm.... I didn't notice."
        S "Would you like it to be more?"
        S "I mean, I know you've told me you think of her when we fooled around."
        RT "{i}I was lying when I said that, but after those soft pillows in my face, I might actually start thinking about her.{/i}"
        S "Well?"
        R "Well, what?"
        S "Would you like it to be more?"
        menu:
            "Yes.":
                R "I mean I guess I wouldn't complain if she wanted a go at me."
                RT "{i}Could Sidney be right?  Could I really have a chance with Mrs. Stone?{/i}"
                "{i}{b}\"Sidney's Affection -2\"{/b}{/i}"
                $ sidneyaffection -= 2
            "No.":
                R "I'm over her.  I've got another girl in mind."
                R "One that lives a little closer to home, if you know what I mean."
                RT "{i}Actually several, but Sidney will think I just mean her.{/i}"
                RT "{i}At least I'm pretty sure that's what she wants to hear.{/i}"
                "{i}{b}\"Sidney's Affection +2\"{/b}{/i}"
                $ sidneyaffection += 2
        S "Well, the park will be a lot less interesting with Mr. Peterson gone."
        S "Unless we can find a way to make it more interesting."
        S "I'll beat you home!"
        $ timeofdaycounter += 1
        $ mp_captured = True
        jump myroom
    if mp_cockblock and finished_wr_shoot:
        scene bg SidneyRun22
        with fade
        $ renpy.pause ()
        scene bg SidneyRun21
        with dissolve
        S "But do you think we're safe from the crazy pervert?"
        R "Yeah, I think Mr. Peterson will leave us alone while we're together."
        S "Alright, but stay close to me so he can't sneak up between us."
        scene bg SidneyRun52
        with fade
        R "It's ok, Sidney. I'm sure he'd never try anything with me right here."
        scene bg SidneyRun55
        with dissolve
        S "I sure hope you're right."
        MPT "{i}Damnit! The prostitute already has a customer!{/i}"
        MPT "{i}I wish I could just snap that commie's scrawny neck and take that whore in the bushes, but I can't risk bringing the wrath and scrutiny of the enemy army on me while I'm all alone out here.{/i}"
        MPT "{i}God, I hope my unit finds me soon.{/i}"
        RT "{i}Damn, Sidney's tits look incredible all covered in sweat and glistening in the sunlight.{/i}"
        scene bg SidneyRun53
        with dissolve
        play music SexMusic
        R "Oh, wow! What's that for?"
        S "I just wanted to thank you for making all the effort to get into shape. I'm so happy that I can keep running in the park, and I feel so much safer with you here."
        RT "{i}Oh my God! My sister is making me hard.{/i}"
        S "{i}(teasingly){/i} [ryan]? Is that what I think it is?"
        S "Oh my God! That's turning me on so bad!"
        scene SidneyRunVideo01
        with fade
        R "Holy shit, Sidney!  You do realize we are in public right?"
        S "Shhh.... Just enjoy it."
        R "But what if someone we know...."
        S "Shhh...."
        R "But what if Mr. Peterson...."
        S "Shhh...."
        R "...."
        X "Hey! You two on the bench"
        stop music
        play sound Scratch
        play music Honey
        scene bg SidneyRun56
        with dissolve
        P "I'm going to have to ask you two to tone it down."
        S "I'm sorry. I didn't realize we were doing anything wrong."
        P "Well, what you were doing isn't technically illegal, but you two were sure pushing the boundaries of indecent exposure."
        R "We're sorry."
        P "Ok buddy, Why don't you take your little girlfriend and do this in the privacy of your own home."
        R "But she's not my girlfriend, she's my.... I mean uhhh...."
        S "Just friends with benefits."
        ST "{i}He can be such an idiot!{/i}"
        P "Yeah, I don't really care about the details of your relationship, just take it somewhere else, ok?"
        R "Yeah, we're leaving right now."
        scene bg SleepBlack
        with fade
        scene bg SidneyRun57
        with fade
        R "Holy shit! I can't believe that just happened."
        S "I know! Wasn't it exciting?"
        R "Exciting?"
        S "Yeah, the fact that anyone could've been watching?"
        R "Someone was watching.  The fucking policeman saw it all!"
        S "Haha.... I wonder if he'll think about us the next time he jacks off, or is fucking his wife."
        R "Holy shit, Sidney!"
        R "Are you some kind of exhibitionist?"
        S "...."
        S "No.... I don't think so...."
        ST "{i}Shit!!!.... What is wrong with me?....{/i}"
        ST "{i}First incestual desires, and now exhibitionism?.... God, I need to go to church.{/i}"
        $ timeofdaycounter += 1
        $ cop_block = True
        jump myroom
    else:
        scene bg SidneyRun22
        with fade
        $ renpy.pause ()
        scene bg SidneyRun21
        with dissolve
        S "But, do you think we're safe from the crazy pervert?"
        R "Yeah, I think Mr. Peterson will leave us alone while we're together."
        S "Alright, but stay close to me so he can't sneak up between us."
        scene bg SidneyRun52
        with fade
        R "It's ok, Sidney. I'm sure he'd never try anything with me right here."
        scene bg SidneyRun55
        with dissolve
        S "I sure hope you're right."
        MPT "{i}Damnit! The prostitute already has a customer!{/i}"
        MPT "{i}I wish I could just snap that commie's scrawny neck and take that whore in the bushes, but I can't risk bringing the wrath and scrutiny of the enemy army on me while I'm all alone out here.{/i}"
        MPT "{i}God, I hope my unit finds me soon.{/i}"
        RT "{i}Damn, my sister's tits look incredible all covered in sweat and glistening in the sunlight.{/i}"
        scene bg SidneyRun53
        with dissolve
        R "Oh wow! What's that for?"
        S "I just wanted to thank you for making all the effort to get into shape. I'm so happy that I can keep running in the park, and I feel so much safer with you here."
        "{i}{b}\"Sidney's Respect +1\"{/b}{/i}"
        $ sidneyrespect += 1
        RT "{i}Oh my God! Is my sister going to kiss me?{/i}"
        "{i}(rustling sound in bushes){/i}"
        scene bg SidneyRun54
        with dissolve
        S "Oh, shit!  I'm pretty sure I heard something."
        S "Hurry, let's run home."
        RT "{i}Damnit! Cock-blocked by Mr. Peterson.{/i}"
        R "Ok, let's go."
        scene bg SleepBlack
        with fade
        scene bg SidneyRun57
        with fade
        $ renpy.pause ()
        $ mp_cockblock = True
        $ timeofdaycounter += 1
        jump myroom

label park_menu:
    scene bg SidneyRun53
    menu:
        "Public Fingering" if sidneylibido >=8:
            play music SexMusic
            S "Oh my God!  Are you serious?"
            S "I can't fucking wait!"
            play sound Sidney01 loop
            scene SidneyRunVideo02
            with fade
            $ renpy.pause ()
            S "I'm going to cum with my own brother's fingers in my pussy!"
            S "I should be thinking of someone else.... fuck.... but that doesn't turn me on as much!"
            $ renpy.pause ()
            scene bg SidneyRun79
            with dissolve
            S "Holy shit, I'm going to cum!"
            scene bg SidneyRun80
            with dissolve
            ST "{i}Fuck, fuck, fuck, I'm squirting right into my shorts!{/i}"
            stop sound
            scene bg SidneyRun81
            with dissolve
            S "Holy fuck! It looks like I completely pissed myself."
            S "You made me gush like a fountain."
            "{i}{b}\"Sidney's Libido -3\"{/b}{/i}"
            $ sidneylibido -= 3
            S "It's a good thing I've got that shirt I can tie around my waist."
            S "I think we better head straight home."
            R "Yeah, whenever you're ready."
            $ park_finger = True
            if park_finger and park_hj and park_pussy_eat and park_bj:
                $ park_full_menu = True
            else:
                pass
            play music Honey
            $ timeofdaycounter += 1
            jump myroom
        "{s}Public Fingering{/s} {i}(Sidney's Libido 8+){/i}" if sidneylibido <=7:
            jump park_menu
        "Public Handjob":
            play music SexMusic
            S "Oh my God! Do you think we can get away with it, right here on the park bench?"
            S "I kind of hope someone sees us."
            S "It's just so naughty."
            scene SidneyRunVideo03
            with dissolve
            $ renpy.pause ()
            S "I can't believe I'm stroking your huge cock in public like this."
            $ renpy.pause ()
            scene bg SidneyRun82
            with dissolve
            R "Holy fuck, I'm gonna cum!"
            S "Just let it go!"
            play sound Ejaculate
            scene bg SidneyRun83
            with dissolve
            with vpunch
            with hpunch
            R "Ahhhhh...."
            $ renpy.pause ()
            play sound Ejaculate
            scene bg SidneyRun84
            with dissolve
            with vpunch
            with hpunch
            ST "{i}It's still coming!{/i}"
            $ renpy.pause ()
            scene bg SidneyRun85
            with dissolve
            S "Wow! You covered me."
            S "Do you think anyone saw?"
            R "Probably not, I don't see anybody watching, but maybe."
            S "Oh, I can't believe we did that in the open like this."
            S "Should I run home with your cum all over me?"
            R "God! Are you kidding?"
            S "Of course I'm kidding, numb-nuts."
            S "So, were you thinking about Megan or Mrs. Stone?"
            R "Oh, shit! It was feeling so good, I just completely forgot to think about someone else!"
            S "[ryan]! You can't think about your sister while she's jacking you off, it will make things weird!"
            ST "{i}That's right, he was thinking of me! Suck it Megan and Mrs. Stone!{/i}"
            "{i}{b}\"Sidney's Libido +2\"{/b}{/i}"
            R "Sorry, I'll try to remember next time."
            S "Now do you see my shirt anywhere? I need to wipe myself off so we can go home."
            play music Honey
            $ sidneylibido += 2
            $ park_hj = True
            if park_finger and park_hj and park_pussy_eat and park_bj:
                $ park_full_menu = True
            else:
                pass
            $ timeofdaycounter += 1
            jump myroom
        "Eat Pussy" if sidneylibido >=8:
            play music SexMusic
            R "Can I taste your pussy?"
            S "Hmmm.... I don't think we could get away with that one on the park bench, without someone calling the cops."
            S "I've got an idea, though."
            S "Follow me."
            scene bg SidneyRun86
            with fade
            R "Ok, the coast is clear. Let's go."
            scene bg SidneyRun87
            with fade
            R "What if someone walks in on us while...."
            S "Shhhh...."
            S "We'll deal with that when it happens."
            R "You mean *if* it happens."
            S "Yes.... of course."
            R "But, what if it's someone we know?"
            S "Do you want to talk, or do you want to take my shorts off?"
            play sound Sidney01 loop
            scene bg SidneyRun95
            with fade
            $ renpy.pause ()
            scene SidneyRunVideo04
            with fade
            $ renpy.pause ()
            ST "{i}Holy fuck! I can't believe I'm getting my pussy licked in the park.{/i}"
            ST "{i}Ohh.... He's even licking my ass-hole!{/i}"
            $ renpy.pause ()
            ST "{i}Oh God! My own brother is licking my ass-hole!{/i}"
            ST "{i}I've got to think about someone else besides him!.... Fuck!.... It's just not as exciting that way!{/i}"
            ST "{i}Fine, I'll just give in this one last time.{/i}"
            ST "{i}Oh God, yes! My brother is licking my pussy and ass!{/i}"
            $ renpy.pause ()
            scene bg SidneyRun96
            with fade
            S "Holy shit! My pussy is exploding!"
            R "Holy shit! You're like a fire hydrant!"
            S "Oh God, that feels good!"
            "{i}{b}\"Sidney's Libido -3\"{/b}{/i}"
            $ sidneylibido -= 3
            stop sound
            scene bg SidneyRun97
            with dissolve
            S "Wow! You just gave me one of the best orgasms I've ever had!"
            R "I just can't believe how much you squirted.  It was like a fucking porno."
            R "If the fashion industry doesn't work out for you, I think you still have a bright future in...."
            S "Don't you dare finish that sentence."
            S "Haha.... Let me get my shorts back on, and we'll run home."
            play music Honey
            $ park_pussy_eat = True
            if park_finger and park_hj and park_pussy_eat and park_bj:
                $ park_full_menu = True
            else:
                pass
            $ timeofdaycounter += 1
            jump myroom
        "{s}Eat Pussy{/s} {i}(Sidney's Libido 8+){/i}" if sidneylibido <=7:
            jump park_menu
        "Blowjob":
            play music SexMusic
            R "Would you be willing to suck my dick?"
            S "Hmmm.... I don't think we could get away with that one on the park bench, without someone calling the cops."
            S "I've got an idea though."
            S "Follow me."
            scene bg SidneyRun86
            with fade
            R "Ok, the coast is clear. Let's go."
            scene bg SidneyRun87
            with fade
            R "What if someone walks in on us while...."
            S "Shhhh...."
            S "We'll deal with that when it happens."
            R "You mean *if* it happens."
            S "Yes.... of course."
            R "But, what if it's someone we know?"
            S "Do you want to talk, or do you want to get your dick sucked?"
            R "Ok, I choose the dick option."
            play sound Blow03 loop
            scene SidneyRunVideo05
            with fade
            $ renpy.pause ()
            ST "{i}It's going down my throat much easier than it used to.{/i}"
            ST "{i}I wonder if he can tell.{/i}"
            menu:
                "That feels so good!":
                    R "Holy fuck, Sidney!  You just keep getting better and better at this!"
                    ST "{i}Yay!.... He noticed!{/i}"
                    "{i}{b}\"Sidney's Affection +1\"{/b}{/i}"
                    "{i}{b}\"Sidney's Libido +2\"{/b}{/i}"
                    $ sidneyaffection += 1
                    $ sidneylibido += 2
                    $ renpy.pause ()
                "Yeah, suck it whore!":
                    ST "{i}Did he just call me a whore?{/i}"
                    ST "{i}And why the fuck did it make my pussy tingle when he did?{/i}"
                    "{i}\"Sidney's Submission +1\"{/i}"
                    "{i}{b}\"Sidney's Libido +2\"{/b}{/i}"
                    $ sidneysubmission += 1
                    $ sidneylibido += 2
                    $ renpy.pause ()
            R "Oh.... I'm going to cum!"
            $ renpy.pause ()
            menu:
                "Cum down her throat.":
                    stop sound
                    scene bg SidneyRun88
                    with fade
                    ST "{i}Oh, shit!  He grabbed my head again.  He's going to....{/i}"
                    play sound Ejaculate
                    scene bg SidneyRun89
                    with dissolve
                    with hpunch
                    ST "{i}Shit! He always cums bucketloads.... Just focus on swallowing, Sidney!{/i}"
                    $ renpy.pause ()
                    play sound Ejaculate
                    scene bg SidneyRun90
                    with dissolve
                    with vpunch
                    ST "{i}Fuck! It shot up my sinuses.... I can feel it dripping out my nose!{/i}"
                    $ renpy.pause ()
                    play sound WomanBreath
                    scene bg SidneyRun91
                    with dissolve
                    S "Damnit, [ryan]!"
                    S "I've told you not to do that without warning me!"
                    "{i}{b}\"Sidney's Anger +1\"{/b}{/i}"
                    $ sidneyanger += 1
                    S "Now I have to smell and taste your cum most of the day! It takes a long time for it to drain completely out of my sinuses!"
                    R "Sorry, Sid! I just got carried away."
                    S "Yeah, yeah, that's what you always say."
                    S "Come on. Let's get home."
                    stop sound
                    play music Honey
                    $ park_bj = True
                    if park_finger and park_hj and park_pussy_eat and park_bj:
                        $ park_full_menu = True
                    else:
                        pass
                    $ timeofdaycounter += 1
                    jump myroom
                "Cum all over her face.":
                    stop sound
                    R "Sidney! I'm about to cum!"
                    play sound Ejaculate
                    scene bg SidneyRun92
                    with fade
                    $ renpy.pause ()
                    play sound Ejaculate
                    scene bg SidneyRun93
                    with dissolve
                    $ renpy.pause ()
                    scene bg SidneyRun94
                    with dissolve
                    R "Oh God! Sidney, you're so good!"
                    S "Well, thank you!"
                    S "But don't you mean \"Megan, or Miss Stone, you're so good?\""
                    R "Oh, shit!  Yeah, I forgot again."
                    S "Damnit, [ryan]! You've got to start remembering! You can't think about your sister while she's sucking you off! It'll make things too weird."
                    ST "{i}Haha that's right, bitches! He was thinking about me, not you. So, suck it!.... or.... Don't suck it.... I mean.{/i}"
                    R "Sorry. I'll try to remember next time."
                    S "Alright well, pull up your pants and let's go home."
                    play music Honey
                    $ park_bj = True
                    if park_finger and park_hj and park_pussy_eat and park_bj:
                        $ park_full_menu = True
                    else:
                        pass
                    $ timeofdaycounter += 1
                    jump myroom
        "Sex {i}(Bonus){/i}" if sidneylibido >= 8 and progress >= 16:
            jump park_sex
        "{s}Sex{/s} {i}(Sidney's Libido 8+){/i}" if sidneylibido <=7 and progress >= 16:
            jump park_menu

############# CLUB ######################################### CLUB ################################################################ CLUB ################################################## CLUB ################################################################## CLUB ###################################################################### CLUB ########################

label club_tip_bj:
    scene SidClubVideo04
    with dissolve
    $ club_tip = True
    $ renpy.pause ()
    menu:
        "Deeper":
            jump club_deeper_bj
        "Throat Fuck":
            jump club_throat_bj
        "Finish" if club_tip and club_deeper and club_throat and more_club_bjs == False:
            jump first_club_cum
        "Finish" if more_club_bjs:
            jump club_cum

label club_deeper_bj:
    scene SidClubVideo05
    with dissolve
    $ club_deeper = True
    $ renpy.pause ()
    menu:
        "Just the tip":
            jump club_tip_bj
        "Throat Fuck":
            jump club_throat_bj
        "Finish" if club_tip and club_deeper and club_throat and more_club_bjs == False:
            jump first_club_cum
        "Finish" if more_club_bjs:
            jump club_cum

label club_throat_bj:
    scene SidClubVideo06
    with dissolve
    $ club_throat = True
    $ renpy.pause ()
    menu:
        "Just the tip":
            jump club_tip_bj
        "Deep":
            jump club_deeper_bj
        "Finish" if club_tip and club_deeper and club_throat and more_club_bjs == False:
            jump first_club_cum
        "Finish" if more_club_bjs:
            jump club_cum

label first_club_cum:
    R "Oh my God!.... Sidney, I'm about to cum!"
    stop sound
    $ renpy.pause ()
    R "Hhhnnnnggghhhh...."
    play sound Ejaculate
    scene bg SidClub37
    with dissolve
    S "Mmmmpphhhhh......"
    play sound Gulp
    scene bg SidClub38
    with dissolve
    $ renpy.pause ()
    play sound Ejaculate
    scene bg SidClub37
    with dissolve
    $ renpy.pause ()
    play sound Gulp
    scene bg SidClub38
    with dissolve
    $ renpy.pause ()
    scene bg SidClub39
    with dissolve
    $ renpy.pause ()
    scene bg SidClub40
    with dissolve
    $ renpy.pause ()
    play sound Gulp
    scene bg SidClub41
    with dissolve
    S "I did it!"
    S "I was able to swallow all of it without it blasting into my sinuses!"
    S "Ha.... I'm getting better."
    R "I'll say.... That was incredible!"
    S "Oh.... That's so sweet!"
    S "There's not any on my face is there?"
    R "No, you got it all."
    R "Oh.... I almost forgot to ask you."
    S "Yeah?"
    R "Why the hell are you dressed like one of the waitresses?"
    scene bg SidClub43
    with dissolve
    S "Well.... You're probably not going to like this.... but Joey just offered me a job as a waitress, and I was trying it out for the first time."
    R "You're right, I don't like it."
    S "Well, the main reason I would do it, is to help out with our weekly payment to the Mafia."
    scene bg SidClub42
    with dissolve
    S "So, except for Mondays, when I'm required to be here, I'll only work on the days you ask me to."
    S "You can just tell me each day in the evenings when I'm in the kitchen."
    S "Oh.... And Joey said I can't work Saturdays because Mom might be here."
    R "Aaahhh.... I don't think it's a good idea...."
    scene bg SidClub43
    with dissolve
    S "Well, since you aren't the boss of me, I'm going to do it anyways."
    S "I'm going to save most of the money I make, so I can go back to my fashion design college."
    R "Sidney! It's the fucking Mafia!"
    S "Yeah! One of our only options for income that we can hide from the FBI."
    S "And I promise I'll be careful."
    if first_xmas_ntr == True and second_xmas_ntr == True:
        RT "{i}Shit!.... maybe that dream I had was more than a dream.  This seems like this could be the start of it all. I sure don't want that kind of future for her.  I need her to be super careful.{/i}"
    else:
        pass
    R "There's no being careful with the Mafia!"
    R "Once they're in your life, there's no getting them out."
    S "Yeah well Dad already put them in our lives, so now we just need to survive."
    S "And my God!.... Don't be so paranoid.  I'm only serving drinks."
    R "I'm sorry! I just really care about you."
    S "Thanks [ryan], but I'm not sure what you mean.  After the things we've been doing lately, I don't know if you care about me like a sister, or more like a girlfriend."
    menu:
        "Like a sister.":
            scene bg SidClub42
            with dissolve
            S "Oh, thank God! I was worried you were wanting more out of our relationship than siblings should ever have."
            RT "{i}She says right after she deepthroats my cock.{/i}"
            "{i}{b}\"Sidney's Respect +3\"{/b}{/i}"
            $ sidneyrespect += 3
        "Like a girlfriend.":
            if sidneyaffection >= 3:
                S "Oh no [ryan]! I was worried you were going to say that."
                R "Why? Who cares?"
                S "Everyone says it's wrong, and that's just the problem."
                R "What?"
                S "Because I'm starting to feel the same way as you."
                R "Really?"
                scene bg SidClub42
                with dissolve
                S "Yes.... But I'm not sure if that's a good thing or not.  I really just need some time to think about it some more."
                "{i}{b}\"Sidney's Affection +8\"{/b}{/i}"
                $ sidneyaffection += 8
            else:
                S "Shit [ryan]!  I just got done talking about how we need to be more careful about doing sexual stuff."
                S "It can only be for fun!"
                S "We are fucking siblings! We can't fall in love in the other way too!"
                R "Why not?"
                S "Because it's fucking wrong!"
                "{i}{b}\"Sidney's Anger +5\"{/b}{/i}"
    S "Alright, Mom's going to be done stripping in a few minutes.  We'd better get out of here before she sees either of us."
    S "Don't forget to come talk to me if you decide you need my help to pay the weekly Mafia bill.  You're pretty safe to look for me in the kitchen every evening. I'm usually there."
    R "I don't like it. But I can't control you. Just be sure to be careful."
    S "I promise I will. See you at home."
    R "Do you need a ride?"
    S "No, I brought Mom's car."
    R "Well, shit!  You'll beat me home then."
    $ sidney_took_job = True
    play music Honey
    jump citymap

label sid_working_club:
    if visited_sid:
        scene bg ImageMapCasinoWSidney
        RT "{i}I've already talked to her tonight... she might get in trouble if I don't let her keep working.{/i}"
        $ screen_on = "casinosidneymap"
        call screen casinosidneymap
    else:
        play music ClubMusic
        scene bg SleepBlack
        with fade
        scene bg WalkingCasino
        with fade
        RT "{i}I've got to keep my eye out for Sidney. If I don't see her, I'm sure I can just wait for her to turn up at the bar.{/i}"
        scene bg SidClub48
        with fade
        if daycounter == 1:
            $ sidney_money += 200
            $ monday_sid_worked = True
        else:
            pass
        $ more_club_bjs = True
        if first_bar_convo == False:
            A "If anybody else grabs your ass, remind them that we're only here to serve drinks and look hot. They're not allowed to touch."
            A "If that doesn't work, tell the bouncer, and he'll remind him with a black eye."
            S "Will I eventually get an apron too?"
            scene bg SidClub47
            with dissolve
            A "Well, the uniform doesn't actually come with the apron."
            S "Really?.... These pantyhose give me the worst cameltoe. Why do you get one?"
            A "My Uncle made me start wearing it shortly after I started serving drinks. I noticed he had a hard time not letting his eyes wander down there.  So I think he added it to my uniform to try to protect himself from temptation."
            A "It's actually kind of cute."
            scene bg SidClub48
            with dissolve
            A "My mom thinks I'm helping him with the book keeping each night.  Which is what I started out doing.  But I noticed that the waitresses made more money than I did, thanks to the tips."
            A "And being a server just looked like more fun, so I convinced him to let me try it, and now I'm learning to tend the bar as well."
            A "I wanted to give stripping a try too, but I think my Uncle Joey is too afraid of my mom, since she's his sister, and even more hot blooded than he is."
            A "So I don't think that's ever going to happen."
            A "Sorry, I started talking too much.... I tend to do that.  So, I think the answer you're looking for is no, your uniform doesn't get an apron."
            S "Oh.... Ok.... I guess it is what it is."
            scene bg SidClub49
            with fade
            RT "{i}There's Sidney. Wow!, and she's working with another extremely sexy waitress.{/i}"
            R "Hey Sidney!"
            R "I hope I'm not interrupting anything."
            S "Well, we are working."
            A "No it's ok, we're pretty slow right now."
            scene bg SidClub71
            with fade
            A "So who's this, Sidney?  Your boyfriend?"
            S "Yeah right, he wishes."
            S "Armani, this is my brother [ryan]."
            S "[ryan], this is Joey's niece, Armani."
            A "Brother huh?.... and do you really wish Sidney was your girlfriend?"
            menu:
                "Yes":
                    R "Sure, why not?"
                    "{i}{b}\"Sidney's Affection +1\"{/b}{/i}"
                    $ sidneyaffection += 1
                    R "It makes sense, we don't even have to move in together, since we already live with each other."
                    A "Haha.... I like your sense of humor!"
                    ST "{i}Don't flirt with my brother, you ho!{/i}"
                "No":
                    R "What?.... Psssshhhh.... Of course not!"
                    R "That would be so weird!"
                    A "It's not really that weird to me. In Italian culture, especially in the strong Mafia families, incest is actually fairly common."
                    ST "{i}We've got some italian blood in us.{/i}"
                    "{i}\"Sidney Libido +1\"{/i}"
                    $ sidneylibido += 1
            A "Anyways, it was nice to meet you [ryan]. I'll let you guys talk, I've got to run to the store room to grab some more vodka."
            R "Thanks Armani.... It was nice to meet you too!"
            scene bg SidClub50
            with dissolve
            S "So, what's up?"
            RT "{i}Holy shit! Those pantyhose are trying to get as far up Sidney's pussy as they can!{/i}"
            R "Uhhhh.... Not much.... I just wanted to come check on you on your first day of work."
            R "You know.... Make sure the Mafia hasn't sold you into prostitution yet."
            R "Glad to see they're keeping you safe by dressing you in puritan garb."
            scene bg SidClub51
            with dissolve
            S "Hahah.... How do you know they haven't."
            RT "{i}It's so hard to keep my eyes from wandering down there!{/i}"
            R "Uhhh.... Because if they had, there'd be a line out the door."
            scene bg SidClub50
            with dissolve
            ST "{i}Holy Fuck!.... I don't know if that was smooth or insulting.{/i}"
            if ntrcontent:
                ST "{i}Is [ryan] thinking about me getting fucked by other guys?{/i}"
            else:
                ST "{i}Is [ryan] imagining buying me to be his whore?{/i}"
            ST "{i}Shit!.... Now I am.{/i}"
            "{i}{b}\"Sidney's Libido +1\"{/b}{/i}"
            $ sidneylibido += 1
            RT "{i}Aaahhh!.... Should I just risk a peek?{/i}"
            menu:
                "Yes!.... Peek!":
                    scene bg SidClub70
                    with fade
                    RT "{i}Holy Fuck!  That leaves very little to the imagination.{/i}"
                    S "Huh Hemm...."
                    if sidneylibido >= 8:
                        scene bg SidClub51
                        with fade
                        S "See something you like down there?"
                        R "Ummmm.... I wasn't.... I mean...."
                        S "Hahaha.... Relax [ryan]."
                        S "I know these pantyhose are distracting.... Just ask any guy in the club."
                        "{i}{b}\"Sidney's Affection +1\"{/b}{/i}"
                        $ sidneyaffection += 1
                    else:
                        scene bg SidClub52
                        with fade
                        S "See something you like down there?"
                        R "Ummmm.... I wasn't.... I mean...."
                        S "It's bad enough that I have to have a club full of guys staring at me the whole time I'm here,"
                        S "But for you to come treat me the same way? Just stare at me like I'm something on the menu?"
                        R "I'm sorry!"
                        S "You should be!"
                        "{i}{b}\"Sidney's Anger +1\"{/b}{/i}"
                        $ sidneyanger += 1
                "No!.... Don't risk it.":
                    scene bg SidClub51
                    with dissolve
                    ST "{i}Look at him trying so hard not to take a peek at my cameltoe.{/i}"
                    ST "{i}I know he's dying to see it, but he's being so respectful to control his temptations.{/i}"
                    "{i}{b}\"Sidney's Respect +1\"{/b}{/i}"
                    $ sidneyrespect += 1
            scene bg SidClub50
            with dissolve
            $ visited_sid = True
            $ sidney_money += 200
            S "So, was there something you wanted to talk to me about?"
#            $ visited_sid = True
            $ first_bar_convo = True
            menu:
                "Working for the Mafia":
                    jump mafia_chat
                "Are you making good money?":
                    jump money_chat
                "Can we?.... You know....":
                    jump club_fun
        if progress >= 16 and not after_bondage_chat:
            jump post_bondage_chat
        else:
            A "And that's just another example of why getting involved with my Uncle's \"soldatos\" is a bad idea!"
            S "Holy shit!.... You're such a slut!"
            A "Hahaha.... I know!"
            R "Hello again, ladies."
            scene bg SidClub49
            with fade
            A "Oh Hey [ryan]!"
            A "I was just sharing more secrets about the Mafia with Sidney."
            A "Wasn't I?"
            scene bg SidClub50
            with fade
            S "More like secrets about sleeping with the Mafia."
            A "Hey!.... Haha.... See if I tell you anything ever again!"
            A "Haha.... Like I can even help it."
            A "Anyways, I've got to run and fill out an order form for the booze we're getting short on."
            A "Sidney, watch the bar for me while I'm gone."
            S "You got it!"
            $ visited_sid = True
#            $ sidney_money += 200
            S "So, was there something you wanted to talk to me about?"
#            $ visited_sid = True
            menu:
                "Working for the Mafia":
                    jump mafia_chat
                "Are you making good money?":
                    jump money_chat
                "Can we?.... You know....":
                    jump club_fun

label mafia_chat:
    scene bg SidClub50
    with dissolve
    if first_mafia_chat == False:
        R "So, I can see that you're bound and determined to keep working for the Mafia, so I had an idea."
        R "I figure that as long as you're going to be here anyways, maybe you can do some spying for us."
        scene bg SidClub52
        with dissolve
        S "Are you fucking serious?  I thought you said you wanted me to be safe!  How will spying on the Mafia keep me safe?"
        R "No.... I don't mean to sneak around and risk getting caught hiding under the desk in Joey's office or anything."
        R "I just mean that if in the course of your job, you happen to overhear a couple guys talking, or hear a chatty guy blabbing information he shouldn't to some stripper in the VIP room."
        R "You may not even know it's important at the time, but try to remember it.  Something that could seem unimportant, might be the key to getting us out of trouble with the Mafia."
        scene bg SidClub50
        with dissolve
        S "Ok, I think I can do that."
        R "I'll come by from time to time when you're working to see if you've learned anything."
        R "It would also be really helpful if you got close to somebody here at the club."
        scene bg SidClub52
        with dissolve
        S "Once again, you said you don't want me to get involved with the Mafia, and now you're asking me to befriend one of them?"
        R "Well, since you didn't take my advice, maybe we can benefit from your stubbornness."
        S "Well, who are you thinking I should get close to?"
        scene bg SidClub50
        with dissolve
        $ first_mafia_chat = True
        menu:
            "Joey (NTR Warning)":
                R "Well, who better than the big cheese himself?"
                S "How would I get close to a Mafia boss?"
                R "I don't know!  You'll just have to try to get to know him, and figure out what his interests are."
                R "I'll leave most of that up to you."
                $ chose_joey = True
            "Armani":
                R "You and Armani seem to be hitting it off already."
                S "I mean yeah, she seems nice and all."
                S "And she does have a tendency to run her mouth nonstop."
                R "Well, that's perfect then!"
                S "Alright.... I'll see what I can learn."
                $ chose_armani = True
        S "Was there something else you wanted?"
        menu:
            "Are you making good money?":
                jump money_chat
            "Can we?.... You know....":
                jump club_fun
            "That's all for tonight." if first_money_chat and first_club_fun:
                scene bg ImageMapCasinoWSidney
                with fade
                $ screen_on = "casinosidneymap"
                call screen casinosidneymap
    else:
        if chose_joey:
            R "So, have you been able to learn anything from Joey?"
        else:
            R "So, have you been able to learn anything from Armani?"
        S "Not yet.  I'm going to need some more time."
        "{i}\"This storyline will be continued in future updates.\"{/i}"
        S "Was there something else you wanted?"
        menu:
            "Are you making good money?":
                jump money_chat
            "Can we?.... You know....":
                jump club_fun
            "That's all for tonight." if first_money_chat and first_club_fun:
                scene bg ImageMapCasinoWSidney
                with fade
                $ screen_on = "casinosidneymap"
                call screen casinosidneymap
label money_chat:
    scene bg SidClub50
    with dissolve
    if first_money_chat == False:
        R "So, I know you're trying to save up enough money to go back to fashion design school, is this job paying you well enough so that you can go back soon?"
        S "Well, it's better than nothing, but fashion school is really expensive, but this is probably the best money I can make without the FBI finding out about it."
        RT "{i}Well.... I can guarantee that at least one person at the FBI will know about it.... Fuck.... Agent Diaz will have leverage over Sidney now too.  Hopefully she's only into redheads.{/i}"
        S "I want to keep the money for college, but it will also be a good emergency fund, just in case our family gets into some trouble."
        R "Well, once our family photo business is making better money, I'll start contributing to your savings fund as well."
        R "How much have you saved up so far?"
        S "Well, tonight is my first night, so whatever I make tonight will be what I have in my savings fund.  You'll have to ask me another time, when I've actually made some money."
        S "Was there something else you wanted?"
        $ first_money_chat = True
        menu:
            "Working for the Mafia.":
                jump mafia_chat
            "Can we?.... you know....":
                jump club_fun
            "That's all for tonight." if first_mafia_chat and first_club_fun:
                scene bg ImageMapCasinoWSidney
                with fade
                $ screen_on = "casinosidneymap"
                call screen casinosidneymap
    else:
        R "So, how much money have you been able to save up?"
        S "Well, with tonight's earnings, my college-slash-emergency fund should be about $[sidney_money]"
        R "That's a good start.  I hope I can start contributing to your college fund soon as well."
        scene bg SidClub51
        with dissolve
        S "that would be awesome!"
        S "...."
        S "Was there something else you wanted?"
        menu:
            "Working for the Mafia.":
                jump mafia_chat
            "Can we?.... you know....":
                jump club_fun
            "That's all for tonight." if first_mafia_chat and first_club_fun:
                scene bg ImageMapCasinoWSidney
                with fade
                $ screen_on = "casinosidneymap"
                call screen casinosidneymap

label club_fun:
    scene bg SidClub50
    with dissolve
    R "There's just something about being in a strip club that makes me...."
    S "Extra horny?.... Well, no shit Sherlock."
    R "So.... I was wondering if there was something we could do about it?"
    $ first_club_fun = True
    if sidneylibido >= 7 and club_fun_counter == 0:
        menu:
            "Blowjob":
                S "Yeah.... I guess so...."
                S "We are kind of slow."
                S "Let's go to the usual spot."
                R "Maybe we should start going somewhere more private.... You know with less chance of getting caught."
                S "Where's the fun in that?"
                S "Let's go to the usual spot, or not go at all."
                RT "{i}I can't believe what an exhibitionist Sidney is becoming.{/i}"
                R "Ok.... let's go."
                scene bg SleepBlack
                with fade
                scene bg SidClub36
                with fade
                ST "{i}Oh.... I love this cock!{/i}"
                scene SidClubVideo04
                with dissolve
                play sound Blow02 loop
                $ renpy.pause ()
                scene bg SidClub46
                with fade
                ST "{i}Oh.... I love watching the strip show while I'm giving my brother a blowjob!{/i}"
                "{i}{b}\"Sidney's Libido +1\"{/b}{/i}"
                $ sidneylibido += 1
                $ renpy.pause ()
                play sound Blow03 loop
                scene SidClubVideo04
                with dissolve
                $ renpy.pause ()
                $ club_fun_counter = 1
                jump club_tip_bj
            "Sex" if fucked_sid:
                jump club_sex
    if sidneylibido <= 6 and club_fun_counter == 0:
        S "Yeah, that's a big no for me."
        R "Really?.... Why?...."
        S "I'm just not feeling it tonight."
        "{i}\"Sidney's libido must be at least 7+ to have fun with Sidney.\"{/i}"
        R "Fine.... I'm already here anyways.... I might as well go watch the stripshow."
        scene bg SleepBlack
        with fade
        scene bg SidClub53
        with fade
        if first_diaz_convo == False:
            AD "Well, There's a face I recognize."
            scene bg SidClub54
            with fade
            R "Oh!.... Holy shit!  Agent Diaz?"
            R "Sorry I didn't notice you sitting there, my attention was focused elsewhere."
            scene bg SidClub55
            with dissolve
            AD "Haha.... I'm sure it was."
            AD "So, you decided to come watch a stripshow from somewhere else besides behind the corner?"
            R "How did you know?...."
            AD "I know the cleaning lady pretty well, and she's no fan of yours, and everyone here just assumes it was you, and now you just confirmed it."
            R "Shit!...."
            scene bg SidClub54
            with dissolve
            AD "Hahaha.... Don't worry about it!  This is a strip club, they see all kinds of weird shit."
            R "I'm really surprised to see you here with your badge on display."
            scene bg SidClub55
            with dissolve
            AD "Ahh.... Everybody knows me here.  There's no sense in trying to hide anything."
            R "What about the FBI?"
            AD "They just assume I'm working an informant."
            AD "And the DeCapos give me some small time criminals from outside the family from time to time."
            AD "Then I just tell the FBI they are part of the DeCapo family, and they are pleased as can be."
            AD "The DeCapos further their interests, and I get promoted."
            R "Do you mean small time criminals like my dad?"
            AD "Exactly.... Only we weren't responsible for that one.  We wouldn't purposefully incarcerate your dad.  He knows too much about the DeCapos."
            AD "And if he wants to stay alive, he'll keep his mouth shut.  But he already knows that."
            RT "{i}Diaz sure is brazenly unashamed about her relationship with the DeCapos, maybe I could record a conversation with her where she reveals something more incriminating.{/i}"
            AD "So, are you excited for my next visit on Thursday?"
            if first_diaz_dance == False:
                AD "Maybe if you stop paying me, and let me get a better shot at Lauren, I'll start involving you in her punishments."
                R "I don't care what I have to do to get the money by Thursday every week!  There is no way you'll get a shot at Lauren!"
                scene bg SidClub56
                with dissolve
                R "And I'm going to find a way to get you off our back if it's the last thing I do."
            else:
                AD "I'd think you'd have all kinds of money since you're not using it to save your sister. Thanks for giving me a shot at her though."
                R "I've only ever let you have a shot at Lauren because I didn't have the money, or I needed it elsewhere!"
                R "I swear I'm going to find a way to get you off our back if it's the last thing I do."
            AD "Well, good luck with that!  Much better men and women than you have tried."
            R "Well, Fuck you very much too, and now I'd like to watch the show."
            $ first_diaz_convo = True
        else:
            AD "Back again I see."
            scene bg SidClub54
            with fade
            R "Ahhh.... Agent Diaz.... I thought I smelled brimstone!"
            scene bg SidClub56
            with dissolve
            AD "Nice to see you too. How's Lauren?  Is she asking about me?"
            R "Well, Fuck you very much too, and now I'd like to watch the show."
        scene SidClubVideo07
        with fade
        $ renpy.pause ()
        ST "{i}Don't get jealous, don't get jealous, don't get jealous{/i}"
        scene bg SleepBlack
        with fade
        scene bg SidClub52
        with fade
        S "Well, I hope you enjoyed the show!"
        R "What?.... Are you mad I watched another girl strip?"
        S "What?.... That's ridiculous!.... Of course not!"
        scene bg SidClub50
        with dissolve
        $ watched_with_Diaz = True
        S "So, was there anything else you wanted to talk to me about?"
        menu:
            "Working for the Mafia.":
                jump mafia_chat
            "Are you making good money?":
                jump money_chat
            "That's all for tonight." if first_mafia_chat and first_money_chat:
                scene bg ImageMapCasinoWSidney
                with fade
                $ screen_on = "casinosidneymap"
                call screen casinosidneymap
    if watched_with_Diaz:
        scene bg SidClub52
        with dissolve
        S "What?.... No!.... I've already told you no!"
        S "And you've already watched a strip dance."
        S "Is there anything else you want, because if not, maybe you should head home."
        scene bg SidClub50
        with dissolve
        menu:
            "Working for the Mafia.":
                jump mafia_chat
            "Are you making good money?":
                jump money_chat
            "That's all for tonight." if first_mafia_chat and first_money_chat:
                scene bg ImageMapCasinoWSidney
                with fade
                $ screen_on = "casinosidneymap"
                call screen casinosidneymap
    if club_fun_counter == 1:
        scene bg SidClub52
        with dissolve
        S "What?.... No!.... We've already screwed around enough tonight!"
        S "Is there anything else you want, because if not, maybe you should head home."
        scene bg SidClub50
        with dissolve
        menu:
            "Working for the Mafia.":
                jump mafia_chat
            "Are you making good money?":
                jump money_chat
            "That's all for tonight." if first_mafia_chat and first_money_chat:
                scene bg ImageMapCasinoWSidney
                with fade
                $ screen_on = "casinosidneymap"
                call screen casinosidneymap
    if club_fun_counter == 2:
        S "Why so greedy?."
        S "We screwed around just last night."
        S "Try me again tomorrow, and maybe I'll be in the mood."
        R "Fine.... I'm already here anyways.... I might as well go watch the stripshow."
        scene bg SleepBlack
        with fade
        scene bg SidClub53
        with fade
        if first_diaz_convo == False:
            AD "Well, There's a face I recognize."
            scene bg SidClub54
            with fade
            R "Oh!.... Holy shit!  Agent Diaz?"
            R "Sorry I didn't notice you sitting there, my attention was focused elsewhere."
            scene bg SidClub55
            with dissolve
            AD "Haha.... I'm sure it was."
            AD "So, you decided to come watch a stripshow from somewhere else besides behind the corner?"
            R "How did you know?...."
            AD "I know the cleaning lady pretty well, and she's no fan of yours, and everyone here just assumes it was you, and now you just confirmed it."
            R "Shit!...."
            scene bg SidClub54
            with dissolve
            AD "Hahaha.... Don't worry about it!  This is a strip club, they see all kinds of weird shit."
            R "I'm really surprised to see you here with badge on display."
            scene bg SidClub55
            with dissolve
            AD "Ahh.... Everybody knows me here.  There's no sense in trying to hide anything."
            R "What about the FBI?"
            AD "They just assume I'm working an informant."
            AD "And the DeCapos give me some small time criminals from outside the family from time to time."
            AD "Then I just tell the FBI they are part of the DeCapo family, and they are pleased as can be."
            AD "The DeCapos further their interests, and I get promoted."
            R "Do you mean small time criminals like my dad?"
            AD "Exactly.... Only we weren't responsible for that one.  We wouldn't purposefully incarcerate your dad.  He knows too much about the DeCapos."
            AD "And if he wants to stay alive, he'll keep his mouth shut.  But he already knows that."
            RT "{i}Diaz sure is brazenly unashamed about her relationship with the DeCapos, maybe I could record a conversation with her where she reveals something more incriminating.{/i}"
            AD "So, are you excited for my next visit on Thursday?"
            AD "Maybe if you stop paying me, and let me get a better shot at Lauren, I'll start involving you in her punishments."
            if first_diaz_dance == False:
                R "I don't care what I have to do to get the money by Thursday every week!  There is no way you'll get a shot at Lauren!"
                scene bg SidClub56
                with dissolve
                R "And I'm going to find a way to get you off our back if it's the last thing I do."
            else:
                R "I've only ever let you have a shot at Lauren because I didn't have the money, or I needed it elsewhere!"
                R "I swear I'm going to find a way to get you off our back if it's the last thing I do."
            AD "Well, good luck with that!  Much better men and women than you have tried."
            R "Well, Fuck you very much too, and now I'd like to watch the show."
            $ first_diaz_convo = True
        else:
            AD "Back again I see."
            scene bg SidClub54
            with fade
            R "Ahhh.... Agent Diaz.... I thought I smelled sulfur!"
            scene bg SidClub56
            with dissolve
            AD "Nice to see you too. How's Lauren?  Is she asking about me?"
            R "Well, Fuck you very much too, and now I'd like to watch the show."
        scene SidClubVideo07
        with fade
        $ renpy.pause ()
        ST "{i}Don't get jealous, don't get jealous, don't get jealous{/i}"
        scene bg SleepBlack
        with fade
        scene bg SidClub52
        with fade
        S "Well, I hope you enjoyed the show!"
        R "What?.... Are you mad I watched another girl strip?"
        S "What?.... That's ridiculous!.... Of course not!"
        scene bg SidClub50
        with dissolve
        $ watched_with_Diaz = True
        S "So, was there anything else you wanted to talk to me about?"
        menu:
            "Working for the Mafia.":
                jump mafia_chat
            "Are you making good money?":
                jump money_chat
            "That's all for tonight." if first_mafia_chat and first_money_chat:
                scene bg ImageMapCasinoWSidney
                with fade
                $ screen_on = "casinosidneymap"
                call screen casinosidneymap
    if watched_with_Diaz:
        scene bg SidClub52
        with dissolve
        S "What?.... No!.... I've already told you no!"
        S "And you've already watched a strip dance."
        S "Is there anything else you want, because if not, maybe you should head home."
        scene bg SidClub50
        with dissolve
        menu:
            "Working for the Mafia.":
                jump mafia_chat
            "Are you making good money?":
                jump money_chat
            "That's all for tonight." if first_mafia_chat and first_money_chat:
                scene bg ImageMapCasinoWSidney
                with fade
                $ screen_on = "casinosidneymap"
                call screen casinosidneymap

label club_cum:
    R "Oh my God!.... Sidney, I'm about to cum!"
    stop sound
    $ renpy.pause ()
    R "Hhhnnnnggghhhh...."
    play sound Ejaculate
    scene bg SidClub37
    with dissolve
    S "Mmmmpphhhhh......"
    play sound Gulp
    scene bg SidClub38
    with dissolve
    $ renpy.pause ()
    play sound Ejaculate
    scene bg SidClub37
    with dissolve
    $ renpy.pause ()
    play sound Gulp
    scene bg SidClub38
    with dissolve
    $ renpy.pause ()
    scene bg SidClub39
    with dissolve
    $ renpy.pause ()
    scene bg SidClub40
    with dissolve
    $ renpy.pause ()
    play sound Gulp
    scene bg SidClub41
    with dissolve
    S "I did it again!"
    S "I was able to swallow all of it without it blasting into my sinuses!"
    S "Ha.... I'm getting better and better."
    R "I'll say.... That was incredible!"
    S "Haha.... I think you say that every time you cum!"
    S "There's not any on my face is there?"
    R "No, you got it all."
    S "Good!  I don't want to mess up my makeup!"
    S "Now I've got to get back to the bar before anyone notices I'm missing."
    scene bg SleepBlack
    with fade
    scene bg SidClub50
    with fade
    S "So, was there anything else you wanted to talk to me about?"
    menu:
        "Working for the Mafia.":
            jump mafia_chat
        "Are you making good money?":
            jump money_chat
        "That's all for tonight." if first_mafia_chat and first_money_chat:
            scene bg ImageMapCasinoWSidney
            with fade
            $ screen_on = "casinosidneymap"
            call screen casinosidneymap
