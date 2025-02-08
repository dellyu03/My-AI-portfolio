[seunghwan08.log](https://velog.io/@youjacha082/posts)

로그인

[seunghwan08.log](https://velog.io/@youjacha082/posts)

로그인

# 재설정만 해주고 넘어갔던 그놈 환경변수(path)에 대해

[Yoo Seung Hwan](https://velog.io/@youjacha082/posts)·2024년 6월 30일

팔로우

0

[CS](https://velog.io/tags/CS) [군대](https://velog.io/tags/%EA%B5%B0%EB%8C%80) [코딩](https://velog.io/tags/%EC%BD%94%EB%94%A9) [환경변수](https://velog.io/tags/%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98)

0

[새로운 프로그램을 설치 했는데...](https://velog.io/@youjacha082/%EC%84%A4%EC%B9%98%EB%A7%8C-%ED%95%98%EB%A9%B4-%EB%82%98%EC%98%A4%EB%8A%94-%EA%B7%B8%EB%86%88-%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98%EC%97%90-%EB%8C%80%ED%95%B4#%EC%83%88%EB%A1%9C%EC%9A%B4-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%EC%9D%84-%EC%84%A4%EC%B9%98-%ED%96%88%EB%8A%94%EB%8D%B0)

[환경변수란?](https://velog.io/@youjacha082/%EC%84%A4%EC%B9%98%EB%A7%8C-%ED%95%98%EB%A9%B4-%EB%82%98%EC%98%A4%EB%8A%94-%EA%B7%B8%EB%86%88-%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98%EC%97%90-%EB%8C%80%ED%95%B4#%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98%EB%9E%80)

[환경변수의 기능](https://velog.io/@youjacha082/%EC%84%A4%EC%B9%98%EB%A7%8C-%ED%95%98%EB%A9%B4-%EB%82%98%EC%98%A4%EB%8A%94-%EA%B7%B8%EB%86%88-%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98%EC%97%90-%EB%8C%80%ED%95%B4#%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98%EC%9D%98-%EA%B8%B0%EB%8A%A5)

[1) 시스템 설정 관리](https://velog.io/@youjacha082/%EC%84%A4%EC%B9%98%EB%A7%8C-%ED%95%98%EB%A9%B4-%EB%82%98%EC%98%A4%EB%8A%94-%EA%B7%B8%EB%86%88-%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98%EC%97%90-%EB%8C%80%ED%95%B4#1-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EC%84%A4%EC%A0%95-%EA%B4%80%EB%A6%AC)

[2) 프로그램 구성](https://velog.io/@youjacha082/%EC%84%A4%EC%B9%98%EB%A7%8C-%ED%95%98%EB%A9%B4-%EB%82%98%EC%98%A4%EB%8A%94-%EA%B7%B8%EB%86%88-%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98%EC%97%90-%EB%8C%80%ED%95%B4#2-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-%EA%B5%AC%EC%84%B1)

[3) 보안](https://velog.io/@youjacha082/%EC%84%A4%EC%B9%98%EB%A7%8C-%ED%95%98%EB%A9%B4-%EB%82%98%EC%98%A4%EB%8A%94-%EA%B7%B8%EB%86%88-%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98%EC%97%90-%EB%8C%80%ED%95%B4#3-%EB%B3%B4%EC%95%88)

[환경변수 path](https://velog.io/@youjacha082/%EC%84%A4%EC%B9%98%EB%A7%8C-%ED%95%98%EB%A9%B4-%EB%82%98%EC%98%A4%EB%8A%94-%EA%B7%B8%EB%86%88-%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98%EC%97%90-%EB%8C%80%ED%95%B4#%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98-path)

[참고](https://velog.io/@youjacha082/%EC%84%A4%EC%B9%98%EB%A7%8C-%ED%95%98%EB%A9%B4-%EB%82%98%EC%98%A4%EB%8A%94-%EA%B7%B8%EB%86%88-%ED%99%98%EA%B2%BD%EB%B3%80%EC%88%98%EC%97%90-%EB%8C%80%ED%95%B4#%EC%B0%B8%EA%B3%A0)

## [CS 공부](https://velog.io/@youjacha082/series/CS-%EA%B3%B5%EB%B6%80)

목록 보기

1/1

![post-thumbnail](https://velog.velcdn.com/images/youjacha082/post/348032a1-42c6-4e94-bab0-2c12cb53d068/image.png)

# 새로운 프로그램을 설치 했는데...

개발 공부를 하다 보면 새로운 프로그램이나 라이브러리를 자주 설치한다.

분명 책이나 강의에서 하라는 대로 설치했는데 명령어를 찾을 수 없다든가 유효한 경로가 아니라는 등의 오류가 나오곤 한다.

검색해보면 대부분 환경변수 설정이 문제이며 환경변수를 다시 설정해보라고 한다.

이 글에서는 항상 프로그램의 설치와 작동에 급급해 적당히 해결하고 넘어갔던 환경변수에 대해 알아보고자 한다.

# 환경변수란?

> 프로세스가 컴퓨터에서 동작하는 방식에 영향을 미치는 동적인 값들의 모임

환경 변수의 정의는 위와 같다. 코딩에서 변수는 특정한 값들을 저장한 공간을 의미하는 것처럼 환경 변수는 컴퓨터 동작에 필요한 값들을 저장해 놓은 변수이다.

변수명과 값으로 구성되며 시스템의 기본 정보를 저장해 놓는다.

적용 범위에 따라 시스템 전반에 걸쳐 적용되는 **시스템 환경변수** 와 사용자 계정내에서만 적용되는 **사용자 환경변수** 로 구분된다.

쉽게 말해 환경 변수는

> 프로세스 실행에 필요한 어떤한 정보를 쉽게 접근할 수 있게 변수로 저장해 놓은것

예를 들어 실행파일의 위치라던가 사용자 계정의 정보, 운영체제가 설치된 파일의 경로 등을 변수로 저장해둔것!

# 환경변수의 기능

### 1) 시스템 설정 관리

운영 체제 설정이나 시스템 경로를 포함하여 시스템 전반적인 환경을 관리하는 데 사용

### 2) 프로그램 구성

여러 응용 프로그램이 동일한 환경 변수를 사용하여 동작 방식이나 구성을 조정할 수 있도록 함

### 3) 보안

중요한 데이터를 환경 변수에 저장하여 코드에서 하드코딩하지 않고 접근할 수 있도록 함

# 환경변수 path

여느 프로그램들의 변수가 다양한것처럼 환경변수 또한 다양한 변수가 존재한다.

그 중 설치시 오류를 내는 대부분의 경우 환경변수 중 path의설정이 잘못된 경우가 대부분이다.

> **path** 란? 운영체제에서 실행 가능한 프로그램들의 경로를 지정해 놓은 환경변수

path 덕분에 cmd나 터미널의 어떤 위치에서든 프로그램을 실행 요청해도 path 경로에 저장되어 있으면 해당 코드를 실행 시킬 수 있음

만약 path가 잘못되면 해당하는 명령어를 찾지 못해 unknown command라는 결과를 낸다.

### 참고

[https://gliver.tistory.com/43](https://gliver.tistory.com/43)

[https://medium.com/chingu/an-introduction-to-environment-variables-and-how-to-use-them-f602f66d15fa](https://medium.com/chingu/an-introduction-to-environment-variables-and-how-to-use-them-f602f66d15fa)

[https://www.youtube.com/watch?v=QY0Cui1cSUQ](https://www.youtube.com/watch?v=QY0Cui1cSUQ)

[![profile](https://velog.velcdn.com/images/youjacha082/profile/939962f6-1bc1-4fb8-a885-a06e09d33e42/image.png)](https://velog.io/@youjacha082/posts)

[Yoo Seung Hwan](https://velog.io/@youjacha082/posts)

습관이 나를 만든다.

팔로우

#### 0개의 댓글

댓글 작성

#### 관련 채용 정보

[![](https://static.wanted.co.kr/images/company/282/2fbcqmxgdmrro4bs__400_400.jpg)](https://www.wanted.co.kr/wd/260529?client_id=KK03NuM8GrpMbYP7vrf8FxsI)

[![](https://static.wanted.co.kr/images/wdes/0_5.a483934b.png)](https://www.wanted.co.kr/wd/260529?client_id=KK03NuM8GrpMbYP7vrf8FxsI)

[백패커](https://www.wanted.co.kr/wd/260529?client_id=KK03NuM8GrpMbYP7vrf8FxsI)

[\[아이디어스\] 웹서비스 프론트엔드 개발자 (1~5년)](https://www.wanted.co.kr/wd/260529?client_id=KK03NuM8GrpMbYP7vrf8FxsI)

[![](https://static.wanted.co.kr/images/company/2400/atafv8ztzucoecwc__400_400.jpg)](https://www.wanted.co.kr/wd/259152?client_id=KK03NuM8GrpMbYP7vrf8FxsI)

[![](https://static.wanted.co.kr/images/wdes/0_5.6e8f5df8.jpg)](https://www.wanted.co.kr/wd/259152?client_id=KK03NuM8GrpMbYP7vrf8FxsI)

[씨제이이엔엠(CJ ENM)](https://www.wanted.co.kr/wd/259152?client_id=KK03NuM8GrpMbYP7vrf8FxsI)

[\[Mnet Plus\] 백엔드 개발](https://www.wanted.co.kr/wd/259152?client_id=KK03NuM8GrpMbYP7vrf8FxsI)

[![](https://static.wanted.co.kr/images/company/3438/13626_2_0.d80a2070__400_400.jpg)](https://www.wanted.co.kr/wd/254015?client_id=KK03NuM8GrpMbYP7vrf8FxsI)

[![](https://static.wanted.co.kr/images/wdes/0_5.fdc41065.jpg)](https://www.wanted.co.kr/wd/254015?client_id=KK03NuM8GrpMbYP7vrf8FxsI)

[기아](https://www.wanted.co.kr/wd/254015?client_id=KK03NuM8GrpMbYP7vrf8FxsI)

[\[ICT\] Frontend Developer](https://www.wanted.co.kr/wd/254015?client_id=KK03NuM8GrpMbYP7vrf8FxsI)

[![](https://static.wanted.co.kr/images/company/3438/13626_2_0.d80a2070__400_400.jpg)](https://www.wanted.co.kr/wd/254014?client_id=KK03NuM8GrpMbYP7vrf8FxsI)

[![](https://static.wanted.co.kr/images/wdes/0_5.fdc41065.jpg)](https://www.wanted.co.kr/wd/254014?client_id=KK03NuM8GrpMbYP7vrf8FxsI)

[기아](https://www.wanted.co.kr/wd/254014?client_id=KK03NuM8GrpMbYP7vrf8FxsI)

[\[ICT\] Backend Developer](https://www.wanted.co.kr/wd/254014?client_id=KK03NuM8GrpMbYP7vrf8FxsI)

[![Powered by GraphCDN, the GraphQL CDN](https://graphcdn.io/badge.svg)](https://graphcdn.io/?ref=powered-by)