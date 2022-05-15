def studentEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": str(item["student_name"]),
        "email": str(item["student_email"]),
        "phone": str(item["student_phone"])
    }


def listOfStudentEntity(db_item_list) -> list:
    list_stud_entity = []
    for item in db_item_list:
        list_stud_entity.append(studentEntity(item))

    return list_stud_entity
