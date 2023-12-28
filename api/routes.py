from flask import request
from flask_restx import Api, Resource, fields
import pickle
from api.models import db, Datas

rest_api = Api(version="1.0", title="Spotify Prediction API")

"""
API Interface:
   
   - /tracks
       - POST: create a new item
"""

"""
Flask-RestX models Request & Response DATA
"""

# Used to validate input data for creation
track_model = rest_api.model('CreateModel', 
                                {
                                    "id": fields.String(required=True, min_length=1, max_length=255),
                                    "acousticness": fields.Float(required=True, min_length=1, max_length=255),
                                    "data": fields.String(required=True, min_length=1, max_length=255),

                                }
                            )


"""
    Flask-Restx routes
"""

@rest_api.route('/api/tracks')
class Items(Resource):

    """
       Return the prediction of the popularity for several tracks
    """
    @rest_api.expect(track_model, validate=True)
    def post(self):
        print("#################")
        req_data = request.get_json()
        # Get the information    
        item_data = req_data.get("data")
        print(item_data)
        # Create new object
        #new_item = Datas(data=item_data)

        #charger le modèle
        cls = pickle.load(open('model.pkl', 'rb')) 

        #faire la prediction
        prediction = cls.predict(item_data)
        #retourner le resultat

        return {"success" : True,
                "msg"     : "prediction succeeded",
                "datas"   : prediction }, 200
    