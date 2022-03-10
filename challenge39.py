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
                 'sheep' : 'lamb',}


animal = input("What animal baby name do you want to know: ")
animal.lower()


if animal in baby_names:
    print("The baby name of the "+ animal + " is " + baby_names[animal])
else:
    print("This animal is not in the list")