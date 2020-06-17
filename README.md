***READ ME***

## Requirements

1. Python 3
2. Homebrew
3. Xcode
4. Install PIP
5. Libraries for python 3:
	1. Open CV3
	2. Numpy
	3. matplotlib
	4. face_recognition based on Open Face
	5. Image

Links:  http://www.pyimagesearch.com/2016/12/05/macos-install-opencv-3-and-python-3-5/
	http://www.pyimagesearch.com/2016/12/05/macos-install-opencv-3-and-python-3-5/
	https://pypi.python.org/pypi/face_recognition#downloads



## Method-1 using OpenCV, Haarcascade and LBPHF Face Recognizer

### Files:
Face_rec.py (main implementation file)
HaarCascade: Face Detection file (.xml format)
Location to be provided at the top of the Python file
Yale faces: Collection of images for testing. 15 subjects with 10 subjects for each.
learning_data.xml: If we want to store the learning of the program we can do that like this file.
The instruction to save and load the learning are commented inside the Python file.


### Implementation:

1. Open the Face_rec.py file and run the module to see the implementation.
2. I have added comments in the program to help understand the code.
3. The code gets all the images from the Yale Faces folder to learn the faces for each subject except .sad images. We will use the .sad faces for each subject to recognize him with confidence.
4. Lower the confidence the better it is.  .50 is a decent threshold. 0.40 would be better but would need much better images to recognise with that confidence.
5. Face Cascade(haarCascade) is used to detect the face in the image.
6. Labels are the subject name. We have used numbers in our case.
7. Basically, the images and labels function detects the faces and appends it in the form of a numpy array into a list. The labels are appended into a different list but in the exact same order as the faces list.
8. Then we train the recignizer by giving the NUMPY array of faces and Labels in NUMPY array format too as inputs.
9. Final step is finding the .sad images for each subject, detecting the faces in each image and finally comparing this image to the trained images. This is done in line 85 with recognizer.predict function.


### Pros:
-> This method gets better with more and more images.
### Cons:
-> It is slower as it takes the image-to-compare and tries to match it with every image in it\'92s database.
-> So, a database with 5000 images will take 5000x time.
-> It requires about 10 images to start off with also.


## Method-2 using Face_Recognition(OpenFace) (Neural Engine)

Go to examples folder to see the python files. They are named pretty comprehensively so should't be problem.

The main file is facerec_from_webcam_faster.py

There is folder names Recognzed_faces where you need to put the photos of all the people you want the algorithm to train for. 
Note: Please put 1 photo per person. Try with 3-4 photos first as the time to train increases with every photo added.

### Implementation:
1. My file uses the webcam to detect faces but you can also use images to do so.
2. It pulls out the video from the Webcam, scales it down to 1/4 resolution and detects every second frame to save computing power.
3. You will have to change the path according to your location of recognized faces.
4. The code is pretty comprehensive on it\'92s own. Few things to note though:
	1. The huge commented out region in the middle which says 'pickle' is used for saving the learnings.
	2. What it basically does is saves the Neural scans list and the corresponding Image Names list. Pickle is used to save these lists. It saves them as .txt files in the same folder as your python file.
	3. You can then read these learning using the same method(pickle). The code is there in the file but commented out.

### Pros:
1. Very fast method as it uses neural scans to learn the image. Basically, it takes out mathematical distances of each face.
2. Works easily on very large databases as we have to compare only numbers and not images.
3. Same fundamental technology used by almost all major corporations like Facebook and Google.

### Cons:
1. It uses only 1 image per person so it does not get better with each implementation.

# Additional Files:
There is a testing OpenCV installation folder where you can check if you have installed OpenCV correctly by running the python script. It basically converts an image to B&W.
