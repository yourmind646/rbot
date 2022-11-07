# Aiogram imports
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait, PeerIdInvalid, UsernameNotOccupied
from pyrogram.enums import ChatAction
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.handlers import MessageHandler

# Another imports
from datetime import datetime
from re import search as re_search
from asyncio import sleep
import random
import simplejson as json


# Загрузка данных из конфига
with open('login_data.json', 'r') as j:
	login_data = json.load(j)

# Инициализация объекта клиента
client = Client(login_data.get('session_name'), api_id = login_data.get('API_ID'), api_hash = login_data.get('API_HASH'))


# Отправка лога в избранные
async def send_log(msg: str, error_info: str):
	await client.send_message("me", f"❌ {msg}\n💬 [{datetime.now().strftime('%H:%M')}] {error_info}")


# Получаем полное имя, если канал или чат, то title
async def get_name(msg: Message):
	if msg.chat.title is None:

		if msg.chat.first_name is None:
			name = ""
		else:
			name = msg.chat.first_name + " "

		if msg.chat.last_name is None:
			surname = ""
			name = name[:-1]
		else:
			surname = msg.chat.last_name

		return f"{name}{surname}"
	else:
		return msg.chat.title


# /typing text=str; ts=symbol;
# /t text=str; ts=symbol;
@client.on_message(filters.command(commands = ["typing", "t"], prefixes = "/") & filters.me)
async def typing(client: Client, msg: Message, _text = "", _ts = ""):
	# Если функция вызвана из другой
	if _text and _ts:
		text = _text
		ts = _ts
	# Иначе парсим
	else:
		# Парсинг текста
		text_parsing = re_search(r'(?<=text\=).+?(?=;)', msg.text)
		# Парсинг символа печати
		ts_parsing = re_search(r'(?<=ts\=).+?(?=;)', msg.text)
		
		# Обработка парсинга текста
		if text_parsing:
			text = text_parsing[0]
		else:
			await msg.delete()
			await send_log(msg = msg.text, error_info = "Не указан текст для печати")
			return

		# Обработка парсинга символа
		if ts_parsing:
			ts = ts_parsing[0]
		# Value by default
		else:
			ts = "_"
		
	# Копируем, чтобы вытаскивать символы
	copied_text = text

	# Результат печати
	to_be_printed = ""

	# Пока планируемый текст не равен оригинальному, то печатаем
	while to_be_printed != text:

		try:
			await msg.edit(to_be_printed + ts)
			await sleep(.1)

			to_be_printed += copied_text[0]
			copied_text = copied_text[1:]

			await msg.edit(to_be_printed)
			await sleep(.1)

		except FloodWait as fw:
			await sleep(fw.value)

		except Exception:
			pass


# ❤️ magic text=str;
@client.on_message(filters.command(commands = "magic", prefixes = '❤️ ') & filters.me)
async def magic(client: Client, msg: Message):

	# Парсинг текста
	text_parsing = re_search(r'(?<=text\=).+?(?=;)', msg.text)

	# Обработка парсинга текста
	if text_parsing:
		text = text_parsing[0]
	# Value by default
	else:
		text = '❤️'

	# Фреймы
	frame_1 = """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍"""

	frame_2 = frame_1.replace("❤️", "🧡")

	frame_3 = frame_1.replace("❤️", "💛")

	frame_4 = frame_1.replace("❤️", "💚")

	frame_5 = frame_1.replace("❤️", "💙")

	frame_6 = frame_1.replace("❤️", "💜")

	frame_7 = frame_1.replace("❤️", "🖤")

	frame_8 = frame_1.replace("❤️", "🤎")

	# Ассортимент сердец
	heart_assortment = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "🤎"]

	# Рандомные фреймы
	frame_9 = "".join(
		list(map(lambda x: "\n" if x == "\n" else random.choice(heart_assortment) if x != "🤍" else "🤍", frame_8)))

	frame_10 = "".join(
		list(map(lambda x: "\n" if x == "\n" else random.choice(heart_assortment) if x != "🤍" else "🤍", frame_8)))

	frame_11 = "".join(
		list(map(lambda x: "\n" if x == "\n" else random.choice(heart_assortment) if x != "🤍" else "🤍", frame_8)))

	frame_12 = "".join(
		list(map(lambda x: "\n" if x == "\n" else random.choice(heart_assortment) if x != "🤍" else "🤍", frame_8)))

	frame_13 = "".join(
		list(map(lambda x: "\n" if x == "\n" else random.choice(heart_assortment) if x != "🤍" else "🤍", frame_8)))

	# Объединяем все фреймы в список
	frames_to_print = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8, frame_9, frame_10, frame_11, frame_12, frame_13, frame_1]

	# Отображаем все фреймы
	for frame in frames_to_print:

		try:
			await msg.edit(frame)
			await sleep(.4)

		except FloodWait as fw:
			await sleep(fw.value)

			await msg.edit(frame)
			await sleep(.4)

	# Заполняем фон красными сердцами
	while frame_1.find("🤍") != -1:

		try:
			# Реплейсим одно белое на красное
			frame_1 = frame_1.replace("🤍", "❤️", 1)
			# Отображаем
			await msg.edit(frame_1)
			await sleep(.1)

		except FloodWait as fw:
			await sleep(fw.value)

			# Отображаем
			await msg.edit(frame_1)
			await sleep(.1)

	# Список строк фрейма
	heart_rows_list = frame_1.split("\n")
	# Обрезаем строки, пока не останется один символ (8 итераций)
	for _ in range(8):
		# Удаляется нижняя строка
		del heart_rows_list[len(heart_rows_list) - 1]

		# Удаляется по одному последнему символу из строк
		for i in range(len(heart_rows_list)):
			heart_rows_list[i] = heart_rows_list[i][:-2]

		# Отображаем фрейм
		try:
			frame = "\n".join(heart_rows_list)

			await msg.edit(frame)
			await sleep(.4)

		except FloodWait as fw:
			await sleep(fw.value)

			await msg.edit(frame)
			await sleep(.4)

	# Отображаем конечное сообщение
	try:
		await msg.edit(text)

	except FloodWait as fw:
		await sleep(fw.value)
		await msg.edit(text)

	except Exception:
		pass


