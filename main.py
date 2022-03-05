import binaryconvert

eightBitMode = False
signedMode = True


def main():
    print("Welcome to binar")

    value = 0

    usr_input(value)



def usr_input(value):
    print("Enter: bin, num, val, settings, exit")
    choice = input()
    global eightBitMode
    global signedMode

    if choice == "bin":
        print("Enter a number in binary: ")
        binary_input(value)
    elif choice == "num":
        print("Enter a number as an integer: ")
        num_input(value)
    elif choice == "val":
        print_val(value)
    elif choice == "8t":
        print("Now in 8-bit mode.")
        eightBitMode = True
        value = 0
        usr_input(value)
    elif choice == "8f":
        print("8-bit mode deactivated")
        eightBitMode = False
        value = 0
        usr_input(value)
    elif choice == "settings":
        print("")
        print("8-Bit mode: " + eightBitMode.__str__())
        print("Signed byte mode: " + signedMode.__str__())
        print("")
        usr_input(value)
    elif choice == "sf":
        print("Now in unsigned mode")
        signedMode = False
        value = 0
        usr_input(value)
    elif choice == "st":
        print("Now in signed mode")
        signedMode = True
        value = 0
        usr_input(value)
    elif choice == "exit":
        exit()
    else:
        print("Error invalid input")
        usr_input(value)

def print_val(value):
    print("")

    if signedMode == True:
        print("Size: " + binaryconvert.get_bytes_size(value, True).__str__() + " bytes")
    elif signedMode == False:
        print("Size: " + binaryconvert.get_bytes_size(value, False).__str__() + " bytes")

    print("Integer value: " + value.__str__())

    bin_list = bin_string(value)
    print("Binary value: " + bin_list)

    print("Hex value: " + hex(value))

    print("")
    usr_input(value)


def num_input(value):
    numVal = input()

    operator = numVal[0]

    if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "^":
        numVal = numVal[1:]
        numVal = int(numVal)
        value = do_math(value, operator, numVal)
        print("=" + bin_string(value))
        num_input(value)
    elif operator == "=":
        print("=" + value.__str__())
        num_input(value)
    elif operator == "c":
        value = 0
        print("=" + bin_string(value))
        num_input(value)
    elif operator == "x":
        usr_input(value)
    else:
        print("Error invalid input")
        num_input(value)

    usr_input(value)

def binary_input(value):

    bytesList = []
    binary = input()

    binary_list = list(binary)
    binary_list.reverse()

    operator = binary_list.pop()

    binString = "".join(binary_list)
    bytesList.append(binString)

    if binString != "":
        if signedMode == False:
            usrInput = binaryconvert.bin_to_num(bytesList, False)
        elif signedMode == True:
            usrInput = binaryconvert.bin_to_num(bytesList, True)
        else:
            usrInput = None


    if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "^":
        value = do_math(value, operator, usrInput)
        print("=" + bin_string(value))
        binary_input(value)
    elif operator == "=":
        print("=" + value.__str__())
        binary_input(value)
    elif operator == "c":
        value = 0
        print("=" + bin_string(value))
        binary_input(value)
    elif operator == "x":
        usr_input(value)
    else:
        print("Error invalid input")
        binary_input(value)

def do_math(value, operator, input):
    if operator == "+":
        value = value + input
    elif operator == "-":
        value = value - input
    elif operator == "*":
        value = value * input
    elif operator == "^":
        value = value ** input
    elif operator == "/":
        if value % input == 0:
            value = value / input
            value = int(value)
        elif value % input != 0:
            print("Warning loss of precision")
            value = value / input
            value = int(value)

    if eightBitMode == True:
        value = overflow(value)

    return value
def overflow(value):
    if value >= 256:
        print("Warning positive integer overflow")
        value = value % 256
        return value
    elif value < 0:
        print("Warning negative integer overflow")
        value = 256 + value
        return value
    else:
        return value



def bin_string(value):

    if signedMode == False:
        byteList = binaryconvert.num_to_bin(value, False)
    elif signedMode == True:
        byteList = binaryconvert.num_to_bin(value, True)
    else:
        byteList = None


    bytes = ""

    for i in range(len(byteList)):
        bytes = bytes + byteList[i] + " "

    binaryList = list(bytes)

    binaryList = "".join(binaryList)

    return binaryList
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

