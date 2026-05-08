from flask import Flask, jsonify

app = Flask(__name__)

# 健康检查接口
@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

# 业务接口
@app.route('/api/test')
def test_api():
    return jsonify({"msg": "自动化测试通过"}), 200

# 首页
@app.route('/')
def index():
    return "<h1>Docker自动化测试服务</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
