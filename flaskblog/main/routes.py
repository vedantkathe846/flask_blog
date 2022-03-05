from flask import render_template, request, Blueprint
from flaskblog.models import Posts
from flask import Blueprint

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    page=request.args.get('page',1,type=int)
    posts = Posts.query.order_by(Posts.date.desc()).paginate(page=page,per_page=2)
    return render_template("layout.html",posts=posts)

@main.route("/about")
def about():
    return render_template("about.html",title='about')   
