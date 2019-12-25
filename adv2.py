with open('advcode2.txt') as fp:
    opcodesString = fp.readline().split(',')
    opcodes = []
    for s in opcodesString:
        opcodes.append(int(s))
    i = 0
    #print(opcodes)
    #print(len(opcodes))
    opcodes[1] = 12
    opcodes[2] = 2
    while i < len(opcodes):
        opcode = opcodes[i]
        op1 = opcodes[i+1]
        op2 = opcodes[i+2]
        res = opcodes[i+3]
        if opcode == 1:
            opcodes[res] = opcodes[op1] + opcodes[op2]
        elif opcode == 2:
            opcodes[res] = opcodes[op1] * opcodes[op2]
        elif opcode == 99:
            break
        i += 4
        #print(i)
    print(opcodes[0])
    #print(opcodes)

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