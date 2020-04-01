# * from author
# create header


def createHeader(fullname, gender):
    if gender == "L".lower():
        title = "Mas. "
    elif gender == "P".lower():
        title = "Neng. "
    else:
        title = "Mas. atau Neng. "
    header = "Halo " + title + "" + fullname + ","
    return header


print(createHeader("Rahul Khan", "l"))
print(createHeader("Anjali Richard", "p"))
print(createHeader("Meja", "?"))
