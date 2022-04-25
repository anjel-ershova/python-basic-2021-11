from http import HTTPStatus
from os import getenv

from flask import Flask
from flask_migrate import Migrate

from flask import (
    render_template,
    request,
    redirect,
    url_for,
)
from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError

from forms import CatForm
from models import Cat
from models.database import db


app = Flask(__name__)

# app.config.from_object('config.ProductionConfig') вот так будет выбираться жестко ProductionConfig
# а как ниже - с выбором режима из конфига
CONFIG_OBJECT_PATH = "config.{}".format(getenv("CONFIG_NAME", "DevelopmentConfig"))
app.config.from_object(CONFIG_OBJECT_PATH)

db.init_app(app)

migrate = Migrate(app, db)


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
    cats: list[Cat] = Cat.query.all()
    return render_template("list.html", cats=cats)


@app.get("/<int:cat_id>/", endpoint="cat_details")
def get_cat_by_id(cat_id: int):
    cat = Cat.query.get(cat_id)
    if cat is None:
        raise NotFound(f"Cat #{cat.id} not found!")

    return render_template(
        "details.html",
        cat=cat,
    )


@app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_cat():
    form = CatForm()  # форма нужна только для проверок валидации
    if request.method == "GET":
        # return render_template("add_cat.html") # без формы
        return render_template("add_cat.html", form=form)  # с формой

    if not form.validate_on_submit():
        return render_template("add_cat.html", form=form), HTTPStatus.BAD_REQUEST

    cat_name = form.data['name']
    cat_is_fluffy = form.data['is_fluffy']

    cat = Cat(name=cat_name, is_fluffy=cat_is_fluffy)
    db.session.add(cat)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(f"could not save cat, probably name {cat_name!r} is not unique")
    except DatabaseError:
        db.session.rollback()
        raise InternalServerError(f"could not save cat, unexpected error")

    cat_url = url_for("cat_details", cat_id=cat.id)
    return redirect(cat_url)

if __name__ == '__main__':
    app.run(host="0.0.0.0")