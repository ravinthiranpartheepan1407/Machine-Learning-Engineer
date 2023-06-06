-- CREATE Table useraccount(
    name VARCHAR(50),
    email VARCHAR(50),
    password VARCHAR(20),
    phone INTEGER,
    country VARCHAR(50)
);

INSERT INTO useraccount(
    name,
    email,
    password,
    phone,
    country
) VALUES
    ('Watney', 'watney@gmail.com', 'watney*', 47, 'sector47'),
    ('Reeves', 'reeves@gmail.com', 'reeves*', 13, 'sector13');

SELECT * from userAccount;

SELECT name, email from userAccount;

SELECT name, country='Ind' AS indian from useraccount;

