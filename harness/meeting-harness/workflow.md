# 작성·검사·검토 흐름

1. 학생이 요청과 `requirements.md`의 완료 기준을 확인한다. 이번 실습의 기준은 테스트 8개와 `demo.py` 출력이다.
2. 작성자는 `requirements.md`, `src/actions.py`, 테스트를 읽고 `src/actions.py`만 수정한다. 문제와 변경 내역을 `workspace/change.md`에 남긴 뒤 멈춘다. 테스트나 요구사항을 바꾸지 않는다.
3. 검사자는 `.agents/skills/check-meeting/SKILL.md` 절차에 따라 테스트와 demo를 실제 실행한다. 명령, 종료 코드, 원본 출력, 판정을 `workspace/checks.txt`에 누적한다. 앱 코드와 테스트는 수정하지 않는다.
4. 검토자는 규칙·요구사항·변경·검사 기록 및 `git diff -- src/actions.py tests demo.py requirements.md`, `git status --short`를 확인한다. 앱 코드나 테스트를 수정하지 않고 `workspace/review.md`에 통과/수정 필요/판정 불가와 근거를 남긴다.
5. 수정 필요이면 학생이 구체적 검토 항목을 작성자에게 전달한다. 추가 수정은 최대 2회이며, 계속 실패하면 원인과 다음 행동을 기록하고 중단한다.
6. 학생이 최종 테스트와 demo 출력, 변경 파일을 직접 확인하고 채택한다.

한 CLI에서 역할을 순서대로 전환한다. 독립 서브에이전트는 만들지 않는다. 규칙 문장만으로 파일 수정 권한이 기술적으로 제한되지는 않으므로 실제 변경 목록을 검토한다.
