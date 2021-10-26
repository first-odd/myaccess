'''
1.发送请求 获取源代码
2.解析数据 提取地址
3.保存数据
'''
#请求头headers把python伪装成浏览器 ：1. 反爬 2. 请求头 3.ua    然后返回一个数据 response
#headers加 user-agent：浏览器基本信息 cookie：身份验证 referer：防盗链
'''1.'''
import requests
import re
import json

url = str(input('爬取mp3，输入bilibili网址：'))

def get_response(html_url):
    headers = {
        'referer': 'https://www.bilibili.com/',
        'user-agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'
    }
    response = requests.get(url = html_url, headers = headers)
    return response
# response.text 获取相应体的文本数据


def get_audio_info(html_url):
    response = get_response(url)
    title = re.findall('<title>(.*?)</title>',response.text)[0] # 获取标题
    video_info = re.findall('<script>window\.__playinfo__=(.*?)</script>',response.text)[0]  # 获取视频信息
    json_data = json.loads(video_info)
    #print(video_info)
    #print(json_data)
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    #video_url = json_data['data']['dash']['video'][0]['baseUrl']
    audio_info = [title,audio_url]   
    return audio_info
    
def save_info(title,audio_url):
    audio_content = get_response(audio_url).content
    
    with open('/Users/jacksonandrew/Desktop/mp3' +'/'+title + '.mp3',mode='wb') as f1:
        f1.write(audio_content)
    print('Done')

audio_info = get_audio_info(url)
save_info(audio_info[0],audio_info[1]) 


'''出现问题可能会在title上面'''