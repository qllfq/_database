from flask import Flask,render_template
from exts import db
from models import Article,Tag
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    article1 = Article(title='aaa')
    article2 = Article(title='bbb')

    tag1 = Tag(name='android')
    tag2 = Tag(name='python')

    article1.tags.append(tag1)
    article2.tags.append(tag1)

    article1.tags.append(tag2)
    article2.tags.append(tag2)

    db.session.add(article1)
    db.session.add(article2)
    db.session.add(tag1)
    db.session.add(tag2)

    db.session.commit()
    article = Article.query.filter(Article.title == 'aaa').first()
    tags = article.tags
    for tag in tags:
        print(tag.name)
    return 'hello world'


@app.route('/login/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