# ❤️ mini-magic text=str;
@client.on_message(filters.command(commands = "mini-magic", prefixes = '❤️ ') & filters.me)
async def mini_magic(client: Client, msg: Message):

	# Парсинг текста
	text_parsing = re_search(r'(?<=text\=).+?(?=;)', msg.text)

	# Обработка парсинга текста
	if text_parsing:
		text = text_parsing[0]
	# Value by default
	else:
		text = '❤️'

	# Фреймы
	frame_1 = """✨💎💎✨💎💎✨
💎💎💎💎💎💎💎
💎💎💎💎💎💎💎
✨💎💎💎💎💎✨
✨✨💎💎💎✨✨
✨✨✨💎✨✨✨
"""

	frame_2 = frame_1.replace("💎", "🌺")
	frame_3 = frame_1.replace("💎", "😘").replace("✨", "☁️")
	frame_4 = frame_1.replace("💎", "🌸")
	frame_5 = frame_1.replace("💎", "🐸").replace("✨", "🌾")
	frame_6 = frame_1.replace("💎", "💥").replace("✨", "🔫")
	frame_7 = frame_1.replace("💎", "💟").replace("✨", "☁️")
	frame_8 = frame_1.replace("💎", "💖").replace("✨", "🍀")
	frame_9 = frame_1.replace("💎", "🐼").replace("✨", "🌴")

	# Объединяем все фреймы в список
	frames = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8, frame_9]

	# Отображаем каждый фрейм
	for frame in frames:
		
		try:
			await msg.edit(frame)
			await sleep(.5)

		except FloodWait as fw:
			await sleep(fw.value)

			await msg.edit(frame)
			await sleep(.5)

	# Отображаем конечное сообщение
	try:
		await msg.edit(text)

	except FloodWait as fw:
		await sleep(fw.value)
		await msg.edit(text)

	except Exception:
		pass


# /orange
@client.on_message(filters.command(commands = "orange", prefixes = "/") & filters.me)
async def orange(client: Client, msg: Message):
	frame_1 = "🍊🍊🍊 ЗаВодНоЙ АпЕлЬсИн 🍊🍊🍊"
	frame_2 = "🍊🍊 ЗаВодНоЙ АпЕлЬсИн 🍊🍊"
	frame_3 = "🍊 ЗаВодНоЙ АпЕлЬсИн 🍊"

	frames = [frame_1, frame_2, frame_3, frame_2, frame_1, frame_2, frame_3, frame_2, frame_1, frame_2, frame_3, frame_2, frame_1, frame_2, frame_3, frame_2, frame_1, "🍊"]

	for frame in frames:
		try:
			await msg.edit(frame)
			await sleep(.5)

		except FloodWait as fw:
			await sleep(fw.value)

			await msg.edit(frame)
			await sleep(.5)


