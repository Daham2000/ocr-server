from aifc import Error
from firebase_admin import auth
from firebase_admin.exceptions import FirebaseError
from flask import jsonify, make_response


class ItemModel:
    def __init__(self):
        print("__init__")

    def getItems(self, limit, page):
        db = self.db
        query = ""
        items_ref = db.collection(u'items')

        totalPosts = items_ref.order_by('ItemID').get()
        try:
            totalPosts = items_ref.order_by('ItemID').stream()
            if query == None:
                items = items_ref.order_by(
                    'ItemID').limit(limit*(page)).stream()
            elif query == "":
                items = items_ref.order_by(
                    'ItemID').limit(limit*(page)).stream()
            else:
                query = query.strip()
                try:
                    items = items_ref.where(
                        "ItemID", ">=", query).limit(limit*(page)).stream()
                except FirebaseError as e:
                    return make_response(jsonify(str(e)), 422)
            list = []
            for doc in items:
                list.append(doc)
            totalItems = len(list)
            totalNeeded = limit*(page-1)
            # get total posts number
            posts = []
            for doc in totalPosts:
                posts.append(doc)
            numOfTotalPosts = len(posts)

            if totalItems > totalNeeded:
                difference = totalItems-totalNeeded
                print(difference)
                if difference < limit:
                    last_doc = list[(-difference)]
                else:
                    last_doc = list[(-limit)]
                list = []
                last_pop = last_doc.to_dict()['ItemID']
                next_query = (items_ref.order_by('ItemID').start_at({
                    'ItemID': last_pop
                }).limit(limit)).stream()
                for doc in next_query:
                    list.append(doc.to_dict())
            else:
                list = []
            return make_response(jsonify({"totalItems": numOfTotalPosts, "posts": list}), 200)

        except Error as e:
            return make_response(jsonify(str(e)), 422)
    

    def getSingleItem(self, limit, page):
        db = self.db
        query = self.itemId
        items_ref = db.collection(u'items')

        totalPosts = items_ref.order_by('ItemID').get()
        try:
            totalPosts = items_ref.order_by('ItemID').stream()
            if query == None:
                items = items_ref.order_by(
                    'ItemID').limit(limit*(page)).stream()
            elif query == "":
                items = items_ref.order_by(
                    'ItemID').limit(limit*(page)).stream()
            else:
                query = query.strip()
                try:
                    items = items_ref.where(
                        "ItemID", "==", query).limit(limit*(page)).stream()
                except FirebaseError as e:
                    return make_response(jsonify(str(e)), 422)
            list = []
            for doc in items:
                list.append(doc)
            totalItems = len(list)
            totalNeeded = limit*(page-1)
            # get total posts number
            posts = []
            for doc in totalPosts:
                posts.append(doc)
            numOfTotalPosts = len(posts)

            if totalItems > totalNeeded:
                difference = totalItems-totalNeeded
                print(difference)
                if difference < limit:
                    last_doc = list[(-difference)]
                else:
                    last_doc = list[(-limit)]
                list = []
                last_pop = last_doc.to_dict()['ItemID']
                next_query = (items_ref.order_by('ItemID').start_at({
                    'ItemID': last_pop
                }).limit(limit)).stream()
                for doc in next_query:
                    list.append(doc.to_dict())
            else:
                list = []
            return make_response(jsonify({"totalItems": numOfTotalPosts, "posts": list}), 200)

        except Error as e:
            return make_response(jsonify(str(e)), 422)
    

    def getShipments(self, limit, page):
        db = self.db
        query = ""
        shipments_ref = db.collection(u'shipments')

        totalPosts = shipments_ref.order_by('ShipmentID').get()
        try:
            totalPosts = shipments_ref.order_by('ShipmentID').stream()
            if query == None:
                items = shipments_ref.order_by(
                    'ShipmentID').limit(limit*(page)).stream()
            elif query == "":
                items = shipments_ref.order_by(
                    'ShipmentID').limit(limit*(page)).stream()
            else:
                query = query.strip()
                try:
                    items = shipments_ref.where(
                        "ShipmentID", ">=", query).limit(limit*(page)).stream()
                except FirebaseError as e:
                    return make_response(jsonify(str(e)), 422)
            list = []
            for doc in items:
                list.append(doc)
            totalItems = len(list)
            totalNeeded = limit*(page-1)
            # get total posts number
            posts = []
            for doc in totalPosts:
                posts.append(doc)
            numOfTotalPosts = len(posts)

            if totalItems > totalNeeded:
                difference = totalItems-totalNeeded
                print(difference)
                if difference < limit:
                    last_doc = list[(-difference)]
                else:
                    last_doc = list[(-limit)]
                list = []
                last_pop = last_doc.to_dict()['ShipmentID']
                next_query = (shipments_ref.order_by('ShipmentID').start_at({
                    'ShipmentID': last_pop
                }).limit(limit)).stream()
                for doc in next_query:
                    list.append(doc.to_dict())
            else:
                list = []
            return make_response(jsonify({"totalItems": numOfTotalPosts, "posts": list}), 200)

        except Error as e:
            return make_response(jsonify(str(e)), 422)
    

    def saveReport(self):
        db = self.db
        reports_ref = db.collection(u'reports')
        try:
            data = {
                'description': self.description,
                'isRead': self.isRead,
                'time': self.time
            }
            responce = reports_ref.document(self.time).set(data)
        except FirebaseError as e:
            return make_response(jsonify(str(e)),422)

        return make_response(jsonify(str("Post created...")),201)
