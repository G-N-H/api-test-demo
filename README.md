# 接口自动化测试test

使用Pytest + requests 对 Github 公开API进行功能验证。

## 测试内容
- 正常请求：验证状态码为 200，返回数据中的 login 字段正确
- 异常请求：验证不存在用户时，状态码为 404，返回 message 为 “Not Found”

## 运行方式
pip install requests pytest
pytest test_demo.py -v -s

