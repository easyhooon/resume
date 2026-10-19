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

Android를 기반으로 사용자 흐름이 끊기는 지점을 찾고, 웹뷰 프론트엔드·서버 연결·배포와 검증 절차까지 해결 범위를 넓혀온 개발자입니다. 기능을 구현할 때 실패 후 복구 경로와 출시 후 확인 방법을 함께 설계합니다. AI 코딩 에이전트는 구현과 반복 검증에 활용하되, 완료 여부는 실제 동작·테스트·배포 기록으로 판단합니다.

**Android 앱 9개와 iOS 앱 1개**를 출시·운영했고, 직접 만든 오픈소스 [windowinsets.info](https://windowinsets.info/)와 [Dari](https://github.com/easyhooon/dari)가 각각 **Android Weekly [#747](https://androidweekly.net/issues/issue-747)·[#748](https://androidweekly.net/issues/issue-748)**에 소개되었습니다.

## Work Experience

**메디플러스솔루션 (HD현대 계열사)** · Android Developer · 2024.05 ~ 재직 중

헬스케어 앱 개발을 맡아 사용자 흐름 복구, 웹뷰 프론트엔드, 배포·테스트 운영으로 업무를 확장

- **끊긴 사진 업로드 복구**
  - 사진 업로드 실패를 단순 네트워크 오류로 처리하지 않고 Crashlytics와 재현 기록으로 WebView Renderer 종료를 확인
  - 앱 전체를 재시작하는 대신 웹뷰를 재생성하고, 네이티브 대기 상태와 웹 요청 ID를 연결해 업로드를 이어가도록 구현
- **E2E 테스트와 배포 파이프라인으로 검증 경로 구축**
  - 웹뷰 프론트엔드: 건강 데이터 권한 안내를 AI 코딩 에이전트와 구현하고 디자인 시안과 대조. Android·iOS 설정 화면을 3개 모바일 뷰포트의 Playwright E2E로 검증해 30회 반복 실행 통과. OS 권한 화면은 테스트 범위에서 제외
  - 기획 흐름 회귀 검사: 앱 최초 실행부터 WebView 인증·홈 진입까지의 흐름을 Maestro E2E로 작성. Android 실기기에서 2회 연속 통과, 인증 값은 실행 환경에서 주입
  - 배포: Bitbucket에서 GitHub로 옮기며 기존 파이프라인을 쓸 수 없게 되자 GitHub Actions로 재구축. 빌드와 배포 권한을 분리하고 산출물 대조·배포 상태·성공 버전 기록을 남겨 어떤 변경이 배포됐는지 확인할 수 있게 함
- **Crashlytics 알림을 GitHub 이슈로 자동 등록**
  - Crashlytics 알림을 서비스별로 정규화해 회사 GitHub 이슈를 등록·갱신하는 로직을 구현. 실제 알림 재처리에서 기존 이슈 재사용·중복 방지를 확인
  - 원인 분석→앱 수정→검증→Draft PR 경로는 합성 입력과 mock 게시까지 검증했으며 실제 앱 수정·PR 게시 연결은 진행 중

### Hi-me <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2025.10 ~</span>

HD현대 그룹사 임직원 대상 건강관리 서비스 · [Google Play](https://play.google.com/store/apps/details?id=com.mediplussolution.hime) 다운로드 **2,000+**

- **백그라운드 음악 재생**
  - 웹뷰 단독으로는 잠금 화면·알림 재생 제어가 어려워 UI는 웹에 유지하고 재생은 네이티브로 분리
  - 브릿지로 재생 상태·위치를 양방향 동기화해 앱 복귀 뒤에도 제어 흐름이 이어지도록 구현
- **공동 장애 확인**: 웹·네이티브 개발자가 브릿지 실패 지점을 함께 확인할 수 있도록 [Dari](https://github.com/easyhooon/dari)에 요청·응답 로그를 모으고 실제 서비스 개발 환경에 적용

### 세컨드 윈드/닥터 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

만성질환자와 암 수술 환자를 위한 건강관리·재활 서비스 · 현재 5종 운영 · 전체 출시 앱 Google Play 누적 다운로드 합산 **13,000+**

- **테스트 없는 Java 6.4만 줄 → Kotlin 전환 주도** (2026.10 완료 예정, Kotlin 비율 14% → 76%)
  - 원본 동작을 테스트로 고정해 전환 전후를 비교하는 A-A 검증과 뮤테이션 테스트로 모든 전환을 확인하며 단위 테스트 0개 → 1,580개 작성
  - 1만 줄이 넘던 God class 2개(`MainActivity`, API 호출 클래스 `ControlCommand`)를 책임별 Kotlin 클래스와 정의 표 기반 실행기로 분리
  - 전환 중 찾은 기존 버그는 이슈로 따로 관리하고, BLE 기기 이름이 웹뷰에서 JS로 실행되는 보안 취약점은 먼저 수정
- **로그인 후 첫 데이터 로딩 60.6% 단축** (2.835초 → 1.116초)
  - 로그인 뒤 대시보드가 늦게 준비되는 원인을 전역 세마포어의 네트워크 직렬 처리로 특정하고 Health Connect 작업을 유형별로 병렬화
- **R8 적용으로 DEX 78.5% 경량화, 크래시 회귀 CI 추가**
  - 9개 flavor 앱의 R8·리소스 축소로 DEX를 36.7 MB → 7.9 MB로 경량화해 배포
  - 난독화로 생긴 앱 시작 크래시를 CI 회귀 검증에 추가해 재발 방지

## Side Projects · Frontend & Client–Server

### WindowInsets.Info - 기기별 화면 영역 측정·시각화 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2026.09 ~</span>

[서비스](https://windowinsets.info) · [GitHub](https://github.com/easyhooon/windowinsets.info) · [개발 기록](https://velog.io/@mraz3068/windowinsets-rtl-automation)

- **측정 출처를 구분한 화면 영역 데이터**: 개발자가 화면 영역 값을 믿고 쓸 수 있도록 실기기·RTL·Emulator 출처를 구분하고 잘못된 캡처는 제외, 미확인 값은 미측정으로 표시
- **초기 JS 약 59% 감소** (Galaxy S25 Ultra 페이지 351.0 kB → 143.3 kB)
  - 전체 기기 데이터를 초기 번들에서 분리하고 Three.js·코드 블록을 지연 로딩
  - 측정 기준은 prerender HTML 참조 JS의 gzip 합계
- **3D 청크 조건부 prefetch**: 폴더블 링크의 hover·focus·touch에서만 3D 청크를 prefetch. production 빌드에서 클릭 전 도착·마운트 시 재요청 없음 확인. 일반 기기·Save-Data 연결은 제외

### Chat Sync Lab - 응답 유실에도 중복 전송을 막는 채팅 실험

[GitHub](https://github.com/easyhooon/chat-sync-lab) · 배포 서비스가 아닌 개인 학습 프로젝트

- **응답 유실 시 중복 전송 방지**
  - HTTP 수락 응답과 WebSocket 알림이 모두 유실될 때 사용자에게 전송 성공을 섣불리 표시하지 않도록 Room outbox에 `UNKNOWN`을 보존
  - 같은 ID로 수동 재시도해 서버 수락 기록을 중복 생성하지 않도록 설계
- **서버·앱 동기화 경로 연결**: 서버의 중복 키·cursor 과거 조회와 앱의 Room 캐시·Paging·전경 복귀 후 누락 보충을 연결. 로컬 AVD에서 수락 응답 유실, 프로세스 재시작, 과거 조회 중 실시간 메시지, 배경 복귀를 검증
- **검증 범위**: 서버는 메모리 저장·로컬 테스트 신원만 사용. 실제 Firebase 테스트 프로젝트의 단일 배경 메시지 수신은 확인했으나 운영 인증·영속 서버·배포는 구현하지 않음

### Stream Playback Lab - 재생 실패와 라이브 복귀를 확인하는 영상 실험

[GitHub](https://github.com/easyhooon/stream-playback-lab) · 배포 서비스가 아닌 개인 학습 프로젝트

- **장애 주입으로 재생 실패·복구 확인**: VOD 화질 선택·탐색과 일반 라이브 HLS의 이동 창을 구현하고, 서버에서 세그먼트 속도 제한·503·송출 중단을 주입해 앱의 오류 표시와 수동 Retry를 확인
- **재생 로그·서버 상태·화면 대조**: 전용 AVD에서 Auto 화질의 720p→360p→720p 전환, 503 뒤 재생, 라이브 Pause→Go live와 송출 재시작 뒤 복귀를 대조. 서버·앱 자동 검사 9개와 시나리오별 검증 기록 보유
- **검증 범위**: 서버는 loopback 전용이며 실제 단말·통신망·CDN 지연이나 운영 트래픽을 검증한 결과는 아님

## Side Projects · Team

### 반다라트 - 부담 없는 만다라트 계획표 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2023.07 ~</span>

<span style="font-size: 0.9em;">Android 개발자 2명, 배포까지 2개월, 현재 운영 중</span>

- **Compose Multiplatform으로 iOS 앱 배포, 공통 코드 약 73%**
  - 서버 중단 뒤에도 목표 조회·편집을 유지하도록 Room 로컬 저장으로 전환
  - 작은 화면의 탐색 부담을 줄이려 9x9 계획표를 5x5로 재구성

### 유니페스 : 대학축제의 지도를 펼쳐라! <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.03 ~ 2025.10</span>

<span style="font-size: 0.9em;">Android 개발자 2명, 배포까지 2개월</span> · 고려대·가천대·상명대·한국교통대 축제 공식 앱 선정, Play Store 다운로드 **2,000+**, 축제 운영 기간 Android/iOS 통합 최고 **WAU 5,000+**

- **지도 마커 클러스터링**: 밀집된 부스·행사 마커가 겹쳐 보이는 문제를 Naver Map Compose 클러스터링으로 해결해, 줌 레벨에 따라 마커를 묶고 펼쳐 표시
- **축제 기간 운영 대응**
  - QR 현장 인증으로 부스 참여를 앱 안에서 처리
  - Remote Config로 지원 버전을 원격 제어해 구버전 사용자를 업데이트로 유도
  - Room Migration Test로 업데이트 후 기존 데이터 유지를 배포 전 검증

## Other Experience

- 메디플러스솔루션 [브리시드 심리상담센터](https://play.google.com/store/apps/details?id=com.mediplussolution.mentalcounsel) 앱(React Native): 미사용 SDK 등 18개 의존성 제거·pnpm 전환으로 iOS 시뮬레이터 Debug 빌드 **238.7초 → 195.8초(18.0% 단축)**, 동일 Mac·빈 DerivedData에서 각 3회 측정 중앙값
- YAPP 26기: Reed Android 파트 리드로 구조 설계·코드 리뷰와 OCR 입력 흐름 구현, 최우수상 수상

## Awards

**한국관광공사 X 카카오 2024 관광데이터 활용 공모전** <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.11</span><br>
트립메이트 앱 개발 및 출시, **장려상 및 강원관광재단 특별상 수상**

## Certificates

정보처리기사 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2022.09</span>

## Education

건국대학교 컴퓨터 공학부 학사 졸업 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.02</span>
