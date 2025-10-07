#!/usr/bin/env python3
import json
import sys
import os
from datetime import datetime, timedelta

def check_notification_time():
    try:
        # 从仓库根目录读取 data.json
        repo_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        data_file = os.path.join(repo_root, 'data.json')
        
        with open(data_file, 'r') as f:
            data = json.load(f)
        
        for notification in data.get('notifications', []):
            if notification.get('id') == 3:
                print(notification.get('date', ''))
                return
        
        print('NOT_FOUND')
            
    except Exception as e:
        print(f'ERROR: {str(e)}')

if __name__ == "__main__":
    check_notification_time()