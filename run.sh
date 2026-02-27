#!/usr/bin/env bash
set -euo pipefail

APP_DIR="$HOME/budget-bites-app"
APP_FILE="budget-app.py"

cd "$APP_DIR"

# Pull latest code
git fetch --all
git reset --hard origin/main

# Ensure venv exists
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

# Now PY exists
PY="$APP_DIR/.venv/bin/python"

# Install/update deps
"$PY" -m pip install -U pip
"$PY" -m pip install -r requirements.txt

# Stop previous process (if any)
pkill -f "$PY $APP_FILE" || true

# Start new process
nohup "$PY" "$APP_FILE" > log.txt 2>&1 &

echo "Started. Tail logs with: tail -n 200 -f $APP_DIR/log.txt"