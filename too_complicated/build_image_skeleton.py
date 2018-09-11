def run(image_width, image_height):

    from PIL import Image

    print "Building image skeleton..."

    im = Image.new('L', (image_width, image_height), 0)

    return im
