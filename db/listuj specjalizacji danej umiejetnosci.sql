SELECT specjalizacja
FROM specjalizacje
JOIN umiejetnosci ON specjalizacje.id_umiejetnosci = umiejetnosci.id
WHERE umiejetnosci.umiejetnosc = "Występy"
