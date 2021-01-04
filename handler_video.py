import cv2
import numpy as np

def video2frame(file_video):
    cap= cv2.VideoCapture(file_video)
    fps = cap.get(cv2.CAP_PROP_FPS)

    frame_arr = []
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        
        frame_arr.append(frame)
    
    return np.array(frame_arr),fps

def frame2video(frame_array,fps,pathOut):
    height, width, layers = frame_array[0].shape
    size = (width,height)

    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()