#questions
a1 = int(input("On a scale from 1 to 5, highest stress being 1, how stressed are you on a daily basis? "))
if a1 > 5:
    print("invalid input, please restart")
a2 = int(input("On a scale from 1 to 5, definite yes being 1 and absolute no being 5, do you have a history with substance abuse? "))
if a2 > 5:
    print("invalid input, please restart")    
a3 = int(input("On a scale from 1 to 5, great being 5, how is your life at home? "))
if a3 > 5:
    print("invalid input, please restart")
a4 = int(input("On a scale from 1 to 5, a lot being 5, how social are you with other people? "))
if a4 > 5:
    print("invalid input, please restart")
a5 = int(input("On a scale from 1 to 5, highest being 5, how high is your self esteem? "))
if a5 > 5:
    print("invalid input, please restart")   

#functions

score = a1 + a2 + a3 + a4 + a5
def total_score(score):
    help1 = "Seek some help (866-392-8523). You are mentally unstable and it's effecting your wellbeing. Try to exercise, eat well, and make some time for your hobbies and go se the doctor aswell."
    help2 = "Seek some help (866-392-8523). You are in distress and it's effecting your wellbeing. Try to exercise, eat well, and make some time for your hobbies."
    help3 ="It's okay to be in distress sometimes, but make sure you stay healthy mentally. Try to exercise, eat well, and make some time for your hobbies to better your wellbeing."
    help4 = "You are healthy mentally, but if you ever feel down or like you need some extra support you can try to exercise, eat well, or make some time for your hobbies."
    help5 = "You have an ideal mental health, but if you ever feel down or like you need some extra support you can try to exercise, eat well, or make some time for your hobbies and try to help others who have worse mental health."
    
    if score > 20:
        print(help5)
    if score >= 15 and score <= 20:
        print(help4)
    if score < 15 and score >= 10:
        print(help3)
    if score > 5 and score < 10:
        print(help2)
    if score <= 5:
        print(help1)
        
total_score(score)