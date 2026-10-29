# 이지훈 경력기술서

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

## Work Experience

**메디플러스솔루션 (HD현대 계열사)** · Android Developer · 2024.05 ~ 재직 중

2년 이상 Android 개발자로 근무하며, 신규 헬스케어 서비스 Hi-me 개발을 중심으로 기존 건강관리·재활·명상 앱의 유지보수와 기능 고도화를 병행했습니다.

### Hi-me <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2025.10 ~</span>

HD현대 그룹사 임직원 대상 건강관리 헬스케어 서비스 · [Google Play](https://play.google.com/store/apps/details?id=com.mediplussolution.hime) 다운로드 **2,000+**

- **웹뷰 브릿지 규격 표준화와 [Dari](https://github.com/easyhooon/dari) 기반 디버깅 환경 구축**
  - 웹뷰-네이티브 요청/응답 규격과 에러 처리 기준 표준화
  - Android·프론트엔드 개발자가 브릿지 호출 흐름과 실패 지점을 같은 화면에서 확인하도록 구성
- **웹뷰 이미지 전달 시 메인 스레드 점유 76% 감소** (14.2ms → 3.4ms, 실기기 p50)
  - base64 이미지가 담긴 브릿지 메시지의 JSON 직렬화를 메인 스레드 밖으로 옮기고, 이미지 전달 방식을 base64 문자열에서 캐시 파일 기반 로컬 URL로 전환해 Macrobenchmark(실기기, n=20)에서 전달 시간 67% 단축(15.9ms → 5.2ms), 운영 적용은 웹 배포 후 예정
- **BLE 의료기기·헬스 데이터 수집**
  - BLE Glucose/Blood Pressure Profile 기반 혈당계·혈압계 연동, 측정 데이터 동기화와 연동 해제까지 제공
  - Health Connect 경유 시 걸음 수가 갱신되지 않는 경우를 위해 Samsung Health Data SDK 수집 경로 추가
- **웹뷰 오디오의 백그라운드 재생 지원**
  - 웹뷰 오디오 플레이어(video.js)의 재생 위치·재생/일시정지 상태를 네이티브 Media3 ExoPlayer·MediaSession과 동기화
  - 앱을 나가거나 화면을 꺼도 재생이 끊기지 않고, 잠금화면·알림에서 제어하며 앱 복귀 시 같은 위치에서 이어 재생

### 세컨드 윈드/닥터 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

만성질환자와 암 수술 환자를 위한 맞춤 건강관리·재활 서비스 · [세컨드 윈드](https://play.google.com/store/apps/details?id=com.mediplussolution.android.csmsrenewal.secondwindforpatentkr)와 유방암·전립선암·대장암·위암 대상 [세컨드 닥터](https://play.google.com/store/apps/details?id=com.mediplussolution.android.csmsrenewal.breastcancer) 4종으로 현재 총 5종 운영 · 전체 출시 앱 Google Play 누적 다운로드 합산 **13,000+**

- **레거시 Java 6.9만 줄의 97% Kotlin 전환 주도** (Kotlin 비율 12% → 97%)
  - 원본 동작을 테스트로 고정해 전환 전후를 비교하는 A-A 검증과 뮤테이션 테스트로 모든 전환을 확인하며 입사 당시 0개였던 단위 테스트를 현재 1,700개 이상으로 늘림
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

직장인의 건강한 습관 형성을 지원하는 건강관리·리워드 서비스 · [Google Play](https://play.google.com/store/apps/details?id=com.kyobo.mybalance) 다운로드 **2,000+**

- **Health Connect 연동**: 걸음 수·소모 칼로리·평균 심박수·수면시간 데이터 수집 경로 통합
- **CI/CD GitHub Actions 전환**: Bamboo 기반 레거시 CI/CD를 옮겨 빌드 넘버 관리를 자동화하고 충돌 문제 해결

## 기타 사내 업무

- 메디플러스솔루션 [브리시드 심리상담센터](https://play.google.com/store/apps/details?id=com.mediplussolution.mentalcounsel) 앱(React Native): 미사용 SDK 등 18개 의존성 제거·pnpm 전환으로 iOS 시뮬레이터 Debug 빌드 **238.7초 → 195.8초(18.0% 단축)**, 동일 Mac·빈 DerivedData에서 각 3회 측정 중앙값
  - **HotUpdater + Supabase 기반 OTA 업데이트 환경 구축**: 고객사 요청 1건을 스토어 심사 없이 반영, 연말 해당 요건 롤백도 OTA로 반영 예정. Prod/Dev DB 분리, GitHub Actions 배포·롤백·이전 번들 정리 workflow, 강제 업데이트 플래그 적용

<span style="font-size: 0.9em; color: #6b7280;">회사·사이드 프로젝트·오픈소스의 문제 해결 과정은 [포트폴리오](https://github.com/easyhooon/resume/blob/main/PORTFOLIO.md)에 정리했습니다.</span>
