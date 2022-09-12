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
