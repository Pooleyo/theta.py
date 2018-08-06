def run(image_filename, debug, i):

    from PIL import Image

    print "Iteration " + str(i)
    print "Initialising analysis on " + image_filename + " ..."

    im = Image.open(image_filename)

    width, height = im.size

    pix = im.load()
    
    initial_pixel_values = []

    for i in range(width):

        for j in range(height):

            initial_pixel_values.append(pix[i, j])

    total_pixel_value = sum(initial_pixel_values)
    
    im.close()
    
    debug_message = ("\n\n~~~~~~~~~~~~~\nFILENAME = " + __name__ + ".py"
    
    + "\n\nINPUTS:"
    + "\ncurrent_raw_image = " + str(image_filename)
    + "\ndebug = " + str(debug)
    
    + "\n\nOUTPUTS:"
    + "\nim = " + str(im)
    + "\nwidth = " + str(width)
    + "\nheight = " + str(height)
    + "\npix = " + str(pix)
    + "\ntotal_pixel_value = " + str(total_pixel_value)
    
    + "\n~~~~~~~~~~~~~~~")

    if debug:
    
        print debug_message

    return im, width, height, pix, initial_pixel_values, total_pixel_value
