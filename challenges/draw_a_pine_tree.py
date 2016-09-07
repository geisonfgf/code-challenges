# ---------- PROBLEM : DRAW A PINE TREE ----------
# For this problem I want you to draw a pine tree after asking the user
# for the number of rows. Here is the sample program
 
'''
How tall is the tree : 5
    #
   ###
  #####
 #######
#########
    #
'''
 
# You should use a while loop and 3 for loops
 
# I know that this is the number of spaces and hashes for the tree
# 4 - 1
# 3 - 3
# 2 - 5
# 1 - 7
# 0 - 9
# Spaces before stump = Spaces before top
 
# So I need to
# 1. Decrement spaces by one each time through the loop
# 2. Increment the hashes by 2 each time through the loop
# 3. Save spaces to the stump by calculating tree height - 1
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and then hashes for each row
# 6. Print stump spaces and then 1 hash
 
# Get the number of rows for the tree
tree_height = input("How tall is the tree : ")
 
# Convert into an integer
tree_height = int(tree_height)
 
# Get the starting spaces for the top of the tree
spaces = tree_height - 1
 
# There is one hash to start that will be incremented
hashes = 1
 
# Save stump spaces til later
stump_spaces = tree_height - 1
 
# Makes sure the right number of rows are printed
while tree_height != 0:
 
    # Print the spaces
    # end="" means a newline won't be added
    for i in range(spaces):
        print(' ', end="")
 
    # Print the hashes
    for i in range(hashes):
        print('#', end="")
 
    # Newline after each row is printed
    print()
 
    # I know from research that spaces is decremented by 1 each time
    spaces -= 1
 
    # I know from research that hashes is incremented by 2 each time
    hashes += 2
 
    # Decrement tree height each time to jump out of loop
    tree_height -= 1
 
# Print the spaces before the stump and then a hash
for i in range(stump_spaces):
    print(' ', end="")
 
print("#")