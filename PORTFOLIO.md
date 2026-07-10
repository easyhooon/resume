# 이지훈 Android Developer Portfolio

<table>
  <tr>
    <td><strong>Phone</strong> 010-2010-3068</td>
    <td><strong>Email</strong> mraz3068@gmail.com</td>
  </tr>
  <tr>
    <td><strong>GitHub</strong> <a href="https://github.com/easyhooon">github.com/easyhooon</a></td>
    <td><strong>Tech Blog</strong> <a href="https://velog.io/@mraz3068">velog.io/@mraz3068</a></td>
  </tr>
  <tr>
    <td><strong>Resume</strong> <a href="./RESUME.md">RESUME.md</a></td>
    <td><strong>LinkedIn</strong> <a href="https://www.linkedin.com/in/easyhooon/">linkedin.com/in/easyhooon</a></td>
  </tr>
</table>

## Introduce

Android 앱에서 제품 요구사항을 네이티브 기능과 웹뷰 브릿지로 구현하고, 문제 재현과 원인 분석을 돕는 디버깅 환경을 구축합니다. BLE 의료기기 연동, Samsung Health Data SDK, Health Connect, Media3, CameraX/TensorFlow Lite 기반 기능을 실무에 적용했습니다.

사이드 프로젝트와 팀 프로젝트에서는 Android 앱 9개와 iOS 앱 1개를 출시·운영하며, 지도·위치 기반 탐색, OCR 기록, 이미지 공유, 로컬 저장소 전환, CI/CD 구축처럼 사용자 경험과 운영 안정성에 직접 연결되는 기능을 구현했습니다.

## Professional Projects

### Hi-me <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2025.10 ~</span>

HD현대 그룹사 임직원 대상 건강관리 헬스케어 서비스

**Overview**

| 항목 | 내용 |
| --- | --- |
| 역할 | Android 개발, 웹 프론트엔드 업무 병행, 웹뷰-네이티브 연동 |
| 주요 기술 | Kotlin, Android, WebView Bridge, Dari, BLE, Samsung Health Data SDK, Media3, GitHub Actions |

**Key Contributions**

- 웹뷰-네이티브 간 요청/응답 규격과 에러 처리 방식을 정의하고, 외주 개발사가 동일한 기준으로 연동·재현·분류할 수 있도록 가이드 제공
- 서비스 내 웹 프론트엔드 업무를 병행하며 웹뷰-네이티브 연동 이슈를 Android와 웹 양쪽 코드 흐름에서 추적·수정
- Dari 기반 WebView 브릿지 통신 디버깅 환경을 구축해 요청/응답 payload와 성공·실패 상태를 Android·프론트엔드 개발자가 함께 확인하도록 개선
- BLE Glucose/Blood Pressure Profile 기반 혈당계·혈압계 연동, 측정 데이터 동기화와 연동 해제까지 포함한 의료기기 데이터 수집 흐름 제공
- Samsung Health Data SDK 연동으로 Health Connect 경유 시 발생하던 걸음 수 미갱신 이슈를 보완하고 걸음 수·심박수·소모 칼로리 수집 경로 안정화
- 웹뷰 오디오 재생 상태를 MediaSession과 동기화해 백그라운드 재생과 미디어 알림 컨트롤 지원
- GitHub Actions 기반 Play Console 내부 테스트 트랙 CD 환경 구축

### 세컨드 윈드/닥터 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

만성질환자와 암 수술 환자를 위한 맞춤 건강관리·재활 서비스

**Overview**

| 항목 | 내용 |
| --- | --- |
| 역할 | Android 기능 개발, 플레이어 구조 개선, 측정 기능 개발 |
| 주요 기술 | Kotlin, Media3, CameraX, TensorFlow Lite, BLE, AAR |

**Key Contributions**

- ExoPlayer2 기반 운동 영상 플레이어를 Media3로 마이그레이션하고 다운로드·연속 재생 기능을 확장할 수 있는 재생 구조로 개선
- Media3 기반 단계별 다운로드와 연속 재생 기능을 도입해 운동 영상 대기와 재시작으로 끊기던 시청 흐름 개선
- TensorFlow Lite + CameraX 기반 어깨 움직임 측정 기능을 개발하고 팔벌림 각도 정확도 오차범위 ±5도 이내로 개선
- Android OS 정책 변경에 맞춘 BLE 연동 SDK 수정과 AAR 재배포로 웨어러블 기기 연동 중단 이슈 해결

### 브리시드 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

사용자 맞춤 명상 경험을 지원하는 웰니스 서비스

**Overview**

| 항목 | 내용 |
| --- | --- |
| 역할 | Android 기능 개발, 결제·재생·보안 개선 |
| 주요 기술 | Kotlin, Google Play Billing, Flow, Hilt, Play Integrity API |

**Key Contributions**

