# Crear una matriz 3D.
# dimension 1 = 3 ciudades (Quito, Guayaquil, Esmeraldas)
# dimension 2 = 4 semanas.
# dimension 3 = 7 dias de la semana.

matriz_temperaturas = [
    {'ciudad': 'Quito', 'Semanas': [

        [ # 1
            {"dia": "lunes", "temperatura": 7,},
            {"dia": "Martes", "temperatura": 10,},
            {"dia": "Miercoles", "temperatura": 6,},
            {"dia": "Jueves", "temperatura": 7,},
            {"dia": "viernes", "temperatura": 8,},
            {"dia": "Sabado", "temperatura": 11,},
            {"dia": "domingo", "temperatura": 5,}


        ],

        [ #2
            {"dia": "lunes", "temperatura": 18, },
            {"dia": "Martes", "temperatura": 18, },
            {"dia": "Miercoles", "temperatura": 18, },
            {"dia": "Jueves", "temperatura": 16, },
            {"dia": "viernes", "temperatura": 16, },
            {"dia": "Sabado", "temperatura": 11, },
            {"dia": "domingo", "temperatura": 10, }

        ],

        [ #3
            {"dia": "lunes", "temperatura": 18, },
            {"dia": "Martes", "temperatura": 10, },
            {"dia": "Miercoles", "temperatura": 9, },
            {"dia": "Jueves", "temperatura": 12, },
            {"dia": "viernes", "temperatura": 18, },
            {"dia": "Sabado", "temperatura": 17, },
            {"dia": "domingo", "temperatura": 6, }

        ],

        [ #4
            {"dia": "lunes", "temperatura": 18, },
            {"dia": "Martes", "temperatura": 11, },
            {"dia": "Miercoles", "temperatura": 6, },
            {"dia": "Jueves", "temperatura": 7, },
            {"dia": "viernes", "temperatura": 15, },
            {"dia": "Sabado", "temperatura": 7, },
            {"dia": "domingo", "temperatura": 9, }

        ]
    ]},

    {'ciudad': 'Guayaquil', 'Semanas': [

        [ #1
            {"dia": "lunes", "temperatura": 31, },
            {"dia": "Martes", "temperatura": 18, },
            {"dia": "Miercoles", "temperatura": 32, },
            {"dia": "Jueves", "temperatura": 25, },
            {"dia": "viernes", "temperatura": 26, },
            {"dia": "Sabado", "temperatura": 30, },
            {"dia": "domingo", "temperatura": 25, }

        ],

        [ #2
            {"dia": "lunes", "temperatura": 24, },
            {"dia": "Martes", "temperatura": 25, },
            {"dia": "Miercoles", "temperatura": 26, },
            {"dia": "Jueves", "temperatura": 27, },
            {"dia": "viernes", "temperatura": 28, },
            {"dia": "Sabado", "temperatura": 21, },
            {"dia": "domingo", "temperatura": 25, }

        ],

        [ #3
            {"dia": "lunes", "temperatura": 27, },
            {"dia": "Martes", "temperatura": 20, },
            {"dia": "Miercoles", "temperatura": 24, },
            {"dia": "Jueves", "temperatura": 22, },
            {"dia": "viernes", "temperatura": 26, },
            {"dia": "Sabado", "temperatura": 21, },
            {"dia": "domingo", "temperatura": 25, }

        ],

        [ #4
            {"dia": "lunes", "temperatura": 27, },
            {"dia": "Martes", "temperatura": 10, },
            {"dia": "Miercoles", "temperatura": 16, },
            {"dia": "Jueves", "temperatura": 17, },
            {"dia": "viernes", "temperatura": 28, },
            {"dia": "Sabado", "temperatura": 21, },
            {"dia": "domingo", "temperatura": 35, }

        ]

    ]},

    {'ciudad': 'Esmeraldas', 'Semanas': [

        [ #1
            {"dia": "lunes", "temperatura": 37, },
            {"dia": "Martes", "temperatura": 20, },
            {"dia": "Miercoles", "temperatura": 36, },
            {"dia": "Jueves", "temperatura": 27, },
            {"dia": "viernes", "temperatura": 18, },
            {"dia": "Sabado", "temperatura": 31, },
            {"dia": "domingo", "temperatura": 25, }

        ],

        [ #2
            {"dia": "lunes", "temperatura": 17, },
            {"dia": "Martes", "temperatura": 30, },
            {"dia": "Miercoles", "temperatura": 26, },
            {"dia": "Jueves", "temperatura": 27, },
            {"dia": "viernes", "temperatura": 28, },
            {"dia": "Sabado", "temperatura": 21, },
            {"dia": "domingo", "temperatura": 35, }

        ],

        [ #3
            {"dia": "lunes", "temperatura": 32, },
            {"dia": "Martes", "temperatura": 32, },
            {"dia": "Miercoles", "temperatura": 25, },
            {"dia": "Jueves", "temperatura": 28, },
            {"dia": "viernes", "temperatura": 30, },
            {"dia": "Sabado", "temperatura": 18, },
            {"dia": "domingo", "temperatura": 26, }

        ],

        [ #4
            {"dia": "lunes", "temperatura": 30, },
            {"dia": "Martes", "temperatura": 20, },
            {"dia": "Miercoles", "temperatura": 28, },
            {"dia": "Jueves", "temperatura": 29, },
            {"dia": "viernes", "temperatura": 39, },
            {"dia": "Sabado", "temperatura": 12, },
            {"dia": "domingo", "temperatura": 35, }
        ]

    ]}

]

# Funcion para calculo promedio de temperatura

def promedio_de_temperaturas(matriz_temperaturas):

    promedios = {}

    for ciudad in matriz_temperaturas:
        temp = 0
        dias_t = 0

        for semana in ciudad["Semanas"]:
            for dia in semana:
                temp += dia[("temperatura")]
                dias_t += 1


        promedio_ciudad = temp / dias_t
        promedios[ciudad["ciudad"]] = round(promedio_ciudad, 2)

# Retornamos (promedios)

    return promedios

resultados = promedio_de_temperaturas(matriz_temperaturas)

# Plasmamos los resultados en panatalla

print ("El promedio de temperaturas por ciudad es: ")

for ciudad, promedio in resultados.items():
    print (f"{ciudad}, {promedio} grados en promedio")






