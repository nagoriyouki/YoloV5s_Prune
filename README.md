# YoloV5s_Prune
*웹캠을 통해 실시간으로 촬영되는 영상에서 볼라드, 횡단보도, 보행자 신호등 식별



모델 및 경량화 방법: YoloV5s / Prune
-

*Conv2d 레이어 프루닝: 약 40%의 가중치 제거


* BatchNorm2d 프루닝: 약 30%만큼의 가중치 제거


-> 최종적으로 전체 가중치의 약 58% 제거


경량화 결과
-
[Prune 후 Detect.py 실행결과]

- 레이어 수: 157개
- 매개변수 수: 7,225,885개
- 그래디언트 수: 0개
- 연산량: 16.4 GFLOPs


[Prune 후 Detect.py 실행결과]

- 레이어 수: 157개
- 매개변수 수: 1,189,625개
- 그래디언트 수: 0개
- 연산량: 3.2 GFLOPs

[Pruned_weight.pt]
- YOLOv5s summary: 214 layers, 1193553 parameters, 1193553 gradients, 3.3 GFLOPs


Prune 후 성능지표
-
-mAP50: 0.793
-
|:class:|:Images:|:Instances:|:P:|:R:|:mAP:|
|:---:|:---:|:---:|:---:|:---:|:---:|
|all|1608|2156|0.726|0.796|0.793|
|bollard|1608|731|0.82|0.722|0.803|
|crosswalk|1608|752|0.68|0.856|0.826|
|greenlight|1608|349|0.723|0.83|0.801|
-
## PR curve

![KakaoTalk_20230729_005518984](https://github.com/nagoriyouki/YoloV5s_Prune/assets/130470442/4e8a756d-8ea0-4b15-9084-d7f03682a524)

## P-curve
![KakaoTalk_20230729_005518984_01](https://github.com/nagoriyouki/YoloV5s_Prune/assets/130470442/5df60d7a-a121-4033-9c9e-ce81400d43ef)

## Result
![KakaoTalk_20230729_051727539](https://github.com/nagoriyouki/YoloV5s_Prune/assets/130470442/472caaa5-f706-4c17-9ebe-05f15caab0a7)


# 실행방법
[detect.py]
- pip install -r requirements.txt
- python detect.py --source 0 --weights /path/best.pt --data /path/seconddata.yaml

# Pre-trained 모델 로드 방법
loaded_model = Model('path/to/your/yolov5s.yaml')  # Create a new instance of your model structure.
loaded_model.load_state_dict(torch.load('prune_weights.pt'))  # Load saved weights into this instance.

데이터셋 다운로드: kaggle datasets download -d juhyehyeon/crosswalk-bollard-trafficlight
기존 모델 출처: https://github.com/ultralytics/yolov5
