from flask_wtf import FlaskForm
from wtforms.fields import simple, core
from wtforms import IntegerField, StringField, BooleanField, validators, SelectField, DateTimeField,Form, widgets, ValidationError
from wtforms.validators import DataRequired


class BuyBookForm(FlaskForm):
	isSend = simple.BooleanField(
        label='send',
        widget=widgets.CheckboxInput())
	address = StringField ('Address')

class QueryGoodsForm(FlaskForm):
	bookname = StringField('bookname', validators=[validators.DataRequired(message="Book name can not be empty")])

class buyerAdd(FlaskForm):
	bookname = StringField ('bookname', validators=[DataRequired()])
	isbn = StringField ('isbn', validators=[DataRequired()])
	category = StringField ('category', validators=[DataRequired()])
	price = StringField ('price', validators=[DataRequired()])
	sellprice = StringField ('sellprice', validators=[DataRequired()])
	content = StringField ('content', validators=[DataRequired()])
	wanted = simple.BooleanField('purchase',widget=widgets.CheckboxInput())
	image = StringField('image',validators=[DataRequired()])
