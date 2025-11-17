# Python Programs Collection 🐍

**200 Professional Python Programs**

현업에서 가장 많이 사용되는 Python 프로그램 200개 모음집

## 📁 프로그램 구조

각 프로그램은 `XXX_Program/program.py` 형식으로 구성되어 있습니다.

```
Python/
├── 001_Program/
│   └── program.py      # File Reader
├── 002_Program/
│   └── program.py      # File Writer
├── ...
└── 200_Program/
    └── program.py      # Advanced Feature
```

## 🚀 실행 방법

### 기본 실행
```bash
# 방법 1: Python 인터프리터로 직접 실행
cd 001_Program
python3 program.py

# 방법 2: 실행 권한 부여 후 직접 실행
chmod +x program.py
./program.py

# 방법 3: 모듈로 실행
python3 -m program
```

### 가상 환경 사용 (권장)
```bash
# 가상 환경 생성
python3 -m venv venv

# 활성화
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 의존성 설치
pip install -r requirements.txt

# 프로그램 실행
cd 001_Program
python3 program.py
```

## 📚 프로그램 카테고리

### 001-050: 기본 유틸리티 & 파일 작업 📂
- **001**: File Reader - 파일 읽기 및 통계
- **002**: File Writer - 파일 쓰기
- **003**: Directory Lister - 디렉토리 목록
- **004**: File Copy - 파일 복사
- **005**: File Search - 패턴 기반 파일 검색
- **006-050**: 다양한 파일 및 시스템 유틸리티

**주요 기능:**
- 파일 I/O 작업
- 디렉토리 탐색
- 파일 검색 및 필터링
- 경로 처리
- 파일 메타데이터

### 051-100: 데이터 처리 & 분석 📊
- **051**: JSON Reader - JSON 데이터 읽기
- **052**: JSON Writer - JSON 데이터 쓰기
- **053**: CSV Reader - CSV 파일 처리
- **054**: CSV Writer - CSV 데이터 생성
- **055**: XML Parser - XML 파싱
- **056-100**: 데이터 변환 및 분석 도구

**주요 기능:**
- JSON 직렬화/역직렬화
- CSV 파일 처리
- XML 파싱
- 데이터 변환
- 정규표현식
- 텍스트 처리

### 101-150: 웹 & 자동화 🌐
- **101**: Web Scraper - 웹 스크래핑
- **102**: URL Download - 파일 다운로드
- **103**: Email Validator - 이메일 검증
- **104**: Password Generator - 비밀번호 생성
- **105-150**: 웹 크롤링 및 자동화 도구

**주요 기능:**
- HTTP 요청
- 웹 스크래핑
- API 호출
- 자동화 스크립트
- 정규표현식 검증
- 데이터 수집

### 151-200: 데이터 과학 & 고급 기능 🔬
- **151**: Statistics Calculator - 통계 계산
- **152**: List Comprehension - 리스트 컴프리헨션
- **153**: Lambda Functions - 람다 함수
- **154**: Decorator Example - 데코레이터
- **155**: Context Manager - 컨텍스트 매니저
- **156-200**: 고급 Python 기능

**주요 기능:**
- 함수형 프로그래밍
- 데코레이터
- 제너레이터
- 컨텍스트 매니저
- 메타프로그래밍
- 비동기 프로그래밍

## 💡 주요 특징

### Pythonic 코드
- ✅ **PEP 8** 스타일 가이드 준수
- ✅ **Type Hints** 사용 (Python 3.6+)
- ✅ **List Comprehension** 활용
- ✅ **Context Managers** (with 문)
- ✅ **Generators** 및 Iterators
- ✅ **Decorators** 패턴

### 실용성
- ✅ **독립 실행**: 각 프로그램이 완전히 독립적
- ✅ **에러 처리**: try-except 블록
- ✅ **입력 검증**: 사용자 입력 검증
- ✅ **문서화**: Docstrings 및 주석
- ✅ **모듈화**: 함수 기반 구조

## 🔧 필수 요구사항

