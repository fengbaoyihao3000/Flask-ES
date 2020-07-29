#自定义表单类，文本字段、密码字段、提交按钮
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, InputRequired, length


class CommentForm(FlaskForm):
    theme = StringField(validators=[InputRequired(), DataRequired()])
    email=StringField (validators=[DataRequired(),Email()])
    content = TextAreaField(validators=[DataRequired(),length(min=1,max=500)])
    submit = SubmitField(u'发送消息')

class SearchForm(FlaskForm):
    search_key = StringField(validators=[InputRequired(), DataRequired()])
    submit = SubmitField()

