#-*- coding: utf-8 -*-
import os
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/reply', methods=['GET','POST'])
def reply():
    if request.method == 'GET':
        return redirect(url_for('index'))
    if request.form['answer'] == u"こたつ":
        return render_template('ans.html', message=u"せいかーい。")
    else:
        return render_template('ans.html', message=u"ちがいまーす。")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
