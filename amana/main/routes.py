from flask import render_template, request, Blueprint
from amana.models import Post,FAQ,NewsPost,Service
from amana.posts.forms import ServiceForm

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route("/test")
def test():
    page = request.args.get('page', 1, type=int)
    news = NewsPost.query.all()
    FAQs = FAQ.query.order_by(Post.date_posted.desc())
    Services = Service.query.all()
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    if (Services is None):
        print("ssssssssssssssssssssssssssssssssssssssssssssssssss")
    return render_template('mainxx.html', news = news[-4:], FAQs = FAQs, Services = Services, posts =posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/Services/new")
def services():
    form = ServiceForm()
    if form.validate_on_submit():
        Service_to_add = Service(title=form.title.data, content=form.content.data)
        db.session.add(Service_to_add)
        db.session.commit()
        flash('Your Service has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Service',
                           form=form, legend='New Service')
