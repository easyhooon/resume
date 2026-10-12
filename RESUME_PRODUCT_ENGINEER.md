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

Android를 기반으로 사용자 흐름의 중단과 지연을 해결해온 개발자입니다. 웹뷰 제품의 프론트엔드 구현과 테스트, 배포까지 맡으며 제품을 출시한 뒤에도 동작을 확인할 수 있는 절차를 만들었습니다.

**Android 앱 9개와 iOS 앱 1개**를 출시·운영했습니다. AI 코딩 에이전트는 구현 범위를 넓히는 도구로 사용하고, 변경 사항은 테스트와 배포 결과로 확인합니다.

## Work Experience

**메디플러스솔루션 (HD현대 계열사)** · Android Developer · 2024.05 ~ 재직 중

헬스케어 앱의 Android 개발을 담당하며 웹뷰 프론트엔드와 제품 검증·배포 절차까지 업무를 확장

- **프론트엔드 구현·검증**: AI 코딩 에이전트를 활용해 건강 데이터 권한 안내를 구현하고 디자인 시안과 대조해 수정. Android·iOS 설정 화면을 3개 모바일 뷰포트의 Playwright E2E로 검증해 30회 반복 실행 통과
- **CI/CD 재설계**: Bitbucket에서 GitHub로 옮기며 기존 파이프라인을 쓸 수 없게 된 서비스에 GitHub Actions 배포 흐름 구축. 빌드와 배포 권한을 분리하고 산출물 대조·배포 상태·성공 버전 기록을 추가
- **사용자 흐름 E2E 도입**: 기획된 인증 흐름을 앱 최초 실행부터 WebView 로그인·홈 진입까지 Maestro로 작성. Android 실기기에서 2회 연속 통과하고 인증 값은 실행 환경에서 주입
- **AI·장애 대응 절차**: 에이전트의 작업·검증·배포 규칙을 공용 문서와 스킬로 정리. Crashlytics 알림의 서비스 식별·중복 방지·이슈 동기화 로직을 구현하고 실제 알림 재처리로 중복 등록 방지를 확인

## Projects

### Hi-me <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2025.10 ~</span>

HD현대 그룹사 임직원 대상 건강관리 헬스케어 서비스 · [Google Play](https://play.google.com/store/apps/details?id=com.mediplussolution.hime) 다운로드 **2,000+**

- **사용자 작업 복구**: 사진 업로드 중단을 Crashlytics로 추적해 WebView Renderer 종료를 확인. 네이티브의 대기 상태와 웹 요청 ID를 연결해 화면 복원 후 업로드 요청을 다시 전달
- **웹·네이티브 역할 설계**: 음악 UI는 웹, 백그라운드 재생은 네이티브가 맡도록 나누고 브릿지로 재생 상태·위치를 동기화. [Dari](https://github.com/easyhooon/dari)에 브릿지 요청·응답 로그를 모아 양쪽 개발자가 실패 지점을 함께 확인

### 세컨드 윈드/닥터 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

만성질환자와 암 수술 환자를 위한 맞춤 건강관리·재활 서비스 · 현재 5종 운영 · 전체 출시 앱 Google Play 누적 다운로드 합산 **13,000+**

- **대시보드 대기 개선**: 전역 세마포어의 네트워크 직렬 병목을 제거하고 Health Connect 처리를 유형별 병렬화. 로그인 후 첫 데이터 준비 시간 **2.835초 → 1.116초(60.6% 단축)**
- **경량화와 회귀 대응**: 9개 flavor 앱의 R8·리소스 축소로 DEX **36.7 MB → 7.9 MB**. 앱 시작 크래시 19건을 Joda-Time 리플렉션 문제로 특정하고 최소 keep rule·CI 검증으로 해결

## Frontend Project

### WindowInsets.Info - Android 기기별 화면 영역 측정·시각화 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2026.09 ~</span>

**Android 측정 앱·데이터 검증·웹 시각화 개발** · [서비스](https://windowinsets.info) · [GitHub](https://github.com/easyhooon/windowinsets.info) · [개발 기록](https://velog.io/@mraz3068/windowinsets-rtl-automation)

- **웹 시각화·출처 표시**: Galaxy·Pixel의 화면 영역을 디바이스 프리뷰와 수치로 제공. 실기기·RTL·Emulator 출처를 구분하고 잘못된 캡처는 제외, 미확인 값은 미측정으로 표시
- **초기 전송량 개선**: 전체 기기 데이터의 클라이언트 번들 포함을 제거하고 Three.js·코드 블록을 지연 로딩해 Galaxy S25 Ultra 페이지의 초기 JS를 **351.0 kB → 143.3 kB(약 59% 감소)** — prerender HTML 참조 JS의 gzip 합계 비교
- **진입 전 로딩**: 폴더블 링크의 hover·focus·touch에서 3D 청크를 prefetch하고 지연 로딩과 같은 요청을 공유. production 빌드에서 클릭 전 도착·마운트 시 재요청 없음 확인, 일반 기기·Save-Data 연결은 제외
- **수집 자동화**: RTL 수동 다운로드를 Probe → 업로드 API → GitHub PR로 전환하고 Fold8·Flip8 원본 JSON 도착까지 확인

## Team Projects

### 유니페스 : 대학축제의 지도를 펼쳐라! <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.03 ~ 2025.10</span>

<span style="font-size: 0.9em;">Android 개발자 2명, 배포까지 2개월, 현재 운영 중</span> · 4개 대학 축제 공식 앱 선정 · 축제 운영 기간 Android/iOS 통합 최고 **WAU 5,000+**

- 밀집된 부스·행사 마커에 지도 클러스터링을 적용하고 QR 스캔을 부스 참여 상태와 연결해 탐색·현장 인증 흐름 구현
- 웨이팅 신청 버튼이 활성화되지 않는 문제를 상태 관찰 누락으로 특정하고 수정

### 반다라트 - 부담 없는 만다라트 계획표 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2023.07 ~</span>

<span style="font-size: 0.9em;">Android 개발자 2명, 배포까지 2개월, 현재 운영 중</span>

- 작은 화면의 탐색 부담을 줄이기 위해 9x9 계획표를 5x5로 재구성하고 Compose UI로 조작 방식 통일
- 서버 중단 후에도 목표 조회·편집을 유지하도록 Room 로컬 저장 중심으로 전환. Compose Multiplatform으로 iOS 앱까지 배포

## Other Experience

- 브리시드 심리상담센터: React Native 앱의 미사용 SDK 등 18개 의존성 제거·pnpm 전환으로 iOS 시뮬레이터 Debug 빌드 **238.7초 → 195.8초(18.0% 단축)** — 동일 Mac·빈 DerivedData에서 각 3회 측정 중앙값
- YAPP 26기: Reed Android 파트 리드로 구조 설계·코드 리뷰와 OCR 입력 흐름 구현, 최우수상 수상

## Awards

**한국관광공사 X 카카오 2024 관광데이터 활용 공모전** <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.11</span><br>
트립메이트 앱 개발 및 출시, **장려상 및 강원관광재단 특별상 수상**

## Certificates

정보처리기사 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2022.09</span>

## Education

건국대학교 컴퓨터 공학부 학사 졸업 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.02</span>
