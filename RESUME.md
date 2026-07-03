# 이지훈 Android Developer

**Birth date** 1997.06.24<br>
**Phone** 010-2010-3068<br>
**Email** mraz3068@gmail.com<br>
**GitHub** [github.com/easyhooon](https://github.com/easyhooon)<br>
**Tech Blog** [velog.io/@mraz3068/posts](https://velog.io/@mraz3068/posts)<br>
**Portfolio** [Android Developer](https://app.notion.com/p/mraz3068/Android-Developer-12a1067917dc4885bb5570bf5fda9f86?source=copy_link)

## Introduce

헬스케어·웰니스 Android 앱을 개발하며 BLE 의료기기 연동, Samsung Health Data SDK, Health Connect, Media3, CameraX/TensorFlow Lite 기반 기능을 구현해왔습니다.

Android를 중심으로 웹뷰 브릿지, 프론트엔드, 디버깅 도구 개발까지 다루며 하이브리드 앱의 문제를 끝까지 추적합니다. 웹뷰 디버깅 과정에서 Android·프론트엔드 개발자가 함께 문제를 확인할 수 있도록 Dari와 RoutePeek 디버깅 라이브러리를 개발했습니다.

사이드 프로젝트로 Android 앱 9개와 iOS 앱 1개를 출시·운영했고, 대학 축제 공식 앱 선정, Play Store 다운로드 2,000+, Android/iOS 통합 WAU 5,000+ 성과를 경험했습니다.

## Work Experience

**메디플러스솔루션 (HD현대 계열사)** <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~ 재직 중</span><br>
Android Developer, 연구개발부문 매니저

## Core Projects

### Hi-me <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2025.10 ~</span>

HD현대 그룹사 임직원 대상 건강관리 헬스케어 서비스

- 웹뷰-네이티브 간 요청/응답 규격과 에러 처리 방식을 정의하고, 외주 개발사 연동 가이드와 이슈 대응을 담당했습니다.
- 서비스 내 웹 프론트엔드 업무를 병행하며 웹뷰-네이티브 연동 이슈를 양쪽 코드 흐름에서 추적하고 대응했습니다.
- WebView 브릿지 통신 디버깅을 위해 Dari를 개발하고, 요청/응답 payload와 성공·실패 상태를 Android·프론트엔드 개발자가 함께 확인할 수 있는 구조를 만들었습니다.
- BLE Glucose/Blood Pressure Profile 기반 혈당계·혈압계 연동, 측정 데이터 동기화, 연동 해제를 구현했습니다.
- Samsung Health Data SDK를 연동해 Health Connect 경유 시 발생하던 걸음 수 미갱신 이슈를 보완하고, 걸음 수·심박수·소모 칼로리 수집 경로를 안정화했습니다.
- MediaSession 기반 미디어 알림을 구현해 웹뷰 앱에서도 오디오 백그라운드 재생과 미디어 컨트롤을 지원했습니다.
- GitHub Actions 기반 Play Console 내부 테스트 트랙 CD 환경을 구축해 테스트 배포 과정을 자동화했습니다.

### 세컨드 윈드/닥터 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

만성질환자와 암 수술 환자를 위한 맞춤 건강관리·재활 서비스

- ExoPlayer2 기반 운동 영상 플레이어를 Media3로 마이그레이션하고, 관련 레거시 코드를 Kotlin으로 전환했습니다.
- Media3 기반 단계별 다운로드와 연속 재생 기능을 도입해 운동 영상 시청 흐름을 개선했습니다.
- 유방암 환자의 회복 진척도 측정을 위해 TensorFlow Lite + CameraX 기반 어깨 움직임 측정 기능을 개발했고, 팔벌림 각도 정확도를 오차범위 ±5도 이내로 개선했습니다.
- Android OS 정책 변경에 맞춰 BLE 연동 SDK를 수정하고 AAR을 재배포해 웨어러블 기기 연동 중단 이슈를 대응했습니다.

### 브리시드 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

사용자 맞춤 명상 경험을 지원하는 웰니스 서비스

- Google Play 인앱 결제를 연동해 일회성 결제 플로우를 구현했습니다.
- 명상 음악 플레이어의 Activity-Service 통신을 Broadcast Receiver에서 Flow 기반 구조로 전환하고, XML UI를 Compose로 이전했습니다.
- KISA 보안취약점 점검에 대응해 Play Integrity API 기반 앱 무결성 검증, 루팅 탐지, 백그라운드 오버레이 방어를 도입했습니다.

### 마이밸런스 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

직장인의 건강한 습관 형성을 지원하는 건강관리·리워드 서비스

- Health Connect를 연동해 걸음 수, 소모 칼로리, 평균 심박수, 수면시간 데이터를 수집했습니다.
- Bamboo 기반 CI/CD 배포 환경을 구축해 수동 빌드 과정에서 발생하던 빌드 넘버 충돌을 제거했습니다.

### 브리시드 심리상담센터 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2025.03 ~</span>

React Native 기반 임직원 심리 상담 예약 플랫폼

- 사내 서비스 요구사항에 맞춰 React Native 앱 유지보수와 OS 호환성 대응을 담당했습니다.
- 생체인증 기반 로그인 정보 자동 완성 기능을 도입했습니다.
- 실시간 네트워크 디버깅 환경을 구축해 서버 연동 이슈를 재현하고 확인할 수 있도록 했습니다.

## Team Projects

### 유니페스 : 대학축제의 지도를 펼쳐라! <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.03 ~ 2025.10</span>

<span style="font-size: 0.9em;">Android 개발자 2명, 배포까지 2개월, 현재 운영 중</span><br>
고려대·가천대·상명대·한국교통대 축제 공식 앱으로 선정, Play Store 다운로드 2,000+, Android/iOS 통합 WAU 5,000+

- Naver Map Compose 클러스터링을 적용해 축제 지도 내 부스·행사 정보의 가독성을 개선했습니다.
- MVI 패턴과 구글 권장 아키텍처 기반 모듈화를 적용해 상태/이벤트 처리 흐름을 정리했습니다.
- QR 기반 부스 행사 참여 인증, Remote Config 강제 업데이트, API 커스텀 에러 처리, Firebase App Distribution CD, Room Migration Test를 구현했습니다.

### 반다라트 - 부담 없는 만다라트 계획표 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2023.07 ~</span>

<span style="font-size: 0.9em;">Android 개발자 2명, 배포까지 2개월, 현재 운영 중</span>

- Android 앱을 Compose Multiplatform으로 마이그레이션해 iOS 앱을 함께 배포했습니다.
- 서버 API 의존 구조를 로컬 Room Database 기반으로 전환해 서버 중단 이후에도 서비스를 유지할 수 있도록 했습니다.
- Room Database, Repository, ViewModel 테스트 코드와 GitHub Actions CI를 도입했습니다.

## Libraries

- Dari: WebView JavaScript bridge 메시지의 요청·응답·상태를 실시간으로 확인하기 위해 개발한 Android 디버깅 라이브러리입니다. 프론트엔드 개발자도 브릿지 호출 흐름과 실패 지점을 확인할 수 있어 웹뷰 연동 이슈 디버깅에 기여했습니다. debug/release 분리를 위해 no-op 모듈을 함께 제공했습니다.<br>
  [easyhooon/dari](https://github.com/easyhooon/dari)
- RoutePeek: WebView의 현재 route와 SPA route 변경을 Compose overlay로 확인하기 위해 개발한 Android debug 라이브러리입니다. 웹뷰 화면의 현재 경로를 앱 안에서 바로 확인할 수 있게 해 라우팅 이슈 재현과 공유를 쉽게 만들었습니다.<br>
  [easyhooon/routepeek](https://github.com/easyhooon/routepeek)

## Other Experience

- YAPP 26기: Reed 프로젝트 Android 아키텍처 설계·기술 스택 검토·코드 리뷰를 담당했고, 최우수상을 수상했습니다.
- Nexters 23·24·26기: 반다라트, I'lab, Ziine 프로젝트의 Android 아키텍처 설계·기술 스택 선정·코드 리뷰를 담당했습니다.

## Awards

**한국관광공사 X 카카오 2024 관광데이터 활용 공모전** <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.11</span><br>
트립메이트 앱 개발 및 출시, 장려상 및 강원관광재단 특별상 수상

## Certificates

정보처리기사 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2022.09</span>

## Education

건국대학교 컴퓨터 공학부 학사 졸업 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.02</span>
