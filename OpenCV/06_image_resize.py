import cv2
import os

image = cv2.imread("OpenCV/images/cat.jpg")

# 1. 고정 크기로 조정 (가로 320, 세로 240)
dst_fixed = cv2.resize(image, (320, 240))

# 2. 비율로 조정 (가로 0.5배, 세로 0.5배)
dst_ratio = cv2.resize(image, None, fx=0.5, fy=0.5)

cv2.imshow("Fixed Resize", dst_fixed)
cv2.imshow("Ratio Resize", dst_ratio)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 실습 - 영상 리사이즈해서 출력

import cv2
import os

# 현재 파일 기준으로 경로 설정 (한글 경로 대응)
path = os.path.join(os.path.dirname(__file__), "images", "video.mp4")
cap = cv2.VideoCapture(path)

# 파일이 제대로 열렸는지 확인 (경로 틀리면 여기서 종료)
if not cap.isOpened():
    print("영상을 열 수 없어요. 경로를 확인하세요:", path)
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS:", fps)

# 일부 mp4 파일은 OpenCV가 FPS를 못 읽어서 0을 반환하는 경우가 있음
# 그대로 쓰면 1000 / 0 → ZeroDivisionError 발생하므로 기본값 30으로 대체
if fps == 0:
    fps = 30

# waitKey에 넣을 딜레이 계산 (1초 = 1000ms / fps = 한 프레임 재생 시간)
delay = int(1000 / fps)

while cap.isOpened():
    ret, frame = cap.read()  # ret: 읽기 성공 여부, frame: 현재 프레임 이미지

    # 더 이상 읽을 프레임이 없으면 종료
    if not ret:
        break

    # 1.5배 확대 리사이즈
    # fx, fy: 가로/세로 비율 (1.5 = 1.5배)
    # INTER_CUBIC: 확대 시 권장하는 보간법 (더 부드럽게 확대)
    resized = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    cv2.imshow("Original", frame)
    cv2.imshow("Resized x1.5", resized)

    # 'q' 키를 누르면 중간에 종료
    if cv2.waitKey(delay) == ord('q'):
        break

# 자원 해제 (반드시 호출해야 다음 실행 시 카메라/파일 정상 접근 가능)
cap.release()
cv2.destroyAllWindows()