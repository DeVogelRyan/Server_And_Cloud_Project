CREATE DATABASE Project;
use Project;

CREATE TABLE 'user' (
  'id' int unsigned NOT NULL AUTO_INCREMENT,
  'name' varchar(50) NOT NULL
  PRIMARY KEY ('id')
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert  into 'user'('id','name') values (1,'Soumitra Roy'),