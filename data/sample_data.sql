-- Create Patients table
CREATE TABLE Patients (
    patient_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    gender VARCHAR(10),
    address VARCHAR(100),
    phone_number VARCHAR(15)
);

-- Create Providers table
CREATE TABLE Providers (
    provider_id SERIAL PRIMARY KEY,
    provider_name VARCHAR(100),
    speciality VARCHAR(50),
    npi_number VARCHAR(10),
    address VARCHAR(100),
    phone_number VARCHAR(15)
);

-- Create Claims table
CREATE TABLE Claims (
    claim_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES Patients(patient_id),
    provider_id INTEGER REFERENCES Providers(provider_id),
    service_date DATE,
    submission_date DATE,
    claim_amount DECIMAL(10, 2),
    status VARCHAR(20)
);

-- Create Diagnoses table
CREATE TABLE Diagnoses (
    diagnosis_id SERIAL PRIMARY KEY,
    claim_id INTEGER REFERENCES Claims(claim_id),
    icd10_code VARCHAR(10),
    description VARCHAR(255)
);

-- Create Procedures table
CREATE TABLE Procedures (
    procedure_id SERIAL PRIMARY KEY,
    claim_id INTEGER REFERENCES Claims(claim_id),
    cpt_code VARCHAR(10),
    description VARCHAR(255),
    charge_amount DECIMAL(10, 2)
);

-- Insert sample data into Patients
INSERT INTO Patients (first_name, last_name, date_of_birth, gender, address, phone_number) VALUES
('John', 'Doe', '1980-05-15', 'Male', '123 Main St, Anytown, USA', '555-1234'),
('Jane', 'Smith', '1992-08-22', 'Female', '456 Elm St, Othertown, USA', '555-5678'),
('Bob', 'Johnson', '1975-03-10', 'Male', '789 Oak St, Somewhere, USA', '555-9012');

-- Insert sample data into Providers
INSERT INTO Providers (provider_name, speciality, npi_number, address, phone_number) VALUES
('Dr. Alice Williams', 'General Practice', '1234567890', '101 Medical Center, Healthville, USA', '555-2468'),
('Dr. Charles Brown', 'Cardiology', '0987654321', '202 Heart Clinic, Cardiocity, USA', '555-1357');

-- Insert sample data into Claims
INSERT INTO Claims (patient_id, provider_id, service_date, submission_date, claim_amount, status) VALUES
(1, 1, '2023-06-15', '2023-06-20', 150.00, 'Submitted'),
(2, 2, '2023-06-18', '2023-06-22', 500.00, 'Pending'),
(3, 1, '2023-06-19', '2023-06-21', 200.00, 'Approved');

-- Insert sample data into Diagnoses
INSERT INTO Diagnoses (claim_id, icd10_code, description) VALUES
(1, 'J00', 'Acute nasopharyngitis [common cold]'),
(2, 'I10', 'Essential (primary) hypertension'),
(3, 'M54.5', 'Low back pain');

-- Insert sample data into Procedures
INSERT INTO Procedures (claim_id, cpt_code, description, charge_amount) VALUES
(1, '99213', 'Office visit for evaluation and management', 150.00),
(2, '93000', 'Electrocardiogram, complete', 250.00),
(2, '93010', 'Electrocardiogram report', 50.00),
(3, '97110', 'Therapeutic exercises', 100.00);