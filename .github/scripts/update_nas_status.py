#!/usr/bin/env python3
import json
import os
from datetime import datetime, timezone, timedelta

def update_nas_status():
    try:
        # 从仓库根目录读取 data.json
        repo_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        data_file = os.path.join(repo_root, 'data.json')
        
        # 读取现有数据
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 获取北京时间 (UTC+8)
        beijing_tz = timezone(timedelta(hours=8))
        current_time = datetime.now(beijing_tz).strftime('%Y-%m-%dT%H:%M:%S')
        
        nas_notification = None

        for notification in data['notifications']:
            if notification['id'] == 1:
                nas_notification = notification
                break

        if nas_notification:
            nas_notification['title'] = '❌ NAS状态异常 (自动检测)'
            nas_notification['content'] = f'''🔴 NAS状态监测报告 - {current_time}<br><br>
GitHub Action检测到NAS状态通知超过1.5小时未更新，系统可能已离线。<br><br>
📊 最后检测时间: {current_time}<br><br>
⚠️ 注意: 此状态由GitHub Action自动标记'''
            nas_notification['date'] = current_time
        else:
            nas_notification = {
                'id': 1,
                'title': '❌ NAS状态异常 (自动检测)',
                'content': f'''🔴 NAS状态监测报告 - {current_time}<br><br>
GitHub Action检测到NAS状态通知长时间未更新。<br><br>
📊 最后检测时间: {current_time}<br><br>
⚠️ 注意: 此状态由GitHub Action自动标记''',
                'date': current_time
            }
            data['notifications'].append(nas_notification)

        # 保存更新
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print('✅ 已更新NAS异常状态')
        
    except Exception as e:
        print(f'❌ 更新NAS状态时出错: {str(e)}')
        raise

if __name__ == "__main__":
    update_nas_status()