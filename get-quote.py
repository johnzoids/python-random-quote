import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  low = 0
  last = 13
  rnd = random.randint(low ,last)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
