Intercom Interview
====
1. What's your proudest achievement? It can be a personal project or something you've worked on professionally. Just a short paragraph is fine, but I'd love to know why you're proud of it.
----
I am really proud of HP Printables project. The idea of HP Printables is provide print content to customers in a scheduled way, for example using the controle panel of a HP printer or a Smartphone with HP Printables app is possible schedule some print content as newspapers and magazines to be printed periodically.

When I started at this project, the HP printable app does not exist at that time and the user experience to manage printables from the printer control panel was not so good, mainly because the control panel is very small. So in order to solve this issue, I have suggested the following idea to the product manager, mirror the control panel functionality to a mobile app, since the mobile devices will give us the necessary power to provide to users a much better experience.

The project manager have accepted my sugestions and we started the HP Printables Apps development. Today we have our app for iOS https://itunes.apple.com/br/app/hp-printables/id881523106?mt=8 and Android https://play.google.com/store/apps/details?id=com.hp.newsstand&hl=pt_BR what have improved the user experience for our customers. After the release of the apps we could realize in the reports, a print increase, in a matter of 60%.

In this project we had the following challenges to overcome:

- Create and integrate 6 microservices
  - oAuth Login
  - Printables Catalog
  - Printers Catalog
  - Scheduler
  - Device Manager
  - Print Service

- implement a cache content service
- communicate apps with printers
- keep all functionality calls in a matter of seconds
- coordinate the migration from AWS to HPCS with no downtime

2. Write some code, that will flatten an array of arbitrarily nested arrays of integers into a flat array of integers. e.g. [[1,2,[3]],4] -> [1,2,3,4].
----
Answer inside flatten_int_array folder
To run the program go to flatten_int_array folder and execute the follow command:

```python flatten.py```

To run the tests go to flatten_int_array folder and execute the follow command:

```python flatten_tests.py```

3. We have some customer records in a text file (customers.json) -- one customer per line, JSON-encoded. We want to invite any customer within 100km of our Dublin office (GPS coordinates 53.3381985, -6.2592576) for some food and drinks on us.
----
Answer inside calculate_close_customers folder
To run the program go to calculate_close_customers folder and execute the follow command:

```python get_customers_in_a_100km_range.py```

To run the tests go to calculate_close_customers folder and execute the follow command:

```python get_customers_in_a_100km_range_tests.py```