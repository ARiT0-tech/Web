from flask import Flask, request
import random

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
    return '<h1>Жди нас, Марс!<h1>' \
           '<img src="/static/img/mars.jpg" alt="!!!ТУТ ФОТО!!!" />' \
           '<p>Вот она какая, красная планета.</p>'


@app.route('/promotion_image')
def promotion_image():
    color = ['dark', 'success', 'info', 'danger', 'warning', 'primary']
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" href="/static/css/style.css" type="text/css">
                        <title>Реклама с картинкой</title>
                      </head>
                      <body>
                        <h1 class="h1_image_mars">Жди нас, Марс!<h1>
                        <img src="/static/img/mars.jpg" alt="!!!ТУТ ФОТО!!!" />
                        <div class="alert alert-{random.choice(color)} role="alert">
                            Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-{random.choice(color)} role="alert">
                            Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-{random.choice(color)} role="alert">
                            Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-{random.choice(color)} role="alert">
                            И начнем с Марса!
                        </div>
                        <div class="alert alert-{random.choice(color)} role="alert">
                            Присоединяйся!
                        </div>
                      </body>
                    </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
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
                                            <label for="acceptRules">Какие у Вас есть профессии?</label>
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


@app.route('/choice/<name>')
def choice_name(name):
    planets = {
        'марс': ['Эта планета близка к Земле;', 'На ней много необходимых ресурсов;', 'На ней есть вода и атмосфера;',
                 'На ней есть небольшое магнитное поле;', 'Наконец, она просто красива!'],
        'земля': ['Мы как бы тут уже живём...', '........', '...'],
        'меркурий': ['Является ближайшей планетой к Солнцу;', 'У планеты нет спутников;',
                     'Является наименьшей планетой системы;', 'Меркурий имеет крайне разреженную атмосферу.'],
        'венера': ['Венера близка по размеру к Земле;',
                   'Имеет толстую силикатную оболочку вокруг железного ядра и атмосферу;',
                   'Количество воды на Венере гораздо меньше земного, а её атмосфера в 90 раз плотнее;',
                   'Температура поверхности Венеры превышает 400 °C.'],
        'юпитер': ['Юпитер обладает массой в 318 раз больше земной;', 'Он состоит главным образом из водорода и гелия;',
                   'Высокая внутренняя температура Юпитера вызывает множество полупостоянных вихревых структур в его атмосфере.'],
        'сатурн': ['Сатурн, известный своей обширной системой колец;',
                   'Имеет несколько схожие с Юпитером структуру атмосферы и магнитосферы;',
                   'Сатурн — наименее плотная планета Солнечной системы.'],
        'уран': ['Уран имеет массу в 14 раз больше, чем Земля;',
                 'Уникальным среди других планет его делает то, что он вращается «лёжа на боку»;',
                 'Если другие планеты можно сравнить с вращающимися волчками, то Уран больше похож на катящийся шар;',
                 'Он имеет намного более холодное ядро, чем другие газовые гиганты, и излучает в космос очень мало тепла.']}
    if name.lower() in planets:
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>{name}</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {name}</h1>
                        {create_info(planets[name.lower()])}
                      </body>
                    </html>'''
    else:
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <title>Каво?</title>
                              </head>
                              <body>
                                <h1>Мое предложение: {name}</h1>
                                <p>А это где?</p>
                              </body>
                            </html>'''


@app.route('/results/<nickname>/<level>/<rating>')
def results(nickname, level, rating):
    try:
        nickname = str(nickname)
        level = int(level)
        rating = float(rating)
    except Exception:
        return 'Ошибка'
    text = [f'Поздравляем! Ваш рейтинг после {level} этапа отбора', f'составляет {rating}!', 'Желаем удачи!']
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Результаты отбора</title>
                      </head>
                      <body>
                        <h1>Результаты отбора</h1>
                        <h2>Претендента на участие в миссии {nickname}:</h1>
                        {create_info(text)}
                      </body>
                    </html>'''


def create_info(planets):
    container = ''
    color = ['dark', 'success', 'info', 'danger', 'warning', 'primary']
    for planet in planets:
        container += f'<div class="alert alert-{random.choice(color)}" role="alert">{planet}</div> '
    return container


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
