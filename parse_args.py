import argparse


def parse() -> dict:
    """parse command-line arguments or use default arguments if none are given."""
    parser = argparse.ArgumentParser()

    # create necessary argument (directory to parse)
    parser.add_argument("image", help="the image file to evaluate")

    # create optional arguments
    parser.add_argument("-m", type=int, default=1,
                        help="the histogram function to be applied [default: 1]\n"
                             "1: histogram equalization (default)\n"
                             "2: histogram matching with image\n"
                             "3: histogram matching with file\n")
    parser.add_argument("-i", help="the image to match")
    parser.add_argument("-f", help="the image file to match")

    # use the parsed arguments
    args = parser.parse_args()

    # print
    print(f"image file: {args.image}")
    print(f"method: {args.m}")
    print(f"image to match: {args.i}")
    print(f"image file to match: {args.f}")

    # convert to dictionary and return
    args_dict = vars(args)
    return args_dict