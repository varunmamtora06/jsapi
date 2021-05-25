from flask_marshmallow import Marshmallow
from .models import Blog

ma = Marshmallow()

class BlogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Blog
        load_instance = True