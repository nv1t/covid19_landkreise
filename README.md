# covid19_landkreise
short script to aggregate all covid19 cases per "landkreis" and use a Pandas Dataframe.

It fetches it's data through webscraping for each "bundesland" on their respective websites. The sources can be seen below.

# Sources

| Bundesland | Source |
| --- | --- |
| Bayern | https://www.lgl.bayern.de/gesundheit/infektionsschutz/infektionskrankheiten_a_z/coronavirus/karte_coronavirus/index.htm |
| Hessen | https://soziales.hessen.de/gesundheit/infektionsschutz/coronavirus-sars-cov-2/taegliche-uebersicht-der-bestaetigten-sars-cov-2-faelle-hessen |
| Mecklenburg-Vorpommern | https://www.lagus.mv-regierung.de/Services/Aktuelles/?id=158593&processor=processor.sa.pressemitteilung |
| Niedersachsen | https://www.apps.nlga.niedersachsen.de/corona/download.php?csv |
| Nordrhein-Westfalen | https://www.mags.nrw/coronavirus-fallzahlen-nrw |
| Rheinland-Pfalz | https://msagd.rlp.de/de/unsere-themen/gesundheit-und-pflege/gesundheitliche-versorgung/oeffentlicher-gesundheitsdienst-hygiene-und-infektionsschutz/infektionsschutz/informationen-zum-coronavirus-sars-cov-2/ |
| Sachsen-Anhalt | https://verbraucherschutz.sachsen-anhalt.de/hygiene/infektionsschutz/infektionskrankheiten/coronavirus/ |
| Sachsen | https://www.coronavirus.sachsen.de/infektionsfaelle-in-sachsen-4151.html |
| Schlesweig-Holstein | https://www.schleswig-holstein.de/DE/Landesregierung/I/Presse/_documents/Corona-Liste_Kreise.html |
| Thueringen | https://corona.thueringen.de/covid-19-bulletin/ |
