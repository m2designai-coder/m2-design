from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>M2 DESIGN</title>
        <style>
            body { background: #000; color: #00f2ff; font-family: 'Segoe UI', sans-serif; 
                   display: flex; justify-content: center; align-items: center; 
                   height: 100vh; margin: 0; overflow: hidden; }
            .card { border: 2px solid #0044ff; padding: 40px; border-radius: 20px; 
                   text-align: center; background: rgba(0, 5, 20, 0.9);
                   box-shadow: 0 0 30px rgba(0, 68, 255, 0.4); border-left: 5px solid #00f2ff; }
            h1 { font-size: 2.5em; letter-spacing: 2px; margin: 0; }
            .status { color: #fff; margin-top: 15px; font-size: 1.2em; opacity: 0.8; }
            .orbit { border: 1px dashed #0044ff; border-radius: 50%; position: absolute; z-index: -1; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>M2 DESIGN<sup>°</sup></h1>
            <div class="status">M3<sup>°</sup> Assistant: ONLINE</div>
        </div>
    </body>
    </html>
    '''
    res = make_response(html)
    res.headers['Content-Security-Policy'] = "frame-ancestors https://vk.com https://*.vk.com"
    res.headers['X-Frame-Options'] = "ALLOW-FROM https://vk.com"
    return res

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
