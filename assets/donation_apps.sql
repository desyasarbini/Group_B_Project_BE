-- create
CREATE TABLE donatur (
    id int PRIMARY KEY AUTO_INCREMENT, email varchar(100) NOT NULL, phone_number varchar(20) NOT NULL
);

-- insert
INSERT INTO
    donatur (email, phone_number)
VALUES (
        'testing@test.com', '099988293399'
    ),
    (
        'donatur@test.com', '628123456998'
    );

-- fetch
SELECT * FROM donatur;

CREATE TABLE admin (
    id int PRIMARY KEY AUTO_INCREMENT, username varchar(50) NOT NULL, password varchar(50) NOT NULL
);

INSERT INTO
    admin (username, password)
VALUES ('admin', 'admin'),
    ('admin2', 'admin2');

SELECT * FROM admin;

CREATE TABLE project (
    id int PRIMARY KEY AUTO_INCREMENT, 
    project_image varchar(255) NOT NULL, 
    project_name varchar(255) NOT NULL, 
    description varchar(655) NOT NULL,
    target_amount DECIMAL(12,2) DEFAULT 0.00,
    collected_amount decimal(12, 2) default 0.00,
    percentage decimal(3, 2) default 0.00, 
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    end_date TIMESTAMP,  
    admin_id int,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    foreign key (admin_id) references admin (id)
);

DROP TABLE project;

DROP TABLE admin;

INSERT INTO
    project (
        project_image, project_name, description, end_date, target_amount, admin_id
    )
VALUES (
        'qjdwhqfbqbf.com', 'bantuan bencana', 'terjadi bencana alam dibeberapa tempat', '2024-04-30', 2000000.00, 1
    ),
    (
        'https://ibb.co/2ddejid', 'kegiatan go green', 'ayok tanam pohon', '2024-05-30', 2900000.00, 1
    ),
    (
        'https://ibb.co/SJD8nzw', 'Berbagi buku cerita', 'untuk anak-anak yang membutuhkan', '2024-05-22', 3000000.00, 1
    );

CREATE TABLE donation (
    id int PRIMARY KEY AUTO_INCREMENT, donatur_id int, project_id int, amount decimal(10, 2), donation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, foreign key (donatur_id) references donatur (id), foreign key (project_id) references project (id)
);

DROP TABLE donation;

INSERT INTO
    donation (
        donatur_id, project_id, amount
    )
VALUES (1, 2, 2000.00),
    (2, 2, 50000.00),
    (1, 2, 70000.00),
    (2, 2, 970000.00),
    (1, 1, 235000.00),
    (2, 2, 970000.00),
    (1, 1, 235000.00),
    (1, 3, 235000.00);

SELECT * FROM donation;

UPDATE project p
SET
    p.collected_amount = (
        SELECT SUM(d.amount)
        FROM donation d
        WHERE
            d.project_id = p.id
    ),
    p.percentage_donation = (
        collected_amount / target_amount
    ) * 100;

SELECT * FROM project;