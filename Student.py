

students = {}

marks = {}

def add_student(sid, name,grade,age,address):

    students[sid] = {"name": name, "grade": grade, "age":age,"address":address}

def add_marks(sid, phy, chem,bio):
    marks[sid] = {"physics": phy, "checemisty": chem, "biology":bio}

def get_student(sid):
    return students.get(sid)


if __name__ == "__main__":
    add_student(1,"Bubun",10, 20, "address1")
    add_student(2, "Tapaswini", 9, 9, "address1")
    add_student(3, "Balia", 10, 20, "address1")
    add_student(4, "Haria", 10, 20, "address1")
    add_student(5, "Nalia", 8, 20, "address1")
    add_student(1, "Bubun", 10, 20, "address111112")
    add_marks(1,44,55,66)
    print("Students: " + get_student(1)["address"])
    print("Marks: ", str(marks[1]))







