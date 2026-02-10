import cv2
import os

# 장치의 0번째 카메라를 불러옴
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened(): # 카메라가 정상적으로 열리지 않았을 경우
    print("카메라가 없어요")
    exit()

# 카메라 사진 찍기
while cap.isOpened():
    ret, img = cap.read()

    if ret:
        cv2.imshow('camera', img)

        # 10ms 동안 키 입력을 대기
        # 키가 입력되면 (-1이 아니면) 사진을 저장하고 종료
        if cv2.waitKey(10) != -1:
            save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "capture.jpg")
            print(save_path, cv2.imwrite(save_path, img))
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

# 실습 3 - 카메라 컨트롤

import cv2

capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(10) < 0:
    ret, frame = capture.read()
    if not ret:
        break

    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()
