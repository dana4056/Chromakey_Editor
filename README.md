# Chromakey_Editor
A program that cuts object from chromakey image and cuts it into desired background image.
<br>크로마키 영상에서 객체만 오려내 희망하는 배경 영상에 오려넣는 크로마키 에디터입니다. 
<br><br><br>

### 파일구조
```bash
├── Data                        
│   ├── test_dataset.zip
│   └── train_dataset.zip
├── cnn.py                      # 모델 생성 및 학습
├── cnn_text_recognition.py     # 모델 불러와 영상에서 글자 인식 (main)
├── collect_image.py            # dataset 직접 수집
├── resize_image.py             # dataset 한번에 리사이즈
└── text_CNN.h5                 # weight 파일
``` 



![슬라이드1](https://user-images.githubusercontent.com/54545026/146504405-7e4d93cc-9769-4a45-81c1-549d91b4f908.PNG)
![슬라이드2](https://user-images.githubusercontent.com/54545026/146504415-a72a9c78-48b0-49fb-86fe-cdcc74e25355.PNG)
![슬라이드3](https://user-images.githubusercontent.com/54545026/146504417-70303e85-2baf-4741-83aa-f64bd9229368.PNG)
![슬라이드4](https://user-images.githubusercontent.com/54545026/146504419-4b068805-d571-4c93-b0e2-acbf3d39ba90.PNG)
![슬라이드5](https://user-images.githubusercontent.com/54545026/146504423-cb0cb25d-eae0-44df-a47c-9101da52eb9d.PNG)
![슬라이드6](https://user-images.githubusercontent.com/54545026/146504424-e5d2c7d5-9bed-4fb5-a74e-b815f347d6fd.PNG)
![슬라이드7](https://user-images.githubusercontent.com/54545026/146504425-bb04c8d2-c6fc-4ed4-af11-77274ed331cd.PNG)
![슬라이드8](https://user-images.githubusercontent.com/54545026/146504427-ad591f79-7dfa-456d-b70f-7acd90ef58d3.PNG)
![슬라이드9](https://user-images.githubusercontent.com/54545026/146504430-902d7bf7-764e-4e7c-a99e-ad407ad55a6c.PNG)
![슬라이드10](https://user-images.githubusercontent.com/54545026/146504431-ad15c579-9918-4b3b-bc11-4290dc4d22fb.PNG)
![슬라이드11](https://user-images.githubusercontent.com/54545026/146504433-7340f5b1-36b8-46d9-8814-20441f2d7b66.PNG)
![슬라이드12](https://user-images.githubusercontent.com/54545026/146504435-5c65e8f9-e68d-4b32-a496-43ea0ad786d6.PNG)
