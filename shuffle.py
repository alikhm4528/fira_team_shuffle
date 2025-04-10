#!/usr/bin/python3

import random
import math
import sys
import os

def shuffle_file(input_file, iterations):
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        return

    with open(input_file, "r") as file:
        lines = [line for line in (l.strip() for l in file) if line]

    if not lines:
        print(f"Warning: The file '{input_file}' is empty.")
        return
    
    print(f"Shuffling {len(lines)} non-empty lines {iterations} times...\n")

    if iterations >= 10:
        for i in range(1, iterations + 1):
            random.shuffle(lines)
            if (i) % (int(iterations/10)) == 0 or i == iterations:
                print(f"[{int(i/iterations*100)}/100] Shuffle complete")
    else:
        for i in range(iterations):
            random.shuffle(lines)
        print("[100/100] Shuffle complete")

    output_file = f"shuffled_{os.path.basename(input_file)}"
    with open(output_file, "w") as file:
        for line in lines:
            file.write(line + "\n")

    print(f"Successfully shuffled {len(lines)} lines.")
    print(f"Shuffled content saved to '{output_file}'.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python shuffle.py <input_file> <iterations>")
    else:
        shuffle_file(sys.argv[1], int(sys.argv[2]))

