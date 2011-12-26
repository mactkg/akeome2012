#-*- coding: utf-8 -*-
import os
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import flash
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f*7nqma=0o8)3*a%lywecut%l(wh1s+*o#%3)4kb^vanz0kw$2'

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/reply', methods=['GET','POST'])
def reply():
    if request.method == 'GET':
        return redirect(url_for('index'))
    if request.form['answer'] == u"こたつ":
        flash(u'ok')
        return render_template('ans.html', messages=u"せいかーい。")
    elif request.form['answer'] == u"ごたつ":
        flash(u'おしい。うさぎちゃんが求めているのは「冬を超すためにたいせつなもの」だー！')
        return redirect(url_for('index'))
    else:
        flash(u'ヒント：今年の干支と数にちゅうもくだー')
        return redirect(url_for('index'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
