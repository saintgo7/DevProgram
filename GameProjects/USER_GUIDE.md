# 게임 프로젝트 사용 설명서 🎮

**Game Projects User Guide**

## 개요

이 폴더에는 **50개의 게임 프로젝트**가 포함되어 있습니다.

### 게임 엔진
- **Unity**: 2D/3D 게임 개발
- **Unreal Engine**: AAA급 3D 게임
- **Godot**: 오픈소스 게임 엔진

## 빠른 시작

### Unity 게임

```bash
# 1. Unity Hub 설치
# 2. Unity 프로젝트 열기
cd GameProjects/001_PlatformerGame
# Unity에서 폴더 열기

# 3. Play 버튼 클릭
```

### Unreal 게임

```bash
# 1. Unreal Engine 설치
# 2. .uproject 파일 더블클릭
# 3. Compile 후 Play
```

## 주요 게임

| No. | 게임 이름 | 장르 | 엔진 |
|-----|----------|------|------|
| 001 | 2D Platformer | 플랫포머 | Unity |
| 002 | FPS Shooter | 슈팅 | Unreal |
| 003 | Puzzle Game | 퍼즐 | Unity |
| 004 | Racing Game | 레이싱 | Unreal |
| 005 | RPG Game | RPG | Unity |
| 006 | Tower Defense | 전략 | Unity |
| 007 | Card Game | 카드 | Unity |

## 개발 환경

### Unity
- **버전**: Unity 2022.3 LTS
- **C# 스크립팅**
- **Visual Studio / Rider**

### Unreal Engine
- **버전**: Unreal Engine 5.3
- **C++ / Blueprints**
- **Visual Studio 2022**

## 게임 빌드

### Unity 빌드
1. File → Build Settings
2. 플랫폼 선택 (Windows/Mac/Android/iOS)
3. Build 클릭

### Unreal 빌드
1. File → Package Project
2. 플랫폼 선택
3. 저장 위치 선택

## 애셋

### 무료 애셋 스토어
- **Unity Asset Store**
- **Unreal Marketplace**
- **itch.io**
- **OpenGameArt**

## 배포

### Steam
1. Steamworks 계정 생성
2. 앱 ID 발급
3. 빌드 업로드

### Mobile (iOS/Android)
1. 모바일 플랫폼 빌드
2. App Store / Play Store 등록
3. 심사 제출

## 문제 해결

**Unity 컴파일 오류:**
```
Assets → Reimport All
```

**Unreal 크래시:**
```
프로젝트 Clean 후 Rebuild
```

마지막 업데이트: 2025-11-17
