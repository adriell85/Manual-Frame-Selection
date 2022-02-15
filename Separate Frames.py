import cv2
import math
import glob
import numpy as np
from natsort import natsorted

input_path = 'frames_generated/*' # path de onde estão os vídeos
output_path = 'frames_separated/' #path de onde serão salvos os vídeos
isWindows = False #se usar no windows
scale_image_reduction_percentage = 70 # % - porcentagem da escala da imagem em relação à original, para caber em seu monitor
 # taxa de atualização de frames

if isWindows:
     nextKey = 2555904
     previousKey = 2424832
     printKey = 'p' # caso esteja no windows, aperte p e observe o número, em seguida, coloque-o aqui, no lugar de 'p'
else:
     nextKey = 65363
     previousKey = 65361
     printKey = 112

flag = True



frame_names = glob.glob(input_path)

frame_names_len = len(frame_names)
cont = 0


frame_names = natsorted(frame_names)

while(flag):

        frame = frame_names[cont]
        videoPath = frame_names[cont]
        frame_name = videoPath.split('/')[-1]

        print(frame)


        framePath = output_path

        frame = cv2.imread(videoPath)






        scale_percent = scale_image_reduction_percentage
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dim = (width, height)

        resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('frame',resized)
        k = cv2.waitKeyEx(0)
        print(k)
        if k == nextKey:
            cont += 1
        if k == previousKey:
            cont -= 1
        if k == printKey:
            cv2.imwrite(framePath + frame_name[:-4] + '_Frame' + str(cont) + '.png', frame)
            print(str(cont) + ' FRAMES SAVED')
            cont += 1

        if cont == frame_names_len-1:
            print('congratulations, the frame is done!')
            cv2.destroyWindow(0)
        # cv2.destroyWindow(0)




