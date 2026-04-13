## Step 4: 리뷰 자동화하기

맞춤형 리뷰가 잘 작동하는 것 같지만, 문제가 있습니다. 기술적으로 필수는 아닙니다. 여러 교사가 활동 웹사이트에 기여할 때 수동으로 Copilot 리뷰를 요청하는 것은 분명 지속 가능하지 않습니다. 모든 Pull Request가 자동으로 Copilot의 피드백을 받기를 원합니다. 특히 협업자들 사이의 프로그래밍 경험 수준이 다양하기 때문입니다. 모든 변경사항에 Copilot 리뷰를 필수로 하는 저장소 규칙 세트를 설정합시다.

### 📖 이론: 자동 리뷰를 위한 저장소 규칙 세트

저장소 규칙 세트를 사용하면 모든 Pull Request에 자동 코드 리뷰를 강제하여, 개발자가 수동으로 리뷰를 요청하거나 문서를 따르는 것을 기억할 필요 없이 일관된 품질 검사를 보장할 수 있습니다.

각 코드 리뷰는 Pull Request 작성자의 [Premium Request Unit (PRU)](https://docs.github.com/en/copilot/concepts/billing/copilot-requests)을 하나 소모합니다.

**적용 옵션:**

- **저장소 수준**: 특정 저장소의 모든 새 Pull Request
- **브랜치별**: 필터와 이름 패턴으로 특정 브랜치 대상
- **조직 수준**: 여러 저장소에 걸쳐 규칙 세트 적용

**주요 이점:**

- 모든 기여에 걸친 일관된 코드 품질
- 수동 개입 없이 자동 적용
- 브랜치 보호 요구사항에 따라 설정 가능
- 기존 GitHub 워크플로우 권한과 통합

자세한 내용은 [저장소 규칙 세트 문서](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)를 참고하세요.

### ⌨️ 활동: 저장소 규칙 세트 만들기

1. 상단 탐색에서 **Settings** 탭을 선택합니다.

1. 왼쪽 탐색에서 **Rules**를 펼치고 **Rulesets**를 선택합니다.

1. **New ruleset** 버튼을 클릭하고 **New branch ruleset** 옵션을 선택합니다.

1. 규칙 세트 이름과 상태를 설정합니다:

   - **Ruleset Name**: `Require Copilot Reviews`
   - **Enforcement Status**: `Active`

1. **Target branches**에서 `main` 브랜치에 대한 보호를 추가합니다.

   1. **Add target**을 클릭하고 **Include default branch**를 선택합니다.
   1. **Add target**을 클릭하고 **Include by pattern**을 선택합니다.
   1. `main`을 입력하고 **Add inclusion pattern** 버튼을 클릭합니다.

   <img width="300" alt="대상 브랜치 스크린샷" src="https://github.com/user-attachments/assets/217f205c-7a61-4ffa-a0a6-7e76ff8d7906"/>

1. **Rules**에서 다음 옵션을 활성화합니다:

   - **Require a pull request before merging**: ☑️
   - **Require conversation resolution before merging**: ☑️
   - **Automatically request Copilot code review**: ☑️

1. 하단으로 스크롤하여 **Create** 버튼을 클릭합니다.

1. 열려있는 Pull Request로 돌아갑니다.

1. 병합 버튼이 비활성화된 것을 확인합니다.

   <img width="300" alt="비활성화된 병합 버튼 스크린샷" src="https://github.com/user-attachments/assets/28e4cb05-f09d-423d-8c77-8f0ec61c73ad"/>

1. Copilot의 현재 및 오래된 피드백에 대해 **Resolve conversation**을 클릭합니다. 실제로 구현할 필요는 없습니다.

1. Pull Request를 병합합니다.

   > 🪧 **참고**: **Merge pull request** 버튼이 활성화되지 않으면, 오래된 코멘트에서 해결되지 않은 대화를 확인하세요.

1. Pull Request가 병합되면 Mona가 작업을 확인하고, 피드백을 제공하며, 최종 리뷰를 게시합니다. 잘했습니다! 모두 완료했습니다! 🎉

### ⌨️ 활동: (선택사항) 자동 리뷰 테스트하기

아직 끝낼 준비가 안 되셨나요? 하드코딩된 공지 배너가 걱정되시나요? 저희도요!

그러면... 고쳐봅시다! 🧑‍🚀🚀

> [!NOTE]
> 새 공지 기능을 "수정"할 필요는 없습니다. 자동 리뷰를 테스트하고 싶다면 간단한 변경만 하고 새 Pull Request를 시작하면 됩니다.

1. VS Code에서 `main` 브랜치로 돌아가고, 병합된 변경사항을 풀하고, `add-announcement-banner` 브랜치를 삭제합니다.

1. `main`에서 다음 이름으로 새 브랜치를 생성합니다.

   ```txt
   enable-editing-announcements
   ```

1. Copilot Chat 패널을 열고 **Agent 모드**인지 확인합니다. 다음 프롬프트를 사용하여 Copilot에 새 공지 기능 업그레이드를 요청합니다.

   > 💡 **팁**: 프리미엄 모델(PRU 사용)은 일반적으로 더 강력하며 후속 프롬프트가 적거나 필요하지 않습니다.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > The Announcement feature should not be hard coded.
   >
   > - Make it driven from the database.
   > - Add a button in the header that opens a dialog window. It lists all existing announcements and has controls to add/modify/delete them.
   > - Only signed in users have access to manage announcements.
   > - Announcements require an expiration date. Start date is optional.
   > - Add an example message to the database initialization.
   > - Don\'t worry about unit testing.
   > - Make it pretty with a good UI/UX experience.
   > ```

1. (선택사항) 애플리케이션을 실행하여 변경사항을 테스트하고 Copilot에 추가 프롬프트를 제공하여 더 다듬습니다.

1. (선택사항) 변경사항을 커밋하기 전에 VS Code에서 로컬 리뷰를 요청합니다.

1. 변경사항을 커밋하고 푸시합니다.

1. 다음 정보로 새 Pull Request를 생성합니다.

   - **compare:** `enable-editing-announcements`
   - **target:** `main`
   - **title:** `Enable Editing Announcements`

1. Copilot이 자동으로 리뷰어로 추가된 것을 확인합니다. 피드백을 기다립니다.

1. (선택사항) Copilot의 코멘트를 처리합니다.

1. Pull Request를 병합합니다.

1. 잘했습니다! 다시 한번 모두 완료했습니다! 🎉
