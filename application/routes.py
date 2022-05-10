from application import application
from flask import request
from firebase_admin import firestore
from firebase_admin import credentials
from werkzeug.utils import secure_filename
import firebase_admin

from application.model.item import ItemModel

cred = credentials.Certificate("private/key.json")
firebase_admin.initialize_app(cred,{'storageBucket': "travel-app-12783.appspot.com"})
db = firestore.client()

@application.route("/")
def index():
    return "Welcome to the server."

@application.route("/get_items/", methods=['GET'])
def login():
    item = ItemModel()
    item.db = db
    responce = item.getItems(20,1);
    return responce

@application.route("/getShipments/", methods=['GET'])
def getShipments():
    item = ItemModel()
    item.db = db
    responce = item.getShipments(20,1);
    return responce

@application.route("/getaitem/", methods=['GET'])
def getSingleItem():
    itemId = request.args.get('itemId')
    item = ItemModel()
    item.db = db
    item.itemId = itemId
    responce = item.getSingleItem(1,1);
    return responce

@application.route('/report', methods=['POST'])
def my_form_post():
    description = request.form['description']
    isRead = request.form['isRead']
    time = request.form['time']

    item = ItemModel()
    item.db = db
    item.description = description
    item.isRead = isRead
    item.time = time
    res = item.saveReport()
    return res
