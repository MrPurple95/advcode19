import sys

def runIntCodeProgram(intCodes, param1, param2):
    intCodes[1] = param1
    intCodes[2] = param2
    i = 0
    while i < len(intCodes):
        opcode = intCodes[i]
        op1 = intCodes[i+1]
        op2 = intCodes[i+2]
        res = intCodes[i+3]
        if opcode == 1:
            intCodes[res] = intCodes[op1] + intCodes[op2]
        elif opcode == 2:
            intCodes[res] = intCodes[op1] * intCodes[op2]
        elif opcode == 99:
            break
        i += 4
    return intCodes[0]

with open('advcode2.txt') as fp:
    opcodesString = fp.readline().split(',')
    opcodes = []
    for s in opcodesString:
        opcodes.append(int(s))
    i = 0
    #print(opcodes)
    #print(len(opcodes))
    #intCodesCopy = opcodes.copy()
    for k in range(99):
        for j in range(99):
            intCodesCopy = opcodes.copy()
            result = runIntCodeProgram(intCodesCopy, k , j)
            if(result == 19690720):
                print(result , k , j)
                print(100* k +j)
                sys.exit()
    print(opcodes[0])
    #print(opcodes)

