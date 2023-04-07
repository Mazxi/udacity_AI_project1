# Pretrained Dog Image Classifier Using Pytorch.

This project is the my first project in the Artificial intelligence nano degree program and is a prerequiste to graduate. 

## OBJECTIVE
The aim of this project is to use a pretrained dog image classifier to classify dog images.

## Main files in this repository are;
* `get_input_args.py` : A python file that retrieves and parses the command line arguments provided by the user when the run the program.
* `get_pet_labels.py` : This file created a dictionary of petlabels based upon the filenames of the image file.
* `classify_images.py` : This file creates classifier labels with classifier function, compares pet labelsto the classifier labels, and adds the classifier labels and the comparison of the labels to the dictionary created in `get_pet_labels.py` using the extend functions
* `adjust_results4_isadog.py` : This file adjust the results dictionary to determine if the classifier correctly classifier images 'as dog' and 'not a dog'
* `calculates_results_stats.py` : This calculates the result of the program when it been ran using the classifier's model architecture to classify images.
* `print_results.py` : This contains code that prints out summary result on the classification task.


## Author
Maxwell Chinemebudu Chimela
* cchimelamaxwell@gmail.com
* [LinkedIn](www.linkedin/in/maxwell-the-analyst)
