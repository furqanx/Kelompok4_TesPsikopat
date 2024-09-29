from flask import Flask

app = Flask(__name__)

# Menentukan secret_key untuk aplikasi Flask
app.secret_key = '\xbc\xef\xf9\x90\xb4\xa6$\x15C\x96\xfc\xb4\xbf\x18\x15V'

# mengimpor rute dari aplikasi
from app import routes
