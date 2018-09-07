def run(gsqr_bin_list, gsqr_integrated_intensity, filename, debug):

    import matplotlib.pyplot as plt
    
    print "Plotting integrated intensity..."
    
    plt.plot(gsqr_bin_list, gsqr_integrated_intensity)
    plt.savefig(filename)
    plt.close()
                
    debug_message = ("\n\n~~~~~~~~~~~~~\nFILENAME = " + __name__ + ".py"
    
    + "\n\nINPUTS:"
    + "\ngsqr_bin_list =" + str(gsqr_bin_list)
    + "\ngsqr_integrated_intensity = " + str(gsqr_integrated_intensity)
    + "\nfilename = " + str(filename)
    + "\ndebug = " + str(debug)
      
    + "\n\nOUTPUTS:"
    + "\nThis function produces the plot:"
    + "\n" + str(filename) 
    + "\n~~~~~~~~~~~~~~~")
    
    
    if debug:
    
        print debug_message

    
    

    return
