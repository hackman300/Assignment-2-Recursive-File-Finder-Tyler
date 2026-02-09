import os

def sum_list(numbers):

    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list(numbers[1:])

print("\nTest sum_list:")
print(f"    sum_list([1, 2, 3, 4]) = {sum_list([1, 2, 3, 4])} (expected: 10)")
print(f"    sum_list([]) = {sum_list([])} (expected: 0)")
print(f"    sum_list([5, 5, 5]) = {sum_list([5, 5, 5])} (expected: 15)")

def count_even(numbers):

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

"""
The count_files function has a time complexity of O(n), where n is the total number of files and folders in the directory and its subdirectories. The function works recursively, 
and its runtime can be described as: T(n) equals the time to process a directory with n total items. If the current path is a file, it takes constant time: T(1) equals O(1). If it is a
folder with subfolders or files, the function then lists those subfolders and files. So the recurrence is: T(n) equals sum of T(n_i) for each child plus O(d), where the n_i are the 
sizes of the subtrees. Because the function visits every file and folder exactly once, all the work adds up linearly.

In the simulation, the total number of files was 12,686, and the infected ones were around 3,806, which is exactly 30 percent, as the generator aimed for. HR took the biggest 
hit, with 2,316 infected files. Then HR 1 had 1,064, not quite as bad but still a lot. Finance and Creative got hit as well, though not as badly. I hypothesize that the ransomware 
started in HR when an employee opened a malicious email that triggered the malware. This then caused the ransomware to spread through shared files to other departments, encrypting 
whatever it believed was worth encrypting.

Space-wise, it is O (h) for the recursion stack, where h is the tree height. The find_infect function is similar: time is O(n) because checking extensions is quick each time, and 
space O(h) plus whatever the list ends up holding, but the stack still dominates. Both do depth-first searches, hitting files at the end of the tree quickly and going deeper into 
directories. They do not go over any duplicates; they are linear in the files and subdirectories.

Recursion makes sense for file systems, since they are trees: each subdirectory is like a mini version of the whole thing. It follows the structure naturally, 
handles files at base and passes off to subdirectories in the recursive part, so code stays clean without messing with your own stack.

Iteration could be useful sometimes for super-deep trees that hit Python's limit, or to avoid crashing applications and programs. In large systems, too many recursive 
calls can slow it down. Modules can perform simple traversals iteratively. However, here, recursion keeps things straightforward for a tree-like task. It is not always the best, 
though some prefer loops better for easier debugging.
"""
