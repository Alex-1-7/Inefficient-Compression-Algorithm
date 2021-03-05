import numpy as np

#This solution uses a 2D array of size [128][2] to store the frequency of all ascii characters in the string.
#Therefore this solution will only work for base 128 ascii characters since I use the 0-127 indices of the
#array to corespond to the 128 ascii values.
#This 2D array is then sorted, using a stable sort, by the frequency column and this ordering of ascii values
#is used as a key to compress and decompress the text.

#Note: My solution gives a slightly different result to the expected result. But I believe this is because of
#variations in the compression due to some characters appearing the same number of times. To try to minimise the
#variations I used a stable sort so all characters of the same frequency will appear in the order of their ascii values.

def Compress(text):
    char_freq = np.zeros([128,2], dtype = int)
    for x in range (0 ,128):
        char_freq[x][0] = x
    for x in text:
        y = ord(x)
        char_freq[y][1] -= 1 #-1 so sort is in descending order
    char_freq = char_freq[char_freq[:,1].argsort(kind ='stable')] #Sort the list to get most common character at the top
    #A stable sort is used for consistency when characters appear with the same frequency
    key1 = [0]*128
    for x in range(0, 128):
        key1[x] = char_freq[x][0] #Stores order of characters by frequency, so key1[2] = ascii value of the second most common character
    key = [0]*128
    for x in range (0, 128):
        key[key1[x]] = x #Stores the position in the ordered list indexed by ascii value, so key[32] = the position of character with ascii value 32 in the list of order characters
    compressed_text = ""
    for x in text:
        compressed_text += get_compression_value(key, x)
    return compressed_text, key1

#Computes compression value for each character
def get_compression_value(key, ascii_value):
    value = ""
    freq_order = key[ord(ascii_value)]
    while (freq_order > 14):
        freq_order -= 15
        value += 'f'
    if (freq_order > 9):
        if (freq_order == 10):
            value += 'a'
        if (freq_order == 11):
            value += 'b'
        if (freq_order == 12):
            value += 'c'
        if (freq_order == 13):
            value += 'd'
        if (freq_order == 14):
            value += 'e'
    else:
        value += str(freq_order)
    return value

def Decompress(compressed_text, key):
    temp = ''
    text = ''
    temp_is_word = False
    for x in compressed_text:
        temp += x
        if (x != 'f'):
            temp_is_word = True; #Set to true when a compression word is fully read, e.g 5, f0, ff3
        if (temp_is_word):
            temp_value = get_decompressed_value(temp, key)
            text += temp_value
            temp = ''
            temp_is_word = False
    return text

#Computes the ascii value of the character from its compression value and the key used to compress it
def get_decompressed_value(temp, key):
    temp_value = 0
    for x in temp:
        if (x == 'a'):
            temp_value += 10
        elif (x == 'b'):
            temp_value += 11
        elif (x == 'c'):
            temp_value += 12
        elif (x == 'd'):
            temp_value += 13
        elif (x == 'e'):
            temp_value += 14
        elif (x == 'f'):
            temp_value += 15
        else:
            temp_value += int(x)

    value = chr(key[temp_value])

    return value


text = "Marley was dead: to begin with. There is no doubt whatever about that. The register of his burial was signed by the clergyman, the clerk, the undertaker, and the chief mourner. Scrooge signed it: and Scrooge's name was good upon 'Change, for anything he chose to put his hand to. Old Marley was as dead as a door-nail. Mind! I don't mean to say that I know, of my own knowledge, what there is particularly dead about a door-nail. I might have been inclined, myself, to regard a coffin-nail as the deadest piece of ironmongery in the trade. But the wisdom of our ancestors is in the simile; and my unhallowed hands shall not disturb it, or the Country's done for. You will therefore permit me to repeat, emphatically, that Marley was as dead as a door-nail."

print (text)
print ("")
compressed_text, key = Compress(text)
print ("Compressed text:")
print (compressed_text)
print ("")
text = Decompress(compressed_text, key)
print ("Decompressed text:")
print (text)
