from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Required


class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')

# class PostForm(FlaskForm):
#     title = StringField('Title',[DataRequired(),length(max=255)])
#     text = TextAreaField('Content',[DataRequired()])
#     categories = SelectMultiField('Categories',coerce=int)

#     def __init__(self):
#         super(PostForm,self).__init__()
#         self.categories.choices = [(c.id,c.title) for c in Category.query.order_by('id')]

class ArticleForm(FlaskForm):
    title = StringField(u"标题", validators=[DataRequired()])
    # category = QuerySelectField(u"分类", query_factory=getUserFactory(), get_label='name')
    categories = StringField(u'分类',validators=[DataRequired()])
    # categories = SelectMultipleField(u'分类', coerce=int,validators=[DataRequired()])
    tags = StringField(u"标签", validators=[DataRequired()]) #这里本来准备绑定到`models.py`定义的`Tag`表的，但是`WTFORMS`貌似没有这种字段，只有用字符串来表示了
    content = TextAreaField(u"正文", validators=[DataRequired()])
    submit = SubmitField(u"发布")

    def __init__(self):
        super(ArticleForm,self).__init__()