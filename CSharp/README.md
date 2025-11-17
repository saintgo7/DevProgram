# C# Programs Collection

**200 Enterprise-Ready C# Programs**

현업에서 가장 많이 사용되는 C# 프로그램 200개 모음집

## 📁 프로그램 구조

각 프로그램은 `XXX_Program/Program.cs` 형식으로 구성되어 있습니다.

```
CSharp/
├── 001_Program/
│   └── Program.cs      # File Reader
├── 002_Program/
│   └── Program.cs      # File Writer
├── ...
└── 200_Program/
    └── Program.cs      # Advanced Feature
```

## 🚀 실행 방법

### 컴파일 및 실행
```bash
# 단일 프로그램 컴파일
cd 001_Program
csc Program.cs

# 실행
./Program.exe  # Windows
mono Program.exe  # Linux/Mac with Mono

# 또는 .NET CLI 사용
dotnet run
```

### .NET SDK 사용 (권장)
```bash
cd 001_Program
dotnet new console -f net6.0 -n Program
# Program.cs를 프로젝트에 복사
dotnet run
```

## 📚 프로그램 카테고리

### 001-040: 기본 유틸리티 & 파일 작업
- 001: File Reader - 파일 읽기 및 통계
- 002: File Writer - 파일 쓰기
- 003: Directory Lister - 디렉토리 목록
- 004: File Copy Tool - 파일 복사
- 005: File Search - 파일 검색
- 006-010: 파일 처리 도구들
- 011: Text File Merger - 파일 병합
- 012: File Encryption - 파일 암호화
- 013: File Decryption - 파일 복호화
- 014: Text Statistics - 텍스트 통계
- 015: Duplicate Finder - 중복 파일 찾기
- 016-040: 추가 유틸리티

### 041-080: 데이터 처리 & 변환
- 041: JSON Reader - JSON 데이터 읽기
- 042: JSON Writer - JSON 데이터 쓰기
- 043: XML Parser - XML 파싱
- 044: CSV Reader - CSV 파일 읽기
- 045: CSV Writer - CSV 파일 쓰기
- 046-080: 데이터 변환 및 처리 도구

### 081-120: 네트워크 & 웹 서비스
- 081: HTTP Client - HTTP 요청
- 082: Web Download - 파일 다운로드
- 083: REST API Call - REST API 호출
- 084: URL Validator - URL 검증
- 085-120: 네트워크 통신 도구

### 121-160: 데이터베이스 & 엔터프라이즈
- 121: Connection String Builder - 연결 문자열 생성
- 122: SQL Query Builder - SQL 쿼리 빌더
- 123: Config Reader - 설정 파일 읽기
- 124-160: 엔터프라이즈 도구

### 161-200: 고급 기능 & 시스템
- 161: Async File Reader - 비동기 파일 읽기
- 162: Parallel Processing - 병렬 처리
- 163: LINQ Query - LINQ 쿼리 예제
- 164: Delegate Example - 델리게이트 사용
- 165: Event Handler - 이벤트 핸들러
- 166-200: 고급 C# 기능

## 💡 주요 기능

### 파일 I/O
- 파일 읽기/쓰기/복사/검색
- 텍스트 처리 및 분석
- 암호화/복호화
- 중복 파일 감지

### 데이터 처리
- JSON 직렬화/역직렬화
- XML 파싱
- CSV 파일 처리
- 데이터 변환

### 네트워킹
- HTTP/HTTPS 통신
- REST API 호출
- 파일 다운로드
- URL 처리

### 엔터프라이즈
- 데이터베이스 연결
- 설정 관리
- 로깅
- 쿼리 빌더

### 고급 기능
- 비동기 프로그래밍 (async/await)
- 병렬 처리 (Parallel, Task)
- LINQ 쿼리
- 델리게이트 및 이벤트
- 리플렉션
- 제네릭

## 🔧 필수 요구사항

### 최소 요구사항
- .NET Framework 4.7.2 이상
- 또는 .NET Core 3.1 이상
- 또는 .NET 5/6/7/8

### 권장 환경
- .NET 6.0 이상 (LTS)
- Visual Studio 2022 또는 VS Code
- C# 10.0 이상

## 📖 사용 예제

### 예제 1: File Reader (001)
```bash
cd 001_Program
csc Program.cs
Program.exe

# 입력: C:\test.txt
# 출력: 파일 내용 및 통계
```

