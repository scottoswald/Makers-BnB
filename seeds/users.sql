DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255),
    email VARCHAR(255),
    phone_number VARCHAR(11)
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    location VARCHAR(255), -- Added from listings
    type VARCHAR(100),     -- Added from listings
    start_date DATE,       -- Added from listings
    end_date DATE,         -- Added from listings
    price_per_night DECIMAL(10, 2),
    user_id int,
    CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO users (username, password, email, phone_number) VALUES ('Dave', 'HelloWorld1!', 'dave@dave.com', '07123456789');
INSERT INTO users (username, password, email, phone_number) VALUES ('Karen', 'HelloWorld2!', 'karen@dave.com', '07987654321');
INSERT INTO users (username, password, email, phone_number) VALUES ('Scott', 'HelloWorld3!', 'scott@dave.com', '07067543278');
INSERT INTO users (username, password, email, phone_number) VALUES ('John', 'HelloWorld4!', 'john@dave.com', '07984386385');

INSERT INTO spaces (name, description, location, type, start_date, end_date, price_per_night, user_id) VALUES ('Buckingham Palace', 'A gorgeous location in the heart of town!', 'London', 'Palace', '2025-07-24', '2026-12-31', 100.00, 1);
INSERT INTO spaces (name, description, location, type, start_date, end_date, price_per_night, user_id) VALUES ('The Natural History Museum', 'For the history buffs and taxidermy fans.', 'London', 'Museum', '2025-07-24', '2026-12-31', 200.00, 1);
INSERT INTO spaces (name, description, location, type, start_date, end_date, price_per_night, user_id) VALUES ('Kensington Park', 'Very spacious and green. Perfect for a romantic getaway.', 'London', 'Park', '2025-07-24', '2026-12-31', 250.00, 2);
INSERT INTO spaces (name, description, location, type, start_date, end_date, price_per_night, user_id) VALUES ('The Tower of London', 'Very old. Very quaint. Lovely stuff.', 'London', 'Historic Site', '2025-07-24', '2026-12-31', 999.99, 3);


