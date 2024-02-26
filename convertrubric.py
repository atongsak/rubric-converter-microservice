import os
import time

def can_convert(path):
    # Open the microservice's text file in read mode
    f=open("checkupload.txt", "r")
    # Read the content of the text file
    content = f.read()

    # Check the content and print corresponding messages
    if content == "No files found in uploads folder.":  
        print(content + " We can't convert the rubric.")
    elif content == "File(s) found in uploads folder.":
        print(content + " Now we can convert the rubric.")
    else:
        print("There's nothing in the text file yet.")

    # Close the file 
    f.close()

def main():
    # Define the path to the microservice's text file
    path = "checkupload.txt"
    # Set the interval for checking the text file
    poll_interval = 5 # seconds

    while True:
        # Check if the text file exists
        if os.path.exists(path):
            while True:
                # Check and print messages based on text file's content
                can_convert(path)
                # Wait for the specified interval before checking again
                time.sleep(poll_interval)
        else:
            # Print error message if text file doesn't exist yet
            print("Waiting for Upload Checker microservice to begin..")
            # Wait for a longer interval before checking again
            time.sleep(10)

# Ensures that main() is only executed when the script is run directly and not when imported as a module
if __name__ == "__main__":
    main()