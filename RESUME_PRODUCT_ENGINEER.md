# 이지훈 Product Engineer

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

Android 제품의 화면 상태, 비동기 처리, 성능과 오류 복구를 개선해온 개발자입니다. 웹뷰 제품에서는 웹·네이티브의 역할을 설계하고 프론트엔드까지 함께 개발했습니다. AI 코딩 에이전트로 구현 범위를 넓히며 검증과 리뷰 반영 절차를 구성해왔습니다.

**Android 앱 9개와 iOS 앱 1개**를 출시·운영하며 입력 부담, 서비스 중단과 플랫폼 확장 문제를 해결해왔습니다. 기술 선택과 운영 중 배운 점을 개발 블로그와 팀 내 공유로 정리해왔습니다.

## Work Experience

**메디플러스솔루션 (HD현대 계열사)** · Android Developer · 2024.05 ~ 재직 중

신규 헬스케어 서비스 Hi-me의 Android 개발과 기존 건강관리·재활·명상 앱의 유지보수 및 기능 고도화 담당. Android를 기반으로 회사 서비스의 프론트엔드 개발, 검증과 배포 절차 개선까지 수행

- **프론트엔드 업무 확장**: AI 코딩 에이전트를 활용해 회사 서비스의 프론트엔드 업무를 함께 수행하고, 웹·네이티브 양쪽의 상태와 오류 처리 흐름 구현
- **AI 개발 절차 표준화**: 작업 분석, 구현 후 검증, 커밋·PR 생성, 코드 리뷰 반영 절차를 에이전트용 스킬과 체크리스트로 정의해 반복 작업에 같은 검증 기준 적용
- **CI/CD 재설계**: 담당 서비스의 빌드·테스트·배포 절차를 재설계하고, GitHub Actions 기반 Hi-me 내부 테스트 배포와 Bamboo 기반 마이밸런스 빌드 넘버 관리를 자동화
- **E2E 테스트 도입**: 회사 서비스에 E2E 테스트를 도입해 사용자 흐름의 동작을 확인하는 검증 절차 추가

## Projects

### Hi-me <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2025.10 ~</span>

