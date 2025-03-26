# Course: DSK814
# Project 1
# Group members: Michal Sycik, Igor Rachuta

import sys

# Side functions:

def Left(i):
    return 2*i+1
def Right(i):
    return 2*i+2
def Parent(i):
    return (i-1)//2

def Min_heapify(A,i):
    l = Left(i)
    r = Right(i)
    if l < len(A) and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        temp=A[i]
        A[i] = A[smallest]
        A[smallest] = temp
        Min_heapify(A,smallest)
    
def createEmptyPQ():
    return []

def insert(A,e):
    A.append(e)
    i=len(A)-1
    while i>0 and A[Parent(i)]>A[i]:
        temp = A[i]
        A[i] = A[Parent(i)]
        A[Parent(i)] = temp
        i = Parent(i)
    
def extractMin(A):
    if len(A) == 0:
        return None
    min_elem= A[0]   # root , root is the smallest value in the heap
    A[0] = A[-1]     # move higher number (from the end) to the first place in list 
    A.pop()          # remove last number, its now duplicate, since we moved it before.
    Min_heapify(A,0) # Min_heapify will move it (the first number in list, moved here) down to the right spot.
    return min_elem  # Return 1st (root) element, saved before changes as min_elem.
    
 
# Testing
    
if __name__ == "__main__":
    pq = createEmptyPQ()
    for val in [34, 645, 3, -45, 1, 34, 0]:
        insert(pq, val)

    print(f"For values {pq}, sorted:")
    
    while len(pq) > 0:
        print(extractMin(pq))

