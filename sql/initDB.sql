CREATE table users (
	primary key (id),
    id int NOT NULL AUTO_INCREMENT,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	account_type INT,
	password VARCHAR(30),
	email VARCHAR(30),
    points INT
);

CREATE table tasks (
	primary key (id),
    id int,
    name varchar(20),
    point_value INT,
    category_id INT,
    estimated_time datetime,
    description varchar(50),
    start_time datetime,
    estimated_completion_time datetime,
    status INT,
    image_path varchar(30),
    assigned_user_id int,
    created_user_id int
);
