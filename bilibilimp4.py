import os,subprocess,shutil

path=input('请输入缓存视频文件夹路径')

print(f'目录文件:{os.listdir(path)}\n开始查找视音频\n')
m4s = [f for f in os.listdir(path) if f.endswith('.m4s')]
audio = [i for i in m4s if '30280' in i]
video = [i for i in m4s if '30280' not in i]

#用临时文件操作
audio_temp = os.path.join(path, 'audio_temp.m4s')
video_temp = os.path.join(path, 'video_temp.m4s')
shutil.copy(os.path.join(path,audio[0]), audio_temp)
shutil.copy(os.path.join(path,video[0]), video_temp)

#audio_temp和video_temp已经是路径.

for i in(audio_temp,video_temp):          #删开头9个0
    with open(i,'rb') as f:
        data = f.read()
        if data[:9] == b'0' * 9:      #字节的表示方法,b'0',意思是值为0的字符(加b是因为二进制),因为文件打开的格式就是二进制,要用字节来操作文件内容
            data=data[9:]
        else:
            print(f'错误,开头不一致  文件{i}')
            os.remove(video_temp);os.remove(audio_temp)
            exit()
    with open(i,'wb') as f:
        f.write(data)

#检测使用系统的还是工具的ffmpeg

try:
    import imageio_ffmpeg
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
except:
    ffmpeg = shutil.which('ffmpeg')

subprocess.run([ffmpeg,'-v','error','-i',video_temp,'-i',audio_temp,'-c','copy',os.path.join(path,'output.mp4')])

os.remove(video_temp);os.remove(audio_temp)
print('结束')


#ffmpeg -i xxxxx30120.m4s -i xxxxxx.30280.m4s -c:v copy -c:a copy 自己命名.mp4