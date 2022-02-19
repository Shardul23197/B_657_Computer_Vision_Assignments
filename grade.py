#Import the Image and ImageFilter classes from PIL (Pillow)
# from turtle import width
from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
import sys
import random
# from matplotlib.pyplot import fill
import numpy as np
import math
import heapq
# from sklearn.cluster import MeanShift 
# from matplotlib import pyplot as plt




def sobel(gray_im):
    xkernel = np.array((
                                (1, 0, -1),
                                (2, 0, -2),
                                (1,0,-1))) /8.

    ykernel = np.array((
                                (-1, -2, -1),
                                (0, 0, 0),
                                (1,2,1))) /8.

    xresult = gray_im.filter(ImageFilter.Kernel(
        size=xkernel.shape,
        kernel=xkernel.flatten(),
        scale=1
        ))
    # xresult.show()
    # xresult.save('xkernel.png')
    yresult = gray_im.filter(ImageFilter.Kernel(
        size=ykernel.shape,
        kernel=ykernel.flatten(),
        scale=1
        ))
    # yresult.show()
    # yresult.save('ykernel.png')
    result = Image.new(mode="L", size=(xresult.width, xresult.height))
    direction=[[0 for i in range(xresult.height)] for j in range(xresult.width)]
    for i in range(xresult.width):
        for j in range(xresult.height):
            value=math.sqrt(xresult.getpixel((i,j))**2+yresult.getpixel((i,j))**2)
            direction[i][j]=np.arctan2(yresult.getpixel((i,j)),xresult.getpixel((i,j)))*180/np.pi
            result.putpixel((i,j),round(value))
            
    # xresult.show()
    # xresult.save("sobel_edge.png")
    return xresult,yresult,result,direction



# def cannyThreshold(im):
#     high= 70
#     low=40
#     mid=[]
#     intensity=[]
#     for i in range(160,1470):
#         for j in range(670,im.height-1):
#             value=im.getpixel((i,j))
#             intensity.append(value)
#             if value>=high:
#                 im.putpixel((i,j),255)
#             elif value<low:
#                 im.putpixel((i,j),0)
#             else:
#                 mid.append((i,j))
#                 # im.putpixel((i,j),0)
    
#     for pixel in mid:
#         i,j=pixel[0],pixel[1]
#         if im.getpixel((i-1,j)) ==255 or im.getpixel((i+1,j)) ==255 or im.getpixel((i,j-1)) ==255 or im.getpixel((i,j+1)) ==255:
#             im.putpixel((i,j),255)
#         else:
#             im.putpixel((i,j),0)
#     return im


def cannyThreshold_axis(imx,imy):
    high= 70
    low=40
    midx=[]
    midy=[]
    for i in range(160,1470):
        for j in range(670,imx.height-1):
            value=imx.getpixel((i,j))
            if value>=high:
                imx.putpixel((i,j),255)
            elif value<low:
                imx.putpixel((i,j),0)
            else:
                midx.append((i,j))
                # im.putpixel((i,j),0)
            value=imy.getpixel((i,j))
            if value>=high:
                imy.putpixel((i,j),255)
            elif value<low:
                imy.putpixel((i,j),0)
            else:
                midy.append((i,j))
    
    for pixel in midx:
        i,j=pixel[0],pixel[1]
        if imx.getpixel((i-1,j)) ==255 or imx.getpixel((i+1,j)) ==255 or imx.getpixel((i,j-1)) ==255 or imx.getpixel((i,j+1)) ==255:
            imx.putpixel((i,j),255)
        else:
            imx.putpixel((i,j),0)
    for pixel in midy:
        i,j=pixel[0],pixel[1]
        if imy.getpixel((i-1,j)) ==255 or imy.getpixel((i+1,j)) ==255 or imy.getpixel((i,j-1)) ==255 or imy.getpixel((i,j+1)) ==255:
            imy.putpixel((i,j),255)
        else:
            imy.putpixel((i,j),0)
    # imx.save("canny_imx.png")
    # imy.save("canny_imy.png")
    return imx,imy

