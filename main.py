import cv2


def main():
    img1 = cv2.imread("Dog_Strong.jpg")
    img2 = cv2.imread("Dog_Weak.jpg")
    window_name = "Blending"

    def change_trackbar(val):
        alpha = float(val / 255)
        blend_img = cv2.addWeighted(img2, alpha, img1, 1.0 - alpha, 0.0)
        cv2.imshow(window_name, blend_img)
    
    cv2.namedWindow(window_name)
    cv2.createTrackbar("trackbar", window_name, 0, 255, change_trackbar)
    cv2.imshow(window_name, img1)
    while True:
        if cv2.waitKey(100) == 27:  # ESC
            cv2.destroyWindow(window_name)
            break


if __name__ == "__main__":
    main()
