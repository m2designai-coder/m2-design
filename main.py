from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Мы переносим весь HTML в файл templates/index.html
    # А здесь просто вызываем его
    res = make_response(render_template('index.html'))
    
    # Оставляем твои настройки для работы внутри ВК
    res.headers['Content-Security-Policy'] = "frame-ancestors https://vk.com https://*.vk.com"
    res.headers['X-Frame-Options'] = "ALLOW-FROM https://vk.com"
    return res

if __name__ == "__main__":
    # Render сам назначит порт, поэтому host='0.0.0.0' важен
    app.run(host='0.0.0.0')
