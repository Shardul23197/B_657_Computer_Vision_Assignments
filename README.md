# a1

#### Extract students's answer from scanned sheet

We planned to draw horizontal and vertical lines using Hough transform, from these lines we are able to locate each question and its options and from this we can able get answers student chosen.

For drawing hough transform lines we followed bellow steps:
1. Smoothing the image using gaussian filter
2. Find derivative along x and y direction using Sobel operator.
3. Find magnitude and orientation of gradients
4. Perform non-maximal suppression on Sobel results.
5. Perform Canny threshold and linking the edges.
6. Perform Hough transform on resulting image.

#### Smooth the image using a Gaussian filter
As smoothing the images spreads the edges, to avoid the more spread we chose gaussian filter of sigma 0.3 which is less than Sobel operator sigma. So that Sobel detect prominent edges.

#### Find derivative along x and y direction using Sobel operator.
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


#### Find magnitude and orientation of gradients
Magnitude= sqrt(xvalue^2 +yvalue^2)
Gradient tan-1(yvalue/xvalye)

#### Perform non-maximal suppression on Sobel results.
To draw horizontal line we resultant image when image is convoluted by ykernel of Sobel operator, as horizontal lines are more prominent without interruption of vertical lines. Similarly, images produced by convoluting xkernel is used to detect vertical lines in Hough transform. 
Non-maximal suppression is done for 5 pixels before and after the gradient direction. This avoided multiple edge lines of same edge.

#### Perform Canny threshold and linking the edges.
For canny threshold we used 70 as high threshold and 40 as low threshold. More the 70 as intensity is considered as edges, lower than 40 pixel intensity are considered as not edges. Pixel which has intensity in between 70 and 40 are considered as edges if adjacent pixels are edges, if not they are not edge pixels.

#### Perform Hough transform on resulting image.
```
row=(-1*(x)*np.cos(theta))+(y*np.sin(theta))

```
Above equation is used to detect the Hough transform parameters row and theta. After calculating total votes to these parameters. Most voted parameters are chosen to draw horizontal and vertical lines.

#### x mark detection
After detecting all horizontal and vertical lines, we can locate each question and its options. We used these relative locations to find whether student written answers beside the question using edges pixels in that area. If the edge pixels are more than 50 in the area left to the question, it is considered that student has written some answer in that area.

#### detecting student bubbled answers.
We used relative positions to know which option student selected for that question. If option area contains more than 350 pixels whose intensity is less than 50, then it is considered as answer, we think this way is robust because it is valid to think that student didn’t chose an option if the student isn’t bubbled minimum area of the box. We used gray scale image of the scanned copy. This method is working good for all test images. We can use gray scale image which convoluted with gaussian filter to avoid noise, Since it is working fine with present setup we didn’t used convoluted image.


### Limitations
For detecting horizontal and vertical lines, we started detecting lines from pixels (160,670) , this is because the questions start from around these pixels. These values are chosen based on the testcases given along with this problem, espesially in b-13.jpg and a-48.jpg,  there are some extra lines, by keeping these in mind we chose to start from (160,670). If there is an extra line after this (160,670), the program will not extract the student's answer properly because relative positions changes with one extra horizontal line. This is a drawback.



