# Check Uploads Microservice 
This microservice, checkupload.py, incrementally checks the "uploads" folder and updates a message to checkupload.txt that indicates the presence of a .csv file. There are two possible outputs in the text file: "No files found in uploads folder." and "File(s) found in uploads folder." 

# How to Request & Receive Data from the Check Uploads Microservice
As this microservice primarily communicates via checkupload.txt, a program must open and read the contents of checkupload.txt to receive outputted data about the "uploads" folder. An example implementation of this is seen in convertrubric.py:
```
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
```
In this example, convertrubric.py is opening and reading checkupload.txt every 5 seconds before determining whether rubric conversions on the .csv file can begin.

# UML Sequence Diagram
<img src="readme/uml.png">
