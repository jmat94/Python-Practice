"""
This program is used to calculate the total cost of tiles.
"""

# Create class to calculate the area of the room and area required for one tile
class RoomInformation():
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area_of_room(self):
         area = self.width * self.height
         # print("The total area of the room is: {}".format(area))
         return area

    def perimeter_of_room(self):
        perimeter = 2 * (self.height + self.width)
        print("Perimeter: {}".format(perimeter))

    def area_of_one_tile(self, value1, value2):
        area_one_tile = value1 * value2
        return area_one_tile
        # print("Area of one tile is: {}".format(area_one_tile))

# Creating cost object
cost =RoomInformation(4,3)
# cost.area_of_room()

# Creating area and are of one tile object
area_room = cost.area_of_room()
one_tile_area = cost.area_of_one_tile(0.3,0.3)


# Calcualting the total area
total_area = area_room/one_tile_area
# print(total_area)

# Number of tiles That could be wasted
wastage = total_area * 0.05
# print(wastage)

# Total number of tiles required
number_of_tiles_required = total_area + wastage
# print(number_of_tiles_required)


# User input taken for cost
try:
    cost_of_tiles = float(input("Enter The cost: "))
except ValueError:
    print("Please enter a proper value.")

# Calculate the total cost
total_cost_of_tiles = cost_of_tiles * number_of_tiles_required
print(total_cost_of_tiles)