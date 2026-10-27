# NBA Fantasy 10-CAT Dashboard — Yahoo API 승인 전

GitHub Pages 정적 대시보드입니다. `index.html`에서 2026–27 CSV를 `data/2026-27-player-season-totals.csv`에서 자동 로딩합니다. 로스터는 수동 관리하며 FA 여부는 Yahoo API 전까지 확인되지 않습니다.

GitHub에 전체 폴더 내용을 업로드하세요 (`.github/workflows/update.yml` 포함). Settings > Pages > Source: GitHub Actions. Actions 탭에서 워크플로 실행.

주의: 현재 CSV 다운로드 URL은 검증되지 않았습니다. 다운로드 실패 시 기존 CSV로 배포되며 데이터가 갱신된 것은 아닙니다. GitHub Actions 로그에서 `Updated CSV` 출력 확인이 필요합니다.
