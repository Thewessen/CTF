USE wafwaf;

CREATE TABLE IF NOT EXISTS notes (
    id int auto_increment primary key,
    note varchar(256),
    assignee varchar(128)
);

INSERT INTO notes (note, assignee) VALUES ('Hello, world!', 'json');
