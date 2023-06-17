
my_wife_name = 'Natasha'
my_wife_age = 23;
my_name = 'Kat';
my_age = 24;
age_difference = my_age-my_wife_age
if age_difference >= 1:
    print('This is the age difference: {} between me and my wife'.format(age_difference));

my_fav_food, wife_fav_food = 'ramen', 'burger';
my_fav_music = 'pop';
wife_fav_music = 'electro';
print(my_fav_food, wife_fav_food, my_fav_music, wife_fav_music);
print(my_name[1])
if 'Nat' in my_wife_name:
    sentence = my_name +' ' + 'and' + ' ' + my_wife_name + ' ' + '= love'
    print(sentence.lower())
else:
    print(my_fav_food.upper(), wife_fav_music.capitalize())

if 'Kat' in my_wife_name:
    sentence = my_name +' ' + 'and' + ' ' + my_wife_name + ' ' + '= love'
    print(sentence.lower())
else:
    pass

my_wife_favorite_philosopher = 'Wittgenstein';

if my_wife_favorite_philosopher == 'Plato':
    print("My wife's favorite philosopher is Plato")
elif my_wife_favorite_philosopher == 'S.D.Bovuir':
    print("My wife's favorite philosopher is S.D.Bovuir")
elif my_wife_favorite_philosopher == 'Kafka':
    print("My wife's favorite philosopher is Kafka")
else:
    print("My wife's favorite philosopher is Wittgenstein")

sleep_hours = 8;

health = 'good' if sleep_hours >= 8 else 'bad'
print('I slept {} hours today so my health is {}'.format(sleep_hours,health))


i = 1;

while i < my_wife_age:
    i+=1

print(i);

j = 1;   
while j < my_wife_age:
    j+=1
    if j == 21:
        print("She met me at {}".format(j))
        continue
print(j);

for char in my_wife_name:
    print(char)

OurFavoriteFood = (my_fav_food, wife_fav_food, 'ice cream', 'veg salad')
for food in OurFavoriteFood:
    print("What we both love to eat? ", food)

def move_cost(rent, comission, deposit, taxi_cost):
    """this function calculates the overall sum of moving to another flat with 4 incoming values:

    rent - the amount of monthly rent (rub)
    deposit - how much is landlord asking for deposit (rub)
    comission - the percent from rent that is goint to estate agent (number)
    taxi_cost - payment for moving (rub)
    """
    comission = (rent/100)*comission
    sum_cost = rent + deposit + comission + taxi_cost
    return sum_cost

cost_of_moving1 = move_cost(36000,50,36000,0)
print(cost_of_moving1)

cost_of_moving2 = move_cost(37000,0,15000,0)
print(cost_of_moving2)
help(move_cost)

import numpy as np
a = np.array([2, 3, 4])
print(a)

import urllib.request

urllib.request.urlretrieve(
    'https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 
    'climate.txt')
climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)
print(climate_data)
