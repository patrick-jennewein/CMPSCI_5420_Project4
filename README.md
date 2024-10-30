# Image Sampling and Processing

This project performs image processing tasks with histograms. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Arguments](#arguments)

## Installation

### Prerequisites
To run the project, you'll need the following:

- Python 3.9 or higher

Required libraries:
- `opencv-python~=4.10.0.84`
- `numpy~=2.1.0`
- `matplotlib~=3.9.2`

Additionally, the `argparse` library is used to handle command-line arguments, which is part of the Python standard library.

### Installing

To install and set up the project:
```bash
git clone https://github.com/patrick-jennewein/CMPSCI_5420_Project4.git
cd CS5420-Project-4
pip install -r requirements.txt
```

## Usage
The program can be run using the following command:

```bash
Copy code
python main.py [-h] IMAGE -m OPERATION -i MATCHINGIMAGE -f FILE
```
### Arguments
Positional Arguments:
* IMAGE (required): Path to the input image file. 

Optional Arguments:
* -h : Show help message and exit.
* -IMAGE : an image file to use histogram functions on
* -m OPERATION : Specify the operation to perform. Options:
  * 1 for histogram equalization (default) 
  * 2 for histogram matching with image
  * 3 for histogram matching with file
* -i MATCHINGIMAGE : image to match
* -f FILE : file to match

### Example Usage:
```bash
python main.py dog.jpg -m=3 -f=hist_light.csv
```