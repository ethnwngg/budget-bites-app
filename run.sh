#!/usr/bin/env bash
set -euo pipefail

# --- Configuration ---
APP_DIR="$HOME/budget-bites-app"
APP_FILE="budget-app.py"
PORT=5050

cd "$APP_DIR"

# --- Pull latest code from GitHub ---
git fetch --all
git reset --hard origin/main

# --- Ensure Python virtual environment exists ---
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

# --- Activate virtual environment ---
source "$APP_DIR/.venv/bin/activate"

# --- Install/update dependencies ---
pip install --upgrade pip
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

# --- Stop any previous instance of this app ---
pkill -f "python $APP_FILE" || true

# --- Start Flask app in background ---
nohup python "$APP_FILE" > log.txt 2>&1 &

echo "✅ App started on port $PORT"
echo "Tail logs with: tail -n 200 -f $APP_DIR/log.txt"