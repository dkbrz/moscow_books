from flask import Flask, render_template, request
from demoapp.models import db, Recommendation, History

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    if request.args:
        user_id = request.args.get("uid")
        recommend = [i.book for i in Recommendation.query.filter_by(iduser=user_id)]
        history = [i.book for i in History.query.filter_by(iduser=user_id)]
        if not recommend:
            recommend = [i.book for i in Recommendation.query.filter_by(iduser=0)]
        if not history:
            user_id = 0
    else:
        recommend, user_id, history = [], 0, []
    return render_template("index.html", recommend=recommend, history=history, user_id=user_id)


if __name__ == '__main__':
    app.run(debug=True)
