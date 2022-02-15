import cv2
import math
import glob

video_path = 'video/*' # path de onde estão os vídeos
frame_path = 'frames_generated/' #path de onde serão salvos os vídeos



i = 0



for video in glob.glob(video_path):
        videoPath = video
        video = video.split('/')[-1]

        print(video)
        videoName = video

        framePath = frame_path

        cap = cv2.VideoCapture(videoPath)
        frameRate = cap.get(5) # Frame rate


        cont = 0
        while(cap.isOpened()):
            frameId = cap.get(1) # Current frame number
            ret, frame = cap.read()
            if ret == False:
                break
            if (frameId % math.floor(frameRate) == 0):
                    cv2.imwrite(framePath + videoName[:-4] + '_Frame' + str(cont) + '.png', frame)
                    print(str(cont) + ' FRAMES SAVED')
                    cont += 1




        cap.release()
        print("Done!")