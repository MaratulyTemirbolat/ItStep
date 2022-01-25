CREATE TABLE customer(
    id serial PRIMARY KEY,
    name varchar(40) NOT NULL UNIQUE
);
-- Таблица названа во множественном числе,
-- потому что выдавалась ошибка, что слово зарезервировано, а так назвал бы "order"
CREATE TABLE orders(
    id serial PRIMARY KEY,
    purchase_date date NOT NULL,
    customer_id integer,
    CONSTRAINT fk_customer FOREIGN KEY(customer_id) REFERENCES customer(id)
);

CREATE TABLE category(
    id serial PRIMARY KEY,
    name varchar(30) NOT NULL UNIQUE
);

CREATE TABLE  good(
    id serial PRIMARY KEY,
    category_id integer,
    name varchar(20) NOT NULL UNIQUE,
    price double precision NOT NULL,
    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES category(id)
);

CREATE TABLE order_good(
    id serial PRIMARY KEY,
    order_id integer,
    good_id integer,
    quantity integer NOT NULL,
    CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES orders(id),
    CONSTRAINT fk_good FOREIGN KEY (good_id) REFERENCES  good(id)
);

