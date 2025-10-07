#!/usr/bin/env python3
import json
import sys
from datetime import datetime, timedelta

def check_notification_time():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        for notification in data.get('notifications', []):
            if notification.get('id') == 3:
                print(notification.get('date', ''))
                return
        
        print('NOT_FOUND')
            
    except Exception as e:
        print('ERROR')

if __name__ == "__main__":
    check_notification_time()