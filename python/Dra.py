# Name: Fentahun Reta
# Date: 10/15/15
# Dicription: This program demonstrates drawing shapes on a canvas using
#             some Gui tools. It is not interactive. It draws the same picture
#             every time it is executed. To run this program, you must save the
#             file Gui3.py in the same folder as this program.
# Required import statement for Gui tools

import Gui3

# Named Constants 
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480


# Function Definition Section

# Draws one sky.  The parmeters base_x and base_y specify
# the location point at the bottom edge
# of the sky. hus, all the other parameters have units of pixels.

def sky (base_x, base_y, height):
    # the sky picture is obtained by assuming a circle that has a
    # center outside the scene space
    sky_bottom_x = base_x
    sky_bottom_y = base_y
    canvas.circle([sky_bottom_x, sky_bottom_y + (10/20)*height], (10/20)*height,\
                   fill='skyblue')
    
# Draws a car. The parmeters x and y specify for the coordinate point for the
# center of the bottom edge of the car. The last parameter is the "height" of
# the car, the distance from the bottom part of the tayer to the top of the car.
# All other measurments in pixels unit.

def car(base_x, base_y, height):
    
    # main body
    # The body of the car has trapizoid shape. we can use the digonal points.
    # car left bottom corner (clbc) and car right top corner (wrtc)
    clbc_x = base_x - (6/5)*height 
    crbc_x = base_x + (6/5)*height
    cltc_x = base_x - (3/5)*height
    crtc_x = base_x + (6/5)*height
    
    clbc_y = base_y + (1/5)*height 
    crbc_y = base_y + (1/5)*height            
    cltc_y = base_y + height 
    crtc_y = base_y + height              
    canvas.polygon([[clbc_x, clbc_y], [cltc_x, cltc_y], [crtc_x, crtc_y], [crbc_x, crbc_y]],\
                   fill='red')
    # rare tayer
    rare_tayer_x = base_x + (4/5)*height
    rare_tayer_y = base_y + (1/5)*height
    canvas.circle([rare_tayer_x, rare_tayer_y], (1/5)*height, fill='black')
    # front tayer
    front_tayer_x = base_x - (3/5)*height
    front_tayer_y = base_y + (1/5)*height
    canvas.circle([front_tayer_x, front_tayer_y], (1/5)*height, fill='black')
    # line on the side body of the car
    x1 = base_x - height
    y1 = base_y + (2/5)*height
    x2 = base_x + (6/5)*height
    y2 = base_y + (2/5)*height
    canvas.line([[x1, y1], [x2, y2]], width=4)
    
# Draw a tree.  The parmeters base_x and base_y specify the location of a point at the center
# of the bottom edge of the tree trunk.  The last parameter is the height of the tree.  All
# other parameters are in units of pixels.

def draw_tree(base_x, base_y, height):
    # draw trunk
    # The trunk has lower left (TLL) and top right (TTR) points to get the stem or the trunk
    TLL_x = base_x - (0.5/5)*height 
    TTR_x = base_x + (0.5/5)*height
    TLL_y = base_y  
    TTR_y = base_y + (3/5)*height
    canvas.rectangle([[TLL_x, TLL_y], [TTR_x, TTR_y]], fill='brown', width = 0)
    # draw top part of the tree or leaf
    # It has has one peak (leaf Peak) and two lower parts, left bottom(LLB) and right bottom (LRB)
    LP_x = base_x
    LP_Y = base_y + height
    LLB_x = base_x - (2/5)* height 
    LRB_x = base_x + (2/5)* height 
    LLB_y = LRB_y = base_y + (3/5)*height
    canvas.polygon([[LP_x, LP_Y], [LLB_x, LLB_y], [LRB_x, LRB_y]], fill='darkgreen', width=0)

# Draws a cluster of three trees.  The parmeters x and y specify
# the location of a point at the center of the bottom edge
# of the tree trunk of the largest tree in the cluster.
# The last parameter is the "size" of the cluster -- the distance
# in pixels from the bottom to the top of the cluster.


