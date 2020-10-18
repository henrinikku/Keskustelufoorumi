# Keskustelufoorumi
Sovelluksen avulla käyttäjät voivat luoda ja käsitellä aihealueita/kategorioita sekä keskustella niiden alla. 

https://keskustelufoorumi123.herokuapp.com

## Admin-tunnukset testausta varten
Käyttäjänimi: admin

Salasana: testi123

## Sovelluksen ajaminen paikallisesti
Asenna riippuvuudet requirements.txt tiedostosta ja luo projektin juureen .env -tiedosto seuraavilla avaimilla
```
DATABASE_URL=postgresql:///<tietokanta>
APP_SETTINGS=<config.DevelopmentConfig|config.ProductionConfig>
SECRET_KEY=<avain>
```
Ensimmäinen admin-käyttäjä pitää tehdä luomalla peruskäyttäjä ja antamalla sille tietokannassa admin-rooli käsin. En jaksanut tehdä mitään komentorivityökalua tms. tätä varten, kun käsittääkseni ei ole tarkoituksena, että arvostelijat ajavat näitä omilla koneillaan.

## Toiminnallisuus
Sovelluksessa on ainakin kolme käyttäjäroolia, _peruskäyttäjä_, _premium-käyttäjä_ ja _ylläpitäjä_. Rekisteröitymisen yhteydessä luodaan peruskäyttäjä.

Peruskäyttäjät voivat
- [x] hakea keskusteluita esimerkiksi avainsanojen perusteella
- [x] aloittaa keskusteluita
- [x] vastata keskusteluihin
- [x] muokata vastauksiaan

Premium-käyttäjät voivat tehdä kaiken mitä peruskäyttäjät, ja lisäksi
- [x] luoda ja muokata omia aihealueitaan
- [ ] hallinnoida luomiensa aihealueiden käyttöoikeuksia (ainakin aluksi pelkästään käyttäjäkohtaisesti)

Ylläpitäjät voivat tehdä kaiken mitä premium-käyttäjät, ja lisäksi
- [x] ylentää tai alentaa käyttäjiä (esim. peruskäyttäjä -> premium-käyttäjä)
- [x] poistaa käyttäjiä
- [x] poistaa aihealueita
- [x] poistaa ketjuja
- [x] poistaa viestejä
