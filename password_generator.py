import argparse
import random
import string
import sys

# Arguments
parser = argparse.ArgumentParser(prog='Password Generator', description='Use to generate a random string for a password')

parser.add_argument('length', type=int, help='The length of the string returned')
parser.add_argument('--fullRandom', action='store_true', help='Removes requirement of at least one character type')
parser.add_argument('--noDigits', action='store_true', help='No digits')
parser.add_argument('--noUppercase', action='store_true', help='No uppercase characters')
parser.add_argument('--noLowercase', action='store_true', help='No lowercase characters')
parser.add_argument('--noSpecial', action='store_true', help='No special characters')

# Specific special character exclusion
parser.add_argument('--noExclamation', action='store_true', help='No exclamation mark')
parser.add_argument('--noAt', action='store_true', help='No at sign')
parser.add_argument('--noHash', action='store_true', help='No hash sign')
parser.add_argument('--noDollar', action='store_true', help='No dollar')
parser.add_argument('--noPercent', action='store_true', help='No percent')
parser.add_argument('--noCaret', action='store_true', help='No caret')
parser.add_argument('--noAmpersand', action='store_true', help='No ampersand')
parser.add_argument('--noAsterisk', action='store_true', help='No asterisk')

args = parser.parse_args()

if args.length < 1:
  sys.exit('Length should be a positive number')

allCharacters = ''

if not args.noLowercase:
  allCharacters += string.ascii_lowercase

if not args.noUppercase:
  allCharacters += string.ascii_uppercase

if not args.noDigits:
  allCharacters += string.digits

# Check special characters
specialCharacters = ''
if not args.noSpecial:
  if not args.noExclamation:
    specialCharacters += '!'
  if not args.noAt:
    specialCharacters += '@'
  if not args.noHash:
    specialCharacters += '#'
  if not args.noDollar:
    specialCharacters += '$'
  if not args.noPercent:
    specialCharacters += '%'
  if not args.noCaret:
    specialCharacters += '^'
  if not args.noAmpersand:
    specialCharacters += '&'
  if not args.noAsterisk:
    specialCharacters += '*'
  
  allCharacters += specialCharacters

if not bool(allCharacters):
  sys.exit('You disallowed all characters!')


needsSpecial = not args.noSpecial and bool(specialCharacters)
needsDigit = not args.noDigits
needsLowercase = not args.noLowercase
needsUppercase = not args.noUppercase

needsShuffle = False

# Gather comparator based on how many are required
comparator = needsSpecial + needsDigit + needsLowercase + needsUppercase

randomList = list()
length = args.length

# If the length is greater than or equal to the comparator, append random characters and guarantee one of each type
if length >= comparator and not args.fullRandom:
  while length > 0:
    # If less or equal to comparator, choose random character from the necessary list
    if length <= comparator:
      if needsSpecial:
        randomCharacter = random.choice(specialCharacters)
      elif needsDigit:
        randomCharacter = random.choice(string.digits)
      elif needsLowercase:
        randomCharacter = random.choice(string.ascii_lowercase)
      elif needsUppercase:
        randomCharacter = random.choice(string.ascii_uppercase)
      
      needsShuffle = True
    else:
      randomCharacter = random.choice(allCharacters)

    # Check if one of the unused required types
    if needsSpecial and randomCharacter in specialCharacters:
      needsSpecial = False
      comparator -= 1
    elif needsDigit and randomCharacter in string.digits:
      needsDigit = False
      comparator -= 1
    elif needsLowercase and randomCharacter in string.ascii_lowercase:
      needsLowercase = False
      comparator -= 1
    elif needsUppercase and randomCharacter in string.ascii_uppercase:
      needsUppercase = False
      comparator -= 1
    
    randomList += randomCharacter
    length -= 1
# Otherwise just get the result back with no guarantees
else:
  randomList += random.choices(allCharacters, k = args.length)

# Since the comparator logic isn't random, use shuffle to make it random
if needsShuffle:
  random.shuffle(randomList)

randomString = ''.join(randomList)

print(randomString)