#!/bin/bash

LOG_DIR="$HOME/logs"
DAYS=7

echo "Cleaning logs older than $DAYS days..."

find "$LOG_DIR" -name "*.log" -type f -mtime +$DAYS -delete

echo "Log cleanup completed."
