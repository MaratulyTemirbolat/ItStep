CREATE TABLE product_type
(
    id   serial PRIMARY KEY,
    name varchar(50) NOT NULL UNIQUE
);

CREATE TABLE nomenclature_group
(
    id                       serial PRIMARY KEY,
    abbreviation             varchar(5)         NOT NULL,
    abbreviation_description varchar(30) UNIQUE NOT NULL
);

CREATE TABLE category
(
    id                    serial PRIMARY KEY,
    name                  varchar(100) UNIQUE NOT NULL,
    nomenclature_group_id integer             NOT NULL,
    CONSTRAINT fk_nomenclature_group_id FOREIGN KEY (nomenclature_group_id) REFERENCES nomenclature_group (id) ON DELETE RESTRICT
);

CREATE TABLE manufacturer
(
    id         serial PRIMARY KEY,
    brand_name varchar(15) NOT NULL UNIQUE
);

CREATE TABLE characteristics
(
    id   serial PRIMARY KEY,
    name varchar(50) UNIQUE NOT NULL
);

CREATE TABLE product
(
    id              serial PRIMARY KEY,
    wholesale_price integer             NOT NULL CHECK (wholesale_price > 0),
    internet_price  integer             NOT NULL CHECK (internet_price > 0),
    product_type_id integer             NOT NULL,
    category_id     integer             NOT NULL,
    manufacturer_id integer             NOT NULL DEFAULT 0,
    name            varchar(100) UNIQUE NOT NULL,
    CONSTRAINT fk_category_id FOREIGN KEY (category_id) REFERENCES category (id) ON DELETE SET NULL,
    CONSTRAINT fk_manufacturer_id FOREIGN KEY (manufacturer_id) REFERENCES manufacturer (id) ON DELETE SET DEFAULT,
    CONSTRAINT fk_product_type_id FOREIGN KEY (product_type_id) REFERENCES product_type (id) ON DELETE RESTRICT
);

CREATE TABLE good_characteristics
(
    id                 serial PRIMARY KEY,
    good_id            integer NOT NULL,
    characteristics_id integer NOT NULL,
    description        varchar(50),
    CONSTRAINT fk_good_id FOREIGN KEY (good_id) REFERENCES product (id) ON DELETE CASCADE,
    CONSTRAINT fk_characteristics_id FOREIGN KEY (characteristics_id) REFERENCES characteristics (id) ON DELETE NO ACTION
);

INSERT INTO product_type(name)
VALUES ('Планшет'),
       ('Смартфон'),
       ('Планшетный компьютер'),
       ('Подставка-зарядка');

INSERT INTO manufacturer(brand_name)
VALUES ('Elenberg'),
       ('Hier'),
       ('Huawei'),
       ('Lenovo'),
       ('Samsung'),
       ('Apple');
INSERT INTO manufacturer(brand_name)
VALUES ('Bravis'),
       ('Defender'),
       ('A-case');

INSERT INTO nomenclature_group(abbreviation, abbreviation_description)
VALUES ('TC', 'Телекоммуникации');

INSERT INTO category
VALUES (0413, 'Цифровые устройства', 1),
       (0501, 'Сотовые телефоны', 1),
       (0504, 'Мультифункциональное устройство', 1),
       (0709, 'Кабели, адаптеры, переходники, переноски', 1);

INSERT INTO characteristics
VALUES (2, 'Диагональ'),
       (3, 'Процессор'),
       (4, 'Тип защиты'),
       (5, 'Сим карта'),
       (6, 'Тип аккумулятора'),
       (7, 'RAM'),
       (8, 'Память'),
       (9, 'Передняя Камера'),
       (10, 'Емкость батареи'),
       (11, 'Задняя Камера'),
       (12, 'Версия ОС'),
       (13, 'ОС');

INSERT INTO product
VALUES (61800, 15980, 16400, 1, 0413, 1, 'TAB730 (Black)'),
       (73094, 14663, 18420, 1, 0413, 2, 'E700G-B (Black)'),
       (69950, 34409, 39920, 1, 0413, 3, 'MediaPad T1 7.0 3G (T1-701U) Silver'),
       (70813, 33426, 34900, 1, 0413, 4, 'TAB3 710I 3G 8GB'),
       (72159, 150108, 169900, 2, 0501, 6, 'iPhone 6 32Gb 2017 (Space Gray) MQ3D2RM/A/'),
       (69924, 260873, 269990, 2, 0501, 6, 'iPhone 6s 128GB Gold (MKQV2)'),
       (65925, 269980, 269990, 2, 0501, 6, 'iPhone 6s 128GB Rose Gold (MKQW2)'),
       (73447, 60215, 69990, 2, 0501, 3, 'GR3 2017 (DIG-L21 ) Gold'),
       (70147, 18704, 19990, 3, 0504, 7, 'NB74 7" 3G (black)'),
       (70959, 1161, 1490, 4, 0504, 8, 'Автомобильное зарядное устр-во (83517)  ACA-01-5V1А для iPhone'),
       (58288, 480, 490, 4, 0504, 1, 'CA472 Iphone cable (6937510858859)');

INSERT INTO good_characteristics(good_id, characteristics_id, description)
VALUES (61800, 2, '7.0'),
       (61800, 4, 'IPS1024X600'),
       (61800, 3, 'двух ядерный процессор MTK8312'),
       (73094, 3, 'MTK 6572M 1,0 ГГц,двухъядерный'),
       (73094, 13, 'Android™ KitKat 4.4'),
       (73094, 10, '2800 м·Ач'),
       (73094, 6, 'литий-полимерный'),
       (69950, 9, '2MP'),
       (69950, 11, '2MP'),
       (69950, 3, 'Quad Core A7'),
       (70813, 7, '8Gb'),
       (70813, 11, '2MP'),
       (72159, 13, 'IOS 8'),
       (72159, 8, '32 Гб'),
       (72159, 11, '8 МП'),
       (69924, 9, '128GB'),
       (69924, 13, 'IOS 13'),
       (69924, 3, 'A9 (64 bit)'),
       (65925, 7, '2GB'),
       (65925, 3, 'A9 (64 bit)'),
       (73447, 5, '2 SIM'),
       (73447, 13, 'Android 6.0 Marshmallow');

CREATE INDEX product_code_index ON product (id);
CREATE INDEX nomenclature_group_index ON nomenclature_group (abbreviation_description);


SELECT p.id AS poduct_code,
       CONCAT(n_g.abbreviation, ' (', n_g.abbreviation_description, ')') AS nomenclature_group,
       CONCAT(cat.id, ' ', cat.name) AS category,
       m.brand_name AS brand,
       CONCAT(p.name, '/', p_t.name, ' ', m.brand_name) AS nomenclature,
       p.wholesale_price,
       p.internet_price,
       CONCAT(char.name, ': ', g_c.description) AS description
FROM product p
         JOIN good_characteristics g_c
              ON p.id = g_c.good_id
         JOIN characteristics char
              ON char.id = g_c.characteristics_id
         JOIN product_type p_t
              ON p_t.id = p.product_type_id
         JOIN manufacturer m
              ON m.id = p.manufacturer_id
         JOIN category cat
              ON cat.id = p.category_id
         JOIN nomenclature_group n_g
              ON n_g.id = cat.nomenclature_group_id;