### Python 버전
- **최소**: Python 3.6+
- **권장**: Python 3.9+ 또는 3.10+
- **최신**: Python 3.11+ (성능 향상)

### 기본 패키지 (표준 라이브러리)
```python
import os           # 파일 시스템
import sys          # 시스템
import json         # JSON 처리
import csv          # CSV 처리
import xml.etree.ElementTree  # XML
import re           # 정규표현식
import urllib       # URL 처리
import random       # 랜덤
import string       # 문자열 유틸
```

### 추가 패키지 (선택사항)
```bash
pip install requests      # HTTP 라이브러리
pip install beautifulsoup4  # 웹 스크래핑
pip install pandas        # 데이터 분석
pip install numpy         # 수치 계산
pip install matplotlib    # 시각화
```

## 📖 사용 예제

### 예제 1: File Reader (001)
```bash
cd 001_Program
python3 program.py

# 입력: /path/to/file.txt
# 출력: 파일 내용 및 통계
```

### 예제 2: JSON Reader (051)
```bash
cd 051_Program
python3 program.py

# JSON 데이터 파싱 및 출력
```

### 예제 3: Web Scraper (101)
```bash
cd 101_Program
python3 program.py

# 입력: https://example.com
# 출력: HTML 내용 (처음 500자)
```

## 🌟 Python 주요 기능

### 1. 파일 처리
```python
# 파일 읽기
with open('file.txt', 'r') as f:
    content = f.read()

# 파일 쓰기
with open('file.txt', 'w') as f:
    f.write('Hello, World!')
```

### 2. 리스트 컴프리헨션
```python
# 제곱수 리스트
squares = [x**2 for x in range(10)]

# 필터링
evens = [x for x in range(20) if x % 2 == 0]
```

### 3. 람다 함수
```python
# 람다 함수
square = lambda x: x**2

# map 함수와 함께 사용
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
```

### 4. 데코레이터
```python
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time: {end - start}s")
        return result
    return wrapper

@timer
def slow_function():
    # 함수 내용
    pass
```

### 5. 컨텍스트 매니저
```python
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager('test.txt') as f:
    f.write('Hello!')
```

## 📝 코드 규칙

### 네이밍 컨벤션 (PEP 8)
- **변수/함수**: snake_case (예: `file_name`, `read_file()`)
- **클래스**: PascalCase (예: `FileReader`, `DataProcessor`)
- **상수**: UPPER_CASE (예: `MAX_SIZE`, `DEFAULT_PATH`)
- **Private**: _leading_underscore (예: `_internal_method`)

### 파일 구조
```python
#!/usr/bin/env python3
"""
모듈 docstring
프로그램에 대한 설명
"""

# 표준 라이브러리 import
import os
import sys

# 서드파티 라이브러리 import
import requests

# 로컬 모듈 import
from mymodule import something

# 상수
MAX_SIZE = 100

# 클래스 정의
class MyClass:
    pass

# 함수 정의
def main():
    """메인 함수"""
    pass

# 스크립트 실행
if __name__ == "__main__":
    main()
```

## 🚀 고급 활용

### 가상 환경 관리
```bash
# venv 사용
python3 -m venv venv
source venv/bin/activate

# virtualenv 사용
pip install virtualenv
virtualenv venv
source venv/bin/activate

# conda 사용
conda create -n myenv python=3.10
conda activate myenv
```

### 패키지 관리
```bash
# requirements.txt 생성
pip freeze > requirements.txt

# 의존성 설치
pip install -r requirements.txt

# 특정 버전 설치
pip install requests==2.28.0
```

### 프로파일링
```bash
# cProfile로 성능 측정
python3 -m cProfile program.py

# line_profiler로 라인별 측정
pip install line_profiler
kernprof -l -v program.py
```

## 📊 카테고리별 학습 순서

### 초급 (1-2주)
1. **001-025**: 기본 파일 I/O
2. **026-050**: 시스템 유틸리티
3. 파이썬 기본 문법 복습

