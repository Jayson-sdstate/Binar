def num_to_bin(value, signed):
    if not signed and value < 0:
        value = value * -1
        sign = None
    elif signed and value < 0:
        sign = False
        value = value * -1
    elif signed and value > 0:
        sign = True
    else:
        sign = None
    bin_list = []
    byteList = []
    temp_val = value
    remainder = True

    if signed:
        count = (get_bytes_size(value, True) * 8) - 1
    elif not signed:
        count = (get_bytes_size(value, False) * 8) - 1

    if signed and sign:
        bin_list.append("1")
        count -= 1
    elif signed and not sign:
        bin_list.append("0")
        count -= 1
    if temp_val == 0:
        for i in range(8):
            bin_list.append("0")
    else:
        while remainder == True:
            if temp_val > 2 ** count:
                bin_list.append("1")
                temp_val = temp_val - (2 ** count)
                count -= 1
            elif temp_val < 2 ** count:
                bin_list.append("0")
                count -= 1
            elif temp_val == 2 ** count:
                bin_list.append("1")
                for i in range(count):
                    bin_list.append("0")
                remainder = False

    # bin_list = "".join(bin_list)
    temp_list = []
    c = 0
    for i in range(len(bin_list)):
        temp_list.insert(c, bin_list[i])
        if c == 7:
            temp_string = "".join(temp_list)
            byteList.append(temp_string)
            temp_list.clear()
            c = -1

        c += 1

    return byteList


def bin_to_num(bytesList, signed):
    bytes = ""

    for i in range(len(bytesList)):
        bytes = bytes + bytesList[i]

    binaryList = list(bytes)

    if signed == True:
        sign = binaryList.pop(0)
    else:
        sign = None

    count = 0
    num_val = 0
    binaryList.reverse()
    for i in binaryList:
        if i == "1":
            num_val = num_val + (2 ** count)
        count += 1

    if signed == True:
        if sign == "0":
            num_val = num_val * -1

    return num_val


def get_bytes_size(value, signed):
    count = 1
    is_cal = False

    if value < 0:
        value = value * -1

    if not signed:
        while not is_cal:
            if value < 2 ** (8 * count):
                bytes = count
                is_cal = True
            else:
                count += 1
    elif signed:
        while not is_cal:
            if value < 2 ** (7 * count):
                bytes = count
                is_cal = True
            else:
                count += 1

    return bytes


# splits binary integers into binary character values
def num_to_char(bytesList):
    number = bin_to_num(bytesList, False)

    num_list = num_to_list(number)
    char_list = []
    binary_list = []

    # adding 48 to integer values gives the proper value for an ascii character
    for i in num_list:
        char_list.append(i + 48)

    for i in char_list:
        char = num_to_bin(i,False)
        charString = char[0]
        binary_list.append(charString)

    return binary_list


def char_to_num(bytesList):
    numList = []

    for i in bytesList:
        number = bin_to_num(i, False) - 48
        numList.append(number)

    value = list_to_num(numList)

    binary_list = num_to_bin(value, False)

    return binary_list


# converts a list of single digit integers a single integer value
# [1,2,3] = 123
def list_to_num(numList):
    value = 0

    count = len(numList) - 1
    for i in range(len(numList)):
        value = value + (numList[i] * 10 ** count)
        count -= 1

    return value


def num_to_list(value):
    num_list = []

    # splits integer into list of ints for each digit place
    for i in range(get_digits(value)):
        temp_num = value % 10
        value = value - temp_num
        value = value / 10
        num_list.append(int(temp_num))

    num_list.reverse()

    return num_list


# gets the number of digit in an integer value
def get_digits(value):
    # makes negatives positive
    if value < 0:
        value = value * -1
    is_cal = False
    digits = 0

    while not is_cal:
        if value > (10 * 10) ** (0.5 * digits) - 1:
            digits += 1
        else:
            is_cal = True

    return digits

# accepts a list of binary bytes, and turns it into a string seperated by bytes
def bytelist_to_bytestring(byteList):

    bytes = ""

    for i in range(len(byteList)):
        bytes = bytes + byteList[i] + " "

    binaryList = list(bytes)

    binaryList = "".join(binaryList)

    return bytes