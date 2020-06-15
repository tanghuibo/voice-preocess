from aip import AipSpeech
import playsound
from ffmpy3 import FFmpeg


class VoiceHelp(object):
    """
        音频工具
    """

    __api_client = None

    def __init__(self, app_id, api_key, secret_key):
        self.__api_client = AipSpeech(app_id, api_key, secret_key)

    def wav_to_text(self, stream):
        return self.__api_client.asr(stream, 'amr', 16000, {'lan': 'zh'})

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
       with open(path, 'wb') as f:
        f.write(stream)

    @staticmethod
    def mp3_to_wav(mp3_path, wav_path):

        """
        媒体格式转换
        :param self:
        :param mp3_path:
        :param wav_path:
        :return:
        """
        FFmpeg(inputs={mp3_path: None}, outputs={wav_path: None}).run()

    @staticmethod
    def play_sound(path):
        """
        播放音频
        :param self:
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




