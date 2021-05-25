# I miss Django 🥺
from flask import Blueprint
from flask import jsonify, after_this_request, Response, request
import json
from .models import db, Blog
from .schemas import BlogSchema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/blogs', methods=['GET'])
def get_blogs():
    @after_this_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    if request.method == 'GET':
        blog_query = Blog.query.all()
        blog_schema = BlogSchema(many=True)
        blogs = blog_schema.dump(blog_query)
        print(blogs)
        
        return jsonify({'blogs':blogs})

@api.route('/blog/<int:id>', methods=['GET'])
def get_blog(id):
    @after_this_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    if request.method == 'GET':
        blog_query = Blog.query.get_or_404(id)
        blog_schema = BlogSchema()
        blog = blog_schema.dump(blog_query)
        print(blog)
        
        return jsonify({'blog':blog})

@api.route('/postblog', methods=['POST'])
def post_blog():
    @after_this_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    if request.method == 'POST':
        print(request.form)
        title = request.form['title']
        content = request.form['content']
        print(f'title={title}, content={content}')
        blog = Blog(title=title, content=content)
        
        try:
            db.session.add(blog)
            db.session.commit()

            return Response(status=201)

        except:
            return Response(status=401)

@api.route('/updateblog/<int:id>', methods=['GET', 'POST'])
def update_blog(id):
    @after_this_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    blog = Blog.query.get_or_404(id)

    if request.method == 'POST':
        blog.title = request.form['title']
        blog.content = request.form['content']

    try:
        db.session.commit()

        return Response(status=201)

    except:
        return Response(status=401)

@api.route('/deleteblog/<int:id>')
def delete(id):
    @after_this_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
        
    blog = Blog.query.get_or_404(id)

    try:
        db.session.delete(blog)
        db.session.commit()
        return Response(status=201)

    except:
        return Response(status=401)