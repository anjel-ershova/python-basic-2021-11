from http import HTTPStatus

from flask import Flask
from flask_migrate import Migrate

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
)
from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError

from .forms import CatForm
from .models import Cat
from .models.database import db

app = Flask(__name__)

app.config.update(
    SECRET_KEY="\xe4X\xb2\xd6\xf2\x94\xca\xd3m\xccMM\x07l",
    SQLALCHEMY_DATABASE_URI="sqlite:///cat_db.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
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

    form = CatForm() # форма нужна только для проверок валидации
    if request.method == "GET":
        # return render_template("add_cat.html") # без формы
        return render_template("add_cat.html", form=form) # с формой

    if not form.validate_on_submit(): # хосспаде, ну до чего ж сумбуроне объяснение
        return render_template("add_cat.html", form=form), HTTPStatus.BAD_REQUEST

    # вот так работает с формами
    cat_name = form.data['name']
    cat_is_fluffy = form.data['is_fluffy']


    #  как ниже - работает с простым html, без всяких form
    # cat_name = request.form.get("cat-name")
    # if not cat_name:
    #     raise BadRequest("Cat name is required, please fill it")
    # cat_is_fluffy = bool(request.form.get("is-fluffy"))

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5012)