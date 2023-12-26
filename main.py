filename = "program.b#"
register = 0

tape = [0] * 256
index = 0

def truth_machine():
    a = input("Enter: ")
    if a == "1":
        while True:
            print("1")
    elif a == "0":
        print(0)

def evaluate(command):
    global tape
    global index
    global register
    
    match command:
        case "+":
            tape[index] += 1
        case "-":
            tape[index] -= 1
        case ">":
            index += 1
        case "<":
            index -= 1
        case " ":
            pass
        case "\n":
            pass
        case "o":
            print(tape[index])
        case "f":
            print(tape)
        case "i":
            print(index)
        case "p":
            register += 1
        case "l":
            register -= 1
        case "a":
            tape[index] = register
        case "b":
            index = register
        case "c":
            print(register)
        case "d":
            print(chr(tape[index]))
        case "e":
            print(chr(register))
        case "u":
            print(chr(index))
        case "t":
            truth_machine()
        case _:
            print(f"Unrecognized command: {command}")


with open(filename) as f:
    while True:
        char = f.read(1)
        if not char: 
            break
        evaluate(char)