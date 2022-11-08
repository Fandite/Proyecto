create database proy;
use proy;
create table area( 
idArea int(15) PRIMARY KEY AUTO_INCREMENT,
descrp varchar(45) NOT NULL
);
insert into area(idArea, descrp) values (1, "Ventas"), (2, "Informática");

create table carrera( 
idCarrera int(15) PRIMARY KEY AUTO_INCREMENT,
descrp varchar(45) NOT NULL
);
insert into carrera(idCarrera, descrp) values (1, "No apto"), (2, "Programación"),(3, "Estadística");

create table escolaridad( 
idEscolaridad int(15) PRIMARY KEY AUTO_INCREMENT,
descrp varchar(45) NOT NULL
);
insert into escolaridad(idEscolaridad, descrp) values (1, "No apto"), (2, "Universidad"), (3, "Bachillerato");

create table EstadoCiv( 
idEstadoCiv int(15) PRIMARY KEY AUTO_INCREMENT,
descrp varchar(45) NOT NULL
);
insert into EstadoCiv(idEstadoCiv, descrp) values (1, "Casado"), (2, "Unión libre"), (3, "Soltero");

create table GradoAv( 
idGradoAv int(15) PRIMARY KEY AUTO_INCREMENT,
descrp varchar(45) NOT NULL
);
insert into GradoAv(idGradoAv, descrp) values (1, "No apto"), (2, "Bueno"), (3, "Medio");

create table Habilidades( 
idHabili int(15) PRIMARY KEY AUTO_INCREMENT,
descrp varchar(45) NOT NULL
);
insert into Habilidades(idHabili, descrp) values (1, "NO REQUERIDAS"), (2, "Ágil"), (3, "Tolerante"), (4, "Pacífico");

create table Idioma( 
idIdioma int(15) PRIMARY KEY AUTO_INCREMENT,
descrp varchar(45) NOT NULL
);
insert into Idioma(idIdioma, descrp) values (1, "NO REQUERIDAS"), (2, "Inglés"), (3, "Hindi"), (4, "Musulmán");

create table MedioPub( 
idMedioPub int(15) PRIMARY KEY AUTO_INCREMENT,
descrp varchar(45) NOT NULL
);


CREATE TABLE `puesto` (
  `idPuesto` int(11) NOT NULL auto_increment primary key,
  `codPuesto` varchar(15) NOT NULL,
  `idArea` int(11) NOT NULL,
  `nomPuesto` varchar(50) NOT NULL,
  `puestoJefeSup` varchar(50) NOT NULL,
  `jornada` varchar(70) NOT NULL,
  `remunMensual` int(11) NOT NULL,
  `prestaciones` varchar(70) NOT NULL,
  `descripcionGeneral` varchar(250) NOT NULL,
  `funciones` varchar(250) NOT NULL,
  `edad` varchar(50) NOT NULL,
  `sexo` varchar(15) NOT NULL,
  `idEstadoCivil` int(11) NOT NULL,
  `idEscolaridad` int(11) NOT NULL,
  `idGradoAvance` int(11) NOT NULL,
  `idCarrera` int(11) NOT NULL,
  `experiencia` varchar(70) NOT NULL,
  `conocimientos` varchar(70) NOT NULL,
  `manejoEquipo` varchar(70) NOT NULL,
  `reqFisicos` varchar(70) NOT NULL,
  `reqPsicologicos` varchar(70) NOT NULL,
  `responsabilidades` varchar(70) NOT NULL,
  `condicionesTrabajo` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

insert into puesto(idPuesto, codPuesto, idArea, nomPuesto, puestoJefeSup, jornada, remunMensual, prestaciones, descripcionGeneral, funciones,edad, sexo, idEstadoCivil, idEscolaridad, idGradoAvance, idCarrera, experiencia,conocimientos,manejoEquipo,reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo) values ("1", "V009", "2", "Supervisor de equipo", "Supervisor", "Lunes a viernes", 5000, "De ley", "Dar mantenimiento de computo", "Mantenimiento de cómputo", "45 años", "Indistinto", "2", "2", "3", "2", "2 años", "Programación", "De computo", "Hábil con las manos", "Estable mentalmente", "Inventario", "Buenas");


ALTER TABLE `puesto`
  ADD KEY `idEscolaridad` (`idEscolaridad`),
  ADD KEY `idEstadoCivil` (`idEstadoCivil`),
  ADD KEY `idGradoAvance` (`idGradoAvance`),
  ADD KEY `idCarrera` (`idCarrera`),
  ADD KEY `area` (`idArea`);
  
alter table `proy`.`puesto`
  add constraint `Esco_Puesto_Rel` foreign key (`idEscolaridad`) references `escolaridad`(`idEscolaridad`),
  add constraint `EstCiv_Puesto_Rel` foreign key (`idEstadoCivil`) references `estadociv`(`idEstadoCiv`),
  add constraint `Grado_Puesto_Rel` foreign key (`idGradoAvance`) references `gradoav`(`idGradoAv`),
  add constraint `Carrera_Puesto_Rel` foreign key (`idCarrera`) references `carrera`(`idCarrera`),
  add constraint `Area_Puesto_Rel` foreign key (`idArea`) references `area`(`idArea`);

create table puesto_has_habilidades(
  `idPuesto` int(11),
  `idHabili` int(11), 
  primary key (`idPuesto`, `idHabili`)
);

ALTER TABLE `puesto_has_habilidades`
  ADD KEY `idHabili` (`idHabili`),
  ADD KEY `idPuesto` (`idPuesto`),
  add constraint `Hab_Has_Rel` foreign key (`idHabili`) references `Habilidades`(`idHabili`),
  add constraint `Puesto_Has_Rel` foreign key (`idPuesto`) references `Puesto`(`idPuesto`);

create table puesto_has_idiomas(
  `idPuesto` int(11),
  `idIdioma` int(11),
  primary key (`idPuesto`, `idIdioma`)
);
ALTER TABLE `puesto_has_idiomas`
  ADD KEY `idIdioma` (`idIdioma`),
  ADD KEY `idPuesto` (`idPuesto`),
  add constraint `Idi_Has_Rel` foreign key (`idIdioma`) references `Idioma`(`idIdioma`),
  add constraint `Puesto_Idio_Rel` foreign key (`idPuesto`) references `Puesto`(`idPuesto`);

insert into puesto_has_habilidades(idPuesto,idHabili) values ("1", "2"), ("1", "3"), ("1", "4");
insert into puesto_has_idiomas(idPuesto,idIdioma) values ("1", "2"), ("1", "4");

create table requisicion(
  idReq int(11) auto_increment not null,
  Folio varchar(25) not null,
  FechaElab date not null,
  FechaRec date not null,
  FechaIni date not null,
  MotivoReq varchar(30) not null,
  MotivoEspe varchar(70) not null,
  TipoVac varchar(15) not null,
  NomSol varchar(70) not null,
  NomAutoriza varchar(70) not null,
  NomRev varchar(70) not null,
  Autorizar int(1) not null,
  idPuesto int(11) not null,
  idArea int(11) not null,
  PRIMARY KEY (`idReq`),
  KEY (`idArea`),
  KEY (`idPuesto`),
  constraint `Llave_Req_Area` 
  foreign key (`idArea`)
  references `proy`.`area`(`idArea`),
  constraint `Llave_Req_Pue` 
  foreign key (`idPuesto`)
  references `proy`.`puesto`(`idPuesto`)
);

