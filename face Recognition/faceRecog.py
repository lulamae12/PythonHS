import face_recognition as fr

KnownPeople = [

    "Tommy Smith",

]





Tommy = fr.load_image_file("D:\\Programs\\Python\\face Recognition\\Known\\Tommy Smith.jpg")
TommyEncoding = fr.face_encodings(Tommy)[0]
Dillon = fr.load_image_file("D:\\Programs\\Python\\face Recognition\\Known\\Dillon Brooks.jpg")
DillonEncoding = fr.face_encodings(Dillon)[0]




unknownImage = fr.load_image_file("D:\\Programs\\Python\\face Recognition\\Unknown\\unknown.jpg")
unknownEncoding = fr.face_encodings(unknownImage)[0]


#load source"known" and image to idnetify into np array



#compare database (in brackets ) with unknown
isTommy = fr.compare_faces([TommyEncoding], unknownEncoding)
isDillon = fr.compare_faces([DillonEncoding], unknownEncoding)
if isTommy:
    print("that is: ",KnownPeople[0])
