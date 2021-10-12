def solution(list, num):
    a = 0
    b = 0
    solution=[]
    differ_map={}
    for i, ele in enumerate(list):
        difference = num-ele
        if difference in differ_map:
            b = i
            a = differ_map[difference]
            break;
        else:
            differ_map[ele] = i
    return a, b


numbers = [2, 7, 11, 4]
print("Indices for solution 13", solution(numbers, 13))
print("Indices for solution 10:", solution(numbers, 10))