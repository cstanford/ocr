'''
' Name: Connor Stanford
' Date: Mon Jul 10, 2017
' I certify that this work is mine alone. 
'
' Requirements: Python 3.6.0
' Usage: 
'       * Open cmd or terminal
'           - Unix:     $ python3 ocr.py
'           - Windows:  $ py ocr.py
'           - That's it!
'       * Pass a filename as an optional arg
'           - python3 ocr.py <filename>
'
'''

import argparse
from collections import deque
import pprint


ACCOUNT_NUMBER_LENGTH = 9

'''
' Binary representations of each possible account number.
' Spaces (' ') are mapped to '0'. Pipes and bars ('|', '_') are mapped to 1.
'
' Ex: let ZERO = the figure below:
'
'       ' _ '  -> space, bar, space ->  0,1,0 -> S0
'       '| |'  -> pipe, space, pipe ->  1,0,1 -> S1
'       '|_|'  -> pipe, bar, pipe   ->  1,1,1 -> S2
'
'       ZERO = S0 + S1 + S2 = '010101111'
'
'''
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


'''
' Each account number consists of 3 lines: 
'
'   line1: [0,1,0,1,0,1,1,1,1]
'   line2: [1,0,1,1,1,1,1,1,1]
'   line3: [1,1,1,0,0,0,0,1,1]
'
'   popleft() each line three times to get the binary sequence of the corresponding entry:
'
'   -> s0 = line1.popleft() += line1.popLeft() += line1.popleft() -> 0,1,0
'   -> s1 = line2.popleft() += line2.popLeft() += line2.popleft() -> 1,0,1
'   -> s2 = line3.popleft() += line3.popLeft() += line3.popleft() -> 1,1,1
'
'   resultSeq = s0 += s1 += s2 -> 0,1,0,1,0,1,1,1,1
'
'''
def getBinarySequenceToCorrespondingEntryByLine(account_num_line):
    try:
        s0 = account_num_line.popleft()     # O(1)
        s1 = account_num_line.popleft()
        s2 = account_num_line.popleft()        
        account_num_entry = s0 + s1 + s2
        return account_num_entry
    except IndexError:
        print('\nUnable to parse account number. Attempted dequeue of empty queue.\n')
        exit()


def getCheckSum(account_number, iterator, acc):

        # account number:  3  4  5  8  8  2  8  6  5
        # position names:  d9 d8 d7 d6 d5 d4 d3 d2 d1
        # checksum calculation:
        # (d1+2*d2+3*d3 +..+9*d9) mod 11 = 0

        entry = int(account_number[ACCOUNT_NUMBER_LENGTH - iterator])
        acc += entry * iterator
        if iterator is 9:
            print('Check Sum Calculated: {}'.format(acc))
            return acc

        return getCheckSum(account_number, iterator + 1, acc)


def validateAcctNum(account_number):
    check_sum = getCheckSum(account_number, 1, 0)
    account_number_is_valid = check_sum % 11 is 0
    print('Account Number is Valid: {}'.format(account_number_is_valid))       
    return account_number_is_valid


def parseAccountNum(top_account_num_line, mid_account_num_line, bottom_account_num_line):

    print('\nAccount Sequence Read:')
    pprint.pprint(top_account_num_line.replace('\n',''))
    pprint.pprint(mid_account_num_line.replace('\n',''))
    pprint.pprint(bottom_account_num_line.replace('\n',''))

    # 1. Map each account_num_line to its corresponding binary sequence.
    # 2. Filter out any values that were not mapped successfully.
    #       - Post mapCharToBinraySequence(), each account_num_line may contain 'None' values due to it containing entries
    #         such as '\n', '\r', ect..., so we filter them out. 
    # 3. Place the result of (2) in a queue.
    top_account_num_line = deque(filter(lambda char: char is not None, (mapCharToBinarySequence(char) for char in top_account_num_line)))
    mid_account_num_line = deque(filter(lambda char: char is not None, (mapCharToBinarySequence(char) for char in mid_account_num_line)))
    bottom_account_num_line = deque(filter(lambda char: char is not None, (mapCharToBinarySequence(char) for char in bottom_account_num_line)))

    account_number = ['','','','','','','','','']

    for index, entry in enumerate(account_number):
        entry = getBinarySequenceToCorrespondingEntryByLine(top_account_num_line)
        entry += getBinarySequenceToCorrespondingEntryByLine(mid_account_num_line)
        entry += getBinarySequenceToCorrespondingEntryByLine(bottom_account_num_line)
        if (entry in account_num_map):
            account_number[index] = account_num_map[entry]
        else:
            print('Unable to parse account number. Binary sequence {} does not exist in account_num_map.\n'.format(entry))
            account_number[index] = None
    
    print('\nParsed Account Number: ' + ''.join(account_number))
    return account_number        


def initiateNeitherIngeniousNorInfallibleManchine():

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', type=argparse.FileType('r'), default='ocr.txt')
    args = parser.parse_args()    
    in_file = args.filename

    valid_account_numbers_found = []
    invalid_account_numbers_found = []
    total_account_numbers_found = 0

    while in_file:

        top_account_num_line = in_file.readline()
        mid_account_num_line = in_file.readline()
        bottom_account_num_line = in_file.readline()

        if not top_account_num_line or not mid_account_num_line or not bottom_account_num_line: break

        account_number = parseAccountNum(top_account_num_line, mid_account_num_line, bottom_account_num_line)
        acccount_number_is_valid = validateAcctNum(account_number)

        if (acccount_number_is_valid):
            valid_account_numbers_found.append(account_number)
        else:
            invalid_account_numbers_found.append(account_number)
        
        total_account_numbers_found += 1
        in_file.readline()  # Burn the empty line seperating account numbers


    print('\n\nTotal Account Numbers Found: {}'.format(total_account_numbers_found))
    print('\nValid Account Numbers Found: ')
    for index, entry in enumerate(valid_account_numbers_found):
        print('{}: '.format(index + 1) + ''.join(entry))

    print('\nInvalid Account Numbers Found: ')
    for index, entry in enumerate(invalid_account_numbers_found):
        print('{}: '.format(index + 1) + ''.join(entry))

    print('\n\n')

    ambulance_ascii_art = '''          
       o_______________}o{          
       |              |   \         
       |   Acadian    |____\_____   
       | _____        |    |_o__ |  
       [/ ___ \       |   / ___ \|  
      []_/.-.\_\______|__/_/.-.\_[] 
         |(O)|             |(O)|    
          '-'               '-'       
    ---   ---   ---   ---   ---   --- '''

    print(ambulance_ascii_art)



initiateNeitherIngeniousNorInfallibleManchine()

