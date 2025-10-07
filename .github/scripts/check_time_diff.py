#!/usr/bin/env python3
import sys
from datetime import datetime

def check_time_difference(notification_time_str):
    try:
        current = datetime.utcnow()
        notification_time = datetime.strptime(notification_time_str, '%Y-%m-%dT%H:%M:%S')
        diff = current - notification_time
        
        if diff.total_seconds() > 5400:  # 1.5小时 = 5400秒
            print('true')
        else:
            print('false')
    except Exception as e:
        print('false')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        check_time_difference(sys.argv[1])
    else:
        print('false')