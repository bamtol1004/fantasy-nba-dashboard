# Fantasy NBA 10-CAT Dashboard

A static NBA Fantasy dashboard with 2024-25, 2025-26, 2026-27 player stats and three-season blended averages.

## Setup
1. Upload the **contents** of this package to the repository root on branch `main` (keep the `.github/workflows/update.yml` folder path).
2. In **Settings > Pages > Build and deployment**, select **GitHub Actions** as Source.
3. Open **Actions > NBA stats refresh and GitHub Pages deploy > Run workflow**.
4. View `https://bamtol1004.github.io/fantasy-nba-dashboard/` after a successful deployment.

## Updating
The workflow runs daily at 01:00 UTC (10:00 Korea time) and downloads `https://boxscorelab.com/downloads/2026-27-player-season-totals.csv`. It validates CSV columns and row count, and keeps the bundled snapshot if download fails. The website reads the deployed CSV on load; the embedded snapshot is a fallback. GitHub Actions cron runs may be delayed. This does **not** automatically refresh Yahoo Fantasy rosters or FA ownership status; Yahoo API integration is a separate future step.

No OAuth secrets should be committed to this public repository.
