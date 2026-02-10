import cv2
import os

# 비디오 경로 설정
path = os.path.join(os.path.dirname(__file__), "images", "video.mp4")
cap = cv2.VideoCapture(path)

# FPS 정보 가져오기
fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS:", fps)

# 프레임 재생 딜레이 (기본 속도)
delay = int(1000 / fps)

while cap.isOpened():  # 영상이 열려 있는 동안 반복
    ret, frame = cap.read()  # ret: 성공 여부, frame: 불러온 이미지

    if not ret:
        print("불러올 프레임이 없어요")
        break

    cv2.imshow("Video Player", frame)

    # waitKey(ms): ms마다 키 입력 확인 → 재생 속도 결정
    if cv2.waitKey(delay) == ord('q'):
        print("사용자 입력에 의해 종료되었어요")
        break

cap.release()
cv2.destroyAllWindows()

# 실습 2 - 속도 조절

# 영상의 FPS (초당 프레임 수) 정보 얻기
fps = cap.get(cv2.CAP_PROP_FPS)
total_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# 재생 속도 설정을 위한 변수 (기본값)
# 1000 // fps 기본
delay = int(1000 // fps)

while True:
    # 루프 재생
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == total_frame -1:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow("VideoFrame", frame)
    # 1. 일반 속도: cv2.waitKey(delay)
    # 2. 2배 빠른 속도: cv2.waitKey(delay // 2)
    # 3. 2배 느린 속도: cv2.waitKey(delay * 2)
    if cv2.waitKey(delay // 2) >= 0:
        break

cap.release()
cv2.destroyAllWindows
