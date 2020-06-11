import os
import random
import sys

# windows beta
def homemade_shred_mode(user_input, passes=60):
    print("[i] Beta")
    if not os.path.isfile(user_input):
        print("Could not find the specified file!")
    with open(user_input, "ba+") as f2w:
        size = f2w.tell()
        print("Size: " + str(size))
        for i in range(int(passes)):
            f2w.seek(0)
            f2w.write(os.urandom(size))
    new_name = str(random.randint(1000,1000000000000))
    os.rename(user_input, new_name)
    os.remove(new_name)
    print("Success!")

def tree(user_input, verbose):
    try:
        for dirName, subdirName, files in os.walk(user_input):
            print("Directory: " + dirName)
            for fname in files:
                #print(" --- File: " + fname)
                os.system("shred -z -f -u -z -n 60 " + verbose + dirName + "/" + fname)
            print("-"*100)
    except Exception as e:
        print(e)

def justFile(user_input, verbose):    
    try:
        os.system("shred -z -f -u -n 60 " + verbose + user_input)
    except Exception as e:
        print(e)

print("-"*100)
print("Linux file shredder utility")
print("Windows is in testing fase")
print("Default Cycles are 60 (paranoid)")
print("-"*100)

user_input = input("Put the fullpath here: ")

if os.name == "nt":
    print("Windows Detected")
    if os.path.isfile(user_input):
        print("Single File found")
        cipher_mode = input("[N]ormal homemade shred mode or [C]ipher mode (this will make a long time): ")
        if cipher_mode == "N":
            homemade_shred_mode(user_input, passes=60)
        elif cipher_mode == "C":
            user_input_path = os.path.dirname(os.path.abspath(user_input)) + "\\"
            user_input_new_name = str(random.randint(1000,1000000000000))
            os.rename(f, user_input_new_name)
            os.system("cipher /W"+user_input_path)

    if os.path.isdir(user_input):
        print("not yet implemented")
        sys.exit(0)
        """
        print("Directory Tree found, using 'cipher' mode, this will make a long time but is better")
        cipher_mode = input("Continue? [y/n]: ")
        if cipher_mode == "y":
            os.system("cipher /W"+user_input)
        elif cipher_mode == "n":
            sys.exit(0)
        """
else: 
    print("Linux Detected")
    print("Shred a single file or an entire directory tree")
    verbose = input("You can use also the verbose mode [y/n]: ")

    if verbose == "y":
        verbose = "-v "
    elif verbose == "n":
        verbose = ""

    if os.path.isfile(user_input):
        print("Single File")
        print("File found: " + user_input)
        justFile(user_input, verbose)
    elif os.path.isdir(user_input):
        print("Entire Tree")
        print("Directory Tree Found: " + user_input)
        tree(user_input, verbose)
