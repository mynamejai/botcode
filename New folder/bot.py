import telebot
import random
import time

# Initialize the Telegram Bot
bot = telebot.TeleBot("6990869019:AAFJfr-xIp9e4baRCiANu9ORkBDWeRjNIsY")

# Command handler for /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    # Send countdown animation
    msg = bot.send_message(chat_id, "3")
    time.sleep(1)
    bot.edit_message_text(chat_id=chat_id, message_id=msg.message_id, text="2")
    time.sleep(1)
    bot.edit_message_text(chat_id=chat_id, message_id=msg.message_id, text="1")
    time.sleep(1)
    bot.edit_message_text(chat_id=chat_id, message_id=msg.message_id, text="Insult bot activated! Type /insult to get insulted.")

# Command handler for /insult
@bot.message_handler(commands=['insult'])
def send_insult(message):
    insults = [
        "You're as useless as the 'g' in lasagna.",
    "I'd agree with you, but then we'd both be wrong.",
    "Somewhere out there is a tree tirelessly producing oxygen for you. You owe it an apology.",
    "You smell like a yeast infection.",
    "You're as useless as a barber working at the make a wish foundation.",
    "Your shirt is green but nothing else matches.",
    "1,2, buckle my shoe, 3,4, your mom's a whore.",
    "Here's to a man who never unduly felt the pang of 'imposter syndrome'.",
    "All your friends are fake.",
    "Amy Schumer is a better comedian than you.",
    "An aqueduct is a very large structure used to transport a large amount of fluid from one place to another.",
    "And what are you supposed to be? A disappointment?",
    "Anyone can hide ugliness, but you can't hide stupidity like yours.",
    "Anyone willing to fuck you is just too lazy to masturbate.",
    "Are you a clitoris? Because you are goddamn sensitive.",
    "Are you a lays bag? Because your 40% air.",
    "Are you the monster from bird box?",
    "Behold, the field in which I grow my fucks. Lay thine eyes up on it, for it is barren.",
    "Believe in yourself all you want.",
    "Bitch please, your vagina has more users than Facebook.",
    "BITCH YOU ARE A SLAPPER.",
    "Bitch, your ears are so fucking big that a swift wind will dumbo your ass all the way to florida.",
    "Body pillow sweat smelling weeb.",
    "Can you stop talking like an uneducated Instagram human defect and start speaking like a normal person.",
    "Cream pied asshole piece of shit.",
    "Cremation is your only chance of having a smoking hot body.",
    "Ctrl + Z yourself.",
    "Cum guzzling thunder slut.",
    "Cum soaked urinal cake.",
    "Dad called me stupid for not doing HW.",
    "Damn you're uglier than me.",
    "De-count-da-money fuck face.",
    "Dick cannibal.",
    "Did a thousand deaths, you infected goat rectum!",
    "Did it hurt? When you fell from someone's butt into the toilet water, you piece of shit.",
    "Did Walmart have a sale on chromosomes when you were born?",
    "Did you eat a whole bowl of Dumb for breakfast and go back for seconds?",
    "Did you fall from heaven?",
    "Did you know scientists have finally found a way to achieve a temperature of absolute zero in a controlled setting?",
    "Did you take classes on how to be a moron or are you just naturally gifted?",
    "Do the world a favour and climb back into your mum you degenerate inbred cretin.",
    "Does your ass jealous with the amount of shits that comes from your mouth?",
    "Does your asshole get jealous of all the shit that comes out of your mouth?",
    "Don't break your neck sucking your own cock.",
    "Don't play hard to get when you are hard to want.",
    "Douche things to refer to people as.",
    "DoucheBo Baggins.",
    "Duct tape can't fix stupid, but it sure can muffle the sound.",
    "Eat a bowl of fuck.",
    "Eat my fuck, bitch.",
    "Elephants remember everything that’s why your mom never forgets.",
    "English, you stupid bitch. I don't speak hoppity boppity.",
    "Even Females in your family have a bigger penis than yours.",
    "Even if you dont want to have kids, you regret not being able to regret having kids.",
    "Even Leni Loud could do better in an IQ test than you!",
    "Ever since your birth, the rate of suicides increased exponentially.",
    "Ever wonder how life would have been if you had received enough oxygen at birth?",
    "Every yo mama joke had been done thousands of different times by thousands of different people.",
    "Everyone has the right to be ugly.",
    "Everyone on this sub can go fuck themselves.",
    "Everyone who loves you is wrong.",
    "Everyone's heritage is shaped like a tree while yours is a pole.",
    "Everytime you open up your mouth my cock gets homesick.",
    "For my Halloween costume this year I am going to wear two bags over my head and go as the only person willing to fuck you.",
    "Frankly, I don't have the time or the crayons to explain it to you.",
    "Fuck you you fucking yellow stupid b carotene lookin staple food cunt face plant.",
    "Get a colonoscopy for that attitude.",
    "Get back to eating your uncrustables kiddo.",
    "Giidy Goose.",
    "Go apologize to your mother for not being a stillborn.",
    "Go deepthroat a tailpipe with the engine on.",
    "Go die in a hole filled with my shit.",
    "Go eat you're mama's ass milk.",
    "Go fall down some stairs, you uncoordinated schmuck.",
    "Go find your place in a dumpster.",
    "Go fuck a tornado.",
    "Go fuck off with your elongated urethra that you call a penis!",
    "Go hop in a microwave you uncooked grit bag.",
    "Go jack off with sand paper you ass spelunker.",
    "Go put a condom on your head. If you're going to act like a dick, you might as well dress like one too.",
    "Go radiate your liver.",
    "Go snort a radish.",
    "Go stand on a reef you duck toaster -my 8 year old brother.",
    "Go swap your balls/ovaries with your tonsils and go hang yourself.",
    "Go up to a plant and apologise for wasting the oxygen it provides!",
    "God wasted a perfectly good asshole when he jamed teeth in your mouth.",
    "Going to go fuck your mom, but line was too long.",
    "Got her head so far up her ass she eats breakfast twice.",
    "Great job! For Christmas I'll get you half a chair so you can sit on it with your half ass.",
    "Have you always been this stupid or do you practice in your free time?",
    "Having more chromosomes is a bad thing?",
    "Here's a potted plant to replace the air you wasted.",
    "Hey bitch if I had a choice between sex with you and $5 I'd take the $5 and buy you 5 times.",
    "Hey fuckwit if I wanted to listen to a rambling cokeheaded steaming pile of trash talk about bullshit that doesn't matter I would ask your wrinkled foreskin of a granddad about his opinions.",
    "Hey how about you go fuck yourself with a broken beer bottle you sly sack of human shit.",
    "Hey man, you remind me of an injection.",
    "Hey that’s funny it’s what your mum said when you were born.",
    "Hey train wreck, this isn't your station.",
    "Hey, are you sausage?",
    "Hi mom why did you make me a son of a bitch.",
    "How about you go home, draw a nice warm bath, pour a drink and GO FUCK YOURSELF!",
    "How about you stick some candle in your ass and go pretend you are the street lamp.",
    "How about you stick some flowers in your ass and go pretend to be vase?",
    "How do I know that's a shitty idea? Because you just pulled it out of your ass!",
    "How long do you have to live?",
    "Huh? Oh sorry I wasn’t listening. I was trying to figure out how many drugs your mom was on when she was pregnant with you.",
    "Humans are deuterostomes.",
    "I am blessed to not know you because god damn you are a massive prick.",
    "I appreciate that you're trying to be funny.",
    "I asked siri for the cheapest whore in town.",
    "I ate your mom out last night, but it was salty. Probably because that's where you came out.",
    "I bet it takes you an hour and a half to watch an episode of 60 Minutes.",
    "I bet you drink milk with a fork.",
    "I bet you had to fight your way out of your mother's cunt because the doctors kept trying to shove you back in."
    ]
    insult = random.choice(insults)
    bot.reply_to(message, insult)

# Command handler for any other commands
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "I'm an insult bot. Type /insult to get insulted.")

# Start the bot
bot.polling()