- Google Play 인앱 결제 연동과 일회성 결제 플로우 구현
- 명상 음악 플레이어의 Activity-Service 통신을 Broadcast Receiver에서 Flow 기반 구조로 전환해 상태 동기화 복잡도 완화
- KISA 보안취약점 점검 항목을 반영하고 Play Integrity API 기반 앱 무결성 검증, 루팅·백그라운드 오버레이 방어 적용
- 전역 싱글톤에 의존하던 플레이어·결제 객체를 Hilt 기반 의존성 주입으로 전환

### 마이밸런스 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

직장인의 건강한 습관 형성을 지원하는 건강관리·리워드 서비스

**Overview**

| 항목 | 내용 |
| --- | --- |
| 역할 | Android 기능 개발, 건강 데이터 연동, 배포 환경 개선 |
| 주요 기술 | Kotlin, Health Connect, Bamboo CI/CD |

**Key Contributions**

- Health Connect 연동으로 걸음 수·소모 칼로리·평균 심박수·수면시간 데이터 수집 경로 통합
- Bamboo 기반 CI/CD 배포 환경 구축으로 수동 빌드 과정의 빌드 넘버 충돌 제거
- 클래스 사진 업로드 로직을 갤러리 저장 방식에서 임시 파일 생성/제거 방식으로 전환해 디바이스 리소스 사용 개선

## Team Projects

### Reed(리드) - 문장과 감정을 함께 담는 독서 기록 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2025.05 ~ 2026.04</span>

독서 중 만난 문장과 감정을 함께 기록하고 공유하는 서비스

**Overview**

| 항목 | 내용 |
| --- | --- |
| 역할 | Android 파트 리드, 앱 개발·출시·운영·리팩토링 |
| 주요 기술 | Kotlin, Jetpack Compose, Circuit(MVI), Google 권장 아키텍처, Retrofit, OkHttp, Kotlinx Serialization, DataStore, Hilt, Firebase |
| 성과 | YAPP 26기 최우수상 |

**Key Contributions**

- Google 권장 아키텍처와 Circuit(MVI) 기반 프로젝트 구조 및 상태 관리 방식 설계
- Version Catalog와 Gradle Convention Plugin 기반 멀티 모듈 구조 최적화
- 커스텀 Pagination 기반 도서 검색·상세 조회 화면 구현
- DataStore 기반 최근 검색어, 온보딩, 자동 로그인 기능 구현
- Circuit Navigation 기반 Type-safe 네비게이션 시스템 구현으로 복잡한 객체 전달과 시작 화면 동적 변경 지원
- 로그인 없이 앱을 먼저 체험할 수 있는 Guest Mode 구현
- 도서 기록 카드 저장·공유 기능과 Firebase Remote Config 기반 앱 버전 관리 시스템 구현
- GitHub Actions, GitHub Secret, Firebase App Distribution 기반 CI/CD 파이프라인 구축
- ktlint, detekt 기반 정적 코드 분석 자동화와 Debug/Release 환경 분리

**Impact**

- Google Drive APK 수동 배포 흐름을 Firebase App Distribution 링크 기반 QA 프로세스로 전환
- OCR 지원과 도서 기록 템플릿 제공으로 사용자가 수기로 입력해야 하는 부분을 줄여 기록 피로도 완화
- 팀원에게 Circuit 도입 필요성과 장점을 설명하며 Android 구조 설계와 기술 선택을 리딩

### 유니페스 : 대학 축제의 지도를 펼쳐라! <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.03 ~ 2025.10</span>

대학 축제 통합 플랫폼으로 지도 기반 행사 정보, 부스 웨이팅, QR 인증 이벤트, 알림 기능을 제공하는 서비스

**Overview**

