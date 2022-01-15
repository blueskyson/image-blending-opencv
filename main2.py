import cv2


def main():
    img1 = cv2.imread("Dog_Strong.jpg")
    img2 = cv2.imread("Dog_Weak.jpg")
    alpha = 0.0
    beta = 0.0
    gamma = 0.0

    def alpha_trackbar(val):
        alpha = float(val / 255)
        beta = float(cv2.getTrackbarPos("beta", "Blending") / 255)
        gamma = float(cv2.getTrackbarPos("gamma", "Blending"))
        blend_img = cv2.addWeighted(img2, alpha, img1, beta, gamma)
        cv2.imshow("Blending", blend_img)

    def beta_trackbar(val):
        beta = float(val / 255)
        alpha = float(cv2.getTrackbarPos("alpha", "Blending") / 255)
        gamma = float(cv2.getTrackbarPos("gamma", "Blending"))
        blend_img = cv2.addWeighted(img2, alpha, img1, beta, gamma)
        cv2.imshow("Blending", blend_img)

    def gamma_trackbar(val):
        gamma = val
        alpha = float(cv2.getTrackbarPos("alpha", "Blending") / 255)
        beta = float(cv2.getTrackbarPos("beta", "Blending") / 255)
        blend_img = cv2.addWeighted(img2, alpha, img1, beta, gamma)
        cv2.imshow("Blending", blend_img)

    cv2.namedWindow("Blending")
    cv2.createTrackbar("alpha", "Blending", 0, 255, alpha_trackbar)
    cv2.createTrackbar("beta", "Blending", 0, 255, beta_trackbar)
    cv2.createTrackbar("gamma", "Blending", 0, 255, gamma_trackbar)
    cv2.imshow("Blending", img1)
    while True:
        if cv2.waitKey(100) == 27:  # ESC
            cv2.destroyWindow("Image")
            break


if __name__ == "__main__":
    main()