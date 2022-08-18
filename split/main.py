#!/bin/python3
import random
p = 1e9+7 # upper bound on the random numbers

secret_int = 0 # store the message
num_of_keys = 0 # number of keys we will generate
min_keys = 0 # number of keys needed to decrypt
def main():
  print("Enter a secret integer: ", end="")
  secret_int = int(input())

  print("Enter total number of share holders: ", end="")
  num_of_keys = int(input())

  print("Enter minimum number of shares to decrypt: ", end="")
  min_keys = int(input())

  poly = []
  poly.append(secret_int)
  for _ in range(min_keys-1):
    poly.append(random.randint(0, p))

  #actual generation of n keys
  keys = {}
  for i in range(1, num_of_keys+1):
    # we have to find out Q(i)
    # poly array (i)
    ans = 0
    for exp, coef in enumerate(poly):
      ans += coef * int(pow(i, exp))

    keys[i] = ans

  #print(keys)
  for i in keys.keys():
    print(i, keys[i])

main()
