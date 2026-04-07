#program to calculate the cost of tile to cover floor width and height using the cost entered by user 
import math 
def tile_cost():
    #user input to enter the floor width and height 

    floor_width = float(input("Enter floor width in (foot):\n"))
    floor_height = float(input("Enter floor heigh in (foot)\n"))

    floor_area = floor_width * floor_height

    tile_width = float(input("Enter tile width of the tile in (foot):\n"))
    tile_height = float(input("Enter the height of the tile in (foot)\n"))

    tile_area = tile_width * tile_height

    tile_cost = float(input("Enter the cost of the tile"))

    number_tiles = math.ceil(floor_area /tile_area)

    total_cost =  tile_cost * number_tiles
    
    print("---Calculating total tile cost---")
    print("The floor area is :", floor_area)
    print("The tile area is:", tile_area)
    print("The number of tiles is :", number_tiles)
    print("The total cost is:", total_cost)


total_tile_cost = tile_cost()
print(total_tile_cost)




