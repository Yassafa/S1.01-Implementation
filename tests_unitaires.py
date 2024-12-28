def test_nb_villes():
   assert nb_villes(villes)==10
   assert nb_villes([])==0
   assert nb_villes([0])==0
   assert nb_villes(["Paris"])==1
   print("Test de la fonction nb_villes : ok")

def test_nom_villes():
   assert noms_villes(villes)==['Paris', 'Lyon', 'Marseille', 'Lille', 'Strasbourg', 'Rennes','Clermont-Ferrand', 'Bordeaux', 'Toulouse', 'Grenoble']
   assert noms_villes([])==[]
   assert noms_villes([0,1,2,3])==[]
   assert noms_villes(["Paris",2])==['Paris']
   print("Test de la fonction nom_villes : ok")

def test_distance():
   assert isclose(distance(2.33,48.86,5.40,43.30),661,86)
   assert isclose(distance(0,0,0,0),0.0)
   assert isclose(distance(2.33,48.86,4.85,45.75),394.507)
   print("Test de la fonction distance : ok")

def test_indexCity():
   assert indexCity("Paris", villes) == 0
   assert indexCity("Clermont-Ferrand",villes) == 18
   assert indexCity("Villetaneuse",villes) == -1
   print("Test de la fonction indexCity : ok")

def test_distance_noms():
   assert isclose(distance_noms("Paris","Marseille",villes),661.86)
   assert distance_noms("Madrid","Paris",villes) == -1
   assert distance_noms("Berlin","Londres",villes) == -1
   assert isclose(distance_noms("Paris","Paris",villes),0.0)
   assert isclose(distance_noms("Paris","Lyon",villes),394.507)
   print("Test de la fonction distance_noms : ok")

def test_long_tour():
   assert isclose(long_tour(villes,["Paris","Marseille"]),1323.72)
   assert long_tour(villes,["Madrid","Paris"]) == -1
   assert long_tour(villes,["Berlin","Londres"]) == -1
   assert isclose(long_tour(villes,["Paris","Paris"]),0.0)
   assert isclose(long_tour(villes,["Paris","Lyon"]),789.014)
   print("Test de la fonction long_tour : ok")
