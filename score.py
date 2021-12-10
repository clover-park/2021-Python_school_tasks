def total(student):
    total_score = student[1] + student[2] + student[3]
    return total_score


def ave(student):
    average = student[4] / 3
    return average


def grade(student):
    if student[5] >= 90:
        result = 'A'
    elif student[5] >= 80:
        result = 'B'
    elif student[5] >= 70:
        result = 'C'
    elif student[5] >= 60:
        result = 'D'
    else:
        result = 'F'
    return result


def output(student):
    print(student[0], ':', '국어:', student[1], '영어:', student[2], '수학:',
          student[3], '총점:', student[4], '평균:', '{:.2f}'.format(student[5]), '학점:', student[6])


def max_student(*student):
    if len(student) > 0:
        max = student[0]
        for s in student:
            if s[4] > max[4]:
                max = s
        return max
    else:
        return None
