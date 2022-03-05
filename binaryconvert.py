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