destinations = ['Houston', 'Wichita', 'Milwaukee', 'New York City']

#houston_restaurants = ['Kings BBQ', 'Whataburger', 'Mamacitas mexican restaurant', 'Killens BBQ']
#houston_entertainment = ['Tour Buffalo Bayou Park Cistern', 'Play Top Golf', 'NASA Space Center','Kemah Broadwalk']

#wichita_resturants = ['Hog Wild Pit BBQ', 'Bomber Burger', 'Spangels', 'Fredddys Frozen Custard']
#wichita_entertainment = ['Wichita Wingnuts game', 'Wichita riverwalk', 'Club Rodeo', 'Sedgwick County Zoo']

#milwaukee_resturants = ['Kopps', 'Oscars Frozen Custard' 'AJ Bombers', 'Milwaukee Burger Company']
#milwaukee_entertainment = ['Harley-Davison Museum', 'Concert at Eagles Ballroom', 'Brewers game', 'Potawatomi Casino']

#nyc_resturants = ['Grand Central Oyster Bar', 'Tavern on the Green', 'Rosas Pizza', 'Royal 35 Steakhouse']
#nyc_entertainment = ['Tour Empire State Bulding', 'Tour Central Park', '9/11 Memorial', 'show on Broadway']


import random
#def destinations_random(destinations):
#    for pick in destinations:
#        destinations = (random.randint(0, 3))
#        if destinations == (0):
#            return 'Houston'
#        elif destinations == (1):
#            return 'Wichita'
#        elif destinations == (2):
#            return 'Milwaukee'
#        elif destinations == (3):
#            return 'New York City'

#location = destinations_random(destinations)
#print("Hello welcome to the day trip planner.")
#while location:
#    city = destinations_random(destinations)
#    greeting = input(f"Would you like to start your trip in {city} ? y/n ")
#    if greeting == ("y"):
#        break
#    else:
#        print("Okay lets try somewhere else?")

mode_of_transport = ['train', 'car', 'bus', 'walk']
def mode_of_movement(mode_of_transport):
    for vehicle in mode_of_transport:
        variable = len(mode_of_transport)
        vehicle = (random.randrange(0, variable))
        transport = mode_of_transport.pop(vehicle)
        variable = len(mode_of_transport) - 1
        return transport
while mode_of_transport:
    transport = mode_of_movement(mode_of_transport)
    means_of_travel = input(f"would you like to use {transport} as your mode of transportation? y/n ")
    if means_of_travel == ("y"):
        break
    else:print("Okay lets try something else")

