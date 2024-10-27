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

def histogram_image_match(image, histogram, matched_histogram):
    """histogram matching of two grayscale images"""
    # calculate the CDF of the original image
    original_cdf = np.cumsum(histogram)
    original_cdf_normalized = (original_cdf / original_cdf[-1]) * 255  # Normalize to 255 range

    # calculate the CDF of the matched image
    matched_cdf = np.cumsum(matched_histogram)
    matched_cdf_normalized = (matched_cdf / matched_cdf[-1]) * 255  # Normalize to 255 range

    # create a lookup table mapping original CDF values to matched CDF values
    lookup_table = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        # Find the intensity in the matched CDF that corresponds to the original CDF
        closest_value = np.argmin(np.abs(matched_cdf_normalized - original_cdf_normalized[i]))
        lookup_table[i] = closest_value

    # map the intensities of the original image using the lookup table
    new_image = cv2.LUT(image, lookup_table)

    return new_image