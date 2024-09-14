def a_and_b(a,b):
    if a==1:
        prob_student=0.3
        if b==1:
            prob_dinning=0.75
        else:
            prob_dinning=0.25
        print("Probablity if a given b",prob_dinning)

    if a==2:
        prob_student=0.7
        if b==1:
            prob_dinning=0.6
        else:
            prob_dinning=0.4
        print("Probablity if a given b",prob_dinning)
    prob_a_and_b=prob_student*prob_dinning
    return round(prob_a_and_b,3)

print("first enter your choices:")
print("1:freshman  2:old")
a=int(input("enter your choices:"))

print("1:dinning hal  2:room")
b=int(input("enter your choices:"))

print("the answer is ",a_and_b(a,b))