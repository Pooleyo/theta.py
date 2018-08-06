def run(input_image, iteration_step):

    # This function simply moves the files around after the program has run. This is to keep the directory somewhat
    # ordered.

    import subprocess
    import os

    # The first directory in the list should be the 'plots_and_images' directory since it is referenced by index later
    directory_list = ['iter_' + str(iteration_step) + '_plots_and_images',
                      'iter_' + str(iteration_step) + '_logs',
                      'iter_' + str(iteration_step) + '_csv_data']

    for i in directory_list:

        shell_command = ('rm -r ' + i)

        subprocess.call(shell_command, shell=True)

        shell_command = ('mkdir ' + i)

        subprocess.call(shell_command, shell=True)

    shell_command = ('mv *.png ' + directory_list[0])

    subprocess.call(shell_command, shell=True)

    shell_command = ('mv *.tif ' + directory_list[0])

    subprocess.call(shell_command, shell=True)

    # This command moves the input image file we just moved back into the main directory
    os.rename(directory_list[0] + '/' + input_image, './' + input_image)

    return
