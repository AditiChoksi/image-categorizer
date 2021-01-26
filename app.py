from flask import Flask, request
from flask import jsonify
from collections import defaultdict
#import boto3
#from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
# cors = CORS(app, resources={r"/api/": {"origins": ""}})

# client = boto3.client('s3')
# s3 = boto3.resource('s3')

# @app.route('/')
# def render_homepage():
    
#     location = request.args.get('location')
#     bucketname = "insta" + location
#     bucket = s3.Bucket(bucketname).objects.all()

#     data = defaultdict(list)
#     for obj in bucket:
#         url = 'https://' + bucketname + '.s3.amazonaws.com/' + obj.key
#         tag_name = obj.key.split('/')[0]
#         tags = [{'value': tag_name, 'title': tag_name}]
#         image_info = {
#             'src': url,
#             'thumbnail': url,
#             'thumbnailWidth': obj.key,
#             'thumbnailHeight': obj.key,
#             'tags': tags,
#         }
#         data['all'].append(image_info)
#         data[tag_name].append(image_info)
        
#     return jsonify(data)

@app.route('/sayHi')
def sayHi():
    data = {"greeting": "Hi"}
        
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)