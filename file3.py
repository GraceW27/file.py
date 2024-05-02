def write_to_file(filename):
    try:
        with open(filename, 'r') as f:
            f.write("What a great day\n")
            f.write("My student number is 16015\n")
            f.write("Today is raining heavily\n")
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found")
    except PermissionError:
        print (f"Error: Permission denied to write to '{filename}' .")
    finally:
        print("File creation process completed.\n")   

def read_and_display (filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(f"Contents of '{filename}':")
            print(contents)      
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except PermissionError:
        print(f"Permission denied to read the file '{filename}' .")
    finally:
        print("File reading process completed.\n")    

def append_to_file(filename):
    try:
        with open(filename, 'a') as f:
            f.write("\n This is where i draw the line\n")
            f.write("16015 i change number\n")
            f.write("yet another day.\n ")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found .")
    except PermissionError:
        print(f"Error: Permission denied to append to '{filename}' ." )   
    finally:
        print("File appending process completed.\n")   