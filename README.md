# PJ_01 hahaha
메이플 캐릭터에 실존하는 옷입히기를 시작한다 ~ 7개월ing<br><br>

### Info
◾  MODEL : CP-VTON<br>
◾  <br>
◾  <br>

<br>
<br>

## Step 1 : Pretrain
이미 학습된 체크포인트를 활용하여 결과 예측<br>
<br>
<b>Result</b>
<div style="width:80%; margin:0 auto;">
<img src = "https://user-images.githubusercontent.com/64413742/183881567-d642b629-69cc-4673-a5d8-300f2fc1f351.png" width="15%">
<img src = "https://user-images.githubusercontent.com/64413742/183881615-da1ed498-df01-4ead-92fb-cffde8d009e2.png" width="15%">
<img src = "https://user-images.githubusercontent.com/64413742/183881633-88b9d994-da96-4baf-9bdd-9868fcf1b314.png" width="45%">
</div>


- <b>상체가 중앙에 있는 사람</b> (캐릭터) 이미지에게 잘 입힘
- 캐릭터 여러 자세나 크기에 대해 학습되어 있지 않음
- 메이흘 캐릭터에 맞게 모델 학습 필요
  - parse
  - cp-vton

<br>
<br>

## Step 2 : Train
메이플 캐릭터에 맞게 모델 학습
<br>
<br>
<b>Data preparation</b>
|이름|설명|수급.. 방법|
|---|---|---|
|cloth|옷 이미지|내용|
|person|캐릭터 이미지|내용|
|cloth person|캐릭터가 옷 입은 이미지|내용|
|parse|캐릭터의 영역 색칠 이미지|내용|
|keypoint|캐릭터 키포인트|내용|
