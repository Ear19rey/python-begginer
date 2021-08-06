from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def game():
    return render_template('game_order.html')

@app.route('/order', methods=['POST'])
def order():
    user=request.form['user']
    game=request.form['game']
    area=request.form['area']
    pf=request.form.getlist('pf')
    return render_template("result.html",
                           user=user,
                           game=game,
                           area=area,
                           pf=pf)

@app.route('/about/<user>')
def about(user):
    return render_template('index2.html',name=user)

@app.route('/test/<int:score>')
def test(score):
    return render_template('score.html',score=score)

app.run('0.0.0.0',80,debug=True)
