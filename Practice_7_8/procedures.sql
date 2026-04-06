-- 3. Procedure: insert new user or update phone if name already exists
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;


-- 4. Procedure: insert many users from arrays
-- invalid phone numbers will be shown by NOTICE
CREATE OR REPLACE PROCEDURE insert_many_users(p_names VARCHAR[], p_phones VARCHAR[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    IF array_length(p_names, 1) IS DISTINCT FROM array_length(p_phones, 1) THEN
        RAISE EXCEPTION 'Arrays must have the same length';
    END IF;

    FOR i IN 1..array_length(p_names, 1) LOOP
        IF p_phones[i] ~ '^\+?[0-9]{10,15}$' THEN
            IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_names[i]) THEN
                UPDATE phonebook
                SET phone = p_phones[i]
                WHERE name = p_names[i];
            ELSE
                INSERT INTO phonebook(name, phone)
                VALUES (p_names[i], p_phones[i]);
            END IF;
        ELSE
            RAISE NOTICE 'Incorrect data: %, %', p_names[i], p_phones[i];
        END IF;
    END LOOP;
END;
$$;


-- 5. Procedure: delete by name or phone
CREATE OR REPLACE PROCEDURE delete_user(p_value VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = p_value OR phone = p_value;
END;
$$;