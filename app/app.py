from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MLOps Task</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f4f4f4;
                font-family: Arial, sans-serif;
            }
            .container {
                text-align: center;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 18px;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>21i_1743</h1>
            <h2>Shah Meeran Ali</h2>
            <p>This is MLOps Task</p>
        </div>
    </body>
    </html>
    """

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, render_template_string

app = Flask(_name_)

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MLOps Task</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .container {
            text-align: center;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        h1 {
            color: #333;
        }
        p {
            font-size: 18px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>21i2654</h1>
        <h2>Muhammad Zoraib Qadir</h2>
        <p>This is MLOps Task</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(template)

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=5000)