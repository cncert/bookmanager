# bookmanager

## 添加变量
在根目录创建.env文件：
EMAIL_HOST_USER="your eamil"
EMAIL_HOST_PASSWORD="your passwd"
EMAIL_SERVER="smtp.xx"
EMAIL_SERVER_PORT=25
MANAGER_NAME = ""

1. 添加定时任务
python manage.py crontab add  --settings=bookmanager.prod
2. 查看定时任务
python manage.py crontab show  --settings=bookmanager.prod
```
(venv) [wt@bogon bookmanager]$ python manage.py crontab show  --settings=bookmanager.prod
Currently active jobs in crontab:
e0e8013d3c784ad38255d8c5709b3557 -> ('*/2 * * * *', 'books.tasks.scan_user', '> /tmp/cron.log')
```
3. 在定时任务中修改：
```
*/2 * * * * cd /home/wt/project/apps/bookmanager && /home/wt/project/apps/venv/bin/python /home/wt/project/apps/bookmanager/manage.py crontab run e0e8013d3c784ad38255d8c5709b3557 --settings=bookmanager.prod >> /tmp/cron.log
```

## Ubuntu 解决 OSError: mysql_config not found 报错
```
sudo apt-get install libmysqlclient-dev
```