#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Chinemebudu Chimela Maxwell
# DATE CREATED: 05/12/2022                              
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
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
    # Replace None with the results_dic dictionary that you created with this
    # function
    
    file_list = listdir(image_dir) #Creates a list that contains image file names
    results_dic = {} #Creates an empty dictionary

    for idx in range(0, len(file_list), 1): # Iterate through the list to extract pet names
        if file_list[idx][0] != ".": # skips a file if it starts with "."
            file_name = file_list[idx].split('_') # Splitting a file name into a list.
            pet_label = ""
            for word in file_name:
                if word.isalpha(): # checks if the word making up file name, contains only alphabets
                    pet_label += word + " " # Stores word in pet_label if it has space at the end
            pet_label = pet_label.lower().strip() # makes the pet name lower case and trailing spaces
            if file_list[idx] not in results_dic:
                    results_dic[file_list[idx]] = [pet_label] # Assigns the value pet name to the filename serving as it's key. 
            else:
                print("**warning: Duplicate files exist in directory: {}".format(file_list[idx]))  # prints a warning message if duplicate name if found              
                    
    return results_dic