import json

insert_coach_data = '''
    INSERT INTO coaches (id, name, surname, mail, password, telephone)
    SELECT %(id)s, %(name)s, %(surname)s, %(mail)s, %(password)s, %(telephone)s
    WHERE NOT EXISTS (
        SELECT 1 FROM coaches WHERE id = %(id)s
    );
'''
insert_student_data = '''
    INSERT INTO students (id,name, surname,mail,password,telephone,programs)
    SELECT %(id)s, %(name)s, %(surname)s, %(mail)s, %(password)s, %(telephone)s,%(programs)s::jsonb
    WHERE NOT EXISTS (
        SELECT 1 FROM students WHERE id = %(id)s
    );
'''
insert_program_data = '''
    INSERT INTO programs (id,class, subclass)
    SELECT (%(id)s,%(class)s, %(subclass)s)
    WHERE NOT EXISTS (
        SELECT 1 FROM programs WHERE id = %(id)s
    );;
'''
delete_coach = '''
    DELETE FROM IF EXISTS coaches WHERE id=%s;
'''
delete_student = '''
    DELETE FROM students WHERE id=%s;
'''
delete_program = '''
    DELETE FROM IF EXISTS programs WHERE id=%s;
'''
change_to_coach_password='''
    UPDATE coaches set password=%s WHERE id=%s;
'''
change_to_student_password='''
    UPDATE students set password=%s WHERE id=%s;
'''
#ilk 2 %s student id diğeri coach id bunu güncelleyecem aynı şeyin 2 kez tekrar etmesine ne gerek vars
insert_student_to_coach='''
    UPDATE coaches set student_list=CASE WHEN array_position(student_list,%s) IS NULL 
                                          THEN array_append(student_list,%s) 
                                          ELSE student_list
                                    END
                                          WHERE id=(%s);
'''
insert_program_to_studentprograms='''
    UPDATE students SET programs = jsonb_concat(programs::jsonb, %s::jsonb) WHERE id = %s
'''
return_program='''
    select name from students WHERE id=(%s)
'''
