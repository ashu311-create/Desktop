studentdata={
    "id1":{"name":"Sara", "Class":"V", "sub_int":"english, math, science"},
    "id2":{"name":"David", "Class":"V", "sub_int":"english, math, science"},
    "id3":{"name":"Sarah", "Class":"V", "sub_int":"english, math, science"},
    "id4":{"name":"Nathan", "Class":"V", "sub_int":"english, math, science"}
}
result={}
seen_keys=[]
for student_id, details in studentdata.items():
    unique_key=(details["name"], details["Class"], details["sub_int"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id]=details
for k, v in result.items():
    print (k, ":", v)