#this is an 'easy' question with following solutions
'''
method 1 is a general way to solve the problem. Build two dictionaries and check them when scanning string s and t.
'''
def method1(s: str, t: str) -> bool:
  dict_s = {}
  dict_t = {}
  for x, y in zip(s, t):
    if (x not in dict_s) and (y not in dict_t):
      dict_s[x] = y
      dict_t[y] = x
    elif (dict_s.get(x) != y) or (dict_t.get(y) != x):
      return False
    
    return True

'''
method2 leverages zip() function. zip(s, t) returns a tuple like (s[0], t[0]), (s[1], t[1]), ..., (s[len(s)], t[len(t)]).
Then use set to remove identical terms, and check length to get result. 
method2 is far faster than method1
'''  
def method2(s: str, t: str) -> bool:
  return  len(set(zip(s, t))) == len(set(s)) == len(set(t))

'''
s.find(x) will return the first index i that s[i] = x
'''
def method3(s: str, t: str) -> bool:
  return [s.find(x) for x in s] == [t.find(y) for y in t]

'''
map(fun, list) is fun(list[i]) for i in range(len(list))
'''
def method4(s: str, t: str) -> bool:
  return list(map(s.find, s)) == list(map(t.find, t))
