# 회의록 할 일 추출기 실습 규칙

- 목적: `requirements.md`의 회의록 할 일 추출 요구사항을 만족한다. 새로운 기능이나 외부 API를 추가하지 않는다.
- 앱 동작 수정은 `src/actions.py`만 허용한다. `tests/`, `requirements.md`, `demo.py`는 변경하지 않는다.
- 하네스 문서는 `AGENTS.md`, `workflow.md`, `.agents/skills/check-meeting/SKILL.md`에 두고, 실행 기록은 `workspace/`에 남긴다.
- 검사는 `python -m unittest discover -s tests -v`와 `python demo.py`를 실제 실행한다. 실패와 미실행을 성공으로 기록하지 않는다.
- 완료 기준: 테스트 8개 통과, demo의 빈 회의록 `[]` 및 할 일 목록 `['자료 조사', '슬라이드 작성']`, 수정 범위 확인, 검토 기록 완료.
- 요구사항 변경, 테스트 변경, 외부 패키지 설치, API 연결, 범위 확대가 필요하면 먼저 학생에게 확인한다.
- 상세 역할과 재시도 순서는 `workflow.md`를 따른다. 이 규칙은 도구 권한을 강제하는 샌드박스가 아니다.
