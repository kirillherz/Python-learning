 CREATE TABLE IF NOT EXISTS person(
   id INTEGER PRIMARY KEY,
   name varchar(50) not null,
   id_city INT not null,
   foreign key(id_city) references city(id)
);

 CREATE TABLE IF NOT EXISTS city(
    id INTEGER PRIMARY KEY,
    name varchar(50) not null
);

CREATE TABLE IF NOT EXISTS author(
    id INTEGER PRIMARY KEY,
    name varchar(50) not null
);

CREATE TABLE IF NOT EXISTS book(
    id INTEGER PRIMARY KEY,
    name varchar(50) not null
);

