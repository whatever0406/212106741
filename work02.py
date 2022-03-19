import requests
import datetime
import time


# 获取数据
def getData():
    url = 'https://j1.pupuapi.com/client/marketing/storeproduct/v2/search?store_id=831b632e-12bd-4c23-a6fd-a18749d8d508&page=1&size=20&name=&category_id=&sort=0&tag=&brands=&in_stock=-1&is_commend=-1&business=scenes&business_id=100'
    # 浏览器标识
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
    }
    # 发送请求给url
    productData = requests.get(url, headers=headers).json()
    return productData


# 获取产品信息
def getProduct():
    # 解析JSON获取相应的值
    response = getData()
    for data in response['data']['products']:
        pid = data['id']
        # 匹配商品id
        if pid == 'bc48e939-88bd-444d-b843-00e6faee4a1d':
            name = data['name']
            spec = data['spec']
            price = str(data['price'] / 100)
            guide = str(data['price_guide'] / 100)
            title = data['sub_title']
            text = data['custom_tag_text']
    # 打印输出商品信息
    print('---------------' + '商品: ' + name + '---------------')
    print('规格:' + spec)
    print('价格: ' + price)
    print('原价/折扣价: ' + guide + '/' + price)
    print('详细内容: ' + spec + '; ' + title + '.' + text)
    print('---------------' + '商品: ' + name + '的价格波动---------------')


# 监控价格
def monitor():
    # 设置死循环来实时监控价格
    while 1:
        # 获取相应的值
        response = getData()
        for data in response['data']['products']:
            pid = data['id']
            # 匹配商品id
            if pid == 'bc48e939-88bd-444d-b843-00e6faee4a1d':
                price = str(data['price'] / 100)
        # 获取当前时间
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('当前时间为' + now_time + ', ' + '价格为' + price)
        time.sleep(1)


# 调用函数
def run():
    getProduct()
    monitor()


# 运行
run()
