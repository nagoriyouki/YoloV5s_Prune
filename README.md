# <div align="center"> YoloV5s_Prune </div>
<div align="center"> <strong>웹캠을 통해 실시간으로 촬영되는 영상에서 볼라드, 횡단보도, 보행자 신호등 식별</strong><br>

<div align="center">
    <div style="display: inline-block; text-align: center;">
        <div>⌨️Language⌨️</div>
        <br>
        <img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white" />
        <br><br>
        <div>⚙️Tools⚙️</div>
        <br>
        <img src="https://img.shields.io/badge/github-181717?style=flat&logo=python&logoColor=white" />
        <img src="https://img.shields.io/badge/pycharm-000000?style=flat&logo=python&logoColor=white" />
        <img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=flat&logo=python&logoColor=white" />
        <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=flat&logo=python&logoColor=white" />
        <img src="https://img.shields.io/badge/opencv-5C3EE8?style=flat&logo=python&logoColor=white" />
        <br><br>
        <div>📝Portfolio📝</div>
        <br>
        <img src="https://img.shields.io/badge/notion-000000?style=flat&logo=python&logoColor=white" />
    </div>
</div>

# 🧠모델 및 경량화 방법: YoloV5s / Prune🧠


Conv2d 레이어 프루닝: 약 40%의 가중치 제거

BatchNorm2d 프루닝: 약 30%만큼의 가중치 제거

# ✂️경량화 결과✂️

 <strong>[Prune 전 Detect.py 실행결과]</strong>

| 항목 | 값 |
| --- | --- |
| 레이어 수 | 157개 |
| 매개변수 수 | 7,225,885개 |
| 그래디언트 수 | 0개 |
| 연산량 | 16.4 GFLOPs |

 <strong>[Prune 후 Detect.py 실행결과]</strong>

| 항목 | 값 |
| --- | --- |
| 레이어 수 | 157개 |
| 매개변수 수 | 1,189,625개 |
| 그래디언트 수 | 0개 |
| 연산량 | 3.2 GFLOPs |


# 📋Pruned_weight.pt📋
YOLOv5s summary: 214 layers, 1193553 parameters, 0 gradients, 3.3 GFLOPs


# 📊(.pt) Prune 후 성능지표📊

mAP50: 0.793

|class|Images|Instances|P|R|mAP50|
|:---:|:---:|:---:|:---:|:---:|:---:|
|all|1608|2156|0.726|0.796|0.793|
|bollard|1608|731|0.82|0.722|0.803|
|crosswalk|1608|752|0.68|0.856|0.826|
|greenlight|1608|349|0.723|0.83|0.801|
|redlight|1608|324|0.681|0.778|0.745|

# PR curve

<p align="center">
  <img src="https://github.com/nagoriyouki/YoloV5s_Prune/assets/130470442/397839f0-58a4-47fd-9fef-26ac161f0d5c">
</p>

# P-curve
<p align="center">
  <img src="https://github.com/nagoriyouki/YoloV5s_Prune/assets/130470442/94b55951-26c9-4267-96da-d198724e4de8">
</p>

# Result
<p align="center">
  <img src="https://github.com/nagoriyouki/YoloV5s_Prune/assets/130470442/d80c08fe-e788-4824-869c-b76f4060e158">
</p>

# 실행방법
[detect.py]
▶️pip install -r requirements.txt
▶️python detect.py --source 0 --weights /path/best.pt --data /path/seconddata.yaml


# 📊(.onnx) Prune 후 성능지표📊

mAP50: 0.789

|class|Images|Instances|P|R|mAP50|
|:---:|:---:|:---:|:---:|:---:|:---:|
|all|1608|2156|0.735|0.789|0.789|
|bollard|1608|731|0.857|0.679|0.782|
|crosswalk|1608|752|0.693|0.864|0.83|
|greenlight|1608|349|0.704|0.84|0.8|
|redlight|1608|324|0.687|0.773|0.742|

# PR curve

<p align="center">
  <img src="https://github.com/nagoriyouki/YoloV5s_Prune/assets/130470442/a90d04b3-bbc9-4737-bdcd-6701e3112221">
</p>

# P-curve
<p align="center">
  <img src="https://github.com/nagoriyouki/YoloV5s_Prune/assets/130470442/38575484-f9d6-4715-8de2-16d136a6032b">
</p>

# R-curve
<p align="center">
  <img src="https://github.com/nagoriyouki/YoloV5s_Prune/assets/130470442/2f315e05-a687-44d4-9f6a-a974b0f1a409">
</p>

# 실행방법
<strong>[detect.py]</strong><br>
▶️ pip install -r requirements.txt<br>
▶️ python detect.py --source 0 --weights /path/best_cpu.onnx --data /path/seconddata.yaml

# 기타
⬇️<strong>데이터셋 다운로드</strong>: kaggle datasets download -d juhyehyeon/crosswalk-bollard-trafficlight<br>
💡<strong>기존 모델 출처</strong>: Jocher, G. (2020). YOLOv5 by Ultralytics (Version 7.0) [Computer software]. https://doi.org/10.5281/zenodo.3908559
</div>