# def nonMaximalSuppression(im,directions):
#     for i in range(160,1470):
#         for j in range(670,im.height-1  ):
#             value=im.getpixel((i,j))
#             if value >0:
#                 d=directions[i][j]
#                 if 0 <= d <= 22.5:
#                     p=max(im.getpixel((i-1,j)),im.getpixel((i-2,j)),im.getpixel((i-3,j)),im.getpixel((i-4,j)),im.getpixel((i-5,j)))
#                     n=max(im.getpixel((i+1,j)),im.getpixel((i+2,j)),im.getpixel((i+3,j)),im.getpixel((i+4,j)),im.getpixel((i+5,j)))
#                 elif  158 <= d<= 180:
#                     # if im.getpixel((i,j-1)) >=value:
#                     p=max(im.getpixel((i,j-1)),im.getpixel((i,j-2)),im.getpixel((i,j-3)),im.getpixel((i,j-4)),im.getpixel((i,j-5)))
#                     n=max(im.getpixel((i,j+1)),im.getpixel((i,j+2)),im.getpixel((i,j+3)),im.getpixel((i,j+4)),im.getpixel((i,j+5)))
#                     # p=im.getpixel((i,j-1))
#                     # n=im.getpixel((i,j+1))

#                 elif 22.5<=d<=67.5:
#                     p=max(im.getpixel((i+1,j-1)),im.getpixel((i+2,j-2)),im.getpixel((i+3,j-3)),im.getpixel((i+4,j-4)),im.getpixel((i+5,j-5)))
#                     n=max(im.getpixel((i-1,j+1)),im.getpixel((i-2,j+2)),im.getpixel((i-3,j+3)),im.getpixel((i-4,j+4)),im.getpixel((i-5,j+5)))
#                 elif 67.5<= d<= 112.5:
#                     p=max(im.getpixel((i,j+1)),im.getpixel((i,j+2)),im.getpixel((i,j+3)),im.getpixel((i,j+4)),im.getpixel((i,j+5)))
#                     n=max(im.getpixel((i,j-1)),im.getpixel((i,j-2)),im.getpixel((i,j-3)),im.getpixel((i,j-4)),im.getpixel((i,j-5)))
#                 elif 112.5<=d<=157.5:
#                     p=max(im.getpixel((i-1,j-1)),im.getpixel((i-2,j-2)),im.getpixel((i-3,j-3)),im.getpixel((i-4,j-4)),im.getpixel((i-5,j-5)))
#                     n=max(im.getpixel((i+1,j+1)),im.getpixel((i+2,j+2)),im.getpixel((i+3,j+3)),im.getpixel((i+4,j+4)),im.getpixel((i+5,j+5)))
#                 if not (im.getpixel((i,j))>=p and im.getpixel((i,j))>=n):
#                     im.putpixel((i,j),0)
                    
#     im.save("nonMax.png")
#     return im


def nonMaximalSuppression_axis(imy,imx):
    for i in range(160,1470):
        for j in range(670,imx.height-1  ):
            # xvalue
            value=imx.getpixel((i,j))
            if value >0:
                p=max(imx.getpixel((i,j+1)),imx.getpixel((i,j+2)),imx.getpixel((i,j+3)),imx.getpixel((i,j+4)),imx.getpixel((i,j+5)))
                n=max(imx.getpixel((i,j-1)),imx.getpixel((i,j-2)),imx.getpixel((i,j-3)),imx.getpixel((i,j-4)),imx.getpixel((i,j-5)))
                
                if not (imx.getpixel((i,j))>=p and imx.getpixel((i,j))>=n):
                    imx.putpixel((i,j),0)
            
            # yresult
            value=imy.getpixel((i,j))
            if value >0:
                p=max(imy.getpixel((i-1,j)),imy.getpixel((i-2,j)),imy.getpixel((i-3,j)),imy.getpixel((i-4,j)),imy.getpixel((i-5,j)))
                n=max(imy.getpixel((i+1,j)),imy.getpixel((i+2,j)),imy.getpixel((i+3,j)),imy.getpixel((i+4,j)),imy.getpixel((i+5,j)))
                
                if not (imy.getpixel((i,j))>=p and imy.getpixel((i,j))>=n):
                    imy.putpixel((i,j),0)       
    # imx.save("nonMax_xresult.png")
    # imy.save("nonMax_yresult.png")
    return imx,imy
    




def getHoughPoints_axis(imx,imy):
    thetas=np.deg2rad([0,90])
    pointsV={}
    pointsH={}
    for i in range(160,1470):
    # for i in range(160,300):
        for j in range(670,imx.height-1):
        # for j in range(600,900):
            # if im.getpixel((i,j))>0:
            for theta in thetas:
                # row=(-1*(i)*np.cos(theta))+(j*np.sin(theta))
                # row=round(row)
                # k=(row,theta)
                if theta!=0:
                    # imx.show()
                    if imx.getpixel((i,j))>0:
                        row=(-1*(i)*np.cos(theta))+(j*np.sin(theta))
                        row=round(row)
                        k=(row,theta)
                        pointsV[k]=pointsV.get(k,0)+1      
                else:
                    # imy.show()
                    if imy.getpixel((i,j))>0:
                        row=(-1*(i)*np.cos(theta))+(j*np.sin(theta))
                        row=round(row)
                        k=(row,theta)
                        pointsH[k]=pointsH.get(k,0)+1
                            
    return pointsV,pointsH


