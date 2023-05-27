# Deezer To Mp3

This project is a simple Python script that allows you to download playlist and album in MP3 format using its unique identifier. It utilizes the API of Deezer to search for and retrieve the corresponding audio files.

## Prerequisites

Before using this script, make sure you have the following:

- Python 3 installed on your machine.
- Required Python packages, which can be installed by running the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone or download this repository to your machine.

2. Navigate to the project directory:

```bash
cd DTM
```

3. Run the Python script using the following command:

```bash
python main.py
```

The script searches for all the music on a given album or playlist according to the ID supplied, then searches for the corresponding music on Youtube and downloads the MP3 file into the specified output directory.

## Additional Notes

- Ensure that you have an active internet connection for the script to access the online music service's API.
- The script does not guarantee the availability or validity of the provided music ID. Make sure to use correct music IDs to obtain the desired results.
- Remember to respect copyright and the terms of use for downloaded music files. This script is intended for personal use and should not be used to violate copyright or illegally distribute music files.

## Authors

This script was developed by Valox and is available under the MIT license. Feel free to contribute, report issues, or suggest improvements by creating an issue or submitting a pull request.

## Acknowledgments

We would like to thank the developers and contributors of all the open-source packages used in this project. Your work is greatly appreciated.
