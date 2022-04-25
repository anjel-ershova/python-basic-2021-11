from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length


class CatForm(FlaskForm):
    name = StringField("Cat name", name="cat-name", validators=[
        DataRequired(),
        Length(min=2),
    ])
    is_fluffy = BooleanField("Is fluffy", default=False)