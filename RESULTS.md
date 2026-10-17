ashserver@vasant:~/AshWorks/synk-demo$ cd ~/AshWorks/synk-demo/before && snyk test | tail -n 15
│   Project name:      snyk-demo-before                             │
│   Project path:      /home/ashserver/AshWorks/synk-demo/before    │
│   Target file:       package-lock.json                            │
│                                                                   │
│   Total security issues: 65                                       │
│   Ignored: 0 [ 0 CRITICAL  0 HIGH  0 MEDIUM  0 LOW ]              │
│   Open   : 65 [ 2 CRITICAL  22 HIGH  37 MEDIUM  4 LOW ]           │
╰───────────────────────────────────────────────────────────────────╯


💡 Tip

   To view ignored issues, use the --include-ignores option.
                                                            

ashserver@vasant:~/AshWorks/synk-demo/before$ snyk container test snyk-demo:before --file=Dockerfile --exclude-app-vulns | tail -n 25
^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D\ Analyzing container dependencies f
Base image:        node:14
Licenses:          enabled

Tested 413 dependencies for known issues, found 545 issues.

Base Image  Vulnerabilities  Severity
node:14     545              8 critical, 77 high, 76 medium, 384 low

Recommendations for base image upgrade:

Major upgrades
Base Image    Vulnerabilities  Severity
node:24.19.0  694              6 critical, 39 high, 42 medium, 607 low

Debian 10 is no longer supported by the Debian maintainers. Vulnerability detection may be affected by a lack of security updates.

Pro tip: use `--exclude-base-image-vulns` to exclude from display Docker base image vulnerabilities.

Snyk found some vulnerabilities in your image applications (Snyk searches for these vulnerabilities by default). See https://snyk.co/app-vulns for more information.

To remove these messages in the future, please run `snyk config set disableSuggestions=true`

Learn more: https://docs.snyk.io/products/snyk-container/getting-around-the-snyk-container-ui/base-image-detection


ashserver@vasant:~/AshWorks/synk-demo/before$ cd ../after && snyk test | tail -n 15
│   Organization:      persuasivepost                              │
│   Test type:         Software Composition Analysis               │
│   Project name:      snyk-demo-after                             │
│   Project path:      /home/ashserver/AshWorks/synk-demo/after    │
│   Target file:       package-lock.json                           │
│                                                                  │
│   Total security issues: 0                                       │
╰──────────────────────────────────────────────────────────────────╯


💡 Tip

   To view ignored issues, use the --include-ignores option.
                                                            

ashserver@vasant:~/AshWorks/synk-demo/after$ snyk container test snyk-demo:after --file=Dockerfile --exclude-app-vulns | tail -n 25


Organization:      persuasivepost
Package manager:   apk
Target file:       Dockerfile
Project name:      docker-image|snyk-demo
Docker image:      snyk-demo:after
Platform:          linux/amd64
Target OS:         Alpine Linux v3.24
Base image:        node:22-alpine
Licenses:          enabled

Tested 18 dependencies for known issues, found 1 issue.

According to our scan, you are currently using the most secure version of the selected base image

Pro tip: use `--exclude-base-image-vulns` to exclude from display Docker base image vulnerabilities.

Snyk found some vulnerabilities in your image applications (Snyk searches for these vulnerabilities by default). See https://snyk.co/app-vulns for more information.

To remove these messages in the future, please run `snyk config set disableSuggestions=true`

Learn more: https://docs.snyk.io/products/snyk-container/getting-around-the-snyk-container-ui/base-image-detection


ashserver@vasant:~/AshWorks/synk-demo/after$ cd ..
ashserver@vasant:~/AshWorks/synk-demo$ diff before/package.json after/package.json
2c2
<   "name": "snyk-demo-before",
---
>   "name": "snyk-demo-after",
4c4
<   "description": "INTENTIONALLY VULNERABLE demo app - old pinned dependencies. Do not deploy.",
---
>   "description": "Remediated demo app - upgraded dependencies.",
10,16c10,16
<     "axios": "0.18.0",
<     "ejs": "2.5.7",
<     "express": "4.16.0",
<     "jsonwebtoken": "8.3.0",
<     "lodash": "4.17.4",
<     "minimist": "1.2.0",
<     "moment": "2.19.1"
---
>     "axios": "^1.7.9",
>     "ejs": "^3.1.10",
>     "express": "^4.21.2",
>     "jsonwebtoken": "^9.0.2",
>     "lodash": "^4.17.21",
>     "minimist": "^1.2.8",
>     "moment": "^2.30.1"
ashserver@vasant:~/AshWorks/synk-demo$ diff before/Dockerfile after/Dockerfile
1,3c1,2
< # INTENTIONALLY OUTDATED base image (Node 14 on Debian buster, both end-of-life).
< # Snyk will report many OS-level CVEs in this image. Used for the "before" scan only.
< FROM node:14
---
> # Remediated image: current LTS Node on a minimal Alpine base, running as a non-root user.
> FROM node:22-alpine
8c7
< RUN npm ci
---
> RUN npm ci --omit=dev
12a12
> USER node
ashserver@vasant:~/AshWorks/synk-demo$ python3 scripts/compare.py
| Target | Version | Critical | High | Medium | Low | Total |
|---|---|---:|---:|---:|---:|---:|
| Dependencies (npm) | before | 2 | 22 | 37 | 4 | **65** |
| Dependencies (npm) | after | 0 | 0 | 0 | 0 | **0** |
| Dependencies (npm) | _reduction_ | | | | | _100%_ |
| Docker image | before | 8 | 77 | 76 | 384 | **545** |
| Docker image | after | 0 | 1 | 0 | 0 | **1** |
| Docker image | _reduction_ | | | | | _100%_ |

Saved /home/ashserver/AshWorks/synk-demo/results/comparison.png and /home/ashserver/AshWorks/synk-demo/results/summary.md
ashserver@vasant:~/AshWorks/synk-demo$ 