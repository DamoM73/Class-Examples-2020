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
tile_size = calculate_tile_size(345,150)
print(tile_size)