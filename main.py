from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>🚀 Deployment Status</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f0f2f5;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background-color: #ffffff;
                padding: 2rem 3rem;
                border-radius: 1rem;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
                text-align: center;
                transition: transform 0.3s ease;
            }
            .card:hover {
                transform: scale(1.02);
            }
            h1 {
                color: #4CAF50;
                margin-bottom: 1rem;
            }
            p {
                font-size: 1.2rem;
                color: #333333;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Hello from Version 1</h1>
            <p>This is a new update! Deployment was <strong>successful ✅</strong></p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
