CREATE TABLE tb_seg_auditoria
( 
  id_auditoria numeric  NOT NULL ,
  id_usuario numeric  NOT NULL ,  
  modulo varchar(100)  NULL , 
  link varchar(100)  NULL , 
  icono varchar(100)  NULL , 
  fecha_creacion date,
  CONSTRAINT pk_tb_auditoria PRIMARY KEY (id_auditoria)
);

CREATE TABLE tb_seg_funcionalidad (
	id_funcionalidad numeric NOT NULL,
	nombre_funcionalidad varchar(100) NULL,
	link varchar(100) NULL,
	icono varchar(100) NULL,
	fecha_creacion date null,
	CONSTRAINT pk_tb_seg_funcionalidad PRIMARY KEY (id_funcionalidad)
);