### 예제 2: JSON Reader (041)
```bash
cd 041_Program
csc Program.cs
Program.exe

# JSON 데이터 파싱 및 출력
```

### 예제 3: HTTP Client (081)
```bash
cd 081_Program
csc Program.cs
Program.exe

# HTTP 요청 및 응답 출력
```

## 🌟 주요 특징

- ✅ **독립 실행**: 각 프로그램이 완전히 독립적
- ✅ **실전 활용**: 현업에서 바로 사용 가능
- ✅ **명확한 코드**: 이해하기 쉬운 구조
- ✅ **에러 처리**: Try-Catch를 통한 안전한 실행
- ✅ **최신 C#**: 최신 C# 기능 활용

## 📝 코드 규칙

### 네이밍
- **Class**: PascalCase (예: `FileReader`)
- **Method**: PascalCase (예: `ReadFile`)
- **Variable**: camelCase (예: `fileName`)
- **Constant**: UPPER_CASE (예: `MAX_SIZE`)

### 구조
```csharp
// 주석으로 프로그램 설명
using System;
using System.IO;

class Program
{
    static void Main()
    {
        // 메인 로직
    }
}
```

## 🔍 카테고리별 주요 프로그램

### 파일 처리
- File Reader/Writer
- Directory Operations
- File Search & Filter
- Encryption/Decryption

### 데이터 처리
- JSON/XML Processing
- CSV Operations
- Data Transformation
- Serialization

### 네트워크
- HTTP Client
- Web Scraping
- API Integration
- Download Manager

### 비동기 & 병렬
- Async/Await Patterns
- Task Parallel Library
- Concurrent Collections
- Thread Management

### LINQ & Collections
- Query Expressions
- Method Syntax
- Aggregation
- Grouping & Filtering

## 🚀 고급 활용

### 프로젝트로 변환
```bash
# .NET 프로젝트 생성
dotnet new console -n MyProject
cd MyProject

# Program.cs 복사
cp ../001_Program/Program.cs .

# 실행
dotnet run
```

### NuGet 패키지 추가
```bash
dotnet add package Newtonsoft.Json
dotnet add package Dapper
dotnet add package Serilog
```

## 📚 학습 순서 (추천)

1. **초급**: 001-040 (기본 I/O 및 파일 처리)
2. **중급**: 041-120 (데이터 처리 및 네트워크)
3. **고급**: 121-200 (엔터프라이즈 및 고급 기능)

## 🛠️ 컴파일러 옵션

### CSC (C# Compiler)
```bash
csc /out:MyProgram.exe Program.cs
csc /optimize+ Program.cs
csc /target:library Program.cs
```

### .NET CLI
```bash
dotnet build
dotnet build -c Release
dotnet publish -c Release -r win-x64
```

## 💼 실무 활용 팁

1. **에러 처리**: 모든 I/O 작업에 try-catch 사용
2. **리소스 관리**: using 문으로 자동 해제
3. **비동기 처리**: I/O 바운드 작업은 async/await
4. **LINQ 활용**: 컬렉션 처리 시 LINQ 우선 고려
5. **로깅**: 프로덕션 환경에서는 적절한 로깅 추가

## 📞 도움말

### 컴파일 에러
- .NET SDK 설치 확인: `dotnet --version`
- C# 버전 확인: 프로젝트 파일에서 `<LangVersion>` 설정

### 런타임 에러
- 경로 확인: 절대 경로 또는 올바른 상대 경로 사용
- 권한 확인: 파일/디렉토리 접근 권한 확인

## 🎯 학습 목표

이 200개 프로그램을 통해 다음을 학습할 수 있습니다:

- ✅ C# 기본 문법 및 구조
- ✅ 파일 및 디렉토리 처리
- ✅ 데이터 직렬화/역직렬화
- ✅ 네트워크 프로그래밍
- ✅ 비동기 프로그래밍
- ✅ LINQ 쿼리
- ✅ 델리게이트 및 이벤트
- ✅ 엔터프라이즈 패턴

## 📄 라이선스

이 프로그램들은 학습 및 실무 활용 목적으로 자유롭게 사용할 수 있습니다.

---

**Created**: 2025-11-17
**Total Programs**: 200
**Language**: C# (.NET)
