def run(filename, x, y):
    
    f = open(filename, 'w')
    for i in range(len(x)):
        f.write(str(x[i]) + "," + str(y[i]) + "\n")
        
    f.close()
    
    return
