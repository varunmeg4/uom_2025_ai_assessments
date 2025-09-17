def print_christmas_tree(height):
    if height < 1:
        print("Height must be at least 1.")
        return
    # Print the tree leaves
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    # Print the trunk
    trunk_width = height // 3 if height > 3 else 1
    trunk_height = max(1, height // 4)
    trunk_spaces = ' ' * (height - trunk_width // 2 - 1)
    for _ in range(trunk_height):
        print(trunk_spaces + '|' * trunk_width)

if __name__ == "__main__":
    try:
        h = int(input("Enter the height of the Christmas tree: "))
        print_christmas_tree(h)
    except ValueError:
        print("Please enter a valid integer.")