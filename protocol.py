from opentrons import instruments, containers, robot
from opentrons.util import environment
from opentrons.util.vector import Vector
from math import *

#robot.connect(robot.get_serial_ports_list()[0])
def initall():
	robot.connect(robot.get_serial_ports_list()[0])
	robot.is_connected()
	robot.home()

#Inital all variables
trash = containers.load('point', 'A1')
tiprack = containers.load('tiprack-200ul', 'A3')


water_1 = containers.load('point', 'B3')
water_2 = containers.load('point', 'C3')
water_3 = containers.load('point', 'D3')

pcr96_1 = containers.load('96-PCR-flat', 'B1')
pcr96_2 = containers.load('96-PCR-flat', 'C1')
pcr96_3 = containers.load('96-PCR-flat', 'D1')

petri_1 = containers.load('point', 'B2')
petri_2 = containers.load('point', 'C2')
petri_3 = containers.load('point', 'D2')

pipette = instruments.Pipette(
	axis='b',
	min_volume=20,
	max_volume=200,
	tip_racks=[tiprack],
	trash_container=trash,
	)

pcr = [pcr96_1, pcr96_2, pcr96_3]
water = [water_1, water_2, water_3]
petri = [petri_1, petri_2, petri_3]

# find the x y of the other 2 petri dishes later
#aryofxpetri = [52, 666, 444]

#aryofypetri = [48, 666, 444]

#x_a1 = 52
#y_a1 = 48
#z_a1 = 100;

def archimdeanspiral(a, b, theta):
	r = a + b * theta
	return r


def polartoxy(r, theta):
	x = r * cos(theta)
	y = r * sin(theta)

	return x, y

def samplepick2(n, x, y):
	#goes to the petridish
	pipette.move_to(( petri[n], Vector(
		petri[n]._coordinates.coordinates.x,
		petri[n]._coordinates.coordinates.y,
		petri[n]._coordinates.coordinates.z
		)), 'arc' )
	#wiggle
	pipette.aspirate(100)

def samplepick(x1, y1, z1):

	robot.move_head(x=x1, y=y1, z=100)
	robot.move_head(x=x1, y=y1, z=z1)
	#wiggle
	robot.move_head(x=x1+.5, y=y1+.5, z=z1)
	robot.move_head(x=x1-1, y=y1-1, z=z1)

	pipette.aspirate(100)
	robot.move_head(x=x1, y=y1, z=10)

def goto1():
	robot.move_head(x=89, y=125, z=100)

def goto2():
	robot.move_head(x=181, y=125, z=100)

def goto3():
	robot.move_head(x=272, y=125, z=100)

def mainprogram(timez):
	pipette.drop_tip(trash)
	for each in range(timez):
		a, b = 5, 1
		petri_diameter = 85
		theta = 1
		deltaincrease = (petri_diameter / 2 - 2 - a) / b / len(pcr96_1.wells())
		#n = 0
		#pick up the tip from the tiprack, the variable each will do the next one
		pipette.pick_up_tip(tiprack.wells(each))
		#loop through each well
		for well in range(96):
			print(well)
			#get water from the water trough

			pipette.aspirate(100, water[each])

			#a turns the spiral, while b controls the distance between successive turnings
			r = a + b * theta

			x = r * cos(theta)
			y = r * sin(theta)
			theta += deltaincrease

	#		print(petri[each])

			pipette.move_to(( petri[each], Vector(
				petri[each]._coordinates.coordinates.x + x,
				petri[each]._coordinates.coordinates.y + y,
				petri[each]._coordinates.coordinates.z
			)), 'arc' )

			pipette.aspirate(100)

			pipette.move_to(( petri[each], Vector(
				petri[each]._coordinates.coordinates.x + x - 1,
				petri[each]._coordinates.coordinates.y + y - 1,
				petri[each]._coordinates.coordinates.z
			)), 'direct' )

			pipette.move_to(( petri[each], Vector(
				petri[each]._coordinates.coordinates.x + x + 2,
				petri[each]._coordinates.coordinates.y + y + 2,
				petri[each]._coordinates.coordinates.z
			)), 'direct' )


			pipette.dispense(200, pcr[each].wells(well).bottom())
			
			

			
			'''
			pipette.move_to(( petri[each], Vector(
				pcr[each].wells(well)._coordinates.coordinates.x + 2,
				pcr[each].wells(well)._coordinates.coordinates.y + 2,
				pcr[each].wells(well)._coordinates.coordinates.z
			)), 'direct' )'''


			#find the location to aspirate the yeast samples
		'''	t = n / 20 * 3.14
			x = (1 + 5 * t) * cos(t)
			y = (1 + 5 * t) * sin(t)
			n = n + 1 '''
			#samplepick(x + aryofxpetri[each], y + aryofypetri[each], - 40)
			#samplepick2(each, x, y)
			#pipette.aspirate
		#drop pippete into trash 
		pipette.drop_tip(trash)
#initall()
#mainprogram(3)

def btest(n, photoary):

	petri1 = [89, 125]
	petri2 = [181, 125]
	petri3 = [272, 125]

	petri = [petri1, petri2, petri3]

	for i in range(n):
		count = 0
		pipette.pick_up_tip(tiprack.wells(i))
		for num in range(336):
			x = 0
			y = 0
			while y < 640:
				while x < 480:
					color = photoary[i][y,x]
					print(color)
					x+= 20
					if color == 255 :
						pipette.aspirate(100, water[i])
						robot.move_head(x=(petri[i][0] + (x/10)), y= (petri[i][1] +(y/10)), z=100)
						robot.move_head(x=(petri[i][0] + (x/10)), y= (petri[i][1] +(y/10)), z=-40)
						pipette.aspirate(100)
						pipette.dispense(200, pcr[i].wells(count).bottom())
						count += 1
					if count == 96:
						return
				y+= 20
			count += 1

initall()
mainprogram(3)
