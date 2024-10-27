import numpy as np
import cv2

def histogram_equalization(image, histogram):
    """manual histogram equalization on a grayscale image."""

    # normalize the histogram
    total_pixels = image.shape[0] * image.shape[1]
    normalized_histogram = histogram / total_pixels

    # calculate the cumulative distribution function
    cdf = np.cumsum(normalized_histogram)

    # maps the intensity values to the full range (0 to 255)
    cdf_min = cdf[cdf > 0].min()
    cdf_normalized = (cdf - cdf_min) / (1 - cdf_min) * 255
    cdf_normalized = cdf_normalized.astype('uint8')

    # map the original image pixel values using the normalized CDF
    equalized_image = cdf_normalized[image]
    return equalized_image
