while True:
    print('Hi! Do you want to know how to calculate apothem quickly? This is the program for you')

    shapes = ["equilater triangle", "square", "pentagon", "hexagon", "heptagon", "octagon", "nonagon", "decagon", "dodecagon"]

    f_triangle = 0.289
    f_square = 0.5
    f_pentagon = 0.688
    f_hexagon = 0.866
    f_heptagon = 1.038
    f_octagon = 1.207
    f_nonagon = 1.374
    f_decagon = 1.539
    f_dodecagon = 1.866

    print('Of which shapes do you want to know the apothem?')

    for figura in shapes:
        print(figura)

    print('Press 0 for equilater triangle, 1 for squaref_square, 2 for pentagon, 3 for hexagon, 4 for heptagon, 5 for octagon, 6 for nonagon, 7 for decagon, 8 for dodecagon')

    chosen_number = int(input())
    chosen_shape = shapes [chosen_number]

    print("You choose " + chosen_shape)
    print('Insert the lenght of the side of the shape')

    side = int(input())

    apotema = ""
    if (chosen_number == 0):
        apotema = (side * f_triangle)
    if (chosen_number == 1):
        apotema = (side * f_square)
    if (chosen_number == 2):
        apotema = (side * f_pentagon)
    if (chosen_number == 3):
        apotema = (side * f_hexagon)
    if (chosen_number == 4):
        apotema = (side * f_heptagon)
    if (chosen_number == 5):
        apotema = (side * f_octagon)
    if (chosen_number == 6):
        apotema = (side * f_nonagon)
    if (chosen_number == 7):
        apotema = (side * f_decagon)
    if (chosen_number == 8):
        apotema = (side * f_dodecagon)

    print(apotema)

    print('Do you want to calculate it again?')
    response = int(input('Insert 0 to continue or 1 to exit: '))
    if response == 0:
        continue
    else:
        break