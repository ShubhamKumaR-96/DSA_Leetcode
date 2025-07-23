# Given:

# N tasks, where A[i] is the time taken to complete the i-th task.

# K workers.

# Constraints:

# One task can only be done by one person.

# A worker can only do continuous tasks (i.e., if a worker takes tasks i to j, they cannot skip any task in between).

# All workers can work simultaneously.

# Goal: Find the minimum time required to complete all tasks under these constraints.


def minTimeToTask(A,k):
    left=max(A)
    right=sum(A)

    ans=0

    def isFeasible(mid):
        worker=1
        curr_sum=0

        for time in A:
            if curr_sum+time>mid:
                worker+=1
                curr_sum=time
                
                if worker > k:
                    return False
                
            else:
                curr_sum+=time   

        return True         

    while left<=right:
        mid=left+(right-left)//2

        if isFeasible(mid):
            ans=mid
            right=mid-1

        else:
            left=mid+1

    return ans

A = [3, 5, 1, 7, 2, 4] 
K = 3

print(f"Min time {minTimeToTask(A,K)}")