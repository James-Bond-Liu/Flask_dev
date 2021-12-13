import requests
res = requests.get("http://www.baidu.com")
print(res.elapsed)
print(res.elapsed.total_seconds())
print(res.elapsed.microseconds)  # 单位微秒ms，当响应时间大于1s时，只截取返回微秒部分
print(res.elapsed.seconds)
print(res.elapsed.days)
print(res.elapsed.max)
print(res.elapsed.min)
print(res.elapsed.resolution)