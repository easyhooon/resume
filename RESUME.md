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
    <td><strong>Portfolio</strong> <a href="https://app.notion.com/p/mraz3068/Android-Developer-12a1067917dc4885bb5570bf5fda9f86?source=copy_link">Notion</a></td>
    <td><strong>LinkedIn</strong> <a href="https://www.linkedin.com/in/easyhooon/">linkedin.com/in/easyhooon</a></td>
  </tr>
</table>

## Introduce

웹뷰와 네이티브가 맞물리는 Android 제품에서 브릿지 규격, 디버깅 도구, 헬스·미디어·카메라 기능을 구현하며 안정적인 사용자 경험을 만들어왔습니다.

반복되는 commit/PR 생성, 배포 체크리스트, 코드 리뷰 반영 보조를 AI 기반 자동화 skill로 정리해 1인 Android 개발 환경의 한계를 보완했습니다.

사이드 프로젝트로 Android 앱 9개와 iOS 앱 1개를 출시·운영하며 사용자가 겪는 문제를 제품 기능으로 해결해왔습니다.\
개발 블로그와 팀 내 기술 공유를 통해 학습 내용을 정리하고, 실무 적용 관점의 기술 선택 과정을 공유합니다.

## Work Experience

| 회사 | 기간 | 직무 |
| --- | --- | --- |
| 메디플러스솔루션 (HD현대 계열사) | 2024.05 ~ 재직 중 | Android Developer |

Hi-me 신규 헬스케어 서비스 개발을 주력으로, 기존 건강관리·재활·명상 서비스의 Android 운영과 고도화를 함께 담당했습니다.

## Projects

### Hi-me <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2025.10 ~</span>

HD현대 그룹사 임직원 대상 건강관리 헬스케어 서비스

- 웹뷰-네이티브 요청/응답 규격과 에러 처리 기준을 정의하고, 샘플 payload·상태값·재현 케이스를 표준화해 Android·웹·외주 개발사 간 이슈 분류 기준 통일
- Dari 기반 WebView 브릿지 통신 디버깅 환경 구축, 요청/응답 payload와 성공·실패 상태를 Android·프론트엔드 개발자가 함께 확인하도록 개선
- BLE Glucose/Blood Pressure Profile 기반 혈당계·혈압계 연동, 측정 데이터 동기화와 연동 해제까지 포함한 의료기기 데이터 수집 흐름 제공
- Samsung Health Data SDK 연동으로 Health Connect 경유 시 발생하던 걸음 수 미갱신 이슈 보완, 걸음 수·심박수·소모 칼로리 수집 경로 안정화
- 웹뷰 오디오 재생 상태를 MediaSession과 동기화, 백그라운드 재생과 미디어 알림 컨트롤을 지원해 웹뷰 앱의 오디오 사용성 보완
- GitHub Actions 기반 Play Console 내부 테스트 트랙 CD 환경 구축, 반복되는 테스트 배포 작업 자동화

### 세컨드 윈드/닥터 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

만성질환자와 암 수술 환자를 위한 맞춤 건강관리·재활 서비스

- ExoPlayer2 기반 운동 영상 플레이어를 Media3로 마이그레이션하고 긴 영상을 구간 단위로 내려받는 단계별 다운로드를 도입해, 전체 다운로드 완료를 기다려야 하던 운동 영상 시작 대기 흐름 개선
- TensorFlow Lite + CameraX 기반 어깨 움직임 측정 기능 개발, 팔벌림 각도 정확도 오차범위 ±5도 이내로 개선
- Android OS 정책 변경에 맞춘 BLE 연동 SDK 수정과 AAR 재배포, 웨어러블 기기 연동 중단 이슈 해결

### 브리시드 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

사용자 맞춤 명상 경험을 지원하는 웰니스 서비스

- Google Play 인앱 결제 연동, 일회성 결제 플로우를 구현해 유료 콘텐츠 구매 경로 추가
- 명상 음악 플레이어의 Activity-Service 통신을 Broadcast Receiver에서 Flow 기반 구조로 전환, 상태 동기화 복잡도 완화
- KISA 보안취약점 점검에서 지적된 앱 위변조·루팅·백그라운드 오버레이 항목을 Play Integrity API와 런타임 탐지 로직으로 대응
- 전역 싱글톤에 의존하던 플레이어·결제 객체를 Hilt 기반 의존성 주입으로 전환, 생명주기 관리와 테스트 용이성 개선

### 마이밸런스 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.05 ~</span>

직장인의 건강한 습관 형성을 지원하는 건강관리·리워드 서비스

