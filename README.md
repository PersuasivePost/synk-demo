# Automated Vulnerability Scanning for Dependencies and Containers Using Snyk

DevOps Theory Internal Assessment · Group 71
Ashish Kumar (16010123084) · Ashvatth Joshi (16010123085)

## What this project shows

A small Node.js/Express app is built twice from **identical code**:

| | `before/` (vulnerable) | `after/` (remediated) |
|---|---|---|
| npm packages | old pinned versions (express 4.16.0, lodash 4.17.4, jsonwebtoken 8.3.0, ejs 2.5.7, axios 0.18.0, moment 2.19.1, minimist 1.2.0) | upgraded to current releases |
| Docker base image | `node:14` (end-of-life, Debian buster) | `node:22-alpine`, non-root user |

Snyk scans **both the dependencies and the Docker image** for each version. The
difference in vulnerability counts is the result of the case study: finding problems early
(shift-left security) and proving that the fixes worked.

> The `before/` app is intentionally vulnerable. Run it locally only. Never deploy it.

```
snyk-demo/
├── before/            vulnerable app (package.json, server.js, views/, Dockerfile, package-lock.json)
├── after/             remediated app (same code, upgraded deps + base image)
├── scripts/
│   ├── scan.sh        runs both Snyk scans for one version, saves JSON reports
│   └── compare.py     builds the before/after table and chart from the reports
├── ci/snyk.yml        GitHub Actions workflow (copied into .github/ by setup.sh)
├── results/           reports, summary.md, comparison.png
└── setup.sh           creates the hidden files (.github/, .gitignore)
```

## Prerequisites

- Node.js 18+ and npm
- Docker (running)
- Python 3 with matplotlib (`pip install matplotlib`) for the chart
- A free Snyk account: https://app.snyk.io

## 1. One-time setup

```bash
bash setup.sh
npm install -g snyk
snyk auth
```

## 2. Scan the vulnerable version

```bash
bash scripts/scan.sh before
```

Snyk prints every vulnerability with its CVE/Snyk ID, severity, the affected package, and the
version that fixes it. For the image it also prints base-image upgrade recommendations.
Take screenshots of both outputs.

## 3. Remediate (this is already done in `after/`)

The fixes are exactly what Snyk recommends:

1. **Dependencies:** bump each package to the fixed version (see `before/package.json` vs `after/package.json`).
2. **Base image:** change `FROM node:14` to `FROM node:22-alpine`, and run as a non-root user.

Show the diff, which is the fix in a single command:

```bash
diff before/package.json after/package.json
diff before/Dockerfile after/Dockerfile
```

## 4. Rescan the remediated version

```bash
bash scripts/scan.sh after
```

## 5. Compare

```bash
python3 scripts/compare.py
```

This prints a Markdown table and creates `results/comparison.png`. Put both in your report.

## 6. Automate it in CI (GitHub Actions)

1. Create a GitHub repo and push this project.
2. Snyk dashboard → Account settings → **Auth Token** → copy.
3. GitHub repo → Settings → Secrets and variables → Actions → new secret `SNYK_TOKEN`.
4. Push. In the Actions tab you get two jobs:
   - **Snyk gate - remediated app:** fails the build on any HIGH/CRITICAL finding, so it is green only when the fixes hold.
   - **Snyk report - vulnerable app:** expected to find issues; it never fails the workflow.

### Optional: monitor continuously

```bash
cd before && snyk monitor
cd ../after && snyk monitor
```

The projects appear in the Snyk dashboard and Snyk alerts you when new CVEs are published.

## Run the app locally (optional)

```bash
cd after
npm ci
npm start            # http://localhost:3000
```

Endpoints: `/`, `/health`, `/api/products`, `/api/time`, `/api/token`, `/api/ping`.

## Demo script (viva)

1. Show the two folders: same `server.js`, different `package.json` and `Dockerfile`.
2. Run `bash scripts/scan.sh before`: show critical/high CVEs and the image findings.
3. Show the `diff` of the two package.json / Dockerfile files.
4. Run `bash scripts/scan.sh after`: show the counts dropping.
5. Show `results/comparison.png`.
6. Show the Actions tab: the gate job is green and the vulnerable job reports issues.

Keep screenshots and the JSON reports as a fallback in case there is no internet at the venue.

## Troubleshooting

- **`snyk: command not found`**: reinstall with `npm install -g snyk`, or open a new terminal.
- **`Authentication needed`**: run `snyk auth` again (locally) or check the `SNYK_TOKEN` secret (CI).
- **Container scan fails to find the image**: make sure Docker is running and `docker build` succeeded.
- **Free plan limit reached**: the free plan allows a limited number of tests per month. Don't re-run scans needlessly; reuse the saved JSON reports.
- **Hidden folders missing after unzip**: extract with `unzip` in the terminal, not the file manager, then run `bash setup.sh`.
