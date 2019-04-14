a = [1, 1, 2, 4, 5, 11, 14, 33, 45, 13]
b = [1, 0, 2, 3, 9, 99, 11, 33]

common = []

# loop through contents in a
for item in a:

    # loop through the contents in b
    for number in b:

        # check if contents in a is in b and not in common
        if item == number and item not in common:

            # adds the common value
            common.append(item)


print(common)
