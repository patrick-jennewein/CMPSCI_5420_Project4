# Created by Patrick Jennewein
# November 4, 2024
# CS5420, University of Missouri - St. Louis

import cv2
from parse_args import parse
from create_histogram import make_histogram, print_hist_comparison
from hist_functions import histogram_equalization, histogram_image_match

def main():
    try:
        # parse the command line
        args = parse()

        # read image(s)
        image = cv2.imread(args['image'], cv2.IMREAD_GRAYSCALE)
        image_match = None
        if args['m'] == 2:
            image_match = cv2.imread(args['i'], cv2.IMREAD_GRAYSCALE)
            if image_match is None:
                raise Exception(f"\nERROR: Invalid image file. You provided: {args['i']}")
            if len(image_match.shape) != 2:
                raise Exception(f"\nERROR: Invalid image file. {args['m']} a color image.")

        # check file
        if args['m'] == 3:
            image_match = cv2.imread(args['i'])
            if image_match is None:
                raise Exception(f"\nERROR: Invalid image file. You provided: {args['i']}")

        # ensure image is valid
        if image is None:
            raise Exception(f"\nERROR: Invalid image file. You provided: {args['image']}")

        # ensure image is grayscale
        if len(image.shape) != 2:
            raise Exception(f"\nERROR: Invalid image file. {args['m']} a color image.")

        # show original image
        cv2.imshow("Original Image", image)

        # plot original histogram
        original_histogram = make_histogram(image)

        # perform histogram equalization
        if args['m'] == 1:
            print("Performing histogram equalization...")
            equalized_image = histogram_equalization(image, original_histogram)
            cv2.imshow("Equalized Image", equalized_image)
            equalized_histogram = make_histogram(equalized_image)
            print_hist_comparison(image, equalized_image, original_histogram, equalized_histogram)
            cv2.moveWindow("Original Image", 100, 100)
            cv2.moveWindow("Equalized Image", 200, 100)

        # perform histogram matching from image
        if args['m'] == 2:
            print("Performing histogram matching from image...")
            cv2.imshow("Match Image", image_match)
            histogram_match = make_histogram(image_match)
            result_image = histogram_image_match(image, original_histogram, histogram_match)
            cv2.imshow("Result Image", result_image)
            print_hist_comparison(image, image_match, original_histogram, histogram_match)
            cv2.moveWindow("Original Image", 100, 100)
            cv2.moveWindow("Matched Image", 200, 100)

        # perform histogram matching from image
        if args['m'] == 3:
            print("Performing histogram matching from file...")

        # Wait for a key press after both images are shown
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"{str(e)}")
        return 1

    return 0

if __name__ == '__main__':
    main()
