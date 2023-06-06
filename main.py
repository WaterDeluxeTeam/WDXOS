import os
import shutil
import subprocess

VIRTUAL_DIR = "D:/VirtualDisk"

def clear_screen():
    # Clear the console screen
    subprocess.call("clear" if os.name == "posix" else "cls", shell=True)

def start_dos_mode():
    subprocess.call("python DOSmode.py", shell=True)

def start_os_mode():
    subprocess.call("python OSmode.py", shell=True)

def display_menu():
    clear_screen()
    print("Select mode:")
    print("1. DOS")
    print("2. OS")
    print("3. README")

def create_readme():
    readme_path = os.path.join(VIRTUAL_DIR, "README.txt")
    readme_content = """
    DENOS README
    Welcome to DenOS - Your Virtual Command Line Interface

DenOS is a simple command line interface that allows you to navigate directories, create and edit files, copy files, run various scripts, and compile and run C, C++, LUA, and Ruby files. It provides a basic file system simulation within a virtual disk.

Commands:
- cd <directory>: Change the current working directory.
- mkdir <directory>: Create a new directory.
- edit <filename>: Create or edit a text file.
- type <filename>: Display the contents of a text file.
- copy <source> <destination>: Copy a file from the virtual directory to the local machine.
- python <command or script>: Run a Python command or script.
- run <batch file>: Run a batch file.
- gcc <c_file>: Compiles and runs a C file (.c).
- g++ <cpp_file>: Compiles and runs a C++ file (.cpp).
- lua <lua_file>: Runs a LUA file (.lua).
- ruby <ruby_file>: Runs a Ruby file (.rb).
- exit: Exit DenOS.

Usage:
1. Use the command prompt to enter commands.
2. Enter "exit" to quit DenOS.

Virtual Disk:
- A virtual disk is created at D:/VirtualDisk.
- All files and directories created within DenOS are stored in this virtual disk.

Note:
- DenOS does not support advanced features such as networking, multi-threading, or GUI.
- Certain commands may require specific software or dependencies to be installed on your system.

Enjoy your virtual command line experience with DenOS!


    """
    with open(readme_path, "w") as f:
        f.write(readme_content)

def start_program():
    # Create the virtual directory if it doesn't exist
    if not os.path.exists(VIRTUAL_DIR):
        os.makedirs(VIRTUAL_DIR)
        create_readme()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            start_dos_mode()
            break
        elif choice == "2":
            start_os_mode()
            break
        elif choice == "3":
            readme_path = os.path.join(VIRTUAL_DIR, "README.txt")
            with open(readme_path, "r") as f:
                readme_content = f.read()
            clear_screen()
            print(readme_content)
            input("Press Enter to continue...")
        else:
            print("Invalid choice. Please try again.")

start_program()


# Create the virtual directory if it doesn't exist
if not os.path.exists(VIRTUAL_DIR):
    os.makedirs(VIRTUAL_DIR)
    with open(os.path.join(VIRTUAL_DIR, "README.txt"), "w") as f:
        f.write("This is your virtual 2MB disk. Store your files here.")

start_program()

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
            os.chdir(command[3:])
        except FileNotFoundError:
            print("Directory not found")

    # Create a new directory
    elif command.startswith("mkdir "):
        try:
            os.makedirs(os.path.join(os.getcwd(), command[6:]))
        except:
            print("Invalid directory name")

    # Create a new text file
    elif command.startswith("edit "):
        try:
            file_name = command[5:]
            file_path = os.path.join(os.getcwd(), file_name)

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
            file_path = os.path.join(os.getcwd(), command[5:])
            with open(file_path, "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("File not found")
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

            dst_path = os.path.join(os.getcwd(), dst)
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

    # Run a LUA file
    elif command.startswith("lua "):
        try:
            file_path = os.path.join(os.getcwd(), command[4:])
            os.system(f"lua {file_path}")
        except Exception as e:
            print(f"Error: {str(e)}")

    # Run a Ruby file
    elif command.startswith("ruby "):
        try:
            file_path = os.path.join(os.getcwd(), command[5:])
            os.system(f"ruby {file_path}")
        except Exception as e:
            print(f"Error: {str(e)}")
