import pandas as pd

from http.client import HTTPConnection

Gs = HTTPConnection("openapi.seoul.go.kr:8088")
Gs.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")