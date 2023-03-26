from flask_rest_jsonapi_next import Api
from blog.api.tag import TagList, TagDetail


def init_api(app):
    api = Api(app)
    api.route(TagList, "tag_list", "/api/tags/")
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/")
    return api
