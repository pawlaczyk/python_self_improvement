# i = 1
# while i <= 20:
#     if (i % 2) == 0:
#         i += 1
#         continue
#     if i == 15:
#         break
#     print("OddL ", i)
#     i += 1

# hohinka wysokosci
tree_height = int(input("How tall is the tree: "))

# spaces = tree_height - 1
# hashes = 1
# stump_spaces = tree_height - 1
#
# while tree_height != 0:
#     for i in range(spaces):
#         print(" ", end="")
#     for i in range(hashes):
#         print("#", end="")
#     print()
#     spaces -= 1
#     hashes += 2
#     tree_height -= 1
#
# for i in range(stump_spaces):
#     print(" ", end="")
# print("#")
#

i = 1
while i <= tree_height:
    hashes = i + (i-1)
    spaces = tree_height - i
    print(" "*spaces, "#"*hashes, " "*spaces)
    i+= 1

spaces = tree_height - 1
print(" "*spaces, "#", " "*spaces)