import cv2


def main():
    img1 = cv2.imread("Dog_Strong.jpg")
    img2 = cv2.imread("Dog_Weak.jpg")
    window_name = "Blending"
    alpha = 0.0
    beta = 0.0
    gamma = 0.0

    def alpha_trackbar(val):
        alpha = float(val / 255)
        beta = float(cv2.getTrackbarPos("beta", window_name) / 255)
        gamma = float(cv2.getTrackbarPos("gamma", window_name))
        blend_img = cv2.addWeighted(img2, alpha, img1, beta, gamma)
        cv2.imshow(window_name, blend_img)

    def beta_trackbar(val):
        beta = float(val / 255)
        alpha = float(cv2.getTrackbarPos("alpha", window_name) / 255)
        gamma = float(cv2.getTrackbarPos("gamma", window_name))
        blend_img = cv2.addWeighted(img2, alpha, img1, beta, gamma)
        cv2.imshow(window_name, blend_img)

    def gamma_trackbar(val):
        gamma = val
        alpha = float(cv2.getTrackbarPos("alpha", window_name) / 255)
        beta = float(cv2.getTrackbarPos("beta", window_name) / 255)
        blend_img = cv2.addWeighted(img2, alpha, img1, beta, gamma)
        cv2.imshow(window_name, blend_img)

    cv2.namedWindow(window_name)
    cv2.createTrackbar("alpha", window_name, 0, 255, alpha_trackbar)
    cv2.createTrackbar("beta", window_name, 0, 255, beta_trackbar)
    cv2.createTrackbar("gamma", window_name, 0, 255, gamma_trackbar)
    cv2.imshow(window_name, img1)
    while True:
        if cv2.waitKey(100) == 27:  # ESC
            cv2.destroyWindow(window_name)
            break


if __name__ == "__main__":
    main()