# def getHoughPoints(im):
#     thetas=np.deg2rad([0,90])
#     pointsV={}
#     pointsH={}
#     for i in range(160,1470):
#     # for i in range(160,300):
#         for j in range(670,im.height-1):
#         # for j in range(600,900):
#             if im.getpixel((i,j))>0:
#                 for theta in thetas:
#                     row=(-1*(i)*np.cos(theta))+(j*np.sin(theta))
#                     row=round(row)
#                     k=(row,theta)
#                     if theta!=0:
#                         pointsV[k]=pointsV.get(k,0)+1      
#                     else:
#                         pointsH[k]=pointsH.get(k,0)+1
                            
#     return pointsV,pointsH


def getHoughparamsV(points, im,color_im):
    k=heapq.nlargest(len(points),points.items(),key=lambda x:x[1])
    # (row,theta)=k[1][0]
    setV=set()
    Vpoints=[]
    im1=ImageDraw.Draw(color_im)
    im2=ImageDraw.Draw(im)
    for index,line in enumerate(k):
        (row,theta)=line[0]
        linePoints=[]
        if len(setV)>=58:
            break;
        neigh={row+i for i in range(-12,13)}
        neigh.remove(row)
        # l=0
        if not neigh.intersection(setV):
            setV.add(row)
            for i in range(160,1470):
                j=(row+(i*np.cos(theta)))/np.sin(theta)
                # if j==float('-inf'):
                #     j=0

                if j<im.height and j>=0:
                    linePoints.append((i,j))
            im1.line(linePoints,fill='red',width=1)
            im2.line(linePoints,fill='red',width=1)
            Vpoints.append(int(round(j)))
            # color_im.show()
        else:
            l=0
    # color_im.save('sample.png')
    # color_im.show()
    # im.save('sobelsample.png')
    Vpoints.sort()
    return Vpoints

# def getHoughparamsV(points, im,color_im):
#     k=heapq.nlargest(len(points),points.items(),key=lambda x:x[1])
#     setV=set()
#     Vpoints=[]
#     for index,line in enumerate(k):
#         (row,theta)=line[0]
#         if len(setV)>=58:
#             break;
#         neigh={row+i for i in range(-12,13)}
#         neigh.remove(row)
#         # l=0
#         if not neigh.intersection(setV):
#             setV.add(row)
#             j=(row)/np.sin(theta)
#             if j<im.height and j>=0:
#                 Vpoints.append(round(j))
#     Vpoints.sort()
#     return Vpoints


def getHoughparamsH(points, im,color_im):
    k=heapq.nlargest(len(points),points.items(),key=lambda x:x[1])
    # (row,theta)=k[1][0]
    setH=set()
    Hpoints=[]
    im1=ImageDraw.Draw(color_im)
    im2=ImageDraw.Draw(im)
    for index,line in enumerate(k):
        (row,theta)=line[0]
        linePoints=[]
        if len(setH)>=30:
            break;
        if not {row-5,row-4,row-3,row-2,row-1,row+1,row+2,row+3,row+4,row+5}.intersection(setH):
            setH.add(row)
            for j in range(670,im.height):
                i=((j*np.sin(theta))-row)/np.cos(theta)
                # if i==float('-inf'):
                #     j=0

                if 160<=i<=1470:
                    linePoints.append((i,j))
            im1.line(linePoints,fill='red',width=1)
            im2.line(linePoints,fill='red',width=1)
            Hpoints.append(round(i))
            # color_im.show()
        else:
            l=0
    # color_im.save('sample.png')
    # color_im.show()
    # im.save('sobelsample.png')
    Hpoints.sort()
    return Hpoints

# def getHoughparamsH(points, im,color_im):
#     k=heapq.nlargest(len(points),points.items(),key=lambda x:x[1])
#     setH=set()
#     Hpoints=[]
#     for index,line in enumerate(k):
#         (row,theta)=line[0]
#         if len(setH)>=30:
#             break;
#         if not {row-5,row-4,row-3,row-2,row-1,row+1,row+2,row+3,row+4,row+5}.intersection(setH):
#             setH.add(row)
#             i=(-row)/np.cos(theta)
#             if 160<=i<=1470:
#                 Hpoints.append(round(i))
#     Hpoints.sort()
#     return Hpoints


