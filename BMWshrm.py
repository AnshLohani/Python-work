
#BMW Virtual  Showroom

while True:
    print("Welcome to the BMW virtual showroom! {We Have only i/X/M Series}")
    print('''Enter which series do you want from the following list:
              1. BMWi Series
              2. X Series
              3. M Series
             ''')
    srs= int(input("Enter the series you want( enter the corresponding number in the list ): "))

############################


    if srs==1:
        print("Thanks for picking the BMWi Series (btw this is the fully electric collection!)")
        print('''Pick your car from the given list to see its basic info:
                               1. BMW iX
                               2. BMW i4
                               3. BMW i7
             ''')
        srs1= int(input("Enter the number corresponding to your car! : "))
        if srs1 == 1:
            print("BMW iX is a good choice!")
            print('''
Price: 1.18 Cr
Charging time: 7.25hours
Range: 372-425km
Seating Capacity: 5''')
            break
                 
        elif srs1 == 2:
                 print("BMW i4 is a good choice!")
                 print('''
Price: 69.9 lakhs
Charging time: 8.25 hours
Range: Upto 590km
Seating Capacity: 5''')
                 break
        elif srs1 == 3:
                print("BMW i7 is a good choice!")
                print('''
Price: 1.95 Cr
Charging time: 12 hours
Range: Upto 625km
Seating Capacity: 5''')
                break


#############################################



    elif srs==2:
        print("Thanks for picking the BMW X Series !")
        print('''Pick your car from the given list to see its basic info:
                               1. BMW X1
                               2. BMW X3
                               3. BMW X5
                               4. BMW X7
             ''')
        srs1= int(input("Enter the number corresponding to your car! : "))
        if srs1 == 1:
            print("BMW X1 is a good choice!")
            print('''
Price: 41.5 Lakhs
Fuel Type: Petrol & Diesel
Engine: 1995cc - 1998cc
Seating Capacity: 5
Top Speed: 222- 226 km/h''')
            break
    
        elif srs1==2:
                print("BMW X3 is a good choice!")
                print('''
Price: 61.89 Lakhs
Fuel Type: Petrol & Diesel
 Engine: 1995cc - 1998cc
Seating Capacity: 5
Top Speed: 213 km/h
                              ''')
                break
                 
        elif srs1==3:
                print("BMW X5 is a good choice!")
                print('''
Price: 99.9 Lakhs
Fuel Type: Petrol & Diesel
Engine: 2993 cc - 2998 cc
Seating Capacity: 5
Top Speed: 243 km/h''')
                break

        elif srs1==4:
                print("BMW X7 is a good choice!")
                print('''
Price: 1.2 Cr
Fuel Type: Petrol & Diesel
Engine: 2993 cc - 2998 cc
Seating Capacity: 6
Top Speed: 250 km/h''')
                break
        
    elif srs == 3:
        print("Thanks for picking the BMW M Series !")
        print('''Pick your car from the given list to see its basic info:
                               1. BMW Z4 M40i
                               2. BMW M4
                               3. BMW M8
                               4. BMW M340i
                               5. BMW XM
             ''')
        srs1= int(input("Enter the number corresponding to your car! : "))
        if srs1==1:
                print("BMW Z4 M40i is a good choice!")
                print('''
Price: 84.9 Lakhs
Fuel Type: Petrol 
Engine: 2998 cc
Seating Capacity: 2
Top Speed: 268 km/h''')
                break
        if srs1==2:
                print("BMW M4 is a good choice!")
                print('''
Price: 1.44 Cr
Fuel Type: Petrol 
Engine: 2993 cc
Seating Capacity: 5
Top Speed: 295 km/h''')
                break
        if srs1==3:
                print("BMW M8 is a good choice!")
                print('''
Price: 2.5 Cr
Fuel Type: Petrol 
Engine: 4395 cc
Seating Capacity: 5
Top Speed: 310 km/h''')
                break
        if srs1==4:
                print("BMW M340i is a good choice!")
                print('''
Price: 69.2 Lakhs
Fuel Type: Petrol 
Engine: 2998 cc
Seating Capacity: 5
Top Speed: 215 km/h''')
                break
        if srs1==5:
                print("BMW XM is a good choice!")
                print('''
Price: 2.6 Cr
Fuel Type: Plugin Hybrid 
Engine: 4395 cc
Seating Capacity: 6
Top Speed: 249 km/h
Range: 82km
Charging time: 12hrs''')
                break

    else:
        print("Pick a number! ")
        break
   
print("Thanks for using our virtual showroom! Made for a school project by Ansh Lohani and Abhinav Deo class 11th G")
