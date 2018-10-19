create table person(
   id INTEGER PRIMARY KEY,
   name varchar(50) not null,
   id_city INT not null,
   foreign key(id_city) references city(id)
);
