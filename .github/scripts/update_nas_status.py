#!/usr/bin/env python3
import json
from datetime import datetime

def update_nas_status():
    # 读取现有数据
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 更新ID为3的通知
    current_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    nas_notification = None

    for notification in data['notifications']:
        if notification['id'] == 3:
            nas_notification = notification
            break

    if nas_notification:
        nas_notification['title'] = '❌ NAS状态异常 (自动检测)'
        nas_notification['content'] = f'''🔴 NAS状态监测报告 - {current_time}

GitHub Action检测到NAS状态通知超过1.5小时未更新，系统可能已离线。

📊 最后检测时间: {current_time}

⚠️ 注意: 此状态由GitHub Action自动标记'''
        nas_notification['date'] = current_time
    else:
        nas_notification = {
            'id': 3,
            'title': '❌ NAS状态异常 (自动检测)',
            'content': f'''🔴 NAS状态监测报告 - {current_time}

GitHub Action检测到NAS状态通知长时间未更新。

📊 最后检测时间: {current_time}

⚠️ 注意: 此状态由GitHub Action自动标记''',
            'date': current_time
        }
        data['notifications'].append(nas_notification)

    # 保存更新
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print('✅ 已更新NAS异常状态')

if __name__ == "__main__":
    update_nas_status()