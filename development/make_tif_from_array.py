def run(array, filename, output_folder):

    from PIL import Image

    img = Image.fromarray(array)

    img.save(output_folder + "/" + filename)

    img.close()

    return
