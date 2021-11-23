# Analizator psiej karmy dla schronisk

## Spis Treści:

1. [Opis projektu](#opis-projektu)
2. [Demo na kanale YouTube](#demo-na-kanale-youtube)
3. [Zespół](#zespół)
4. [Opis funkcjonalności](#opis-funkcjonalności)
5. [Schemat działania rozwiązania](#prezentacja-działania-rozwiązania)
6. [Architektura](#architektura)
7. [Wybrany stos technologiczny](#wybrany-stos-technologiczny)
   * [Azure Cognitive Services Computer Vision](#azure-cognitive-services-computer-vision)
   * [Azure Cognitive Services Computer Vision Optical character recognition](#azure-cognitive-services-computer-vision-optical-character-recognition)
   * [Azure Web Apps](#azure-web-apps)
   * [Flask](#flask)
8. [Problemy](#problemy)


## Opis projektu: 

Projekt miał na celu stworzenie analizatora składu karmy dla psów. Powstał, by ułatwić darczyńcom schronisk zakup odpowiedniej jakościowo karmy dla psiaków.

## Demo na kanale YouTube: 

https://youtu.be/XHffBHFIBww

## Zespół:

* Martyna Jakubowska: https://github.com/mjakubowska
* Aleksandra Kowalczyk: https://github.com/Olakow

## Opis funkcjonalności: 

* Użytkownik wchodzi na stronę https://karma-web.azurewebsites.net

* Dodaje zdjęcie składu karmy, którą chce sprawdzić
	
* Program wyświetla informacje, czy karma jest odpowiednia dla psiaków czy lepiej jej unikać


## Prezentacja działania rozwiązania

1. Aplikacja webowa została napisana przy użyciu frameworka Flask.
	
2. Kod w Pythonie do optycznego rozwpoznawania znaków został napisany przy użyciu Azure Cognitiveservices Vision Computervision.
	
3. Gotowy kod został zamieszczony w repozytorium na GitHubie.
	
4. Utworzony AppService został połączony z repozytorium na GitHubie (zakładka Deployment Center, czyli Centrum wdrożenia):

![Połączenie AppService z repozytorium z GitHuba](images/appconect.png)

5. Po uruchomieniu strony aplikacji webowej użytkownik dodaje wybrane zdjęcie znajdujące się lokalnie na jego urządzeniu, następnie obraz jest przesyłany
i wywoływujemy na nic OCR. Po przeanalizowaniu składu karmy, analizator decyduje, czy karma spełnia warunki do zakwalifikowania się do dobrego składu karmy czy wręcz przeciwnie.
	
	
## Architektura

![Azure Architecture](images/architecture.png)


## Wybrany stos technologiczny:


### Azure Cognitive Services Computer Vision 

![ ](images/computervision.png)

Usługa sztucznej inteligencji służąca do analizowania zawartości obrazów i filmów wideo

 * Dokumentacja: https://docs.microsoft.com/en-en/azure/cognitive-services/computer-vision/
 * Cennik: https://azure.microsoft.com/en-en/pricing/details/cognitive-services/computer-vision/



### Azure Cognitive Services Computer Vision Optical Character Recognition

![ ](images/ocr.png)

Wyodrębniaj tekst drukowany i napisany odręcznie z obrazów oraz dokumentów o mieszanych językach i stylach pisania.

W swoim projekcie wykorzystałyśmy funkcje wyodrębniania tekstu dostępną w Computer Vision (przetwarzanie obrazu). Pozowliła nam ona w łatwy sposób wyodrębnić tekst ze zdjęcia składu karmy, a następnie już sam tekst poddać analizie, która roztrzyga czy karma zawiera dobry czy zły skład.
	
 * OCR Quickstart w Pythonie: https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts-sdk/client-library?success=run-the-application&tabs=visual-studio&pivots=programming-language-python#clean-up-resources
 * Dokumentacja: https://centraluseuap.dev.cognitive.microsoft.com/docs/services/computer-vision-v3-2/operations/56f91f2e778daf14a499f20d
 * Obsługiwane języki: https://docs.microsoft.com/en-en/azure/cognitive-services/computer-vision/language-support
	
### Azure App Service Web Apps

![](images/webapps.png)

Usługa Azure App Service zapewnia szybsze tworzenie aplikacji dzięki jedynej w swoim rodzaju usłudze w chmurze, która umożliwia szybkie i proste tworzenie gotowych do użycia w przedsiębiorstwie aplikacji sieci Web i mobilnych dla dowolnej platformy i urządzenia oraz wdrażanie ich w skalowalnej i niezawodnej infrastrukturze chmury.

Użyłyśmy jej by w łatwy sposób móc utworzyć webową aplikacje, do której dostęp będzie miał każdy użytkownik, który chciałby skorzystać z naszego analizatora.

 * Dokumentacja: https://azure.microsoft.com/en-us/services/app-service/#overview
 * Cennik: https://azure.microsoft.com/en-us/pricing/details/app-service/windows/

### Flask

![](images/flask.png)

Flask to lekką platformę języka Python dla aplikacji internetowych, która zapewnia podstawowe informacje dotyczące routingu adresów URL i renderowania stron.

Użyłyśmy Flaska, ponieważ jest rekomendowany dla osób początkujących. Flask jest polecany jako dobry framework, jeśli chcemy dowiedzieć się, jak wszystko działa od środka, włączając samego Python.


 * Dokumentacja: https://azure.microsoft.com/en-us/pricing/details/app-service/windows/
 
## Problemy

Napotkałyśmy problem z działaniem App Services. Wcześniej po połączeniu aplikacji z kodem na GitHubie aplikacja działała poprawnie, w którymś momencie jednak zaczął pojawiać nam się błąd, którego nie byłyśmy w stanie rozwiązać. Diagnoztyka problemów dostępna na Portalu Azure nie działała.

![](images/error.png)

