from flask import Flask, render_template_string
import subprocess
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "LIKITH A"

    username = subprocess.check_output("whoami", shell=True).decode().strip()

    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f %Z')

    top_output = subprocess.check_output("top -bn1", shell=True).decode()
    
    html_template = """
    <pre>
    Name: {{ name }}
    user: {{ username }}
    Server Time (IST): {{ server_time }}
    TOP output:
    {{ top_output }}
    </pre>
    """
    
    return render_template_string(html_template, name=name, username=username, server_time=server_time, top_output=top_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)