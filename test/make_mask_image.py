def run(filename, colour_label, pixel_list, width, height):

    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import numpy as np
    
    print "Making image mask '" + filename + "'..."

    pixel_array = np.asarray(pixel_list)

    pixel_array.shape = (width, height)
    
    plt.imshow(pixel_array, interpolation='none', cmap='viridis')
    plt.ylabel("Pixels")
    plt.xlabel("Pixels")
    plt.colorbar()
    plt.savefig(filename)
    plt.close()
    

    return
