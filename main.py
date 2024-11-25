from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handlet = Mangum(app)

@app.get("/integraciones/{id_integracion}")
def main_integraciones(id_integracion:int):
    lst_integraciones = [{ "id_integracion":1,
            "nombre_integracion":"API Simpli Route GPS",
            "url_integracion":"https://9zyupks8yg.execute-api.us-west-2.amazonaws.com/prod/track/"
            },
            { "id_integracion":2,
            "nombre_integracion":"API Sercoing",
            "url_integracion":"http://ws.sercoingltda.cl/WS_SERCOINGGPS_INTEGRACION_PUBLIC/integracion/inputGPS"
            }]
    
    if(id_integracion != 0):
        return [lst_integraciones[id_integracion-1]]
    
    return lst_integraciones


@app.get("/clientes/{id_cliente}")
def main_clientes(id_cliente:int):
    lst_clientes = [{
            "id_cliente":1,
            "nombre_cliente":"SALFA"
            },
            {
            "id_cliente":2,
            "nombre_cliente":"FIRST"
            }]
    
    if(id_cliente != 0):
        return [lst_clientes[id_cliente-1]]
    
    return lst_clientes


@app.get("/clientes/{id_cliente}/integraciones")
def clientes_integraciones(id_cliente:int):
    lst_clientes = [{
            "id_cliente":1,
            "nombre_cliente":"SALFA",
            "integraciones":[{ 
                "id_integracion":1,
                "nombre_integracion":"API Simpli Route GPS",
                "url_integracion":"https://9zyupks8yg.execute-api.us-west-2.amazonaws.com/prod/track/"
                },
                { "id_integracion":2,
                "nombre_integracion":"API Sercoing",
                "url_integracion":"http://ws.sercoingltda.cl/WS_SERCOINGGPS_INTEGRACION_PUBLIC/integracion/inputGPS"
                }]
            },
            {
            "id_cliente":2,
            "nombre_cliente":"FIRST",
            "integraciones":[{ 
                "id_integracion":1,
                "nombre_integracion":"API Simpli Route GPS",
                "url_integracion":"https://9zyupks8yg.execute-api.us-west-2.amazonaws.com/prod/track/"
                }]
            }]
    
    if(id_cliente != 0):
        return [lst_clientes[id_cliente-1]]
    
    return lst_clientes


@app.get("/clientes/{id_cliente}/moviles/{mov_patente}")
def clientes_moviles(id_cliente:int,mov_patente:str):
    lst_clientes = [{
            "id_cliente":1,
            "nombre_cliente":"SALFA",
            "integraciones":[{ 
                "id_integracion":1,
                "nombre_integracion":"API Simpli Route GPS",
                "url_integracion":"https://9zyupks8yg.execute-api.us-west-2.amazonaws.com/prod/track/",
                "moviles": [
                    {
                        "mov_patente ": "ABCD-11"
                    },{
                        "mov_patente ": "ABCD-12"
                    },]
                },
                { "id_integracion":2,
                "nombre_integracion":"API Sercoing",
                "url_integracion":"http://ws.sercoingltda.cl/WS_SERCOINGGPS_INTEGRACION_PUBLIC/integracion/inputGPS",
                "moviles": [
                    {
                        "mov_patente ": "ABCD-12"
                    },{
                        "mov_patente ": "ABCD-13"
                    },{
                        "mov_patente ": "ABCD-14"
                    },{
                        "mov_patente ": "ABCD-15"
                    },]
                }]
            },
            {
            "id_cliente":2,
            "nombre_cliente":"FIRST",
            "integraciones":[{ 
                "id_integracion":1,
                "nombre_integracion":"API Simpli Route GPS",
                "url_integracion":"https://9zyupks8yg.execute-api.us-west-2.amazonaws.com/prod/track/",
                "moviles": [
                    {
                        "mov_patente ": "VWXY-11"
                    },{
                        "mov_patente ": "VWXY-12"
                    },]
                }]
            }]
    
    if(id_cliente != 0):
        return [lst_clientes[id_cliente-1]]
    
    #return lst_clientes
