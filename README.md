## Extract students's answer from scanned sheet

We planned to draw horizontal and vertical lines using Hough transform, from these lines we are able to locate each question and its options and from this we can able get answers student chosen.

For drawing hough transform lines we followed bellow steps:
1. Smoothing the image using gaussian filter
2. Find derivative along x and y direction using Sobel operator.
3. Find magnitude and orientation of gradients
4. Perform non-maximal suppression on Sobel results.
5. Perform Canny threshold and linking the edges.
6. Perform Hough transform on resulting image.

### Smooth the image using a Gaussian filter
As smoothing the images spreads the edges, to avoid the more spread we chose gaussian filter of sigma 0.3 which is less than Sobel operator sigma. So that Sobel detect prominent edges.

### Find derivative along x and y direction using Sobel operator.
We used Sobel operator which is discussed in the class to find derivatives along x and y axis. 

```
xkernel = np.array((
                                (1, 0, -1),
                                (2, 0, -2),
                                (1,0, -1))) /8.
ykernel = np.array((
                                (-1, -2, -1),
                                (0, 0, 0),
                                (1, 2, 1))) /8.
```


### Find magnitude and orientation of gradients
Magnitude= sqrt(xvalue^2 +yvalue^2)
Gradient tan-1(yvalue/xvalye)

### Perform non-maximal suppression on Sobel results.
To draw horizontal line we resultant image when image is convoluted by ykernel of Sobel operator, as horizontal lines are more prominent without interruption of vertical lines. Similarly, images produced by convoluting xkernel is used to detect vertical lines in Hough transform. 
Non-maximal suppression is done for 5 pixels before and after the gradient direction. This avoided multiple edge lines of same edge.

### Perform Canny threshold and linking the edges.
For canny threshold we used 70 as high threshold and 40 as low threshold. More the 70 as intensity is considered as edges, lower than 40 pixel intensity are considered as not edges. Pixel which has intensity in between 70 and 40 are considered as edges if adjacent pixels are edges, if not they are not edge pixels.

### Perform Hough transform on resulting image.

```
row=(-1*(x)*np.cos(theta))+(y*np.sin(theta))

```
Above equation is used to detect the Hough transform parameters row and theta. After calculating total votes to these parameters. Most voted parameters are chosen to draw horizontal and vertical lines.

### x mark detection
After detecting all horizontal and vertical lines, we can locate each question and its options. We used these relative locations to find whether student written answers beside the question using edges pixels in that area. If the edge pixels are more than 50 in the area left to the question, it is considered that student has written some answer in that area.

### detecting student bubbled answers.
We used relative positions to know which option student selected for that question. If option area contains more than 350 pixels whose intensity is less than 50, then it is considered as answer, we think this way is robust because it is valid to think that student didn’t chose an option if the student isn’t bubbled minimum area of the box. We used gray scale image of the scanned copy. This method is working good for all test images. We can use gray scale image which convoluted with gaussian filter to avoid noise, Since it is working fine with present setup we didn’t used convoluted image.


### Limitations
For detecting horizontal and vertical lines, we started detecting lines from pixels (160,670) , this is because the questions start from around these pixels. These values are chosen based on the testcases given along with this problem, espesially in b-13.jpg and a-48.jpg,  there are some extra lines, by keeping these in mind we chose to start from (160,670). If there is an extra line after this (160,670), the program will not extract the student's answer properly because relative positions changes with one extra horizontal line. This is a drawback.


## Injection

For injection, we are making something like a barcode but not exactly a barcode. We are taking all the answers. There are 85 questions with 5 options which can be multi selected. So, for each option of each question we are allocating 5*100 pixels worth of space in the blank space above the answering area. We are making them in two lines. The first line contains the answers of first 46 questions and the second one contains the remaining. If any option is correct, then we are turning the pixels allocated to that option of the answer to (0,0,0). For starting the barcode, we are taking the left most line detected in hough transform to find the answer boxes. So, the barcode starts from where the boxes start on left side. For height, we are taking the topmost line in hough transform to find the horizontal line. If the topmost line is at 'x' pixel, then we are ploting our first line of barcode from x-250 to x-151 (100 pixels) and for the second line, we are plotting the barcode from x-150 to x-51 (100 pixels) pixels.

To inject: 

```
python3 inject.py ./test-images/a-27.jpg ./test-images/a-27_groundtruth.txt injected.jpg
```


### Limitations Of Injection

The main scenario for injection failure is linked to hough transform. Because the placement of the barcode is related to the lines detected by hough transform, the injection might fail if the hough transform fails. There needs to be atleast 250 pixels worth of space above the topmost line else it might fail. The other scenario where it might fail is if the dimensions of the answer sheet changes. We made this with 1700*2200 pixel dimensions will be used as an assumption. With little change in dimensions, it might not affect anything. But if the dimension cange is substantial, then it might fail.


## Extraction

For extraction, we are taking the hough transform the topmost and left most lines and tract the 5*100 worth pixel grid related to each option. Then we are adding the pixel values of all the pixels in that grid. Then we are checking if that value is less than the threshold set by us. If it is less that that threshold, then that option is part of the answers. We check all the options like that. For allowing noise, we are setting threshold in a way that even if there is a substantial maount of noise, it won't affect our extraction of correct answers. We can moce 1-2 pixels left or right without affecting our answers much. We can move 5-10 pixels up or down without much problem in extracting correct answers. But this might not happen because we are actually taking the leftmost and uppermost hough transform lines for injecting and extracting barcode. But this will give us nice wiggle room even if some noise is created due to external conditions.

To extract: 

```
python3 extract.py injected.jpg op.txt
```

### Limitations Of Extraction

The extraction might fail if there is a lot of noise introduced into the photo but a little noise won't be a problem. The other scenario when extraction might fail is when hough transform fails. Just like with injection, we are using the leftmost and topmost lines of hough transform. So, if it fails, then extraction might also fail. Another scenario when extraction can fail is when there is some orientation change while scanning the answer sheets. If the answer copies are scanned in diagonal fashion, it will fail.



## Contributions of the Authors

