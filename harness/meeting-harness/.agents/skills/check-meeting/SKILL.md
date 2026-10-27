---
name: check-meeting
description: 회의록 추출기 변경 후 요구사항과 테스트를 검증할 때 사용한다.
---

# 입력

- `requirements.md`, `AGENTS.md`, `workflow.md`, `src/actions.py`, `tests/test_actions.py`, `demo.py`
- 이전 실행 기록 `workspace/checks.txt`가 있으면 그 내용을 보존한다.

# 절차

1. 요구사항과 완료 기준, 수정 가능 범위를 읽는다.
2. `python -m unittest discover -s tests -v`를 실제 실행하고 종료 코드 및 원본 출력을 확보한다.
3. `python demo.py`를 실제 실행하고 종료 코드 및 원본 출력을 확보한다.
4. `workspace/checks.txt`에 실행 번호를 붙여 각 명령, 종료 코드, 원본 출력, 통과/실패/미실행 판정과 실패 원인을 추가한다. 기존 기록을 덮어쓰지 않는다.
5. 두 명령이 모두 성공하고 테스트 8개 및 demo 기대 출력이 확인될 때만 전체 통과로 판정한다.

# 산출물과 중단 조건

- 산출물: 누적 검사 기록 `workspace/checks.txt`와 짧은 결과 보고.
- 명령을 실행하지 못하면 원인과 미실행 상태를 남기고 멈춘다. 테스트 실패를 통과로 표시하지 않는다.
- 이 스킬은 앱 코드, 테스트, 요구사항 또는 기준을 고치지 않는다.
