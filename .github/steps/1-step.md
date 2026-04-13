## Step 1: VS Code에서 리뷰 요청하기

Mergington 고등학교에는 교외 활동 웹사이트가 있습니다. 지난 몇 달간 많은 기능을 추가했고, 동료 교직원과 학생들이 점점 더 많이 사용하게 되었습니다.

이제 여러 교사가 새로운 기능 개발을 돕고 싶어합니다. 좋은 일이지만, 에너지는 한정되어 있고 변경사항을 리뷰할 시간이 없으면 애플리케이션이 지저분해질까 걱정됩니다. 리뷰 가용성을 확장하기 위해 **GitHub Copilot 코드 리뷰**를 구현합시다!

Copilot으로 자동 코드 리뷰를 구현하기 전에, 먼저 VS Code에서 로컬 리뷰를 시도해 봅시다. 이를 통해 더 잘 이해하고, 리뷰 기준을 만들고, 교사-협업자들이 기여를 시작할 때 일관된 피드백을 받을 수 있습니다.

### 📖 이론: GitHub Copilot 로컬 코드 리뷰

GitHub Copilot은 VS Code에서 직접 코드를 리뷰하여 커밋하지 않은 변경사항에 대해 즉각적인 피드백을 제공합니다. Pull Request의 피드백과 유사한 코멘트도 추가합니다! 이 로컬 리뷰 기능을 통해 개발자는 버전 관리에 도달하기 전에 문제를 발견하여 처음부터 코드 품질을 향상시킬 수 있습니다. 그리고 부끄러운 오타도 잡을 수 있죠! 😅

주요 기능:

- 커밋하지 않은 변경사항의 **로컬 분석**
- **코드 품질 및 스타일** 권장사항
- 일반적인 보안 취약점 **탐지**
- **성능 최적화** 제안

이 즉각적인 피드백은 개발 과정 초기에 문제를 식별하고 수정하여 Pull Request에 도달하기 전에 코드를 더 견고하게 만드는 데 도움됩니다.

## ⌨️ 활동: 교외 활동 사이트 살펴보기

개발과 리뷰를 시작하기 전에, 현재 사이트를 이해하는 시간을 가집시다.

1. 아래 버튼을 우클릭하여 새 탭에서 **Create Codespace** 페이지를 엽니다. 기본 구성을 사용하세요.

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. 환경이 준비될 때까지 잠시 기다립니다. 모든 요구사항과 서비스가 자동으로 설치됩니다.

1. **GitHub Copilot**과 **Python** 확장이 설치되고 활성화되어 있는지 확인합니다.

   <img width="300" alt="VS Code용 copilot 확장" src="https://github.com/user-attachments/assets/ef1ef984-17fc-4b20-a9a6-65a866def468" /><br/>
   <img width="300" alt="VS Code용 python 확장" src="https://github.com/user-attachments/assets/3040c0f5-1658-47e2-a439-20504a384f77" />

1. 애플리케이션을 실행해 봅니다. 왼쪽 사이드바에서 **실행 및 디버그** 탭을 선택한 후 **디버깅 시작** 아이콘을 누릅니다.

   <img width="300" alt="실행 및 디버그" src="https://github.com/user-attachments/assets/50b27f2a-5eab-4827-9343-ab5bce62357e" />

   <details>
   <summary>🤷 문제가 있나요?</summary><br/>

   **실행 및 디버그** 영역이 비어있다면 VS Code를 새로고침해 보세요: 명령 팔레트(`Ctrl`+`Shift`+`P`)를 열고 `Developer: Reload Window`를 검색합니다.

   <img width="300" alt="빈 실행 및 디버그 패널" src="https://github.com/user-attachments/assets/0dbf1407-3a97-401a-a630-f462697082d6" />

   </details>

1. **Ports** 탭에서 웹페이지 주소를 찾아 열고 실행 중인지 확인합니다.

   <img width="350" alt="ports 탭" src="https://github.com/user-attachments/assets/8d24d6b5-202d-4109-8174-2f0d1e4d8d44" />

   ![Mergington 고등학교 웹앱 스크린샷](https://github.com/user-attachments/assets/5e1e7c1e-1b0e-4378-a5af-a266763e6544)

### ⌨️ 활동: Copilot에 리뷰 요청하기

교사가 공지사항을 게시할 수 있는 간단한 배너 기능을 추가한 후 Copilot에 피드백을 요청합시다.

1. VS Code에서 다음 이름으로 새 브랜치를 생성합니다.

   ```txt
   add-announcement-banner
   ```

1. `src/static/index.html` 파일을 엽니다. `<body>` 태그 뒤에 다음을 추가합니다.

   ```html
   <div class="announcement-banner">
     📢 Activity registration is open until the end of the month. Don\'t lose your spot!
   </div>
   ```

1. `src/static/styles.css` 파일을 엽니다. 끝에 다음을 추가합니다.

   ```css
   .announcement-banner {
     background-color: #4caf50;
     color: white;
     text-align: center;
     padding: 15px;
     font-weight: bold;
   }
   ```

1. (선택사항) 실행 중인 앱을 새로고침하여 변경사항을 확인합니다.

   <img width="400" alt="공지 배너가 추가된 사이트 스크린샷" src="https://github.com/user-attachments/assets/39de7fe0-58f2-4eba-a163-d3037b2b3b06"/>

1. VS Code에서 소스 컨트롤 패널을 열고 커밋하지 않은 변경사항이 있는지 확인합니다.

1. **Changes** 섹션 위에 마우스를 올려 아이콘들을 표시합니다. **Code Review** 버튼을 클릭하고 Copilot이 코멘트를 추가할 때까지 잠시 기다립니다.

   <img width="300" alt="코드 리뷰 버튼 스크린샷" src="https://github.com/user-attachments/assets/6c52d550-d67b-4af9-99dd-e181695a4933"/>

   > 💡 **팁:** `unstaged changes(스테이지되지 않은 변경)`, `staged changes(스테이지된 변경)`, `uncommitted changes(커밋되지 않은 변경)` 3가지 리뷰 레벨을 사용할 수 있습니다

1. **Comments** 패널을 펼쳐 Copilot의 리뷰 피드백 목록을 확인합니다.

   <img width="300" alt="Copilot 코멘트가 있는 문제 제어판 스크린샷" src="https://github.com/user-attachments/assets/64c5efb6-9071-4511-b2a2-2dc85c9e929b"/>

1. **Apply** 또는 **Discard** 버튼을 사용하여 Copilot의 피드백을 처리합니다.

   <img width="300" alt="피드백 처리 버튼이 있는 인라인 코멘트 스크린샷" src="https://github.com/user-attachments/assets/aef73097-acaf-4f5b-a52f-52a142bb413f"/>

1. 공지 관련 변경사항을 `add-announcement-banner` 브랜치에 커밋하고 푸시합니다.

1. 변경사항이 푸시되면 Mona가 작업을 확인하고, 피드백을 제공하며, 다음 레슨을 안내합니다.

<details>
<summary>문제가 있나요? 🤷</summary><br/>

- VS Code의 Copilot 리뷰는 커밋하지 않은 변경사항만 고려합니다. 리뷰를 요청하기 전에 커밋하지 마세요.
- Copilot이 리뷰 피드백을 제공하지 않으면, 그룹(unstaged, staged, uncommitted)에 맞는 올바른 리뷰 버튼을 클릭했는지 확인하세요.
- Copilot이 변경사항을 인식하지 못하면, 먼저 파일을 저장했는지 확인하세요.

</details>
