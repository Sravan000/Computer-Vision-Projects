{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#importing libraries\n",
    "import cv2\n",
    "images_rgb = cv2.imread(\"kanaki.jpg\")  #image path\n",
    "numBilateralFilters = 30  \n",
    "\n",
    "for _ in range(numBilateralFilters): \n",
    "    images_rgb = cv2.bilateralFilter(images_rgb, 9, 9, 7) \n",
    "\n",
    "images_gray = cv2.cvtColor(images_rgb, cv2.COLOR_RGB2GRAY) #converting rgb to gray scale\n",
    " \n",
    "images_blur = cv2.medianBlur(images_gray, 3) \n",
    " \n",
    "images_edge = cv2.adaptiveThreshold(images_blur, 255, \n",
    "                                         cv2.ADAPTIVE_THRESH_MEAN_C, \n",
    "                                         cv2.THRESH_BINARY, 9, 2)  #measuring threshold\n",
    "\n",
    "images_edge = cv2.cvtColor(images_edge, cv2.COLOR_GRAY2RGB) #converting brg to gray scale of edge detected images\n",
    "cv2.imshow(\"images_rgb\", images_rgb) \n",
    "cv2.imshow(\"images_edge\", images_edge) \n",
    "\n",
    "res=cv2.bitwise_and(images_rgb, images_edge) #applying bitwise comparator between colored image and sketch\n",
    "  \n",
    "cv2.imshow(\"Cartoon version\", res) \n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()  #clearing ram memory\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
