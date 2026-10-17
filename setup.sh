#!/usr/bin/env bash
# One-time setup. Creates the hidden files that zip/file managers often drop:
#   .github/workflows/snyk.yml   and   .gitignore
# Run from the repo root:  bash setup.sh
set -e
mkdir -p .github/workflows
cp ci/snyk.yml .github/workflows/snyk.yml
cat > .gitignore <<'EOF'
node_modules/
*.log
.env
__pycache__/
EOF
echo "Created:"
ls -a .github/workflows .gitignore
