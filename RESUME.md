# 이지훈 Android Developer

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
    <td><strong>Portfolio</strong> <a href="https://github.com/easyhooon/resume/blob/main/PORTFOLIO.md">PORTFOLIO.md</a></td>
    <td><strong>LinkedIn</strong> <a href="https://www.linkedin.com/in/easyhooon/">linkedin.com/in/easyhooon</a></td>
  </tr>
</table>

## Introduce

운영 중 재현하기 어려운 Android 문제의 원인을 끝까지 추적해 해결하고, 문제 재현부터 원인 분석, 수정 결과 확인까지 이어지는 도구와 절차를 구축해왔습니다.

사이드 프로젝트로 **Android 앱 9개와 iOS 앱 1개**를 출시·운영했고, 직접 만든 오픈소스 [windowinsets.info](https://windowinsets.info/)와 [Dari](https://github.com/easyhooon/dari)가 각각 **Android Weekly [#747](https://androidweekly.net/issues/issue-747)·[#748](https://androidweekly.net/issues/issue-748)**에 소개되었습니다.

## Work Experience

**메디플러스솔루션 (HD현대 계열사)** · Android Developer · 2024.05 ~ 재직 중

2년 이상 Android 개발자로 근무하며, 신규 헬스케어 서비스 Hi-me 개발을 중심으로 기존 건강관리·재활·명상 앱의 유지보수와 기능 고도화를 병행했습니다.

### Hi-me <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2025.10 ~</span>

HD현대 그룹사 임직원 대상 건강관리 헬스케어 서비스 · [Google Play](https://play.google.com/store/apps/details?id=com.mediplussolution.hime) 다운로드 **2,000+**

- **웹뷰 브릿지 규격 표준화와 [Dari](https://github.com/easyhooon/dari) 기반 디버깅 환경 구축**
  - 웹뷰-네이티브 요청/응답 규격과 에러 처리 기준 표준화
  - Android·프론트엔드 개발자가 브릿지 호출 흐름과 실패 지점을 같은 화면에서 확인하도록 구성
- **BLE 의료기기·헬스 데이터 수집**
  - BLE Glucose/Blood Pressure Profile 기반 혈당계·혈압계 연동, 측정 데이터 동기화와 연동 해제까지 제공
  - Health Connect 경유 시 걸음 수가 갱신되지 않는 경우를 위해 Samsung Health Data SDK 수집 경로 추가
- **웹뷰 오디오의 백그라운드 재생 지원**
  - 웹뷰 오디오 플레이어(video.js)의 재생 위치·재생/일시정지 상태를 네이티브 Media3 ExoPlayer·MediaSession과 동기화
  - 앱을 나가거나 화면을 꺼도 재생이 끊기지 않고, 잠금화면·알림에서 제어하며 앱 복귀 시 같은 위치에서 이어 재생

### 세컨드 윈드/닥터 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

만성질환자와 암 수술 환자를 위한 맞춤 건강관리·재활 서비스 · [세컨드 윈드](https://play.google.com/store/apps/details?id=com.mediplussolution.android.csmsrenewal.secondwindforpatentkr)와 유방암·전립선암·대장암·위암 대상 [세컨드 닥터](https://play.google.com/store/apps/details?id=com.mediplussolution.android.csmsrenewal.breastcancer) 4종으로 현재 총 5종 운영 · 전체 출시 앱 Google Play 누적 다운로드 합산 **13,000+**

- **레거시 Java 6.9만 줄의 97% Kotlin 전환 주도** (Kotlin 비율 12% → 97%)
  - 원본 동작을 테스트로 고정해 전환 전후를 비교하는 A-A 검증과 뮤테이션 테스트로 모든 전환을 확인하며 단위 테스트 0개 → 1,700개 이상 작성
  - 1만 줄이 넘던 God class 2개(`MainActivity`, API 호출 클래스 `ControlCommand`)를 책임별 Kotlin 클래스와 정의 표 기반 실행기로 분리
  - 전환 중 찾은 기존 버그는 이슈로 따로 관리하고, BLE 기기 이름이 웹뷰에서 JS로 실행되는 보안 취약점은 먼저 수정
- **로그인 후 첫 데이터 로딩 60.6% 단축** (2.835초 → 1.116초)
  - 전역 세마포어 기반 네트워크 직렬 병목을 제거하고 Health Connect 데이터 처리를 유형별 병렬화
  - 최초 동기화 완료 시간도 6.546초 → 4.740초(27.6% 단축)
- **R8 적용으로 DEX 78.5% 경량화, 크래시 회귀 CI 추가**
  - 9개 flavor 레거시 앱의 Release 빌드에 R8·리소스 축소를 적용해 DEX 36.7 MB → 7.9 MB로 줄여 배포
  - 난독화로 생긴 앱 시작 크래시를 CI 회귀 검증에 추가해 재발 방지
- **재활 운동 영상·측정 기능**
  - ExoPlayer2 기반 운동 영상 플레이어를 Media3로 마이그레이션하고 긴 영상을 구간 단위로 내려받아, 전체 다운로드 전에도 첫 구간부터 재생
  - TensorFlow Lite + CameraX 기반 어깨 움직임 측정 기능 개발, 팔벌림 각도 정확도 오차범위 ±5도 이내로 개선

### 브리시드 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

사용자 맞춤 명상 경험을 지원하는 웰니스 서비스 · [Google Play](https://play.google.com/store/apps/details?id=com.mediplussolution.android.breeseed) 다운로드 **500+**

- **Google Play 인앱 결제 연동**: 일회성 결제 플로우를 구현해 유료 콘텐츠 구매 경로 추가
- **명상 플레이어 Compose·Media3 전환**
  - XML 기반 UI를 Jetpack Compose로 전환하고, Activity-Service 통신을 Broadcast Receiver에서 Flow 기반 스트림으로 재구성
  - 인증 토큰 만료 시 플레이어 객체를 재생성하던 복구 방식을 인증 헤더 갱신·재시도 구조로 바꿔 재생 중단 가능성을 낮춤
- **KISA 보안취약점 대응**: 지적된 앱 위변조·루팅·백그라운드 오버레이 항목에 Play Integrity API와 런타임 탐지 로직 적용

### 마이밸런스 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

직장인의 건강한 습관 형성을 지원하는 건강관리·리워드 서비스 · [Google Play](https://play.google.com/store/apps/details?id=com.kyobo.mybalance) 다운로드 **1,000+**

- **Health Connect 연동**: 걸음 수·소모 칼로리·평균 심박수·수면시간 데이터 수집 경로 통합
- **CI/CD GitHub Actions 전환**: Bamboo 기반 레거시 CI/CD를 옮겨 빌드 넘버 관리를 자동화하고 충돌 문제 해결
- **업로드 후 기기에 남던 챌린지 사진 제거**: 갤러리 저장 방식에서 임시 파일 생성·업로드 후 제거하는 방식으로 전환

<span style="font-size: 0.9em; color: #6b7280;">각 프로젝트의 문제 해결 과정은 [포트폴리오](https://github.com/easyhooon/resume/blob/main/PORTFOLIO.md)의 Company Troubleshooting에 정리했습니다.</span>

## Side Projects

### 반다라트 - 부담 없는 만다라트 계획표 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2023.07 ~</span>

<span style="font-size: 0.9em;">Android 개발자 2명, 배포까지 2개월, 현재 운영 중</span>

- **Compose Multiplatform으로 iOS 앱 출시, 공통 코드 73%**
  - Android 앱을 Compose Multiplatform으로 마이그레이션해 iOS 개발자 없이 Android 개발자 2명이 iOS 앱까지 출시(2025.03)
  - 앱 코드의 약 73%(20,189줄)를 Android·iOS 공통 코드로 유지해 기능 추가·수정을 한 번에 양쪽에 반영
- **서버 중단 이후에도 서비스 유지**: 서버 API 의존 구조를 로컬 Room Database 기반으로 전환
- **넓은 화면 레이아웃 대응**: 기기 종류 대신 화면 비율 기준으로 레이아웃을 나눠, Galaxy Z Fold·iPhone Duo·iPad에서는 목표 정보(제목·달성률·마감일)와 계획표를 좌우로 나란히 배치
- **Circuit 기반 상태 로직 분리**
  - Slack Circuit Presenter로 계획표 상태 생성과 이벤트 처리를 UI에서 분리해 상태 로직을 독립적으로 테스트할 수 있게 하고, UI 컴포저블은 렌더링과 이벤트 전달에만 집중하도록 구성

### 유니페스 : 대학축제의 지도를 펼쳐라! <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.03 ~ 2025.10</span>

<span style="font-size: 0.9em;">Android 개발자 2명, 배포까지 2개월</span> · 고려대·가천대·상명대·한국교통대 축제 공식 앱 선정, Play Store 다운로드 **2,000+**, 축제 운영 기간 Android/iOS 통합 최고 **WAU 5,000+**

- **지도 마커 클러스터링**: 밀집된 부스·행사 마커가 겹쳐 보이는 문제를 Naver Map Compose 클러스터링으로 해결해, 줌 레벨에 따라 마커를 묶고 펼쳐 표시
- **축제 기간 운영 대응**
  - QR 현장 인증으로 부스 참여를 앱 안에서 처리
  - Remote Config로 지원 버전을 원격 제어해 구버전 사용자를 업데이트로 유도
  - Room Migration Test로 업데이트 후 기존 데이터 유지를 배포 전 검증

## Open Source

- **[Dari](https://github.com/easyhooon/dari): [Android Weekly #748](https://androidweekly.net/issues/issue-748) 소개** (2026.10.11), 사내 앱 4종 적용
  - 웹뷰 브릿지 메시지는 Chrome inspector에 보이지 않아 IDE를 연결해야만 확인할 수 있던 문제를 해결하려고 직접 만든 라이브러리
  - Hi-me·세컨드 윈드·브리시드·마이밸런스에서 Logcat으로 요청·응답을 짝짓는 대신 기기·PC 화면에서 바로 확인하고, QA(STG) 빌드의 버그는 테스트 기기에 남은 로그를 프론트엔드 개발자에게 넘겨 웹·앱 중 어느 쪽 실패인지 함께 판단
  - adb로 연결해 PC에서 메시지를 보는 Desktop 앱을 macOS·Windows·Linux용으로 배포. ProGuard·아키텍처별 네이티브 라이브러리 정리와 LZFSE 압축 전환으로 macOS DMG를 70.7 MB → 45.4 MB(35.7% 감소, 2.5.2 기준)로 축소
- **[windowinsets.info](https://windowinsets.info/): [Android Weekly #747](https://androidweekly.net/issues/issue-747) 소개** (2026.10.04)
  - Galaxy·Pixel 기기별 WindowInsets·DisplayCutout을 측정해 디바이스 프리뷰와 수치로 확인하도록 지원
- [RoutePeek](https://github.com/easyhooon/routepeek): WebView의 현재 route와 SPA route 변경을 Compose overlay로 확인하는 Android 디버깅 라이브러리. 앱 안에서 경로를 확인해 라우팅 이슈 재현·공유 지원.

## Other Experience

- 메디플러스솔루션 [브리시드 심리상담센터](https://play.google.com/store/apps/details?id=com.mediplussolution.mentalcounsel) 앱(React Native): 미사용 SDK 등 18개 의존성 제거·pnpm 전환으로 iOS 시뮬레이터 Debug 빌드 **238.7초 → 195.8초(18.0% 단축)**, 동일 Mac·빈 DerivedData에서 각 3회 측정 중앙값
- YAPP 26기: Reed 프로젝트 Android 파트 리드로 구조 설계·기술 스택 검토·코드 리뷰 담당, Android Manifest Interview 도서/기술 블로그 작성 스터디 운영, 최우수상 수상, 27·28기 Android 개발자 선발 면접 참여
- Nexters 23·24·26기: 반다라트, I'lab, Ziine 프로젝트 Android 구조 설계·기술 스택 선정·코드 리뷰, 출시 후 리팩터링과 성능 병목 분석 담당

## Awards

**한국관광공사 X 카카오 2024 관광데이터 활용 공모전** <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.11</span><br>
트립메이트 앱 개발 및 출시, **장려상 및 강원관광재단 특별상 수상**

## Certificates

정보처리기사 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2022.09</span>

## Education

건국대학교 컴퓨터 공학부 학사 졸업 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.02</span>
