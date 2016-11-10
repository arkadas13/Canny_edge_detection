import cv2
import os
def main():

    capWebcam = cv2.VideoCapture(0)

    if capWebcam.isOpened() == False:
        print ("error: capWebcam not accessed successfully\n\n")      
        os.system("pause")
        return

    while cv2.waitKey(1) != 27 and capWebcam.isOpened():
        blnFrameReadSuccessfully, imgOriginal = capWebcam.read()

        if not blnFrameReadSuccessfully or imgOriginal is None:
            print ("error: frame not read from webcam\n")
            os.system("pause")
            break

        imgGrayscale = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)

        imgBlurred = cv2.GaussianBlur(imgGrayscale, (5, 5), 0)

        imgCanny = cv2.Canny(imgBlurred, 100, 200)

        cv2.namedWindow("imgOriginal", cv2.WINDOW_NORMAL)
        cv2.namedWindow("imgCanny", cv2.WINDOW_NORMAL)

        cv2.imshow("imgOriginal", imgOriginal)
        cv2.imshow("imgCanny", imgCanny)
    # end while

    cv2.destroyAllWindows()

    return

if __name__ == "__main__":
    main()         # remove windows from memory