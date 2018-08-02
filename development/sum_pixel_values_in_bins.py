def run(image_bin_list, pixel_value, debug):

    print "Summing pixel values in each bin..."

    for current_bin in image_bin_list:
           
        new_pixel_value = 0
        
        for pixel_index in current_bin[2]:
            new_pixel_value += pixel_value[pixel_index]
            
        current_bin[3] = new_pixel_value
        
        
        
    debug_message = ("\n\n~~~~~~~~~~~~~\nFILENAME = " + __name__ + ".py"
    
    + "\n\nINPUTS:"
    + "\nimage_bin_list = " + str(image_bin_list)
    + "\npixel_value = " + str(pixel_value)
    + "\ndebug = " + str(debug)
  
    + "\n\nOUTPUTS:"
    + "\nimage_bin_list = " + str(image_bin_list)
    + "\n~~~~~~~~~~~~~~~")
    
    
    if debug:
    
        print debug_message
    
        
    return image_bin_list
