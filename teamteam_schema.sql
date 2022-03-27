-- Emma Mickas
-- Connor Dellwo
-- Reagan Kelley
-- Abhiram Bondada


CREATE TABLE Business ( -- done
	y_business_id CHAR(33),
	y_business_name VARCHAR NOT NULL,
	y_rating INT,
	y_review_count INT DEFAULT 0,
	y_checkin_count INT DEFAULT 0,
	y_tip_count INT DEFAULT 0,
	y_open_status BOOLEAN,
	y_city VARCHAR,
	y_state VARCHAR,
	y_zipcode VARCHAR,
    y_latitude FLOAT,
    y_longitude FLOAT,
	PRIMARY KEY (y_business_id)
);

CREATE TABLE Categories ( -- multi valued variable of business -- done
	y_category_name VARCHAR,
	y_business_id CHAR(33),
    PRIMARY KEY (y_business_id, y_category_name),
    FOREIGN KEY (y_business_id) REFERENCES Business(y_business_id)
);

CREATE TABLE Users ( -- done
	y_user_id CHAR(33),
	y_tip_like_count INTEGER DEFAULT 0,
	y_tip_count INTEGER DEFAULT 0,
	y_avg_stars DECIMAL,
	y_num_fans INTEGER,
	y_user_name VARCHAR NOT NULL,
	y_vote_count INTEGER DEFAULT 0,
	y_date_joined DATE,
	y_longitude DECIMAL, --composite
	y_latitude DECIMAL, --composite
    PRIMARY KEY (y_user_id)
);

CREATE TABLE Friends_With ( -- done
	y_user_id_friender CHAR(33),
	y_user_id_friended CHAR(33),
	PRIMARY KEY (y_user_id_friender, y_user_id_friended),
	FOREIGN KEY (y_user_id_friender) REFERENCES Users(y_user_id),
	FOREIGN KEY (y_user_id_friended) REFERENCES Users(y_user_id)
);

CREATE TABLE Tip ( -- done
	y_date TIMESTAMP,
	y_tip_text VARCHAR,
	y_user_id CHAR(33),
	y_business_id CHAR(33),
	PRIMARY KEY (y_user_id, y_business_id, y_date),
	FOREIGN KEY (y_user_id) REFERENCES Users(y_user_id),
	FOREIGN KEY (y_business_id) REFERENCES Business(y_business_id)
);

CREATE TABLE Business_Hours ( -- done
	y_day  CHAR(9),
	y_Opening_time TIME,
	y_closing_time TIME,
	y_business_id CHAR(33),
    PRIMARY KEY (y_day, y_business_id),
    FOREIGN KEY (y_business_id) REFERENCES Business(y_business_id)
);

CREATE TABLE Attribute ( -- done
	y_attribute_name CHAR(30),
	y_attribute_value VARCHAR,
	y_business_id CHAR(33),
	PRIMARY KEY (y_attribute_name, y_business_id),
	FOREIGN KEY (y_business_id) REFERENCES Business(y_business_id)
);

CREATE TABLE Check_In( -- done
	y_business_id CHAR(33),
	y_check_in_time TIMESTAMP, --in the format yyyy-mm-dd hh:mm:ss
	PRIMARY KEY (y_business_id,y_check_in_time),
	FOREIGN KEY (y_business_id) REFERENCES Business(y_business_id)
);
