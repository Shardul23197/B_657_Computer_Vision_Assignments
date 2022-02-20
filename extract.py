from PIL import Image
from PIL import ImageFilter
import sys
from grade import *

def extract(injected_img,opt_text):

    im = Image.open('injected.jpg')
    im = im.convert("RGB")
    Hpoints,Vpoints = getHoughpoints(im)

    #im.show()

    # print("Image is %s pixels wide." % im.width)
    # print("Image is %s pixels high." % im.height)
    # print("Image mode is %s." % im.mode)
    # print("Pixel value at (265,250) is %s" % str(im.getpixel((265,250))))


    op = {}
    for i in range(1,86):
        op[i] = []
    # print("op1 : ",op)
    for x1 in range(1,47):
        st = Vpoints[0] + x1*25
        en = st + 5
        # print("st : ",st)
        # print("en : ",en)
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-300,Hpoints[0]-200):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        # print("pa : ",p)
        if p < 200000:
            op[x1].append('A')
        st = en
        en = st + 5
        # print("st : ",st)
        # print("en : ",en)
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-300,Hpoints[0]-200):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        # print("pb : ",p)
        if p < 200000:
            op[x1].append('B')
        st = en
        en = st + 5
        # print("st : ",st)
        # print("en : ",en)
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-300,Hpoints[0]-200):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        # print("pc : ",p)
        if p < 200000:
            op[x1].append('C')
        st = en
        en = st + 5
        # print("st : ",st)
        # print("en : ",en)
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-300,Hpoints[0]-200):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        # print("pd : ",p)
        if p < 200000:
            op[x1].append('D')
        st = en
        en = st + 5
        # print("st : ",st)
        # print("en : ",en)
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-300,Hpoints[0]-200):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        # print("pe : ",p)
        if p < 200000:
            op[x1].append('E')

    for x1 in range(47,86):
        st = Vpoints[0] + (x1-46)*25
        en = st + 5
        # print("st : ",st)
        # print("en : ",en)
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-200,Hpoints[0]-100):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        # print("pa : ",p)
        if p < 200000:
            op[x1].append('A')
        st = en
        en = st + 5
        # print("st : ",st)
        # print("en : ",en)
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-200,Hpoints[0]-100):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        # print("pb : ",p)
        if p < 200000:
            op[x1].append('B')
        st = en
        en = st + 5
        # print("st : ",st)
        # print("en : ",en)
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-200,Hpoints[0]-100):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        # print("pc : ",p)
        if p < 200000:
            op[x1].append('C')
        st = en
        en = st + 5
        # print("st : ",st)
        # print("en : ",en)
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-200,Hpoints[0]-100):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        # print("pd : ",p)
        if p < 200000:
            op[x1].append('D')
        st = en
        en = st + 5
        # print("st : ",st)
        # print("en : ",en)
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-200,Hpoints[0]-100):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        # print("pe : ",p)
        if p < 200000:
            op[x1].append('E')
        
    #print("op : ",op)
    lines = []
    for i in op.keys():
        i1 = ''
        for j in op[i]:
            i1 = i1 + j
        abd = str(i) + ' ' + i1
        lines.append(abd)
    # print("lines : ",lines)
    with open(sys.argv[2],'w') as f:
        for k in lines:
            f.write(k)
            f.write('\n')
    f.close()

    

extract(sys.argv[1],sys.argv[2])