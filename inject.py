from PIL import Image
from PIL import ImageFilter
import sys
from grade import *

def inject(blanktext_name,answerstext_name,injectedimg_name):



    ip = open(answerstext_name)
    #print("ip : ",ip)
    c = ip.read()
    #print("c : ",c)
    arr = c.splitlines()

    dict1 = {}
    for i in arr:
        arr2 = i.split()
        arr3 = [j for j in arr2[1]]
        #print("arr3 : ",arr3)
        dict1[int(arr2[0])] = arr3
    #print("dict1 : ",dict1)

    im = Image.open(blanktext_name)

    im = im.convert("RGB")

    Hpoints,Vpoints = getHoughpoints(im)
    # print("Hpoints : ",Hpoints)
    # print("Vpoints : ",Vpoints)
    

    # print("Image is %s pixels wide." % im.width)
    # print("Image is %s pixels high." % im.height)
    # print("Image mode is %s." % im.mode)

    '''for x in range(250,1400):
        abc = [350,450,550]
        for t in abc:
            if t < im.height:
                for y in range(t-2,t):
                    im.putpixel((x,y), (0,0,0))'''
    #print("dict_keys : ",dict1.keys())
    for x1 in dict1.keys():
        #print("x1 : ",x1)
        if x1 <= 46:
            st = Vpoints[0] + x1*25
            arrx = dict1[x1]
            en = st + 5
            #print("arrx : ",arrx)
            #print("st : ",st)
            # print("en : ",en)
            if 'A' in arrx:
                # print("In A")
                for x2 in range(st,en):
                    for x3 in range(Hpoints[0]-300,Hpoints[0]-200):
                        im.putpixel((x2,x3), (0,0,0))
            st = en
            en = en + 5
            # print("st : ",st)
            # print("en : ",en)
            if 'B' in arrx:
                # print("In B")
                for x2 in range(st,en):
                    for x3 in range(Hpoints[0]-300,Hpoints[0]-200):
                        im.putpixel((x2,x3), (0,0,0))
            st = en
            en = en + 5
            # print("st : ",st)
            # print("en : ",en)
            if 'C' in arrx:
                # print("In C")
                for x2 in range(st,en):
                    for x3 in range(Hpoints[0]-300,Hpoints[0]-200):
                        im.putpixel((x2,x3), (0,0,0))
            st = en
            en = en + 5
            # print("st : ",st)
            # print("en : ",en)
            if 'D' in arrx:
                # print("In D")
                for x2 in range(st,en):
                    for x3 in range(Hpoints[0]-300,Hpoints[0]-200):
                        im.putpixel((x2,x3), (0,0,0))
            st = en
            en = en + 5
            # print("st : ",st)
            # print("en : ",en)
            if 'E' in arrx:
                # print("In E")
                for x2 in range(st,en):
                    for x3 in range(Hpoints[0]-300,Hpoints[0]-200):
                        im.putpixel((x2,x3), (0,0,0))

    for x1 in dict1.keys():
        # print("x1 : ",x1)
        if x1 > 46:
            st = Vpoints[0] + (x1-46)*25
            arrx = dict1[x1]
            en = st + 5
            # print("arrx : ",arrx)
            # print("st : ",st)
            # print("en : ",en)
            if 'A' in arrx:
                # print("In A")
                for x2 in range(st,en):
                    for x3 in range(Hpoints[0]-200,Hpoints[0]-100):
                        im.putpixel((x2,x3), (0,0,0))
            st = en
            en = en + 5
            # print("st : ",st)
            # print("en : ",en)
            if 'B' in arrx:
                # print("In B")
                for x2 in range(st,en):
                    for x3 in range(Hpoints[0]-200,Hpoints[0]-100):
                        im.putpixel((x2,x3), (0,0,0))
            st = en
            en = en + 5
            # print("st : ",st)
            # print("en : ",en)
            if 'C' in arrx:
                # print("In C")
                for x2 in range(st,en):
                    for x3 in range(Hpoints[0]-200,Hpoints[0]-100):
                        im.putpixel((x2,x3), (0,0,0))
            st = en
            en = en + 5
            # print("st : ",st)
            # print("en : ",en)
            if 'D' in arrx:
                # print("In D")
                for x2 in range(st,en):
                    for x3 in range(Hpoints[0]-200,Hpoints[0]-100):
                        im.putpixel((x2,x3), (0,0,0))
            st = en
            en = en + 5
            # print("st : ",st)
            # print("en : ",en)
            if 'E' in arrx:
                # print("In E")
                for x2 in range(st,en):
                    for x3 in range(Hpoints[0]-200,Hpoints[0]-100):
                        im.putpixel((x2,x3), (0,0,0))


            



    #gray_im = im.convert("L")
    im.save(injectedimg_name)
    #im.show()
    # print("Pixel value at (265,350) is %s" % str(im.getpixel((265,350))))

inject(sys.argv[1],sys.argv[2],sys.argv[3])