# import cv2

# image = cv2.imread("OpenCV/images/cat.jpg")

# # 이미지 자르기
# img_crop = image[100:200, 100:400]

# cv2.imshow("Original", image)
# cv2.imshow("Crop", img_crop)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 실습 - 이미지 조정

import cv2
import os

# 이미지 읽기
path = os.path.join("OpenCV", "images", "huchu.jpg")
img = cv2.imread(path)

# ✅ None 체크 (핵심)
if img is None:
    print('파일을 찾을 수 없습니다.')
    exit()

# 원본 크기
h, w = img.shape[:2]

# 1. 1/2 축소
small_img = cv2.resize(img, (w//2, h//2))

# 2. 좌우 반전
flipped_img = cv2.flip(small_img, 1)

# 3. 우하단 배치
result = img.copy()
sh, sw, _ = flipped_img.shape

# 시작점으로부터 이미지 높이만큼만 영역 지정
result[h//2 : h //2 + sh, w//2 : w//2 + sw] = flipped_img

# 결과 출력
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
