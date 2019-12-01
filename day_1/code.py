import math

def main():
  path = 'input.txt'

  with open(path, 'r') as f:
    mass = f.readline()

    total_fuel_required = 0
    while mass:
      fuel_for_module = math.floor(int(mass) / 3) - 2
      total_fuel_required += fuel_for_module
      mass = f.readline()

    print('Day 1 part 1 puzzle answer is:', total_fuel_required)


if __name__ == '__main__':
  main()
