def run(image_width, image_height):

    import PIL
    from PIL import Image
    
    im = Image.new('L', (image_width, image_height), 255)
    
    return im
