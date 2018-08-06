def run(initial, transformed_image_filename, debug):
       
    from PIL import Image
    
    print "Checking image total pixel value..."

    image = Image.open(transformed_image_filename)
    pixels = image.load()
    width, height = image.size

    transformed_total_pixel_value = 0.0
    
    for i in range(width):
        for j in range(height):
            transformed_total_pixel_value += pixels[i,j]

    print "Total pixel value initially = "+ str(initial)
    print "After transformation = "+ str(transformed_total_pixel_value)
    
    image.close()
    
    debug_message = ("\n\n~~~~~~~~~~~~~\nFILENAME = " + __name__ + ".py"
    
    + "\n\nINPUTS:"
    + "\ninitial = " + str(initial)
    + "\ntransformed_image_filename = " + str(transformed_image_filename)
    + "\ndebug = " + str(debug)
  
    + "\n\nOUTPUTS:"
    + "\nThis function checks the total pixel value before and after transformation. The total pixel value after transformation is:"
    + "\n" + str(transformed_total_pixel_value)
    + "\n~~~~~~~~~~~~~~~")

    if debug:
    
        print debug_message

    return
