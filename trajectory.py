"""Takes height and distance of an object and calculates
the optimal angle with the minimum intial velocity required to 
reach the object"""

"""for some reason gives math domain error
 when height == distance"""

import math

	
def trajectory(d, h, r):
	#takes distance, height and angle in radians to get inital velocity
	v0 = (d / math.cos(r)) * math.sqrt(9.8 / (2 * (d * math.tan(r) - h)))
	return v0

print("The distance cannot be less than 1/57th of the height")
	
distance = float(input("How far away is the target?(meters) "))
height = float(input("How high up is the target?(meters) "))

hypotenuse = math.sqrt(distance ** 2 + height ** 2)

#minimum angle required to still be pointing about the target
min_angle = int(math.degrees(math.asin(height / hypotenuse)))

possible_radians = []
#create list of all possible angles that aim above the height
for x in range((min_angle + 1), 90):
	rad = math.radians(x)
	possible_radians.append(rad)
	
velocities = []
#calculate all initial velocities for possible angles and store in list
for i in possible_radians:
	v = trajectory(distance, height, i)
	velocities.append(v)
#calculates best velocity and the angle for that velocity	
best_velocity = min(velocities)
best_angle = velocities.index(best_velocity) + (min_angle + 1)

print("The optimal launch angle for minimum initial velocity would be " + str(best_angle) + " degrees")	
print("The initial velocity needed at this angle is " + str(best_velocity) + " m/s")
	
