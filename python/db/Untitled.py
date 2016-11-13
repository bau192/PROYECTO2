from py2neo import Graph,Node,Relationship

graph = Graph(password="password")
graph = Graph("http://localhost:7474/db/data/")
buscar="Fifa 17"
quiero="Tipo"

    ## VideoJuegos
fifa17 = Node ("VideoJuego", name="Fifa 17")
graph.create(fifa17)

madden17 = Node ("VideoJuego", name="Madden 17")
graph.create(madden17)

    ##Consolas
ps3 = Node ("Consola", name="Play Station 3")
graph.create(ps3)

ps4 = Node ("Consola", name="Play Station 4")
graph.create(ps4)
xboxone = Node ("Consola", name="XBox One")
graph.create(xboxone)

xbox360 = Node ("Consola", name="Xbox 360")
graph.create(xbox360)
pc = Node ("Consola", name="PC")
graph.create(pc)

    ## Generos
deporte = Node ("Genero", name= "Deporte")
graph.create(deporte)
rpg = Node ("Genero", name= "RPG")
graph.create(rpg)
aventura = Node ("Genero", name= "Aventura")
graph.create(aventura)
pelea = Node ("Genero", name= "Pelea")
graph.create(pelea)
shooter = Node ("Genero", name= "Shooter")
graph.create(shooter)


    ## Relaciones
graph.create(Relationship(fifa17, "Disponible", ps3))
graph.create(Relationship(fifa17, "Disponible", ps4))
graph.create(Relationship(fifa17, "Disponible", xboxone))
graph.create(Relationship(fifa17, "Disponible", xbox360))
graph.create(Relationship(fifa17, "Tipo", deporte))
graph.create(Relationship(madden17, "Disponible", ps3))
graph.create(Relationship(madden17, "Disponible", ps4))
graph.create(Relationship(madden17, "Disponible", xboxone))
graph.create(Relationship(madden17, "Disponible", xbox360))
graph.create(Relationship(madden17, "Tipo", deporte))
    ## Condiciones de busqueda


if buscar=="Fifa 17":
    if quiero=="Tipo":
        for rel in graph.match(start_node=fifa17, rel_type="Tipo",end_node=None):
            print(rel.end_node()["name"])
    elif quiero== "Disponible":
        for rel in graph.match(start_node=fifa17, rel_type="Disponible",end_node=None):
            print(rel.end_node()["name"])
            
else:
    print("No no no...")
        
graph.delete_all()


