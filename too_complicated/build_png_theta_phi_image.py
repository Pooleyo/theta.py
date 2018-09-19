def run(filename, image_bin_list, width, height, gsqr_bin_list, phi_bin_list, normalisation, debug):
    import numpy as np
    from PIL import Image

    new_pixel_values = []

    for i in image_bin_list:
        new_pixel_values.append(i[3])

    if normalisation is True:

        normalisation_constant = max(new_pixel_values) / float(255)

        for i in range(len(new_pixel_values)):
            # The pixel value is now normalised according to our normalising condition declared above.
            # If no normalisation is wanted, the normalisation_constant is set to 1.

            inverted_pixel_value = new_pixel_values[i] / normalisation_constant

            new_pixel_values[i] = abs(inverted_pixel_value - 255.0)

    elif normalisation is False:

        pass

    else:

        print "Invalid value for 'normalisation';\n'normalisation' is of type 'bool'"

    image_array = np.asarray(new_pixel_values).reshape(height, width)

    image = Image.fromarray(image_array)

    image = image.convert('L')

    image.save(filename)

    image.close()

    debug_message = ("\n\n~~~~~~~~~~~~~\nFILENAME = " + __name__ + ".py"

                     + "\n\nINPUTS:"
                     + "\nfilename = " + str(filename)
                     + "\nimage_bin_list = " + str(image_bin_list)
                     + "\nworking_width = " + str(width)
                     + "\nworking_height = " + str(height)
                     + "\ngsqr_bin_list = " + str(gsqr_bin_list)
                     + "\nphi_bin_list = " + str(phi_bin_list)
                     + "\nnormalisation = " + str(normalisation)
                     + "\ndebug = " + str(debug)

                     + "\n\nOUTPUTS:"
                     + "\nnew_pixel_values = " + str(new_pixel_values)
                     + "\n~~~~~~~~~~~~~~~")

    if debug:
        print debug_message

    return new_pixel_values

