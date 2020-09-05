from flask import render_template, request, Blueprint
from amana.models import FAQ,NewsPost,Service,Information_and_Records
from amana.posts.forms import ServiceForm

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route("/contact")
def contact():

    return render_template('contact.html')

@main.route("/test")
def test():
    page = request.args.get('page', 1, type=int)
    news = NewsPost.query.all()
    FAQs = FAQ.query.order_by()
    info = Information_and_Records.query.first()
    Services = Service.query.all()
    return render_template('mainxx.html', news = news[-3:], FAQs = FAQs, Services = Services, posts =True, slider= True,info = info)


@main.route("/about")
def about():
    info = Information_and_Records.query.first()
    return render_template('about.html', title='About', info = info)


@main.route("/Services")
def services():
    Services = Service.query.all()
    return render_template('Service.html', title='Service', legend='New Service', Services = Services)
