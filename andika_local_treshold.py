import imageio as img # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

def localThres(image,block_size,c):
    imgPad =np.pad(image,pad_width=1,mode='constant', constant_values=0)
    threshold =np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            local_area = imgPad[i:i+block_size,j:j+block_size]
            local_mean = np.mean(local_area) # type: ignore
            threshold[i,j] = 255 if image[i][j] > (local_mean - c) else 0 # type: ignore
    return threshold

image1 = img.imread('C:\Users\komputer 12\Documents\local treshold\cartoon.jpg1',mode='F')
image2 = img.imread('C:\Users\komputer 12\Documents\local treshold\cartoon2.jpg2.')

thres = localThres(image1,15,10)
mask = (thres==255).astype(np.uint8)
segmented = image2 * mask[:,:,np.newaxis]

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(image2)

plt.subplot (1,3,2)
plt.imshow(thres,cmap='gray')


