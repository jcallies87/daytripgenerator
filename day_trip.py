print("Hello welcome to the day trip planner.")
day_trip_planner = True
while (day_trip_planner):
    import random
    def random_generator(list_one):
        for vehicle in list_one:
            variable = len(list_one)
            vehicle = (random.randrange(0, variable))
            product_one = list_one.pop(vehicle)
            variable = len(list_one) - 1
            return product_one
    location = ["Houston", 'Wichita', 'Milwaukee', 'New York City']
    list_one = location
    while location:
        city = random_generator(list_one)
        greeting = input(f"Would you like to start your trip in {city} ? y/n ")
        if greeting == ("y"):
            break
        else:
            print("Okay lets try somewhere else?")
    product_one = city

    resturants = ['Whataburger', 'Olive Garden', 'Ruby Tuesday', 'Taco Bell']
    list_one = resturants
    while resturants:
        dining = random_generator(list_one)
        where_to_eat = input(f"Would you like to have dinner at {dining} tonight ? y/n ")
        if where_to_eat == ("y"):
            break
        else:
            print("Okay lets try somewhere else?")
    product_one = dining

    mode_of_transport = ['the train', 'the car', 'the bus', 'walking']
    list_one = mode_of_transport
    while mode_of_transport:
        transport = random_generator(list_one)
        means_of_travel = input(f"would you like to use {transport} as your mode of transportation? y/n ")
        if means_of_travel == ("y"):
            break
        else:print("Okay lets try something else")
    product_one = transport

    entertainment = ['go to a movie at the movie theater', 'see a concert', 'visit the zoo', 'enjoy the museum']
    list_one = entertainment
    while entertainment:
        activity = random_generator(list_one)
        what_to_see = input(f"would you like to {activity} as your activity? y/n ")
        if what_to_see == ("y"):
            break
        else:print("Okay lets try something else")
    product_one = activity

    print(f"So your day trip is set to take place in {city}. We will get there via {transport}. We will be dining at {dining} tonight, and we are planning to {activity}.")
    confirm = input("Do you want to take this day trip? y/n ")
    for day_trip_planner in confirm:
        if confirm == "y":
            print("Thank you for using the day trip planner, enjoy your trip.")
            day_trip_planner = False
        elif print( "ok lets try this again"):
            break
