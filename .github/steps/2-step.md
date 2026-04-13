## Step 2: Pull Request 리뷰 받기

이제 Copilot의 로컬 리뷰 기능을 테스트하고 활동 웹사이트를 개선하는 변경을 했으니, Pull Request를 생성하고 메인 브랜치에 병합되기 전에 Copilot의 피드백을 받아봅시다. 다른 교사가 하는 것처럼요. Copilot이 Pull Request 과정에서 변경사항을 어떻게 리뷰하는지 살펴봅시다.

### 📖 이론: Pull Request 코드 리뷰

GitHub Copilot은 코드를 분석하고 즉시 적용할 수 있는 실행 가능한 제안과 함께 지능적인 피드백을 제공합니다. 각 코드 리뷰는 요청자의 [Premium Request Unit (PRU)](https://docs.github.com/en/copilot/concepts/billing/copilot-requests)을 하나 소모합니다.

> [!IMPORTANT]
> [코드 리뷰를 책임감 있게](https://docs.github.com/en/copilot/responsible-use/code-review) 사용하세요 - Copilot은 많은 일반적인 보안 문제에 익숙하도록 훈련되었지만, 전용 보안 도구, 가이드라인, 표준을 대체하기 위한 것은 아닙니다. 작업에 맞는 올바른 도구를 사용해 주세요.

**주요 기능:**

- **자동 분석**: 품질, 보안, 성능 문제에 대한 코드 리뷰
- **실행 가능한 제안**: 코드 변경 제안과 함께 구체적인 권장사항 제공
- **통합**: 일반 동료 피드백과 동일하게 GitHub의 네이티브 Pull Request 플로우와 원활하게 작동
- **비차단**: 병합을 차단하지 않고 필수 승인에 포함되지 않는 "Comment" 리뷰 제공
- **커스터마이징 가능**: 팀 표준에 맞춘 커스텀 지침 지원
- **안전**: GitHub의 보안 인프라 내에서 작동

자세한 내용은 [GitHub Copilot 코드 리뷰 문서](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review)를 참고하세요.

### ⌨️ 활동: 리뷰 요청하기

1. 필요하면 다른 웹 브라우저 탭을 열고 이 실습 저장소로 이동합니다.

1. 새 Pull Request를 시작합니다. 다음 정보를 입력하고 **Create pull request** 버튼을 클릭합니다.

   - **compare:** `add-announcement-banner`
   - **target:** `main`
   - **title:** `Add announcement banner`

1. 오른쪽 세부 정보 영역에서 **Reviewers** 메뉴를 찾습니다. **설정 아이콘**을 클릭하여 사용 가능한 리뷰어 목록을 표시하고 **Copilot**을 선택합니다.

   <img width="300" alt="리뷰어 메뉴 스크린샷" src="https://github.com/user-attachments/assets/0f9f2e86-51b7-4542-82a1-afb6a22ab3ca"/>

1. Copilot이 변경사항을 리뷰하고 Pull Request에 코멘트를 추가할 때까지 잠시 기다립니다. 대화 로그에 항목이 추가된 것을 확인합니다.

   <img width="300" alt="새 로그 항목 - copilot에게 리뷰 요청" src="https://github.com/user-attachments/assets/3e522bda-e68e-4469-93f4-a7ad103cca97"/>

   <img width="500" alt="새 로그 항목 - copilot의 PR 요약" src="https://github.com/user-attachments/assets/0a870950-560e-4df8-80d5-2b93f1be99ab"/>

1. 리뷰가 요청되면 Mona가 작업을 확인하고, 피드백을 제공하며, 다음 레슨을 안내합니다.

<details>
<summary>문제가 있나요? 🤷</summary><br/>

- Copilot이 리뷰어 목록에 나타나지 않으면 저장소에서 Copilot이 활성화되어 있는지 확인하세요
- Copilot이 리뷰어 목록에 나타나지 않으면 구독 플랜을 확인하세요. 무료 티어에서는 사용할 수 없습니다.
- 리뷰가 완료되는 데 1-2분 정도 걸릴 수 있습니다.

</details>
