# for name in range(1,10):
#     print(f"Name index is : {name}")
#     if name == 5:
#         print(f"Found at Index : {name}")

name = [ "abhay","rahul","pratap"]
mark = [ 45,67,89]
for nam,mar in zip(name,mark):
    print(f"The Candidate {nam} got {mar}")