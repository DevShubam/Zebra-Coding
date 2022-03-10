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