# /coin
@client.on_message(filters.command(commands = "coin", prefixes = "/") & filters.me)
async def coin(client: Client, msg: Message):
	# Начальный текст
	text = "♻️ Подкидываю монетку..."
	# Два исхода
	events = ["Орёл 🦅", "Решка 💸"]

	# Анимируем точки
	try:
		await msg.edit(text)

		await sleep(.4)

		for _ in range(3):
			for i in range(-1, -3, -1):
				await msg.edit(text[:i])

				await sleep(.4)
		
	except FloodWait as fw:
		await sleep(fw.value)

	# Отображаем результат рандоминга
	try:
		await msg.edit(random.choice(events))

	except FloodWait as fw:
		await sleep(fw.value)
		await msg.edit(random.choice(events))


# /roll to=int;
@client.on_message(filters.command(commands = "roll", prefixes = "/") & filters.me)
async def roll(client: Client, msg: Message):
	
	# Парсинг to
	to_parsing = re_search(r'(?<=to\=).+?(?=;)', msg.text)

	# Обработка парсинга to
	if to_parsing:
		try:
			to = int(to_parsing[0])
		except ValueError:
			await msg.delete()
			await send_log(msg = msg.text, error_info = "Параметр 'to' должен быть числовым")
			return

	# Value by default
	else:
		to = 100

	emojis = {
		"0": "0️⃣",
		"1": "1️⃣",
		"2": "2️⃣",
		"3": "3️⃣",
		"4": "4️⃣",
		"5": "5️⃣",
		"6": "6️⃣",
		"7": "7️⃣",
		"8": "8️⃣",
		"9": "9️⃣",
	}

	text = f"♻️ Рандомлю число (от 1 до {to}) |"

	# Воспроизведение анимации роллинга
	try:
		await msg.edit(text)

		await sleep(.4)

		for _ in range(3):
			for s in ["/", "-", "\\", "|"]:
				await msg.edit(text[:-1] + s)
				await sleep(.4)

		random_number = str(random.randint(1, to))

		result = ""

		for n in random_number:
			result += emojis[n]

	except FloodWait as fw:
		await sleep(fw.value)

	# Отображаем результат
	try:
		await msg.edit(result)

	except FloodWait as fw:
		await sleep(fw.value)
		await msg.edit(result)


# /reverse text=str;
@client.on_message(filters.command(commands = ["reverse", "r"], prefixes = "/") & filters.me)
async def reverse(client: Client, msg: Message):
	
	# Парсинг текста
	text_parsing = re_search(r'(?<=text\=).+?(?=;)', msg.text)
	
	# Обработка парсинга текста
	if text_parsing:
		text = text_parsing[0]
	else:
		await msg.delete()
		await send_log(msg = msg.text, error_info = "Не указан текст для 'reverse'")
		return

	# Reversing
	reversed_text = "".join(reversed(list(text)))

	# Result
	try:
		await msg.edit(reversed_text)

	except FloodWait as fw:
		await sleep(fw.value)
		await msg.edit(reversed_text)


# /ily text=str; ts=str;
# /iloveyou text=str; ts=str;
@client.on_message(filters.command(commands = ["ily", "iloveyou"], prefixes = "/") & filters.me)
async def ily(client: Client, msg: Message):

	# Парсинг текста
	text_parsing = re_search(r'(?<=text\=).+?(?=;)', msg.text)
	# Парсинг символа печати
	ts_parsing = re_search(r'(?<=ts\=).+?(?=;)', msg.text)
	
	# Обработка парсинга текста
	if text_parsing:
		text = text_parsing[0]
	# Value by default
	else:
		text = "❤️"

	# Обработка парсинга символа
	if ts_parsing:
		ts = ts_parsing[0]
	# Value by default
	else:
		ts = "_"

	# Фреймы анимации
	first_frame = """✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨✨✨✨✨✨
✨✨✨✨✨✨🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

	i_frame = """✨✨✨✨✨✨✨✨✨✨✨
✨❤️❤️❤️❤️❤️❤️❤️❤️❤️✨
✨❤️❤️❤️❤️❤️❤️❤️❤️❤️✨
✨✨✨✨❤️❤️✨✨✨✨✨
✨✨✨✨❤️❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃❤️❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃❤️❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃❤️❤️🌃🌃🌃🌃🌃
🌃❤️❤️❤️❤️❤️❤️❤️❤️❤️🌃
🌃❤️❤️❤️❤️❤️❤️❤️❤️❤️🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

	second_frame = """✨✨✨✨✨✨✨✨✨✨✨
✨❤️❤️✨✨✨✨✨✨✨✨
✨❤️❤️✨✨✨✨✨✨✨✨
✨❤️❤️✨✨✨✨✨✨✨✨
✨❤️❤️✨✨✨🌃🌃🌃🌃🌃
🌃❤️❤️🌃🌃🌃🌃🌃🌃🌃🌃
🌃❤️❤️🌃🌃🌃🌃🌃🌃🌃🌃
🌃❤️❤️🌃🌃🌃🌃🌃🌃🌃🌃
🌃❤️❤️❤️❤️❤️❤️❤️❤️🌃🌃
🌃❤️❤️❤️❤️❤️❤️❤️❤️🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

	third_frame = """✨✨✨✨✨✨✨✨✨✨✨
