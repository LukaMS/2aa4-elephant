import sys

def main():

  tax = {"ON": 0.13, "QC": 0.14975, "MB": 0.05, "NS": 0.15, "BC": 0.05}

  #Extract First argument as the price of the item
  price = float(sys.argv[1])

  #Extract second arg as the quatitiy
  quantity = int(sys.argv[2])

  prov = sys.argv[3]

  pre_tax = price * quantity

  after_tax = str(pre_tax * (1 + tax[prov]))

  print("Price after tax: " + after_tax)

if __name__ == '__main__':
  main()