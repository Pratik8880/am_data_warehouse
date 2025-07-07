USE am_db;

CREATE OR REPLACE VIEW MergedPrintData AS
SELECT 
    p.id as job_id,
    p.date,
    pr.model as printer_model,
    m.name as material_name,
    m.cost_per_kg,
    p.part_name,
    p.weight_g,
    p.status,
    u.name as user_name,
    (SELECT AVG(t.value) FROM Tests t WHERE t.print_job_id = p.id) as test_avg
FROM PrintJobs p
JOIN Printers pr ON p.printer_id = pr.id
JOIN Materials m ON p.material_id = m.id
JOIN Users u ON p.user_id = u.id;
