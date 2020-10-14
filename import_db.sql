PRAGMA foreign_keys=ON;

BEGIN TRANSACTION;

DROP TABLE IF EXISTS paintings;
DROP TABLE IF EXISTS painters;

CREATE TABLE paintings (
    _id INTEGER PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    year INTEGER,
    painter_id INTEGER NOT NULL,

    FOREIGN KEY (painter_id) REFERENCES painters(_id)
);

CREATE TABLE painters (
    _id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birth_year INTEGER
);

INSERT INTO
    painters
    (name, birth_year)
VALUES
    ('Claude Monet',1840),
    ('Edvard Munch',1863),
    ('Rico Lebrun',1900),
    ('Betty Parsons',1900),
    ('Virginia True',1900),
    ('Andy Warhol',1928),
    ('Jasper Johns',1930),
    ('Robert Rauschenberg',1925),
    ('Frank Stella',1925),
    ('David Hockney',1937),
    ('Mark Rothko',1903),
    ('Jackson Pollock',1912),
    ('Henri Matisse',1869);

INSERT INTO
    paintings
    (title, year, painter_id)
VALUES
    ('Wisteria',1925,1),
    ('The Scream',1893,2),
    ('The Yellow Log',1912,2),
    ('The Haymaker',1917,2),
    ('Figure in Rain',1949,3),
    ('Musician',1940,3),
    ('Inferno Series - B',1961,3),
    ('Inferno Series - E',1961,3),
    ('Bright Day',1966,4),
    ('Cactus',1931,5),
    ('Empire',1964,6),
    ('Orange and Yellow',1956,11),
    ('Blue Poles',1952,12),
    ('Le bonheur de vivre',1905,13),
    ('Flag',1955,7),
    ('White Painting (Three Panel)',1951,8);

COMMIT;