✨✨✨❤️❤️❤️❤️❤️✨✨✨
✨✨❤️❤️❤️❤️❤️❤️❤️✨✨
✨❤️❤️❤️✨✨✨❤️❤️❤️✨
✨❤️❤️✨✨✨🌃🌃❤️❤️🌃
🌃❤️❤️🌃🌃🌃🌃🌃❤️❤️🌃
🌃❤️❤️🌃🌃🌃🌃🌃❤️❤️🌃
🌃❤️❤️❤️🌃🌃🌃❤️❤️❤️🌃
🌃🌃❤️❤️❤️❤️❤️❤️❤️🌃🌃
🌃🌃🌃❤️❤️❤️❤️❤️🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

	fourth_frame = """✨✨✨✨✨✨✨✨✨✨✨
✨❤️✨✨✨✨✨✨✨❤️✨
✨❤️✨✨✨✨✨✨✨❤️✨
✨❤️❤️✨✨✨✨✨❤️❤️✨
✨✨❤️✨✨✨🌃🌃❤️🌃🌃
🌃🌃❤️❤️🌃🌃🌃❤️❤️🌃🌃
🌃🌃❤️❤️🌃🌃🌃❤️❤️🌃🌃
🌃🌃🌃❤️🌃🌃🌃❤️🌃🌃🌃
🌃🌃🌃🌃❤️❤️❤️🌃🌃🌃🌃
🌃🌃🌃🌃🌃❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

	fifth_frame = """✨❤️❤️❤️❤️❤️❤️❤️❤️❤️✨
✨❤️❤️❤️❤️❤️❤️❤️❤️❤️✨
✨❤️❤️✨✨✨✨✨✨✨✨
✨❤️❤️✨✨✨✨✨✨✨✨
✨❤️❤️❤️❤️❤️❤️❤️❤️❤️🌃
🌃❤️❤️❤️❤️❤️❤️❤️❤️❤️🌃
🌃❤️❤️🌃🌃🌃🌃🌃🌃🌃🌃
🌃❤️❤️🌃🌃🌃🌃🌃🌃🌃🌃
🌃❤️❤️❤️❤️❤️❤️❤️❤️❤️🌃
🌃❤️❤️❤️❤️❤️❤️❤️❤️❤️🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

	sixth_frame = """✨✨✨✨✨✨✨✨✨✨✨
✨❤️✨✨✨✨✨✨✨❤️✨
✨✨❤️✨✨✨✨✨❤️✨✨
✨✨✨❤️✨✨✨❤️✨✨✨
✨✨✨✨❤️✨❤️🌃🌃🌃🌃
🌃🌃🌃🌃🌃❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃❤️🌃🌃🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

	seventh_frame = """✨✨✨✨✨✨✨✨✨✨✨
✨✨✨❤️❤️❤️❤️❤️✨✨✨
✨✨❤️❤️❤️❤️❤️❤️❤️✨✨
✨❤️❤️❤️✨✨✨❤️❤️❤️✨
✨❤️❤️✨✨✨🌃🌃❤️❤️🌃
🌃❤️❤️🌃🌃🌃🌃🌃❤️❤️🌃
🌃❤️❤️🌃🌃🌃🌃🌃❤️❤️🌃
🌃❤️❤️❤️🌃🌃🌃❤️❤️❤️🌃
🌃🌃❤️❤️❤️❤️❤️❤️❤️🌃🌃
🌃🌃🌃❤️❤️❤️❤️❤️🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

	eighth_frame = """✨✨✨✨✨✨✨✨✨✨✨
✨❤️❤️✨✨✨✨✨❤️❤️✨
✨❤️❤️✨✨✨✨✨❤️❤️✨
✨❤️❤️✨✨✨✨✨❤️❤️✨
✨❤️❤️✨✨✨🌃🌃❤️❤️🌃
🌃❤️❤️🌃🌃🌃🌃🌃❤️❤️🌃
🌃❤️❤️🌃🌃🌃🌃🌃❤️❤️🌃
🌃❤️❤️❤️🌃🌃🌃❤️❤️❤️🌃
🌃🌃❤️❤️❤️❤️❤️❤️❤️🌃🌃
🌃🌃🌃❤️❤️❤️❤️❤️🌃🌃🌃
🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃🌃"""

	# Объединяем фреймы в один список
	frames = [first_frame, i_frame, second_frame, third_frame, fourth_frame, fifth_frame, sixth_frame, seventh_frame, eighth_frame]

	# Выводим каждый фрейм с к/д в 0.7 сек
	for frame in frames:

		try:
			await msg.edit(frame)
			await sleep(.7)

		except FloodWait as fw:
			await sleep(fw.value)
			
			await msg.edit(frame)
			await sleep(.7)

	# Запускаем печать текста, если он не равен дефолтному значению
	if text == "❤️":
		await msg.edit(text)

	else:
		await typing(client, msg, text, ts)


