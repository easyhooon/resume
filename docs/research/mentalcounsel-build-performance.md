# 심리상담 앱 빌드 개선 성과 근거

2026-09-09 작업 완료. React Native 기반 브리시드 심리상담센터 앱에서 Yarn Classic을 pnpm으로 전환하고, 사용하지 않는 Jitsi·WebRTC·CallKeep·VoIP 등 18개 의존성과 관련 통화 코드·권한을 정리했다. pnpm 단독 전환과 SDK 제거를 포함한 최종 구성을 나눠 측정했다.

## 이력서에 반영한 수치

| 지표 | 변경 전 | 변경 후 | 결과 |
|---|---:|---:|---:|
| iOS 시뮬레이터 DebugDev 빌드 중앙값, 빈 DerivedData, 각 n=3 | 238.726초 | 195.750초 | 42.976초 / 18.00% 단축 |
| 동일 의존성, 빈 패키지 캐시 설치 중앙값, 각 n=3 | 34.136초 | 20.528초 | 13.608초 / 39.86% 단축 |
| Android assembleDevDebug actionable tasks, 각 3회 동일 | 1,071개 | 761개 | 310개 / 28.94% 감소 |

이력서에는 초와 퍼센트를 소수점 첫째 자리까지 표시한다. 시간 단축률은 `(변경 전 − 변경 후) / 변경 전 × 100`이며 반올림 전 수치로 계산한다. 빌드 작업 수 감소율은 실행 시간 단축률과 구분한다.

## 측정 조건과 해석

동일 Apple M2 Mac(8 logical CPUs, RAM 16 GiB), Node 26.7.0, Yarn 1.22.22, pnpm 10.13.1에서 측정했다. iOS는 Xcode 26.6, arm64 시뮬레이터 DebugDev, jobs=4, 코드 서명 없이 빌드했다. 타깃 휴대폰 성능보다 빌드를 실행하는 Mac의 CPU·메모리·디스크 상태가 빌드 시간에 영향을 준다. 앱 설치·실행 시간은 측정에서 제외했다.

iOS는 매회 DerivedData를 초기화했지만 설치된 Pods와 시스템 SDK 캐시는 유지했다. 의존성 설치·서명·배포·Release Archive를 포함한 전체 소요 시간이나 새 Mac의 최초 환경 구성 시간은 아니다. iOS 빌드 단축은 pnpm 전환과 SDK 제거를 합친 결과다. pnpm만으로 네이티브 빌드 시간이 개선됐다는 근거는 확보하지 못했다.

| iOS 빌드 표본 | 1회 | 2회 | 3회 |
|---|---:|---:|---:|
| Yarn + 기존 SDK | 249.593초 | 214.993초 | 238.726초 |
| pnpm + SDK 제거 | 166.523초 | 195.750초 | 206.815초 |

각 n=3 중앙값의 관측 단축률이며 통계적 유의성 검정은 수행하지 않았다. 네이티브 비교군 측정 순서를 무작위화하지 않았고 시스템 캐시·열 상태·외부 부하를 완전히 통제하지 못했다. CI 환경에서 같은 단축률이 재현된다고 일반화하지 않는다.

## Android 시간 개선률을 성과로 쓰지 않은 이유

| Android assembleDevDebug (Metro/Hermes 포함) | Yarn + 기존 SDK | pnpm + SDK 제거 |
|---|---:|---:|
| 개별 실행 시간 | 152.237 / 193.595 / 194.336초 | 143.922 / 283.165 / 138.067초 |
| 중앙값 | 193.595초 | 143.922초 |
| 평균 | 180.056초 | 188.385초 |
| 표본 표준편차 | 24.095초 | 82.134초 |

중앙값은 25.66% 감소했지만 평균은 4.63% 증가했다. 외부 부하와 큰 편차가 관측되어 안정적인 Android 빌드 시간 개선은 확인되지 않았다. 느린 표본을 제외하거나 중앙값 단축률만 골라 이력서에 쓰지 않는다. 대신 모든 실행에서 확인한 Gradle 작업 수 28.94% 감소를 기록한다. 프로젝트 및 네이티브 모듈 빌드 산출물을 초기화하고 task build cache를 비활성화했지만 Gradle 다운로드·artifact transform 캐시는 유지했다.

## 알림 회귀 검증

VoIP 토큰 콜백에 묶여 있던 iOS 일반 알림 등록을 FCM 직접 등록으로 분리했다. iPhone 17 Pro / iOS 26.5 시뮬레이터에서 FCM·APNs 토큰과 로그인 후 deviceId 저장을 확인했다. FCM HTTP v1로 해당 시뮬레이터에 직접 발송한 실제 원격 알림 3건에 대해 실행 중 onMessage 수신, 백그라운드·프로세스 종료 상태의 OS 알림 표시와 탭 후 대상 예약 상세 이동을 확인했다.

모의 알림 주입이 아닌 FCM → APNs Sandbox 전달을 검증했다. 다만 업무 서버의 예약 이벤트 자동 발송, 실행 중 배너·탭, 실기기·운영 APNs는 별도 확인 범위다. 3건의 테스트를 운영 알림 성공률 100%로 표현하지 않는다. SDK·알림 변경은 pnpm 전환과 별도 커밋으로 분리해 선택적 원복이 가능하도록 했다.

## 원본 근거

원본 저장소 접근 권한이 필요한 링크다. 토큰·계정 정보·예약 ID는 이 문서에 포함하지 않았다.

- [이슈 #3](https://github.com/Team-MPS/mps-mental-counsel-app/issues/3): 범위, 수치, 해석과 최종 검증
- [PR #5](https://github.com/Team-MPS/mps-mental-counsel-app/pull/5): pnpm 전환·SDK 제거·빌드 벤치마크
- [PR #7](https://github.com/Team-MPS/mps-mental-counsel-app/pull/7): Android 반복 측정 통계
- [PR #8](https://github.com/Team-MPS/mps-mental-counsel-app/pull/8): 일반 알림 회귀 검증
- [측정 명령·환경·원시 JSON](https://github.com/Team-MPS/mps-mental-counsel-app/tree/f75148f0a3a6a6c2dba62c69d1828ef9ea286753/docs/benchmarks): 병합 시점에 고정한 근거
