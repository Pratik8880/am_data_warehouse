from models import db
from sqlalchemy import text

def failure_rate_per_material():   #For each material, the number of print jobs and the number of failed print jobs
    # Define SQL query:
    sql = text("""
    SELECT m.name as material, 
           COUNT(*) as total, 
           SUM(CASE WHEN p.status='fail' THEN 1 ELSE 0 END) as failed
    FROM PrintJobs p
    JOIN Materials m ON p.material_id = m.id
    GROUP BY m.name
    """)
    result = db.session.execute(sql).fetchall()      # Execute the query and fetch all results 
    return [{'material': r.material, 'failure_rate': r.failed / r.total} for r in result]           # dictionaries:
