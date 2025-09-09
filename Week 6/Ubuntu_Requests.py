import requests
import os
from urllib.parse import urlparse
import hashlib

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URL from user
    url = input("Please enter the image URL: ")
    
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename or '.' not in filename:
            # Handle cases where URL path doesn't have a filename
            content_type = response.headers.get('Content-Type', '').split('/')
            if len(content_type) == 2 and content_type[0] == 'image':
                extension = content_type[1]
                filename = f"downloaded_image.{extension}"
            else:
                filename = "downloaded_image.jpg"

        # Save the image
        filepath = os.path.join("Fetched_Images", filename)
        
        # Check if file already exists to prevent duplicates
        if os.path.exists(filepath):
            print(f"✓ File '{filename}' already exists. Skipping download.")
        else:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
        
        print("\nConnection strengthened. Community enriched.")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()

# ... (rest of the code remains the same)

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    os.makedirs("Fetched_Images", exist_ok=True)
    
    while True:
        url = input("Please enter an image URL (or 'done' to finish): ")
        if url.lower() == 'done':
            break
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename or '.' not in filename:
                content_type = response.headers.get('Content-Type', '').split('/')
                if len(content_type) == 2 and content_type[0] == 'image':
                    extension = content_type[1]
                    filename = f"downloaded_image.{extension}"
                else:
                    filename = "downloaded_image.jpg"

            filepath = os.path.join("Fetched_Images", filename)

            if os.path.exists(filepath):
                print(f"✓ File '{filename}' already exists. Skipping download.")
            else:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"✓ Successfully fetched: {filename}")
                print(f"✓ Image saved to {filepath}")
        
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred for {url}: {e}")

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()

# ... (inside the try block)


def hash_file(filepath):
    """Generates a SHA256 hash of a file."""
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

# Inside the main loop after downloading the content
response_content = response.content
downloaded_hash = hashlib.sha256(response_content).hexdigest()

# Check for existing hashes in the directory
hashes_in_dir = []
for existing_file in os.listdir("Fetched_Images"):
    hashes_in_dir.append(hash_file(os.path.join("Fetched_Images", existing_file)))

if downloaded_hash in hashes_in_dir:
    print(f"✓ A duplicate image was found. Skipping download.")
else:
    # Save the image as before
    # ...
