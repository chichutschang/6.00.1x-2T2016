# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 12:21:11 2016

@author: chi-chu tschang
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    # Your code here
    #array of length L    
    P=[None]*len(L)
    #array of length L+1    
    M=[None]*len(L)
    
    N=0
    M[0]=0    
    j=0
    for i in range(len(L)-1):
        #binary search for the largest positive j <= N
        #such that X[M[j]]<X[i]
        print('i',i)
        print('L[M[j]]',L[M[j]])
        print('L[i]',L[i])
        lo = 1
        hi = N
        while lo <= hi:
            print('lo',lo)
            print('hi',hi)
            mid = (lo+hi) // 2
            print('mid',mid)
            if L[M[mid-1]]<L[i]:
                lo = mid + 1
                print('L[M[mid-1]]',L[M[mid-1]])
                print('L[i]', L[i])
                print('lo',lo)
            else:
                hi = mid-1
                print('hi',hi)
        #after searching, lo is 1 greater than the 
        #length of the longest prefix of X[i]
        j = lo
        print('j',j)
        
        #the predecessor of X[i] is the last index of
        #the substance of length newN-1
        P[i] = M[j-1]
        #print('P[i]',P[i])
        M[j] = i
        #print('M[j]', M[j])
            
        if j > N:
        # if we found a subsequence longer than any we've 
        #found yet, update L
            N = j
            #print('N',N)
        #reconstruct the longest increasing subsequence
        #S = [None] 
        #k = M[N]
        #for i in range(N-1):
        #    S[i] = L[k]
        #    k=P[k]
        #return S
            
            