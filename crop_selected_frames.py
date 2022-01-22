import cv2
import math
import glob

video_path = 'video/*' # path de onde estão os vídeos
frame_path = 'frames_selected/' #path de onde serão salvos os vídeos
isWindows = False #se usar no windows
scale_image_reduction_percentage = 70 # % - porcentagem da escala da imagem em relação à original, para caber em seu monitor
seconds_per_frame = 0.1 # taxa de atualização de frames

if isWindows:
     nextKey = 2555904
     previousKey = 2424832
     printKey = 'p' # caso esteja no windows, aperte p e observe o número, em seguida, coloque-o aqui, no lugar de 'p'
else:
     nextKey = 65363
     previousKey = 65361
     printKey = 112


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
                scale_percent = scale_image_reduction_percentage
                width = int(frame.shape[1] * scale_percent / 100)
                height = int(frame.shape[0] * scale_percent / 100)
                dim = (width, height)

                resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
                cv2.imshow('frame',resized)
                k = cv2.waitKeyEx(0)
                print(k)
                if k == nextKey:
                    cont += seconds_per_frame
                if k == previousKey:
                    cont -= seconds_per_frame
                if k == printKey:
                    cv2.imwrite(framePath + videoName[:-4] + '_Frame' + str(cont) + '.png', frame)
                    print(str(cont) + ' FRAMES SAVED')
                    cont += seconds_per_frame




        cap.release()
        print("Done!")