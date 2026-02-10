import cv2
import numpy as np
import os
import sys

# 현재 파일 기준 경로 (한글 경로 대응용)
base_dir = os.path.dirname(__file__)

# ===============================
# cat 이미지
# ===============================
# cat_path = os.path.join(base_dir, "images", "cat.jpg")
#
# if not os.path.exists(cat_path):
#     print("cat 이미지 파일을 찾을 수 없습니다:", cat_path)
#     sys.exit()
#
# cat_color = cv2.imdecode(
#     np.fromfile(cat_path, np.uint8),
#     cv2.IMREAD_COLOR
# )

# ===============================
# logo 이미지 (채널 확인 예제)
# ===============================
logo_path = os.path.join(base_dir, "images", "logo.png")

if not os.path.exists(logo_path):
    print("logo 이미지 파일을 찾을 수 없습니다:", logo_path)
    sys.exit()

# 기본 컬러 이미지 (BGR)
logo_color = cv2.imdecode(
    np.fromfile(logo_path, np.uint8),
    cv2.IMREAD_COLOR
)

# 알파 채널 포함 이미지 (BGRA)
logo_unchanged = cv2.imdecode(
    np.fromfile(logo_path, np.uint8),
    cv2.IMREAD_UNCHANGED
)

if logo_color is None or logo_unchanged is None:
    print("logo 이미지 로드 실패")
    sys.exit()

# 이미지 출력
cv2.imshow("Logo Color", logo_color)
cv2.imshow("Logo Unchanged (Alpha)", logo_unchanged)

# 채널 수 확인
print("Logo Shape (Color):", logo_color.shape)
print("Logo Shape (Unchanged):", logo_unchanged.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ===============================
# 실습 1 - 원하는 이미지 띄우기
# ===============================
img_path = os.path.join(base_dir, "images", "dessert.jpg")

# 이미지 파일 존재 여부 확인
if not os.path.exists(img_path):
    print("이미지 파일을 찾을 수 없습니다:", img_path)
    sys.exit()

# 컬러 이미지
img_color = cv2.imdecode(
    np.fromfile(img_path, np.uint8),
    cv2.IMREAD_COLOR
)

# 흑백 이미지
img_gray = cv2.imdecode(
    np.fromfile(img_path, np.uint8),
    cv2.IMREAD_GRAYSCALE
)

if img_color is None or img_gray is None:
    print("이미지 로드 실패")
    sys.exit()

# 화면에 맞게 크기 조절 (너무 큰 이미지 대비)
img_color = cv2.resize(img_color, (800, 600))
img_gray = cv2.resize(img_gray, (800, 600))

# 이미지 출력
cv2.imshow("Dessert - Color", img_color)
cv2.imshow("Dessert - Grayscale", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
