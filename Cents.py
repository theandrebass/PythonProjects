def coins(n)
  if n < 4:
    print("Error: function does not work for numbers that are less than 4)
    return (1, -1)  
  if n == 4
    return (2, 0) #base case return 2, 2 cents
  c = coins(n - 1)
  twos = c[0]
  fives = c[1]
  if twos >= 2:
    twos = twos - 2
    fives = fives + 1
  elif fives >= 1:
    fives = fives - 1
    twos = twos + 3
  c = [twos, fives]
  return c
  
def printCoins(n):
  coinVals = coins(n)
  print(str(n) + " cents can be created with " + str(coinVals))
