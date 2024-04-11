import os
import random
import re
import shutil
import subprocess
import argparse


def find_op_position(line):
    numbers = re.findall(r'\d+', line)
    op_position = [int(num) for num in numbers][-2:]
    op_position[1] = op_position[1] - 3
    return op_position


mutant_amount = 10
binary_operators = ('+', '-', '*', '/', '%', '**', '//')

parser = argparse.ArgumentParser(description='mojo-parse')
parser.add_argument('filepath', help='mojo file to parse')
filepath = parser.parse_args().filepath
os.makedirs('mutants', exist_ok=True)

result = subprocess.run(["npx", "tree-sitter", "parse", filepath], stdout=subprocess.PIPE)
stringout = result.stdout.decode("utf-8")

mutant = "binary_operator"

arithmetic_operators = [line for line in stringout.splitlines() if mutant in line]

op_positions = [find_op_position(line) for line in arithmetic_operators]
mutant_ops = []

for op_position in op_positions:
    mutant_ops.append(random.choice(binary_operators))

print(op_positions)

mutant_path = 'mutants/mutant.mojo'
with open(filepath, 'r') as file:
    mutated = file.readlines()

print(mutated)

for idx, pos in enumerate(op_positions):
    mutated_line = mutated[pos[0]]
    mutated_line = mutated_line[:pos[1]] + mutant_ops[idx] + mutated_line[pos[1] + 1:]
    mutated[pos[0]] = mutated_line

print(mutated)

with open(mutant_path, 'w') as file:
    file.writelines(mutated)














