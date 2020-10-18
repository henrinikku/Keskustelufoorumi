# Keskustelufoorumi
Sovelluksen avulla käyttäjät voivat luoda ja käsitellä aihealueita/kategorioita sekä keskustella niiden alla. 

https://keskustelufoorumi123.herokuapp.com

## Admin-tunnukset testausta varten
Käyttäjänimi: admin

Salasana: testi123

## Toiminnallisuus
Sovelluksessa on ainakin kolme käyttäjäroolia, _peruskäyttäjä_, _premium-käyttäjä_ ja _ylläpitäjä_. Rekisteröitymisen yhteydessä luodaan peruskäyttäjä.

Peruskäyttäjät voivat
- [ ] hakea keskusteluita esimerkiksi avainsanojen perusteella
- [x] aloittaa keskusteluita
- [x] vastata keskusteluihin
- [ ] muokata vastauksiaan

Premium-käyttäjät voivat tehdä kaiken mitä peruskäyttäjät, ja lisäksi
- [x] luoda ja muokata omia aihealueitaan
- [ ] hallinnoida luomiensa aihealueiden käyttöoikeuksia (ainakin aluksi pelkästään käyttäjäkohtaisesti)

Ylläpitäjät voivat tehdä kaiken mitä premium-käyttäjät, ja lisäksi
- [x] ylentää tai alentaa käyttäjiä (esim. peruskäyttäjä -> premium-käyttäjä)
- [x] poistaa käyttäjiä
- [x] poistaa aihealueita
- [x] poistaa ketjuja
- [x] poistaa viestejä
