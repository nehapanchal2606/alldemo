student_lst = []
while True:

    print("-----------Student Management System--------------")
    print("1. Display Students List")
    print("2. Add Student Details")
    print("3. Search for Student")
    print("4. Delete Student from List")
    print("5. Update Student List")
    print("6. Sorting Student List")
    print("0. Exit")
    print("-" * 25)


    try:
        user_input = int(input("Enter choice :"))
    except ValueError:
        print("x" * 50)
        print("Choice must be an integer!!!")
        continue

    print("-" * 25)
    if user_input == 0:
        print("exit!!")
        print("-" * 25)
        break

    elif user_input == 1:
        if student_lst == []:
            print("There is no record!!!")
            print("-" * 25)
        else:
            for i in range(len(student_lst)):
                print("Student Roll Number:", student_lst[i]["roll_no"])
                print("Student Name:", student_lst[i]["name"])
                print("Student Gender:", student_lst[i]["gender"])
                print("Student Age:", student_lst[i]["age"])
                print("Student Department:", student_lst[i]["department"])
                print("Student Semester:", student_lst[i]["semester"])
                print("Student Subjects:", student_lst[i]["subject"])
                print("\n")
                print("-" * 25)

    elif user_input == 2:
        add_dict = {}
        try:
            enter_len = int(input("Number of Student Record you want to Add : "))
        except:
            print("not valid!!!")
            continue
        for record in range(0, enter_len):
            try:
                roll_num = int(input("Roll Number:"))
            except:
                print("not valid!!!")
                continue
            else:
                name = str(input("Name:"))
                gender = str(input("Gender:"))
                age = int(input("Age:"))
                department = str(input("Department:"))
                sem = int(input("Sem:"))
                add_sub_dict = {}
                add_dict.update(
                    {"roll_no": roll_num, "name": name, "gender": gender, "age": age, "department": department,
                     "semester": sem, "subject": [add_sub_dict]})

            add_sub_dict = {}
            enter_num_of_sub = int(input("Number of subject you want to Add: "))
            for subject in range(0, enter_num_of_sub):
                sub_code = int(input("Subject Code:"))
                sub_name = input("Subject Name:")
                add_sub_dict.update({"sub_code": sub_code, "sub_name": sub_name})
                add_dict.update(add_sub_dict)
            add_dict.update(add_sub_dict)

            student_lst.append(add_dict)
        for i in student_lst:
            for j in i.items():
                if j[0] == 'subject':
                    print(j)
                    print(j[0], ':')
                    for subject in j[1]:
                        print('\t', 'sub_code', '-', i['sub_code'], '\t', 'sub_name', '-',
                              i['sub_name'])
                    print('-' * 80)
                else:
                    print(j[0], ':', j[1])


    elif user_input == 3:
        while True:
            print("Search Options :")
            print("1. Roll Number Wise")
            print("2. Name Wise")
            print("3. Department Wise")
            print("0. Exit")

            try:
                srch = int(input("Search as:"))
            except ValueError:
                print("x" * 50)
                print("Choice must be an integer")
                continue

            if srch == 1:
                srch_rn = int(input("Enter Roll Number to Search:"))
                srch_data = []
                for i in student_lst:
                    if i["roll_no"] == srch_rn:
                        srch_data.append(i)
                        print("Student is:", srch_data)
                    else:
                        print("Student Not Found!!!")
            elif srch == 2:
                srch_rn = str(input("Please Provide Name for Search:"))
                for i in range(len(student_lst)):
                    if (student_lst[i]["name"][0:2] == srch_rn or student_lst[i]["name"][0] == srch_rn or
                        student_lst[i]["name"][0:] == srch_rn) == True:
                        print("Students are:")
                        print(student_lst[i])
                    else:
                        print("Student Not Found!!!")
            elif srch == 3:
                srch_rn = str(input("Please Provide Department Name for Search:"))
                for i in range(len(student_lst)):
                    if (student_lst[i]["department"][0:2] == srch_rn or student_lst[i]["name"][0] == srch_rn or
                        student_lst[i]["name"][0:] == srch_rn) == True:
                        print("Students are:")
                        print(student_lst[i])
                    else:
                        print("Student Not Found!!!")
            elif srch == 0:
                print("exit")
                break

            else:
                print("invalid choice!!")

    elif user_input == 4:
        if student_lst == []:
            print("There is no record!!!")
            print("-" * 25)
        else:
            for i in range(len(student_lst)):
                print("Student Roll Number:", student_lst[i]["roll_no"])
                print("Student Name:", student_lst[i]["name"])
                print("Student Gender:", student_lst[i]["gender"])
                print("Student Age:", student_lst[i]["age"])
                print("Student Department:", student_lst[i]["department"])
                print("Student Semester:", student_lst[i]["semester"])
                print("Student Subjects:", student_lst[i]["subject"])
                print("\n")
                print("-" * 25)
        stu_rn = int(input("Enter Roll Number to Delete:"))
        for i in range(len(student_lst)):
            if student_lst[i]["roll_no"] == stu_rn:
                del student_lst[i]
                print("After Delete Record is:", student_lst)
                break
            else:
                print("Student Record Not Available!!!")

    elif user_input == 5:

        if student_lst == []:
            print("There is no record!!!")
            print("-" * 25)
        else:
            for i in range(len(student_lst)):
                print("Student Roll Number:", student_lst[i]["roll_no"])
                print("Student Name:", student_lst[i]["name"])
                print("Student Gender:", student_lst[i]["gender"])
                print("Student Age:", student_lst[i]["age"])
                print("Student Department:", student_lst[i]["department"])
                print("Student Semester:", student_lst[i]["semester"])
                print("Student Subjects:", student_lst[i]["subject"])
                print("\n")
                print("-" * 25)

        print("-" * 25)
        print("1. Update Name")
        print("2. Update Gender")
        print("3. Update Age")
        print("4. Update Department")
        print("5. Update Sem")
        print("0. Exit")
        while True:
            try:
                user_ip = int(input("What Do you Want to Update?"))
            except ValueError:
                print("x" * 50)
                print("Choice must be an integer!!!")
                continue

            if user_ip == 0:
                print("exit")
                break
            elif user_ip == 1:
                old_nm = str(input("Enter old Name : "))
                new_nm = str(input("Enter new Name: "))
                for i in student_lst:
                    if i["name"] == old_nm:
                        i["name"] = new_nm
                        print("RECORD UPDATED!!!", i)

            elif user_ip == 2:
                old_gen = str(input("Enter old Gender : "))
                new_gen = str(input("Enter new Gender: "))
                for i in student_lst:
                    if i["gender"] == old_gen:
                        i["gender"] = new_gen
                        print("RECORD UPDATED!!!", i)

            elif user_ip == 3:
                old_age = int(input("Enter old Age : "))
                new_age = int(input("Enter new Age: "))
                for i in student_lst:
                    if i["age"] == old_age:
                        i["age"] = new_age
                        print("RECORD UPDATED!!!", i)

            elif user_ip == 4:
                old_dep = str(input("Enter old Department : "))
                new_dep = str(input("Enter new Department: "))
                for i in student_lst:
                    if i["department"] == old_dep:
                        i["department"] = new_dep
                        print("RECORD UPDATED!!!", i)

            elif user_ip == 5:
                old_sem = int(input("Enter old semester : "))
                new_sem = int(input("Enter new semester: "))
                for i in student_lst:
                    if i["semester"] == old_sem:
                        i["semester"] = new_sem
                        print("RECORD UPDATED!!!", i)

            else:
                print("enter valid choice!!!")
                continue

    elif user_input == 6:
        while True:
            print("-" * 25)
            print("1. Roll No wise Sorting")
            print("2. Name wise Sorting")
            print("3. Gender wise Sorting")
            print("4. Age wise Sorting")
            print("5. Department wise Sorting")
            print("6. Semester wise Sorting")
            print("0. Exit")
            print("-" * 25)

            try:
                 user_ip = int(input("Sorting Options :"))
            except ValueError:
                 print("x" * 50)
                 print("Choice must be an integer")
                 continue
            if user_ip == 0:
                 print("EXIT!!!")
                 break

            elif user_ip == 1:
                  print("1. For Ascending order:")
                  print("2. For Descending order:")
                  ip = int(input("Please Enter your Choice:"))
                  if ip == 1:
                      print("Sorting Roll Number in Ascending order:")
                      print(sorted(student_lst, key=lambda i: i['roll_no']))
                  elif ip == 2:
                      print("Sorting Roll Number in Descending order:")
                      print(sorted(student_lst, key=lambda i: i['roll_no'], reverse=True))

            elif user_ip == 2:
                  print("1. For Ascending order:")
                  print("2. For Descending order:")
                  ip = int(input("Please Enter your Choice:"))
                  if ip == 1:
                     print("Sorting Name in Ascending order:")
                     print(sorted(student_lst, key=lambda i: i['name']))
                  elif ip == 2:
                      print("Sorting Name in Descending order:")
                      print(sorted(student_lst, key=lambda i: i['name'], reverse=True))

            elif user_ip == 3:
                  print("1. For Ascending order:")
                  print("2. For Descending order:")
                  ip = int(input("Please Enter your Choice:"))
                  if ip == 1:
                     print("Sorting Gender in Ascending order:")
                     print(sorted(student_lst, key=lambda i: i['gender']))
                  elif ip == 2:
                      print("Sorting Gender in Descending order:")
                      print(sorted(student_lst, key=lambda i: i['gender'], reverse=True))

            elif user_ip == 4:
                  print("1. For Ascending order:")
                  print("2. For Descending order:")
                  ip = int(input("Please Enter your Choice:"))
                  if ip == 1:
                     print("Sorting Age in Ascending order:")
                     print(sorted(student_lst, key=lambda i: i['age']))
                  elif ip == 2:
                      print("Sorting Age in Descending order:")
                      print(sorted(student_lst, key=lambda i: i['age'], reverse=True))

            elif user_ip == 5:
                  print("1. For Ascending order:")
                  print("2. For Descending order:")
                  ip = int(input("Please Enter your Choice:"))
                  if ip == 1:
                     print("Sorting Department in Ascending order:")
                     print(sorted(student_lst, key=lambda i: i['department']))
                  elif ip == 2:
                      print("Sorting Department in Descending order:")
                      print(sorted(student_lst, key=lambda i: i['department'], reverse=True))

            elif user_ip == 6:
                  print("1. For Ascending order:")
                  print("2. For Descending order:")
                  ip = int(input("Please Enter your Choice:"))
                  if ip == 1:
                     print("Sorting semester in Ascending order:")
                     print(sorted(student_lst, key=lambda i: i['semester']))
                  elif ip == 2:
                      print("Sorting semester in Descending order:")
                      print(sorted(student_lst, key=lambda i: i['semester'], reverse=True))

    else:
        print("Invalid choice")
        continue