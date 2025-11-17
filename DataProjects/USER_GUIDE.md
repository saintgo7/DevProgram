# 데이터 프로젝트 사용 설명서 📊

**Data Projects User Guide**

## 개요

이 폴더에는 **50개의 데이터 분석 및 머신러닝 프로젝트**가 포함되어 있습니다.

### 기술 스택
- **Python**: Pandas, NumPy, Scikit-learn
- **R**: ggplot2, dplyr, tidyverse
- **Julia**: DataFrames.jl, MLJ.jl
- **Visualization**: Matplotlib, Seaborn, Plotly

## 빠른 시작

```bash
# Python 프로젝트
cd DataProjects/001_SalesAnalysis
pip install -r requirements.txt
jupyter notebook analysis.ipynb

# R 프로젝트
cd DataProjects/002_CustomerSegmentation
Rscript analysis.R

# Julia 프로젝트
cd DataProjects/003_SentimentAnalysis
julia analysis.jl
```

## 주요 프로젝트

| No. | 프로젝트 이름 | 분야 | 기술 |
|-----|--------------|------|------|
| 001 | Sales Analysis | 매출 분석 | Pandas, Matplotlib |
| 002 | Customer Segmentation | 고객 분류 | K-Means, Scikit-learn |
| 003 | Sentiment Analysis | 감성 분석 | NLP, NLTK |
| 004 | Stock Prediction | 주가 예측 | LSTM, TensorFlow |
| 005 | Image Classification | 이미지 분류 | CNN, PyTorch |
| 006 | Recommendation System | 추천 시스템 | Collaborative Filtering |
| 007 | Time Series Forecasting | 시계열 예측 | Prophet, ARIMA |
| 008 | A/B Testing | A/B 테스트 | 통계 분석 |
| 009 | Churn Prediction | 이탈 예측 | XGBoost |
| 010 | Fraud Detection | 사기 탐지 | Anomaly Detection |

## 개발 환경 설정

### Anaconda (권장)

```bash
# Anaconda 설치
wget https://repo.anaconda.com/archive/Anaconda3-latest-Linux-x86_64.sh
bash Anaconda3-latest-Linux-x86_64.sh

# 환경 생성
conda create -n data-science python=3.10
conda activate data-science

# 패키지 설치
conda install pandas numpy scikit-learn matplotlib seaborn
conda install jupyter notebook jupyterlab
conda install tensorflow pytorch
```

### pip 사용

```bash
python -m venv venv
source venv/bin/activate
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

## 데이터 소스

### 공개 데이터셋
- **Kaggle**: https://www.kaggle.com/datasets
- **UCI ML Repository**: https://archive.ics.uci.edu/
- **Google Dataset Search**: https://datasetsearch.research.google.com/
- **Data.gov**: https://data.gov/

### API
- **Alpha Vantage** (주식 데이터)
- **OpenWeather** (날씨 데이터)
- **Twitter API** (소셜 미디어)

## 워크플로우

### 1. 데이터 수집

```python
import pandas as pd

# CSV 읽기
df = pd.read_csv('data.csv')

# API 호출
import requests
response = requests.get('https://api.example.com/data')
data = response.json()
```

### 2. 데이터 전처리

```python
# 결측치 처리
df.dropna()
df.fillna(df.mean())

# 이상치 제거
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
```

### 3. EDA (탐색적 데이터 분석)

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 기본 통계
df.describe()

# 시각화
sns.pairplot(df)
plt.show()
```

### 4. 모델 학습

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)
```

### 5. 평가 및 배포

```python
from sklearn.metrics import accuracy_score, classification_report

y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# 모델 저장
import joblib
joblib.dump(model, 'model.pkl')
```

## 시각화 도구

### Matplotlib/Seaborn

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.barplot(x='category', y='value', data=df)
plt.title('Title')
plt.show()
```

### Plotly (인터랙티브)

```python
import plotly.express as px

fig = px.scatter(df, x='x', y='y', color='category')
fig.show()
```

### Tableau/Power BI
- 대시보드 생성
- 비즈니스 인텔리전스

## 머신러닝 라이브러리

### Scikit-learn
- 분류, 회귀, 클러스터링
- 전처리, 모델 선택
- 파이프라인

### TensorFlow/Keras
- 딥러닝
- 신경망
- 이미지/텍스트 처리

### PyTorch
- 딥러닝
- 연구용
- 유연한 API

### XGBoost/LightGBM
- Gradient Boosting
- 경진대회에서 인기
- 고성능

## Jupyter Notebook 사용

```bash
# Notebook 시작
jupyter notebook

# JupyterLab (고급 기능)
jupyter lab

# 원격 접속
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser
```

### 유용한 매직 명령어

```python
%matplotlib inline  # 그래프 인라인 표시
%%time              # 실행 시간 측정
%load_ext autoreload
%autoreload 2       # 모듈 자동 리로드
```

## 모범 사례

### 1. 프로젝트 구조

```
project/
├── data/
│   ├── raw/           # 원본 데이터
│   └── processed/     # 전처리된 데이터
├── notebooks/         # Jupyter 노트북
├── src/              # Python 모듈
├── models/           # 학습된 모델
├── outputs/          # 결과물
└── requirements.txt  # 의존성
```

### 2. 버전 관리

```bash
# Git LFS로 대용량 파일 관리
git lfs install
git lfs track "*.csv"
git lfs track "*.pkl"
```

### 3. 재현성

```python
# 랜덤 시드 고정
import numpy as np
import random

random.seed(42)
np.random.seed(42)
```

## 문제 해결

**메모리 오류:**
```python
# 청크 단위로 읽기
for chunk in pd.read_csv('large_file.csv', chunksize=10000):
    process(chunk)
```

**느린 실행:**
```python
# Vectorization 사용
df['new_col'] = df['col1'] + df['col2']  # 빠름
# vs.
df['new_col'] = df.apply(lambda x: x['col1'] + x['col2'], axis=1)  # 느림
```

## 학습 자료

### 온라인 코스
- Coursera: Machine Learning (Andrew Ng)
- Fast.ai: Practical Deep Learning
- DataCamp: Data Science Career Track

### 책
- "Python for Data Analysis" (Wes McKinney)
- "Hands-On Machine Learning" (Aurélien Géron)
- "Deep Learning" (Ian Goodfellow)

### 커뮤니티
- Kaggle Forums
- Stack Overflow
- Reddit - r/datascience, r/MachineLearning

마지막 업데이트: 2025-11-17
