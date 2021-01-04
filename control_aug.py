import cv2 
import numpy as np

def augmented_rotate(image,degree):
    rows,cols,_ = image.shape
    
    M = cv2.getRotationMatrix2D((cols/2,rows/2),degree,1)
    dst = cv2.warpAffine(image,M,(cols,rows))
    
    dst = dst.reshape(dst.shape[0],dst.shape[1],3)
    
    return dst

def augmented_translate(image,value):
    rows,cols,_ = image.shape
    temp = []
    vector = value['vector']
    axis = value['axis']
    flip = value['flip']

    if axis == 'xy':
        vector = value['vector'].split(",")
        vector={'x':int(vector[0]),'y':int(vector[1])}
    else:
        vector={axis:int(value['vector'])}
    
    if flip:
        image = cv2.flip(image,1)
    
    if axis == 'x':
        M = np.float32([[1,0,vector['x']],[0,1,0]])
        dst = cv2.warpAffine(image,M,(cols,rows))
        
    elif axis == 'y':
        M = np.float32([[1,0,0],[0,1,vector['y']]])
        dst = cv2.warpAffine(image,M,(cols,rows))
    
    elif axis == 'xy':
        M = np.float32([[1,0,vector['x']],[0,1,vector['y']]])
        dst = cv2.warpAffine(image,M,(cols,rows))
    
    return dst