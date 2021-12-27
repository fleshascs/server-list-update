# Server list updates

---
## Install python packages
**Note:** Open terminal in PyCharm
```shell
pip install -r requirements.txt
```

## setup cron
```shell
crontab –e
00 4 * * * python3 /path/main.py
```