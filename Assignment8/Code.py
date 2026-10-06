input_file = input("Enter the input file name: ")
with open(input_file, "r") as file:
    lines = file.readlines()

line_count = len(lines)
first_two_lines = lines[:2]

output_file = "output.txt"
with open(output_file, "w") as file:
    file.writelines(first_two_lines)
    
print("Total number of lines:", line_count)
print("First two lines:")
print("".join(first_two_lines))
print("Extracted data has been written to", output_file)