-- Tip Count Trigger

CREATE OR REPLACE FUNCTION UpdateTipCount()
RETURNS trigger AS '
BEGIN 
   UPDATE Users
   SET y_tip_count = y_tip_count + 1
   WHERE Users.y_user_id = NEW.y_user_id;
   UPDATE Business
   SET y_tip_count = y_tip_count + 1
   WHERE Business.y_business_id = NEW.y_business_id;
   RETURN NEW;
END
' LANGUAGE plpgsql; 

CREATE TRIGGER TipCount
AFTER INSERT ON Tip
FOR EACH ROW
WHEN (NEW.y_business_id IS NOT NULL)
EXECUTE PROCEDURE UpdateTipCount();

-- CheckIn Count Trigger
CREATE OR REPLACE FUNCTION UpdateCheckInCount()
RETURNS trigger AS '
BEGIN 
   UPDATE Business
   SET y_checkin_count = y_checkin_count + 1
   WHERE Business.y_business_id = NEW.y_business_id;
   RETURN NEW;
END
' LANGUAGE plpgsql; 

CREATE TRIGGER CheckInCount
AFTER INSERT ON Check_In
FOR EACH ROW
WHEN (NEW.y_business_id IS NOT NULL)
EXECUTE PROCEDURE UpdateCheckInCount();

-- TEST TRIGGERS
SELECT y_business_id, y_tip_count
FROM Business
WHERE y_business_id = '5KheTjYPu1HcQzQFtm4_vw';

SELECT y_user_id, y_tip_count
FROM Users
WHERE y_user_id = 'jRyO2V1pA4CdVVqCIOPc1Q';

INSERT INTO Tip (y_date, y_tip_text, y_user_id, y_business_id, y_like_count)
VALUES ('2010-11-23 16:19:50', 'New Tip to test trigger!', 'jRyO2V1pA4CdVVqCIOPc1Q', '5KheTjYPu1HcQzQFtm4_vw', 4);

SELECT y_business_id, y_tip_count
FROM Business
WHERE y_business_id = '5KheTjYPu1HcQzQFtm4_vw';

SELECT y_user_id, y_tip_count
FROM Users
WHERE y_user_id = 'jRyO2V1pA4CdVVqCIOPc1Q';

SELECT y_business_id, y_checkin_count
FROM Business
WHERE y_business_id = '5KheTjYPu1HcQzQFtm4_vw';

INSERT INTO Check_In (y_business_id, y_check_in_time)
VALUES ('5KheTjYPu1HcQzQFtm4_vw', '2010-11-23 16:19:55');

SELECT y_business_id, y_checkin_count
FROM Business
WHERE y_business_id = '5KheTjYPu1HcQzQFtm4_vw';