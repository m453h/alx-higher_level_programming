#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the last argument passed.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    cursor = db.cursor()
    query = "SELECT `c`.`id`, `c`.`name`, `s`.`name` FROM `cities` as `c`\
    INNER JOIN `states` as `s` ON `c`.`state_id` = `s`.`id`\
     WHERE `s`.`name` LIKE BINARY %s\
      ORDER BY `c`.`id` ASC"
    cursor.execute(query, (sys.argv[4],))
    cities = cursor.fetchall()
    for city in cities:
        print(city)
