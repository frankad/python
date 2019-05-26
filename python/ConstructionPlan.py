# Name: Fentahun Reta
# CSC 110 Assigment 1
# Date: 10/02/14
# Building foundation
# The Bricks & Mortar Construction Company builds strong foundations
# Description:The program can calculate  some features of the building foundation, and then calculating the mass
#             number, and costs of bricks and mortar to build the foundation.
# Constants---information we already know
# one brick measures 6 cm x 9 cm x 19 cm.
# volume of one brick = 0.001026 cubic_meter and its mass = 2.3 kg,
costs bricks $0.65, dollars per bricks
costs bricks $633.53 # dollars per cubic_meter
# costs bricks $0.0.283 # dollars per kg
# One bag of mortar contains 0.025 cubic_meter of mortar with a mass of 43 kg.
cost a bag of mortar of $7.25. # dollars per bag
cost a bag of mortar of $290. # dollars cubic_meter
cost a bag of mortar of $0.1686. # dollars per kg
# 15% of the volume of a foundation make by mortar and 85% by bricks.
cubic_meter per cubic_centimeters = 1,000,000.00  # conversion factors
square_meter per square_centimeters = 1000.00     # conversion factors
wall_thickness = 0.4 # meters
 
# Input section
data = 'please enter the external \"length\" of the foundation in centimeters.\nThe '\
          +'length is the external longest dimension of the building: '
height = float(input(data))
data = '\nNow enter the \'heighth\' of the foundation in centimeters.\n'\
          + 'Height is the distance from the ground to the top of the foundation: '
height = float(input(data))
data = '\nFinally, enter the third dimension of the foundation building, ' \
          + '\nit is \'width\', and also in centimeters: '
width = float(input(data))
wall_thickness = float(input('whta is the thickness of the wall in centimeters: ')


# PROCESSING section -- performing calculations
overall_area = length*width*height; # in square centimeters

enclosed_area = (length - 2*wall_thickness)

area_covered_by_foundation = overall_area - enclosed_area
                       
total_volume_foundation_wall = area_covered_by_foundation*height

volume_one_bricks = 1026 cubic centimeters

total_volume_bricks = total_volume_foundation_wall*85/100

total-bricks_number = total_volume_bricks/volume_one_bricks

total_cost_bricks = total_bricks_number*0.65 dollars

bricks_mass = total_bricks_number*2.3 kg

total_volume_bag = total_volume_foundation_wall*15/100

volume_one_bag = 0.025 cubic meter

total_bag_number = total_volume_bag/volume_one_bag

mass_bag_mortar = total_bag_number*43 kg

total_cost_mortar = total_bag_number*7.25 dollars

material_total_mass = mass_bag_mortar + bricks_mass

material_total_cost = total_cost_bricks + total_cost_mortar


# output section
print('\n\nThis is the summarized features and costs of the \"foundation of the building\":\n')

print('wall length: ' + str(length)'cm.')
print('wall height: ' + str(height)'cm.')
print('wall width: ' + str(width)'cm.')

print('Overall area: ' + str(overall_area) 'cubic cm.')
print('Enclosed area: ' + str(enclosed_area) 'cubic cm.')
print('Overall area: ' + str(overall_area) 'cubic cm.')
print('Area of ground covered by the wall: ' + str(area_covered_by_foundation) 'cubic cm.')


print('Total volume of the wall: ' + str(total_volume_foundation_wall) 'cubic cm.')

print('Total number of bricks needed: ' + int(total_bricks_number))
print('Number of bags of mortar: ' + int(total_bag_number))

print('The total mass of bricks and mortar: ' + str(material_total_mass))

print('The total material cost to build the foundation of your building is: ' + str(material_total_cost))
                       
rint('\nThank you for choosing XY Construction PLC. Company.'\)
print('XY Construction PLC. Company will meet and exceed your expectations for your building!')
                    



                      


        
                        
                        
