import os
import time

def check_uploads(folder_path):
    # Check for a .csv file in the uploads folder 
    current_state = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

    f=open("checkupload.txt", "w")

    # If there are no .csv files found in the folder
    if current_state == []:
        print("No files found in uploads folder.")
        f.write("No files found in uploads folder.")
    # If there is a .csv file found in the folder
    else: 
        print("File(s) found in uploads folder.")
        f.write("File(s) found in uploads folder.")

    f.close()

def main():
    folder_path = "uploads"
    poll_interval = 3 # seconds

    # If valid folder path, continuously check for a .csv file every 3 seconds
    if os.path.exists(folder_path):
        while True:
            check_uploads(folder_path)
            time.sleep(poll_interval)
    else:
        print("Invalid folder path.")

# Ensures that main() is only executed when the script is run directly and not when imported as a module
if __name__ == "__main__":
    main()