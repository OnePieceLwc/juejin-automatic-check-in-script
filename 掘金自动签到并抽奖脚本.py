import requests
import time
import datetime

def my_function():
    timestamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))) # 北京时间
    try:
        response = requests.get("https://api.juejin.cn/growth_api/v1/")
        response.raise_for_status()
        print(f"[{timestamp}] API 请求成功")
    except requests.exceptions.RequestException as e:
        print(f"[{timestamp}] API 请求失败: {e}")

def check_sign_in_status(base_url, headers):
    api = "get_today_status"
    url = base_url + api
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data['err_no'] == 0:
            if data['data'] is True:
                print("【今日是否签到】", "已签到")
                return True
            elif data['data'] is False:
                print("【今日是否签到】", "未签到")
                return False
        else:
            print("【当前登录状态】", "未登录,请登录")
            pass
            return False
    else:
        print("【请求失败】", response.status_code)
        return False


def sign_in(base_url, params, headers):
    # data = '{}'
    data = ''
    url = f"{base_url}check_in"
    response = requests.post(url, headers=headers, data=data,params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                print("【当前签到状态】", "签到成功")
                return True
            elif data['err_no'] == 3013 and data['err_msg'] == "掘金酱提示：签到失败了~":
                print("【当前签到状态】", data['err_msg'])
                return False
            elif data['err_no'] == 15001:
                print("【当前签到状态】", '重复签到')
                return True
            else:
                print("【当前签到状态】", data['err_msg'])
                return False
        except requests.JSONDecodeError:
            print("【签到功能】服务器返回的数据无法解析为JSON格式。")
            return False


def get_points(base_url, headers):
    api = "get_cur_point"
    url = base_url + api
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                print("【矿石最新余额】", data['data'])
                return data['data']
        except requests.JSONDecodeError:
            print("【获取余额功能】服务器返回的数据无法解析为JSON格式。")
            return False


def get_free(base_url,params, headers):
    url = f"{base_url}lottery_config/get"
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                if data['data']['free_count'] > 0:
                    print("【免费抽奖次数】", data['data']['free_count'])
                    return True
                else:
                    print("【免费抽奖次数】", data['data']['free_count'])
                    return False
        except requests.JSONDecodeError:
            print("【获取免费抽奖次数功能】服务器返回的数据无法解析为JSON格式。")
            return False


def draw(base_url, params, headers):
    url = f"{base_url}lottery/draw"
    # data = '{}'
    data = ''
    response = requests.post(url, headers=headers, data=data,params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                print("【今日抽奖奖品】", data['data']['lottery_name'])
        except requests.JSONDecodeError:
            print("【抽奖功能】服务器返回的数据无法解析为JSON格式。")
            return False


def get_win(base_url, aid, uuid, spider, headers):
    api = "lottery_lucky/my_lucky"
    url = base_url + api
    data = {
        "aid": aid,
        "uuid": uuid,
        "spider": spider
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                total_value = data['data']['total_value']
                points = get_points(base_url, header1)
                cha = points - (6000 - total_value) * 20
                print("【当前幸运数值】：", total_value)
                if cha >= 0:
                    print("【距离中奖还差】：0 矿石！")
                elif cha <= 0:
                    print("【距离中奖还差】：", str(abs(cha)) + "矿石！")
        except requests.JSONDecodeError:
            print("【获取免费抽奖次数功能】服务器返回的数据无法解析为JSON格式。")
            return False
    else:
        print("【请求失败】", response.status_code)
        return False



if __name__ == "__main__":
    # 掘金自动签到并抽奖脚本
    my_function()
    # 在左侧的搜索框输入：get_cur_point回车 ，点击任意接口
    cookie =""
    aid = ""
    uuid = ""
    spider = ""
    # msToken  获取后测试 url解码和未解码 哪种可以使用
    # 解密网址1:https://www.toolhelper.cn/EncodeDecode/Url
    # 解密网址2:https://www.bejson.com/enc/urlencode/index.html#google%20vignette

    msToken = ''
    a_bogus = ''
    base_url = "https://api.juejin.cn/growth_api/v1/"

    common_params = {"aid": aid, "uuid": uuid, "spider": spider, "msToken": msToken, "a_bogus": a_bogus}
    header1 = {
        'Cookie': cookie,
        'User-Agent': ''
    }

    if check_sign_in_status(base_url, header1):
        if get_free(base_url,common_params, header1):
            draw(base_url,common_params, header1)
            pass
        else:
            pass
    else:
        if not sign_in(base_url, common_params, header1):
            sign_in(base_url, common_params, header1)
        if get_free(base_url,common_params, header1):
            draw(base_url, common_params, header1)
            pass
        else:
            pass
    get_win(base_url, aid, uuid, spider, header1)
