def run(filename, x, y, debug):
    
    
    print "Writing data to file..."
    
    
    f = open(filename, 'w')
    for i in range(len(x)):
        f.write(str(x[i]) + "," + str(y[i]) + "\n")
        
    f.close()
    
    
        
    debug_message = ("\n\n~~~~~~~~~~~~~\nFILENAME = " + __name__ + ".py"
    
    + "\n\nINPUTS:"
    + "filename = " + str(filename)
    + "x = " + str(x)
    + "y = " + str(y)
    + "\ndebug = " + str(debug)
    
    + "\n\nOUTPUTS:"
    + "\nThis function writes data to:"
    + "\n" + str(filename)
    + "\n~~~~~~~~~~~~~~~")
    
    
    if debug:
    
        print debug_message

    
    return