| 항목 | 내용 |
| --- | --- |
| 역할 | Android 개발, 출시·운영·리팩토링 |
| 주요 기술 | Kotlin, Jetpack Compose, Naver Map Compose, MVI, Retrofit, Room, DataStore, Hilt, Firebase Remote Config |
| 링크 | [Play Store](https://play.google.com/store/apps/details?id=com.unifest.android) |
| 성과 | 고려대·가천대·상명대·한국교통대 축제 공식 앱 선정, Play Store 다운로드 2,000+, Android/iOS 통합 WAU 5,000+ |

**Key Contributions**

- Naver Map Compose 기반 지도 화면 구현, 위치 권한·커스텀 마커·클러스터링 적용
- 구글 권장 아키텍처와 MVI 패턴 기반 모듈 구조 설계
- QR 기반 부스 행사 참여 인증 기능 구현
- Room과 DataStore를 활용한 관심 축제, 관심 부스, 사용자 설정 관리
- Type Safe Compose Navigation 적용으로 화면 전환과 데이터 전달 안정성 확보
- Firebase Remote Config 기반 강제 업데이트와 API 커스텀 에러 처리 적용
- GitHub Actions와 Firebase App Distribution 기반 CD 파이프라인 구축
- Room Migration Test 도입으로 데이터베이스 스키마 변경 안정성 확보

**Impact**

- Naver Map Compose 클러스터링 적용으로 축제 지도 내 부스·행사 정보 가독성 개선
- 대학 총학생회와 협업해 실제 축제 운영 환경에서 공식 앱으로 사용
- 테스터 QA 배포 흐름을 자동화해 앱 설치와 검증 과정을 단순화

### 트립메이트 - 강원도 여행 정보 및 동행 찾기 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.06 ~ 2024.11</span>

강원도 여행 동행 플랫폼으로 현위치 기반 여행지 탐색, 개인 여행 스타일 분석, 동행 매칭을 제공하는 서비스

**Overview**

| 항목 | 내용 |
| --- | --- |
| 역할 | Android 앱 개발 및 출시 |
| 주요 기술 | Kotlin, Jetpack Compose, Clean Architecture, MVI, Kakao Map, Kakao Auth, Room, Flow, Hilt |
| 링크 | [Play Store](https://play.google.com/store/apps/details?id=com.tripmate.android), [GitHub](https://github.com/TeamTripmate/tripmate-android) |
| 성과 | 한국관광공사 X 카카오 2024 관광데이터 활용 공모전 장려상 및 강원관광재단 특별상 |

**Key Contributions**

- 카카오 소셜 로그인과 사용자 인증 구현
- 여행 스타일 온보딩 설문 조사, 여행 목록 필터링, 마이페이지 기능 구현
- Composable 기반 화면을 Bitmap으로 변환해 여행 스타일 이미지 공유 기능 구현
- Room 기반 관심 여행지 로컬 데이터베이스 구축
- Flow combine을 활용해 Remote/Local 좋아요 상태를 실시간 동기화
- ViewModel 스코프 내 인메모리 캐싱 전략을 적용해 카테고리 변경 시 불필요한 API 호출 감소

**Impact**

- 여행 카테고리 변경 시 인메모리 캐싱 전략으로 API 호출을 줄이고 화면 반응성 개선
- Compose 렌더링 메커니즘과 Canvas 처리에 대한 실무 경험 확보

### 반다라트 - 부담 없는 만다라트 계획표 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2023.07 ~</span>

기존 9x9 만다라트 계획표를 모바일 환경에 맞게 5x5 구조로 줄인 목표 관리 앱

**Overview**

| 항목 | 내용 |
| --- | --- |
| 역할 | Android 개발, 출시·운영·리팩토링, Compose Multiplatform 마이그레이션 |
| 주요 기술 | Kotlin, Jetpack Compose, Compose Multiplatform, Circuit(MVI), Room, DataStore, Hilt, GitHub Actions |
| 링크 | [Play Store](https://play.google.com/store/apps/details?id=com.nexters.bandalart.android), [GitHub](https://github.com/Nexters/BandalArt-Android) |
| 성과 | Play Store 다운로드 1,000+ |

**Key Contributions**

- Jetpack Compose 기반 반다라트 계획표 Custom UI 구현과 공통 컴포넌트 정의
- Clean Architecture와 MVVM 구조를 MVI 기반 구조로 전환하고 Circuit 도입
- now in android 기반 feature 모듈 구조와 Gradle Convention Plugin 적용
- 반다라트 계획표 CRUD, 게스트 로그인, 온보딩, 목표 달성 화면 구현
- 서버 API 의존 구조를 Room 로컬 저장소 기반 offline-first 구조로 전환해 서버 중단 이후에도 서비스 유지
- Android 앱을 Compose Multiplatform으로 마이그레이션해 iOS 앱까지 배포
- Google Play In-App Update API 적용으로 업데이트 유도 흐름 제공
- Room Database, Repository, ViewModel 테스트 코드와 GitHub Actions CI 도입

**Impact**

- Circuit 도입으로 상태 관리와 이벤트 처리 복잡도 감소
- 사용자 피드백 기반 사용성·성능 개선을 지속하며 운영 경험 확보
- 태블릿·가로 모드 대응을 통해 다양한 화면 환경에서 사용성 개선

### I'Lab - 나만의 AI 프로필 연구소 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.01 ~ 2024.04</span>

생성형 AI 기반으로 취향에 맞는 프로필 사진을 만들고 공유할 수 있는 카메라 앱

**Overview**

| 항목 | 내용 |
| --- | --- |
| 역할 | Android 앱 개발 및 출시 |
| 주요 기술 | Kotlin, Jetpack Compose, Clean Architecture, MVI, Orbit, Kakao Auth, Retrofit, Hilt, Firebase |
| 링크 | [Play Store](https://play.google.com/store/apps/details?id=com.nexters.ilab.android), [GitHub](https://github.com/Nexters/ilab-android) |

**Key Contributions**

- Clean Architecture와 MVI 패턴 기반 프로젝트 구조 설계
- Orbit 기반 단방향 데이터 흐름과 UI 상태 관리 구조 구현
- Version Catalog와 Gradle Convention Plugin 기반 멀티 모듈 구조 최적화
- 카카오 소셜 로그인, 카메라·앨범 기반 사진 업로드, 스타일 선택, AI 이미지 생성 및 공유 기능 구현
- Kotlin Result와 runCatching 기반 네트워크 에러 처리 표준화
- GitHub Actions, ktlint, detekt 기반 CI와 정적 코드 분석 자동화

**Impact**

- Orbit 도입으로 상태 관리 효율성과 이벤트 처리 예측 가능성 향상
- Gradle Convention Plugin 적용으로 모듈 간 빌드 설정 중복 제거
- MaterialTheme 기반 다크모드 지원과 복구 가능한 에러 UI로 앱 안정성 보완

### ImagePicker <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2023.12 ~ 2024.01</span>

Compose Multiplatform 기반 갤러리 사진 피커 앱

**Overview**

| 항목 | 내용 |
| --- | --- |
| 역할 | Android/iOS 이미지 선택 흐름 구현 |
| 주요 기술 | Kotlin, Compose Multiplatform, expect/actual, PHPicker, Coil3, Decompose |
| 링크 | [GitHub](https://github.com/KwonDae/ImagePicker) |

**Key Contributions**

- expect/actual 패턴을 통해 iOS 환경의 PHPicker를 호출하고 갤러리 사진 선택 기능 구현
- Coil3로 Android/iOS 플랫폼의 이미지 타입(Network Uri, ByteArray)을 통합 처리
- Decompose 기반 메인·상세 화면 상태 관리와 화면 전환 로직 통합

## Other Projects

| 프로젝트 | 기간 | 설명 | 주요 기여 |
| --- | --- | --- | --- |
| 이끔 | 2023.07 ~ 2024.04 | 카페에서 공부하는 사용자를 위한 맞춤 카페 탐색 앱 | 페이징 API 결과를 Naver Map에 마킹, Flow flatMapLatest 기반 최신 검색 결과 처리, 검색어 디바운스, Navigator 모듈 도입 |
| 나나공 | 2021.09 ~ 2023.04 | 인강 수강 독려 서비스 앱 | MVVM·Hilt 도입, LiveData를 Flow로 전환, Navigation 기반 Single Activity 구조 전환, FCM 기반 주기적 알림 |
| GalleryApp | - | 갤러리 앱 | 이미지 목록과 상세 화면 구성, 로컬 미디어 접근 경험 확보 |
| MyVoca | - | 영어 단어 학습 앱 | 단어장 CRUD와 학습 흐름 구현 |
| PsyChat | - | 정신 건강 케어 앱 서비스 | 상담·채팅형 기능 구현 경험 |
| 도서 검색 앱 | - | 도서 검색 기능 중심 앱 | 검색 API 연동과 목록·상세 UI 구성 |
| 카카오 미디어 검색 앱 | - | 카카오 미디어 검색 API 기반 앱 | 외부 API 연동과 검색 결과 UI 구성 |
| Buddy Call | - | 커뮤니케이션 앱 | 앱 화면 구조와 기본 기능 구현 |
| Traveler | - | 여행 일정 관리 앱 | 여행 일정 생성·관리 기능 구현 |

## Libraries

- [Dari](https://github.com/easyhooon/dari): WebView JavaScript bridge 메시지의 요청·응답·상태를 실시간으로 확인하는 Android 디버깅 라이브러리. 프론트엔드 개발자도 브릿지 호출 흐름과 실패 지점을 확인할 수 있어 웹뷰 연동 이슈 디버깅에 기여. debug/release 분리를 위한 no-op 모듈 제공.
- [RoutePeek](https://github.com/easyhooon/routepeek): WebView의 현재 route와 SPA route 변경을 Compose overlay로 확인하는 Android debug 라이브러리. 웹뷰 화면의 현재 경로를 앱 안에서 바로 확인해 라우팅 이슈 재현과 공유를 쉽게 개선.

## Awards

**YAPP 26기 최우수상** <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2026.04</span><br>
Reed 프로젝트 Android 파트 리드로 구조 설계·기술 스택 검토·코드 리뷰 담당

**한국관광공사 X 카카오 2024 관광데이터 활용 공모전** <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.11</span><br>
트립메이트 앱 개발 및 출시, 장려상 및 강원관광재단 특별상 수상

## Source

- 기존 Notion 포트폴리오: <a href="https://app.notion.com/p/b13a4ca9bef54f52b2f0c01046359dfe">Portfolio</a>
- 최신 이력서: <a href="./RESUME.md">RESUME.md</a>
