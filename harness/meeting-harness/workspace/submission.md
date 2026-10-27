# 회의록 하네스 실습 제출 정리

## 실습 결과

- 최초 상태: `workspace/baseline.txt` — 테스트 8개 중 4개 통과, 2개 실패, 2개 오류.
- 실패 예시: 빈 문자열 입력에서 기대 `[]`, 실제 `ValueError`; `workspace/baseline-analysis.md` 참조.
- 하네스: `AGENTS.md`, `workflow.md`, `.agents/skills/check-meeting/SKILL.md`.
- 작성 변경: `src/actions.py`만 수정. `workspace/change.md`에 설명.
- 검사: `workspace/checks.txt` Run 1과 CLI 스킬 호출 Run 2 — 모두 테스트 8개 통과, demo 기대 출력 확인.
- 검토: `workspace/review.md` — 요구사항과 수정 범위 통과.

## 남은 학생 확인

1. Codex CLI에서 `$check-meeting`을 호출했고 스킬 발견과 Run 2 기록을 확인했다. 제출 전 `workspace/checks.txt`의 명령·종료 코드·출력을 확인한다.
2. `git status --short`, 테스트와 demo 출력을 직접 확인하고 변경을 채택한다.
3. 아래 개인 회고 초안을 본인의 실제 경험에 맞게 검토하고 수업 제출 양식에 옮긴다. 안내에 언급된 `03_제출_양식.md`는 제공된 작업 파일에서 찾지 못해 이 요약을 대신 작성했다.

## 개인 회고 초안 — 학생 검토 필요

이번 실습에서는 코드를 고치기 전에 테스트를 실행해 최초 실패를 기록했다. 빈 문자열 입력에서 `[]`가 나와야 하지만 `ValueError`가 발생한 사례를 요구사항 1번과 연결하니 수정할 부분이 분명해졌다. `AGENTS.md`에 앱 코드 수정 범위를 `src/actions.py`로 정하고, `workflow.md`에 작성·검사·검토 순서를 적어 두니 어떤 파일을 바꿔야 하고 무엇을 증거로 남겨야 하는지 확인할 수 있었다.

수정 후에는 테스트 8개와 `demo.py`가 통과했고, 명령·종료 코드·출력을 `workspace/checks.txt`에 남겼다. 이 기록 덕분에 “고쳤다”는 설명과 실제 검증 결과를 구분할 수 있었다. 테스트 통과는 준비된 사례의 결과이므로 모든 입력에서 오류가 없다는 뜻으로 받아들이지 않겠다. 다음 작업에서도 최초 상태 기록 → 범위에 맞는 수정 → 실제 검사 → 변경 범위 검토의 순서를 따르겠다.

처음 `$check-meeting` CLI 호출은 프로젝트 파일 전송에 대한 승인 검토로 실행 전에 중단됐다. 실습 폴더의 전송을 승인받은 뒤 VS Code에서 연 폴더를 대상으로 CLI를 호출했고, 스킬 발견과 테스트 8개 및 demo 통과를 Run 2에 남겼다.
