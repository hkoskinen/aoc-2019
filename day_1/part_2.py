import math

def calc_module_fuel(mass):
  mass = math.floor(int(mass) / 3) - 2
  return 0 if mass < 1 else mass + calc_module_fuel(mass)

def main():
  path = 'input.txt'

  with open(path, 'r') as f:
    mass = f.readline()

    total_fuel_required = 0
    while mass:
      total_fuel_required += calc_module_fuel(mass)
      mass = f.readline()

    print('Day 1 part 2 puzzle answer is:', total_fuel_required)

if __name__ == '__main__':
  main()
