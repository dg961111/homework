import json
import re
import mitmproxy.http
from mitmproxy import http

url = "https://stock.xueqiu.com/v5/stock/batch/quote.json"
values = [0, -999999, 999999, 0.01, -0.01]


class MockLocal:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if url in flow.request.pretty_url and 'x=' in flow.request.pretty_url:
            with open('quote.json', encoding="utf-8") as f:
                # mapLocal返回
                flow.response = http.HTTPResponse.make(
                    200,
                    f.read()
                )


class MockRewrite:

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if url in flow.request.pretty_url and 'x=' in flow.request.pretty_url:
            data = json.loads(flow.response.text)
            items = data.get("data").get("items")
            for i in range(min(len(values), len(items))):
                quote = items[i].get("quote")
                value = values[i]
                quote["percent"] = value
            flow.response.text = json.dumps(data)


class MockDouble:

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if url in flow.request.pretty_url and 'x=' in flow.request.pretty_url:
            res = flow.response.text
            result = self.double_float(res, times=3)
            flow.response.text = result

    def double_float(self, text, times=2):
        match = re.finditer(':\s*[-]{0,1}\d*\.\d*', text)
        for m in match:
            v = m.group().split(':')[1]
            text = re.sub(v, str(float(v) * times), text)
        return text


addons = [
    MockLocal(),
    # MockRewrite(),
    # MockDouble()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    mitmdump(['-p', '8080', '-s', __file__])
