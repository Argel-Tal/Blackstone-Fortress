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
    #Type is Ur-Ghul
    if InstanceEnemy=='1':
        print('Ur-Ghul')
    #generate dice roll
        roll=random.randint(1,20)
        status=input("Enter the status: Hidden = 1, Engaged = 2, Close = 3, Other *   ")
        print("roll = "+str(roll))
    #conditionals
        if status == '1':
            print('Hidden')
            if roll<=3:
                return("Hold\n")
            elif roll <9:
                return("Sneak\n")
            elif roll <19:
                return("Charge\n")
            else:
                return("Rush\n")
    
        elif status == '2':
            print('Engaged')
            if roll<=6:
                return("Fall Back\n")
            elif roll<=19:
                return("Onslaught\n")
            else:
                return("Pounce\n")
            
        elif status == '3':
            print('Close')
            if roll<=6:
                return("Fall Back\n")
            elif roll<=19:
                return("Charge\n")
            else:
                return("Pounce\n")
            
        else:
            print('Other')
            if roll<=9:
                return("Fall Back\n")
            else:
                return("Rush\n")

    #Type is Spindle Drone
    elif InstanceEnemy=='2':
        print('Spindle Drone')
        #generate dice roll
        roll=random.randint(1,20)
        status=input("Enter the status: Hidden = 1, Engaged = 2, In Cover = 3, Close = 4, Other *   ")
        print("roll = "+str(roll))
    #conditionals
        if status == '1':
            print('Hidden')
            if roll<=3:
                return("Hold\n")
            elif roll <9:
                return("Sneak\n")
            elif roll <19:
                return("Advance\n")
            else:
                return("Alert\n")

        elif status == '2':
            print('Engaged')
            if roll<=6:
                return("Fall Back\n")
            elif roll<=19:
                return("Onslaught\n")
            else:
                return("Alert\n")

        elif status == '3':
            print('In Cover')
            if roll<=6:
                return("Aim\n")
            elif roll<=19:
                return("Onslaught\n")
            else:
                return("Alert\n")  

        elif status == '4':
            print('Close')
            if roll<=3:
                return("Fall Back\n")
            elif roll<=9:
                return('Aim\n')
            elif roll<=19:
                return("Onslaught\n")
            else:
                return("Alert\n")

        else:
            print('Other')
            if roll<=3:
                return("Fall Back\n")
            elif roll<=9:
                return('Aim\n')
            elif roll<=15:
                return("Onslaught\n")
            elif roll<=19:
                return("Advance\n")
            else:
                return("Alert\n")
    

    #Type is TraitorGuardsman
    elif InstanceEnemy=='3':
        print('Traitor Guardsman')
        #generate dice roll
        roll=random.randint(1,20)
        status=input("Enter the status: Hidden = 1, Engaged = 2, In Cover w/ Lasgun = 3, Close = 4, Other *   ")
        print("roll = "+str(roll))
    #conditionals
        if status == '1':
            print('Hidden')
            if roll<=3:
                return("Hold\n")
            elif roll <6:
                return("Sneak\n")
            elif roll <12:
                return("Advance\n")
            elif roll <19:
                return("Charge\n")
            else:
                return("Rush")
    
        elif status == '2':
            print('Engaged')
            if roll<=6:
                return("Fall Back\n")
            elif roll<=19:
                return("Onslaught\n")
            else:
                return("Fury\n")
            
        elif status == '3':
            print('In Cover')
            if roll<=9:
                return("Aim\n")
            elif roll<=19:
                return("Onslaught\n")
            else:
                return("Fury\n")
            
        elif status == '4':
            print('Close')
            if roll<=3:
                return("Fall Back\n")
            elif roll<=9:
                return('Onslaught\n')
            elif roll<=19:
                return("Charge\n")
            else:
                return("Fury\n")
            
        else:
            print('Other')
            if roll<=6:
                return("Advance\n")
            elif roll<=12:
                return('Aim\n')
            elif roll<=19:
                return("Onslaught\n")
            else:
                return("Alert\n")
    
    #Type is Rogue Psyker
    elif InstanceEnemy=='4':
        print('Rogue Psyker')
        #generate dice roll
        roll=random.randint(1,20)
        status=input("Enter the status: Hidden = 1, Engaged = 2, Close = 3, Other *   ")
        print("roll = "+str(roll))
    #conditionals
        if status == '1':
            print('Hidden')
            if roll<=9:
                return("Hold\n")
            elif roll <15:
                return("Disrupt\n")
            elif roll <19:
                return("Regenerate\n")
            else:
                return("Empower\n")
    
        elif status == '2':
            print('Engaged')
            if roll<=6:
                return("Fall Back\n")
            elif roll<=15:
                return("Onslaught\n")
            else:
                return("Annihilate\n")
            
        elif status == '3':
            print('Close')
            if roll<=3:
                return("Fall Back\n")
            elif roll<=9:
                return('Disrupt\n')
            elif roll<=15:
                return("Onslaught\n")
            elif roll<=19:
                return("Regenerate\n")
            else:
                return("Empower\n")
            
        else:
            print('Other')
            if roll<=3:
                return("Hold\n")
            elif roll<=9:
                return('Disrupt\n')
            elif roll<=15:
                return("Onslaught\n")
            elif roll<=19:
                return("Regenerate\n")
            else:
                return("Empower\n")

    #Type is Negavolt Cultist
    elif InstanceEnemy=='5':
        print('Negavolt Cultist')
        #generate dice roll
        roll=random.randint(1,20)
        status=input("Enter the status: Hidden = 1, Engaged = 2, Other *   ")
        print("roll = "+str(roll))
    #conditionals
        if status == '1':
            print('Hidden')
            if roll<=3:
                return("Recharge\n")
            elif roll<=6:
                return("Hold\n")
            elif roll <19:
                return("Charge\n")
            else:
                return("Rush\n")
    
        elif status == '2':
            print('Engaged')
            if roll<=3:
                return("Recharge\n")
            elif roll <19:
                return("Onslaught\n")
            else:
                return("Fury\n")
            
        else:
            print("Other")
            if roll<=3:
                return("Recharge\n")
            elif roll <19:
                return("Charge\n")
            else:
                return("Rush\n")       

    #Type is ChaosBeastman
    elif InstanceEnemy=='6':
        print('Chaos Beastman')
        #generate dice roll
        roll=random.randint(1,20)
        status=input("Enter the status: Hidden = 1, Engaged = 2, Close = 3, Other *   ")
        print("roll = "+str(roll))
    #conditionals
        if status == '1':
            print('Hidden')
            if roll<=3:
                return("Hold\n")
            elif roll <9:
                return("Advance\n")
            elif roll <19:
                return("Charge\n")
            else:
                return("Rush\n")
    
        elif status == '2':
            print('Engaged')
            if roll<=15:
                return("Onslaught\n")
            else:
                return("Fury\n")
            
        elif status == '3':
            print('Close')
            if roll<=9:
                return("Onslaught\n")
            elif roll<=19:
                return("Charge\n")
            else:
                return("Rush\n")
            
        else:
            print('Other')
            if roll<=9:
                return("Advance\n")
            elif roll<=19:
                return("Charge\n")
            else:
                return("Rush\n")

	#Type is Chaos Space Marine
    elif InstanceEnemy=='7':
        print('Chaos Space Marine')
        #generate dice roll
        roll=random.randint(1,20)
        status=input("Enter the status: Hidden = 1, Engaged = 2, In Cover = 3, Close = 4, Other *   ")
        print("roll = "+str(roll))
    #conditionals
        if status == '1':
            print('Hidden')
            if roll<=3:
                return("Sneak\n")
            elif roll <9:
                return("Advance\n")
            elif roll <19:
                return("Charge\n")
            else:
                return("Rush\n")
    
        elif status == '2':
            print('Engaged')
            if roll<=15:
                return("Onslaught\n")
            else:
                return("Rapid Fire\n")
            
        elif status == '3':
            print('In Cover')
            if roll<=3:
                return("Aim\n")
            elif roll<=12:
                return("Onslaught\n")
            elif roll<=15:
                return("Advance\n")
            else:
                return("Rapid Fire\n")

            
        elif status == '4':
            print('Close')
            if roll<=6:
                return("Aim\n")
            elif roll<=12:
                return("Onslaught\n")
            elif roll<=15:
                return("Advance\n")
            else:
                return("Rapid Fire\n")
            
        else:
            print('Other')
            if roll<=9:
                return('Aim\n')
            elif roll<=15:
                return("Advance\n")
            else:
                return("Rapid Fire\n")
    
    #Type is ObsidiusMallex
    elif InstanceEnemy=='8':
        print('Obsidius Mallex')
        #generate dice roll
        roll=random.randint(1,20)
        status=input("Enter the status: Hidden = 1, Engaged = 2, In Cover w/ Lasgun = 3, Close = 4, Other *   ")
        print("roll = "+str(roll))
    #conditionals
        if status == '1':
            print('Hidden')
            if roll<=3:
                return("Sneak\n")
            elif roll <9:
                return("Advance\n")
            elif roll <12:
                return("Charge\n")
            else:
                return("Rush")
    
        elif status == '2':
            print('Engaged')
            if roll<=12:
                return("Onslaught\n")
            else:
                return("Fury\n")
            
        elif status == '3':
            print('In Cover')
            if roll<=6:
                return("Charge\n")
            elif roll<=19:
                return("Aim\n")
            elif roll<=15:
                return("Onslaught\n")
            elif roll<=19:
                return("Overcharge\n")
            else:
                return("Fury\n")
            
        elif status == '4':
            print('Close')
            if roll<=6:
                return("Onslaught\n")
            elif roll<=15:
                return("Charge\n")
            else:
                return("Overcharge\n")
            
        else:
            print('Other')
            if roll<=6:
                return("Advance\n")
            elif roll<=9:
                return('Aim\n')
            elif roll<=15:
                return("Onslaught\n")
            elif roll<=19:
                return("Overcharge\n")
            else:
                return("Rush\n")
    
    # Otheriwse exit
    else:
        return

