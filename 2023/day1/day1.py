def find_calibration_value(line):
    # Find all digits in the line
    digits = [int(d) for d in line if d.isdigit()]

    # Check if there are enough digits
    if len(digits) >= 2:
        # Return the combination of the first and last digits
        return digits[0] + digits[-1]
    else:
        # Return 0 if there are not enough digits
        return 0
    # TODO: Test
    # FIXME:


# Initialize the sum
total_sum = 0

# Read the calibration document
with open('day1input.txt', 'r') as file:
    for line in file:
        total_sum += find_calibration_value(line.strip())

# Print the total sum
print(total_sum)
