#!/usr/bin/env python3

with open('english.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

converted_data = []
for line in lines:
    # Splitting the line and checking if it has exactly two elements
    parts = line.strip().split(',')
    if len(parts) == 2:
        word, emoji = parts
        converted_data.append(f'("{word}", "{emoji}")')
    else:
        print(f"Skipping line: {line.strip()}")  # Optional warning message

output_data = ', '.join(converted_data)

with open('converted_english.txt', 'w', encoding='utf-8') as file:
    file.write(output_data)
