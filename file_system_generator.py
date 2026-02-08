"""
File System Generator for Recursion Assignment
Generates a simulated compromised file system with nested directories
and files with various extensions including .encrypted files.
"""

import os
import random
import shutil

def generate_breach_data(root_path="breach_data", max_depth=8, max_dirs=5, max_files=10):
    """
    Generate a realistic file system structure with simulated breach data.
    
    Args:
        root_path: Root directory name
        max_depth: Maximum nesting depth
        max_dirs: Maximum subdirectories per level
        max_files: Maximum files per directory
    """
    # Clean up existing directory if it exists
    if os.path.exists(root_path):
        shutil.rmtree(root_path)
    
    # Create root directory
    os.makedirs(root_path)
    
    # File extensions (simulating a marketing firm's files)
    normal_extensions = ['.pdf', '.docx', '.xlsx', '.pptx', '.jpg', '.png', '.mp4', '.txt']
    encrypted_extension = '.encrypted'
    
    # Department/folder names for realistic structure
    departments = ['Marketing', 'Sales', 'Creative', 'Finance', 'HR', 'Operations']
    project_names = ['Q1_Campaign', 'Q2_Campaign', 'Q3_Campaign', 'Q4_Campaign', 
                     'Client_Projects', 'Internal_Docs', 'Archive', 'Drafts']
    
    file_types = ['report', 'presentation', 'budget', 'photo', 'video', 'contract', 
                  'invoice', 'memo', 'brief', 'strategy']
    
    def create_structure(current_path, current_depth):
        """Recursively create directory structure with files."""
        if current_depth >= max_depth:
            return
        
        # Create files in current directory
        num_files = random.randint(2, max_files)
        for i in range(num_files):
            # 30% chance of being encrypted
            if random.random() < 0.3:
                extension = encrypted_extension
            else:
                extension = random.choice(normal_extensions)
            
            file_name = f"{random.choice(file_types)}_{random.randint(1000, 9999)}{extension}"
            file_path = os.path.join(current_path, file_name)
            
            # Create empty file
            with open(file_path, 'w') as f:
                f.write(f"Mock content for {file_name}\n")
        
        # Create subdirectories
        if current_depth < max_depth - 1:
            num_dirs = random.randint(1, max_dirs)
            for i in range(num_dirs):
                if current_depth == 0:
                    dir_name = random.choice(departments)
                elif current_depth == 1:
                    dir_name = random.choice(project_names)
                else:
                    dir_name = f"Subfolder_{random.randint(100, 999)}"
                
                dir_path = os.path.join(current_path, dir_name)
                
                # Avoid duplicate directory names
                counter = 1
                while os.path.exists(dir_path):
                    dir_path = os.path.join(current_path, f"{dir_name}_{counter}")
                    counter += 1
                
                os.makedirs(dir_path)
                create_structure(dir_path, current_depth + 1)
    
    print("Generating compromised file system...")
    create_structure(root_path, 0)
    
    # Count total files and infected files
    total_files = 0
    infected_files = 0
    
    for root, dirs, files in os.walk(root_path):
        total_files += len(files)
        infected_files += len([f for f in files if f.endswith('.encrypted')])
    
    print(f"✓ File system generated at: {root_path}/")
    print(f"✓ Total files: {total_files}")
    print(f"✓ Infected files (.encrypted): {infected_files}")
    print(f"✓ Infection rate: {infected_files/total_files*100:.1f}%")
    print("\nYou can now implement your recursive functions to analyze this breach!")

def generate_test_cases():
    """Generate small test cases with known answers."""
    test_dir = "test_cases"
    
    # Clean up existing test directory
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    
    # Test Case 1: Simple flat structure
    case1 = os.path.join(test_dir, "case1_flat")
    os.makedirs(case1)
    for i in range(5):
        with open(os.path.join(case1, f"file{i}.txt"), 'w') as f:
            f.write("test")
    
    # Test Case 2: One level of nesting
    case2 = os.path.join(test_dir, "case2_nested")
    os.makedirs(case2)
    with open(os.path.join(case2, "root_file.txt"), 'w') as f:
        f.write("test")
    
    subdir = os.path.join(case2, "subdir")
    os.makedirs(subdir)
    for i in range(3):
        with open(os.path.join(subdir, f"nested_file{i}.txt"), 'w') as f:
            f.write("test")
    
    # Test Case 3: Multiple levels with .encrypted files
    case3 = os.path.join(test_dir, "case3_infected")
    os.makedirs(case3)
    with open(os.path.join(case3, "normal.txt"), 'w') as f:
        f.write("test")
    with open(os.path.join(case3, "infected.encrypted"), 'w') as f:
        f.write("test")
    
    level1 = os.path.join(case3, "level1")
    os.makedirs(level1)
    with open(os.path.join(level1, "data.encrypted"), 'w') as f:
        f.write("test")
    
    level2 = os.path.join(level1, "level2")
    os.makedirs(level2)
    with open(os.path.join(level2, "deep.txt"), 'w') as f:
        f.write("test")
    with open(os.path.join(level2, "virus.encrypted"), 'w') as f:
        f.write("test")
    
    print(f"\n✓ Test cases generated at: {test_dir}/")
    print("\nTest Case 1 (case1_flat): 5 files, max depth 0")
    print("Test Case 2 (case2_nested): 4 files total (1 root + 3 in subdir), max depth 1")
    print("Test Case 3 (case3_infected): 5 files total, 3 .encrypted files, max depth 2")

if __name__ == "__main__":
    generate_test_cases()
    print("\n" + "="*60 + "\n")
    generate_breach_data()