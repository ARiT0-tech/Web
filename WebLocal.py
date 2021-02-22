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
    return '<h1 class="h1_image_mars">Жди нас, Марс!<h1><img src="/static/img/mars.jpg" alt="!!!ТУТ ФОТО!!!" />'


@app.route('/promotion_image')
def promotion_image():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <link rel="stylesheet" href="/static/css/style.css" type="text/css">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1 class="h1_image_mars">Жди нас, Марс!<h1>
                    <img src="/static/img/mars.jpg" alt="!!!ТУТ ФОТО!!!" />
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
                                <title>Анкета</title>
                              </head>
                              <body>
                                <h1 class="h">Анкета претендента</h1>
                                <h2 class="h">на участие в мисси</h2>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="text" class="form-control" id="surname" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surname">
                                        <input type="text" class="form-control" id="name" aria-describedby="emailHelp" placeholder="Введите имя" name="name">
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у Вас образование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                              <option>Среднее специальное</option>
                                              <option>Бакалавр</option>
                                              <option>Магистр</option>
                                              <option>Специалитет</option>
                                              <option>Доктор наук</option>
                                            </select>
                                         </div>
                                        <div class="form-group">
                                            <label for="acceptRules">Какое у Вас образование?</label>
                                            <div class="check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                            </div>
                                            <div class="check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                            </div>
                                            <div class="check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                <label class="form-check-label" for="acceptRules">Пилот</label>
                                            </div>
                                            <div class="check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                            </div>
                                            <div class="check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                            </div>
                                            <div class="check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
                                            </div>
                                            <div class="check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                <label class="form-check-label" for="acceptRules">Врач</label>
                                            </div>
                                            <div class="check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                            </div>
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
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about" style="max-width: 445px;"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file" style="display: block; margin-bottom: 10px";
                                        </div>
                                        <div class="form-group form-check" style="display: block; margin-bottom: 10px">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="answer">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['accept'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['answer'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=666, host='127.0.0.1')
