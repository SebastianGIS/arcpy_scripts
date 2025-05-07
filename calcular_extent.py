import arcpy

fc = input(r"Insertar path ")

fc_mbg = fc + "_mbg"

#Fields con nombre, tipo y alias
xmin = ["west" , "DOUBLE" , "West"]
ymin = ["south" , "DOUBLE" , "South"]
xmax = ["east" , "DOUBLE" , "East"]
ymax = ["north", "DOUBLE" , "North"]

#Para calcular geometría por cada campo
campos = {"west" : "EXTENT_MIN_X" ,
          "south" : "EXTENT_MIN_Y" ,
          "east" : "EXTENT_MAX_X" , 
          "north" : "EXTENT_MAX_Y"}

arcpy.management.MinimumBoundingGeometry(fc , fc_mbg , geometry_type= "ENVELOPE" , group_option= "ALL" , mbg_fields_option= "NO_MBG_FIELDS")

arcpy.management.AddFields(fc_mbg , [xmin , ymin, xmax , ymax])

for cardinal , extension in campos.items():
    arcpy.management.CalculateGeometryAttributes(fc_mbg , [[cardinal , extension]] , coordinate_format= "SAME_AS_INPUT")

#Imprimir coordenada por cada punto cardinal
for i in list(campos):
    with arcpy.da.SearchCursor(fc_mbg , i) as cursor:
        for coord in cursor:
            print(i , "--> " , coord[0])
 
#A futuro añadir edición automática de metadata

