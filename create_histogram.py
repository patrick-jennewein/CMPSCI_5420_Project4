import cv2
import csv
import matplotlib.pyplot as plt

def make_histogram(image):
    """Create the histogram of a grayscale image."""
    histogram = cv2.calcHist([image],
                             [0],
                             None,
                             [256],
                             [0, 256])
    histogram = histogram.flatten()
    return histogram


def make_histogram_from_csv(csv_file):
    """create a histogram from a .csv file with 256 probability values."""
    histogram = []

    # read csv file with 256 floats
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 1:
                try:
                    value = float(row[0])
                    histogram.append(value)
                except ValueError:
                    print(f"invalid row: {row}")

    if len(histogram) != 256:
        raise ValueError("csv file does not contain exactly 256 lines")

    return histogram

def print_hist_comparison(image1, image2, histogram1, histogram2):
    total_pixels_1 = image1.shape[0] * image1.shape[1]
    total_pixels_2 = image2.shape[0] * image2.shape[1]

    # color codes
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    # header
    print(f"{'Intensity':<10} | {'Orig Freq':<10} | {'Orig Prob':<12} | "
          f"{'New Freq':<10} | {'New Prob':<12} | {'Diff (Freq)'}")
    print("-" * 90)

    # compare intensity values
    for intensity in range(256):
        freq1 = int(histogram1[intensity])
        freq2 = int(histogram2[intensity])
        prob1 = freq1 / total_pixels_1
        prob2 = freq2 / total_pixels_2
        freq_diff = freq1 - freq2

        # colorize differences
        if freq_diff > 0:
            diff_str = f"{GREEN}+{freq_diff}{RESET}"
        elif freq_diff < 0:
            diff_str = f"{RED}{freq_diff}{RESET}"
        else:
            diff_str = f"{freq_diff}"

        # print row
        print(f"{intensity:<10} | {freq1:<10} | {prob1:<12.6f} | "
              f"{freq2:<10} | {prob2:<12.6f} | {diff_str:<12}")
