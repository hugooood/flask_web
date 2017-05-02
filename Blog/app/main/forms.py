from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required

# class PostForm(FlaskForm):
#     title = StringField('Title',[DataRequired(),length(max=255)])
#     text = TextAreaField('Content',[DataRequired()])
#     categories = SelectMultiField('Categories',coerce=int)

#     def __init__(self):
#         super(PostForm,self).__init__()
#         self.categories.choices = [(c.id,c.title) for c in Category.query.order_by('id')]

class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')