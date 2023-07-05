def star_pattern_pyramid(rows):
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

# Example usage
num_rows = 10
star_pattern_pyramid(num_rows)
