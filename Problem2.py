def superManChicken(n, k, p):
   
    
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

print(superManChicken(5, 5, [2,5,10,12,15]))