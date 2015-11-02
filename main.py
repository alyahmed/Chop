from math import floor
import string

from flask import Flask

app = Flask(__name__)


def toBase62(num, b=62):
    if b <= 0 or b > 62:
        return 0
    base = string.digits + string.lowercase + string.uppercase
    r = num % b
    res = base[r];
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res


def toBase10(num, b=62):
    base = string.digits + string.lowercase + string.uppercase
    limit = len(num)
    res = 0
    for i in range(limit):
        res = b * res + base.find(num[i])
    return res


@app.route('/', methods=['GET', 'POST'])
def home():
    return "Hello World!"


@app.route('/<short_url>')
def redirect_short_url(short_url):
    return short_url


if __name__ == '__main__':
    # This code checks whether database table is created or not
    app.run(debug=True)
