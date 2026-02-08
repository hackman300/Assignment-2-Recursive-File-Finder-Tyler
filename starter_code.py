"""
Recursion Assignment Starter Code
Complete the recursive functions below to analyze the compromised file system.
"""

import os

def sum_list(numbers):
    """
    Recursively calculate the sum of a list of numbers.

    This is your first recursion problem. Think about:
    - Base case: What's the sum of an empty list?
    - Recursive case: If you know the sum of the rest of the list,
      how do you include the first number?

    Args:
        numbers (list): List of numbers to sum

    Returns:
        int: Sum of all numbers in the list

    Example:
        sum_list([1, 2, 3, 4]) should return 10
        sum_list([]) should return 0
    """
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list(numbers[1:])

print("\nTest sum_list:")
print(f"    sum_list([1, 2, 3, 4]) = {sum_list([1, 2, 3, 4])} (expected: 10)")
print(f"    sum_list([]) = {sum_list([])} (expected: 0)")
print(f"    sum_list([5, 5, 5]) = {sum_list([5, 5, 5])} (expected: 15)")

def count_even(numbers):
    """
    Recursively count how many even numbers are in a list.

    This teaches you how to count items that match a condition.
    You'll use this same pattern for counting files!

    Args:
        numbers (list): List of numbers

    Returns:
        int: Count of even numbers in the list

    Example:
        count_even([1, 2, 3, 4, 5, 6]) should return 3
        count_even([1, 3, 5]) should return 0
    """
    if len(numbers) == 0:
        return 0
    if numbers[0] % 2 == 0:
        return 1 + count_even(numbers[1:])
    return count_even(numbers[1:])

print("\nTest count_even:")
print(f"    count_even([1, 2, 3, 4, 5, 6]) = {count_even([1, 2, 3, 4, 5, 6])} (expected: 3)")
print(f"    count_even([1, 3, 5]) = {count_even([1, 3, 5])} (expected: 0)")
print(f"    count_even([2, 4, 6]) = {count_even([2, 4, 6])} (expected: 3)")

def find_strings_with(strings, target):
    """
    Recursively find all strings that contain a target substring.

    This teaches you how to build a list of items that match a condition.
    You'll use this same pattern for finding infected files!

    Args:
        strings (list): List of strings to search
        target (str): Substring to search for

    Returns:
        list: All strings that contain the target substring

    Example:
        find_strings_with(["hello", "world", "help"], "hel")
        should return ["hello", "help"]
    """
    if len(strings) == 0:
        return []
    if target in strings[0]:
        return [strings[0]] + find_strings_with(strings[1:], target)
    return find_strings_with(strings[1:], target)

print("\nTest find_strings_with:")
result = find_strings_with(["hello", "world", "help", "test"], "hel")
print(f"  find_strings_with(['hello', 'world', 'help', 'test'], 'hel') = {result}")
print(f"  (expected: ['hello', 'help'])")

result = find_strings_with(["cat", "dog", "bird"], "z")
print(f"  find_strings_with(['cat', 'dog', 'bird'], 'z') = {result}")
print(f"  (expected: [])")

def count_files(directory_path):
    """
    Recursively count all files in a directory and its subdirectories.

    Args:
        directory_path (str): Path to the directory to analyze

    Returns:
        int: Total number of files in the directory tree

    Example:
        If directory structure is:
        root/
            file1.txt
            file2.txt
            subdir/
                file3.txt

        count_files('root') should return 3
    """
    if os.path.isfile(directory_path):
        return 1
    elif os.path.isdir(directory_path):
        total = 0
        for item in os.listdir(directory_path):
            full_path = os.path.join(directory_path, item)
            total += count_files(full_path)
        return total
    return 0


def find_infected_files(directory_path, extension=".encrypted"):
    """
    Recursively find all files with a specific extension in a directory tree.

    Args:
        directory_path (str): Path to the directory to analyze
        extension (str): File extension to search for (default: ".encrypted")

    Returns:
        list: List of full paths to all files with the specified extension

    Example:
        If directory structure is:
        root/
            normal.txt
            virus.encrypted
            subdir/
                data.encrypted

        find_infected_files('root', '.encrypted') should return:
        ['root/virus.encrypted', 'root/subdir/data.encrypted']
    """
    if os.path.isfile(directory_path):
        if directory_path.endswith(extension):
            return [directory_path]
        return []
    elif os.path.isdir(directory_path):
        infected = []
        for item in os.listdir(directory_path):
            full_path = os.path.join(directory_path, item)
            infected.extend(find_infected_files(full_path, extension))
        return infected
    return []


if __name__ == "__main__":
    print("RECURSION ASSIGNMENT - STARTER CODE")
    print("Complete the functions above, then run this file to test your work.\n")

    print("Total files (Test Case 1):", count_files("test_cases/case1_flat")) # 5
    print("Total files (Test Case 2):", count_files("test_cases/case2_nested")) # 4
    print("Total files (Test Case 3):", count_files("test_cases/case3_infected")) # 5

    print("Total files (breached files):", count_files("breach_data")) # ???

    print("Total Infected Files (Test Case 1):", len(find_infected_files("test_cases/case1_flat"))) # 0
    print("Total Infected Files (Test Case 2):", len(find_infected_files("test_cases/case2_nested"))) # 0
    print("Total Infected Files (Test Case 3):", len(find_infected_files("test_cases/case3_infected"))) # 3

    infected = find_infected_files("breach_data")
    print("Total Infected Files (breached files):", len(infected)) # ???

    with open('infected_files.txt', 'w') as f:
        for path in infected:
            f.write(path + '\n')
    print("\nFiles saved to: 'infected_files.txt'")

    print("\nInfected by department:")
    for dept in os.listdir("breach_data"):
        dept_path = os.path.join("breach_data", dept)
        if os.path.isdir(dept_path):
            count = len(find_infected_files(dept_path))
            print(f"{dept}: {count}")
