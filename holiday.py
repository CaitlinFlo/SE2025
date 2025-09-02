# Program to calculate cost of holiday
# Initialise variables 

print('The cities you could fly to are: London (1), Paris (2), or Berlin (3).')

city_flight = int(input('Please enter the corresponding number to the city you would like to fly to:'))

num_nights = int(input('Please enter the amount of nights you want to stay for:'))

rental_days = int(input('Please enter how many days you will need a hire care for:'))

print(f'Thank you for entering the details! \n Cost calulating...')

# Define functions for hotel cost, plane cost, and car rental

price_per_night = 75
def hotel_cost(num_nights):
    x = price_per_night * num_nights
    return(x)

ticket = 0
def plane_cost(city_flight):
    if city_flight == 1:
            ticket = 125
    elif city_flight == 2:
            ticket = 150
    elif city_flight == 3:
            ticket = 200
    else:
        print('You have not selected a valid option - try again!')
    return(ticket)

price_rental = 50
def car_rental(rental_days):
    z = price_rental * rental_days
    return(z)

# Work out total holiday cost

print(f'The hotel costs {hotel_cost(num_nights)} for {num_nights} nights')
print(f'The flight will cost {plane_cost(city_flight)}')
print(f'The car rental will cost {car_rental(rental_days)} for {rental_days} days')


cost = 0
def holiday_cost(cost):
    cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return(cost)

print(f'The total cost of your holiday is {holiday_cost(cost)}')


