from http.client import HTTPSConnection
from urllib.parse import quote

api_key = "RGAPI-36935516-8a45-41d3-92db-033af8ebfaac"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
    "Accept-Language": "ko,en;q=0.9,en-US;q=0.8",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com"
}

userNickname = "96년생 티모장인"
tagLine = "9202"
encodedName = quote(userNickname)
# url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{encodedName}/{tagLine}"


# rt_conn = HTTPSConnection("americas.api.riotgames.com")
# rt_conn.request("GET", "/riot/account/v1/accounts/by-riot-id/%s/9202?api_key=RGAPI-36935516-8a45-41d3-92db-033af8ebfaac" % encodedName, headers=header)

# rt_conn.close()
