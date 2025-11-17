# 웹 애플리케이션 사용 설명서 📚

**Web Applications User Guide**

---

## 📖 목차 (Table of Contents)

1. [개요](#개요)
2. [시작하기](#시작하기)
3. [프로젝트 목록](#프로젝트-목록)
4. [설치 가이드](#설치-가이드)
5. [개발 환경 설정](#개발-환경-설정)
6. [배포 가이드](#배포-가이드)
7. [문제 해결](#문제-해결)
8. [자주 묻는 질문](#자주-묻는-질문)

---

## 개요

이 폴더에는 **50개의 실제 웹 애플리케이션 프로젝트**가 포함되어 있습니다. 각 프로젝트는 실무에서 사용할 수 있는 완전한 풀스택 애플리케이션입니다.

### 🎯 주요 특징

- ✅ **풀스택 구현**: Frontend + Backend + Database
- ✅ **최신 기술 스택**: React, Vue, Next.js, Django, FastAPI 등
- ✅ **실전 기능**: 인증, CRUD, 실시간 업데이트
- ✅ **보안 기능**: JWT, 암호화, 입력 검증
- ✅ **배포 준비**: Docker, CI/CD 설정 포함
- ✅ **완전한 문서화**: README, API 문서, 주석

### 📊 기술 스택

**Frontend Frameworks:**
- React.js + TypeScript
- Vue.js 3 + Composition API
- Next.js (SSR/SSG)
- Angular 17
- Svelte + SvelteKit

**Backend Frameworks:**
- Node.js + Express
- Django + Django REST Framework
- FastAPI (Python)
- ASP.NET Core (C#)
- Spring Boot (Java)

**Databases:**
- PostgreSQL (관계형)
- MongoDB (NoSQL)
- MySQL
- Redis (캐싱)

---

## 시작하기

### 1️⃣ 필수 도구 설치

```bash
# Node.js 설치 확인
node --version  # v18 이상

# Python 설치 확인 (Django/FastAPI 프로젝트용)
python --version  # 3.8 이상

# Docker 설치 확인
docker --version
docker-compose --version

# Git 설치 확인
git --version
```

### 2️⃣ 프로젝트 선택

웹 애플리케이션 목록에서 원하는 프로젝트를 선택하세요:

```bash
# 프로젝트 목록 보기
ls WebApps/

# 예시: 블로그 플랫폼 선택
cd WebApps/001_BlogPlatform
```

### 3️⃣ README 확인

각 프로젝트의 README.md를 확인하세요:

```bash
cat README.md
```

---

## 프로젝트 목록

### 🌟 Featured Projects (1-10)

| No. | 프로젝트명 | 기술 스택 | 설명 |
|-----|-----------|----------|------|
| 001 | **Blog Platform** | Next.js + MongoDB | 블로그 플랫폼 (인증, 게시글, 댓글, 태그) |
| 002 | **E-commerce Store** | React + Express + PostgreSQL | 온라인 쇼핑몰 (장바구니, 결제, 재고관리) |
| 003 | **Project Management** | Vue.js + Django + MySQL | 프로젝트 관리 (태스크, 타임라인, 팀 협업) |
| 004 | **Social Network** | Next.js + GraphQL + MongoDB | 소셜 네트워크 (프로필, 게시글, 친구, 좋아요) |
| 005 | **Video Streaming** | React + Node.js + AWS S3 | 비디오 스트리밍 (업로드, 재생, 구독) |
| 006 | **Chat Application** | Svelte + Socket.io + Redis | 실시간 채팅 (채널, DM, 파일 공유) |
| 007 | **Learning Management** | Angular + ASP.NET + SQL Server | 온라인 교육 플랫폼 (강의, 퀴즈, 진도) |
| 008 | **Weather Dashboard** | React + OpenWeather API | 날씨 대시보드 (예보, 지도, 알림) |
| 009 | **Recipe Sharing** | Django + PostgreSQL | 레시피 공유 (저장, 식단 계획) |
| 010 | **Fitness Tracker** | Vue.js + FastAPI + MongoDB | 운동 추적 (운동, 영양, 목표, 차트) |

### 📱 Productivity & Business (11-25)

| No. | 프로젝트명 | 설명 |
|-----|-----------|------|
| 011 | Portfolio Website | 개인 포트폴리오 사이트 |
| 012 | Job Board | 구인구직 플랫폼 |
| 013 | Event Planner | 이벤트 관리 시스템 |
| 014 | Digital Library | 디지털 도서관 |
| 015 | Expense Tracker | 지출 관리 앱 |
| 016 | Music Streaming | 음악 스트리밍 서비스 |
| 017 | Photo Gallery | 사진 갤러리 |
| 018 | Discussion Forum | 온라인 포럼 |
| 019 | URL Shortener | URL 단축 서비스 |
| 020 | Markdown Editor | 마크다운 에디터 |
| 021 | Code Snippet Manager | 코드 스니펫 관리 |
| 022 | News Aggregator | 뉴스 수집 서비스 |
| 023 | CRM System | 고객 관계 관리 |
| 024 | Inventory Manager | 재고 관리 시스템 |
| 025 | Help Desk System | 고객 지원 시스템 |

### 🛠️ Enterprise & Tools (26-40)

| No. | 프로젝트명 | 설명 |
|-----|-----------|------|
| 026 | Wiki Platform | 위키 플랫폼 |
| 027 | Poll & Survey Tool | 설문조사 도구 |
| 028 | Calendar Application | 캘린더 앱 |
| 029 | Password Vault | 비밀번호 관리자 |
| 030 | File Sharing Service | 파일 공유 서비스 |
| 031 | Invoice Generator | 송장 생성기 |
| 032 | Time Tracking | 시간 추적 도구 |
| 033 | Form Builder | 폼 빌더 (드래그앤드롭) |
| 034 | Quiz Platform | 퀴즈 플랫폼 |
| 035 | Bug Tracking System | 버그 추적 시스템 |
| 036 | Web Email Client | 웹 이메일 클라이언트 |
| 037 | Kanban Board | 칸반 보드 |
| 038 | Document Editor | 문서 편집기 |
| 039 | Real Estate Portal | 부동산 포털 |
| 040 | Restaurant Menu System | 레스토랑 메뉴 시스템 |

### 🎯 Specialized Applications (41-50)

| No. | 프로젝트명 | 설명 |
|-----|-----------|------|
| 041 | Appointment Scheduler | 예약 스케줄러 |
| 042 | Crypto Dashboard | 암호화폐 대시보드 |
| 043 | Gym Management | 헬스장 관리 시스템 |
| 044 | Pet Adoption Platform | 반려동물 입양 플랫폼 |
| 045 | Travel Planner | 여행 계획 도구 |
| 046 | Online Examination | 온라인 시험 시스템 |
| 047 | Donation Platform | 기부 플랫폼 |
| 048 | Podcast Platform | 팟캐스트 플랫폼 |
| 049 | Stock Portfolio Tracker | 주식 포트폴리오 추적 |
| 050 | Language Learning App | 언어 학습 앱 |

---

## 설치 가이드

### 방법 1: Docker 사용 (권장) 🐳

가장 빠르고 쉬운 방법입니다!

```bash
# 1. 프로젝트 폴더로 이동
cd WebApps/001_BlogPlatform

# 2. Docker Compose 실행
docker-compose up -d

# 3. 애플리케이션 접속
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
```

### 방법 2: 수동 설치

#### Frontend 설정

```bash
# 1. Frontend 폴더로 이동
cd frontend

# 2. 의존성 설치
npm install
# 또는
yarn install

# 3. 환경 변수 설정
cp .env.example .env
# .env 파일 편집

# 4. 개발 서버 시작
npm run dev
```

#### Backend 설정

**Node.js/Express:**
```bash
cd backend
npm install
cp .env.example .env
npm run dev
```

**Django:**
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**FastAPI:**
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload
```

#### Database 설정

**PostgreSQL:**
```bash
# Docker로 PostgreSQL 실행
docker run --name postgres-db \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=myapp \
  -p 5432:5432 \
  -d postgres:15

# 또는 로컬 설치
sudo apt-get install postgresql
createdb myapp
```

**MongoDB:**
```bash
# Docker로 MongoDB 실행
docker run --name mongo-db \
  -p 27017:27017 \
  -d mongo:7

# 또는 로컬 설치
sudo apt-get install mongodb
```

---

## 개발 환경 설정

### IDE 추천

**Visual Studio Code:**
```bash
# 추천 확장 프로그램
code --install-extension dbaeumer.vscode-eslint
code --install-extension esbenp.prettier-vscode
code --install-extension ms-python.python
code --install-extension bradlc.vscode-tailwindcss
```

**WebStorm / IntelliJ IDEA:**
- TypeScript 지원
- 통합 디버거
- 데이터베이스 도구

### 코드 품질 도구

```bash
# ESLint (JavaScript/TypeScript)
npm install -D eslint prettier

# Black (Python)
pip install black flake8

# Pre-commit hooks
npm install -D husky lint-staged
```

### 브라우저 개발 도구

- **React Developer Tools** (Chrome/Firefox)
- **Vue.js DevTools** (Chrome/Firefox)
- **Redux DevTools** (React 상태 관리)
- **Apollo Client DevTools** (GraphQL)

---

## 배포 가이드

### Vercel 배포 (Next.js)

```bash
# 1. Vercel CLI 설치
npm i -g vercel

# 2. 로그인
vercel login

# 3. 배포
cd frontend
vercel

# 4. 프로덕션 배포
vercel --prod
```

### Heroku 배포 (Node.js/Python)

```bash
# 1. Heroku CLI 설치 및 로그인
heroku login

# 2. 앱 생성
heroku create my-app-name

# 3. PostgreSQL 추가
heroku addons:create heroku-postgresql:mini

# 4. 환경 변수 설정
heroku config:set JWT_SECRET=your-secret

# 5. 배포
git push heroku main

# 6. 마이그레이션 실행
heroku run python manage.py migrate
```

### AWS 배포

**S3 + CloudFront (정적 사이트):**
```bash
# Frontend 빌드
npm run build

# S3에 업로드
aws s3 sync build/ s3://my-bucket/

# CloudFront 무효화
aws cloudfront create-invalidation --distribution-id XXX --paths "/*"
```

**EC2 (백엔드):**
```bash
# 1. EC2 인스턴스 생성 (Ubuntu 22.04)
# 2. SSH 접속
ssh -i key.pem ubuntu@your-ec2-ip

# 3. 애플리케이션 설정
git clone your-repo
cd your-app
npm install
npm run build

# 4. PM2로 프로세스 관리
npm install -g pm2
pm2 start npm --name "my-app" -- start
pm2 startup
pm2 save
```

### Docker 배포 (프로덕션)

```bash
# 1. 이미지 빌드
docker build -t my-app:latest .

# 2. Docker Hub에 푸시
docker tag my-app:latest username/my-app:latest
docker push username/my-app:latest

# 3. 서버에서 실행
docker pull username/my-app:latest
docker run -d -p 80:3000 username/my-app:latest
```

---

## 문제 해결

### 자주 발생하는 문제

#### 1. 포트 충돌

**문제:** `Error: listen EADDRINUSE: address already in use :::3000`

**해결:**
```bash
# 포트 사용 중인 프로세스 찾기
lsof -i :3000
# 또는
netstat -ano | findstr :3000

# 프로세스 종료
kill -9 <PID>

# 또는 다른 포트 사용
PORT=3001 npm run dev
```

#### 2. 의존성 설치 오류

**문제:** `npm install` 실패

**해결:**
```bash
# 캐시 정리
npm cache clean --force

# node_modules 삭제 후 재설치
rm -rf node_modules package-lock.json
npm install

# Node 버전 확인
node --version  # v18+ 필요
```

#### 3. 데이터베이스 연결 오류

**문제:** `Error: connect ECONNREFUSED`

**해결:**
```bash
# PostgreSQL 실행 확인
sudo systemctl status postgresql

# MongoDB 실행 확인
sudo systemctl status mongod

# Docker 컨테이너 확인
docker ps

# 연결 문자열 확인
echo $DATABASE_URL
```

#### 4. CORS 오류

**문제:** `Access to fetch blocked by CORS policy`

**해결:**

Backend에서 CORS 설정:
```javascript
// Express
const cors = require('cors');
app.use(cors({
  origin: 'http://localhost:3000',
  credentials: true
}));

// Django
# settings.py
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

#### 5. 환경 변수 인식 안됨

**문제:** 환경 변수가 undefined

**해결:**
```bash
# .env 파일 위치 확인
ls -la .env

# .env 파일 로드 확인 (Node.js)
require('dotenv').config();

# React에서는 REACT_APP_ 접두사 필요
REACT_APP_API_URL=http://localhost:8000
```

---

## 자주 묻는 질문

### Q1: 어떤 프로젝트부터 시작해야 하나요?

**A:** 초보자라면 다음 순서를 추천합니다:
1. **011_PortfolioSite** - 가장 간단한 구조
2. **001_BlogPlatform** - CRUD 기본 학습
3. **003_TaskManager** - 복잡한 상태 관리 학습
4. **002_EcommerceSite** - 실전 프로젝트

### Q2: 프론트엔드와 백엔드를 동시에 실행해야 하나요?

**A:** 네, 풀스택 애플리케이션은 두 서버가 필요합니다:
- Frontend: 포트 3000 (React/Vue/Next.js)
- Backend: 포트 8000 (API 서버)

터미널 2개를 열어서 각각 실행하세요.

### Q3: 데이터베이스는 어떻게 선택하나요?

**A:**
- **PostgreSQL**: 복잡한 관계형 데이터 (추천)
- **MongoDB**: 유연한 스키마, NoSQL
- **MySQL**: 전통적인 관계형 DB
- **SQLite**: 개발/테스트용 (작은 프로젝트)

### Q4: 프로덕션 배포 시 주의사항은?

**A:**
- ✅ 환경 변수 설정 (.env)
- ✅ HTTPS 사용
- ✅ 데이터베이스 백업
- ✅ 로그 모니터링
- ✅ Rate Limiting 설정
- ✅ CDN 사용 (정적 파일)

### Q5: 인증은 어떻게 구현되나요?

**A:** 대부분의 프로젝트는 JWT 사용:
1. 사용자 로그인
2. 서버가 JWT 토큰 발급
3. 클라이언트가 토큰 저장 (localStorage/cookie)
4. API 요청 시 토큰 포함

### Q6: TypeScript를 사용해야 하나요?

**A:** 강력 추천! 장점:
- 타입 안정성
- 자동 완성
- 리팩토링 용이
- 버그 사전 방지

### Q7: 테스트는 어떻게 작성하나요?

**A:**
```bash
# Frontend (Jest + React Testing Library)
npm test

# Backend (pytest for Python)
pytest

# E2E (Cypress)
npx cypress open
```

### Q8: API 문서는 어디서 확인하나요?

**A:**
- FastAPI: http://localhost:8000/docs (Swagger UI)
- Express: Postman 컬렉션 사용
- Django REST: http://localhost:8000/api/docs/

---

## 📚 추가 학습 자료

### 공식 문서
- [React](https://react.dev/)
- [Vue.js](https://vuejs.org/)
- [Next.js](https://nextjs.org/)
- [Django](https://www.djangoproject.com/)
- [FastAPI](https://fastapi.tiangolo.com/)

### 튜토리얼
- [freeCodeCamp](https://www.freecodecamp.org/)
- [The Odin Project](https://www.theodinproject.com/)
- [Full Stack Open](https://fullstackopen.com/)

### 커뮤니티
- [Stack Overflow](https://stackoverflow.com/)
- [Reddit - r/webdev](https://reddit.com/r/webdev)
- [Dev.to](https://dev.to/)

---

## 📞 지원

문제가 발생하면:
1. 각 프로젝트의 README.md 확인
2. 문제 해결 섹션 참조
3. GitHub Issues에 문의

---

**Happy Coding!** 🚀

마지막 업데이트: 2025-11-17
