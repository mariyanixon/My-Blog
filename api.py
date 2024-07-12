from flask_restful import Resource, Api
from models import db, Post
from flask import jsonify,request,make_response

api=Api()
class PostResource(Resource):
    def get(self,id=None):
        if id is None:
            posts=Post.query.all()
            list=[]
            for post in posts:
                list.append({
                    'id':post.id,
                    'title':post.title,
                    'author':post.author,
                    'content':post.content
                })
            return list,200
        else:
            post=Post.query.get(id)
            return {'id':post.id,
                    'title':post.title,
                    'author':post.author,
                    'content':post.content},200
        
    def post(self):
        data=request.get_json()
        post=Post(title=data['title'],author=data['author'],content=data['content'])
        db.session.add(post)
        db.session.commit()
        return make_response(jsonify({'message':'Post added successfully','id':post.id}),201)
    
    def put(self,id):
        post=Post.query.get(id)
        data=request.get_json()
        post.title=data['title']
        post.author=data['author']
        post.content=data['content']
        db.session.commit()
        return jsonify({'message':'Post updated successfully'})
    
    def delete(self,id):
        post=Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        return make_response(jsonify({'message':'Post deleted successfully'}),200)
    
api.add_resource(PostResource,'/api/posts','/api/posts/<int:id>')