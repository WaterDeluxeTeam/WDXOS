import os
import shutil

VIRTUAL_DIR = "D:/VirtualDisk"
current_dir = os.getcwd()
previous_dirs = []

# Create the virtual directory if it doesn't exist
if not os.path.exists(VIRTUAL_DIR):
    os.makedirs(VIRTUAL_DIR)
    with open(os.path.join(VIRTUAL_DIR, "README.txt"), "w") as f:
        f.write("This is your virtual 2MB disk. Store your files here.")

# Define the command prompt loop
while True:
    command = input("DENOS> ")

    # Exit the loop if the user enters "exit"
    if command == "exit":
        break

    # Change the current working directory
    elif command.startswith("cd "):
        try:
            directory = command[3:]

            # Store the current directory in the previous_dirs list
            previous_dirs.append(current_dir)

            os.chdir(directory)
            current_dir = os.getcwd()
            print(f"Current Directory: {current_dir}")
        except FileNotFoundError:
            print("Directory not found")

    # Go back to the previous directory
    elif command == "back":
        if len(previous_dirs) > 0:
            # Get the previous directory from the list
            directory = previous_dirs.pop()

            # Change to the previous directory
            os.chdir(directory)
            current_dir = os.getcwd()
            print(f"Current Directory: {current_dir}")
        else:
            print("No previous directory available")

    # Create a new directory
    elif command.startswith("mkdir "):
        try:
            directory = command[6:]
            os.makedirs(os.path.join(current_dir, directory), exist_ok=True)
            print(f"Directory created: {directory}")
        except Exception as e:
            print(f"Error creating directory: {str(e)}")

    # Remove a directory and its contents
    elif command.startswith("rmdir "):
        try:
            directory = command[6:]
            shutil.rmtree(os.path.join(current_dir, directory))
            print(f"Directory removed: {directory}")
        except FileNotFoundError:
            print(f"Directory not found: {directory}")
        except Exception as e:
            print(f"Error removing directory: {str(e)}")

    # Remove a file or directory
    elif command.startswith("rm "):
        try:
            path = command[3:]
            full_path = os.path.join(current_dir, path)
            if os.path.isfile(full_path) or os.path.isdir(full_path):
                confirm = input(f"Are you sure you want to remove {path}? (y/n): ")
                if confirm.lower() == "y":
                    shutil.rmtree(full_path) if os.path.isdir(full_path) else os.remove(full_path)
                    print(f"File or directory removed: {path}")
                else:
                    print("Removal canceled.")
            else:
                print(f"Path not found: {path}")
        except Exception as e:
            print(f"Error removing file or directory: {str(e)}")

    # Create a new text file
    if command.startswith("edit "):
        try:
            file_name = command[5:]
            file_path = os.path.join(current_dir, file_name)

            # If the file already exists, open it for editing and append to it
            if os.path.exists(file_path):
                with open(file_path, "a") as f:
                    while True:
                        line = input()
                        if line == ":wq":
                            break
                        f.write(line + "\n")
            # If the file doesn't exist, create a new file and open it for editing
            else:
                with open(file_path, "w") as f:
                    while True:
                        line = input()
                        if line == ":wq":
                            break
                        f.write(line + "\n")

        except Exception as e:
            print(f"Error: {str(e)}")

    # Display the contents of a text file
    elif command.startswith("type "):
        try:
            file_path = os.path.join(current_dir, command[5:])
            with open(file_path, "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(f"Error: {str(e)}")

    # Display the contents of a folder
    elif command.startswith("dir "):
        try:
            folder_path = os.path.join(current_dir, command[4:])
            if not os.path.isdir(folder_path):
                print(f"{command[4:]} is not a valid directory")
            else:
                print("Contents:")
                print("-" * 50)
                for item in os.listdir(folder_path):
                    item_path = os.path.join(folder_path, item)
                    if os.path.isdir(item_path):
                        print(f"{item}\t(Folder)")
                    else:
                        print(f"{item}\t(File)")
                print("-" * 50)
        except Exception as e:
            print(f"Error: {str(e)}")

    # Copy a file from the virtual directory to the local machine
    elif command.startswith("copy "):
        try:
            src, dst = command[5:].split()
            src_path = os.path.join(VIRTUAL_DIR, src)

            # check if the source file exists in the virtual directory
            if not os.path.exists(src_path):
                raise FileNotFoundError(f"File {src} not found in virtual directory")

            dst_path = os.path.join(current_dir, dst)
            shutil.copy(src_path, dst_path)
            print(f"File copied from {src_path} to {dst_path}")
        except Exception as e:
            print(f"Error: {str(e)}")

    # Run a Python command or script
    elif command.startswith("python "):
        try:
            os.system(command)
        except Exception as e:
            print(f"Error: {str(e)}")

    # Run a batch file
    elif command.startswith("run "):
        try:
            file_path = os.path.join(current_dir, command[4:])
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"Batch file {file_path} not found")

            os.system(file_path)
        except Exception as e:
            print(f"Error: {str(e)}")

    # Compile and run a C file
    elif command.startswith("gcc "):
        try:
            file_path = os.path.join(current_dir, command[4:])
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"C file {file_path} not found")

            os.system(f"gcc {file_path} -o {os.path.splitext(file_path)[0]}.exe")
            os.system(f"{os.path.splitext(file_path)[0]}.exe")
        except Exception as e:
            print(f"Error: {str(e)}")

    # Compile and run a C++ file
    elif command.startswith("g++ "):
        try:
            file_path = os.path.join(current_dir, command[4:])
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"C++ file {file_path} not found")

            os.system(f"g++ {file_path} -o {os.path.splitext(file_path)[0]}.exe")
            os.system(f"{os.path.splitext(file_path)[0]}.exe")
        except Exception as e:
            print(f"Error: {str(e)}")

    # Run a LUA file
    elif command.startswith("lua "):
        try:
            file_path = os.path.join(current_dir, command[4:])
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"LUA file {file_path} not found")

            os.system(f"lua {file_path}")
        except Exception as e:
            print(f"Error: {str(e)}")

    # Run a Ruby file
    elif command.startswith("ruby "):
        try:
            file_path = os.path.join(current_dir, command[5:])
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"Ruby file {file_path} not found")

            os.system(f"ruby {file_path}")
        except Exception as e:
            print(f"Error: {str(e)}")

    # Run a Java file
    elif command.startswith("java "):
        try:
            file_path = os.path.join(current_dir, command[5:])
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"Java file {file_path} not found")

            os.system(f"java {file_path}")
        except Exception as e:
            print(f"Error: {str(e)}")

    # Run a JavaScript file
    elif command.startswith("node "):
        try:
            file_path = os.path.join(current_dir, command[5:])
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"JavaScript file {file_path} not found")

            os.system(f"node {file_path}")
        except Exception as e:
            print(f"Error: {str(e)}")

    # Run a TypeScript file
    elif command.startswith("ts-node "):
        try:
            file_path = os.path.join(current_dir, command[8:])
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"TypeScript file {file_path} not found")

            os.system(f"ts-node {file_path}")
        except Exception as e:
            print(f"Error: {str(e)}")

    else:
        print(f"Invalid command: {command}(or maybe it is correct, Weird V2 bug) ")
