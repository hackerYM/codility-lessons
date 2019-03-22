def solution(A):
    
    num_count = {}
    for num in A:
        num_count[num] = num_count.get(num, 0) + 1
    
    leader_num, leader_count = 0, 0
    
    for num, count in num_count.items():
        if count > leader_count:
            leader_num, leader_count = num, count

    equi_leader_count = 0
    front_count, rear_count = 0, leader_count
    
    for idx in range(0, len(A)-1):
        if A[idx] == leader_num:
            front_count, rear_count = front_count + 1, rear_count - 1
        
        if front_count > (idx+1) // 2 and rear_count > (len(A)-idx-1) // 2:
            equi_leader_count += 1
    
    return equi_leader_count
