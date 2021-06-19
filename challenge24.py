person_height = float(input("What is your height in inches: "))

# If anyone is 54 inches or taller

if (person_height >= 54):
    print("You may ride all the rides")

# If they are 39 inches or shorter

if (person_height <=39):
    print("You may not ride any rides, the minimum height is 40.")

# If between 40 and 47

if ( person_height > 40 and person_height <= 47):
    print("You may ride Taxi Jam, Sugar Shack, TTAdventure. You may not ride any other rides.")

# If between 48 and 53

if (person_height > 48 and person_height <= 53):
    print("You may ride: Taxi Jam, Sugar Shack, TTAdventure, Lumber Jack, Flying Canoes. You may not ride any other rides")
