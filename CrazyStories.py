import random
X = ['Annokentiy', 'Adam', 'Kirito', 'Rokki', 'Pavlik']
Y = ['Anna', 'Alina', 'Batman', 'Superman', 'Captain America']
Location = ['Vegetable garden', 'River', 'Stark Tower', 'Gym', 'Forest']
Doing_what = ['Ate fat', 'Fished', 'Smoked the peace pipe', 'to dance', 'Run for beer']
questions = ['How are you', 'How your work', 'Buy bread', 'Sold the car', 'Sailed across the ocean ']
end = ['Going to Home', 'Fished Akula', 'Give water']
name1 = [random.choice(X)]
name2 = [random.choice(Y)]
print(random.choice(name1) + ' and ' + random.choice(name2) + ' are in ' + random.choice(Location) + '. ' + 'They are ' + random.choice(Doing_what) + '. ' + random.choice(name1) + ' says to ' + random.choice(name2) + ' ' + random.choice(questions) + '. ' + random.choice(name2) + ' says to ' + random.choice(name1) + ' ' + random.choice(questions) + '. ' + random.choice(end) + '.')