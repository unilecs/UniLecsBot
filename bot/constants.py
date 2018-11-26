# Constants
from task import *

token = 'BOT_TOKEN'  # Bot's token

start_command_message = '''Вас приветсвует бот канала @Unilecs! 🖥 Чем я могу вам помочь?🔖'''

help_command_message = '''У меня есть несколько функций! 
Начнем по порядку :
- *Список задач:* я отправлю Вам ссылку на пост с задачами нашего канала.
- *Поиск:* я нахожу задачи по названию или номеру и отправляю Вам ссылки на посты с ними.
- *Книги:* я отправляю вам ссылки на посты с подборками книг от нашего канала.
- *Получить задачу по сложности:* вы выбираете сложность задачи я отправляю вам ссылку на случайную задачу данной сложности.
- *Отправить решение:* в следуйщем сообщении вы отправляете свое решение последней опубликованной  задачи на нашем канале (@UniLecs).
- *Отправить отзыв:* в следующем сообщеении вы отправляете свой отзыв по поводу моей работы, публикации задач на канале @UniLecs и т.д.

**P.S.** Конечно же, лучше всего ознакомиться с функциями можно, опробовав их все😜'''

categories_dict = {
    'Легкие': '*👨🏻‍💼 Легкие задачи:*\n http://telegra.ph/UniLecsLight-07-10',
    'Средние': '*👨🏻‍💻 Задачи среднего уровня:*\n http://telegra.ph/UniLecsMedium-07-10',
    'Сложные': '*👨🏻‍🎓 Сложные задачи:*\n http://telegra.ph/UniLecsHard-07-10',
    'Отмена': 'Вы отменили поиск по категориям. Выберите следующее действие.'
}

books_message = '''*📚 Подборка книг*\n 
*Основы. Часть 1.*
http://telegra.ph/UniLecsBooks-OsnovyCHast1-07-06 \n
*Основы. Часть 2.*
https://telegra.ph/UniLecs-Books-Osnovy-CHast-2-08-24 \n
*Подборка книг по C# / .Net*
https://telegra.ph/UniLecs-Books-C--Net-10-28 \n
*Алгоритмы. Часть 1.*
https://telegra.ph/UniLecs-Books-Algoritmy---CHast-1-11-19'''

about_command_message = '''Я - бот канала @UniLecs. Предоставляю автоматизированный способ получения задач и не только. Есть вопрос? Вам сюда -> @albert_davletov'''

