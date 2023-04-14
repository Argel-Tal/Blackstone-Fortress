import random
'''
valid method calls:

print(Enemy())
print(specialActions())

'''


''' 
produces an RNG result for any unit type
based on user input
'''
def Enemy():
    print('Enemy Types:\n\nUrGhul\t \t \t1\nSpindleDrone\t\t2\nTraitorGuardsman\t3\nRoguePsyker\t\t4\nNegavoltCultist\t\t5\nChaosBeastman\t\t6\nChaosSpaceMarine\t7\nObsidiusMallex\t\t8\n')
    InstanceEnemy=input("Enter the Enemy Type: ")
    InstanceEnemy = str(InstanceEnemy)
    #Type is Ur-Ghul
    if InstanceEnemy=='1':
        print('Ur-Ghul')
    #generate dice roll
        roll=random.randint(1,20)
        status=input("Enter the status: \n\t\n\tHidden\t= 1,\n\tEngaged\t= 2,\n\tClose\t= 3,\n\tOther *\t")
        print("roll\t= "+str(roll))
    #conditionals
        if status == '1':
            print('Status\t= Hidden')
            if roll<=3:
                return("Hold")
            elif roll <9:
                return("Sneak")
            elif roll <19:
                return("Charge")
            else:
                return("Rush")
    
        elif status == '2':
            print('Status\t= Engaged')
            if roll<=6:
                return("Fall Back")
            elif roll<=19:
                return("Onslaught")
            else:
                return("Pounce")
            
        elif status == '3':
            print('Status\t= Close')
            if roll<=6:
                return("Fall Back")
            elif roll<=19:
                return("Charge")
            else:
                return("Pounce")
            
        else:
            print('Status\t= Other')
            if roll<=9:
                return("Fall Back")
            else:
                return("Rush")

    #Type is Spindle Drone
    elif InstanceEnemy=='2':
        print('Spindle Drone')
        #generate dice roll
        roll=random.randint(1,20)
        status=input("Enter the status: \n\tHidden = 1,\n\tEngaged = 2,\n\tIn Cover = 3,\n\tClose = 4,\n\tOther *\t")
        print("roll\t= "+str(roll))
    #conditionals
        if status == '1':
            print('Status\t= Hidden')
            if roll<=3:
                return("Hold")
            elif roll <9:
                return("Sneak")
            elif roll <19:
                return("Advance")
            else:
                return("Alert")

        elif status == '2':
            print('Status\t= Engaged')
            if roll<=6:
                return("Fall Back")
            elif roll<=19:
                return("Onslaught")
            else:
                return("Alert")

        elif status == '3':
            print('Status\t= In Cover')
            if roll<=6:
                return("Aim")
            elif roll<=19:
                return("Onslaught")
            else:
                return("Alert")  

        elif status == '4':
            print('Status\t= Close')
            if roll<=3:
                return("Fall Back")
            elif roll<=9:
                return('Aim')
            elif roll<=19:
                return("Onslaught")
            else:
                return("Alert")

        else:
            print('Status\t= Other')
            if roll<=3:
                return("Fall Back")
            elif roll<=9:
                return('Aim')
            elif roll<=15:
                return("Onslaught")
            elif roll<=19:
                return("Advance")
            else:
                return("Alert")
    

    #Type is TraitorGuardsman
    elif InstanceEnemy=='3':
        print('Traitor Guardsman')
        #generate dice roll
        roll=random.randint(1,20)
        status=input("Enter the status: \n\tHidden = 1,\n\tEngaged = 2,\n\tIn Cover w/ Lasgun = 3,\n\tClose = 4,\n\tOther *\t")
        print("roll\t= "+str(roll))
    #conditionals
        if status == '1':
            print('Status\t= Hidden')
            if roll<=3:
                return("Hold")
            elif roll <6:
                return("Sneak")
            elif roll <12:
                return("Advance")
            elif roll <19:
                return("Charge")
            else:
                return("Rush")
    
        elif status == '2':
            print('Status\t= Engaged')
            if roll<=6:
                return("Fall Back")
            elif roll<=19:
                return("Onslaught")
            else:
                return("Fury")
            
        elif status == '3':
            print('Status\t= In Cover')
            if roll<=9:
                return("Aim")
            elif roll<=19:
                return("Onslaught")
            else:
                return("Fury")
            
        elif status == '4':
            print('Status\t= Close')
            if roll<=3:
                return("Fall Back")
            elif roll<=9:
                return('Onslaught')
            elif roll<=19:
                return("Charge")
            else:
                return("Fury")
            
        else:
            print('Status\t= Other')
            if roll<=6:
                return("Advance")
            elif roll<=12:
                return('Aim')
            elif roll<=19:
                return("Onslaught")
            else:
                return("Alert")
    
    #Type is Rogue Psyker
    elif InstanceEnemy=='4':
        print('Rogue Psyker')
        #generate dice roll
        roll=random.randint(1,20)
        status=input("Enter the status: \n\tHidden = 1,\n\tEngaged = 2,\n\tClose = 3,\n\tOther *\t")
        print("roll\t= "+str(roll))
    #conditionals
        if status == '1':
            print('Status\t= Hidden')
            if roll<=9:
                return("Hold")
            elif roll <15:
                return("Disrupt")
            elif roll <19:
                return("Regenerate")
            else:
                return("Empower")
    
        elif status == '2':
            print('Status\t= Engaged')
            if roll<=6:
                return("Fall Back")
            elif roll<=15:
                return("Onslaught")
            else:
                return("Annihilate")
            
        elif status == '3':
            print('Status\t= Close')
            if roll<=3:
                return("Fall Back")
            elif roll<=9:
                return('Disrupt')
            elif roll<=15:
                return("Onslaught")
            elif roll<=19:
                return("Regenerate")
            else:
                return("Empower")
            
        else:
            print('Status\t= Other')
            if roll<=3:
                return("Hold")
            elif roll<=9:
                return('Disrupt')
            elif roll<=15:
                return("Onslaught")
            elif roll<=19:
                return("Regenerate")
            else:
                return("Empower")

    #Type is Negavolt Cultist
    elif InstanceEnemy=='5':
        print('Negavolt Cultist')
        #generate dice roll
        roll=random.randint(1,20)
        status=input("Enter the status: \n\tHidden = 1,\n\tEngaged = 2,\n\tOther *\t")
        print("roll\t= "+str(roll))
    #conditionals
        if status == '1':
            print('Status\t= Hidden')
            if roll<=3:
                return("Recharge")
            elif roll<=6:
                return("Hold")
            elif roll <19:
                return("Charge")
            else:
                return("Rush")
    
        elif status == '2':
            print('Status\t= Engaged')
            if roll<=3:
                return("Recharge")
            elif roll <19:
                return("Onslaught")
            else:
                return("Fury")
            
        else:
            print('Status\t= Other')
            if roll<=3:
                return("Recharge")
            elif roll <19:
                return("Charge")
            else:
                return("Rush")       

    #Type is ChaosBeastman
    elif InstanceEnemy=='6':
        print('Chaos Beastman')
        #generate dice roll
        roll=random.randint(1,20)
        status=input("Enter the status: \n\tHidden = 1,\n\tEngaged = 2,\n\tClose = 3,\n\tOther *\t")
        print("roll\t= "+str(roll))
    #conditionals
        if status == '1':
            print('Status\t= Hidden')
            if roll<=3:
                return("Hold")
            elif roll <9:
                return("Advance")
            elif roll <19:
                return("Charge")
            else:
                return("Rush")
    
        elif status == '2':
            print('Status\t= Engaged')
            if roll<=15:
                return("Onslaught")
            else:
                return("Fury")
            
        elif status == '3':
            print('Status\t= Close')
            if roll<=9:
                return("Onslaught")
            elif roll<=19:
                return("Charge")
            else:
                return("Rush")
            
        else:
            print('Status\t= Other')
            if roll<=9:
                return("Advance")
            elif roll<=19:
                return("Charge")
            else:
                return("Rush")

	#Type is Chaos Space Marine
    elif InstanceEnemy=='7':
        print('Chaos Space Marine')
        #generate dice roll
        roll=random.randint(1,20)
        status=input("Enter the status: \n\tHidden = 1,\n\tEngaged = 2,\n\tIn Cover = 3,\n\tClose = 4,\n\tOther *\t")
        print("roll\t= "+str(roll))
    #conditionals
        if status == '1':
            print('Status\t= Hidden')
            if roll<=3:
                return("Sneak")
            elif roll <9:
                return("Advance")
            elif roll <19:
                return("Charge")
            else:
                return("Rush")
    
        elif status == '2':
            print('Status\t= Engaged')
            if roll<=15:
                return("Onslaught")
            else:
                return("Rapid Fire")
            
        elif status == '3':
            print('Status\t= In Cover')
            if roll<=3:
                return("Aim")
            elif roll<=12:
                return("Onslaught")
            elif roll<=15:
                return("Advance")
            else:
                return("Rapid Fire")

            
        elif status == '4':
            print('Status\t= Close')
            if roll<=6:
                return("Aim")
            elif roll<=12:
                return("Onslaught")
            elif roll<=15:
                return("Advance")
            else:
                return("Rapid Fire")
            
        else:
            print('Status\t= Other')
            if roll<=9:
                return('Aim')
            elif roll<=15:
                return("Advance")
            else:
                return("Rapid Fire")
    
    #Type is ObsidiusMallex
    elif InstanceEnemy=='8':
        print('Obsidius Mallex')
        #generate dice roll
        roll=random.randint(1,20)
        status=input("Enter the status: \n\tHidden = 1,\n\tEngaged = 2,\n\tIn Cover w/ Lasgun = 3,\n\tClose = 4,\n\tOther *\t")
        print("roll\t= "+str(roll))
    #conditionals
        if status == '1':
            print('Status\t= Hidden')
            if roll<=3:
                return("Sneak")
            elif roll <9:
                return("Advance")
            elif roll <12:
                return("Charge")
            else:
                return("Rush")
    
        elif status == '2':
            print('Status\t= Engaged')
            if roll<=12:
                return("Onslaught")
            else:
                return("Fury")
            
        elif status == '3':
            print('Status\t= In Cover')
            if roll<=6:
                return("Charge")
            elif roll<=19:
                return("Aim")
            elif roll<=15:
                return("Onslaught")
            elif roll<=19:
                return("Overcharge")
            else:
                return("Fury")
            
        elif status == '4':
            print('Status\t= Close')
            if roll<=6:
                return("Onslaught")
            elif roll<=15:
                return("Charge")
            else:
                return("Overcharge")
            
        else:
            print('Status\t= Other')
            if roll<=6:
                return("Advance")
            elif roll<=9:
                return('Aim')
            elif roll<=15:
                return("Onslaught")
            elif roll<=19:
                return("Overcharge")
            else:
                return("Rush")
    
    # Otheriwse exit
    else:
        return

