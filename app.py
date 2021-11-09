from flask import Flask,jsonify,request,render_template
import numpy as np
from keras.models import load_model as ld
from keras.preprocessing import image as imm
import cv2
import mtcnn


#Mtcnn face detection Method
detector = mtcnn.MTCNN()

# Select Haarcascade_frontalface_alt for opencv face detection
# opencv_default_cascade = '/cascade/data/haarcascade_frontalface_alt.xml'
# cascade = cv2.CascadeClassifier(opencv_default_cascade)

#Loading Emotion Detetion model
emotion_model = ld('model/model.h5')

#Defining emotion class_labels dictionary
class_labels={0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Neutral', 5: 'Sad', 6: 'Surprise'}

#Threshold for predicting emotion
#emotion_threshold = 0.6

#Creating a Flask app
app = Flask(__name__)

# Configure a secret SECRET_KEY
app.config['SECRET_KEY'] = 'apikeyplayemo0'

#Allowed extensions
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])

#A decorator for the flask application routes to be dynamically modified
#Requests methods are GET/POST
@app.route("/", methods=['POST','GET'])


def index():
    if(request.method == 'POST'):   
        try:

            # Get Image file Object from Users Post Request
            image_obj = request.files.get(key='image')
            img = image_obj.read()
            #image_file= image_obj.filename

            #Convert string to array
            image = cv2.imdecode(np.fromstring(img, np.uint8), cv2.IMREAD_UNCHANGED)
            
            #Face Detection on Image Using Mtcnn
            face = detect_face_mtcnn(image)
            
            #If a face is detected
            if face is True:
                
                #Predict Emotion
                result = emotion_prediction(emotion_model,'temp/capture.jpg')
                return jsonify({'result':result})
            
            else:

                return jsonify({'result':'No Face or More than 1(One) face in Frame'})
        
        except Exception as e:

           return  jsonify({"Error":str(e)})
    
    elif(request.method == 'GET'):

        #Renderss Index.html if a get request is recieved
        return render_template('index.html')        
    
    else:
    
        return  jsonify({"Help":"Send a Post request with image as a key in files dictionary.","Python":"""import requests
url = 'https://emoplay.herokuapp.com'
requests.post(url, files={'image': open('local_path_to_your_image_file', 'rb')})"""})


def detect_face_mtcnn(img):
    #read image
    #true_img = imm.load_img(image)
    #image to array
    #img = imm.img_to_array(true_img)
    #img =cv2.imread(image)


    try:
    
        #Using mtcnn detector to detect faces
        detected_faces = detector.detect_faces(img)
        #If only one face is detected
        if len(detected_faces)==1:
            
            face = detected_faces[0]

            #Getting the face's coordinates on image,frame
            x, y, width, height =face['box']

            #cropping out detected face and write to temporary path
            cv2.rectangle(img, (x,y), (x+width,y+height), (0,255,0), 2)
            detected_face_crop = img[y:y+height, x:x+width]
            #save_image=imm.array_to_img(detected_face_crop)
            #save_image.save("temp/capture.jpg',detected_face_crop")
            cv2.imwrite('temp/capture.jpg',detected_face_crop) 
            
            return True
        
        else:

                return False  
    
    except Exception as e:
        
        return str(e)
      

def emotion_prediction(emotion_model,image_path):

    #loading image with with shape [48,48] to fit model's input shape
    img = imm.load_img(image_path,color_mode="grayscale",target_size=(48,48))
    
    #converting image pixels to array
    img_array = imm.img_to_array(img)

    #Image Preprocessing
    img_array = np.expand_dims(img_array,axis=0)
    img_array /=255

    #Using Emotion Model to make Prediction
    custom =emotion_model.predict(img_array)
    prediction = class_labels[custom[0].argmax()]
    return prediction
    
    #Using a threshold for predicted Emotion
    #  index= custom[0].argmax()
    #  if custom[0][index]>=emotion_threshold:
    #     prediction = class_labels[index]
    #     return prediction
    # else:
    #     prediction='Emotion not Recognized'
    #     return prediction  

                  

#Using opencv for Face detection
# def detect_face_opencv(image):  
#     img = cv2.imread(image)
#     try:
#         size = (img.shape[1],img.shape[0])
#         frame = cv2.resize(img, size)
#         detected_faces = cascade.detectMultiScale(frame,1.05,8)
#         if len(detected_faces)==1:
#             for face in detected_faces:
#                 x, y, width, height = [pixel for pixel in face]
#                 cv2.rectangle(img, (x,y), (x+width,y+height), (0,255,0), 2)
#                 detected_face_crop = img[y:y+height, x:x+width]
#                 cv2.imwrite('capture.jpg',detected_face_crop)
#                 print('writing')
#                 return True
#         else:
#             return False
#     except Exception as e:
#         return str(e)

#Run Flask App
if __name__ == '__main__':
   app.run(debug=True)




