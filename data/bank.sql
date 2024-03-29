CREATE DATABASE bank;
USE bank;

CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    iban VARCHAR(255),
    account_number VARCHAR(255),
    date_last_co DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO user (first_name, last_name, email, password, iban, account_number) VALUES
('Hamza','Naya', 'a', "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb", "GB10WWBP10203012345698", 28092002),
('Lucas','Martinie','lucas.m@laplateforme.io', '43e405862bdfbdef17f2f13bf6e8a3efe088de01ad8eb4a9f47ff3fa21f20aae', "GB10WWBP10203012345678", 24121995),
('Vanny','Lamorte','hamza.n@laplateforme.io', 'c9d0532835cc70cbc44011958faed891b3f254627dd0e7b8d3d99c995b2600e4', "GB11WWBP11223387654321", 13052001),
('Lucy','Madec','vanny.l@laplateforme.io', '4f15f99279d26f053ddbe27b8e5d9d3203926820c25ebeade0bd082653ab696b', "GB12WWBP30201054321678", 25121993 );

-- 0. Super User a
-- 1. LucasMartinie1!
-- 2. HamzaNaya1!
-- 3. VannyLamorte1!

CREATE TABLE account (
    id INT PRIMARY KEY AUTO_INCREMENT,
    account_type INT,
    general_description TEXT
);

-- Checking Accounts = 1
-- Savings Accounts = 2

INSERT INTO account(account_type, description) VALUES
('1',"Welcome to your checking account! Let's manage your finances together"),
('2', "Welcome back to your savings account! Let's continue growing your financial goals together");

-- "Unlock the perks of a checking account today! Enjoy easy access to your funds, seamless online transactions, and peace of mind with built-in security features."
-- "Unlock financial freedom with our Saving Account! Enjoy peace of mind knowing your money is safe and growing. With a minimum deposit of 100 pounds per month and a maximum daily withdrawal limit of 300 pounds, it's the perfect way to secure your future while maintaining access to your funds."

CREATE TABLE transaction (
    id INT PRIMARY KEY AUTO_INCREMENT,
    transaction_re INT,
    transaction_name VARCHAR(255),
    description TEXT,
    amount INT,
    date DATETIME,
    id_category INT,
    account_id INT,
    id_sender INT,
    id_receiver INT
);

-- transaction_revenu = 1
-- transaction_expense = 2


-- Hamza
INSERT INTO transaction (transaction_re, transaction_name, description, amount, date, id_category, account_id, id_sender, id_receiver) VALUES
('2', 'Cooper Green', 'water bill', 40,'2024-03-25', 1, 1, 1, 95),
('2', 'Total', 'fuel car', 52,'2024-03-24', 2, 1, 1, 85),
('2', 'Mark Spencer', 'grocery shopping', 150,'2024-03-23', 3, 1, 1, 65),
('2', 'Aqua Mass', 'massage', 220,'2024-02-15', 4, 1, 1, 66),
('2', 'Child Support', "Kylie's aids", 323,'2024-02-09', 5, 1, 1, 22),
('1', 'La Plateforme', 'salary', 3000,'2024-02-14', 0, 1, 6, 1),
('1', 'Salah Naya', 'birthday gift', 1000,'2024-02-14', 0, 1, 5, 1),
('2', 'EDF', 'electricity bill', 45,'2024-01-12', 1, 1, 1, 68),
('2', 'London Underground', 'Oyster Card', 100,'2024-01-11', 2, 1, 1, 62),
('2', 'Tesco', 'grocery shopping', 30,'2024-01-10', 3, 1, 1, 65),
('2', 'Blacks', 'hoodie', 50,'2024-01-09', 4, 1, 1, 15),
('2', 'Cooper Green', 'rent', 950,'2024-01-08', 1, 1, 1, 49),

