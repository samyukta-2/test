CREATE DATABASE attendance_db;

USE attendance_db;

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    date DATE NOT NULL,
    status VARCHAR(10) NOT NULL
);