- Health Connect 연동, 걸음 수·소모 칼로리·평균 심박수·수면시간 데이터 수집 경로 통합
- Bamboo 기반 CI/CD 배포 환경 구축, 수동 빌드 과정에서 발생하던 빌드 넘버 충돌 제거
- 클래스 사진 업로드 로직을 갤러리 저장 방식에서 임시 파일 생성/제거 방식으로 전환, 디바이스 리소스 사용 개선

## Team Projects

### 유니페스 : 대학축제의 지도를 펼쳐라! <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.03 ~ 2025.10</span>

<span style="font-size: 0.9em;">Android 개발자 2명, 배포까지 2개월, 현재 운영 중</span> · 고려대·가천대·상명대·한국교통대 축제 공식 앱 선정, Play Store 다운로드 2,000+, Android/iOS 통합 WAU 5,000+

- Naver Map Compose 클러스터링 적용, 축제 지도 내 부스·행사 정보 가독성 개선
- MVI 패턴과 구글 권장 아키텍처 기반 모듈화 적용, 화면 상태와 이벤트 처리 책임을 분리해 기능 단위 변경이 가능한 구조로 개선
- QR 기반 부스 행사 참여 인증 기능 구현, 학생들의 축제 이벤트 참여 흐름 개선
- Firebase Remote Config 기반 강제 업데이트와 API 커스텀 에러 처리 적용, 앱 버전 관리와 예외 상황 처리 강화
- Firebase App Distribution CD와 Room Migration Test 도입, 테스트 배포와 데이터베이스 스키마 변경 안정성 확보

### 반다라트 - 부담 없는 만다라트 계획표 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2023.07 ~</span>

<span style="font-size: 0.9em;">Android 개발자 2명, 배포까지 2개월, 현재 운영 중</span>

- Android 앱을 Compose Multiplatform으로 마이그레이션, 기존 Android 코드 기반으로 iOS 앱까지 배포
- Slack Circuit 기반으로 계획표 화면의 상태 생성과 이벤트 처리를 분리해 UI 컴포저블의 책임을 단순화
- 서버 API 의존 구조를 로컬 Room Database 기반으로 전환, 서버 중단 이후에도 서비스 유지
- Jetpack Compose 기반 Custom UI와 공통 컴포넌트 정의, 화면 구성 일관성 확보와 Google Play In-App Update 기반 업데이트 유도 흐름 제공
- Room Database, Repository, ViewModel 테스트 코드와 GitHub Actions CI 도입, 데이터 변경과 화면 로직 회귀 검증 자동화

## Libraries

- [Dari](https://github.com/easyhooon/dari): 실무 WebView 연동 디버깅 문제에서 출발해 만든 Android 라이브러리. 특정 WebView 브릿지 구현체에 묶이지 않도록 설계했으며, JavaScript bridge 메시지의 요청·응답·상태를 실시간으로 확인해 프론트엔드 개발자도 호출 흐름과 실패 지점을 함께 추적할 수 있도록 지원. debug/release 분리를 위한 no-op 모듈 제공.
- [RoutePeek](https://github.com/easyhooon/routepeek): WebView의 현재 route와 SPA route 변경을 Compose overlay로 확인하는 Android debug 라이브러리. 웹뷰 화면의 현재 경로를 앱 안에서 바로 확인해 라우팅 이슈 재현과 공유를 쉽게 개선.

## Other Experience

- 브리시드 심리상담센터: React Native 기반 사내 상담 예약 앱 유지보수, OS 호환성 이슈 수정, 생체인증 로그인 정보 자동 완성 도입, 네트워크 이슈 재현 경로 확보
- YAPP 26기: Reed 프로젝트 Android 파트 리드로 구조 설계·기술 스택 검토·코드 리뷰 담당, Android Manifest Interview 도서/기술 블로그 작성 스터디 운영, 최우수상 수상, 27·28기 Android 개발자 선발 면접 참여
- Nexters 23·24·26기: 반다라트, I'lab, Ziine 프로젝트 Android 구조 설계·기술 스택 선정·코드 리뷰, 출시 후 코드 품질 개선과 성능 최적화

## Awards

**한국관광공사 X 카카오 2024 관광데이터 활용 공모전** <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.11</span><br>
트립메이트 앱 개발 및 출시, 장려상 및 강원관광재단 특별상 수상

## Certificates

정보처리기사 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2022.09</span>

## Education

건국대학교 컴퓨터 공학부 학사 졸업 <span style="margin-left: 0.75em; font-size: 0.85em; color: #9ca3af; font-weight: normal;">2024.02</span>
