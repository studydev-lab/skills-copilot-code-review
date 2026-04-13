## Step 3: 리뷰 커스터마이징하기

학교의 코딩 표준은 활동 웹사이트를 유지하는 데 매우 중요합니다. 교사들이 서로 다른 시각적 스타일과 코딩 패턴을 사용하고 있다는 것을 발견했습니다. 교사-협업자들 사이의 다양한 프로그래밍 배경과 우선순위를 고려하여, 학교의 교육 프로그래밍 표준에 맞게 Copilot의 리뷰 동작을 커스터마이징합시다.

### 📖 이론: 저장소 커스텀 지침

저장소 커스텀 지침을 통해 Copilot에 프로젝트 표준과 선호사항에 대한 컨텍스트를 제공할 수 있습니다. 지침 파일을 생성하면 Copilot의 제안이 팀의 규칙을 일관되게 따르고 구체적인 요구사항에 집중하도록 할 수 있습니다. Copilot이 프로젝트를 분석하고 [지침을 생성](https://code.visualstudio.com/docs/copilot/customization/custom-instructions#_generate-an-instructions-file-for-your-workspace)하도록 할 수도 있습니다!

**지침 유형:**

- **저장소 전체 지침**: 저장소의 모든 코드에 적용. 예: `.github/copilot-instructions.md`
- **경로별 지침**: 특정 파일에 적용하여 코드베이스의 다른 부분에 대한 집중 기준 생성. 예: `.github/instructions/NAME.instructions.md`

지침은 자연어와 Markdown 형식으로 작성되며 일반적으로 다음을 포함합니다:

- 보안 요구사항 및 체크리스트
- 코드 표준 및 규칙
- 성능 최적화 우선순위
- 팀별 선호사항 및 스타일 가이드
- 언어별 리뷰 기준

경로별 지침 파일은 특정 파일과 디렉토리를 대상으로 하는 파일 [glob 패턴](https://code.visualstudio.com/docs/editor/glob-patterns)이 포함된 [YAML front matter](https://docs.github.com/en/contributing/writing-for-github-docs/using-yaml-frontmatter)를 포함합니다. 예:

```yaml
---
applyTo: "tests/**/**,docs/*.md"
---
# 테스트 가이드라인 ...
```

```yaml
---
applyTo: "docs/*.md,README.md"
---
# 문서 가이드라인 ...
```

> [!TIP]
> 저장소 [커스텀 지침](https://docs.github.com/en/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot)은 로컬 VS Code 코드 리뷰와 Pull Request 코드 리뷰 모두에서 작동하여 개발 워크플로우 전반에 걸쳐 일관성을 보장합니다.

### ⌨️ 활동: 일반 지침 추가하기

커스텀 지침을 추가하여 Copilot의 리뷰 고려사항을 커스터마이징합시다.

1. VS Code에서 아직 `add-announcement-banner` 브랜치에 있는지 확인합니다.

1. 일반 저장소 가이드라인 파일을 생성합니다.

   파일 위치 및 이름:

   ```txt
   .github/copilot-instructions.md
   ```

   내용:

   ```markdown
   ## Security

   - Validate input sanitization practices.
   - Search for risks that might expose user data.
   - Prefer loading configuration and content from the database instead of hard coded content. If absolutely necessary, load it from environment variables or a non-committed config file.

   ## Code Quality

   - Use consistent naming conventions.
   - Try to reduce code duplication.
   - Prefer maintainability and readability over optimization.
   - If a method is used a lot, try to optimize it for performance.
   - Prefer explicit error handling over silent failures.
   ```

### ⌨️ 활동: 집중 지침 추가하기

프론트엔드와 백엔드에 대한 구체적인 Copilot 리뷰 고려사항을 만들어 봅시다.

1. 프론트엔드 전용 가이드라인 파일을 생성합니다.

   > ❗️ **중요**: 파일별 지침은 `.github/` 폴더가 아닌 `.github/instructions/` 폴더에 넣어야 합니다.

   파일 위치 및 이름:

   ```txt
   .github/instructions/frontend.instructions.md
   ```

   내용:

   ```markdown
   ---
   applyTo: "*.html,*.css,*.js"
   ---

   ## Frontend Guidelines

   - Use accessibility attributes (alt text, aria labels) and color schemes.
   - Use responsive design for compatibility with mobile devices.
   - Validate HTML structure and semantic elements
   ```

1. 백엔드 전용 가이드라인 파일을 생성합니다.

   파일 위치 및 이름:

   ```txt
   .github/instructions/backend.instructions.md
   ```

   내용:

   ```markdown
   ---
   applyTo: "backend/**/*,*.py"
   ---

   ## Backend Guidelines

   - All API endpoints must be defined in the `routers` folder.
   - Load example database content from the `database.py` file.
   - Error handling is only logged on the server. Do not propagate to the frontend.
   - Ensure all APIs are explained in the documentation.
   - Verify changes in the backend are reflected in the frontend (`src/static/**`). If possible breaking changes are found, mention them to the developer.
   ```

1. 지침 파일을 커밋하고 푸시합니다.

> [!TIP]
> VS Code에는 지침을 관리하는 내장 명령이 있습니다. 명령 팔레트를 열고 `instructions`를 검색해 보세요.

### ⌨️ 활동: 다시 리뷰 요청하기

새 지침이 정의되었으니, Copilot은 이제 프로젝트에서 중요한 것이 무엇인지 더 잘 알게 되었습니다. 다시 리뷰를 요청합시다.

1. VS Code에서 지침이 커밋되고 저장소에 푸시되었는지 확인합니다.

1. 웹 브라우저에서 최근 생성한 Pull Request로 돌아갑니다.

1. 오른쪽 상단에서 **Reviewers** 메뉴와 **Copilot** 옆의 **리뷰 재요청** 버튼을 찾습니다. 클릭하고 Copilot이 Pull Request에 코멘트를 추가할 때까지 잠시 기다립니다.

   <img width="300" alt="리뷰 재요청 버튼 스크린샷" src="https://github.com/user-attachments/assets/c45aa8de-278d-46e7-bfe2-2dc6b574e11e"/>

   > 🪧 **참고:** 새 커밋을 푸시한 직후에는 버튼이 나타나기까지 잠시 기다리거나 페이지를 새로고침해야 할 수 있습니다.

1. Copilot의 피드백이 이전 리뷰와 다른 것을 확인합니다.

1. 리뷰가 요청되면 Mona가 작업을 확인하고, 피드백을 제공하며, 다음 레슨을 안내합니다.

<details>
<summary>문제가 있나요? 🤷</summary><br/>

- 지침 파일이 올바른 디렉토리에 있는지 다시 확인하세요.
- 커밋되지 않은 변경사항이 있으면 커밋하고 푸시하세요.
- 리뷰 재요청 버튼이 보이지 않으면 Pull Request 페이지를 새로고침해 보세요.

</details>
