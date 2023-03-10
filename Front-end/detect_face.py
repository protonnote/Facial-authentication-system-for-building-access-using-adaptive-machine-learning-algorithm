# import cv2
# import time
# from datetime import datetime
# import os

# # Loading classifiers
# # faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# # noseCascade = cv2.CascadeClassifier('Nariz.xml')
# # mouthCascade = cv2.CascadeClassifier('Mouth.xml')


# video_capture = cv2.VideoCapture(0)
# video_capture.set(3, 640)
# video_capture.set(4, 640)
# video_capture.set(cv2.CAP_PROP_FPS, 60)

# def print_file_size(tfile):
#     File_Size = os.path.getsize(tfile)
#     File_Size_MB = round(File_Size/1024/1024,2)
#     print("Image File Size is " + str(File_Size_MB) + "MB" )

# def find_face():
#     name_face = []
#     img_counter = 1
#     shutter = 0
#     while True:
#         # Reading image from video stream
#         _, img = video_capture.read()
#         # Call method we defined above
#         color = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255)}

#         gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         features = eyesCascade.detectMultiScale(gray_img, 1.1, 20)

#         flag = False
#         for (x, y, w, h) in features:
#             # cv2.rectangle(img, (x,y), (x+w, y+h), color['blue'], 2)
#             # cv2.putText(img, 'eye', (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color["blue"], 1, cv2.LINE_AA)
#             flag = True

#         # coords = draw_boundary(img, eyesCascade, 1.3, 20, color['blue'], "eye")

#         if flag :
#             print(img_counter)
#             img_counter += 1

#         # img = detect(img, faceCascade, eyesCascade, noseCascade, mouthCascade)

#         # output
#         # cv2.imshow("face detection", img)

#         # save picture
#         if img_counter % 10 == 0:
#             shutter += 1
#             current_time =  datetime.now().strftime("%H_%M_%S")
#             img_name = "image_{}_{}.png".format(shutter, current_time)
#             status = cv2.imwrite("pic/"+ img_name, img,[int(cv2.IMWRITE_PNG_COMPRESSION),0])
#             print("{} written!".format(img_name))
#             print("status :",status)
#             print_file_size("pic/"+img_name)
#             name_face.append(img_name)

#             if shutter == 5 :  
#                 print("closing…")
#                 break
#         # if cv2.waitKey(1) & 0xFF == ord('q'):   # ESC pressed
#         #     break

#     # releasing web-cam
#     video_capture.release()
#     # Destroying output window
#     cv2.destroyAllWindows()
#     return name_face


import cv2
import mediapipe as mp
from datetime import datetime
import os


def print_file_size(tfile):
    File_Size = os.path.getsize(tfile)
    File_Size_MB = round(File_Size/1024/1024,2)
    print("Image File Size is " + str(File_Size_MB) + "MB" )

def find_face():

    cap = cv2.VideoCapture(0)
    cap.set(3,480)
    cap.set(4,640)

    mpFaceDection = mp.solutions.face_detection
    mpDraw = mp.solutions.drawing_utils

    faceDection = mpFaceDection.FaceDetection(0.85)
    pTime = 0

    name_face = []
    img_counter = 1
    shutter = 0


    while True :
        _,img = cap.read()

        imgRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        results = faceDection.process(imgRGB)

        flag = False
        # detect face
        if results.detections:
            for id,detection in enumerate(results.detections):
                # mpDraw.draw_detection(img, detection)
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih) , int(bboxC.width * iw) , int(bboxC.height * ih)
                if int(detection.score[0]*100) > 80 :
                    flag = True
                    # cv2.rectangle(img , bbox,(255,0,255),2)
                    # cv2.putText(img, "FPS:{:d}%".format(int(detection.score[0]*100)),(bbox[0],bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 2,(0,255,0),2)
        if flag :
            print(img_counter)
            img_counter += 1
                # print(detection.score)

        if img_counter % 4 == 0:
            shutter += 1
            current_time =  datetime.now().strftime("%H_%M_%S")
            img_name = "image_{}_{}.png".format(shutter, current_time)
            status = cv2.imwrite("pic/"+ img_name, img,[int(cv2.IMWRITE_PNG_COMPRESSION),0])
            print("{} written!".format(img_name))
            print("status :",status)
            print_file_size("pic/"+img_name)
            name_face.append(img_name)

            if shutter == 4 :  
                print("success...")
                break

        #draw fps 
        # cTime = time.time()
        # fps = 1 / (cTime - pTime)
        # pTime = cTime
        # cv2.putText(img, "FPS:{:d}".format(int(fps)),(20,70), cv2.FONT_HERSHEY_PLAIN, 3,(0,255,0),2)

        # part for fix bugs *************************************
        # #render frame 
        # cv2.imshow("Image", img)
        # # kill frame
        # if cv2.waitKey(1) & 0xFF == ord('q'):   # q pressed
        #     break

    # releasing web-cam
    cap.release()
    # Destroying output window
    cv2.destroyAllWindows()
    return name_face