# /m
# /moon
@client.on_message(filters.command(commands = ["m", "moon"], prefixes = "/") & filters.me)
async def moon(client: Client, msg: Message):
	# str -> list
	text_list = list("Спокойной ночи ❤️🌕❤️")
	# Фреймы луны
	moons_list = ["🌖", "🌗", "🌘", "🌑", "🌒", "🌓", "🌔", "🌕"]

	# Изменяем сообщение на первый фрейм
	try:
		await msg.edit("".join(text_list))

	except FloodWait as fw:
		await sleep(fw.value)
		await msg.edit("".join(text_list))

	# 3 полных оборота
	for _ in range(3):
		
		# Выполняется полный оборот луны
		for moon in moons_list:

			try:
				# КД 0.5 сек
				await sleep(.35)
				# Заменяем луну на другую стадию поворота
				text_list[-3] = moon
				# Отображаем
				await msg.edit("".join(text_list))

			except FloodWait as fw:
				await sleep(fw.value)

				# Отображаем
				await msg.edit("".join(text_list))


# ❤️ magic2 text=str;
@client.on_message(filters.command(commands = "magic2", prefixes = '❤️ ') & filters.me)
async def magic2(client: Client, msg: Message):

	# Парсинг текста
	text_parsing = re_search(r'(?<=text\=).+?(?=;)', msg.text)
	
	# Обработка парсинга текста
	if text_parsing:
		text = text_parsing[0]
	# Value by default
	else:
		text = "❤️"


	# Поле
	field = ["⚪️"]
	
	# Отправляем белый кружок
	try:
		await msg.edit(field[0])
		await sleep(.4)

	except FloodWait as fw:
		await sleep(fw.value)

		await msg.edit(field[0])
		await sleep(.4)

	# Заполняем фон
	for i in range(8):
		for row in enumerate(field):
			field[row[0]] = row[1] + "⚪️"

		field.append(field[0])

		try:
			frame = "\n".join(field)

			await msg.edit(frame)
			await sleep(.4)

		except FloodWait as fw:
			await sleep(fw.value)

			await msg.edit(frame)
			await sleep(.4)

	# Копируем фон
	white_fon = field.copy()

	# Шаблоны строк
	heart_rows = {
		1: "⚪️⚪️❤️❤️⚪️❤️❤️⚪️⚪️",
		2: "⚪️❤️❤️❤️❤️❤️❤️❤️⚪️",
		3: "⚪️❤️❤️❤️❤️❤️❤️❤️⚪️",
		4: "⚪️❤️❤️❤️❤️❤️❤️❤️⚪️",
		5: "⚪️⚪️❤️❤️❤️❤️❤️⚪️⚪️",
		6: "⚪️⚪️⚪️❤️❤️❤️⚪️⚪️⚪️",
		7: "⚪️⚪️⚪️⚪️❤️⚪️⚪️⚪️⚪️"
	}
	
	# Отрисовываем сердце
	for i in range(1, 8):
		field[i] = heart_rows[i]

		try:
			frame = "\n".join(field)

			await msg.edit(frame)
			await sleep(.4)

		except FloodWait as fw:
			await sleep(fw.value)

			await msg.edit(frame)
			await sleep(.4)


	# Assortment
	heart_assortment = ["🧡", "💛", "💚", "💙", "💜"]

	# Анимируем сердце разными цветами
	for heart in heart_assortment:
		try:
			frame = "\n".join(field).replace("❤️", heart)

			await msg.edit(frame)
			await sleep(.4)

		except FloodWait as fw:
			await sleep(fw.value)

			await msg.edit(frame)
			await sleep(.4)
	
	# Шаблоны строк 2
	rainbow_heart_rows = {
		1: "⚪️⚪️❤️❤️⚪️❤️❤️⚪️⚪️",
		2: "⚪️🧡🧡🧡🧡🧡🧡🧡⚪️",
		3: "⚪️💛💛💛💛💛💛💛⚪️",
		4: "⚪️💚💚💚💚💚💚💚⚪️",
		5: "⚪️⚪️💙💙💙💙💙⚪️⚪️",
		6: "⚪️⚪️⚪️💜💜💜⚪️⚪️⚪️",
		7: "⚪️⚪️⚪️⚪️💜⚪️⚪️⚪️⚪️"
	}

	# Отрисовываем сердце
	for i in range(1, 8):
		field[i] = rainbow_heart_rows[i]

	try:
		frame = "\n".join(field)

		await msg.edit(frame)
		await sleep(.4)

	except FloodWait as fw:
		await sleep(fw.value)

		await msg.edit(frame)
		await sleep(.4)
	###

	# Радужная анимация
	# * 2 - количество полных повторов
	for _ in range(7 * 2):

		first_heart = ""

		for i in range(1, 8):
			if i == 1:
				first_heart = field[i][4]

				field[i] = field[i].replace(
					field[i][4],
					field[i + 1][len(field[i + 1]) // 2 + 1]
				)
			elif i == 6:
				field[i] = field[i].replace(
					field[i][len(field[i]) // 2 + 1],
					field[i + 1][len(field[i + 1]) // 2]
				)
			elif i == 7:
				field[i] = field[i].replace(field[i][len(field[i]) // 2], first_heart)
			else:
				field[i] = field[i].replace(
					field[i][len(field[i]) // 2 + 1],
					field[i + 1][len(field[i + 1]) // 2 + 1]
				)

		try:
			frame = "\n".join(field)

			await msg.edit(frame)
			await sleep(.4)

		except FloodWait as fw:
			await sleep(fw.value)

			await msg.edit(frame)
			await sleep(.4)

	try:
		field = white_fon.copy()
		frame = "\n".join(field)

		await msg.edit(frame)
		await sleep(.4)

	except FloodWait as fw:
		await sleep(fw.value)

		await msg.edit(frame)
		await sleep(.4)

	for _ in range(8):
		del field[len(field) - 1]

		for i in range(len(field)):
			field[i] = field[i][2:]

		try:
			frame = "\n".join(field)

			await msg.edit(frame)
			await sleep(.4)
		except FloodWait as fw:
			await sleep(fw.value)

			await msg.edit(frame)
			await sleep(.4)

	try:
		await msg.edit(text)

	except FloodWait as fw:
		await sleep(fw.value)

		await msg.edit(text)


# /choice cond1;cond2;cond3
@client.on_message(filters.command(commands = "choice", prefixes = "/") & filters.me)
async def choice(client: Client, msg: Message):
	try:
		options = [option for option in msg.text.split(maxsplit = 1)[1].split(";")]
	except IndexError:
		await msg.delete()
		await send_log(msg = msg.text, error_info = "Не указаны варианты выбора")
		return

	text = "♻️ Делаю рандомный выбор из:"

	for option in options:
		text += f"\n • {option}"

	text += "\n\n🕘 Дай мне 7 сек..."

	try:
		await msg.edit(text)

		await sleep(.4)

		for _ in range(7):
			for i in range(-1, -3, -1):
				await msg.edit(text[:i])

				await sleep(.5)

		await msg.edit(f"✅ Результат: {random.choice(options)}")

	except FloodWait as fw:
		await sleep(fw.value)


#### FLOODERS


flooding_targets = {}


# /repeat text=str; amount=int;
@client.on_message(filters.command(commands = "repeat", prefixes = "/") & filters.me)
async def repeat(client: Client, msg: Message):
	# Получатель флуда
	receiver_id = msg.chat.id
	receiver_fullname = await get_name(msg)

	# Исходное сообщение
	msg_list = msg.text.split(maxsplit = 2)

	# Парсинг текста
	text_parsing = re_search(r'(?<=text\=).+?(?=;)', msg.text)
	# Парсинг символа печати
	amount_parsing = re_search(r'(?<=amount\=)\d+?(?=;)', msg.text)
		
	# Обработка парсинга текста
	if text_parsing:
		text = text_parsing[0]
	else:
		await msg.delete()
		await send_log(msg = msg.text, error_info = "Не указан текст для 'repeat'")
		return

	# Обработка парсинга колва повторений
	if amount_parsing:
		try:
			amount = int(amount_parsing[0])
		except ValueError:
			await msg.delete()
			await send_log(msg = msg.text, error_info = "Значение 'amount' должно быть числовым")
			return
	# Value by default
	else:
		amount = 10

	# Удаляем исходное сообщение
	await msg.delete()

	# Если уже запущено на тот же айди, то выкидываем
	if receiver_id in flooding_targets.keys():
		try:
			await send_log(msg.text, f"На '{receiver_fullname}' уже запущен флудер!")
			return

		except FloodWait as fw:
			await sleep(fw.value)
			await send_log(msg.text, f"На '{receiver_fullname}' уже запущен флудер!")
	
	# Добавляем в список айди получателя
	flooding_targets[receiver_id] = receiver_fullname

	# Начинаем флуд
	while amount != 0 and receiver_id in flooding_targets.keys():
		try:
			# Имитация печати сообщения на 1.5 сек
			await client.send_chat_action(receiver_id, ChatAction.TYPING)
			await sleep(1)
			# Отправляем сообщение
			await client.send_message(receiver_id, text)
			
		# Обработка FloodWait
		except FloodWait as fw:
			await sleep(fw.value)

		# Декрементируем количество повторений
		amount -= 1
	
	# Если флудер остановили, то проверим не удалена ли уже запись
	if receiver_id in flooding_targets.keys():
		del flooding_targets[receiver_id]


# /deadinside
# /di
@client.on_message(filters.command(commands = ["deadinside", "di"], prefixes = "/") & filters.me)
async def dead_inside(client: Client, msg: Message):
	# Получатель флуда
	receiver_id = msg.chat.id
	receiver_fullname = await get_name(msg)

	# Исходное сообщение
	msg_list = msg.text.split()

	# Удаляем исходное сообщение
	await msg.delete()
	
	# Если уже запущено на тот же айди, то выкидываем
	if receiver_id in flooding_targets.keys():
		try:
			await send_log(msg.text, f"На '{receiver_fullname}' уже запущен флудер!")
			return

		except FloodWait as fw:
			await sleep(fw.value)

	# Добавляем в список айди получателя
	flooding_targets[receiver_id] = receiver_fullname

	# Начинаем флуд
	num = 1000

	while num != 6 and receiver_id in flooding_targets.keys():
		try:
			# Имитация печати сообщения на 1.5 сек
			await client.send_chat_action(receiver_id, ChatAction.TYPING)
			await sleep(2)
			# Отправляем результат
			await client.send_message(receiver_id, f"{num} - 7 = {num - 7}")
			

		except FloodWait as fw:
			await sleep(fw.value)

		# Декрементируем стартовое значение
		num -= 7

	# Если флудер остановили, то проверим не удалена ли уже запись
	if receiver_id in flooding_targets.keys():
		del flooding_targets[receiver_id]


# /stop_flood
@client.on_message(filters.command(commands = "stop_flood", prefixes = "/") & filters.me)
async def stop_flood(client: Client, msg: Message):
	# Получатель флуда
	receiver_id = msg.chat.id
	receiver_fullname = await get_name(msg)

	# Исходное сообщение
	msg_list = msg.text.split()
	
	# Удаляем исходное сообщение
	await msg.delete()

	if receiver_id not in flooding_targets.keys():
		try:
			await send_log(msg.text, f"На '{receiver_fullname}' не запущен флудер!")
			return

		except FloodWait as fw:
			await sleep(fw.value)

	del flooding_targets[receiver_id]


# /stop_allflood
@client.on_message(filters.command(commands = "stop_allflood", prefixes = "/") & filters.me)
async def stop_all_flood(client: Client, msg: Message):

	# Исходное сообщение
	msg_list = msg.text.split()
	
	# Удаляем исходное сообщение
	await msg.delete()

	if len(flooding_targets) == 0:
		try:
			await send_log(msg.text, f"Ни в одном чате, не запущен флудер!")
			return

		except FloodWait as fw:
			await sleep(fw.value)

	flooding_targets.clear()


# /flood_list
@client.on_message(filters.command(commands = "flood_list", prefixes = "/") & filters.me)
async def flood_list(client: Client, msg: Message):

	# Удаляем исходное сообщение
	await msg.delete()

	result_msg = "♻️ В следующих чатах запущен флудер:\n"

	if len(flooding_targets) == 0:
		try:
			await client.send_message("me", f"☁ Ни в одном чате, не запущен флудер")
			return

		except FloodWait as fw:
			await sleep(fw.value)
	else:

		for name in flooding_targets.values():
			result_msg += f"• {name}\n"

		try:
			await client.send_message("me", result_msg)
			return

		except FloodWait as fw:
			await sleep(fw.value)


### FAKE-MEDIA

is_running = False
target_global = None
handler = None

async def process_voice(client: Client, msg: Message):
	global is_running
	
	if msg.text == "/cancel":
		is_running = False
		client.remove_handler(*handler)
		await msg.edit("↩️ Отменено")
		return

	target = target_global

	# Имитация чтения сообщения
	try:
		await client.read_chat_history(target)
	except PeerIdInvalid:
		await send_log(client, ["", ""], "Некорректный таргет!")
		is_running = False
		client.remove_handler(*handler)
		return

	if msg.voice is None:
		audio = msg.audio
	else:
		audio = msg.voice


	file = await client.download_media(msg, in_memory = True)
	


	# Имитация записи гс
	if audio.duration // 5 == 0:
		pass
	else:
		for i in range(audio.duration // 5):
			await client.send_chat_action(target, ChatAction.RECORD_AUDIO)
			await sleep(5)

	if audio.duration - 5 * (audio.duration // 5) != 0:
		await client.send_chat_action(target, ChatAction.RECORD_AUDIO)
		await sleep(audio.duration - 5 * (audio.duration // 5))

	# Отправка гс
	await client.send_voice(target, file)

	is_running = False
	client.remove_handler(*handler)

	

# /send_voice {target}
@client.on_message(filters.command(commands = "send_voice", prefixes = "/") & filters.me & filters.user("me"))
async def send_voice(client: Client, msg: Message):
	global is_running, target_global, handler

	msg_list = msg.text.split()

	target = msg_list[1]

	if is_running:
		await send_log(client, msg_list, "Запущен другой процесс, связанный с fake_media!")
		return

	is_running = True

	if target.startswith("@"):
		target = target[1:]
	else:
		try:
			target = int(target)
		except ValueError:
			await send_log(client, msg_list, "Таргет не корректен!")
			return

	target_global = target

	handler = client.add_handler(MessageHandler(process_voice, filters.me & (filters.voice | filters.audio | filters.command(commands = "cancel", prefixes = "/")) & filters.user("me") ))
	print("handler добавлен")

	await msg.edit("🎵 Отправь .ogg или .mp3 файл в этот чат:")





async def process_video_note(client: Client, msg: Message):
	global is_running
	
	if msg.text == "/cancel":
		is_running = False
		client.remove_handler(*handler)
		await msg.edit("↩️ Отменено")
		return

	target = target_global

	# Имитация чтения сообщения
	try:
		await client.read_chat_history(target)
	except PeerIdInvalid:
		await send_log(client, ["", ""], "Некорректный таргет!")
		is_running = False
		client.remove_handler(*handler)
		return
	except UsernameNotOccupied:
		await send_log(client, ["", ""], "Некорректный таргет!")
		is_running = False
		client.remove_handler(*handler)
		return
		

	if msg.video_note is None:
		video = msg.video

		if video.width != 384 or video.height != 384:
			await msg.edit("‼️ Разрешение видео должно быть 384x384 ‼️")
			is_running = False
			client.remove_handler(*handler)
			return
	else:
		video = msg.video_note


	file = await client.download_media(msg, in_memory = True)
	

	# Имитация записи кружка
	if video.duration // 5 == 0:
		pass
	else:
		for i in range(video.duration // 5):
			await client.send_chat_action(target, ChatAction.RECORD_VIDEO_NOTE)
			await sleep(5)

	if video.duration - 5 * (video.duration // 5) != 0:
		await client.send_chat_action(target, ChatAction.RECORD_VIDEO_NOTE)
		await sleep(video.duration - 5 * (video.duration // 5))

	# Отправка кружка
	await client.send_video_note(target, file)

	is_running = False
	client.remove_handler(*handler)

	

# /send_circle {target}
@client.on_message(filters.command(commands = "send_circle", prefixes = "/") & filters.me & filters.user("me"))
async def send_video_note(client: Client, msg: Message):
	global is_running, target_global, handler

	msg_list = msg.text.split()

	target = msg_list[1]

	if is_running:
		await send_log(client, msg_list, "Запущен другой процесс, связанный с fake_media!")
		return

	is_running = True

	if target.startswith("@"):
		target = target[1:]
	else:
		try:
			target = int(target)
		except ValueError:
			await send_log(client, msg_list, "Таргет не корректен!")
			return

	target_global = target

	handler = client.add_handler(MessageHandler(process_video_note, filters.me & (filters.video_note | filters.video | filters.command(commands = "cancel", prefixes = "/")) & filters.user("me") ))

	await msg.edit("🎦 Отправь .mp4 файл с разрешением (384x384) в этот чат:")

# Получение id пользователя
@client.on_message(filters.command(commands = "id", prefixes = "/") & filters.me)
async def get_id(client: Client, msg: Message):
	await client.send_message("me", f"👨🏻‍🎓 {await get_name(msg)}\n ∟ ID: <code>{msg.chat.id}</code>", parse_mode = ParseMode.HTML)
	await msg.delete()


client.run()