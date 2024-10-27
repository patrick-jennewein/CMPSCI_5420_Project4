# Created by Patrick Jennewein
# November 4, 2024
# CS5420, University of Missouri - St. Louis

import cv2
from parse_args import parse
from create_histogram import make_histogram, print_hist_comparison
from hist_functions import histogram_equalization

def main():
    try:
        # parse the command line
        args = parse()

        # read image
        image = cv2.imread(args['image'])

        # ensure image is valid
        if image is None:
            raise Exception(f"\nERROR: Invalid image file. You provided: {args['image']}")

        # ensure image is grayscale
        if len(image.shape) != 2:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            print("\nERROR: Invalid image file. You provided a color image.\nImage has been converted to grayscale.")

        # show original image
        cv2.imshow("Original Image", image)

        # plot original histogram
        original_histogram = make_histogram(image)

        # perform histogram equalization
        if args['m'] == 1:
            print("Performing histogram equalization...")
            equalized_image = histogram_equalization(image, original_histogram)  # No need to pass histogram
            cv2.imshow("Equalized Image", equalized_image)
            equalized_histogram = make_histogram(equalized_image)
            print_hist_comparison(image, equalized_image, original_histogram, equalized_histogram)
            cv2.moveWindow("Original Image", 100, 100)
            cv2.moveWindow("Equalized Image", 200, 100)

        # Wait for a key press after both images are shown
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"{str(e)}")
        return 1

    return 0

if __name__ == '__main__':
    main()
