# Dictionary
baby_names =    {'dog' : 'pup',
                 'rabbit' : 'bunny',
                 'kangaroo' : 'joey',
                 'monkey' : 'infant',
                 'hippo' : 'calf',
                 'horse' : 'foal',
                 'owl' : 'owlet',
                 'parrot' : 'chick',
                 'rat' : 'pup',
                 'cow' : 'calf',
                 'skunk' : 'kit',
                 'sheep' : 'lamb'}


# while loop
userChoice = 0
while userChoice != 4:
    print("Select one of the options below:")
    print("1: Lookup Animal Baby Names")
    print("2: Add Animal Names")
    print("3: Delete Animal Name")
    print("4: End")
    userChoice = int(input("Choose what you want to do: "))

    # 1
    if userChoice == 1:
        animal = input("What animal baby name do you want to know: ")
        animal.lower()
        if animal in baby_names:
            print("The baby name of the "+ animal + " is " + baby_names[animal])
        else:
            added_animal = input("This animal is not in the list, would you like to add it to the list: ")
            if added_animal == 'yes':
                key = input("What's the adult name of the animal: ")
                value = input("What's the baby name of the animal: ")
                baby_names[key] = value
                print(baby_names)
        

    # 2
    if userChoice == 2:
        key = input("What's the adult name of the animal: ")
        value = input("What's the baby name of the animal: ")
        baby_names[key] = value
        print(baby_names)


    # 3
    if userChoice == 3:
        key = input("Which animal do you want to delete: ")
        del baby_names[key]
        print(baby_names)