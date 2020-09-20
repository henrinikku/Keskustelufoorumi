# Keskustelufoorumi
Sovelluksen avulla käyttäjät voivat luoda ja käsitellä aihealueita/kategorioita, ja keskustella niiden alla. 

## Tilanne 20.09.2020
Sovellus on vielä todella keskeneräinen. Toteutettuna on käytännössä ainastaan rekisteröityminen, kirjautuminen ja (admin-käyttäjällä) käyttäjien poistaminen.

## Admin-tunnukset testausta varten
Käyttäjänimi: admin
Salasana: testi123

## Toiminnallisuus
Sovelluksessa on ainakin kolme käyttäjäroolia, _peruskäyttäjä_, _premium-käyttäjä_ ja _ylläpitäjä_. Rekisteröitymisen yhteydessä luodaan peruskäyttäjä.

Peruskäyttäjät voivat
- hakea keskusteluita esimerkiksi avainsanojen perusteella
- aloittaa keskusteluita
- vastata keskusteluihin
- muokata vastauksiaan

Premium-käyttäjät voivat tehdä kaiken mitä peruskäyttäjät, ja lisäksi
- luoda ja muokata omia aihealueitaan
- hallinnoida luomiensa aihealueiden käyttöoikeuksia (ainakin aluksi pelkästään käyttäjäkohtaisesti)

Ylläpitäjät voivat tehdä kaiken mitä premium-käyttäjät, ja lisäksi
- ylentää tai alentaa käyttäjiä (esim. peruskäyttäjä -> premium-käyttäjä)
- poistaa käyttäjiä
- poistaa aihealueita
- poistaa ketjuja
- poistaa viestejä
