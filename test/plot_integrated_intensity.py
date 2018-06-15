def run(gsqr_bin_list, gsqr_integrated_intensity):

    import matplotlib.pyplot as plt
    
    print "Plotting integrated intensity..."
    
    plt.plot(gsqr_bin_list, gsqr_integrated_intensity)
    plt.savefig('integrated_intensity_vs_gsqr.png')
    plt.close()
    

    return