HD현대 그룹사 임직원 대상 건강관리 헬스케어 서비스 · [Google Play](https://play.google.com/store/apps/details?id=com.mediplussolution.hime) 다운로드 **2,000+**

- **사용자 작업 복구**: 사진 업로드 중단을 Crashlytics Non-Fatal로 추적해 WebView Renderer 종료가 원인임을 확인. 네이티브 pending state와 웹 request id·TTL 저장을 연결해 WebView 복원 후 사진 요청을 재전달하고 업로드를 완료하는 흐름 구현
- **웹·네이티브 역할 설계**: 일정과 하이브리드 구조를 고려해 웹은 음악 UI를, 네이티브는 백그라운드 재생을 담당하도록 분리. 양방향 브릿지로 상태·위치를 동기화해 잠금화면·알림 제어와 복귀 시 재생 위치 복원 제공
- **협업 도구 개발·운영**: 흩어진 브릿지 로그를 [Dari](https://github.com/easyhooon/dari)로 모아 Android·프론트엔드 개발자가 요청·응답과 실패 지점을 함께 확인하도록 구성. 실무 적용 후 로그 유실·다중 WebView 충돌을 저장 방식과 태그 구분으로 개선
- **건강 데이터 수집 안정화**: BLE 혈당계·혈압계의 기기별 동작 차이에 맞춰 측정값 확보 후 삭제, 마지막 동기화 시점 필터링과 로컬 캐싱을 적용해 누락·중복 위험 완화. 걸음 수 갱신 문제에는 Samsung Health Data SDK 수집 경로 추가

### 세컨드 윈드/닥터 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

만성질환자와 암 수술 환자를 위한 맞춤 건강관리·재활 서비스 · 현재 5종 운영 · 전체 출시 앱 Google Play 누적 다운로드 합산 **13,000+**

- **대시보드 대기 개선**: 전역 세마포어의 네트워크 직렬 병목을 제거하고 Health Connect 데이터 처리를 유형별 병렬화해, 로그인 후 첫 대시보드 데이터 준비 시간을 **2.835초 → 1.116초(60.6% 단축)**, 최초 동기화 완료 시간을 **6.546초 → 4.740초**(27.6% 단축)로 개선
- **영상 재생 흐름 개선**: ExoPlayer2를 Media3로 전환하고 긴 영상의 전체 다운로드를 기다리던 구조를 구간 단위 다운로드로 변경해 첫 구간부터 재생하도록 구성
- **재활 측정 기능**: TensorFlow Lite·CameraX 기반 어깨 움직임 측정 기능 개발, 팔벌림 각도 정확도를 **오차범위 ±5도 이내**로 개선
- **경량화와 회귀 대응**: 9개 flavor 앱에 R8·리소스 축소를 적용해 DEX **36.7 MB → 7.9 MB(78.5% 감소)**. Crashlytics의 앱 시작 크래시 19건을 Joda-Time 리플렉션 리소스 제거로 특정하고 최소 keep rule·CI 회귀 검증으로 해결

### 브리시드 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

사용자 맞춤 명상 경험을 지원하는 웰니스 서비스 · [Google Play](https://play.google.com/store/apps/details?id=com.mediplussolution.android.breeseed) 다운로드 **500+**

- **화면·재생 상태 통합**: XML 플레이어 UI를 Jetpack Compose로 전환하고 Activity-Service 통신을 Broadcast Receiver에서 Flow로 재구성해 UI와 재생 상태의 생산·소비 경로 통합
- **재생 연속성 개선**: MediaPlayer를 Media3로 전환하고 인증 만료 시 플레이어를 재생성하던 방식을 인증 헤더 갱신·재시도로 변경해 재생 중단 가능성 완화
- **콘텐츠 구매·보안 대응**: Google Play 일회성 결제로 유료 콘텐츠 구매 경로 추가. KISA 점검 항목에 Play Integrity API와 런타임 탐지 적용

### 마이밸런스 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

직장인의 건강한 습관 형성을 지원하는 건강관리·리워드 서비스 · [Google Play](https://play.google.com/store/apps/details?id=com.kyobo.mybalance) 다운로드 **1,000+**

- Health Connect로 걸음 수·소모 칼로리·심박수·수면시간 수집 경로 통합
- 사진 업로드용 파일을 갤러리 저장에서 임시 파일 생성·업로드 후 제거로 변경해 사용자 기기에 불필요한 미디어 파일이 남는 문제 해결

## Frontend Project

### WindowInsets.Info - Android 기기별 화면 영역 측정·시각화 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2026.09 ~</span>

**Android 측정 앱·데이터 검증·웹 시각화 개발** · [서비스](https://windowinsets.info) · [GitHub](https://github.com/easyhooon/windowinsets.info) · [개발 기록](https://velog.io/@mraz3068/windowinsets-rtl-automation)

- **웹 시각화·출처 표시**: Galaxy·Pixel의 화면 영역을 디바이스 프리뷰와 수치로 제공. 실기기·RTL·Emulator 출처를 구분하고 잘못된 캡처는 제외, 미확인 값은 미측정으로 표시
- **초기 전송량 개선**: 전체 기기 데이터의 클라이언트 번들 포함을 제거하고 Three.js·코드 블록을 지연 로딩해 Galaxy S25 Ultra 페이지의 초기 JS를 **351.0 kB → 143.3 kB(약 59% 감소)** — prerender HTML 참조 JS의 gzip 합계 비교
- **진입 전 로딩**: 폴더블 링크의 hover·focus·touch에서 3D 청크를 prefetch하고 지연 로딩과 같은 요청을 공유. production 빌드에서 클릭 전 도착·마운트 시 재요청 없음 확인, 일반 기기·Save-Data 연결은 제외
- **수집 자동화**: RTL 수동 다운로드를 Probe → 업로드 API → GitHub PR로 전환하고 Fold8·Flip8 원본 JSON 도착까지 확인
- **외부 소개**: [Android Weekly #747](https://androidweekly.net/issues/issue-747) Libraries & Code 섹션에 Android Window Insets & Safe Areas로 소개 (2026.10.04)

## Team Projects

### 유니페스 : 대학축제의 지도를 펼쳐라! <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.03 ~ 2025.10</span>

<span style="font-size: 0.9em;">Android 개발자 2명, 배포까지 2개월, 현재 운영 중</span> · 4개 대학 축제 공식 앱 선정 · 축제 운영 기간 Android/iOS 통합 최고 **WAU 5,000+**

- 밀집된 부스·행사 마커에 지도 클러스터링을 적용하고 QR 스캔을 부스 참여 상태와 연결해 탐색·현장 인증 흐름 구현
- 입력 조건을 충족해도 웨이팅 신청 버튼이 활성화되지 않는 문제를 상태 관찰 누락으로 특정하고 검증 로직 수정
- Remote Config로 지원 버전 기준을 원격 관리하고, Room Migration Test로 업데이트 후 기존 사용자 데이터 유지 검증

### 반다라트 - 부담 없는 만다라트 계획표 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2023.07 ~</span>

<span style="font-size: 0.9em;">Android 개발자 2명, 배포까지 2개월, 현재 운영 중</span>

- 작은 화면의 탐색 부담을 줄이기 위해 9x9 계획표를 5x5로 재구성하고 Compose Custom UI로 조작 방식 통일
- 서버 중단 후에도 목표 조회·편집을 유지하도록 Room 로컬 저장 중심으로 전환. 기존 Android 코드를 Compose Multiplatform으로 확장해 iOS 앱까지 배포
- 상태 생성·이벤트 처리를 Circuit Presenter로 분리하고 Room·Repository·ViewModel 테스트를 GitHub Actions에서 실행해 회귀 검증 자동화

## Other Experience

- 브리시드 심리상담센터: React Native 앱의 미사용 SDK 등 18개 의존성 제거·pnpm 전환으로 iOS 시뮬레이터 Debug 빌드 **238.7초 → 195.8초(18.0% 단축)** — 동일 Mac·빈 DerivedData에서 각 3회 측정 중앙값
- YAPP 26기: Reed Android 파트 리드로 구조 설계·기술 스택 검토·코드 리뷰 담당. OCR 입력과 로그인 전 탐색 경로 구현, 최우수상 수상
- Nexters 23·24·26기: 반다라트, I'lab, Ziine Android 구조 설계·기술 스택 선정·코드 리뷰와 출시 후 리팩터링 담당

## Awards

**한국관광공사 X 카카오 2024 관광데이터 활용 공모전** <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.11</span><br>
트립메이트 앱 개발 및 출시, **장려상 및 강원관광재단 특별상 수상**

## Certificates

정보처리기사 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2022.09</span>

## Education

건국대학교 컴퓨터 공학부 학사 졸업 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.02</span>
