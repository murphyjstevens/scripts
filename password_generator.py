import argparse
import random
import string

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', type=int)
parser.add_argument('--noSpecial', action='store_true')
parser.add_argument('--noDigits', action='store_true')
parser.add_argument('--noUppercase', action='store_true')
parser.add_argument('--noLowercase', action='store_true')
args = parser.parse_args()

allCharacters = ''

if not args.noLowercase:
  allCharacters += string.ascii_lowercase

if not args.noUppercase:
  allCharacters += string.ascii_uppercase

if not args.noDigits:
  allCharacters += string.digits

specialCharacters = '!@#$%^&*'

if not args.noSpecial:
  allCharacters += specialCharacters

randomString = random.choices(allCharacters, k = args.length)

result = ''.join(randomString)
print(result)