import argparse
import csv
import random
import sys

# Arguments
parser = argparse.ArgumentParser(prog='Biography Generator', description='Generates a random biography for a given name')

parser.add_argument('name', type=str, help='The name of the person')

args = parser.parse_args()

activities = list()

with open('csv/interests.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

for item in data:
    activities.append(item[0])

selectedActivities = random.sample(activities, k=2)

print(f'{args.name} adores {selectedActivities[0]} and {selectedActivities[1]}!')