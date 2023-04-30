
# Project Name: ImageUpscale-ReplicateAPI

## Introduction

This project aims to upscale low-resolution images using the Replicate API. The code loops through all image files in the input folder and uses the Replicate API to upscale them. The upscaled images are then saved in the output folder. The code also provides the elapsed time and output file size for each image.

## Requirements

This project requires Python 3.7 or higher and the following packages:

- replicate
- requests
- dotenv
- glob
- tqdm

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory and install the required packages using the following command:
```
pip install -r requirements.txt
```
3. Create an account on [Replicate](https://replicate.ai/) and obtain an API key.
4. Create a .env file or rename the .env_template file in the project directory and add the following line, replacing "your_api_key" with your Replicate API key:
```
REPLICATE_API_TOKEN=your_api_key
```
5. Place your input images in the input_folder directory.

## Usage

1. Run the following command to start upscaling images:
```
python upscale_images.py
```
2. The upscaled images will be saved in the output_folder directory, and the original images will be deleted.
3. The output file path and elapsed time will be printed for each image in the console.

## Suggestions

Here are some possible suggestions for improvement:

- Add support for other image formats.
- Allow users to choose the output image size.
- Add an option to keep the original images.
- Create a GUI for the application.