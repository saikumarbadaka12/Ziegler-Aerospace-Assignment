def maskify(mobile_number):
    masked = '#' * (len(mobile_number) - 3) + mobile_number[-3:]
    print(masked)

# Test
maskify("9988776655")  # Output: #######655
