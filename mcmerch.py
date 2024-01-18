import sys

def main():

  tax = {"ON": 0.13}

  #Extract First argument as the price of the item
  price = float(sys.argv[1])

  #Extract second arg as the quatitiy
  quantity = int(sys.argv[2])

  pre_tax = price * quantity

  after_tax = pre_tax * (1 + tax["ON"])

  print("Price after tax: " + after_tax)

if __name__ == '__main__':
  main()