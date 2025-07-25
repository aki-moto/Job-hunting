create database accountbook
CREATE TABLE list(
    id INT  NOT NULL AUTO_INCREMENT COMMENT'ID',
    day DATE NOT NULL COMMENT'日付',
    type INT NOT NULL COMMENT'種類',
    title TEXT NOT NULL COMMENT'内訳',
    money INT NOT NULL COMMENT'金額',

    PRIMARY KEY(id)
)
