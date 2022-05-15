# import
from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity


student_router = APIRouter()


# get all student
@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(connection.local.student.find())


# create student
@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())


# update
@student_router.put('/students/{studentId}')
async def update_student(studentId, student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())


# delete
@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())


@student_router.get('/hello')
async def hello_world():
    return "Hello World"
