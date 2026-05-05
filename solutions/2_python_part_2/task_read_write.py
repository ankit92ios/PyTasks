"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os

def combine_files(input_dir = "files", output_file = "result.txt"):
    values = []
    for filename in sorted(os.listdir(input_dir)):
        file_path = os.path.join(input_dir, filename)

        if os.path.isfile(file_path):
            with open(file_path, "r") as f:
                content = f.read().strip()
                if content:
                    values.append(content)
    
    result = ", ".join(values)

    with open(output_file, "w") as f:
        f.write(result)


combine_files()