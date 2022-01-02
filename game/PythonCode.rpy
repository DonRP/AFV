init python:
        def limit_stats():
            try:
                if store.money <0:
                    store.money = 0
                if store.momaffection > 75:
                    store.momaffection = 75
                if store.momaffection < 0:
                    store.momaffection = 0
                if store.laurenaffection > 75:
                    store.laurenaffection = 75
                if store.laurenaffection < 0:
                    store.laurenaffection = 0
                if store.sidneyaffection > 75:
                    store.sidneyaffection = 75
                if store.sidneyaffection < 0:
                    store.sidneyaffection = 0
                if store.auntaffection > 50:
                    store.auntaffection = 50
                if store.auntaffection < 0:
                    store.auntaffection = 0
                if store.cousinaffection > 75:
                    store.cousinaffection = 75
                if store.cousinaffection < 0:
                    store.cousinaffection = 0
                if store.momsubmission > 100:
                    store.momsubmission = 100
                if store.momsubmission < 0:
                    store.momsubmission = 0
                if store.laurensubmission > 100:
                    store.laurensubmission = 100
                if store.laurensubmission < 0:
                    store.laurensubmission = 0
                if store.sidneysubmission > 100:
                    store.sidneysubmission = 100
                if store.sidneysubmission < 0:
                    store.sidneysubmission = 0
                if store.auntsubmission > 100:
                    store.auntsubmission = 100
                if store.auntsubmission < 0:
                    store.auntsubmission = 0
                if store.cousinsubmission > 100:
                    store.cousinsubmission = 100
                if store.cousinsubmission < 0:
                    store.cousinsubmission = 0
                if store.momlibido > 10:
                    store.momlibido = 10
                if store.momlibido < 0:
                    store.momlibido = 0
                if store.laurenlibido > 10:
                    store.laurenlibido = 10
                if store.laurenlibido < 0:
                    store.laurenlibido = 0
                if store.sidneylibido > 10:
                    store.sidneylibido = 10
                if store.sidneylibido < 0:
                    store.sidneylibido = 0
                if store.auntlibido > 10:
                    store.auntlibido = 10
                if store.auntlibido < 0:
                    store.auntlibido = 0
                if store.cousinlibido > 10:
                    store.cousinlibido = 10
                if store.cousinlibido < 0:
                    store.cousinlibido = 0
                if store.momrespect > 10:
                    store.momrespect = 10
                if store.momrespect < 0:
                    store.momrespect = 0
                if store.laurenrespect > 10:
                    store.laurenrespect = 10
                if store.laurenrespect < 0:
                    store.laurenrespect = 0
                if store.sidneyrespect > 10:
                    store.sidneyrespect = 10
                if store.sidneyrespect < 0:
                    store.sidneyrespect = 0
                if store.auntrespect > 10:
                    store.auntrespect = 10
                if store.auntrespect < 0:
                    store.auntrespect = 0
                if store.cousinrespect > 10:
                    store.cousinrespect = 10
                if store.cousinrespect < 0:
                    store.cousinrespect = 0
                if store.momanger > 10:
                    store.momanger = 10
                if store.momanger < 0:
                    store.momanger = 0
                if store.laurenanger > 10:
                    store.laurenanger = 10
                if store.laurenanger < 0:
                    store.laurenanger = 0
                if store.sidneyanger > 10:
                    store.sidneyanger = 10
                if store.sidneyanger < 0:
                    store.sidneyanger = 0
                if store.auntanger > 10:
                    store.auntanger = 10
                if store.auntanger < 0:
                    store.auntanger = 0
                if store.cousinanger > 10:
                    store.cousinanger = 10
                if store.cousinanger < 0:
                    store.cousinanger = 0
                if store.timeofdaycounter >5:
                    store.timeofdaycounter = 5
                if store.cosplayoutfitcounter >3:
                    store.cosplayoutfitcounter = 3
                if store.picsarepostedcounter >1:
                    store.picsarepostedcounter = 1
                if store.familyofsquirters >4:
                    store.familyofsquirters = 4
                if store.shampoobottle >3:
                    store.shampoobottle = 3
                if store.clubcounter >5:
                    store.clubcounter = 5
                if store.loyaltycounter >3:
                    store.loyaltycounter = 3
                if store.aunt_visit_counter >10:
                    store.aunt_visit_counter = 10
            except:
                pass
        config.python_callbacks.append(limit_stats)

define persistent.patreonsafe = True
