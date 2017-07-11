'''
' Name: Connor Stanford
' Date: Mon Jul 10, 2017
'''

import sys
import pprint

ACCOUNT_NUMBER_LENGTH = 9

ZERO  = '010101111' 
ONE   = '000001001'
TWO   = '010011110'
THREE = '010011011'
FOUR  = '000111001'
FIVE  = '010110011'
SIX   = '010110111'
SEVEN = '010001001'
EIGHT = '010111111'
NINE  = '010111011'

account_num_map = {}
account_num_map[ZERO]  = '0'
account_num_map[ONE]   = '1'
account_num_map[TWO]   = '2'
account_num_map[THREE] = '3'
account_num_map[FOUR]  = '4'
account_num_map[FIVE]  = '5'
account_num_map[SIX]   = '6'
account_num_map[SEVEN] = '7'
account_num_map[EIGHT] = '8'
account_num_map[NINE]  = '9'

def mapCharToBinarySequence(char):
    if (char == '|' or char == '_'):
        return '1'
    elif (char is ' '):
        return '0'

def getAcctNumEntry(account_num_line):
    try:
        d2 = account_num_line.pop() # O(1)
        d1 = account_num_line.pop()
        d0 = account_num_line.pop()
        account_num_entry = d0 + d1 + d2
        return account_num_entry
    except IndexError:
        print('Unable to parse account number. Attempted pop of empty list.\n')
        exit()

def parseAccountNum(top_account_num_line, mid_account_num_line, bottom_account_num_line):

    print('\nAccount Sequence Read:')
    pprint.pprint(top_account_num_line.replace('\n',''))
    pprint.pprint(mid_account_num_line.replace('\n',''))
    pprint.pprint(bottom_account_num_line.replace('\n',''))

    top_account_num_line = list(filter(lambda char: char is not None, (mapCharToBinarySequence(char) for char in top_account_num_line)))
    mid_account_num_line = list(filter(lambda char: char is not None, (mapCharToBinarySequence(char) for char in mid_account_num_line)))
    bottom_account_num_line = list(filter(lambda char: char is not None, (mapCharToBinarySequence(char) for char in bottom_account_num_line)))

    account_number = ['','','','','','','','','']

    for index, entry in enumerate(account_number):
        entry = getAcctNumEntry(top_account_num_line)
        entry += getAcctNumEntry(mid_account_num_line)
        entry += getAcctNumEntry(bottom_account_num_line)
        if (entry in account_num_map):
            account_number[ACCOUNT_NUMBER_LENGTH - index - 1] = account_num_map[entry]
        else:
            print('Unable to parse account number. Binary sequence ' + entry + 'does not exist in account_num_map.\n')
            account_number[ACCOUNT_NUMBER_LENGTH - index - 1] = None
    
    print('\nParsed Account Number: ' + ''.join(account_number) + '\n')
    return account_number        

def main():
    in_file = open(sys.argv[1], 'r')
    account_numbers_found = []
    while in_file:
        top_account_num_line = in_file.readline()
        if not top_account_num_line: break
        mid_account_num_line = in_file.readline()
        bottom_account_num_line = in_file.readline()
        account_number = parseAccountNum(top_account_num_line, mid_account_num_line, bottom_account_num_line)
        account_numbers_found.append(account_number)
        in_file.readline() # burn line


main()
