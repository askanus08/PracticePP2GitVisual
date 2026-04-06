-- 1. Function: search by pattern
-- searches by part of name or part of phone
CREATE OR REPLACE FUNCTION search_by_pattern(p_pattern TEXT)
RETURNS TABLE (
    id INT,
    name VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.name, pb.phone
    FROM phonebook pb
    WHERE pb.name ILIKE '%' || p_pattern || '%'
       OR pb.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- 2. Function: get contacts with pagination
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE (
    id INT,
    name VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.name, pb.phone
    FROM phonebook pb
    ORDER BY pb.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;