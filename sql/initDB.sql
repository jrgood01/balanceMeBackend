DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS tasks;

CREATE table users (
	PRIMARY KEY (id),
    	id int NOT NULL AUTO_INCREMENT,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	account_type INT,
	password VARCHAR(30),
	email VARCHAR(30),
    points INT
);

CREATE TABLE tasks (
	PRIMARY KEY(id),
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(40), 
	point_value INT, 
	category_id INT, 
	estimate_time INT, 
	description VARCHAR(100), 
	start_time time,
	estimated_completion_time time, 
	status INT, 
	completion_time time,
	image_path VARCHAR(50), 
	assigned_user_id INT, 
	created_user_id INT,
	history VARCHAR(100), 
	repeat_r BOOL, 
	active BOOL, 
	steps JSON);
