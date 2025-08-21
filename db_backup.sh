#!/bin/bash
mysqldump -u root -pYourPassword paymentdb > backup.sql
echo "Backup completed: $(date)"
