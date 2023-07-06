import manager
import json
import database_functions
import sample_data as smp

#manager.cursor.execute(database_functions.insert_coach_data,(1,'Melisa', 'Aydinci', "melisa@gmail.com","123","0534"))
#manager.cursor.execute(database_functions.insert_coach_data,coach_data)
#print(f'{new_program}')
#students=manager.cursor.execute("select programs from students where id=4")
#exist_c=manager.cursor.fetchall()
#existing_tuple = exist_c[0]
#existing_dict, = existing_tuple
#existing_dict.update(new_program)
#print(existing_dict)
#print(exist_c)
#print(exist_c[0]["program1"].update(new_program))

manager.cursor.execute(database_functions.insert_student_data,smp.student_data)
manager.cursor.execute(database_functions.insert_student_data,smp.another_student_data)

manager.cursor.execute(database_functions.insert_coach_data,(smp.coach_data))
manager.cursor.execute(database_functions.insert_coach_data,(smp.another_student_data))

manager.cursor.execute(database_functions.insert_student_to_coach,(0,0,3))
manager.cursor.execute(database_functions.insert_student_to_coach,(6,6,6))


manager.cursor.execute(database_functions.insert_program_to_studentprograms,(smp.new_program,"0"))
manager.cursor.execute(database_functions.insert_program_to_studentprograms,(smp.new_program,"6"))


manager.cursor.execute(database_functions.insert_student_data,smp.another_student_data)

#manager.cursor.execute(database_functions.delete_student,("0"))

manager.conn.commit()