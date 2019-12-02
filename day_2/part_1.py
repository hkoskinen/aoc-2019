
def main():
  path = 'input.txt'
  codes = open(path, 'r')

  # split string and convert each part to int
  inp = [int(x) for x in codes.read().split(',')]
  print('START', inp)

  # set input to "1202 program alarm" state
  inp[1] = 12
  inp[2] = 2

  # loop over the input
  index = 0
  opcode = inp[0]
  while opcode != 99:
    if opcode == 1:  # add
      inp[inp[index + 3]] = inp[inp[index + 1]] + inp[inp[index + 2]]
    elif opcode == 2:  # multiply
      inp[inp[index + 3]] = inp[inp[index + 1]] * inp[inp[index + 2]]
    elif opcode == 99:  # program is finished and should immediately halt
      print('FINISHED', opcode)
      break
    else: # unknown opcode, something went wrong
      print('UNKNOWN OPCODE', opcode)
      break

    index = index + 4
    opcode = inp[index]

  print('END', inp)
  print()
  print('Day 2 part 1 puzzle answer is:', inp[0])

if __name__ == '__main__':
  main()
