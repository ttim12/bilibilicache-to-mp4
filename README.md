# bilibili cache-to-mp4

此工具为方便将bilibili客户端缓存的m4s视频快捷转换成通用的mp4格式,操作简单.

step 1:

    下载bilibilimp4.py,requirements.txt
  
step 2:

  安装所需依赖(如果本地环境没有配置ffmpeg)
  
    pip install -r requirements.txt
  
step 3:

    运行py文件,选择目标缓存视频的目录 --> 自动执行转换,保存至缓存视频所在目录

为了防止破坏源文件,脚本处理过程使用临时文件,处理完成后自动清理.
