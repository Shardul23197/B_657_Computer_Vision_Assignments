from PIL import Image
from PIL import ImageFilter
import sys
from grade import *

def extract(injected_img,opt_text):

    #im = Image.open('injected.jpg')
    im=Image.open(injected_img)
    im = im.convert("RGB")

    #Taking Hough Transform of topmost and leftmost lines
    Hpoints,Vpoints = getHoughpoints(im)

   

    # checking if that value is less than the threshold set by us. If it is less than that threshold, 
    # then that option is part of the answers
    op = {}
    for i in range(1,86):
        op[i] = []
    for x1 in range(1,47):
        st = Vpoints[0] + x1*25
        en = st + 5
        # Code to check if A is the answer
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-300,Hpoints[0]-200):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        if p < 150000:
            op[x1].append('A')
        st = en
        en = st + 5
        
        # Code to check if B is the answer
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-300,Hpoints[0]-200):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        if p < 150000:
            op[x1].append('B')
        st = en
        en = st + 5
        # Code to check if C is the answer
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-300,Hpoints[0]-200):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        if p < 150000:
            op[x1].append('C')
        st = en
        en = st + 5
        # Code to check if D is the answer
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-300,Hpoints[0]-200):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        if p < 150000:
            op[x1].append('D')
        st = en
        en = st + 5
        # Code to check if E is the answer
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-300,Hpoints[0]-200):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        if p < 150000:
            op[x1].append('E')

    for x1 in range(47,86):
        st = Vpoints[0] + (x1-46)*25
        en = st + 5

        
        # Code to check if A is the answer
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-200,Hpoints[0]-100):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        if p < 150000:
            op[x1].append('A')
        st = en
        en = st + 5
        
        # Code to check if B is the answer
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-200,Hpoints[0]-100):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        if p < 150000:
            op[x1].append('B')
        st = en
        en = st + 5

        # Code to check if C is the answer
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-200,Hpoints[0]-100):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        # print("pc : ",p)
        if p < 150000:
            op[x1].append('C')
        st = en
        en = st + 5

        # Code to check if D is the answer
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-200,Hpoints[0]-100):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        if p < 150000:
            op[x1].append('D')
        st = en
        en = st + 5
        
        # Code to check if E is the answer
        p = 0
        for x2 in range(st,en):
            for x3 in range(Hpoints[0]-200,Hpoints[0]-100):
                px = im.getpixel((x2,x3))
                p = p + px[0] + px[1] + px[2]
        if p < 150000:
            op[x1].append('E')
        
    lines = []
    for i in op.keys():
        i1 = ''
        for j in op[i]:
            i1 = i1 + j
        abd = str(i) + ' ' + i1
        lines.append(abd)
    
    #Write extracted answer sheet into text file
    with open(opt_text,'w') as f:
        for k in lines:
            f.write(k)
            f.write('\n')
    f.close()

    

extract(sys.argv[1],sys.argv[2])