# Function to read from a file and write to a new file
def process_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()
            modified_content = content.upper()

        # Open the output file for writing
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Successfully processed '{input_filename}' and wrote to '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
process_file('input.txt', 'output.txt')

def read_user_file():
    """Asks the user for a filename and handles file-related errors."""
    filename = input("Please enter the name of the file you want to read: ")

    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile content:")
            print("---------------")
            print(content)
            print("---------------")
    except FileNotFoundError:
        # This block runs if the file does not exist
        print(f"Error: The file '{filename}' was not found.")
    except IOError as e:
        # This block catches other I/O related errors
        print(f"Error: An I/O error occurred while reading the file. Details: {e}")
    except Exception as e:
        # This is a general catch-all for any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Call the function to run the program
read_user_file()