'''
defines the behaviour output for unit
'''
def specialActions():
    result= str.lower(input("Enter behaviour result here for a definition: "))
    if result=="sneak":
        return('Make a move that ends as close as possible to an explorer without entering a hex that is visible to any explorers')
    elif result=="hold":
        return("Do nothing")
    elif result=="fall back":
        return("Double this hostile's Move Value when they take this action. If this hostile can make a move that ends in a hex not visible to any explorers, they do so. If they cannot, they attack the closest explorer that is in range and visible to this hostile.")
    elif result=="advance":
        return("Move towards the closest explorer. Then attack the closest explorer that is in range and visible to this hostile.")
    elif result=="aim":
        return("Attack the furthest explorer that is in range and visible to this hostile. That attack ignores Cover.")
    elif result=="charge":
        return("Move towards the closest explorer. Then attack an explorer that is adjacent and visible to this hostile. If there are no explorers adjacent and visible to this hostile, move towards the closest explorer a second time.")
    elif result=="onslaught":
        return("Attack the closest explorer that is in range of and is visible to this hostile. Then attack the closest explorer that is in range and visible to this hostile (may be a different target)")
    elif result=="alert":
        return("Increase the Threat Level by 1 and then take an Onslaught action. IF the Threat Level is 3, take an Onslaught action and reroll failed attack rolls for that action instead.")
    elif result=="rush":
        return("Move towards the closest explorer. The take a Charge action")
    elif result=="overcharge":
        return("Make an overcharged Plasma Pistol attack against thge closest explorer that is in range of and visible to Obsidius Mallex.")
    elif result=="recharge":
        return("Remove a Wound counter from this Negavolt Cultist. If the Negavolt Cultist does not have a Wound counter, treat this as an Advance result instead.")
    elif result=="disrupt":
        return("One unspent activation or Destiny dice chosen by the hostile player is discarded and cannot be spent this turn. If no unspent activation or Destiny dice are available, one explorer chosen by the hostile player suffers a wound.")
    elif result=="regenerate":
        return("Remove a Wound counter from this Rogue Psyker. If the Rogue Psyker does not have a Wound counter, treat this as an Disrupt result instead.")
    elif result=="empower":
        return("Place the Empower marker beside the Rogue Psyker. If the Rogue Psyker is already Empowered, treat this result as a Disrupt result instead. The Rogue Psyker remains Empowered until they suffer a Wound or Grevious Wound.")
    elif result=="annihilate":
        return("Place the Empower marker beside the Rogue Psyker. Then attack an explorer that is adjacent and visible to this hostile. Reroll failed attack rolls for that attack. The Rogue Psyker remains Empowered until they suffer a Wound or Grevious Wound.")
    elif result=="rapid fire":
        return("Take an Onslaught action. Reroll failed attack rolls for that action.")
    elif result=="fury":
        return("Take an Onslaught action. Reroll all failed attack rolls for that action.")
    elif result=="pounce":
        return("If there is an explorer adjacent and visible to this Ur-Ghul, take an Onslaught action. Otherwise take a Charge action. Reroll failed attack rolls for whichever action is taken.")
    else:
        return

def mainMeth():
    inp = input("do you need help? y/n ")
    while (inp == "y"):
        if (inp == "y"):
            print(Enemy())
            print(specialActions())
            print()
            inp = input("do you need help? y/n ")
        else:
            return
            
    

mainMeth()