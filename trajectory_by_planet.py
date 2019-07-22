import math

"""Takes height and distance of an object and calculates
the optimal angle with the minimum initial velocity required to 
reach the object (in ballistic motion) on a provided planet"""


planets = ['earth', 'mars', 'venus', 'saturn', 'jupiter', 'mercury', 'neptune', 'uranus']

print("The distance cannot be less than 1/57th of the height")

distance = float(input("How far away is the target?(meters) "))
height = float(input("How high up is the target?(meters) "))
planet = str.lower(input("What planet are you on? "))

while planet not in planets:
    response = str.lower(input("Sorry that's not a planet in our solar system, are you on earth? "))
    if response == 'yes':
        planet = 'earth'
    else:
        planet = str.lower(input('What planet are you on then? '))

hypotenuse = math.sqrt(distance ** 2 + height ** 2)

# minimum angle required to still be pointing at or above the target
min_angle = int(math.degrees(math.asin(height / hypotenuse)))

possible_radians = []
# create list of all possible angles that aim above the height
for x in range((min_angle + 1), 90):
    rad = math.radians(x)
    possible_radians.append(rad)


def trajectory(d, h, r):
    # takes distance, height and angle in radians to get initial velocity
    global gravity
    if planet == 'earth':
        gravity = 9.8
    elif planet == 'mercury':
        gravity = 3.7
    elif planet == 'jupiter':
        gravity = 24.79
    elif planet == 'saturn':
        gravity = 10.44
    elif planet == 'mars':
        gravity = 3.71
    elif planet == 'venus' or planet == 'uranus':
        gravity = 8.87
    elif planet == 'neptune':
        gravity = 11.15

    v0 = (d / math.cos(r)) * math.sqrt(math.fabs(gravity / (2 * (d * math.tan(r) - h))))
    return v0


velocities = []
# calculate all initial velocities for possible angles and store in list
for i in possible_radians:
    v = trajectory(distance, height, i)
    velocities.append(v)
# calculates best velocity and the angle for that velocity
best_velocity = min(velocities)
best_angle = velocities.index(best_velocity) + (min_angle + 1)

print("The optimal launch angle for minimum initial velocity would be " + str(best_angle) + " degrees")
print("The initial velocity needed at this angle is " + str("%.2f" % best_velocity) + " m/s")

input('Press Enter to exit')