def draw_tree_cluster(x, y, height):
    draw_tree(x - (0.8/5)*height, y + (1/5)*height, (2/5)* height)
    draw_tree(x + (0.8/5)*height, y + (1/5)*height, (2/5)*height)
    draw_tree(x, y, (2.5/5)*height)
    
# Draw a bigsnowman. The parmeters x and y specify the point or coordinate
# of for the center of the bottom edge of the big snowman, and the last parameter
# is the "height" of the big snowman: the distance from the bottom to the top of
# the big snowman. All parameters have units of pixels.

def big_snowman(base_x,base_y,height):
    #bottom
    bottom_part_x = base_x
    bottom_part_y = base_y
    canvas.circle([ bottom_part_x,  bottom_part_y + (2.8/9.5)*height], (2.8/9.5)*height, \
                  fill='white')
    #abdomen
    #abdomen represents all the middle body of the snowman
    abdomen_x = base_x
    abdomen_y = base_y +(4/9.5)*height
    canvas.circle([abdomen_x, abdomen_y + (2.5/9.5)*height], (2.5/9.5)*height, fill='white')
    #face
    big_face_x = base_x
    big_face_y = base_y + (7.5/9.5)*height
    canvas.circle([big_face_x, big_face_y + (1.5/9.5)*height], (1.5/9.5)*height, fill='white')
    #nose
    big_nose_x = base_x
    big_nose_y = base_y + (8.5/9.5)*height
    canvas.circle([big_nose_x, big_nose_y], (0.25/9.5)*height, fill='black')
    #eyes
    big_left_eye_x = base_x - (0.5/9.5)*height
    big_left_eye_y = base_y + (9/9.5)*height
    canvas.circle([big_left_eye_x, big_left_eye_y +(0.2/9.5)*height], (0.2/9.5)*height,\
                  fill='black')
    big_right_eye_x = base_x + (0.5/9.5)*height
    big_right_eye_y = base_y + (9/9.5)*height
    canvas.circle([big_right_eye_x, big_right_eye_y +(0.2/9.5)*height], (0.2/9.5)*height,\
                  fill='black')
    #button_1
    big_button_X = base_x
    big_button_y = base_y + (6/9.5)*height
    canvas.circle([big_button_X, big_button_y], (0.25/9.5)*height, fill='blue')
    #button_2
    big_button_X = base_x
    big_button_y = base_y + (5/9.5)*height
    canvas.circle([big_button_X, big_button_y], (0.25/9.5)*height, fill='blue')
    #button_3
    big_button_X = base_x
    big_button_y = base_y + (4/9.5)*height
    canvas.circle([big_button_X, big_button_y], (0.25/9.5)*height, fill='blue')
    #hat
    hat_top_x = base_x
    hat_top_y = base_y + (12/9.5)*height
    hat_left_x = base_x -(1.5/9.5)*height
    hat_left_y = base_y + height
    hat_right_x = base_x + (1.5/9.5)* height
    hat_right_y = base_y + height
    canvas.polygon([[hat_top_x ,hat_top_y], [hat_left_x, hat_left_y], \
                    [hat_right_x, hat_right_y]], fill='red')

def small_snowman(base_x,base_y,height):
    #bottom
    small_bottom_x = base_x
    small_bottom_y = base_y
    canvas.circle([small_bottom_x, small_bottom_y + 2.8/8*height], (2.8/8)*height, fill='white')
    #small snowman face
    small_face_x = base_x
    small_face_y = base_y + (4/8)*height
    canvas.circle([small_face_x, small_face_y + (2/8)*height], (2/8)*height, fill='white')
    #nose
    small_nose_x = base_x
    small_nose_y = base_y + (5/8)*height
    canvas.circle([small_nose_x, small_nose_y], (0.2/8)*height, fill='black')
    #eyes
    small_left_eye_x = base_x - (0.5/8)*height
    small_left_eye_y = base_y + (6/8)*height
    canvas.circle([small_left_eye_x, small_left_eye_y], (0.15/8)*height, fill='black')
    small_right_eye_x = base_x + (0.5/8)*height
    small_right_eye_y = base_y + (6/8)*height
    canvas.circle([small_right_eye_x, small_right_eye_y], (0.15/8)*height, fill='black')
    #button_1
    small_button_x = base_x
    small_button_y = base_y + (4/8)*height
    canvas.circle([small_button_x, small_button_y], (0.25/8)*height, fill='blue')
    #button_2
    bsmall_button_x = base_x
    small_button_y = base_y + (3/8)*height
    canvas.circle([small_button_x, small_button_y], (0.25/8)*height, fill='blue')
    
    #hat
    hat_top_x = base_x
    hat_top_y = base_y + (9/8)*height
    hat_left_x = base_x -(1.8/8)*height
    hat_left_y = base_y + (7/8)*height
    hat_right_x = base_x + (1.8/8)*height
    hat_right_y = base_y + (7/8)*height
    canvas.polygon([[hat_top_x ,hat_top_y], [hat_left_x, hat_left_y], \
                    [hat_right_x, hat_right_y]], fill='red')
