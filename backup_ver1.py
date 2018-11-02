import os
import time

#   1.需要备份的目录由一个列表指定
source = [r'E:\test']

#   2.主备份目录
target_dir = r'F:\backup'

#   3.zip存档名称
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

#   4.压缩命令
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

#   5.执行命令
if os.system(zip_command) == 0:
    print('successful backup to', target)
else:
    print('Backup Failed')