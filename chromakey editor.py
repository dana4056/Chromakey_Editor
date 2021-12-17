import cv2
import cv2 as cv
import numpy as np, random

# ========================================================================================================
# 단계1: 폴더와 파일 이름 지정 및 열기
# ========================================================================================================
Path = 'data/'
C_Name = 'person.jpg'
B_Name = 'background.jpg'
crop_Name = 'crop.jpg'
ch_key = Path + C_Name
back_gr = Path + B_Name
crop_img = crop_Name

image = cv.imread(ch_key, -1)                   #객체 원본 이미지(BGR)_화소값 추출에 이용
#image = cv.resize(image, (300, 200))
copy_image = np.copy(image)                     #객체 사본 이미지(BGR)_창으로 보여지는데 이용
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)    #객체 원본 이미지(HSV)
hsv = cv.GaussianBlur(hsv, (5,5), 5)

back_img = cv.imread(back_gr, -1)               #배경 이미지

img_h = hsv[:, :, 0]
img_s = hsv[:, :, 1]
img_v = hsv[:, :, 2]

#객체 원본 이미지 사이즈
img_width = len(image[0])
img_height = len(image)
print(img_height, img_width)

assert image is not None, 'No image file....!'  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.

# ========================================================================================================
# 단계2: call back 함수 정의
# ========================================================================================================

def mouse_callback(event, x, y, flags, param):  #A창에 적용되는 마우스 콜백함수
    global image, copy_image, c_x,c_y,s_x, s_y, e_x, e_y, mouse_pressed, drawing_needed

    if event == cv2.EVENT_LBUTTONDOWN : # 왼쪽 버튼 누르는 순간
        mouse_pressed = True
        s_x, s_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 이동중
        if mouse_pressed:
            copy_image = np.copy(image)
            cv2.rectangle(copy_image, (s_x, s_y),(x, y), (0, 255, 0), 1)

    elif event == cv2.EVENT_LBUTTONUP and mouse_pressed ==True: # 왼쪽 떼는 누르는 순간
        mouse_pressed = False
        e_x, e_y = x, y
        drawing_needed = True
        if e_x == s_x and e_y == s_y:  #같은 좌표에서 마우스를 누르고 뗴면 해당 화소 정보 출력
            mouse_pressed = False
            print('===========================================')  #평가항목 1
            print('좌표: (', x, ', ', y, ')')
            print('B : ', param[y][x][0], '\tG : ', param[y][x][2], '\tR : ', param[y][x][1])
            print('H : ', img_h[y][x], '\tS : ', img_s[y][x], '\tV : ', img_v[y][x])
            print('===========================================')
            c_x, c_y = x, y  # 선택 시작 좌표 기록

        # 시작점과 끝점이 바뀌었으면 두 좌표를 바꾼다.
        if s_y > e_y:
            s_y, e_y = e_y, s_y
        if s_x > e_x:
            s_x, e_x = e_x, s_x
        if e_y - s_y > 1 and e_x - s_x > 0:  #평가항목 3: 이미지 crop하고 저장
            img_crop = copy_image[s_y:e_y, s_x:e_x]
            cv2.imshow('crop', img_crop)
            cv2.imwrite('crop.jpg', img_crop)
            drawing_needed = False


def onMouse(event, x, y, flags, param):  #B창에 적용되는 마우스 콜백함수
    global image, c_x, c_y, s_x, s_y, e_x, e_y, mouse_pressed, drawing_needed, back_img, result
    back_img = cv.imread(back_gr, -1)
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        s_x, s_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 이동중
        if mouse_pressed:
            copy_image = np.copy(image)
            cv2.rectangle(copy_image, (s_x, s_y),(x, y), (0, 255, 0), 1)

    elif event == cv2.EVENT_LBUTTONUP and mouse_pressed == True:
        mouse_pressed = False
        e_x, e_y = x, y             # 선택 종료 좌표 기록
        drawing_needed = True

        # 시작점과 끝점이 바뀌었으면 두 좌표를 바꾼다.
        if s_y > e_y:
            s_y, e_y = e_y, s_y
        if s_x > e_x:
            s_x, e_x = e_x, s_x

        if e_y - s_y > 1 and e_x - s_x > 0:
            w = e_x - s_x  #너비
            h = e_y - s_y  #높이
            crop_image = cv.imread(crop_img, -1)
            crop_image = cv.resize(crop_image, dsize=(w, h))  #드래그한 크기에 맞춰 리사이즈
            for i in range(h):
                for j in range(w):
                    #평가항목 4: 크롭한 이미지 중 검정색이 아닌 화소(객체에 해당)를 배경 이미지에 할당
                    if crop_image[i][j][0] > 0 and crop_image[i][j][1] > 0 and crop_image[i][j][2] > 0:
                        back_img[s_y+i][s_x+j] = crop_image[i][j]
            cv2.imshow('background', back_img)
            result = back_img
            drawing_needed = False

def nothing(x, *userdata):    # 이것이 원래 올바른 형식
    pass

# ========================================================================================================
# 단계3: 메인 루틴
# ========================================================================================================

mouse_pressed = False
drawing_needed = False
modified = False

s_x = s_y = e_x = e_y = c_x = c_y = -1
result = np.copy(copy_image)

cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback, image)  #원본이미지에 마우스 콜백 함수 적용

cv.createTrackbar('H_margin', 'image', 0, 10, nothing) #원본이미지에 트랙바 생성
cv.createTrackbar('S_margin', 'image', 0, 10, nothing)
cv.createTrackbar('V_margin', 'image', 0, 10, nothing)

while True:
    cv2.imshow('image', copy_image)

    t = cv.waitKey(1)
    if t == 27:  # break if any key in input.
        break
    if t == ord('b'):  #B창 열기
        cv2.imshow('background', back_img)
        cv2.setMouseCallback('background', onMouse, back_img)
    if t == ord('c'):  #B창 초기화
        cv2.imshow('background', back_img)
    if t == ord('s'):  #최종 결과물 저장
        cv2.imwrite('image.jpg', result)

    #H,S,V 마진값
    h_m = cv.getTrackbarPos('H_margin', 'image')
    s_m = cv.getTrackbarPos('S_margin', 'image')
    v_m = cv.getTrackbarPos('V_margin', 'image')

    #범위 계산
    minH = img_h[c_y][c_x] - (img_h[c_y][c_x] * h_m * 0.15)
    maxH = img_h[c_y][c_x] + (img_h[c_y][c_x] * h_m * 0.15)
    minS = img_s[c_y][c_x] - (img_s[c_y][c_x] * s_m * 0.15)
    maxS = img_s[c_y][c_x] + (img_s[c_y][c_x] * s_m * 0.15)
    minV = img_v[c_y][c_x] - (img_v[c_y][c_x] * v_m * 0.15)
    maxV = img_v[c_y][c_x] + (img_v[c_y][c_x] * v_m * 0.15)

    #평가항목2: 계산된 범위 안에 있는 값 검정색으로
    copy_image = np.copy(image)
    copy_image[((img_h >= minH) & (img_h < maxH)) & ((img_s >= minS) & (img_s < maxS)) & ((img_v >= minV) & (img_v < maxV))] = 0
    #copy_image[((img_s >= minS) & (img_s < maxS))] = 0
    #copy_image[((img_v >= minV) & (img_v < maxV))] = 0

cv2.destroyAllWindows()
