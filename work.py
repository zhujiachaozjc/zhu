import re
import requests


headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
}                           #为了不让在爬取评论信息的时候遭到网页的反爬措施，而设立的头部请求
result_list = []            #将爬取到的评论信息存入到这里
result = []                 #将每一个url爬取到的评论信息存到这里，也是为了之后存储
cursor = '0'                #给第一个url设立初始值
last_id = '1613957017612'   #给第一个url设立初始值

for i in range(1,999):
    url='https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor='\
        +cursor+'&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_='+last_id
    sources = requests.get(url, headers=headers).content.decode()
    result_list = re.findall('content":"(.*?),"', sources, re.S)   #获得评论信息
    result.append(result_list)                                     #追加到result里
    cursor = re.findall('last":"(.*?)"', sources, re.S)[0]         #获得cursor值
    last_id = str(int(last_id) + 1)                                #在url爬取到所有评论信息之后，进入到下一个网页
    print('over' + str(i))                                         #为了能看出代码是否正常在运行而设置的计数器


with open('comment.txt', 'a', encoding='utf-8') as file:           #将爬取到的所有评论信息保存到comment.txt文件里
    file.write(str(result))

