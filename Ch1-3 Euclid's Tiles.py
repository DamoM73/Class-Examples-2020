# FUNCTIONS
# calcuate tile size
def calculate_tile_size(long_side, short_side):
    remainder = long_side % short_side
    while remainder != 0:
        remainder = long_side % short_side
        long_side = short_side
        short_side = remainder

    return long_side

# display the floor


# display tile size



# ---- MAIN PROGRAM ----
room_length = int(input("Room length: "))
room_width = int(input("Room width: "))
tile_size = calculate_tile_size(room_length,room_width)
print(tile_size)