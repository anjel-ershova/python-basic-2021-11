"""
Домашнее задание №4
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""
from flask import Flask, render_template, request, url_for, jsonify
from werkzeug.exceptions import BadRequest, NotFound
from werkzeug.utils import redirect

app = Flask(__name__)

CATS = {
    1: "Tom",
    2: "Tim",
    3: "Vasya",
}

@app.get("/")  # то же, что и @app.route("/")
def root():
    return render_template(
        "base.html"
    )

@app.get("/about/")
def about():
    return render_template(
        "about.html"
    )

@app.get("/cats_list", endpoint="cats_list")
def list_cats():
    # return jsonify(CATS)
    return render_template("list.html", cats=list(CATS.items()))

@app.get("/<int:cat_id>/", endpoint="cat_details")
def get_cat_by_id(cat_id: int):
    try:
        cat_name = CATS[cat_id]
    except KeyError:
        raise NotFound(f"Cat #{cat_id} not found!")

    return render_template(
        "details.html",
        cat_id=cat_id,
        cat_name=cat_name,
    )



@app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_cat():
    if request.method == "GET":
        return render_template("add_cat.html")

    cat_name = request.form.get("cat-name")
    if not cat_name:
        raise BadRequest("cat name is required, please fill `cat-name`")

    cat_id = len(CATS) + 1
    CATS[cat_id] = cat_name

    cat_url = url_for("cat_details", cat_id=cat_id)
    return redirect(cat_url)