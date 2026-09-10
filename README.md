# bilibilicache-to-mp4
此工具为方便将bilibili客户端缓存的m4s视频快捷转换成通用的mp4格式,操作简单.

step 1:
  下载bilibilimp4.py,requirements.txt
step 2:
  'pip install -r requirement.txt' 安装所需依赖(如果本地环境没有ffmpeg)
step 3:
  运行py文件,输入需要转换的缓存视频的绝对路径 --> 自动执行转换,保存至脚本运行目录

为了防止破坏原文件,脚本处理过程使用临时文件,处理完成后自动清理.
