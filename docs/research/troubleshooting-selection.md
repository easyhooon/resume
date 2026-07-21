# 프로젝트별 Troubleshooting 추가 후보 조사

조사일: 2026-07-21

## 결론

- **유니페스: 추가 권장** — 동적 이미지의 휘도를 분석해 시스템 바·뒤로가기 아이콘 대비를 보장한 사례
- **반다라트: 추가 권장** — KMP에서 Android/iOS 이미지 저장·공유의 플랫폼 경계를 분리한 사례
- **Reed: 추가하지 않음 권장** — 현재 코루틴 취소와 Metro 마이그레이션 2건으로 문제 해결 폭이 충분하다. 3건째를 넣으면 최근 대표 프로젝트에 분량이 과도하게 몰린다. 꼭 추가한다면 Stability Check CI 병렬화가 최선이다.

권장 최종 개수는 **Reed 2 / 유니페스 2 / 반다라트 1**이다.

## 유니페스 — 동적 이미지와 겹치는 아이콘 가독성 개선

### 선정 이유

- 사용자에게 직접 보이는 가독성 문제다.
- 단순 색상 변경이 아니라 `실제 콘텐츠 분석 → 계산 범위 축소 → UI 반영`의 판단 과정이 선명하다.
- 현재 배운 점에 없는 콘텐츠 기반 UI 판단과 제한적 샘플링 원칙을 보여 준다.

### 출처로 확인되는 사실

- **문제**: 이미지가 StatusBar와 TopAppBar 뒤까지 차는 부스 상세 화면에서, 테마만 기준으로 아이콘 색상을 정하면 이미지와 아이콘의 명도가 겹쳐 아이콘이 보이지 않았다.
- **원인**: 실제 배경은 동적으로 바뀌는 네트워크 이미지인데 기존 구현은 라이트·다크 테마만 판단 기준으로 사용했다. 초기 휘도 계산은 이미지 전체 픽셀을 순회해 화면에 쓰지 않는 영역까지 계산했다.
- **해결**: Coil로 얻은 Bitmap의 RGB에 BT.709 계수 `0.2126 / 0.7152 / 0.0722`를 적용했다. 실제로 아이콘이 겹치는 이미지 상단 30%만 계산하고, 가로 `width / 50`, 세로 `sampleHeight / 20` 간격으로 샘플링했다. 계산은 `Dispatchers.Default`에서 수행하고, 평균 휘도가 0.5보다 밝으면 어두운 아이콘을, 어두우면 밝은 아이콘을 적용했다.
- **결과**: 라이트·다크 모드와 관계없이 이미지와 대비되는 아이콘을 적용해 가독성 문제를 해결했다.
- **제약**: 글은 일부 이미지 엣지 케이스가 남는다고 명시하며 계산 시간이나 연산량의 정량 수치를 제시하지 않는다. 따라서 `성능을 N% 개선` 또는 `모든 이미지에서 대비 보장` 같은 표현은 쓰지 않아야 한다.

### 연결할 배운 점

테마 같은 간접 상태가 아니라 실제 콘텐츠를 UI 판단의 입력으로 삼고, 비용이 큰 연산은 문제와 직접 관련된 영역과 대표 표본으로 제한한다.

### 출처

