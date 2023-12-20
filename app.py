from flask import Flask, request, render_template

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)

# POSTでデータ取得
@app.route('/', methods=['GET', 'POST'])
def do_get_post():
    # if request.method == 'POST':
        # text = request.form.get('text')
        # cmd = f"python ./jano.py {name}"
        # subprocess.call(cmd.split())
        # wakati = jano.wakati
        # import jano
        # wakati = jano.keisotai_kaiseki(text)
        # return render_template('result.html', text=wakati)
    text = ['最初の文','中間の文','最後の文']
    return render_template('index.html', text=text)


# ==================================================
# 実行
# ==================================================
if __name__ == '__main__':
    app.run()

