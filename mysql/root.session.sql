-- Create the 'books' table
CREATE TABLE IF NOT EXISTS `books` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `title` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`)
);

-- Create the 'users' table
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`)
);

-- Create the 'favorite_books' table
CREATE TABLE IF NOT EXISTS `favorite_books` (
    `user_id` INT NOT NULL,
    `book_id` INT NOT NULL,
    PRIMARY KEY (`user_id`, `book_id`),
    INDEX `fk_favorite_books_users_idx` (`user_id` ASC),
    INDEX `fk_favorite_books_books_idx` (`book_id` ASC),
    CONSTRAINT `fk_favorite_books_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_favorite_books_books`
    FOREIGN KEY (`book_id`)
    REFERENCES `books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);
