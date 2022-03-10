from requests import get
from re import findall
from rubika import Bot
import time
from colorama import Fore,init
from pyfiglet import Figlet

#created By Mamad BELECTRON

print(Fore.GREEN+ "\n L o a d i n g . . . ")
time.sleep(2)
print("")

print ("__________")
time.sleep(0.7)
print ("#_________")
time.sleep(0.6)
print ("##________")
time.sleep(0.5)
print ("###_______")
time.sleep(0.4)
print ("####______")
time.sleep(0.3)
print ("#####_____")
time.sleep(0.2)
print ("######____")
time.sleep(0.1)
print ("#######___")
time.sleep(0.5)
print ("########__")
time.sleep(0.1)
print ("#########_")
time.sleep(0.5)
print ("##########")
print ("")

print(Fore.GREEN+ "\n version 2.0.0")
print("")

print(Fore.YELLOW+"\n Please subscribe to the channel to receive updates :")
print("")

print(Fore.BLUE+"\n Rubika --> @Belectron_bot")
print("")

Sa=Figlet(font="slant")
print(Sa.renderText("BELECTRON"))
print("")

bot = Bot(input("Please Enter Your Auth :"))
target=input("Please Enter Your Guid (Group) :")

print(Fore.BLUE+"\n The Robot Was Successfully Activated !")

def hasAds(msg):
	links = list(map(lambda ID: ID.strip()[1:],findall("@[\w|_|\d]+", msg))) + list(map(lambda link:link.split("/")[-1],findall("rubika\.ir/\w+",msg)))
	joincORjoing = "joing" in msg or "joinc" in msg

	if joincORjoing: return joincORjoing
	else:
		for link in links:
			try:
				Type = bot.getInfoByUsername(link)["data"]["chat"]["abs_object"]["type"]
				if Type == "Channel":
					return True
			except KeyError: return False
			
answered = [Bot.getGroupAdmins]
retries = {}
sleeped = False
delmess = ["دولی","کصکش","کون","کص","کیر" ,"خر","کستی","دول","گو","کس","کسکش","کوبص","کون","کص","کصخل","ننه جنده","کونی","کیری","کیرم"]
plus= True

