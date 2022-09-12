#This is an 'easy' questions with following methods.
def method1(s: str, t: str) -> bool:
  if len(s) == 0:
     return True
  pivot = 0
  for x in t:
    if x == s[pivot]:
    pivot += 1
    if pivot >= len(s):
      return True
  return False

'''
iter(t) returns an iterator, which like a stack. Every time visit the first one, and remove it. 
all() helps to check whether all items are True. 
'''
def method2(s: str, t:str) -> bool:
  t = iter(t)
  return all(c in t for c in s)

#However, there are some methods bease on dynamic programming or binary search, which would be faster.
