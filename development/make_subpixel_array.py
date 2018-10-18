def run(raw_pixel_value, num_subpixels_height, num_subpixels_width):

    import numpy as np

    raw_height, raw_width = np.shape(raw_pixel_value)

    subpixel_array_height = num_subpixels_height * raw_height

    subpixel_array_width = num_subpixels_width * raw_width

    subpixel_array = np.empty((subpixel_array_height, subpixel_array_width))

    intensity_divisor = num_subpixels_height * num_subpixels_width

    for i in range(subpixel_array_height):

        current_raw_pixel_height = i / num_subpixels_height

        for j in range(subpixel_array_width):

            current_raw_pixel_width = j / num_subpixels_width

            subpixel_array[i, j] = raw_pixel_value[current_raw_pixel_height, current_raw_pixel_width] / intensity_divisor

    return subpixel_array;