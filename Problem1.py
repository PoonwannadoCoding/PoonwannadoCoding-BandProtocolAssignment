def IsGoodBoy(input):
    count_s = 0
    count_r = 0
    if input[0] == 'R' or input[len(input)-1] =='S':
        return "Bad boy"
    
    for word in input:
        if word == 'S':
            if count_r > count_s:
                return "Bad boy"
            count_s += 1
        elif word == 'R':
            count_r += 1 
    return "Good boy"

assert IsGoodBoy("SRSSRRR") == "Good boy", "The result should be Good boy"
