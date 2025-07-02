import os
import re

# Path to the directory
lecciones_dir = 'lecciones/' # Directory containing the lesson files

def extract_number(filename):
    """Extract the first number from filename for sorting"""
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else 0

# Check if the directory exists
if os.path.isdir(lecciones_dir):
    # Get the list of files
    files = os.listdir(lecciones_dir)
    
    # Filter and process .qmd files
    qmd_files = [f for f in files if f.endswith('.qmd')]
    
    # Sort files by numeric order
    sorted_files = sorted(qmd_files, key=extract_number)
    
    # Write to output file
    with open('./scripts/output_namefiles.txt', 'w') as output_file:
        for filename in sorted_files:
            # Change the extension from .qmd to .html for the output string
            html_filename = filename.replace('.qmd', '.html')
            output_file.write(f"{{{{< revealjs file=\"../lecciones/{html_filename}\" height=\"500px\">}}}}\n")
    
    print("Output written to output.txt")
else:
    print(f"Directory not found: {lecciones_dir}")
