import cv2

img = cv2.imread("solar-system.jpg")
#C:\Users\mcata\Downloads\PRO-116

cv2.putText(img,
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )
cv2.putText(img,
            "Mercúrio",
            (200,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )

cv2.putText(img,
            "Vênus",
            (300,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )

cv2.putText(img,
            "Terra",
            (400,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )

cv2.putText(img,
            "Marte",
            (500,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )

cv2.putText(img,
            "Júpter",
            (600,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )

cv2.putText(img,
            "Saturno",
            (700,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )

cv2.putText(img,
            "Urâno",
            (800,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )

cv2.putText(img,
            "Netuno",
            (900,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )


cv2.imshow("resultado",img)
cv2.imwrite("Solar_systemwithname.jpg",img)
cv2.waitKey(0)

