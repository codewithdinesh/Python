def calculate(sr):
    lower = 0
    upper = 0

    for s in sr:
        if(s.isupper()):
            upper = upper+1
        if(s.islower()):
            lower = lower+1

    print("Lower: ", lower)
    print("Upper: ", upper)


calculate("HEYY whats up")
