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

운영 중 재현하기 어려운 Android 문제를 끝까지 추적해 원인을 찾고 일회성 수정에 그치지 않는 해결책을 만들어왔습니다. BLE 의료기기·헬스 데이터·Media3·CameraX/TensorFlow Lite 기능을 제품에 적용하고, 웹뷰 제품에서는 브릿지와 프론트엔드까지 함께 개발했습니다.

사이드 프로젝트로 **Android 앱 9개와 iOS 앱 1개**를 출시·운영하며 사용자가 겪는 문제를 제품 기능으로 해결해왔습니다.\
개발 블로그와 팀 내 기술 공유를 통해 학습 내용을 정리하고, 실무 적용 관점의 기술 선택 과정을 공유해왔습니다.

## Work Experience

**메디플러스솔루션 (HD현대 계열사)** · Android Developer · 2024.05 ~ 재직 중

총 2년+ 경력으로, Hi-me 신규 헬스케어 서비스 개발을 주력으로 기존 건강관리·재활·명상 서비스의 Android 운영과 고도화를 함께 담당했습니다.

## Projects

### Hi-me <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2025.10 ~</span>

HD현대 그룹사 임직원 대상 건강관리 헬스케어 서비스 · [Google Play](https://play.google.com/store/apps/details?id=com.mediplussolution.hime) 다운로드 **2,000+**

- 웹뷰-네이티브 요청/응답 규격과 에러 처리 기준을 표준화하고, [Dari](https://github.com/easyhooon/dari) 라이브러리 기반 디버깅 환경을 구축해 Android·프론트엔드 개발자가 브릿지 호출 흐름과 실패 지점을 같은 화면에서 확인하도록 구성
- BLE Glucose/Blood Pressure Profile 기반 혈당계·혈압계 연동, 측정 데이터 동기화와 연동 해제까지 포함한 의료기기 데이터 수집 흐름 제공
- Health Connect 경유 시 걸음 수가 갱신되지 않는 경우를 위해 Samsung Health Data SDK 수집 경로를 추가하고, 걸음 수·심박수·소모 칼로리를 직접 동기화
- 웹뷰 오디오 재생 상태를 MediaSession과 동기화해 백그라운드 재생, 잠금화면·미디어 알림 컨트롤 제공
- GitHub Actions 기반 Play Console 내부 테스트 트랙 CD 환경 구축, 반복되는 테스트 배포 작업 자동화

### 세컨드 윈드/닥터 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

만성질환자와 암 수술 환자를 위한 맞춤 건강관리·재활 서비스 · [세컨드 윈드](https://play.google.com/store/apps/details?id=com.mediplussolution.android.csmsrenewal.secondwindforpatentkr)와 [세컨드 닥터 대표 앱](https://play.google.com/store/apps/details?id=com.mediplussolution.android.csmsrenewal.breastcancer)을 포함한 질환별 앱 5종, 총 6종 Google Play 누적 다운로드 합산 **13,000+**

- ExoPlayer2 기반 운동 영상 플레이어를 Media3로 마이그레이션하고 긴 영상을 구간 단위로 내려받아, 전체 파일 다운로드 완료 전에도 내려받은 첫 구간부터 영상을 재생할 수 있도록 변경해 재생 시작 대기 완화
- TensorFlow Lite + CameraX 기반 어깨 움직임 측정 기능 개발, 팔벌림 각도 정확도 **오차범위 ±5도 이내**로 개선
- Android OS 정책 변경에 맞춘 BLE 연동 SDK 수정과 AAR 재배포, 웨어러블 기기 연동 중단 이슈 해결

### 브리시드 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

사용자 맞춤 명상 경험을 지원하는 웰니스 서비스 · [Google Play](https://play.google.com/store/apps/details?id=com.mediplussolution.android.breeseed) 다운로드 **500+**

- Google Play 인앱 결제 연동, 일회성 결제 플로우를 구현해 유료 콘텐츠 구매 경로 추가
- 명상 음악 플레이어의 Activity-Service 통신을 Broadcast Receiver에서 Flow 기반 스트림으로 전환해 재생 상태의 생산·소비 경로 통합
- KISA 보안취약점 점검에서 지적된 앱 위변조·루팅·백그라운드 오버레이 항목에 Play Integrity API와 런타임 탐지 로직을 적용해 보안 대응 강화
- 전역 싱글톤에 의존하던 플레이어·결제 객체를 Hilt가 생성·제공하도록 전환해 전역 접근 제거

### 마이밸런스 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

직장인의 건강한 습관 형성을 지원하는 건강관리·리워드 서비스

- Health Connect 연동, 걸음 수·소모 칼로리·평균 심박수·수면시간 데이터 수집 경로 통합
- Bamboo 기반 CI/CD 배포 환경 구축, 수동 빌드 과정에서 발생하던 빌드 넘버 충돌 제거
- 클래스 사진 업로드 로직을 갤러리 저장 방식에서 임시 파일 생성·업로드 후 제거하는 방식으로 전환해 불필요한 미디어 파일이 기기에 남지 않도록 변경

## Team Projects

### 유니페스 : 대학축제의 지도를 펼쳐라! <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.03 ~ 2025.10</span>

<span style="font-size: 0.9em;">Android 개발자 2명, 배포까지 2개월, 현재 운영 중</span> · 고려대·가천대·상명대·한국교통대 축제 공식 앱 선정, Play Store 다운로드 **2,000+**, 축제 운영 기간 Android/iOS 통합 최고 **WAU 5,000+**

- Naver Map Compose 클러스터링을 적용해 줌 레벨에 따라 밀집된 부스·행사 마커를 묶고 펼쳐서 표시해 지도 정보 가독성 개선
- MVI 패턴과 구글 권장 아키텍처 기반 모듈화를 적용하고 화면 상태·이벤트 처리 책임을 기능 모듈 안으로 분리
- QR 스캔 결과를 부스 참여 상태와 연결해 현장 행사 인증을 앱 안에서 완료하도록 구현
- Firebase Remote Config로 지원 앱 버전 기준을 원격에서 제어하고, API 에러 코드를 앱의 예외 처리 흐름에 연결해 버전·예외 상황 대응 강화
- Firebase App Distribution으로 테스트 빌드를 배포하고, Room Migration Test로 이전 데이터베이스 스키마에서 현재 버전까지의 마이그레이션 회귀 검증 강화

### 반다라트 - 부담 없는 만다라트 계획표 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2023.07 ~</span>

<span style="font-size: 0.9em;">Android 개발자 2명, 배포까지 2개월, 현재 운영 중</span>

- Android 앱을 Compose Multiplatform으로 마이그레이션, 기존 Android 코드 기반으로 iOS 앱까지 배포
- Slack Circuit Presenter가 계획표 상태 생성과 이벤트 처리를 담당하고, UI 컴포저블은 상태 소비와 이벤트 전달만 맡도록 구성
- 서버 API 의존 구조를 로컬 Room Database 기반으로 전환, 서버 중단 이후에도 서비스 유지
- Jetpack Compose 기반 Custom UI와 공통 컴포넌트 정의, 화면 구성 일관성 확보와 Google Play In-App Update 기반 업데이트 유도 흐름 제공
- Room Database, Repository, ViewModel 테스트 코드와 GitHub Actions CI 도입, 데이터 변경과 화면 로직 회귀 검증 자동화

## Libraries

- [Dari](https://github.com/easyhooon/dari): 실무 WebView 연동 디버깅 문제에서 출발해 만든 Android 라이브러리. 특정 WebView 브릿지 구현체에 묶이지 않도록 설계했으며, JavaScript bridge 메시지의 요청·응답·상태를 실시간으로 확인해 프론트엔드 개발자도 호출 흐름과 실패 지점을 함께 추적할 수 있도록 지원. debug/release 분리를 위한 no-op 모듈 제공.
- [RoutePeek](https://github.com/easyhooon/routepeek): WebView의 현재 route와 SPA route 변경을 Compose overlay로 확인하는 Android 디버깅 라이브러리. 웹뷰 화면의 현재 경로를 앱 안에서 바로 확인해 라우팅 이슈를 재현하고 공유하기 쉽게 지원.

## Other Experience

- 개발 워크플로 자동화: **AI 코딩 에이전트용 스킬**에 커밋·PR 생성, 배포 전 검증, 코드 리뷰 반영 절차를 정의해 동일한 체크리스트를 반복 실행할 수 있도록 구성
- 브리시드 심리상담센터: React Native 기반 사내 상담 예약 앱 유지보수, OS 호환성 이슈 수정, 생체인증 로그인 정보 자동 완성 도입, 네트워크 이슈 재현 경로 확보
- YAPP 26기: Reed 프로젝트 Android 파트 리드로 구조 설계·기술 스택 검토·코드 리뷰 담당, Android Manifest Interview 도서/기술 블로그 작성 스터디 운영, 최우수상 수상, 27·28기 Android 개발자 선발 면접 참여
- Nexters 23·24·26기: 반다라트, I'lab, Ziine 프로젝트 Android 구조 설계·기술 스택 선정·코드 리뷰, 출시 후 리팩터링과 성능 병목 분석 담당

## Awards

**한국관광공사 X 카카오 2024 관광데이터 활용 공모전** <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.11</span><br>
트립메이트 앱 개발 및 출시, **장려상 및 강원관광재단 특별상 수상**

## Certificates

정보처리기사 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2022.09</span>

## Education

건국대학교 컴퓨터 공학부 학사 졸업 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.02</span>
