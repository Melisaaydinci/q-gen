import json

coach_data = {
    'id': 3,
    'name': 'John',
    'surname': 'Doe',
    'mail': 'john.doe@example.com',
    'password': 'pass123',
    'telephone': '123456789',
    'student_list':[]
}
another_coach_data = {
    'id': 2,
    'name': 'ertugrul',
    'surname': 'Doe',
    'mail': 'john.doe@example.com',
    'password': 'pass123',
    'telephone': '123456789',
    'student_list':[]
}

student_data = {
    'id': 6,
    'name': 'Melisa',
    'surname': 'aydnc',
    'mail': 'john.doe@example.com',
    'password': 'pass123',
    'telephone': '123456789',
    'programs':json.dumps({"program1":{
                "ders1":{
                "ders":"Matematik",
                "konu":"Fonksiyon",
                "video_id":0,
                "kalan_sure":0
                },
                "ders2":{
                "ders":"Türkçe",
                "konu":"Paragraf",
                "video_id":0,
                "kalan_sure":0
                }} ,
                "program2":{
                "ders1":{
                "ders":"Fen",
                "konu":"Hücre",
                "video_id":0,
                "kalan_sure":0
                },
                "ders2":{
                "ders":"Sosyal",
                "konu":"Savas",
                "video_id":0,
                "kalan_sure":0
                }}
            })
}

another_student_data={
    'id': 0,
    'name': 'John',
    'surname': 'Doe',
    'mail': 'john.doe@example.com',
    'password': 'pass123',
    'telephone': '123456789',
    'programs':json.dumps({})

}
new_program=json.dumps(
    {
    "program222": {
        "ders1": {"ders": "Matematik",
                  "konu": "Fonksiyon", 
                  "video_id": 0, 
                  "kalan_sure": 0}, 
        " ders2": {"ders": "Türkçe",
                  "konu": "Paragraf", 
                  "video_id": 0, 
                  "kalan_sure": 0}
                  }
    })
new_ders=json.dumps(
    {"ders3": {
        "ders": "Matematik", 
        "konu": "Fonksiyon",
        "video_id": 0, 
        "kalan_sure": 0}})