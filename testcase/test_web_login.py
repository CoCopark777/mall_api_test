import jsonpath
import requests
from testdata.web_conf import mall_front_url

class Login:

    def __init__(self):
        self.headers={}

    def login(self):
        url=mall_front_url+"/login"
        data={"principal":"19500000002",
              "credentials":"123456",
              "appType":3,
              "loginType":"0"}
        res=requests.post(url,json=data)
        token = jsonpath.jsonpath(res.json(), "$..access_token")[0]
        self.headers["Authorization"] = "bearer{}".format(token)
        return res.json()

    def test_orderPath(self):
        "获取秒杀地址"
        self.login()
        url = mall_front_url+ "/p/seckill/orderPath"
        res =requests.get(url,headers=self.headers)
        return res.text

    def test_confirm(self):
        "创建订单"
        order_path=self.test_orderPath()
        url= mall_front_url + "/p/seckill/{}/confirm".format(order_path)
        data ={"addrId":0,"prodCount":1,"seckillSkuId":228}
        res =requests.post(url,json=data,headers=self.headers)
        print(res.text)
        shop_id =jsonpath.jsonpath(res.json(),"$..shopId")[0]
        return shop_id

    def test_submit(self):
        "提交订单"
        order_path=self.test_confirm()
        url = mall_front_url + "/p/seckill/{}/submit".format(order_path)
        data={"orderShopParam":{"remarks":"","shopId":""},"orderPath":order_path}
        res =requests.post(url,json=data,headers=self.headers)
        return res

    def test_pay(self):
        "支付订单"
        url=mall_front_url + "/p/order/pay"
        data={"payType": 3, "orderNumbers": "1516774312361857024"}


if __name__ == '__main__':
    cl=Login()
    res=cl.login()
    print(res)
    or_res = cl.test_confirm()
    print(or_res)
"""
{"actualTotal":0.01,"total":0.01,"seckillReduce":0.0,
"transfee":0.0,"totalCount":1,
"userAddr":{"addrId":362,"receiver":"fish","province":"广东省",
"city":"深圳市","area":"福田区","addr":"深圳湾1号","mobile":"19500000002",
"lng":0.0,"lat":0.0,"commonAddr":1,"provinceId":44,
"cityId":4403,"areaId":440304},
"shopCartItem":{"prodName":"玛莎拉蒂","prodNameCn":"玛莎拉蒂",
"prodNameEn":"玛莎拉蒂","prodCount":1,
"pic":"http://mall.lemonban.com:8108/2022/04/fe6e90aa385b4eeaaff795a623bd5210.jpg",
"price":0.01,"categoryId":null,"productTotalAmount":0.01,"prodId":4473,
"skuId":4930,"skuName":"","useScore":null,"scorePrice":0,"basketId":null,
"actualTotal":0.01,"discountId":0,"shareReduce":0.0,"isShareReduce":null,
"scorePayReduce":null,"discounts":[],"deliveryMode":null,"deliveryModeVO":null,
"isCheck":null,"shopId":1,"shopName":null,"oriPrice":null,"distributionCardNo":null,
"basketDate":"2022-04-20 21:42:03","preSellStatus":null,"preSellTime":null,
"shopCityStatus":null,"seckillSkuId":228,"seckillId":178,"seckillPrice":0.01},
"msgId":null,"userId":null,"remarks":null,"orderNumber":null}
"""