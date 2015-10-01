--CREATE VIEW keyword AS
--    SELECT * FROM Frequency
--    UNION
--    SELECT 'q' as docid, 'washington' as term, 1 as count
--    UNION
--    SELECT 'q' as docid, 'taxes' as term, 1 as count
--    UNION
--   SELECT 'q' as docid, 'treasury' as term, 1 as count
SELECT max(summed)
FROM (
    SELECT docid, sum(term_prod) AS summed
    FROM (
        SELECT  b.docid AS docid,
           a.term AS term, 
           a.count * b.count AS term_prod
        FROM (
            SELECT docid, term, count
            FROM keyword
            ) AS a
            , (
            SELECT docid, term, count
            FROM keyword
            ) AS b
        WHERE a.term = b.term 
        AND a.docid = 'q'
    )
    GROUP BY docid
)
;