- [작성자의 유니페스 구현 기록](https://velog.io/@mraz3068/How-To-Know-Image-Luminance)
- [Android 공식 edge-to-edge 문서](https://developer.android.com/develop/ui/views/layout/edge-to-edge)

## 반다라트 — KMP 네이티브 이미지 저장·공유 경계 분리

### 선정 이유

- 현재 반다라트의 두 배운 점인 `공통/플랫폼 책임 경계`와 `ImageBitmap → UIImage 색상 문제`를 하나의 구체적인 문제 해결 흐름으로 묶는다.
- Android 앱을 Compose Multiplatform으로 옮겨 iOS까지 출시했다는 핵심 성과와 직접 연결된다.
- iOS 출시기는 단일 문제 해결보다 전체 마이그레이션 회고에 가까우므로 별도 Troubleshooting 카드보다 결과·참고 링크로 쓰는 편이 정확하다.

### 출처로 확인되는 사실

- **문제**: Android `Context`, `MediaStore`, `FileProvider`에 의존한 이미지 저장·공유 코드를 `commonMain`에서 그대로 사용할 수 없었다. Android 구현에만 `Application`을 주입하면서 iOS용 구현도 제공해야 했고, `commonMain`에서는 `android.net.Uri`도 사용할 수 없었다.
- **원인**: 같은 저장·공유 기능이라도 Android와 iOS가 사용하는 네이티브 API, URI 타입, 이미지 타입과 픽셀·색 공간 처리가 달랐다.
- **해결**: 공통 코드에 `ImageHandlerProvider`와 `platformModule` 계약을 두고 플랫폼 소스셋에서 구현했다. Android는 Koin의 `androidContext`/`androidApplication`으로 `Application`을 생성자 주입하고 `MediaStore`·`FileProvider`를 사용했다. iOS는 Foundation·UIKit·CoreGraphics를 사용했으며, 공통 URI에는 `uri-kmp`를 적용했다.
- **색상 문제 해결**: 처음 참고한 `ImageBitmap → UIImage` 변환 구현은 색이 바래 채택하지 않았다. 이후 sRGB CoreGraphics 컨텍스트를 거쳐 `UIImage`를 만드는 구현으로 교체했다.
- **결과**: 공통 호출부를 유지하면서 Android와 iOS 모두에서 계획표 이미지 저장·공유 기능을 제공했다. 정량 성능 수치는 제시되지 않았다.

### 연결할 배운 점

KMP 전환은 플랫폼 코드를 무조건 공통화하는 일이 아니라, 공통 코드에는 계약과 호출 흐름을 남기고 네이티브 타입·API·DI 구성은 플랫폼 경계에 격리하는 일이다. 이미지 변환은 픽셀 배치, 색 공간, 알파 채널, 바이트 순서까지 이해해야 한다.

### 표현 주의

현재 구현은 `expect class`를 사용하지만, Kotlin 공식 문서는 일반 인터페이스와 DI를 우선 권장하고 `expect/actual`은 DI 구성 지점 등에 제한하는 접근을 권장한다. `expect/actual이 정답`보다는 **플랫폼별 구현 경계를 분리했다**고 표현하는 편이 안전하다.

### 출처

- [작성자의 Koin·expect/actual 이미지 처리 기록](https://velog.io/@mraz3068/KMP-Koin-Expect-Actual-Pattern-For-Native-Image-Handling)
- [작성자의 반다라트 iOS 출시 회고](https://velog.io/@mraz3068/Bandalart-iOS-App-Deployment-Complete)
- [Kotlin 공식 expect/actual 문서](https://kotlinlang.org/docs/multiplatform/multiplatform-expect-actual.html)
- [Koin 공식 Android 주입 문서](https://insert-koin.io/docs/reference/koin-android/get-instances/)

## Reed — 추가하지 않음 권장

Reed README에는 Metro, Compose Stability Analyzer, Toast 내부 분석, 코루틴 취소, 복수 API 예외 처리, Circuit 효과·이벤트·Navigation, OCR, ModalBottomSheet 등 여러 기록이 있다. 현재 포트폴리오에는 이미 다음 두 사례가 있다.

1. 화면 이탈에 따른 `CancellationException`을 API 실패와 분리한 사용자 오류 처리
2. 최소 재현 프로젝트로 Hilt → Metro 마이그레이션의 모듈 클래스패스 문제를 해결한 컴파일러·의존성 경계 분석

두 사례가 사용자 동작과 빌드 아키텍처를 각각 다루므로 폭이 충분하다. 포트폴리오 전체 균형을 위해 Reed는 2건을 유지한다.

### 꼭 하나 더 넣는다면: Stability Check CI 병렬화

- **문제**: Compose Stability Validation을 기존 CI 단계 뒤에 순차 추가하자 평소 8~12분이던 CI가 20분을 넘었다.
- **원인**: 서로 의존하지 않는 빌드 검사와 Stability Check를 하나의 순차 경로로 실행했다.
- **해결**: 공통 설정을 정리하고 Stability Check를 별도 GitHub Actions job으로 분리해 기존 검사와 병렬 실행했다.
- **결과**: 전체 소요 시간이 20분에서 8분으로 약 60% 단축돼 Stability Check를 CI에 유지할 수 있었다.
- **선정 보류 이유**: 수치는 강하지만 최종 프로젝트별 개수가 Reed 3 / 유니페스 2 / 반다라트 1이 되어 분량이 Reed에 치우친다.

### 출처

- [Reed README Troubleshooting 목록](https://github.com/YAPP-Github/Reed-Android#troubleshooting)
- [작성자의 Compose Stability Analyzer 적용 기록](https://velog.io/@mraz3068/compose-stability-analyzer-review)
- [GitHub 공식 workflow jobs 문서](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-jobs)