('2', 'Cooper Green', 'water bill', 46,'2023-06-25', 1, 1, 2, 38), 
('2', 'Total', 'fuel car', 60,'2023-06-24', 2, 1, 2, 5),
('2', 'Mark Spencer', 'grocery shopping', 82,'2023-06-23', 3, 1, 2, 15),
('2', 'Moustache & Hair Salon', 'hairdresser', 35,'2023-05-15', 4, 1, 2, 96),
('2', 'LLoyds Bank', 'student loan repayments', 350,'2023-05-09', 5, 1, 2, 26),
('1', 'La Plateforme', 'salary', 2500,'2023-02-14', 0, 1, 6, 2),
('1', 'JC Martinie', 'birthday gift', 200,'2023-05-14', 0, 1, 7, 2),
('2', 'EDF', 'electricity bill', 1500,'2023-04-12', 1, 1, 2, 45),
('2', 'London Underground', 'Oyster Card', 60,'2023-04-11', 2, 1, 2, 26),
('2', 'Tesco', 'grocery shopping', 120,'2023-04-10', 3, 1, 2, 19),
('2', 'JDSport', 'trouser', 50,'2023-04-09', 4, 1, 2, 22),
('2', 'Cooper Green', 'rent', 800,'2023-04-08', 1, 1, 2, 31),

('2', 'Cooper Green', 'water bill', 55,'2022-03-25', 1, 1, 3, 9),
('2', 'Total', 'fuel car', 30,'2022-03-24', 2, 1, 3, 8),
('2', 'Mark Spencer', 'grocery shopping', 50,'2022-03-23', 3, 1, 3, 9),
('2', 'Nail Time', 'nail salon', 25,'2022-02-15', 4, 1, 3, 27),
('2', 'Natwest', 'Loan Repayments ', 120,'2022-02-09', 5, 1, 3, 37),
('1', 'La Plateforme', 'salary', 2000,'2022-02-14', 0, 1, 5, 3),
('1', 'Gerard Lamorte', 'birthday gift', 100,'2022-02-14', 0, 1, 8, 3),
('2', 'EDF', 'electricity bill', 50,'2022-01-12', 1, 1, 3, 6),
('2', 'London Underground', 'Oyster Card', 120,'2022-01-11', 2, 1, 3, 9),
('2', 'Tesco', 'grocery shopping', 28,'2022-01-10', 3, 1, 3, 10),
('2', 'H&M', 'skirt', 35,'2022-01-09', 4, 1, 3, 32),
('2', 'Cooper Green', 'rent', 650,'2022-01-08', 1, 1, 3, 48),

