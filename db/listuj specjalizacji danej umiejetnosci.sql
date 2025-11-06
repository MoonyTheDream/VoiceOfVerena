SELECT specjalizacja, id_umiejetnosci, umiejetnosci.umiejetnosc
FROM specjalizacje
JOIN umiejetnosci ON specjalizacje.id_umiejetnosci = umiejetnosci.id
WHERE umiejetnosci.umiejetnosc = "Jeździectwo"
