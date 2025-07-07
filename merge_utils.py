from models import db
from sqlalchemy import text

def create_merged_view():
    sql = """
    CREATE OR REPLACE VIEW MergedPrintData AS
    SELECT 
        p.id as job_id,                     -- print job ID
        p.date,                             -- date of the print job
        pr.model as printer_model,          -- printer model used
        m.name as material_name,            -- material name used
        m.cost_per_kg,                      -- cost of material
        p.part_name,                        -- name of printed part
        p.weight_g,                         -- weight of printed part
        p.status,                           -- print status (success/fail)
        u.name as user_name,                -- who ran the print job
        (SELECT AVG(t.value) FROM Tests t WHERE t.print_job_id = p.id) as test_avg    -- average test value for the print job
    FROM PrintJobs p
    JOIN Printers pr ON p.printer_id = pr.id
    JOIN Materials m ON p.material_id = m.id
    JOIN Users u ON p.user_id = u.id
    """
    db.session.execute(text(sql))
    db.session.commit()


