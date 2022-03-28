-- Tip Count Trigger

CREATE OR REPLACE FUNCTION UpdateTipCount()
RETURNS trigger AS '
BEGIN 
   UPDATE Users
   SET y_tip_count = y_tip_count + 1
   WHERE Users.y_user_id = NEW.y_user_id;
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
SELECT y_user_id, y_tip_count
FROM Users
;