'''
defines the behaviour output for unit
'''
def specialActions(result):
    list_actions = ["sneak", "hold", "fall back", "advance", 'aim', 'charge', 'onslaught', 
                        'alert', 'rush', 'overcharge', 'recharge', 'disrupt', 'regenerate', 
                        'empower', 'annihilate', 'rapid fire', 'fury', 'pounce'
                    ] # end action list
    # handle unmatched characters
    if result is None:
            action = ""
            return(action)
    else: 
        result = str.lower(result)
        while result in list_actions:
            result = str.lower(result)
            secondaryAction = ""
            # make whitespace
            print()
            print("Action\t= ", str.capitalize(result), "\n")
            #result = str.lower(input("Enter behaviour result here for a definition: "))
            if result=="sneak":
                action = ('Make a move that ends as close as possible to an explorer without entering a hex that is visible to any explorers')
                secondaryAction = ""
            elif result=="hold":
                action = ("Do nothing")
                secondaryAction = ""
            elif result=="fall back":
                action = ("Double this hostile's Move Value when they take this action. If this hostile can make a move that ends in a hex not visible to any explorers, they do so. If they cannot, they attack the closest explorer that is in range and visible to this hostile.")
                secondaryAction = ""
            elif result=="advance":
                action = ("Move towards the closest explorer. Then attack the closest explorer that is in range and visible to this hostile.")
                secondaryAction = ""
            elif result=="aim":
                action = ("Attack the furthest explorer that is in range and visible to this hostile. That attack ignores Cover.")
                secondaryAction = ""
            elif result=="charge":
                action = ("Move towards the closest explorer. Then attack an explorer that is adjacent and visible to this hostile. If there are no explorers adjacent and visible to this hostile, move towards the closest explorer a second time.")
                secondaryAction = ""
            elif result=="onslaught":
                action = ("Attack the closest explorer that is in range of and is visible to this hostile. Then attack the closest explorer that is in range and visible to this hostile (may be a different target)")
                secondaryAction = ""
            elif result=="alert":
                action = ("Increase the Threat Level by 1 and then take an Onslaught action. IF the Threat Level is 3, take an Onslaught action and reroll failed attack rolls for that action instead.")
                secondaryAction = "onslaught"
            elif result=="rush":
                action = ("Move towards the closest explorer. The take a Charge action")
                secondaryAction = "charge"
            elif result=="overcharge":
                action = ("Make an overcharged Plasma Pistol attack against thge closest explorer that is in range of and visible to Obsidius Mallex.")
                secondaryAction = ""
            elif result=="recharge":
                action = ("Remove a Wound counter from this Negavolt Cultist. If the Negavolt Cultist does not have a Wound counter, treat this as an Advance result instead.")
                secondaryAction = "advance"
            elif result=="disrupt":
                action = ("One unspent activation or Destiny dice chosen by the hostile player is discarded and cannot be spent this turn. If no unspent activation or Destiny dice are available, one explorer chosen by the hostile player suffers a wound.")
                secondaryAction = ""
            elif result=="regenerate":
                action = ("Remove a Wound counter from this Rogue Psyker. If the Rogue Psyker does not have a Wound counter, treat this as an Disrupt result instead.")
                secondaryAction = "disrupt"
            elif result=="empower":
                action = ("Place the Empower marker beside the Rogue Psyker. If the Rogue Psyker is already Empowered, treat this result as a Disrupt result instead. The Rogue Psyker remains Empowered until they suffer a Wound or Grevious Wound.")
                secondaryAction = "disrupt"
            elif result=="annihilate":
                action = ("Place the Empower marker beside the Rogue Psyker. Then attack an explorer that is adjacent and visible to this hostile. Reroll failed attack rolls for that attack. The Rogue Psyker remains Empowered until they suffer a Wound or Grevious Wound.")
                secondaryAction = ""
            elif result=="rapid fire":
                action = ("Take an Onslaught action. Reroll failed attack rolls for that action.")
                secondaryAction = "onslaught"
            elif result=="fury":
                action = ("Take an Onslaught action. Reroll all failed attack rolls for that action.")
                secondaryAction = "onslaught"
            elif result=="pounce":
                action = ("If there is an explorer adjacent and visible to this Ur-Ghul, take an Onslaught action. Otherwise take a Charge action. Reroll failed attack rolls for whichever action is taken.")
                secondaryAction = "onslaught"
            else:
                action = ""
            print(action)
            result = secondaryAction
        # end while
    return()

def mainMeth():
    inp = str(input("do you need help? y/n (1/0)\t"))
    while (inp == "y" or inp == "1"):
        if (inp == "y" or inp == "1"):
            specialActions(Enemy())
            print()
            inp = input("do you need help? y/n (1/0)\t")
        else:
            return
            
    

mainMeth()