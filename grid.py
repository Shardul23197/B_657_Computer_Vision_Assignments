#Import the Image and ImageFilter classes from PIL (Pillow)
from turtle import width
from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
import sys
import random
from matplotlib.pyplot import fill
import numpy as np
import math
import heapq


def sobel(gray_im):
    xkernel = np.array((
                                (1, 0, -1),
                                (2, 0, -2),
                                (1,0,-1))) / 8.

    ykernel = np.array((
                                (-1, -2, -1),
                                (0, 0, 0),
                                (1,2,1))) / 8.

    xresult = gray_im.filter(ImageFilter.Kernel(
        size=xkernel.shape,
        kernel=xkernel.flatten(),
        scale=1
        ))
    # xresult.show()
    xresult.save('xkernel.png')
    yresult = gray_im.filter(ImageFilter.Kernel(
        size=ykernel.shape,
        kernel=ykernel.flatten(),
        scale=1
        ))
    # yresult.show()
    yresult.save('ykernel.png')
    direction=[[0 for i in range(xresult.height)] for j in range(xresult.width)]
    for i in range(xresult.width):
        for j in range(xresult.height):
            value=math.sqrt(xresult.getpixel((i,j))**2+yresult.getpixel((i,j))**2)
            direction[i][j]=np.arctan2(yresult.getpixel((i,j)),xresult.getpixel((i,j)))*180/np.pi
            xresult.putpixel((i,j),round(value))
            
    # xresult.show()
    # xresult.save("sobel_edge.png")
    return xresult,direction



def cannyThreshold(im):
    high= 120
    low=50
    mid=[]
    for i in range(im.width):
        for j in range(im.height):
            value=im.getpixel((i,j))
            if value>=high:
                im.putpixel((i,j),255)
            elif value<low:
                im.putpixel((i,j),0)
            else:
                mid.append((i,j))
    
    for pixel in mid:
        i,j=pixel[0],pixel[1]
        if im.getpixel((i-1,j)) ==255 or im.getpixel((i+1,j)) ==255 or im.getpixel((i,j-1)) ==255 or im.getpixel((i,j+1)) ==255:
            im.putpixel((i,j),255)
        else:
            im.putpixel((i,j),0)
    return im

def nonMaximalSuppression(im,directions):
    for i in range(160,1470):
        for j in range(600,im.height-1  ):
            value=im.getpixel((i,j))
            if value >0:
                d=directions[i][j]
                if 0 <= d <= 22.5:
                    # if im.getpixel((i+1,j)) >= value:
                    # p=max(im.getpixel((i-1,j)),im.getpixel((i-2,j)),im.getpixel((i-3,j)))
                    # n=max(im.getpixel((i+1,j)),im.getpixel((i+2,j)),im.getpixel((i+3,j)))
                    p=im.getpixel((i-1,j))
                    n=im.getpixel((i+1,j))
                elif  158 <= d<= 180:
                    # if im.getpixel((i,j-1)) >=value:
                    # p=max(im.getpixel((i,j-1)),im.getpixel((i,j-2)),im.getpixel((i,j-3)))
                    # n=max(im.getpixel((i,j+1)),im.getpixel((i,j+2)),im.getpixel((i,j+3)))
                    p=im.getpixel((i,j-1))
                    n=im.getpixel((i,j+1))

                elif 22.5<=d<=67.5:
                    # p=max(im.getpixel((i+1,j-1)),im.getpixel((i+2,j-2)),im.getpixel((i+3,j-3)))
                    # n=max(im.getpixel((i-1,j+1)),im.getpixel((i-2,j+2)),im.getpixel((i-3,j+3)))
                    p=im.getpixel((i+1,j-1))
                    n=im.getpixel((i-1,j+1))
                elif 67.5<= d<= 112.5:
                    # p=max(im.getpixel((i,j+1)),im.getpixel((i,j+2)),im.getpixel((i,j+3)))
                    # n=max(im.getpixel((i,j-1)),im.getpixel((i,j-2)),im.getpixel((i,j-3)))
                    p=im.getpixel((i,j+1))
                    n=im.getpixel((i,j-1))
                elif 112.5<=d<=157.5:
                    # p=max(im.getpixel((i-1,j-1)),im.getpixel((i-2,j-2)),im.getpixel((i-3,j-3)))
                    # n=max(im.getpixel((i+1,j+1)),im.getpixel((i+2,j+2)),im.getpixel((i+3,j+3)))
                    p=im.getpixel((i-1,j-1))
                    n=im.getpixel((i+1,j+1))
                else:
                    k=0
                if not (im.getpixel((i,j))>p and im.getpixel((i,j))>n):
                    im.putpixel((i,j),0)
                    
    im.save("nonMax.png")
    return im
    







def getHoughPoints(im):
    thetas=np.deg2rad([0,90])
    pointsV={}
    pointsH={}
    for i in range(160,1470):
    # for i in range(160,300):
        for j in range(600,im.height-1):
        # for j in range(600,900):
            if im.getpixel((i,j))>0:
                for theta in thetas:
                    row=(-1*(i)*np.cos(theta))+(j*np.sin(theta))
                    k=(round(row),theta)
                    if theta!=0:
                        pointsV[k]=pointsV.get(k,0)+1
                    else:
                        pointsH[k]=pointsH.get(k,0)+1
    return pointsV,pointsH


