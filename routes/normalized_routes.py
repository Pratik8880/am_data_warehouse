from flask import Blueprint, jsonify
from models import PrintJob

normalized_bp = Blueprint('normalized', __name__)   # Created a Blueprint named 'normalized' to group related routes

@normalized_bp.route('/normalized/print_jobs')
def list_print_jobs():
    """
    Route to list all print jobs from the PrintJobs table.
    Returns a JSON array with job id, part name, date (formatted), and status.
    """
    jobs = PrintJob.query.all()   # Query print jobs from the database
    return jsonify([{          # Built and return a dictionaries
        'id': job.id,
        'part_name': job.part_name,
        'date': job.date.strftime('%Y-%m-%d'),
        'status': job.status
    } for job in jobs])
