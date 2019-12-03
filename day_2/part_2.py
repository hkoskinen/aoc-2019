
def main():
  path = 'input.txt'
  codes = open(path, 'r')
  original_memory = [int(x) for x in codes.read().split(',')]

  data = original_memory.copy()
  quit_now = False
  for noun in range(99):
    for verb in range(99):
      data[1] = noun
      data[2] = verb

      index = 0
      opcode = data[0]
      while opcode != 99:
        if opcode == 1:  # add
          data[data[index + 3]] = data[data[index + 1]] + data[data[index + 2]]
        elif opcode == 2:  # multiply
          data[data[index + 3]] = data[data[index + 1]] * data[data[index + 2]]
        elif opcode == 99:  # program is finished and should immediately halt
          print('FINISHED', opcode)
          break
        else: # unknown opcode, something went wrong
          print('UNKNOWN OPCODE', opcode)
          break

        index = index + 4
        opcode = data[index]

      #print('data[0] is', data[0])
      if data[0] == 19690720:
        print('Day 2 part 2 puzzle answer is:', 100 * noun + verb)
        quit_now = True
        break
      else:
        # reset state and try again
        data = original_memory.copy()
    if quit_now:
      break

if __name__ == '__main__':
  main()
