import datetime
print("Started Program")
def main():
    # Your existing code here (e.g., print("Hello, World!"))
    print("In a function")

    # Get the current date and time
    now = datetime.datetime.now()
    print(now)

    # Write to the text file
    with open("output.txt", "a") as file:
        file.write(f"Hello, World! ({now:%Y-%m-%d %H:%M:%S})\n")
    print("Script executed successfully!")

if __name__ == "__main__":
    main()
