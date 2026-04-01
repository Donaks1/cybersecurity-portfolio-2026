import os
import stat

def check_file_permissions(filename):
    try:
        st = os.stat(filename)
        mode = st.st_mode

        print("Checking:", filename)
        print("Permissions:", oct(mode & 0o777))

        if mode & stat.S_IWOTH:
            print("Vulnerability: file is world-writable.")
        elif mode & stat.S_IROTH:
            print("Warning: file is world-readable.")
        elif mode & stat.S_IRGRP or mode & stat.S_IWGRP:
            print("Warning: file is accessible by group users.")
        else:
            print("No obvious permission vulnerability detected.")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error:", e)

def main():
    filename = input("Enter file name to check: ")
    check_file_permissions(filename)

if __name__ == "__main__":
    main()