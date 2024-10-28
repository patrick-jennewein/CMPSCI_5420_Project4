# Created by Patrick Jennewein
# November 4, 2024
# CS5420, University of Missouri - St. Louis

import cv2
from parse_args import parse
from create_histogram import make_histogram, print_hist_comparison, make_histogram_from_csv
from hist_functions import histogram_equalization, histogram_image_match

def validate_image(image, image_name):
    """Check if the image is valid and in grayscale."""
    if image is None:
        raise Exception(f"\nERROR: Invalid image file. You provided: {image_name}")
    if len(image.shape) != 2:
        raise Exception(f"\nERROR: Invalid image file. {image_name} is a color image.")

def main():
    try:
        # parse command line arguments
        args = parse()

        # read original image and validate
        image = cv2.imread(args['image'], cv2.IMREAD_GRAYSCALE)
        validate_image(image, args['image'])

        # read matched image if mode is 2
        image_match = None
        if args['m'] == 2:
            image_match = cv2.imread(args['i'], cv2.IMREAD_GRAYSCALE)
            validate_image(image_match, args['i'])

        # show original image
        cv2.imshow("Original Image", image)
        original_histogram = make_histogram(image)

        # execute one of three modes
        if args['m'] == 1:
            print("Performing histogram equalization...")
            equalized_image = histogram_equalization(image, original_histogram)
            cv2.imshow("Equalized Image", equalized_image)
            equalized_histogram = make_histogram(equalized_image)
            print_hist_comparison(image, equalized_image, original_histogram, equalized_histogram)

        elif args['m'] == 2:
            print("Performing histogram matching from image...")
            cv2.imshow("Match Image", image_match)
            histogram_match = make_histogram(image_match)
            result_image = histogram_image_match(image, original_histogram, histogram_match)
            cv2.imshow("Result Image", result_image)
            print_hist_comparison(image, image_match, original_histogram, histogram_match)

        elif args['m'] == 3:
            print("Performing histogram matching from file...")
            histogram_match = make_histogram_from_csv(args['f'])
            result_image = histogram_image_match(image, original_histogram, histogram_match)
            cv2.imshow("Result Image", result_image)

        # adjust window positions and wait for key press
        cv2.moveWindow("Original Image", 100, 100)
        cv2.moveWindow("Matched Image", 200, 100)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0

if __name__ == '__main__':
    main()
