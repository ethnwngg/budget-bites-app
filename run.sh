#!/usr/bin/env bash
set -euo pipefail

APP_DIR="$HOME/budget-bites-app"
APP_FILE="budget-app.py"

cd "$APP_DIR"

# Pull latest code
git fetch --all
git reset --hard origin/main

# Install/update deps globally for this user
python3 -m pip install -U pip
python3 -m pip install -r requirements.txt

# Stop previous process (if any)
pkill -f "python3 $APP_FILE" || true

# Start new process
nohup python3 "$APP_FILE" > log.txt 2>&1 &

echo "Started. Tail logs with: tail -n 200 -f $APP_DIR/log.txt"
