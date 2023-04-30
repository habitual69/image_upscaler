import os
import time
import replicate
import requests
from dotenv import load_dotenv
from glob import glob
from tqdm import tqdm

# Load environment variables from .env file
load_dotenv()

if os.path.exists('input_folder' and 'output_folder') == False:
    os.mkdir('input_folder')
    os.mkdir('output_folder')

input_folder = 'input_folder'
output_folder = 'output_folder'

# Loop through all image files in the input folder
for file in glob(os.path.join(input_folder, '*.jpg')) + \
            glob(os.path.join(input_folder, '*.jpeg')) + \
            glob(os.path.join(input_folder, '*.png')):
    # Set the Replicate API endpoint and key
    endpoint = "nightmareai/real-esrgan:42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b"
    api_key = os.getenv('REPLICATE_API_TOKEN')

    # Get the file size
    input_file_size = os.path.getsize(file) / 1000000  # in MB

    # Start the timer
    start_time = time.time()

    # Upscale the image using Replicate
    response = replicate.run(endpoint, input={"image": open(file, "rb")}, api_key=api_key)
    output = response

    # Create the progress bar
    bar = tqdm(total=100)

    # Save the output to the output folder
    with open(os.path.join(output_folder, os.path.basename(file)), 'wb') as f:
        for chunk in requests.get(output, stream=True).iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                bar.update(len(chunk))

    # Close the progress bar
    bar.close()

    # Calculate the elapsed time and output file size
    elapsed_time = time.time() - start_time
    output_file_size = os.path.getsize(os.path.join(output_folder, os.path.basename(file))) / 1000000  # in MB

    # Print the output file path and elapsed time
    print(f"{os.path.basename(file)} ({input_file_size:.2f} MB) -> ({output_file_size:.2f} MB) in {elapsed_time:.2f} seconds.")
    os.remove(file)