### 중급 (2-3주)
4. **051-075**: 데이터 처리 (JSON, CSV, XML)
5. **076-100**: 정규표현식 및 텍스트 처리
6. **101-125**: 웹 스크래핑 기초

### 고급 (3-4주)
7. **126-150**: 자동화 및 API
8. **151-175**: 함수형 프로그래밍
9. **176-200**: 고급 Python 기능

## 🛠️ 개발 도구

### 에디터/IDE
- **VS Code** + Python 확장
- **PyCharm** (Community/Professional)
- **Jupyter Notebook** (데이터 분석용)
- **Vim/Neovim** + Python 플러그인

### 린터/포매터
```bash
# Black (코드 포매터)
pip install black
black program.py

# Pylint (린터)
pip install pylint
pylint program.py

# Flake8 (스타일 체커)
pip install flake8
flake8 program.py

# isort (import 정렬)
pip install isort
isort program.py
```

### 타입 체커
```bash
# mypy
pip install mypy
mypy program.py
```

## 💼 실무 활용 팁

### 1. 에러 처리
```python
try:
    # 위험한 작업
    result = risky_operation()
except FileNotFoundError:
    # 특정 예외 처리
    print("File not found!")
except Exception as e:
    # 일반 예외 처리
    print(f"Error: {e}")
finally:
    # 정리 작업
    cleanup()
```

### 2. 로깅
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Information message")
logger.warning("Warning message")
logger.error("Error message")
```

### 3. 커맨드 라인 인자
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Input file')
parser.add_argument('--output', help='Output file')
args = parser.parse_args()
```

### 4. 환경 변수
```python
import os

api_key = os.getenv('API_KEY', 'default_key')
debug_mode = os.getenv('DEBUG', 'False') == 'True'
```

## 📦 주요 라이브러리

### 웹 개발
- **Flask** - 마이크로 웹 프레임워크
- **Django** - 풀스택 웹 프레임워크
- **FastAPI** - 현대적인 API 프레임워크

### 데이터 과학
- **Pandas** - 데이터 분석
- **NumPy** - 수치 계산
- **Matplotlib** - 시각화
- **Scikit-learn** - 머신러닝

### 웹 스크래핑
- **Requests** - HTTP 라이브러리
- **BeautifulSoup4** - HTML 파싱
- **Scrapy** - 웹 크롤링 프레임워크
- **Selenium** - 브라우저 자동화

### 유틸리티
- **Click** - CLI 도구
- **python-dotenv** - 환경 변수 관리
- **Pillow** - 이미지 처리
- **PyYAML** - YAML 처리

## 🎯 학습 목표

이 200개 프로그램을 통해 다음을 마스터할 수 있습니다:

- ✅ Python 기본 문법 및 구조
- ✅ 파일 I/O 및 시스템 프로그래밍
- ✅ 데이터 처리 (JSON, CSV, XML)
- ✅ 웹 스크래핑 및 API 호출
- ✅ 정규표현식 및 텍스트 처리
- ✅ 함수형 프로그래밍
- ✅ 객체지향 프로그래밍
- ✅ 데코레이터 및 메타프로그래밍
- ✅ 비동기 프로그래밍 (async/await)
- ✅ 테스팅 및 디버깅

## 🔍 유용한 리소스

### 공식 문서
- [Python 공식 문서](https://docs.python.org/3/)
- [PEP 8 스타일 가이드](https://pep8.org/)
- [Python Package Index (PyPI)](https://pypi.org/)

### 학습 자료
- Real Python
- Python.org Tutorial
- Automate the Boring Stuff with Python

### 커뮤니티
- r/Python (Reddit)
- Stack Overflow
- Python Discord

## 📄 라이선스

이 프로그램들은 학습 및 실무 활용 목적으로 자유롭게 사용할 수 있습니다.

---

**Created**: 2025-11-17
**Total Programs**: 200
**Language**: Python 3.6+
**Style**: PEP 8 Compliant

**Happy Coding! 🐍✨**
