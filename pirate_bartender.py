import random as r

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}



preferences = {}
def drink_style():
    # grabs key value pair from questions dict and finds
    # out what the customer likes to drink
    for key, value in questions.items():
        question = raw_input(value + " ")
        if (question.lower() == 'yes') or (question.lower() == 'y'):
            preferences[key] = True
        else:
            preferences[key] = False
            

def concoct(preferences):
    #finds key value pair in preferences func
    # and makes a drink based on their liking
    drink_type = []
    for key, value in preferences.items():
        if value != True:
            continue
        else:
            drink_type.append(r.choice(ingredients[key]))
    
    return drink_type 

def main():
    # call both drink_style and concoct
    drink_style()
    drink = concoct(preferences)
            
    print(" ")
    print("The ingredients are as followed:")
    for ingredient in drink:
        print("{}".format(ingredient))

if __name__ == '__main__':
    main()  

