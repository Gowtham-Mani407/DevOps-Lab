#!/bin/bash

SOURCE="$HOME/devops-lab"
BACKUP_DIR="$HOME/backups"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")

mkdir -p "$BACKUP_DIR"

tar -czf "$BACKUP_DIR/devops_backup_$DATE.tar.gz" "$SOURCE"

echo "Backup completed:"
echo "$BACKUP_DIR/devops_backup_$DATE.tar.gz"
