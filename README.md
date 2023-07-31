# YoloV5s_Prune
*웹캠을 통해 실시간으로 촬영되는 영상에서 볼라드를 식별



모델 및 경량화 방법: YoloV5s / Prune
-

*Conv2d 레이어 프루닝: 약 40%의 가중치 제거


* BatchNorm2d 프루닝: 약 30%만큼의 가중치 제거


-> 최종적으로 전체 가중치의 약 58% 제거


경량화 결과
-
[Prune 전]

- 레이어 수: 157개
- 매개변수 수: 7,225,885개
- 그래디언트 수: 0개
- 연산량: 16.4 GFLOPs


[Prune 후]

- 레이어 수: 157개
- 매개변수 수: 1,189,625개
- 그래디언트 수: 0개
- 연산량: 3.2 GFLOPs


Prune 후 성능지표
-
-mAP50: 0.793


## PR curve


![PR_curve](https://github.com/nagoriyouki/yolov5_prune_bollard/assets/130470442/e3396c86-dc22-48d9-9cee-351830e24146)



## confusion_matrix

![confusion_matrix](https://github.com/nagoriyouki/yolov5_prune_bollard/assets/130470442/714ec37a-93e0-450c-9e8c-99844b578c54)


# 실행방법
- python detect.py source --0 --data (data.yaml의 경로) --cfg (yolov5s.yaml의 경로) --weights (yolov5s.pt의 경로) --batch-size 16 --epochs 50


기존 모델 출처: https://github.com/ultralytics/yolov5
