import math

def module_fuel(mass):
  module_fuel_total = 0
  while math.floor(int(mass) / 3) - 2 > 0:
    mass = math.floor(int(mass) / 3) - 2
    module_fuel_total += mass

  return module_fuel_total

def main():
  path = 'input.txt'

  with open(path, 'r') as f:
    mass = f.readline()

    total_fuel_required = 0
    while mass:
      total_fuel_required += module_fuel(mass)
      mass = f.readline()

    print('Day 1 part 2 puzzle answer is:', total_fuel_required)

if __name__ == '__main__':
  main()
