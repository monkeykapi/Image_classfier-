# Imports python modules
from os import listdir


# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function
#
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    in_files = listdir(image_dir)
    path = "pet_images/"
    dic = listdir(path)
    # Processes each of the files to create a dictionary where the key
    # is the filename and the value is the picture label (below).
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()

    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for idx in range(0, len(in_files), 1):
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it
        # isn't an pet image file
        if in_files[idx][0] != ".":
            # Creates temporary label variable to hold pet label name extracted
            pet_label = ""
            pet_file_name = in_files[idx]
            lower_file_name = pet_file_name.lower()
            word_list = lower_file_name.split("_")
            for word in word_list:
                if word.isalpha():
                    pet_label += word + " "
            print("filename = {} Pet label = {}".format(in_files[idx], pet_label))
        if dic[idx] not in results_dic:
            results_dic[dic[idx]] = [pet_label.strip()]# results_dic[filenames[idx]] = [pet_labels[idx]]
        else:
            print("the filename exisit here")
            # TODO: 2a. BELOW REPLACE pass with CODE that will process each
            #          filename in the in_files list to extract the dog breed
            #          name from the filename. Recall that each filename can be
            #          accessed by in_files[idx]. Be certain to place the
            #          extracted dog breed name in the variable pet_label
            #          that's created as an empty string ABOVE

            # If filename doesn't already exist in dictionary add it and it's
            # pet label - otherwise print an error message because indicates
            # duplicate files (filenames)
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]
            else:
                print("** Warning: Duplicate files exist in directory:",in_files[idx])

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic

