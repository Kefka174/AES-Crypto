# AES Midterm Project - Andrew Larson
# ECE 5995:0002 Spring 2020

sbox = (0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
        0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
        0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
        0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
        0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
        0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
        0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
        0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
        0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
        0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
        0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
        0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
        0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
        0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
        0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
        0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16)

invSbox = (0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
           0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
           0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
           0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
           0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
           0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
           0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
           0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
           0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
           0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
           0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
           0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
           0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
           0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
           0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
           0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D)

mixColConstant = [[0x02, 0x03, 0x01, 0x01],
                  [0x01, 0x02, 0x03, 0x01],
                  [0x01, 0x01, 0x02, 0x03],
                  [0x03, 0x01, 0x01, 0x02]]

mixColInvConstant = [[0x0e, 0x0b, 0x0d, 0x09],
                     [0x09, 0x0e, 0x0b, 0x0d],
                     [0x0d, 0x09, 0x0e, 0x0b],
                     [0x0b, 0x0d, 0x09, 0x0e]]

roundCo = (0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36)

def genRoundKeys(key): # takes in key(hex/string) and generates the round keys
    roundKeys = ['']
    words = []
    for i in range(4): # the first four words (the first key) is the same as the original key
        words.append(key[(8*i):(8*i)+8])
        roundKeys[0] += words[i]
    for i in range(1,11):
        words.append((hex(int(words[4*(i-1)],16) ^ int(g(words[(4*i)-1], i),16)))[2:]) # the first word uses the g() function and the previous key's word3, [2:] to remove '0x'
        for j in range (1,4): # the last 3 words are just XORed with the previous word
            t = (hex(int(words[(4*i)+j-1],16) ^ int(words[4*(i-1)+j],16)))[2:]
            if (len(t) < 8): t = '0'*(8-len(t)) + t
            words.append(t)
        roundKeys.append(words[4*i] + words[4*i+1] + words[4*i+2] + words[4*i+3]) # add the new key to the round key list
    return roundKeys

def g(word, roundInt): # takes in a word(hex/string) and the round number to run the g() function in key generation
    v = []
    for i in range(4): # splits the word into 4 bytes
        v.append(int(word[2*i:2*i+2],16))
    v.append(v.pop(0)) # moves the first byte to the end
    for i in range(4): # runs the bytes through the sbox
        v.append(sbox[v.pop(0)])
    v[0] = (v[0] ^ roundCo[roundInt]) # XOR the first byte with the round coefficient
    ret = ''
    for i in range(4): # combine the 4 bytes into one word
        if (v[i] < 0x10):
            ret += '0'
        ret += hex(v[i])[2:]
    return ret

def subBytes(matrix):
    for i in range(4):
        for j in range(4):
            matrix[i][j] = hex(sbox[int(matrix[i][j],16)])

def invSubBytes(matrix):
    for i in range(4):
        for j in range(4):
            matrix[i][j] = hex(invSbox[int(matrix[i][j],16)])


def shiftRowLeft(row, amount): # takes in matrix row to shift and how many positionts to shift it by
    for i in range(amount):
        row.append(row.pop(0))

def mixColumns(matrix): # takes in matrix and mixes the columns
    c = [[],[],[],[]] 
    for i in range(4): # loop through matrix columns
        for j in range(4): # loop through mixColConstant rows
            t = hex(gMultiply(mixColConstant[j][0], matrix[0][i]) ^ 
                    gMultiply(mixColConstant[j][1], matrix[1][i]) ^
                    gMultiply(mixColConstant[j][2], matrix[2][i]) ^
                    gMultiply(mixColConstant[j][3], matrix[3][i]))
            if (int(t, 16) < 0x10): c[j].append('0x0' + str(t)[2:]) # add a second digit if t is only one digit
            else: c[j].append(t)
    return c

def invMixColumns(matrix): # takes in matrix and inverse mixes the columns
    b = [[],[],[],[]] 
    for i in range(4): # loop through matrix columns
        for j in range(4): # loop through mixColConstant rows
            t = hex(gMultiply(mixColInvConstant[j][0], matrix[0][i]) ^ 
                    gMultiply(mixColInvConstant[j][1], matrix[1][i]) ^
                    gMultiply(mixColInvConstant[j][2], matrix[2][i]) ^
                    gMultiply(mixColInvConstant[j][3], matrix[3][i]))
            if (int(t, 16) < 0x10): b[j].append('0x0' + str(t)[2:]) # add a second digit if t is only one digit
            else: b[j].append(t)
    return b

def gMultiply(a, b): # takes in a constant (a) and byte (b) and does a polynomial multiplication between the two
    b = int(b,16)
    if (a == 0x01): return b
    elif (a == 0x02):
        if (b*2 <= 0xff): return b*2 # shift left one bit
        else: return b*2 ^ 0x11b # if result is larger than 8 bits it is divided by P(x) for GF(2^8)
    elif (a == 0x03): 
        c = (b * 2) ^ b
        if (c <= 0xff): return c # shift left one bit and add original byte
        else: return c ^ 0x11b # if result is larger than 8 bits it is divided by P(x) for GF(2^8)
    else:
        # convert hex to binary lists
        aStr = ''
        bStr = ''
        while a > 0: 
            aStr = str(a % 2) + aStr 
            a = a >> 1 
        while b > 0: 
            bStr = str(b % 2) + bStr 
            b = b >> 1 
        if (len(bStr) < 8): bStr = '0'*(8-len(bStr)) + bStr # add zeroes removed from string conversion
        tol = [0]*11
        for i in range(4): # polynomial multiplication
            for j in range(8):
                tol[i+j] += int(aStr[i])*int(bStr[j])
                if (tol[i+j] == 2): tol[i+j] = 0
        t = 0
        if (tol[0] or tol[1] or tol[2]): # mod P(x) if the multiplication result is bigger than 0xff
            to = mod(list(reversed(tol)), [1,1,0,1,1,0,0,0,1])
            for i in range(len(to)): # convert from list to int
                t += (2**i)*to[i]
        else:
            for i in range(11): # convert from list to int
                t += (2**(10-i))*int(tol[i])
        return t

