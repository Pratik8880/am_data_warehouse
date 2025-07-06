from flask import Blueprint, jsonify  #organize the routes
from sqlalchemy import text      #import text for raw SQL queries
from models import db   #import the database session
from analytics import failure_rate_per_material #import the analytics function

merged_bp = Blueprint('merged', __name__)      #Create a Blueprint for merged routes

@merged_bp.route('/merged/summary')   # Route to get merged summary data
def merged_summary():
    sql = text("SELECT * FROM MergedPrintData")
    result = db.session.execute(sql).mappings().all()
    result = [dict(row) for row in result]
    return jsonify(result)


@merged_bp.route('/analytics/failure_rate')   # Route to get failure rate per material
def failure_rate():
    data = failure_rate_per_material()
    return jsonify(data)


