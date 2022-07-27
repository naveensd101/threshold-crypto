import random
p = 1e9+7

a = 0 # store the message
n = 0 # number of keys we will generate
k = 0 # number of keys needed to decrypt
def main():
  print("type in a, n and k")
  a = int(input())
  n = int(input())
  k = int(input())

  poly = []
  poly.append(a)
  for _ in range(k-1):
    poly.append(random.randint(0, p))

  #actual generation of n keys
  keys = {}
  for i in range(1, n+1):
    # we have to find out Q(i)
    # poly array (i)
    ans = 0
    for exp, coef in enumerate(poly):
      ans += coef * int(pow(i, exp))

    keys[i] = ans

  print(keys)
  for i in keys.keys():
    print(i, keys[i])

main()