def mod(numerator, denominator): # takes in polynomial(coefficient list) and P(x) to calculate num mod P(x)
    sl = len(numerator) - len(denominator)
    denominator = [0] * sl + denominator
    for i in range(sl + 1):
        mul = numerator[-1]
        if mul != 0:
            d = [mul * u for u in denominator]
            numerator = [abs(u - v) for u, v in zip(numerator, d)]
        numerator.pop()
        denominator.pop(0)
    return numerator

def keyAddition(matrix, key):
    keyMat = stringToMatrix(key)
    for j in range(4):
        for k in range(4):
            t = hex(int(matrix[j][k],16) ^ int(keyMat[j][k],16)) #xor
            if (int(t,16) < 0x10): matrix[j][k] = '0x0' + t[2:] #make single digits 2 digit
            else: matrix[j][k] = t

def encrypt(plainText, key, verbose=False):
    if(validate(plainText, key)):
        roundKeys = genRoundKeys(key) # generate round keys
        if (verbose): print('round[0].input\t' + plainText)
        plainText = hex(int(plainText,16) ^ int(roundKeys[0],16))[2:] # initial key addition layer
        if (verbose): print('round[0].k_sh\t' + roundKeys[0])
        matrix = stringToMatrix(plainText)
        for i in range(1,11): # loop through the 10 rounds
            if (verbose): print('round[' + str(i) + '].start\t' + matrixToString(matrix))
            subBytes(matrix)
            if (verbose): print('round[' + str(i) + '].s_box\t' + matrixToString(matrix))
            shiftRowLeft(matrix[1],1)
            shiftRowLeft(matrix[2],2)
            shiftRowLeft(matrix[3],3)
            if (verbose): print('round[' + str(i) + '].s_row\t' + matrixToString(matrix))
            if (i != 10): 
                matrix = mixColumns(matrix) # won't mix columns on round 10
                if (verbose): print('round[' + str(i) + '].m_col\t' + matrixToString(matrix))
            keyAddition(matrix, roundKeys[i])
            if (verbose): print('round[' + str(i) + '].k_sch\t' + roundKeys[i])
        if (verbose): print('round[10].output\t' + matrixToString(matrix))
        return matrixToString(matrix)

def decrypt(cipherText, key, verbose=False):
    if(validate(cipherText, key)):
        roundKeys = genRoundKeys(key) # generate round keys
        if (verbose): print('round[0].iinput\t' + cipherText)
        if (verbose): print('round[0].ik_sch\t' + roundKeys[10])
        matrix = stringToMatrix(cipherText)
        for i in range(10):
            keyAddition(matrix, roundKeys[10-i])
            if (verbose and i > 0): print('round[' + str(i) + '].ik_add\t' + matrixToString(matrix))
            if (i != 0): matrix = invMixColumns(matrix) #won't mix columns on inv round 1
            if (verbose): print('round[' + str(i+1) + '].istart\t' + matrixToString(matrix))
            shiftRowLeft(matrix[1],3)
            shiftRowLeft(matrix[2],2)
            shiftRowLeft(matrix[3],1)
            if (verbose): print('round[' + str(i+1) + '].is_row\t' + matrixToString(matrix))
            invSubBytes(matrix)
            if (verbose): print('round[' + str(i+1) + '].is_box\t' + matrixToString(matrix))
            if (verbose): print('round[' + str(i+1) + '].ik_sch\t' + roundKeys[9-i])
        keyAddition(matrix, roundKeys[0])
        if (verbose): print('round[10].ioutput\t' + matrixToString(matrix))
        return matrixToString(matrix)

def stringToMatrix(string): # converts string to matrix
    m = []
    string = str(string)
    if (len(string) < 32):
        string = '0'*(32-len(string)) + string
    for i in range(4):
        m.append([string[2*i:2*i+2], string[2*i+8:2*i+10], string[2*i+16:2*i+18], string[2*i+24:2*i+26]])
    return m

def matrixToString(matrix): # converts matrix to string
    s = ''
    for i in range(4):
        if(len(matrix[0][0]) > 2): s += matrix[0][i][2:] + matrix[1][i][2:] + matrix[2][i][2:] + matrix[3][i][2:]
        else: s += matrix[0][i] + matrix[1][i] + matrix[2][i] + matrix[3][i]
    return s

def validate(text, key):
    try:
        int(text,16)
        int(key,16)
        if (len(text) < 32):
            print('currently only a full 128bit block of hex text is supported')
            return False
        elif (len(key) < 32):
            print('currently only a full 128bit hex block key is supported')
            return False
        return True
    except:
        print('Currently only 128bit hex block of text and key are supported')
        return False