# Draws a house. The parmeters x and y specify for the coordinate point at the
# center of the bottom edge of the house. The last parameter is the "height" of
# the house, the distance from the bottom to the top of the house. All measurments
# have in pixels unit. 

    
def draw_house(base_x, base_y, height):
    #House Ceiling, the upper part (above the wall) of the house.
    #ceiling_left_top/bottom_corner_x is abrevated as CLTC_x/CLBC-x
    #ceiling_right_top/bottom_corner_x is CLRT_x/CRTC-y/CRBC_y
    ceiling_house_x = base_x
    ceiling_house_y = base_y + (8/5)*height
    CLTC_x = base_x - (4.5/5)*height
    CLTC_y = base_y + (8/5)*height
    CLBC_x = base_x - (7.5/5)*height
    CLBC_y = base_y + height
    CRTC_x = base_x + (4.5/5)*height
    CRTC_y = base_y + (8/5)*height
    CRBC_x = base_x + (7.5/5)*height
    CRBC_y = base_y + height
    canvas.polygon([[CLTC_x, CLTC_y], [CRTC_x, CRTC_y], [CRBC_x, CRBC_y], [CLBC_x, CLBC_y]],\
                   fill='brown')
    
   #wall
   # The face of the house wall has rectangular shape. we can use the digonal points.
   # wall left bottom corner (wlbc) and wall right top corner (wrtc)

    wlbc_x = base_x - (4.5/5)*height 
    wrtc_x = base_x + (4.5/5)*height
    wlbc_y = base_y  
    wrtc_y = base_y + height
    canvas.rectangle([[wlbc_x,wlbc_y], [wrtc_x,wrtc_y]], fill='gray')
    # The house door has also rectangular shape
    # door left bottom corner (dlbc) and door right top corner (drtc)
    dlbc_x = base_x - (1/5)*height 
    drtc_x = base_x + (1/5)*height
    dlbc_y = base_y 
    drtc_y = base_y + (2/5)*height
    canvas.rectangle([[dlbc_x,dlbc_y], [drtc_x,drtc_y]], fill='red')
    
def main():
    #draw things on the canvas
    
    sky(-260,170,600)
    sky(-60,180,600)
    sky(40,180,500)
    sky(300,210,500)
    sky(140,180,450)
    sky(280,180,400)
    car(-160,-220, 100)
    draw_tree(40, 60, 120)
    draw_tree_cluster(260, 100,80)
    draw_tree_cluster(160, 40, 80)
    draw_house(-150,-40,100)
    
    

    snow_man()
def snow_man():
    big_snowman(60,-220,190)
    big_snowman(130,-220,190)
    small_snowman(250,-220,160)



#####################################################################
#
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#
#####################################################################

# Setup the canvas -- canvas is the drawing area
# Note that 'win' and 'canvas' are GLOBAL VARIABLES in this program
win = Gui3.Gui()
win.title('Playing around with Gui')
canvas = win.ca(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# run the main function
main()

# show the window
win.mainloop()

# Here are some colors you can use: 'white', 'gray', 'black', 'red',
# 'green', 'blue', 'cyan', 'yellow', 'magenta', 'brown', 'darkgreen'
# Hundreds of colors here: http://tmml.sourceforge.net/doc/tk/colors.html




    
