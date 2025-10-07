#!/usr/bin/env python3
import sys
from datetime import datetime, timezone, timedelta

def check_time_difference(notification_time_str):
    try:
        # 获取当前北京时间
        beijing_tz = timezone(timedelta(hours=8))
        current = datetime.now(beijing_tz)
        
        # 解析通知时间（假设已经是北京时间）
        notification_time = datetime.strptime(notification_time_str, '%Y-%m-%dT%H:%M:%S')
        # 将解析的时间设置为北京时间
        notification_time = notification_time.replace(tzinfo=beijing_tz)
        
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