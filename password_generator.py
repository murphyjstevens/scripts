import argparse
import random
import string
import sys

# Arguments
parser = argparse.ArgumentParser(prog='Password Generator', description='Use to generate a random string for a password')

parser.add_argument('length', type=int, help='The length of the string returned')
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



if not args.noSpecial:
  specialCharacters = ''

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

if not allCharacters:
  sys.exit('You disallowed all characters!')

randomString = random.choices(allCharacters, k = args.length)

result = ''.join(randomString)
print(result)