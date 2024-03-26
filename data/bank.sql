-- Active: 1706527539532@@127.0.0.1@3306@discord
CREATE DATABASE ;
USE bank;

CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    surname VARCHAR(255),
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    iban INT,
    last_transaction DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO user(surname, name, email, password, last_transaction) VALUES
('HLV','HLV', 'a', 'a')
('Lucas','Martinie','lucas.m@laplateforme.io', '$2y$10$qIBQqkFGuABUzh8HIv2m2ujXi/oebdIBtChVGz1P0ixyWudg01sDG')
('Hamza','Naya','hamza.n@laplateforme.io', '$2y$10$AXJlbvg/.t9vYiSGPfuGHOYXmAKQT0zIVrcF5iPYIe0YbgdMwVDyi')
('Vanny','Lamorte','vanny.l@laplateforme.io', '$2y$10$cGxUJ9.IKTUilIBT3TJbkOLHMURdMq9KdYodZYzZ5MWAonsk2wA/O
');

-- LucasMartinie1!
-- HamzaNaya1!
-- VannyLamorte1!


CREATE TABLE type (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    intro TEXT,
    photo BOOLEAN
);

INSERT INTO type (name, intro) VALUES
('Checking Accounts','You can put max : ', 1),
('Savings Accounts','You can put max : ', 2);

CREATE TABLE category (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    id_type INT
);
('Living Expenses', 1),
('Transportation Costs', 2),
('Food and Grocery Expenditures', 3),
('Personal Expenses', 4),
('Financial Obligations', 5)


