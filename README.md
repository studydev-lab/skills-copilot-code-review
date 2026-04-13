# GitHub Copilot 코드 리뷰

_GitHub Copilot 코드 리뷰를 활용하여 코드 품질을 높이고 프로덕션에 도달하기 전에 문제를 발견하세요._

## 환영합니다

- **대상**: 코드 리뷰를 확장하고 싶은 GitHub Copilot에 익숙한 개발자
- **배울 내용**: GitHub Copilot을 활용한 자동 코드 리뷰, 리뷰 기준 커스터마이징, 자동 리뷰 설정 방법
- **만들 것**: Mergington 고등학교 교외 활동 웹사이트를 업데이트하고, Copilot이 자동으로 Pull Request를 리뷰하도록 설정하여 더 많은 교사가 기여할 수 있도록 합니다.
- **사전 요구사항**:

  - GitHub Copilot 구독 (유료 플랜 필요)
  - Pull Request에서 코드 리뷰에 대한 이해
  - Codespaces에 대한 이해, 또는 [Codespaces로 코딩하기](https://github.com/skills-kr/code-with-codespaces) 실습
  - GitHub Copilot에 대한 이해, 또는 [GitHub Copilot 시작하기](https://github.com/skills-kr/getting-started-with-github-copilot) 실습

- **소요 시간**: 이 실습은 1시간 이내에 완료할 수 있습니다.

이 실습에서 다음을 수행합니다:

1. VS Code에서 GitHub Copilot을 사용하여 즉각적인 피드백으로 코드 리뷰하기
1. Pull Request에서 Copilot 코드 리뷰 요청하기
1. 저장소별 지침으로 Copilot의 리뷰 기준 커스터마이징하기
1. 저장소 규칙 세트를 사용하여 자동 코드 리뷰 설정하기

### 이 실습을 시작하는 방법

실습을 내 계정으로 복사한 뒤, Octocat(Mona)이 첫 번째 레슨을 준비할 때까지 **약 20초** 기다린 후 **페이지를 새로고침**하세요.

[![](https://img.shields.io/badge/실습%20복사-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/new?template_owner=skills-kr&template_name=copilot-code-review&owner=%40me&name=skills-copilot-code-review&description=실습:+GitHub+Copilot+코드+리뷰&visibility=public)

<details>
<summary>문제가 있나요? 🤷</summary><br/>

실습을 복사할 때 다음 설정을 권장합니다:

- 소유자(owner)는 개인 계정 또는 조직(organization)을 선택하세요.

- 비공개 저장소는 Actions 사용 시간이 소모되므로 공개 저장소를 만드는 것을 권장합니다.

20초 후에도 실습이 준비되지 않으면 [Actions](../../actions) 탭을 확인하세요.

- 작업이 실행 중인지 확인하세요. 때로는 조금 더 오래 걸릴 수 있습니다.

- 페이지에 실패한 작업이 표시되면 이슈를 제출해 주세요. 버그를 발견하셨네요! 🐛

</details>

---

> **참고**: 이 실습은 [skills/copilot-code-review](https://github.com/skills/copilot-code-review)를 기반으로 한글화하고, [🏆 GitHub Skills Workshop Dashboard](https://github-skills.studydev.com)와 연계되어 있습니다.

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)
