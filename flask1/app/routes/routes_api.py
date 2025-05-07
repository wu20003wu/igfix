from flask import Blueprint, jsonify, request
from datetime import datetime
from app.extensions import db  # Korrekter Import der DB-Instanz
from app.models import Db_msg

# Blueprint erstellen statt Flask-App
bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route("/home", methods=['GET'])
def return_home():
    return jsonify({
        'message': "Hello IG-FIX!"
    })

@bp.route("/db_msg/clordid", methods=['GET'])
def get_msg(clordid):
    db_msg = Db_msg.query.filter_by(message_type="D", trans_ref=clordid).first()
    if not db_msg:
        return jsonify({"db_msg": "not found"}), 404
    
    return jsonify([{
        'msg_data': d.msg_data
    } for d in db_msg]), 2000

