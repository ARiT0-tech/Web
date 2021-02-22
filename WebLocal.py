from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def xedni():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/promotion')
def promotion():
    return 'Человечество вырастает из детства.<br>Человечеству мала одна планета.<br>Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!'


@app.route('/image_mars')
def mars_img():
    return '<h1>Жди нас, Марс!<h1><img src="/static/img/mars.jpg" alt="!!!ТУТ ФОТО!!!">'


@app.route('/promotion_image')
def promotion_image():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <link rel="stylesheet" href="/static/css/style.css" type="text/css">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.jpg" alt="!!!ТУТ ФОТО!!!">
                    <div class="block1">
                        Человечество вырастает из детства.
                    </div>
                    <div class="block2">
                        Человечеству мала одна планета.
                    </div>
                    <div class="block3">
                        Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="block4">
                        И начнем с Марса!
                    </div>
                    <div class="block5">
                        Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection')
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet" href="/static/css/style.css" type="text/css">
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1>Форма для регистрации в суперсекретной системе</h1>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                        <div class="form-group">
                                            <label for="classSelect">В каком вы классе</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>7</option>
                                              <option>8</option>
                                              <option>9</option>
                                              <option>10</option>
                                              <option>11</option>
                                            </select>
                                         </div>
                                        <div class="form-group">
                                            <label for="about">Немного о себе</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')