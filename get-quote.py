<<<<<<< HEAD
import random
=======
def main():
  print("Keep it logically awesome.")
>>>>>>> b94ec1f7b9f1e0b4b80bfdd91879c75b62ce0b5d

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