def getHoughparamsV(points, im,color_im):
    k=heapq.nlargest(56,points.items(),key=lambda x:x[1])
    # (row,theta)=k[1][0]
    im1=ImageDraw.Draw(color_im)
    im2=ImageDraw.Draw(im)
    for k,line in enumerate(k):
        (row,theta)=line[0]
        linePoints=[]
        for i in range(160,1470):
            j=(row+(i*np.cos(theta)))/np.sin(theta)
            # if j==float('-inf'):
            #     j=0

            if j<im.height and j>=0:
                linePoints.append((i,j))
        im1.line(linePoints,fill='red',width=1)
        im2.line(linePoints,fill='red',width=1)
        # color_im.show()
    color_im.save('sample.png')
    im.save('sobelsample.png')


def getHoughparamsH(points, im,color_im):
    k=heapq.nlargest(30,points.items(),key=lambda x:x[1])
    # (row,theta)=k[1][0]
    im1=ImageDraw.Draw(color_im)
    im2=ImageDraw.Draw(im)
    for k,line in enumerate(k):
        (row,theta)=line[0]
        linePoints=[]
        for j in range(600,im.height):
            i=((j*np.sin(theta))-row)/np.cos(theta)
            # if i==float('-inf'):
            #     j=0

            if 160<=i<=1470:
                linePoints.append((i,j))
        im1.line(linePoints,fill='red',width=1)
        im2.line(linePoints,fill='red',width=1)
        # color_im.show()
    color_im.save('sample.png')
    im.save('sobelsample.png')




            





if __name__ == '__main__':
    # Load an image 
    im = Image.open('blank_form.jpg')
    # example=Image.open('c-33.jpg')
    
    gray_im = im.convert("L")
    gray_im.show()
   
    # sobel edge detection
    sobel_im,directions=sobel(gray_im)
    sobel_im.save('sobel_im.png')

    
    canny_im=nonMaximalSuppression(sobel_im,directions)
    canny_im=cannyThreshold(canny_im)
    # for i in range(160,1470):
    #     for j in range(600,im.height-1  ):
    #         if 0<canny_im.getpixel((i,j))<255:
    #             wait=1
    canny_im.save('canny_im.png')
    # get Hough points
    pointsV,pointsH=getHoughPoints(canny_im)

    # get Hough lines
    getHoughparamsV( pointsV,canny_im,im)
    getHoughparamsH( pointsH,canny_im,im)







    

    # # Check its width, height, and number of color channels
    # print("Image is %s pixels wide." % im.width)
    # print("Image is %s pixels high." % im.height)
    # print("Image mode is %s." % im.mode)

    # # Pixels are accessed via an (X,Y) tuple.
    # # The coordinate system starts at (0,0) in the upper left-hand corner,
    # # and increases moving right (first coordinate) and down (second coordinate).
    # # So it's a (col, row) indexing system, not (row, col) like we're used to
    # # when dealing with matrices or 2d arrays.
    # print("Pixel value at (10,10) is %s" % str(im.getpixel((10,10))))
    
    # # Pixels can be modified by specifying the coordinate and RGB value
    # # (255, 0, 0) is a pure red pixel.
    # im.putpixel((10,10), (255, 0, 0))
    # print("New pixel value is %s" % str(im.getpixel((10,10))))

    # # Let's create a grayscale version of the image:
    # # the "L" means there's only a single channel, "Lightness"
    # gray_im = im.convert("L")
    
    # # Create a new blank color image the same size as the input
    # color_im = Image.new("RGB", (im.width, im.height), color=0)
    # gray_im.save("gray.png")
    
    # # Highlights any very dark areas with yellow.
    # for x in range(im.width):
    #     for y in range(im.height):
    #         p = gray_im.getpixel((x,y))
    #         if p < 5:
    #             (R,G,B) = (255,255,0)
    #             color_im.putpixel((x,y), (R,G,B))
    #         else:
    #             color_im.putpixel((x,y), (p,p,p))

    # # Show the image. We're commenting this out because it won't work on the Linux
    # # server (unless you set up an X Window server or remote desktop) and may not
    # # work by default on your local machine. But you may want to try uncommenting it,
    # # as seeing results in real-time can be very useful for debugging!
    # # color_im.show()

    # # Save the image
    # color_im.save("output.png")

    # # This uses Pillow's code to create a 5x5 mean filter and apply it to
    # # our image. In the lab, you'll need to write your own convolution code (using
    # # "for" loops, but you can use Pillow's code to check that your answer is correct.
    # # Since the input is a color image, Pillow applies the filter to each
    # # of the three color planes (R, G, and B) independently.
    # box = [1]*25
    # result = color_im.filter(ImageFilter.Kernel((5,5),box,sum(box)))
    # # result.show()
    # result.save("output2.png")
