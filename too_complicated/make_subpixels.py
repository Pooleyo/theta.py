# The purpose of this function is to combat anti-aliasing.
# This is done by splitting each pixel into sub-pixels, so that they are distributed into bins more evenly.


def run(old_image_pixels, old_width, old_height, num_width_subpixels, num_height_subpixels, debug):

    import numpy as np
    from PIL import Image

    print "Making subpixels..."

    if num_width_subpixels == 1 and num_height_subpixels == 1:
        
        new_image_pixels = old_image_pixels
        new_width = old_width
        new_height = old_height
        shape = (new_height, new_width)
        new_image_pixels_array = np.empty(shape)
        new_image_pixels_list = []

        for i in range(new_height):

            for j in range(new_width):

                new_image_pixels_array[i, j] = new_image_pixels[j, i]
                new_image_pixels_list.append(new_image_pixels[j, i])


    elif num_width_subpixels == 0 or num_height_subpixels == 0:
    
        print "Incorrect value for number of subpixels;\nChoose an integer  >= 1"
        exit()
    
    
        
    else:
        
        new_width = old_width * num_width_subpixels
        new_height = old_height * num_height_subpixels
        shape = (new_height, new_width)
        new_image_pixels_array = np.empty(shape)
        new_image_pixels_list = []
        
        for i in range(new_height):
            for j in range(new_width):
            
                current_old_pixel_index = [j / num_width_subpixels, i / num_height_subpixels]  # Remember that for numpy
                # array[i,j], i refers to the row, and j refers to the column. Conversely in PIL, pixel[i,j] uses i to
                # reference the column, and j to reference the row.

                current_old_pixel_intensity = old_image_pixels[current_old_pixel_index[0], current_old_pixel_index[1]]

                current_subpixel_intensity = current_old_pixel_intensity/(float(num_width_subpixels *
                                                                                num_height_subpixels))  # The intensity
                # of each subpixel is divided here so that the TOTAL intensity in the final image is not altered by
                # introducing these subpixels.

                new_image_pixels_array[i, j] = current_subpixel_intensity

                new_image_pixels_list.append(current_subpixel_intensity)
                
    # Now we must convert the new_image_pixels from a np.array to a pixel access object.
    
        new_image = Image.fromarray(new_image_pixels_array)
        new_image_pixels = new_image.load()        
    
    
    
    debug_message = ("\n\n~~~~~~~~~~~~~\nFILENAME = " + __name__ + ".py"
    
    + "\n\nINPUTS:"
    + "\nold_image_pixels = " + str(old_image_pixels)
    + "\nold_width = " + str(old_width)
    + "\nold_height = " + str(old_height)
    + "\nnum_width_subpixels = " + str(num_width_subpixels)
    + "\nnum_height_subpixels = " + str(num_height_subpixels)
    + "\ndebug = " + str(debug)
    
    + "\n\nOUTPUTS:"
    + "\nnew_image_pixels =" + str(new_image_pixels)
    + "\nnew_width = " + str(new_width)
    + "\nnew_height = " + str(new_height)
    + "\n~~~~~~~~~~~~~~~")
    
    
    if debug:
    
        print debug_message

    return new_image_pixels, new_image_pixels_list, new_width, new_height