# def getLetters(Vpoints,Hpoints,canny_im):
#     text={}
#     canny_im.show()
#     box=Vpoints[1]-Vpoints[0]
#     for i in range(0,len(Hpoints),2):
#         for j in range(0,len(Vpoints),10):
#             if j==0:
#                 left=Vpoints[j]-(box*4)
#             else:
#                 left=Vpoints[j-1]+box
#             right=Vpoints[j]-2*box
#             up=Hpoints[i]
#             down=Hpoints[i+1]
#             edgepixels=0
#             for k in range(left,right+1):
#                 for l in range(up,down+1):
#                     if canny_im.getpixel((k,l))==255:
#                         edgepixels+=1
#             if edgepixels >50:
#                 number=((j//10)*29)+((i+2)//2)
#                 text[number]=True
#                 print(number," ",True)
#     return text



def getLetters(Vpoints,Hpoints,i,j,canny_im,box):
    if j==0:
        left=Vpoints[j]-(box*4)
    else:
        left=Vpoints[j-1]+box
    right=Vpoints[j]-2*box
    up=Hpoints[i]
    down=Hpoints[i+1]
    edgepixels=0
    for k in range(left,right+1):
        for l in range(up,down+1):
            if canny_im.getpixel((k,l))>0:
                edgepixels+=1
    if edgepixels >50:
        return True
        # number=((j//10)*29)+((i+2)//2)
        # text[number]=True
        # print(number," ",True)
    return False


# def getBlobCentroids(Vpoints,Hpoints,gray_im,canny_im):

#     left=Vpoints[0]
#     right=Vpoints[9]
#     up=Hpoints[0]
#     down=Hpoints[1]
#     points=[]
#     centroid_row= round((up+down)/2)
#     radius=down-up
#     centroids=[]
#     for k in range(0,9,2):
#         col=round((Hpoints[k]+Hpoints[k+1])/2)
#         centroids.append([col,centroid_row,gray_im.getpixel((col,centroid_row))])


#     for i in range(left,right):
#         for j in range(up,down):
#             if gray_im.getpixel((i,j)) <100:
#                 points.append([i,j,gray_im.getpixel((i,j))])
#     points=np.array(points)
#     ms=MeanShift(bandwidth=radius,cluster_all=False,min_bin_freq=600)
#     ms.fit(points)
#     cluster_centers = ms.cluster_centers_
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.scatter(points[:,0], points[:,1], points[:,2], marker='o')
#     ax.scatter(cluster_centers[:,0], cluster_centers[:,1], cluster_centers[:,2], marker='x', color='red', s=300, linewidth=5, zorder=10)
#     plt.show()
#     k=0

# def getAns(Vpoints,Hpoints,gray_im):
#     ans={}
#     for i in range(0,len(Hpoints),2):
#         for j in range(0,len(Vpoints),10):
#             number=((j//10)*29)+((i+2)//2)
#             ans[number]=list()
#             for k in range(j,j+10,2):
#                 left,right=Vpoints[k],Vpoints[k+1]
#                 top,down=Hpoints[i],Hpoints[i+1]
#                 count=0
#                 for m in range(left,right+1):
#                     for n in range(top,down+1):
#                         if gray_im.getpixel((m,n))<50:
#                             count+=1
#                 if count>400:
#                     ans[number].append((k-j)//2)
#     end=0