task_list = [
    Task(1,
        'Все ли символы в строке встречаются один раз',
        'http://telegra.ph/Task-1-Vse-li-simvoly-v-stroke-vstrechayutsya-odin-raz-09-20',
        'http://telegra.ph/Task-1-Vse-li-simvoly-v-stroke-vstrechayutsya-odin-raz-09-20',
         Complexity.Easy,
         ['string', 'char', 'chars']
    ),

    Task(2,
        'Найти минимальный элемент в отсортированном по возрастанию и циклически сдвинутом массиве',
        'http://telegra.ph/Task-2-Najti-minimalnyj-ehlement-v-otsortirovannom-po-vozrastaniyu-i-ciklicheski-sdvinutom-massive-09-20',
        'http://telegra.ph/Task-2-Najti-minimalnyj-ehlement-v-otsortirovannom-po-vozrastaniyu-i-ciklicheski-sdvinutom-massive-09-20'),

    Task(3,
        "Заменить все пробелы в строке символами '%20'",
        'http://telegra.ph/Task-3-Zamenit-vse-probely-v-stroke-simvolami-20-09-21',
        'http://telegra.ph/Task-3-Zamenit-vse-probely-v-stroke-simvolami-20-09-21'),

    Task(4,
        'Вывести индекс заданного элемента в отсортированном по возрастанию и циклически сдвинутом массиве',
        'http://telegra.ph/Task-4-Vyvesti-indeks-zadannogo-ehlementa-v-otsortirovannom-po-vozrastaniyu-i-ciklicheski-sdvinutom-massive-09-22',
        'http://telegra.ph/Task-4-Vyvesti-indeks-zadannogo-ehlementa-v-otsortirovannom-po-vozrastaniyu-i-ciklicheski-sdvinutom-massive-09-22'),

    Task(5,
        'Можно ли строку сделать палиндромом',
        'http://telegra.ph/Task-5-Mozhno-li-stroku-sdelat-palindromom-09-22',
        'http://telegra.ph/Task-5-Mozhno-li-stroku-sdelat-palindromom-09-22'),

    Task(6,
        'Определить является ли одна строка перестановкой другой',
        'http://telegra.ph/Task-6-Opredelit-yavlyaetsya-li-odna-stroka-perestanovkoj-drugoj-09-22',
        'http://telegra.ph/Task-6-Opredelit-yavlyaetsya-li-odna-stroka-perestanovkoj-drugoj-09-22'),

    Task(7,
        'Вывести слова в строке в порядке убывания их длины',
        'http://telegra.ph/Task-7-Vyvesti-slova-v-stroke-v-poryadke-ubyvaniya-ih-dliny-09-23',
        'http://telegra.ph/Task-7-Vyvesti-slova-v-stroke-v-poryadke-ubyvaniya-ih-dliny-09-23'),

    Task(8,
        'Вывести максимальную сумму элементов в массиве',
        'http://telegra.ph/Task-8-Vyvesti-maksimalnuyu-summu-ehlementov-v-massive-09-23',
        'http://telegra.ph/Task-8-Vyvesti-maksimalnuyu-summu-ehlementov-v-massive-09-23'),

    Task(9,
        'Задача про числа Фибоначчи',
        'http://telegra.ph/Task-9-Zadacha-pro-chisla-Fibonachchi-09-23',
        'http://telegra.ph/Task-9-Zadacha-pro-chisla-Fibonachchi-09-23'),

    Task(10,
        'Обнуление матрицы',
        'http://telegra.ph/Task-10-Obnulenie-matricy-09-23',
        'http://telegra.ph/Task-10-Obnulenie-matricy-09-23'),

    Task(11,
        'Первый уникальный символ в строке',
        'http://telegra.ph/Task-11-Pervyj-unikalnyj-simvol-v-stroke-09-25',
        'http://telegra.ph/Task-11-Pervyj-unikalnyj-simvol-v-stroke-09-25'),

    Task(12,
        'Есть ли такие два числа в массиве, перемножив которые мы получим заданное число X',
        'http://telegra.ph/Task-12-Est-li-takie-dva-chisla-v-massive-peremnozhiv-kotorye-my-poluchim-zadannoe-chislo-X-09-26',
        'http://telegra.ph/Task-12-Est-li-takie-dva-chisla-v-massive-peremnozhiv-kotorye-my-poluchim-zadannoe-chislo-X-09-26'),

    Task(13,
        'Сжатие строки',
        'http://telegra.ph/Task-13-Szhatie-stroki-09-27',
        'http://telegra.ph/Task-13-Szhatie-stroki-09-27'),

    Task(14,
        'Вывести слова в строке в обратном порядке',
        'http://telegra.ph/Task-14-Vyvesti-slova-v-stroke-v-obratnom-poryadke-10-03',
        'http://telegra.ph/Task-14-Vyvesti-slova-v-stroke-v-obratnom-poryadke-10-03'),

    Task(15,
        'Объем воды в гистограмме',
        'http://telegra.ph/Task-15-Obem-vody-v-gistogramme-10-04',
        'http://telegra.ph/Task-15-Obem-vody-v-gistogramme-10-04'),

    Task(16,
        'Как работает банкомат ?!',
        'https://t.me/unilecs/32',
        'http://telegra.ph/Task-16-Kak-rabotaet-bankomat-10-05'),

    Task(17,
        'Поменять значения двух переменных без использования третьей',
        'https://t.me/unilecs/35',
        'https://t.me/unilecs/35'),

    Task(18,
        'Вывести непарный элемент в числовом массиве',
        'http://telegra.ph/Task-18-Vyvesti-neparnyj-ehlement-v-chislovom-massive-10-07',
        'http://telegra.ph/Task-18-Vyvesti-neparnyj-ehlement-v-chislovom-massive-10-07'),

    Task(19,
        'Найти слово в символьной матрице',
        'http://telegra.ph/Task-19-Najti-slovo-v-simvolnoj-matrice-10-10',
        'http://telegra.ph/Task-19-Najti-slovo-v-simvolnoj-matrice-10-10'),

    Task(20,
        'Степень строки',
        'http://telegra.ph/Task-20-Stepen-stroki-10-10',
        'http://telegra.ph/Task-20-Stepen-stroki-10-10'),

    Task(21,
        'Найти отсутствующий элемент в массиве',
        'http://telegra.ph/Task-21-Najti-otsutstvuyushchij-ehlement-v-massive-10-12',
        'http://telegra.ph/Task-21-Najti-otsutstvuyushchij-ehlement-v-massive-10-12'),

    Task(22,
        'Перестановка четных/нечетных элементов в массиве',
        'https://t.me/unilecs/44',
        'http://telegra.ph/Task-22-Perestanovka-chetnyhnechetnyh-ehlementov-v-massive-10-12'),

    Task(23,
        'Вывести все левые элементы в бинарном дереве',
        'https://t.me/unilecs/49',
        'http://telegra.ph/Task-23-Vyvesti-vse-levye-ehlementy-v-binarnom-dereve-10-12'),

    Task(24,
        'Найти цикл в односвязном списке',
        'https://t.me/unilecs/53',
        'http://telegra.ph/Task-24-Najti-cikl-v-odnosvyaznom-spiske-10-13'),

    Task(25,
        'Найти элемент в отсортированной матрице',
        'https://t.me/unilecs/55',
        'http://telegra.ph/Task-25-Najti-ehlement-v-otsortirovannoj-matrice-10-15'),

    Task(26,
        'Преобразование массива путем произведения всех значений',
        'https://t.me/unilecs/57',
        'http://telegra.ph/Task-26-Preobrazovanie-massiva-putem-proizvedeniya-vseh-znachenij-10-15'),

    Task(27,
        'Операции вычитания, умножения и деления через операцию сложения',
        'https://t.me/unilecs/60',
        'http://telegra.ph/Task-27-Operacii-vychitaniya-umnozheniya-i-deleniya-cherez-operaciyu-slozheniya-10-15'),

    Task(28,
        'Строки "близнецы"',
        'https://t.me/unilecs/63',
        'http://telegra.ph/Task-28-Stroki-bliznecy-10-18'),

    Task(29,
        'Найти все пары чисел в массиве, сумма которых равна',
        'https://t.me/unilecs/67',
        'http://telegra.ph/Task-29-Najti-vse-pary-chisel-v-massive-summa-ktr-ravna-X-10-19'),

    Task(30,
        'Найти максимальный элемент без использования if/else и других операторов сравнения',
        'https://t.me/unilecs/73',
        'http://telegra.ph/Task-30-Najti-maksimalnyj-ehlement-bez-ispolzovaniya-ifelse-i-drugih-operatorov-sravneniya-10-21'),

    Task(31,
        'Найти минимальное расстояние между словами в тексте',
        'https://t.me/unilecs/78',
        'http://telegra.ph/Task-31-Najti-minimalnoe-rasstoyanie-mezhdu-slovami-v-tekste-10-22'),

    Task(32,
        'Найти начало цикла в односвязном списке',
        'https://t.me/unilecs/83',
        'http://telegra.ph/Task-32-Najti-nachalo-cikla-v-odnosvyaznom-spiske-10-22'),

    Task(33,
        'Вывести все простые числа до N',
        'https://t.me/unilecs/87',
        'http://telegra.ph/Task-33-Vyvesti-vse-prostye-chisla-do-N-10-22'),

    Task(34,
        'Повернуть матрицу на 90 градусов',
        'https://t.me/unilecs/91',
        'http://telegra.ph/Task-34-Povernut-matricu-na-90-gradusov-10-22'),

    Task(35,
        'Является ли односвязный список палиндромом',
        'https://t.me/unilecs/94',
        'http://telegra.ph/Task-35-YAvlyaetsya-li-odnosvyaznyj-spisok-palindromom-10-22'),

    Task(36,
        'Единицы',
        'https://t.me/unilecs/96',
        'http://telegra.ph/Task-35-Edinicy-10-26'),

    Task(37,
        'Количество участников олимпиады',
        'https://t.me/unilecs/99',
        'http://telegra.ph/Task-37-Kolichestvo-uchastnikov-olimpiady-10-26'),

    Task(38,
        'Максимально возможное число из массива',
        'https://t.me/unilecs/103',
        'http://telegra.ph/Task-38-Maksimalno-vozmozhnoe-chislo-iz-massiva-11-01'),

    Task(39,
        'Найти сумму всех цифр в числе (без циклов)',
        'https://t.me/unilecs/106',
        'http://telegra.ph/Task-39-Najti-summu-vseh-cifr-v-chisle-11-02'),

    Task(40,
        'Проверяем число на простоту без циклов',
        'https://t.me/unilecs/109',
        'http://telegra.ph/Task-40-Proveryaem-chislo-na-prostotu-bez-ciklov-11-02'),

    Task(41,
        'Ханойские башни',
        'https://t.me/unilecs/113',
        'http://telegra.ph/Task-41-Hanojskie-bashni-11-02'),

    Task(42,
        'Баланс скобок',
        'https://t.me/unilecs/116',
        'http://telegra.ph/Task-42-Balans-skobok-11-02'),

    Task(43,
        'Коробки',
        'https://t.me/unilecs/120',
        'http://telegra.ph/Task-43-Korobki-11-12'),

    Task(44,
        'Часы с боем',
        'https://t.me/unilecs/125',
        'http://telegra.ph/Task-44-CHasy-s-boem-11-13'),

    Task(45,
        'Положить плитку',
        'https://t.me/unilecs/130',
        'http://telegra.ph/Task-45-Plitki-11-13'),

    Task(46,
        'Разворот числа',
        'https://t.me/unilecs/133',
        'http://telegra.ph/Task-46-Razvorot-chisla-11-20'),

    Task(47,
        'Разворот числа',
        'https://t.me/unilecs/135',
        'http://telegra.ph/Task-47-Raznica-v-kolichestve-bitov-11-29'),

    Task(48,
        'Выборы',
        'https://t.me/unilecs/139',
        'http://telegra.ph/Task-48-Vybory-11-29'),

    Task(49,
        'Мышка и зернышки',
        'https://t.me/unilecs/143',
        'http://telegra.ph/Task-49-Myshka-i-zernyshki-11-30'),

    Task(50,
        'Спички',
        'https://t.me/unilecs/149',
        'http://telegra.ph/Task-50-Spichki-11-30'),

    Task(51,
        'Доставка заказов',
        'https://t.me/unilecs/152',
        'http://telegra.ph/Task-51-Dostavka-zakazov-11-30'),

    Task(52,
        'Путевки',
        'https://t.me/unilecs/154',
        'http://telegra.ph/Task-52-Putevki-12-09'),

    Task(53,
        'Робот',
        'https://t.me/unilecs/158',
        'http://telegra.ph/Task-53-Robot-12-17'),

    Task(54,
        'Окружности',
        'https://t.me/unilecs/160',
        'http://telegra.ph/Task-54-Okruzhnosti-12-20'),

    Task(55,
        'Квадраты',
        'https://t.me/unilecs/164',
        'http://telegra.ph/Task-55-Kvadraty-12-22'),

    Task(56,
        'Частичные суммы матрицы',
        'https://t.me/unilecs/168',
        'http://telegra.ph/Task-56-CHastichnye-summy-matricy-12-24'),

    Task(57,
        'Парковка',
        'https://t.me/unilecs/170',
        'http://telegra.ph/Task-57-Parkovka-12-26'),

    Task(58,
        'Формула 1',
        'https://t.me/unilecs/176',
        'http://telegra.ph/Task-58-Formula-1-12-26'),

    Task(59,
        'Заказы',
        'https://t.me/unilecs/182',
        'http://telegra.ph/Task-59-Zakazy-01-03'),

    Task(60,
        '"Сложение" связных списков',
        'https://t.me/unilecs/187',
        'http://telegra.ph/Task-60-Slozhenie-svyaznyh-spiskov-01-08'),

    Task(61,
        'Дорожная служба',
        'https://t.me/unilecs/190',
        'http://telegra.ph/Task-61-Dorozhnaya-sluzhba-01-11'),

    Task(62,
        'Подарки',
        'https://t.me/unilecs/195',
        'http://telegra.ph/Task-62-Podarki-01-15'),

    Task(63,
        'НОК',
        'https://t.me/unilecs/198',
        'http://telegra.ph/Task-63-NOK---naimenshee-obshchee-kratnoe-01-19'),

    Task(64,
        'Одинаковый периметр',
        'https://t.me/unilecs/201',
        'http://telegra.ph/Task-64-Odinakovyj-perimetr-01-22'),

    Task(65,
        'Площадь многоугольника',
        'https://t.me/unilecs/205',
        'http://telegra.ph/Task-65-Ploshchad-trapecij-01-25'),

    Task(66,
        'Степень двойки',
        'https://t.me/unilecs/212',
        'http://telegra.ph/Task-66-Stepen-dvojki-01-30'),

    Task(67,
        'Количество точек',
        'https://t.me/unilecs/215',
        'http://telegra.ph/Task-67-Kolichestvo-tochek-02-02'),

    Task(68,
        'Две цифры',
        'https://t.me/unilecs/220',
        'http://telegra.ph/Task-68-Dve-cifry-02-05'),

    Task(69,
        'Количество нулей в конце факториала',
        'https://t.me/unilecs/224',
        'http://telegra.ph/Task-69-Kolichestvo-nulej-v-konce-faktoriala-02-06'),

    Task(70,
        'Прямой угол',
        'https://t.me/unilecs/227',
        'http://telegra.ph/Task-70-Pryamoj-ugol-02-07'),

    Task(71,
        'Как правильно поливать дерево',
        'https://t.me/unilecs/232',
        'http://telegra.ph/Task-71-Kak-pravilno-polivat-derevya-v-sadu-02-13'),

    Task(72,
        'Возводим в степень',
        'https://t.me/unilecs/236',
        'http://telegra.ph/Task-72-Vozvodim-v-stepen-02-18'),

    Task(73,
        'Три единицы',
        'https://t.me/unilecs/239',
        'http://telegra.ph/Task-73-Tri-edinicy-02-21'),

    Task(74,
        'Несократимая дробь',
        'https://t.me/unilecs/243',
        'http://telegra.ph/Task-74-Nesokratimaya-drob-02-25'),

    Task(75,
        'Тумблеры',
        'https://t.me/unilecs/247',
        'http://telegra.ph/Task-75-Tumblery-02-26'),

    Task(76,
        'Перестановка массива',
        'https://t.me/unilecs/250',
        'http://telegra.ph/Task-76-Perestanovka-massiva-03-06'),

    Task(77,
        'Площадь четырехугольника',
        'https://t.me/unilecs/253',
        'http://telegra.ph/Task-77-Ploshchad-chetyrehugolnika-03-07'),

    Task(78,
        'Цифровой корень числа',
        'https://t.me/unilecs/257',
        'http://telegra.ph/Task-78-Cifrovoj-koren-chisla-03-11'),

    Task(79,
        'Гистограмма',
        'https://t.me/unilecs/260',
        'http://telegra.ph/Task-79-Gistogramma-03-12'),

    Task(80,
        'Двоичное дерево поиска',
        'https://t.me/unilecs/264',
        'http://telegra.ph/Task-80-Dvoichnoe-derevo-poiska-03-12'),

    Task(81,
        'Факторизация числа',
        'https://t.me/unilecs/269',
        'http://telegra.ph/Task-81-Faktorizaciya-chisla-03-21'),

    Task(82,
        'Уравнение',
        'https://t.me/unilecs/274',
        'http://telegra.ph/Task-82-Uravnenie-03-26'),

    Task(83,
        'Уравнение 2',
        'https://t.me/unilecs/288',
        'http://telegra.ph/Task-83-Uravnenie-2-04-03'),

    Task(84,
        'Анаграммы',
        'https://t.me/unilecs/292',
        'http://telegra.ph/Task-84-Anagrammy-03-30'),

    Task(85,
        'Незаконченная формула',
        'https://t.me/unilecs/297',
        'http://telegra.ph/Task-85-Nezakonchennaya-formula-04-12'),

    Task(86,
        'Семь раз отмерь, один раз отрежь',
        'https://t.me/unilecs/302',
        'http://telegra.ph/Task-86-Sem-raz-otmer-odin-raz-otrezh-04-17'),

    Task(87,
        'Построение',
        'https://t.me/unilecs/306',
        'http://telegra.ph/Task-87-Postroenie-04-23'),

    Task(88,
        'Биномиальный коэффициент',
        'https://t.me/unilecs/312',
        'http://telegra.ph/Task-88-Binomialnyj-koehfficient-04-24'),

    Task(89,
        'Сейф',
        'https://t.me/unilecs/316',
        'http://telegra.ph/Task-89-Sejf-04-29'),

    Task(90,
        'Грядки',
        'https://t.me/unilecs/319',
        'http://telegra.ph/Task-90-Gryadki-04-30'),

    Task(91,
        'Обработка массива',
        'https://t.me/unilecs/322',
        'http://telegra.ph/Task-91-Obrabotka-massiva-05-03'),

    Task(92,
        'Система уравнений',
        'https://t.me/unilecs/327',
        'http://telegra.ph/Task-92-Sistema-uravnenij-05-08'),

    Task(93,
        'Очередь за билетами',
        'https://t.me/unilecs/329'
        'http://telegra.ph/Task-93-Ochered-za-biletami-05-11'),

    Task(94,
        'Пирог',
        'https://t.me/unilecs/333',
        'http://telegra.ph/Task-94-Pirog-05-15'),

    Task(95,
        'Площадь выделенной области',
        'https://t.me/unilecs/337',
        'http://telegra.ph/Task-95-Ploshchad-vydelennoj-oblasti-05-17'),

    Task(96,
        'Пересечение',
        'https://t.me/unilecs/340',
        'http://telegra.ph/Task-96-Peresechenie-05-22'),

    Task(97,
        'Место в строю',
        'https://t.me/unilecs/345',
        'http://telegra.ph/Task-97-Mesto-v-stroyu-05-24'),

    Task(98,
        'Количество взвешиваний',
        'https://t.me/unilecs/350',
        'http://telegra.ph/Task-98-Kolichestvo-vzveshivanij-05-28'),

    Task(99,
        'Непростая сортировка',
        'https://t.me/unilecs/353',
        'http://telegra.ph/Task-99-Neprostaya-sortirovka-06-01'),

    Task(100,
        'Овощная нарезка',
        'https://t.me/unilecs/359',
        'http://telegra.ph/Task-100-Ovoshchnaya-tarelka-06-03'),

    Task(101,
        'Мажоритарный элемент',
        'https://t.me/unilecs/368',
        'http://telegra.ph/Task-101-Mazhoritarnyj-ehlement-massiva-06-11'),

    Task(102,
        'Минимальное кол-во операций',
        'https://t.me/unilecs/372',
        'http://telegra.ph/Task-102-Minimalnoe-kol-vo-operacij-06-13'),

    Task(103,
        'Количество пересечений',
        'https://t.me/unilecs/377',
        'http://telegra.ph/Task-103-Kolichestvo-peresechenij-06-18'),

    Task(104,
        'Кошки-мышки',
        'https://t.me/unilecs/381',
        'http://telegra.ph/Task-104-Koshki---myshki-06-25'),

    Task(105,
        'Квартальные оценки',
        'https://t.me/unilecs/385',
        'http://telegra.ph/Task-105-Kvartalnye-ocenki-06-26'),

    Task(106,
        'Частичная сумма',
        'https://t.me/unilecs/389',
        'http://telegra.ph/Task-106-CHastichnaya-summa-06-29'),

    Task(107,
        'Основы графов',
        'https://t.me/unilecs/399',
        'https://telegra.ph/Task-107-Osnovy-grafov-07-08'),

    Task(108,
        'Теория множеств',
        'https://t.me/unilecs/402',
        'https://telegra.ph/Task-108-Teoriya-mnozhestv-07-16'),

    Task(109,
        'Медиана и среднее арифметическое',
        'https://t.me/unilecs/407',
        'https://telegra.ph/Task-109-Mediana-i-srednee-arifmeticheskoe-07-17'),

    Task(110,
        'Будни браконьера',
        'https://t.me/unilecs/410',
        'https://telegra.ph/UniLecs-110-Budni-brakonera-07-20'),

    Task(111,
        'Финал',
        'https://t.me/unilecs/414',
        'https://telegra.ph/UniLecs-111-Final-07-24'),

    Task(112,
        'Совещание',
        'https://t.me/unilecs/416',
        'https://telegra.ph/UniLecs-112-Soveshchanie-07-29'),

    Task(113,
        'Инициализация массива',
        'https://t.me/unilecs/421',
        'https://telegra.ph/UniLecs-113-Inicializaciya-massiva-07-31'),

    Task(114,
        'Тетрадь в клеточку',
        'https://t.me/unilecs/424',
        'https://telegra.ph/UniLecs-114-Tetrad-v-kletochku-08-02'),

    Task(115,
        'Чемпионат',
        'https://t.me/unilecs/430',
        'https://telegra.ph/UniLecs-115-CHempionat-08-06'),

    Task(116,
        'Вагонетка',
        'http://telegra.ph/Anons-116-Vagonetka-08-09',
        'https://telegra.ph/UniLecs-116-Vagonetka-08-13'),

    Task(117,
        'Снова степень',
        'https://t.me/unilecs/436',
        'https://telegra.ph/UniLecs-117-Snova-stepen-08-13'),

    Task(118,
        'Сумма на дереве',
        'https://telegra.ph/Anons-118-Summa-na-dereve-08-17',
        'https://telegra.ph/UniLecs-118-Summa-na-dereve-08-20'),

    Task(119,
        'Седловой элемент матрицы',
        'https://telegra.ph/Anons-119-Sedlovoj-ehlement-matricy-08-20',
        'https://telegra.ph/UniLecs-119-Sedlovoj-ehlement-matricy-08-20'),

    Task(120,
        'Линия Фронта',
        'https://telegra.ph/Anons-120-Liniya-fronta-08-23',
        'https://telegra.ph/UniLecs-120-Liniya-Fronta-08-24'),

    Task(121,
        'cAPS LOCK',
        'https://telegra.ph/Anons-121-cAPS-LOCK-08-27',
        'https://telegra.ph/UniLecs-121-cAPS-LOCK-08-27'),

    Task(122,
        'Максимальная подматрица',
        'https://telegra.ph/Anons-122-Maksimalnaya-podmatrica-08-31',
        'https://telegra.ph/UniLecs-122-Maksimalnaya-podmatrica-08-31'),

    Task(123,
        'Разливное пиво',
        'https://telegra.ph/Anons-123-Razlivnoe-pivo-09-04',
        'https://telegra.ph/UniLecs-123-Razlivnoe-pivo-09-03'),

    Task(124,
        'Диверсификация',
        'https://telegra.ph/Anons-124-Diversifikaciya-09-07',
        'https://telegra.ph/UniLecs-124-Diversifikaciya-09-08'),

    Task(125,
        'Ноты фортепиано',
        'https://telegra.ph/Anons-125-Noty-fortepiano-09-09',
        'https://telegra.ph/UniLecs-125-Noty-fortepiano-09-09'),

    Task(126,
        'Строковые комбинации',
        'https://telegra.ph/Anons-126-Strokovye-kombinacii-09-13',
        'https://telegra.ph/UniLecs-126-Strokovye-kombinacii-09-14'),

    Task(127,
        'Интервальная сумма',
        'https://telegra.ph/Anons-127-Intervalnaya-summa-09-16',
        'https://telegra.ph/UniLecs-127-Intervalnaya-summa-09-16'),

    Task(128,
        'Максимальное разбиение числа',
        'https://telegra.ph/Anons-128-Maksimalnoe-razbienie-chisla-09-20',
        'https://telegra.ph/UniLecs-128-Maksimalnoe-razbienie-chisla-09-20'),

    Task(129,
        'Побитовая арифметика',
        'https://telegra.ph/Anons-129-Pobitovaya-arifmetika-09-23',
        'https://telegra.ph/UniLecs-129-Pobitovaya-arifmetika-09-23'),

    Task(130,
        'Разбиение числа',
        'https://telegra.ph/Anons-130-Razbienie-chisla-09-27',
        'https://telegra.ph/UniLecs-130-Razbienie-chisla-09-27'),

    Task(131,
        'Champions League',
        'https://telegra.ph/Anons-131-Champions-League-10-01',
        'https://telegra.ph/UniLecs-131-Champions-League-10-01'),

    Task(132,
        'Дураки и дороги',
        'https://telegra.ph/Anons-132-Duraki-i-dorogi-10-14',
        'https://telegra.ph/UniLecs-132-Duraki-i-dorogi-10-14'),

    Task(133,
        'Pac-Man',
        'https://telegra.ph/Anons-133-Pac-Man-10-18',
        'https://telegra.ph/UniLecs-134-Pac-Man-10-19'),

    Task(134,
        'Пропущенный символ',
        'https://telegra.ph/Anons-134-Propushchennyj-simvol-10-22',
        'https://telegra.ph/UniLecs-134-Propushchennyj-simvol-10-22'),

    Task(135,
        'Пирамида',
        'https://telegra.ph/Anons-135-Piramida-10-26',
        'https://telegra.ph/UniLecs-135-Piramida-10-26'),

    Task(136,
        'Custom String.IndexOf()',
        'https://telegra.ph/Anons-136-Custom-StringIndexOf-10-29',
        'https://telegra.ph/UniLecs-136-Custom-StringIndexOf-10-29'),

    Task(137,
        'Multiplication of digits',
        'https://telegra.ph/Anons-137-Multiplication-of-digits-11-02',
        'https://telegra.ph/UniLecs-137-Multiplication-of-digits-11-04'),

    Task(138,
        'Максимальная последовательность по модулю',
        'https://telegra.ph/Anons-138-Maksimalnaya-posledovatelnost-po-modulyu-11-05',
        'https://telegra.ph/UniLecs-138-Maksimalnaya-posledovatelnost-po-modulyu-11-05'),

    Task(139,
        'Произведение чисел в массива между минимальным и максимальным элементом',
        'https://telegra.ph/Anons-139-Proizvedenie-chisel-v-massive-mezhdu-minimalnym-i-maksimalnym-ehlementom-11-11',
        'https://telegra.ph/UniLecs-139-Proizvedenie-chisel-v-massive-mezhdu-minimalnym-i-maksimalnym-ehlementom-11-11'
        ),

    Task(140,
        'Лошадью ходи!',
        'https://telegra.ph/Anons-140-Loshadyu-hodi-11-12',
        'https://telegra.ph/UniLecs-140-Loshadyu-hodi-11-12',
        'solutionLink',
         Complexity.Middle,
         ['string', 'char', 'chars']
        )
]
