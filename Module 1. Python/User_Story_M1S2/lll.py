vehiculos = {
    "camionetas" : {
        "kia" : {
            "combustion" : {
                "sportage" : ("2022", "1.4"),
            },
            "electrico" : {
                "tank" : ("2025",)
            },
            "hibrido" : {
                "sportage" : ("2027", "1.2", "1200kw"),
            }
        }
    },
    "suv" : {
        "kia" : {
                "combustion" : {
                    "niro" : ("2022", "1.4"),
                },
                "hibrido" : {
                    "niro" : ("2027", "1.2", "1200kw"),
                }
            }
        },
    "sedan" : {
        "kia" : {
            "combustion" : {
                "rio" : {
                        "vibrant" : ("2025", "1.4", "R17"),
                        "zenith" : ("2025", "1.4", "R19"),
                },
                "soluto" : {
                        "vibrant" : ("2025", "1.4", "R11"),
                        "zenith" : ("2025", "1.4", "R15"),
                }
            }
        } 
    }
}

for key, data in vehiculos["camionetas"].items():
    #print(key, data)
    for tipo, info in data.items():
        #print(tipo, info)
        for marca, modelo in info.items():
            print(f"{marca}: {modelo[0]}")