while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]
		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue
		
		open("id.db","w").write(str(messages[-1].get("message_id")))

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if msg.get("text") == "/bot" and msg.get("author_object_guid") in admins :
						bot.sendMessage(target, "📍 The robot is active ", message_id=msg.get("message_id"))
                    #elif msg.get("text") == "@" :
                 #       bot.deleteMessages(target)
					elif msg.get("text").startswith("/add") :
						bot.invite(target, [bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]])
						bot.sendMessage(target, "➕ User added to group", message_id=msg.get("message_id"))

					elif msg.get("text") == "/panel":
						bot.sendMessage(target, "❮ List of robot commands ❯ :\n✅ /start : فعالسازی ربات\n❎ /stop : غیر فعالسازی ربات\n🤖 /bot : وضعیت ربات\n⏳ /time : ساعت\n📆 /date : تاریخ\n♻️ /del : حذف یک پیام\n🔒 /lock : قفل گروه\n🔓 /unlock : باز کردن قفل گروه\n⛔️ /ban : حذف کاربر\n📨 /send : ارسال پیام ناشناس\n🎶 /add : افزودن کاربر به گروه\n🗃 /panel : لیست دستورات ربات\n🔖 /user : اطلاعات کاربر\n📟 /cal : ماشین حساب\n📝 /font : ارسال فونت\n🌐 /ping : گرفتن پینگ سایت\n🔤 /tran : مترجم انگلیسی\n💣 /bomber : اسپم پیامک\n ─┅━━━━━━━┅─ \n🔮 سرگرمی ها :\n✢ با ارسال کلمه جوک ربات برای شما یک جوک ارسال میکند .\n✢ با ارسال کلمه دانستنی ربات برای شما یک دانستنی ارسال میکند .\n ✢ با ارسال کلمه فال ربات برای شما یک فال ارسال میکند .\n✢ با ارسال کلمه داستان ربات برای شما یک داستان ارسال میکند ‌.\n✢ با ارسال کلمه هواشناسی ... ربات آب و هوای اون منطقه رو ارسال میکند .\n✢ با ارسال کلمه اخبار ربات اخبار دقیق همون روز رو ارسال میکند .\n✢ با ارسال کلمه بیوگرافی ربات یک بیوگرافی به طور تصادفی ارسال میکند .\n✢ با ارسال کلمه ذکر ربات ذکر روز رو ارسال میکند.\n✢ با ارسال کلمه حدیث ربات یک حدیث ارسال میکند.\n─┅━━━━━━━┅─ \n🔸ChanneL : rubika.ir/belectron_bot")
				
					elif msg.get("text").startswith("/cal"):
						msd = msg.get("text")
						if plus == True:
							try:
								call = [msd.split(" ")[1], msd.split(" ")[2], msd.split(" ")[3]]
								if call[1] == "+":
									am = float(call[0]) + float(call[2])
									bot.sendMessage(target, "حاصل -->\n"+"".join(str(am)), message_id=msg.get("message_id"))
									plus = False
							
								elif call[1] == "-":
									am = float(call[0]) - float(call[2])
									bot.sendMessage(target, "حاصل -->\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "*":
									am = float(call[0]) * float(call[2])
									bot.sendMessage(target, "حاصل -->\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "/":
									am = float(call[0]) / float(call[2])
									bot.sendMessage(target, "حاصل -->\n"+"".join(str(am)), message_id=msg.get("message_id"))
							except IndexError:
								bot.sendMessage(target, "⊖ دستور صحیح نمیباشد !\n  \n✠ به این فرم دستور را تایپ کنید :\nمثال ⇜ 1 * 2" ,message_id=msg.get("message_id"))
						plus= True
					elif msg.get("text").startswith("/send") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "شما یک پیام ناشناس دارید:\n"+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "Massage was sended !", message_id=msg.get("message_id"))
						 		
					elif msg.get("text").startswith("@"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("rubika.ir"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("+98"):
						bot.sendMessage(target, "پنل بمبر برای شما فعال نمیباشد لطفا اشتراک خریداری کنید تا بتوانید از این دستور استفاده کنید !", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("مدیر"):
						bot.sendMessage(target, "مدییر خوابه !", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("چه خبر"):
						bot.sendMessage(target, "سلامتیت عشقم", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("هعب"):
						bot.sendMessage(target, "هیس چسناله نکن", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("کیر"):
						bot.sendMessage(target, "فحاشی نکن وگرنه همین الان سیکتو از گپ میزنم", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("قرم"):
						bot.sendMessage(target, "بتخمم که قهری", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("قهرم"):
						bot.sendMessage(target, "نه بیا بقلم عشقم قر نکنننننن", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("ممد"):
						bot.sendMessage(target, "پدر منو چیکار داری؟", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("محمد"):
						bot.sendMessage(target, "پدرته سجده بزن جلوش", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("علی"):
						bot.sendMessage(target, "عه علیههههههههههههه", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("میرم"):
						bot.sendMessage(target, "برو به چپم که میری", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("اها"):
						bot.sendMessage(target, "اره", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("هایاه"):
						bot.sendMessage(target, "داری کون میدی عشقم؟", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("هعی"):
						bot.sendMessage(target, "هعی دا هعیییییییی", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("کوس"):
						bot.sendMessage(target, "میتانم کوسیتان را بیقولم ؟", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("خبی"):
						bot.sendMessage(target, "عین آدم چت کن خبی چیه؟", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("من"):
						bot.sendMessage(target, "عن", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("دلام"):
						bot.sendMessage(target, "دلام عجقم قوبی؟", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("لواط"):
						bot.sendMessage(target, "لواط مایه حیات", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("قوبی"):
						bot.sendMessage(target, "نه حالم کیریه همشم تقصیر توعههه", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("چرا"):
						bot.sendMessage(target, "چون زیرا", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("https"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
											
					elif msg.get("text").startswith("ربات زن داری"):
						bot.sendMessage(target, " اره خوبشم دارم کل روبیک برام میماله", message_id=msg["message_id"])       
						
					elif msg.get("text").startswith("ممد کیه"):
						bot.sendMessage(target, "تو فکر کن زن ایلیه ولی به کسی نگیا", message_id=msg["message_id"])
								
					elif msg.get("text").startswith("شعر بخون"):
						bot.sendMessage(target, "سلام ای ناله ی بارون سلام ای کس های گریون سلام کیرمو کردم توش هنوزم ابم نیومد سلام ای کاندوم خوبم سلام ای همدم خپبم سلام شب های تاخیری هنوزم دوسشون دارم", message_id=msg["message_id"])
						
					elif msg.get("text") == "بات":
						bot.sendMessage(target, "جونم عشقممم" or "بله" or "بنال", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "تو":
						bot.sendMessage(target, "سرت تو گوه", message_id=msg.get("message_id"))
								
					elif msg.get("text") == "هی":
						bot.sendMessage(target, "ناله نکن اینجا هیئت نیست", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("خارت گاییدست"):
						bot.sendMessage(target, "اره مثل ننه تو", message_id=msg["message_id"])
						
					elif msg.get("text") == "کیرمی":
						bot.sendMessage(target, "کیر بخور باو تو کیرت کجا بود؟", message_id=msg.get("message_id"))
								
					elif msg.get("text") == "ندارم":
						bot.sendMessage(target, "بکیرم ک نداری😂", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("تایم"):
						bot.sendMessage(target, "تو کست", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("آموزش ساخت ربات"):
						bot.sendMessage(target, "سید اگه میخوای توعم ربات داشته باشی بیا داخل چنل زیر و ربات خودتو بساز :\nhttps://rubika.ir/joinc/BDJGHCCB0JWSIFSUOJJSRFNAMZLSNYRV", message_id=msg["message_id"])
						
					elif msg.get("text") == "کونده":
						bot.sendMessage(target,
				  "کونده هفت جدت", message_id=msg.get("message_id"))
									
					elif msg.get("text").startswith("باشه"):
						bot.sendMessage(target, "وا کن تا جاشه ", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("خدایی رباتی"):
						bot.sendMessage(target, "نه احمق زاده فرا انسانم با دستای جقیم میخام برات بساکم", message_id=msg["message_id"])
						
					elif msg.get("text") == "کیرم بخور":
						bot.sendMessage(target, "به دودولت میگی کیر؟", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "کیرمو بخور":
						bot.sendMessage(target, "من فقط کسمادرتو میخورم", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "کس":
						bot.sendMessage(target, "ای جان کس شق کردم سید", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "🙁":
						bot.sendMessage(target, "خارکسه بغض نکن بیا لواط کنیم حالت خوب میشه", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "بکیرم":
						bot.sendMessage(target, "ننت به زیرم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بی حیاس":
						bot.sendMessage(target, "به خواهرت رفتم😐", message_id=msg.get("message_id"))	
						
					elif msg.get("text") == "خواهر ندارم":
						bot.sendMessage(target, "بکیرم ک نداری", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "چخبر":
						bot.sendMessage(target, "سلامتیت عشقمممم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بگو ممد":
						bot.sendMessage(target, "ممد", message_id=msg.get("message_id"))		
								
					elif msg.get("text") == "کیر میخوری":
						bot.sendMessage(target, "نه بده خواهرت بخوره جون بگیره😂", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "کسننت":
						bot.sendMessage(target, "کیر آقام دست ننت", message_id=msg.get("message_id"))
								
					elif msg.get("text") == "ربات":
						bot.sendMessage(target, "ربات پدر لپرته من یک فرا انسان هستم", message_id=msg.get("message_id"))
					elif msg.get("text") == "زشته":
						bot.sendMessage(tar.
						get, "زشت پدرته", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "🤣🤣🤣":
						bot.sendMessage(target, "کیر توش باشه بخندی", message_id=msg.get("message_id"))
					elif msg.get("text") == "Fuck":
						bot.sendMessage(target, "تو کست", message_id=msg.get("message_id"))	
						
					elif msg.get("text") == "سلان":
						bot.sendMessage(target, "سلان و کیرخر ", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "تایپرها چه کسانی هستند":
						bot.sendMessage(target, "تایپر ها انسان هایی عقب مانده هستند که با چس مست کردن ادعای بزرگی میکنن ولی در واقعیت جز جیش کردن کار دیگری بلد نیستند این فراد در واقعیت بسیار تو سری خور هستند و به همین دلیل برای خالی کردن عقده هایشان به روبیک پناه می اورند باشد که نسلشان منقرض شود\n@belectron_bot", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ریده":
						bot.sendMessage(target, "اره سید عنم گرفته بود ریدم در خونتون😂😂😂", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "بیا سکسچت":
						bot.sendMessage(target, "اوففففف لخت کن دارم میام", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "مایل به کار های گناه":
						bot.sendMessage(target, "بستگی داره چی باشه لواط و پایم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ایلی":
						bot.sendMessage(target, "ایلی مرد خدا بیامرزه از زندگی بحی  داد حالا چیکارش داشتی اون هیزو", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "زنت کیه":
						bot.sendMessage(target, "لیلی خانومه قانومی کوسیتان را بقولم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "با من ازدواج میکنی":
						bot.sendMessage(target, "اگه بهشتتو بزاری دهنم چرا که نه اوخودا کوستان را بیقولم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ایلیا":
						bot.sendMessage(target, "قر بده بیا", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "حوسلم":
						bot.sendMessage(target, "بیا خودمونو با لواط سرگرم کنیم کیر در کیر لب در لب", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بسیک":
						bot.sendMessage(target, "حله الان میرم تو کست حال میکنم هورااا", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "فاک":
						bot.sendMessage(target, "تو کونت عشقم", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "آفرین سید":
						bot.sendMessage(target, "کیرمی سید", message_id=msg.get("message_id"))
								
					elif msg.get("text") == "کی قهره":
						bot.sendMessage(target, "مونا خانوم .قهر نیست چس کرده نازشو بکش برگرده خاکتوسرت ایلیا"
						 or "عشقم ممده" or "دیگه هیشکیو دوست ندارم", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "بابات کیه":
						bot.sendMessage(target, "حضرت آقا محمد بلکترون 😂😔💜\n@seyed_xxx", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "آفرین":
						bot.sendMessage(target, "میدونم من خدام😂😔💋", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "بلکترون خر":
						bot.sendMessage(target, "چیه حاجی ادم ندیدی", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "کانال":
						bot.sendMessage(target, "🤖 کانال ما :\nhttp://rubika.ir/belectron_bot", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "ممد":
						bot.sendMessage(target, "کیرم تو کسعمت"or "ممد مال منه", message_id=msg.get("message_id"))		
					elif msg.get("text") == "علی":
						bot.sendMessage(target, "کیر تو در ولی", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "سلام":
						bot.sendMessage(target, "salam kharkose", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "کسکش":
						bot.sendMessage(target, "کسخل زاده اینجا فحاشی نکن", message_id=msg.get("message_id"))
								
					elif msg.get("text") == "بلکترون":
						bot.sendMessage(target, "چقد صدام میزنی حاجی خارمو ساییدی", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "/bomber":
						bot.sendMessage(target, "کاربر گرامی لطفا اقدام به خرید اشتراک بکنید سپس میتوانید از این دستور استفاده کنید.\nchannel : @Belectron_bot", message_id=msg.get("message_id"))
								
					elif msg.get("text") == "خوبی عزیزم":
						bot.sendMessage(target, "اوفف به من گفتی عزیزم؟🤤💜", message_id=msg.get("message_id"))
										
					elif msg.get("text") == "خوبی":
						bot.sendMessage(target, "ن حالم خرابه هعی", message_id=msg.get("message_id"))
											
					if  msg.get("text").startswith('/user @'):
						try:
							user_info = bot.getInfoByUsername( msg.get("text")[7:])
							if user_info['data']['exist'] == True:
								if user_info['data']['type'] == 'User':
									bot.sendMessage(target, 'Name User:\n ' + user_info['data']['user']['first_name'] + ' ' + user_info['data']['user']['last_name'] + '\n\nBio User:\n ' + user_info['data']['user']['bio'] + '\n\nGuid:\n ' + user_info['data']['user']['user_guid'] ,  msg.get('message_id'))
									print('sended response')
								else:
									bot.sendMessage(target, "خطا !\nاین یوزرنیم مربوط به یک کانال میباشد." ,  msg.get('message_id'))
									print('sended response')
							else:
								bot.sendMessage(target, "کاربری وجود ندارد ❌" ,  msg.get('message_id'))
								print('sended response')
						except:
							print('server bug6')
							bot.sendMessage(target, "خطا در اجرای دستور مجددا سعی کنید ❌" ,message_id=msg.get("message_id"))
							

					elif msg.get("text") == "/stop" and msg.get("author_object_guid") in admins :
						sleeped = True
						bot.sendMessage(target, "the robot is offline !", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("/ping"):
						
						try:
							responser = get(f"https://api.codebazan.ir/ping/?url={msg.get('text').split()[1]}").text
							bot.sendMessage(target, responser,message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن جقی!", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("ترجمه فارسی"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن جقی!", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("ترجمه انگلیسی"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=fa&to=en&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن جقی!", message_id=msg["message_id"])
			     	   
					elif msg.get("text").startswith("ترجمه عربی"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=fa&to=ar&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن جقی!", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("واژه"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/vajehyab/?text={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن جقی!", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("/font"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن جقی!", message_id=msg["message_id"])
									
					elif msg.get("text").startswith("ذکر"):
						
						try:
							response = get("https://api.codebazan.ir/zekr/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن باو", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("حدیث"):
						
						try:
							response = get("https://api.codebazan.ir/hadis").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "اشتباه وارد کردی دستورو عشقم", message_id=msg["message_id"])
					elif msg.get("text").startswith("اوقات شرعی"):
						
						try:
							response = get("https://api.codebazan.ir/owghat/?city=تهران").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "اشتباه وارد کردی دستورو عشقم", message_id=msg["message_id"])
														
					elif msg["text"].startswith("هواشناسی"):
						response = get(f"https://api.codebazan.ir/weather/?city={msg['text'].split()[1]}").json()
						#print("\n".join(list(response["result"].values())))
						try:
							bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:20])).text
							bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
						except:
								bot.sendMessage(target, "متاسفانه نتیجه‌ای موجود نبود!", message_id=msg["message_id"])
										
					elif msg.get("text").startswith("قیمت خودرو"):
						
						try:
							response = get("http://api.codebazan.ir/car-price/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "احمق دستور رو درست وارد کن!!!", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("جوک"):
						
						try:
							response = get("https://api.codebazan.ir/jok/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "احمق دستور رو درست وارد کن!!!", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("ساعت"):
						
						try:
							response = get("http://api.codebazan.ir/time-date/?td=all").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "احمق دستور رو درست وارد کن!!!", message_id=msg["message_id"])
									
					elif msg.get("text").startswith("دانستنی"):
						
						try:
							response = get("https://api.codebazan.ir/danestani/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن باو", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("فال"):
						
						try:
							response = get("https://api.codebazan.ir/fal").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن باو", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("بیوگرافی"):
						
						try:
							response = get("https://api.codebazan.ir/bio/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن باو", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("داستان"):
						
						try:
							response = get("https://api.codebazan.ir/dastan/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "خنگ زاده دستور رو درست وارد کن", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("اخبار"):
						
						try:
							response = get("https://api.codebazan.ir/khabar/?kind=iran").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "اشتباه وارد کردی دستورو عشقم", message_id=msg["message_id"])
													
					elif msg.get("text") == "/time":
						bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))

					elif msg.get("text") == "/date":
						bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))

					elif msg.get("text") == "/del" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "پیام پاک شد ✅", message_id=msg.get("message_id"))
						
					#				elif msg.get("text").split(" ")[0] in  delmess:
	#				bot.deleteMessages(target, [msg.get("message_id")])
	#				bot.sendMessage(target, "یک پیام مستهجن پاک شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "/lock" and msg.get("author_object_guid") in admins :
						print(bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","AddMember"]).text)
						bot.sendMessage(target, "گپ قفل شد ✅", message_id=msg.get("message_id"))						
					elif msg.get("text") == "/unlock" and msg.get("author_object_guid") in admins :
						bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","SendMessages","AddMember"])
						bot.sendMessage(target, "گپ باز شد ✅", message_id=msg.get("message_id"))
							
					elif msg.get("text").startswith("/ban") and msg.get("author_object_guid") in admins :
						try:
							guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							if not guid in admins :
								bot.banGroupMember(target, guid)
								bot.sendMessage(target, f" ✅ کاربر حذف شد", message_id=msg.get("message_id"))
							else :
								bot.sendMessage(target, f" کاربر حذف نشد❌", message_id=msg.get("message_id"))
								
						except IndexError:
							a = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
							if a in admins:
								bot.sendMessage(target, f" کاربر حذف نشد ❌ ", message_id=msg.get("message_id"))
							else:
								bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								bot.sendMessage(target, f" کاربر حذف شد ✅", message_id=msg.get("message_id"))

				else:
					if msg.get("text") == "/start" and msg.get("author_object_guid") in admins :
						sleeped = False
						bot.sendMessage(target, "the robot is online !", message_id=msg.get("message_id"))
			
			elif msg.get("text") == "/pin" and msg.get("author_object_guid") in admins :
				bot.pin(target, msg["reply_to_message_id"])
				
			elif msg.get("text") == "/unpin" and msg.get("author_object_guid") in admins :
				bot.unpin(target, msg["reply_to_message_id"])
				bot.sendMessage(target, "The message was successfully removed from the pin !", message_id=msg.get("message_id"))
			
			elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
				name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
				data = msg['event_data']
				if data["type"]=="RemoveGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"تق خارکسه {user}", message_id=msg["message_id"])
				
				elif data["type"]=="AddedGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"Hey {user} 💜\nWelcome to {name} 🛸\n channel : @Belectron_bot 🗿", message_id=msg["message_id"])
				
				elif data["type"]=="LeaveGroup":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"کون ‌لقت سید", message_id=msg["message_id"])
					
				elif data["type"]=="JoinedGroupByLink":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"Hey {user} 💜\nWelcome to {name} 🛸\nChannel : @Belectron_bot 🗿", message_id=msg["message_id"])

			answered.append(msg.get("message_id"))

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue		
