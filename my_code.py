    # 🖼️ Python Pattern Drawing Project

answer = ''

while True:

    if answer in ('2','no','No', 'NO'):
        print('Goodbye!')
        break

    # Step 1: Display a menu to the user
    print("🌟 Welcome to the Python Pattern Drawing Program!")
    print("Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")

    # Step 2: Get the user's choice
    choice = int(input("Enter the number corresponding to your choice: "))

    # Step 3: Get dimensions based on choice
    if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
        rows = int(input("Enter the number of rows: "))
    elif choice in [2, 5 ]:  # Patterns that need size #removed 8 as it is not needed for a 2d model
        size = int(input("Enter the size of the square/rectangle: "))

    # Step 4: Generate the selected pattern
    if choice == 1:  # Right-angled Triangle
        # TODO: Loop through rows and print increasing stars
        for r in range(rows+1):
            print('*' * r)

    elif choice == 2:  # Square with Hollow Center
        # TODO: Create a square with a hollow center
        print('Original:')
        for s in range(size):
            if s == 0 or s == (size - 1):
                print('*' * size)
            else:
                print('*' + (' ' * (size - 2)) + '*')
        print('Aesthetic:')
        for s in range(size):
            if s == 0 or s == (size - 1):
                print('*  ' * size)
            else:
                print('*' + (' ' * ((size - 1)* 3 -1) + '*'))

    elif choice == 3:  # Diamond
        # TODO: Create a diamond shape using loops
        if rows % 2 != 0:
            repleh = rows // 2
            helper = -1
            for r in range(1, rows):
                if r % 2 != 0:
                    print(' ' * repleh + ('*' * r))
                    repleh -= 1

            for r in range(rows, 0, -1):
                if r % 2 != 0:
                    helper += 1
                    print(' ' * helper + ('*' * r))
        else:
            repleh = (rows // 2) - 1
            helper = -1
            for r in range(1, rows):
                if r % 2 != 0:
                    print(' ' * repleh + ('*' * r))
                    repleh -= 1

            for r in range(rows, 0, -1):
                if r % 2 != 0:
                    helper += 1
                    print(' ' * helper + ('*' * r))

    elif choice == 4:  # Left-angled Triangle
        # TODO: Print decreasing stars for each row
        for r in range(rows, -1, -1):
            print('*' * r)

    elif choice == 5:  # Hollow Square
        # TODO: Similar to choice 2 but ensure perfect square logic
    # what is the difference between this and 2
        print('Original:')
        for s in range(size):
            if s == 0 or s == (size - 1):
                print('*' * size)
            else:
                print('*' + (' ' * (size - 2)) + '*')
        print('Aesthetic:')
        for s in range(size):
            if s == 0 or s == (size - 1):
                print('*  ' * size)
            else:
                print('*' + (' ' * ((size - 1)* 3 -1) + '*'))

    elif choice == 6:  # Pyramid
        # TODO: Center-align stars to form a pyramid
            repleh = rows - 1
            for r in range(1, rows * 2):
                if r % 2 != 0:
                    print(' ' * repleh + ('*' * r))
                    repleh -= 1

    elif choice == 7:  # Reverse Pyramid
        # TODO: Create an upside-down pyramid
        helper = -1
        for r in range(rows * 2, 0, -1):
            if r % 2 != 0:
                helper += 1
                print(' ' * helper + ('*' * r))

    elif choice == 8:  # Rectangle with Hollow Center
        # TODO: Handle separate width and height inputs for rectangle
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        print('Original:')
        for h in range(height):
            if h == 0 or h == (height - 1):
                print(width * '*')
            else:
                print('*' + ((width - 2) * ' ') + '*')

        print('Aesthetic:')
        for h in range(height):
            if h == 0 or h == (height - 1):
                print(width * '*  ')
            else:
                print('*' + (' ' * ((width - 1) * 3 - 1) + '*'))
    else:
        print("❌ Invalid choice! Please restart the program.")

    print('Play again?')
    print("Select your answer:")
    print("1. Yes")
    print("2. No")
    answer = input()

    if answer in ('2','no','No', 'NO'):
        print('Goodbye!')
        break

    elif answer in ('1','yes','Yes', 'YES', 'yea', 'Yea', 'YEA', 'yeah', 'Yeah', 'YEAH', 'ok', 'Ok', 'OK',
                    'okay', 'Okay', 'OKAY', 'sure', 'Sure', 'SURE'):
        continue

    else:
        print("I didn't understand that!")
        print('(☉_ ☉)')
        print('')
        print('Play again?')
        print("Select your answer:")
        print("1. Yes")
        print("2. No")
        answer = input()