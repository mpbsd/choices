create table if not exists campus(
  id int not null,
  name char(10) not null,
  primary key(id)
);

create table if not exists curso(
  id int not null,
  name char(25) not null,
  primary key(id) 
);

create table if not exists disciplina(
  id int not null,
  name char(38) not null,
  primary key(id) 
);

create table if not exists exercicio(
  campus int not null,
  curso int not null,
  disciplina int not null,
  horario char(7) not null,
  semestre char(6) not null,
  foreign key(campus) references campus(id),
  foreign key(curso) references curso(id),
  foreign key(disciplina) references disciplina(id),
  primary key(campus, curso, disciplina, horario, semestre)
);

.mode csv
.separator ;
.import campus.csv campus
.import curso.csv curso
.import disciplina.csv disciplina
.import exercício.csv exercício
.mode table
