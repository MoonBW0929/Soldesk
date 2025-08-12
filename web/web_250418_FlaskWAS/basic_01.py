from flask import Flask

app = Flask(__name__)
@app.get("/te.st")

def test():
    print("aaa")
    return "abcd"

if __name__ == "__main__":
    app.run(
        "0.0.0.0",      # 접속 허용 주소
        4567,           # 포트 번호
        debug=True
    )