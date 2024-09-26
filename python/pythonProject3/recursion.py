"""def rec(n):
    if(n==0 or n==1):
        return 1
    return n*rec(n-1)
print(rec(4))"""
def su(lst, ind):
    if ind == len(lst):  # Base case, when index equals the length of the list
        return
    print(lst[ind])
    su(lst, ind + 1)  # Recursive call with the next index

fu = ["an", "ham", "jak"]
su(fu, 0)
