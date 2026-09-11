#!/bin/bash

echo "===== System Health Check ====="

echo
echo "Hostname:"
hostname

echo
echo "Uptime:"
uptime

echo
echo "Disk Usage:"
df -h /

echo
echo "Memory Usage:"
free -h

echo
echo "===== Health Check Completed ====="
