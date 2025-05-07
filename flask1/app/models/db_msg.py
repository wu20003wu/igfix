from datetime import datetime
from app.extensions import db  # Import von extensions statt main

# Neue Task-Model-Klasse
class Db_msg(db.Model):
    __tablename__ = 'db_msg'
    message_id = db.Column(db.String, primary_key=True, autoincrement=True)
    queue = db.Column(db.String(20))
    in_link = db.Column(db.String(20))
    out_link = db.Column(db.String(20))
    trans_ref = db.Column(db.String(35))
    message_type = db.Column(db.String(30))
    msg_data = db.Column(db.String(2900))

def insert_sample_db_msg():
    if not Db_msg.query.first():
        db_msg = Db_msg(message_type="D", msg_data="8=FIX.4.2;9=1;35=D;49=tag49;56=tag56;11=ClOrdId_xxx;21=3;48=tag48;10=043")
        db.session.add(db_msg)
        db.session.commit()
    
    
    

