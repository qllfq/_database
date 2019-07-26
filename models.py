from exts import db

# 中间表
article_tag = db.Table('article_tag',
                       db.Column('article_id',db.Integer,db.ForeignKey('article.id'),primary_key=True),
                       db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'),primary_key=True))


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    tags = db.relationship('Tag',secondary=article_tag,backref=db.backref('articles'))


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),nullable=False)

