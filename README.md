# Computer Vision RPS

# Used Teachable-Machine to create a model

 Used the website Teach-able Machine to create a model:

https://teachablemachine.withgoogle.com


 Each class was trained with images shown to the camera of the three options in the game: rock, paper, scissor.  The "Nothing" class represents the lack of option in the image.

# Download the model 

once the model had been created using the platform above, the model was downloaded from the "Tensorflow" tab in Teachable-Machine. 
The model was named keras_model.h5 and the text file containing the labels was named labels.txt.

The downloaded files contain the structure and the parameters of a deep learning model.
*They are not files that can be run, and they do not contain anything readable if you look inside.*

# Creating a new conda virtual enviroment 

A new virtual conda enviroment was created by inputting and running the following commands in the terminal:

conda create -n "name_of_new_env"

which was followed by the name of the env created

The conda enviroment was then activated by inputting and running the following command in the terminal followed by the name of the enviroment: 

conda activate "name_of_new_env"

# Installing the necessary libraries 

The following three libraries were installed using pip( a python packaage manager) and by inputting and running the following comands in the terminal 

pip install name_of_library/package

The following three libraries were installed using the above commands : 
*opencv-python, tensorflow, and ipykernel*

# Creating a requirments test file

A requirments file is a file that enables any other user that wants to use your computer to easily install the exact dependencies by running pip install requirements.txt.

A requirements.txt file was created by running the following command:

pip list > requirements.txt



