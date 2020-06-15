from aip import AipSpeech
from ffmpy3 import FFmpeg
import playsound
import os


class VoiceHelp(object):
    """
        音频工具
    """

    __api_client = None

    def __init__(self, _app_id, _api_key, _secret_key):
        self.__api_client = AipSpeech(_app_id, _api_key, _secret_key)

    def wav_to_text(self, stream):
        """
        wav 音频转文本
        :param stream:
        :return:
        """
        return self.__api_client.asr(stream, 'pcm', 16000, {'lan': 'zh'})

    def text_to_voice(self, text):
        """
        文字变声音
        :param text:
        :return:
        """
        return self.__api_client.synthesis(text, "zh")

    @staticmethod
    def stream_to_file(stream, path):
        """
        保存流到文件
        :param stream:
        :param path:
        :return:
        """
        if os.path.exists(path):
            os.remove(path)
        with open(path, 'wb') as f:
            f.write(stream)

    @staticmethod
    def mp3_to_wav(_mp3_path, _wav_path):
        """
        媒体格式转换
        :param _mp3_path:
        :param _wav_path:
        :return:
        """
        if os.path.exists(_wav_path):
            os.remove(_wav_path)
        FFmpeg(inputs={_mp3_path: None}, outputs={_wav_path: None}).run()

    @staticmethod
    def play_sound(path):
        """
        播放音频
        :param path:
        :return:
        """
        playsound.playsound(path)

    @staticmethod
    def get_stream(path):
        """
        地址转流
        :param path:
        :return:
        """
        with open(path, 'rb') as f:
            return f.read()


app_id = "20391833"
api_key = "ABV5EKC1lTZSUvsG8NYGFm0K"
secret_key = "utAHLM3sBASRendZRq06wgnPqKZsFyPj"
mp3_path = '../examples/test.mp3'
wav_path = '../examples/test.wav'

voice_help = VoiceHelp(app_id, api_key, secret_key)

# 获取mp3 音频
mp3_stream = voice_help.text_to_voice("你好，今天你吃饭了吗?")

# 保存 mp3
VoiceHelp.stream_to_file(mp3_stream, mp3_path)

# 播放音频
VoiceHelp.play_sound(mp3_path)

# 转存wav
voice_help.mp3_to_wav(mp3_path, wav_path)

# 播放wav
VoiceHelp.play_sound(wav_path)

# 语音识别
result = voice_help.wav_to_text(VoiceHelp.get_stream(wav_path))

# 打印结果
print(result)




