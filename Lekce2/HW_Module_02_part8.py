while True:
    print("1. Vzor 1")
    print("2. Vzor 2")
    print("3. Vzor 3")
    print("4. Vzor 4")
    print("5. Vzor 5")
    print("6. Vzor 6")
    print("0. Konec")
    
    volba = input("Zadejte vaši volbu (1/2/3/4/5/6/0): ")
    radky = 8

    if volba == '1':
        for i in range(1, radky + 1):
            print('*' * i)
    elif volba == '2':
        for i in range(radky, 0, -1):
            print('*' * i)
    elif volba == '3':
        for i in range(1, radky + 1):
            print(' ' * (radky - i) + '*' * i)
    elif volba == '4':
        for i in range(radky, 0, -1):
            print(' ' * (radky - i) + '*' * i)
    elif volba == '5':
        k = 0
        for i in range(1, radky + 1): 
            for j in range (1, (radky - i) + 1): 
                print(end = " ")
            while k != (2 * i - 1):
                print("*", end = "")
                k = k + 1
            k = 0   
            print()
        k = 2
        m = 1
        for i in range(1, radky): 
            for j in range (1, k):
                print(end = " ") 
            k = k + 1
            while m <= (2 * (radky - i) - 1): 
                print("*", end = "") 
                m = m + 1
            m = 1	
            print()
    elif volba == '6':
        for i in range (0, radky):
            for j in range(0, i + 1):
                print("* ", end='')
            print("\r")
        for i in range (radky, 0, -1):
            for j in range(0, i -1):
                print("* ", end='')
            print("\r")
    elif volba == '0':
        print("Konec programu")
        break
    else:
        print("Neplatná volba. Zadejte prosím 1, 2, 3, 4 nebo 5.")
