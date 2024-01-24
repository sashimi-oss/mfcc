from flask import Flask, request, render_template, url_for, redirect
import os, predictFunction

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)

# POSTでデータ取得
@app.route('/', methods=['GET', 'POST'])
def do_get_post():
    if request.method == 'POST':
        # preVC = result.preVC
        file = request.files['file']
        file.save(os.path.join('./audio', 'uploaded.wav'))
        preVC = predictFunction.predictPostAudio()
        #音声データとして受け取るにはどうしたらよい？
        # text = request.form.get('text')
        # cmd = f"python ./jano.py {name}"
        # subprocess.call(cmd.split())
        # wakati = jano.wakati
        # import jano
        # wakati = jano.keisotai_kaiseki(text)
        return render_template('result.html', preVC=preVC, file=file)
        # return redirect(url_for('result', preVC = preVC, file = file))
    text = ['最初の文','中間の文','最後の文']
    return render_template('index.html', text=text)


# ==================================================
# 実行 
# flask --app app run -h 0.0.0.0 -p 5001 --cert=adhoc
# ==================================================
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5001", ssl_context=('openssl/server.crt', 'openssl/server.key'), threaded=True, debug=True)

