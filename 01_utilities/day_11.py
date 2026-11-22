"""
Challenge : Friendship Compatibility Calculator

Build a Python script that calculate a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
3. Display the percentage with a themes message like;
 "You're like chai and samosa - made for each other!" or 
 "Well... opposites attract, maybe?"

Bonus:
 - Use emojis in the result
 - Give playful advise based on the score range
 - Capitalize and center the final output in a framed box

"""

def friendship_score(name1, name2):
    name1, name2 = name1.lower(),name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2)
    vowels = set('aeiou') 

    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10
    if score >= 80:
        print("you both are made for each other.") 
    elif 50< score <80:
        print("You're like chai and samosa.")
    elif 20<= score <=50:
        print("You're kind of warm spices.")    
    else:
        print("You're tea and your friend is coffee you are not goind to be gelling up together.")
    return min(score,100)

def run_friendship_calculator():
    print("❤️ Friendship Comapatibility Calculator ❤️")
    name1 = input("Enter first name: ") 
    name2 = input("Enter second name: ")

    score = friendship_score(name1,name2)

    print(f"\nYour frindship score is: {score}")
run_friendship_calculator()    