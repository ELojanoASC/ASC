from random import *

drinkList = ["Pickle juice", "Pepsi", "Lemonade", "Salt water"]

petList = ["Michaelangelo the Ninja Turtle", "Tony the Tiger", "Barney the Dinosaur", "Swiper the Fox"]

abilitiesList = ["Coding", "Life", "School", "Sports"]

socialMediaList = ["Facebook", "MySpace", "Twitter", "Eons"]

print("Welcome to Ericks' Game of Chance")

myInput = raw_input("What's your favorite Drink?")
randomDrink = choice(drinkList)
print("Your favorite drink is",randomDrink)

myInput = raw_input("What pet would you like?")
randomPet = choice(petList)
print("Your pet is",randomPet)

myInput = raw_input("What do you suck at?")
randomAbilities = choice(abilitiesList)
print("You SUCK at",randomAbilities)

myInput = raw_input("Whatr social media do you use?")
randomSocialMedia = choice(socialMediaList)
print("You use", randomSocialMedia)

print("Thanks for playing")