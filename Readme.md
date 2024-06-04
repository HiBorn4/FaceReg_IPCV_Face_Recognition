1. The numbers present in "obj.names" file are mapped to roll numbers using the "obj_roll_num.json".
2. The object ids' used in the annotations are the index of each number in the "obj.names" file starting from 0. Example: the number '3' is mapped to object_id '24' in the annotation files (.txt file) [it represents the roll number "21BCS011"] and number '8' is mapped to object_id '4' in the annotations [it represents the roll number "21BCS033"].

Problem Statement:
Attached is the DataseV2.0t.zip folder containing the faces collected during the course. The annotations are rectified.
Attached is test.zip folder containing the images taken in the classroom for recording attendance.

Your task is to train a deep learning model for identifying the faces in the test.zip by using the images in DataseV2.0t.zip

If you succeed in building the model meet me and discuss in August 2024.

Hint:
You need to augment the training images to create additional images for training the deep learning model. This process is called as Data Augmentation. Once the model is trained then check the correctness of the trained model using the test images.