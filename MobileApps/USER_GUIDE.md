# 모바일 애플리케이션 사용 설명서 📱

**Mobile Applications User Guide**

## 개요

이 폴더에는 **50개의 모바일 앱 프로젝트**가 포함되어 있습니다.

### 기술 스택
- **React Native**: Cross-platform (iOS + Android)
- **Flutter**: Google의 UI 프레임워크
- **SwiftUI**: iOS 네이티브
- **Jetpack Compose**: Android 네이티브

## 빠른 시작

```bash
# React Native
cd MobileApps/001_ChatApp
npm install
npx react-native run-ios

# Flutter
cd MobileApps/002_FitnessTracker
flutter pub get
flutter run

# iOS (SwiftUI)
# Xcode에서 프로젝트 열기

# Android (Jetpack Compose)
# Android Studio에서 프로젝트 열기
```

## 주요 프로젝트

| No. | 앱 이름 | 프레임워크 | 설명 |
|-----|---------|-----------|------|
| 001 | Chat App | React Native | 실시간 메시징 |
| 002 | Fitness Tracker | Flutter | 운동 추적 |
| 003 | Expense Manager | SwiftUI | 지출 관리 |
| 004 | Recipe App | Jetpack Compose | 요리 레시피 |
| 030 | Banking App | React Native | 모바일 뱅킹 |
| 033 | Ride Sharing | React Native | 차량 공유 |

## 개발 환경 설정

### React Native
```bash
npm install -g react-native-cli
# iOS: Xcode 필요
# Android: Android Studio 필요
```

### Flutter
```bash
# Flutter SDK 설치
flutter doctor
```

## 배포

### iOS App Store
1. Xcode에서 Archive 생성
2. App Store Connect에 업로드
3. 심사 제출

### Google Play Store
1. 서명된 APK/AAB 생성
2. Play Console에 업로드
3. 프로덕션 릴리스

## 문제 해결

**Metro Bundler 오류:**
```bash
npx react-native start --reset-cache
```

**Flutter 빌드 오류:**
```bash
flutter clean
flutter pub get
```

마지막 업데이트: 2025-11-17