('1', 'La Plateforme', 'salary', 3000, '2024-03-01', 0, 1, 6, 1),
('1', 'La Plateforme', 'salary', 3000, '2023-12-01', 0, 1, 6, 1),
('1', 'La Plateforme', 'salary', 3000, '2024-01-01', 0, 1, 6, 1),
('1', 'La Plateforme', 'salary', 2500, '2023-06-01', 0, 1, 6, 2),
('1', 'La Plateforme', 'salary', 2500, '2023-05-01', 0, 1, 6, 2),
('1', 'La Plateforme', 'salary', 2500, '2023-04-01', 0, 1, 6, 2),
('1', 'La Plateforme', 'salary', 2000, '2023-12-01', 0, 1, 5, 3),
('1', 'La Plateforme', 'salary', 2000, '2022-01-01', 0, 1, 5, 3),
('2', 'EDF', 'electricity bill', 45, '2024-03-05', 1, 1, 1, 95),
('2', 'Total', 'fuel car', 52, '2024-02-10', 2, 1, 1, 85),
('2', 'Mark Spencer', 'grocery shopping', 150, '2024-01-20', 3, 1, 1, 65),
('2', 'EDF', 'electricity bill', 45, '2023-06-05', 1, 1, 1, 38),
('2', 'Total', 'fuel car', 52, '2023-05-10', 2, 1, 1, 5),
('2', 'Mark Spencer', 'grocery shopping', 150, '2024-02-20', 3, 1, 1, 65),
('2', 'EDF', 'electricity bill', 45, '2024-02-05', 1, 1, 1, 38),
('2', 'Total', 'fuel car', 52, '2024-02-19', 2, 1, 1, 5),
('2', 'Mark Spencer', 'grocery shopping', 150, '2023-04-20', 3, 1, 1, 15),
('2', 'EDF', 'electricity bill', 45, '2022-03-05', 1, 1, 1, 9),
('2', 'Total', 'fuel car', 52, '2022-02-10', 2, 1, 1, 8),
('2', 'Mark Spencer', 'grocery shopping', 150, '2022-01-20', 3, 1, 1, 9),
('2', 'EDF', 'electricity bill', 1500, '2023-04-05', 1, 1, 2, 45),
('2', 'London Underground', 'Oyster Card', 60, '2023-03-10', 2, 1, 2, 26),
('2', 'Tesco', 'grocery shopping', 120, '2023-02-20', 3, 1, 2, 19),
('2', 'EDF', 'electricity bill', 1500, '2022-04-05', 1, 1, 2, 6),
('2', 'London Underground', 'Oyster Card', 60, '2022-03-10', 2, 1, 2, 9),
('2', 'Tesco', 'grocery shopping', 120, '2022-02-20', 3, 1, 2, 10),
('2', 'EDF', 'electricity bill', 50, '2024-03-05', 1, 1, 3, 9),
('2', 'Total', 'fuel car', 30, '2024-02-10', 2, 1, 3, 8),
('2', 'Mark Spencer', 'grocery shopping', 50, '2024-01-20', 3, 1, 3, 9),
('2', 'EDF', 'electricity bill', 50, '2023-06-05', 1, 1, 3, 9),
('2', 'Total', 'fuel car', 30, '2023-05-10', 2, 1, 3, 8),
('2', 'Mark Spencer', 'grocery shopping', 50, '2023-04-20', 3, 1, 3, 9),
('2', 'EDF', 'electricity bill', 50, '2022-03-05', 1, 1, 3, 9),
('2', 'Total', 'fuel car', 30, '2022-02-10', 2, 1, 3, 8),
('2', 'Mark Spencer', 'grocery shopping', 50, '2022-01-20', 3, 1, 3, 9),
('2', 'London Underground', 'Oyster Card', 100,'2023-12-11', 2, 1, 1, 62),
('2', 'Tesco', 'grocery shopping', 30,'2023-12-10', 3, 1, 1, 65),
('2', 'Blacks', 'hoodie', 50,'2023-12-09', 4, 1, 1, 15),
('2', 'Cooper Green', 'rent', 950,'2023-12-08', 1, 1, 1, 49),
('2', 'London Underground', 'Oyster Card', 100,'2023-12-11', 2, 1, 2, 62),
('2', 'Tesco', 'grocery shopping', 30,'2023-12-10', 3, 1, 2, 65),
('2', 'Blacks', 'hoodie', 50,'2023-12-09', 4, 1, 2, 15),
('2', 'Cooper Green', 'rent', 950,'2023-12-08', 1, 1, 2, 49),
('2', 'London Underground', 'Oyster Card', 100,'2023-12-11', 2, 1, 3, 62),
('2', 'Tesco', 'grocery shopping', 30,'2023-12-10', 3, 1, 3, 65),
('2', 'Blacks', 'hoodie', 50,'2023-12-09', 4, 1, 3, 15),
('2', 'Cooper Green', 'rent', 950,'2023-12-08', 1, 1, 3, 49);
-- income = 0
-- Living Expenses = 1
-- Transportation Costs = 2
-- Food and Grocery Expenditures = 3
-- Personal Expenses = 4
-- Financial Obligations = 5


CREATE TABLE notification (
    id INT PRIMARY KEY AUTO_INCREMENT,
    notif_message TEXT,
    id_user INT
);