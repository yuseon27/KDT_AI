# 6주차 과제 : ML 기초 실습 과제
## 음식 배달 시간 예측하기

<br>
<br>

## 0. 데이터
[Predciting Food Delivery Time](https://www.kaggle.com/ramprasad273/predicting-food-delivery-time)

<br>
<br>

## 1. 데이터 분석 및 전처리
### 1) 필드(Column) 설명
- Restaurant: A unique ID that represents a restaurant.          (식당의 고유 ID)
- Location: The location of the restaurant.                      (식당의 위치)
- Cuisines: The cuisines offered by the restaurant.              (식당에서 제공하는 요리의 종류)
- AverageCost: The average cost for one person/order.            (한 사람/주문 당 평균 주문 가격)
- MinimumOrder: The minimum order amount.                        (최소 배달 금액)
- Rating: Customer rating for the restaurant.                    (식당에 대한 손님들의 별점)
- Votes: The total number of customer votes for the restaurant.  (투표에 참여한 손님의 수)
- Reviews: The number of customer reviews for the restaurant.    (식당에 대해 손님들이 작성한 리뷰의 수)
- DeliveryTime: The order delivery time of the restaurant.       (타겟, 배달 시간)   (Target Classes)

<br>
<br>

### 2) 필드(Column)별 속성 분석
### (1) 범주형 필드
- Restaurant  : OrdinalEncoding 후, MinMaxScaler를 적용
- Location    : 다중값을 갖음, ','를 기준으로 값을 분리하여 하나의 값이 새로운 Column으로 생성(OneHotEncoding과 유사, 해당하는 값이 있을 경우 1, 없을 경우 0), 
- Cuisines    : 다중값을 갖음. ','를 기준으로 값을 분리하여 하나의 값이 새로운 Column으로 생성
- AverageCost : 대부분 정수, 'for'이라는 값을 갖고 있는 열이 있어 해당 값을 중간값으로 설정, 나머지를 정수로 변환. 이상값에 영향을 덜 받는 RobustScaler 적용
- Rating      : 대부분 실수, ['NEW', 'Opening Soon', 'Temporarily Closed']를 가지고 있는 열에 대해 0으로 설정, 나머지는 실수로 변환


### (2) 숫자형 필드
- MinimumOrder : 정수(Int)  , StandardScaler 적용
- Votes        : 실수(Float), StandardScaler 적용
- Reviews      : 실수(Float), StandardScaler 적용
- DeliveryTime : 정수(Int)


### (3) 결측치 존재 필드
- AverageCost            : 중간값으로 설정 
- Rating, Votes, Reviews : 손님들의 평가가 존재하지 않으므로 0으로 설정

<br>
<br>

## 2. 모델 및 손실함수
- 모델 : RandomForestRegressor 사용
- 최적의 모델 선택 : RamdomizedSearchCV를 사용
    - random_seed=42, n_estimators는 [1,200]사이의 값으로 설정
    - n_estimator가 100 언저리의 값에서 최적
- 손실함수 : 배달 시간의 차를 줄이는 것이 중요하다고 생각되어 Negative MAE(Mean Absolute Error)를 사용했다.

<br>
<br>

## 3. 테스트 데이터 평가
- Mean Absolute Error (MAE) : 9.698449849055324  
$ MAE = {1 \over n}{\sum_{i=1}^{n}|f(x_i) - y_i|} $
- Under-prediction의 비율 : 0.21090581342947273  
$ UnderPrediction_Ratio = {under-prediction 개수 \over 데이터의 샘플수} $
- Mean Squared Error (MSE) : 13.109761615019222  
$ MAE = {1 \over n}{\sum_{i=1}^{n}(f(x_i) - y_i)^2} $
