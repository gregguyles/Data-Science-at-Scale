SELECT summed
FROM (
    SELECT row_num, col_num, sum(prod) as summed
    from (
        SELECT a.row_num AS row_num, 
               b.col_num AS col_num,
               a.value * b.value AS prod
        FROM A AS a, B AS b
        WHERE a.col_num = b.row_num
    )
    GROUP BY row_num, col_num
)
WHERE row_num = 2 AND col_num = 3
;
