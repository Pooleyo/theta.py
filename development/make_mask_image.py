def run(filename, colour_label, pixel_list, width, height, colour_map_limits, debug):

    import matplotlib.pyplot as plt
    import numpy as np
    
    pixel_array = np.asarray(pixel_list).reshape(height, width, order="F")

    plt.imshow(pixel_array, interpolation='none', cmap='viridis', vmin=colour_map_limits[0], vmax = colour_map_limits[1])
    
    plt.ylabel("Pixels")
    plt.xlabel("Pixels")
    
    # The following will only apply ticks to the image if there aren't too many pixels. This is to prevent overcrowding
    # of the final plot.
    if len(pixel_list) <= 100:
        plt.xticks(range(width))
        plt.yticks(range(height))
    else:
        plt.xticks([]) # Disables ticks.
        plt.yticks([])    
    
    plt.colorbar()
    plt.savefig(filename)
    plt.close()
    
    debug_message = ("\n\n~~~~~~~~~~~~~\nFILENAME = " + __name__ + ".py"
    
    + "\n\nINPUTS:"
    + "\nfilename = " + str(filename)
    + "\ncolour_label = " + str(colour_label)
    + "\npixel_list = " + str(pixel_list)
    + "\nwidth = " + str(width)
    + "\nheight = " + str(height)
    + "\ncolour_map_limits = " + str(colour_map_limits) 
    + "\ndebug = " + str(debug)
    
    + "\n\nOUTPUTS:"
    + "\nThis function outputs the image:"
    + "\n" + str(filename)
    
    + "\n~~~~~~~~~~~~~~~")

    if debug:
    
        print debug_message

    return
