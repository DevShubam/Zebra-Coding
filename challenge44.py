# Write a function for checking the speed of drivers. This function should have one parameter: speed.

# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. 
# For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”

def driver_speed(speed):
    if speed <=70:
        return 0
    else: 
        points = (speed - 70) / 5
        if points >= 12.0:
            return -1
        else:
            return points
ret = driver_speed(1000)

if ret == 0:
    print("Ok")
elif ret == -1:
    print ("License Suspended.")
else:
    print("Points:",ret)
