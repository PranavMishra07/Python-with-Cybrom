p=float(input("Enter Physics Marks : "))
c=float(input("Enter Chemistry Marks : "))
m=float(input("Enter maths Marks : "))
h=float(input("Enter Hindi Marks : "))
e=float(input("Enter English Marks : "))
total_marks=p+c+m+h+e
per=total_marks/5
if(p<0 or m<0 or c<0 or h<0 or e<0 or p>100 or c>100 or m>100 or h>100 or e>100):
    print("Invalid Marks")
    print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
elif((p<33 and c>=33 and m>=33 and h>=33 and e>=33) or (p>=33 and c<33 and m>=33    and h>=33 and e>=33) or (p>=33 and c>=33 and m<33 and h>=33 and e>=33 ) or (p>=33 and c>=33 and m>=33 and h<33 and e>=33) or (p>=33 and c>=33 and m>=33 and h>=33 and e<33)):
    if(p<33 and c>=33 and m>=33 and h>=33 and e>=33):
        print("Fail in Physics")
        print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
        print(f"Total Marks : {total_marks} , Percentage : {per}")
    elif(p>=33 and c<33 and m>=33 and h>=33 and e>=33):
        print("Fail In Chemistry")
        print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
        print(f"Total Marks : {total_marks} , Percentage : {per}")
    elif(p>=33 and c>=33 and m<33 and h>=33 and e>=33 ):
        print("Fail In Maths")
        print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
        print(f"Total Marks : {total_marks} , Percentage : {per}")
    elif(p>=33 and c>=33 and m>=33 and h<33 and e>=33):
        print("Fail in Hindi")
        print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
        print(f"Total Marks : {total_marks} , Percentage : {per}")
    else:
        print("Fail in English")
        print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
        print(f"Total Marks : {total_marks} , Percentage : {per}")
elif((p<33 and c<33 and m<33 and h>=33 and e>=33) or (p<33 and c>=33 and m>=33 and h<33 and e<33) or (p>=33 and c<33 and m<33 and h<33 and e>=33) or (p<33 and c<33 and m>=33 and h>=33 and e<33) or (p>=33 and c>=33 and m<33 and h<33 and e<33) or (p<33 and c<33 and m>=33 and h<33 and e>=33)):
    if(p<33 and c<33 and m<33 and h>=33 and e>=33):
        print(f"Fail in Physics : {p} , Chemistry : {c} , Maths : {m}")
        print("Failed In Exam")
        print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
        print(f"Total Marks : {total_marks} , Percentage : {per}")
    elif(p<33 and c>=33 and m>=33 and h<33 and e<33):
        print(f"Fail in Physics : {h} , Hindi : {h} , English : {e}")
        print("Faild in Exam ")
        print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
        print(f"Total Marks : {total_marks} , Percentage : {per}")
    elif(p>=33 and c<33 and m<33 and h<33 and e>=33):
        print(f"Fail in Chemistry : {c} , Maths : {m} ,Hindi : {h}")
        print("Failed In Exam")
        print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
        print(f"Total Marks : {total_marks} , Percentage : {per}")
    elif(p<33 and c<33 and m>=33 and h>=33 and e<33):
        print(f"Fail in Physics : {p} , Chemistry : {c} , English : {e}")
        print("Failed In Exam")
        print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
        print(f"Total Marks : {total_marks} , Percentage : {per}")
    elif(p>=33 and c>=33 and m<33 and h<33 and e<33):
        print(f"Fail in Maths : {m} , Hindi : {h} , English : {e}")
        print("Failed In Exam")
        print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
        print(f"Total Marks : {total_marks} , Percentage : {per}")
    else:
        print(f"Fail in Physics : {p} , Chemistry : {c} , Hindi : {h}")
        print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
        print(f"Total Marks : {total_marks} , Percentage : {per}")
elif(p<=33 and c<=33 and m<33 and h<33 and e<33):
    print("You Are Fail in All Subject..!! ")
    print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
    print(f"Total Marks : {total_marks} , Percentage : {per}")
else:
    if(per<45):
        print("3rd Division 'C' Grade  ")
        print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
        print(f"Total Marks : {total_marks} , Percentage : {per}")
    elif(per<60):
        print("2nd Division 'B' Grade ")
        print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
        print(f"Total Marks : {total_marks} , Percentage : {per}")
    elif(per<80):
        print("1st Division 'A'Grade")
        print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
        print(f"Total Marks : {total_marks} , Percentage : {per}")
    else:
        print("'A++' Topper")
        print(f"Physics: {p} Chemistry : {c} Maths : {m} Hindi : {h} English : {e}  ")
        print(f"Total Marks : {total_marks} , Percentage : {per}")




    

        



