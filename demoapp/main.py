from flask import Flask, render_template, request
from demoapp.models import db, Recommendation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    if request.args:
        user_id = request.args.get("uid")
        recommend = Recommendation.query.get(user_id)
        if recommend is None:
            recommend = Recommendation.query.get(0)
        elif not recommend.recommendations:
            recommend.recommendations = Recommendation.query.get(0).recommendations
    else:
        recommend, user_id = None, 0
    return render_template("index.html", recommend=recommend, user_id=user_id)


if __name__ == '__main__':
    app.run(debug=True)