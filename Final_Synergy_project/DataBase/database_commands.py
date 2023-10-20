
create_command = """INSERT INTO Staff (first_name, second_name, last_name, phone_number, email, salary) VALUES (?, ?, ?, ?, ?, ?)"""

delete_command = """DELETE FROM Staff WHERE id = ?"""

update_command = """UPDATE Staff SET first_name = ?, second_name = ?, last_name = ?, phone_number = ?, email = ?, salary = ? 
                        WHERE id = ?"""

find_by_FCs = """SELECT * FROM Staff WHERE first_name = ? and second_name = ? and last_name = ? LIMIT 1"""

find_all_data = """SELECT * FROM Staff"""
