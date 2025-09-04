import arcpy

fc = input(r"Insertar path ")

fc_mbg = fc + "_mbg" #Capa resultante del minimum bounding geometry

#Fields con nombre, tipo y alias
ymax = ["north", "DOUBLE" , "North"]
ymin = ["south" , "DOUBLE" , "South"]
xmax = ["east" , "DOUBLE" , "East"]
xmin = ["west" , "DOUBLE" , "West"]

#Para calcular geometría por cada campo
campos = {"north" : "EXTENT_MAX_Y" ,
          "south" : "EXTENT_MIN_Y" ,
          "east" : "EXTENT_MAX_X" , 
          "west" : "EXTENT_MIN_X"}

arcpy.management.MinimumBoundingGeometry(fc , fc_mbg , geometry_type= "ENVELOPE" , group_option= "ALL" , mbg_fields_option= "NO_MBG_FIELDS")

arcpy.management.AddFields(fc_mbg , [ymax , ymin, xmax , xmin])

for cardinal , extension in campos.items():
    arcpy.management.CalculateGeometryAttributes(fc_mbg , [[cardinal , extension]] , coordinate_format= "DD")

#Imprimir coordenada por cada punto cardinal
for i in list(campos):
    with arcpy.da.SearchCursor(fc_mbg , i) as cursor:
        for coord in cursor:
            print(i , "--> " , coord[0])
            
#Eliminar el mbg residual
arcpy.Delete_management(fc_mbg)




