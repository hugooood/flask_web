#数据库模型
from . import db
from datetime import datetime
import bleach,markdown #????

# @loginManager.user_loader
# def load_user(user_id):
#     try:
#         return User.query.get(int(user_id))
#     except Exception as e:
#         print(str(e))

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64))
    tags = db.Column(db.String(64))
    categories = db.Column(db.String(64))
    content = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<article %r>' % (self.title)

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        # 需要转换的标签
        allowed_tags = [
            'a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
            'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
            'h1', 'h2', 'h3', 'p', 'img'
        ]
        # 需要提取的标签属性，否则会被忽略掉
        attrs = {
            '*': ['class'],
            'a': ['href', 'rel'],
            'img': ['src', 'alt']
        }
        target.content_html = bleach.linkify(
            bleach.clean(
                markdown(value, output_format='html'),
                tags=allowed_tags,
                attributes=attrs,
                strip=True
            )
        )