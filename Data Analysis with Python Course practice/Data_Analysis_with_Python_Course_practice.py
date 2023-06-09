
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
