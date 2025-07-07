from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Material(db.Model):    # Materials table: stores info about materials used for printing
    __tablename__ = 'Materials'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    cost_per_kg = db.Column(db.Float, nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('Suppliers.id'))   # Foreign key to Suppliers table

class Supplier(db.Model):   # Suppliers table: stores info about suppliers providing materials
    __tablename__ = 'Suppliers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    contact_info = db.Column(db.String(100))

class Printer(db.Model):   # Printers table: stores info about printers in the lab or facility
    __tablename__ = 'Printers'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50))
    location = db.Column(db.String(50))
    status = db.Column(db.String(20))

class User(db.Model):    # Users table: stores info about people using the system
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    role = db.Column(db.String(50))

class PrintJob(db.Model):     # PrintJobs table: each print job, linked to printer, material, and user
    __tablename__ = 'PrintJobs'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    printer_id = db.Column(db.Integer, db.ForeignKey('Printers.id'))   # Foreign key to Suppliers table
    material_id = db.Column(db.Integer, db.ForeignKey('Materials.id'))   # Foreign key to Suppliers table
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))   # Foreign key to Suppliers table
    part_name = db.Column(db.String(100))
    weight_g = db.Column(db.Float)
    status = db.Column(db.String(20))  

class Test(db.Model):          # Tests table: test results for printed parts, linked to print job
    __tablename__ = 'Tests'
    id = db.Column(db.Integer, primary_key=True)
    print_job_id = db.Column(db.Integer, db.ForeignKey('PrintJobs.id'))   # Foreign key to Suppliers table
    test_type = db.Column(db.String(50))
    value = db.Column(db.Float)
    units = db.Column(db.String(20))