def getAns(Vpoints,Hpoints,gray_im,canny_im):
    ans={}
    options={0:'A',1:'B',2:'C',3:'D',4:'E'}
    box=Vpoints[1]-Vpoints[0]
    text={}
    for i in range(0,len(Hpoints),2):
        for j in range(0,len(Vpoints),10):
            number=((j//10)*29)+((i+2)//2)
            if getLetters(Vpoints,Hpoints,i,j,canny_im,box):
                text[number]='x'
            ans[number]=list()
            for k in range(j,j+10,2):
                left,right=Vpoints[k],Vpoints[k+1]
                top,down=Hpoints[i],Hpoints[i+1]
                count=0
                for m in range(left,right+1):
                    for n in range(top,down+1):
                        if gray_im.getpixel((m,n))<50:
                            count+=1
                if count>350:
                    ans[number].append(options[(k-j)//2])
    return ans,text



def printAns(ans,text,file):   
    # f=open('demo.txt','w+')
    f=open(file,'w+')
    for i in range(1,86):
        s=str(i)+" "+"".join(ans[i])
        if i in text:
            s=s+" "+text[i]
        f.write(s+"\n")
    f.close()
        


def getHouhpoints(im):
    gray_im_p = im.convert("L")
    # gray_im_p.show()
    gray_im = gray_im_p.filter(ImageFilter.GaussianBlur(radius = 0.3))
    # gray_im.show()
   
    # sobel edge detection
    xresult,yresult,sobel_im,directions=sobel(gray_im)
    # sobel_im.save('sobel_im.png')

    
    # canny_im=nonMaximalSuppression(sobel_im,directions)
    canny_xresult,canny_yresult=nonMaximalSuppression_axis(xresult,yresult)
    # canny_im=cannyThreshold(canny_im)
    canny_xresult,canny_yresult=cannyThreshold_axis(canny_xresult,canny_yresult)
    # canny_im.save('canny_im.png')

    # get Hough points
    # pointsV,pointsH=getHoughPoints(canny_im)
    pointsV,pointsH=getHoughPoints_axis(canny_xresult,canny_yresult)
    # get Hough lines
    # Hpoints=getHoughparamsV( pointsV,canny_im,im)
    Hpoints=getHoughparamsV( pointsV,canny_xresult,im)
    Vpoints=getHoughparamsH( pointsH,canny_yresult,im)
    return Hpoints,Vpoints

def getStudentAns(im,file):
    gray_im_p = im.convert("L")
    # gray_im_p.show()
    gray_im = gray_im_p.filter(ImageFilter.GaussianBlur(radius = 0.3))
    # gray_im.show()
   
    # sobel edge detection
    xresult,yresult,sobel_im,directions=sobel(gray_im)
    # sobel_im.save('sobel_im.png')

    
    # canny_im=nonMaximalSuppression(sobel_im,directions)
    canny_xresult,canny_yresult=nonMaximalSuppression_axis(xresult,yresult)
    # canny_im=cannyThreshold(canny_im)
    canny_xresult,canny_yresult=cannyThreshold_axis(canny_xresult,canny_yresult)
    # canny_im.save('canny_im.png')

    # get Hough points
    # pointsV,pointsH=getHoughPoints(canny_im)
    pointsV,pointsH=getHoughPoints_axis(canny_xresult,canny_yresult)
    # get Hough lines
    # Hpoints=getHoughparamsV( pointsV,canny_im,im)
    Hpoints=getHoughparamsV( pointsV,canny_xresult,im)
    Vpoints=getHoughparamsH( pointsH,canny_yresult,im)

    # side text ans
    # textAns=getLetters(Vpoints,Hpoints,sobel_im)
    ans,text=getAns(Vpoints,Hpoints,gray_im_p,sobel_im)
    printAns(ans,text,file)
    return ans,text

if __name__ == '__main__':
    # Load an image 
    # im = Image.open('./test-images/c-33.jpg')
    im = Image.open(sys.argv[1])
    output=sys.argv[2]
    # output="output.txt"
    ans,text=getStudentAns(im,output)
    
    
    
    
    
    
    
    
    
    
    # example=Image.open('c-33.jpg')
    
    # gray_im_p = im.convert("L")
    # # gray_im_p.show()
    # gray_im = gray_im_p.filter(ImageFilter.GaussianBlur(radius = 0.3))
    # # gray_im.show()
   
    # # sobel edge detection
    # xresult,yresult,sobel_im,directions=sobel(gray_im)
    # sobel_im.save('sobel_im.png')

    
    # # canny_im=nonMaximalSuppression(sobel_im,directions)
    # canny_xresult,canny_yresult=nonMaximalSuppression_axis(xresult,yresult)
    # # canny_im=cannyThreshold(canny_im)
    # canny_xresult,canny_yresult=cannyThreshold_axis(canny_xresult,canny_yresult)
    # # canny_im.save('canny_im.png')

    # # get Hough points
    # # pointsV,pointsH=getHoughPoints(canny_im)
    # pointsV,pointsH=getHoughPoints_axis(canny_xresult,canny_yresult)
    # # get Hough lines
    # # Hpoints=getHoughparamsV( pointsV,canny_im,im)
    # Hpoints=getHoughparamsV( pointsV,canny_xresult,im)
    # Vpoints=getHoughparamsH( pointsH,canny_yresult,im)

    # # side text ans
    # # textAns=getLetters(Vpoints,Hpoints,sobel_im)
    # ans,text=getAns(Vpoints,Hpoints,gray_im_p,sobel_im)
    # printAns(ans,text)


    # ans,text=getStudentAns(im)
    # k=0








    
