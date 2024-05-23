def superManChicken(n, k, p):
    n = int(n)
    k = int(k)
    p = [int(num) for num in p]
    list_count = []
    for start_point_index in range(0,n-1):
        count = 0
        for point in range(start_point_index, n):
            start = p[start_point_index]
            end = p[start_point_index]+k
            target = p[point]
            if target < end and target >= start:
                count += 1
        list_count.append(count)
    

    
    return max(list_count)

n, k = input().split()
input_list = input().split()

print(superManChicken(n,k,input_list))