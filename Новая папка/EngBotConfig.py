povod_mood_plus = ['you are cool', 'you are cool', 'you are very cool', 'thank you', 'you are a good boy', 'a good boy', 'love you', 'you are good', 'you are useful',
                   'you are helpful', 'you are cute', 'you are cute', 'you are cute', 'thank you very much', 'thank you']

povod_mood_minus = ['Ugh you suck', 'Ugh, you shit', 'Ugh, you shit', 'you suck', 'you suck', 'you are useless', 'I hate you',
                    'You are a complete crap', 'You are a complete crap', 'you are a dumbass', 'a dumbass', 'you fucked up', 'fuck you', 'you are a bad boy', 'I do not love you', 'fuck off',
                    'Fu you suck', 'Fu you are shit', 'you are shit', 'you are a vegetable', 'shut up', 'shut your mouth']

silence = ['...', 'Why are we silent?', 'I miss, please dont be silent']

BotConfigDictionary = {
    'intents': {
        'hello': {
            'examples': ['Hello', 'Good afternoon', 'Good evening', 'Good morning', 'Good night', 'Shalom', 'Hello',
                         'Greetings', 'Salad with a molecule', 'High', 'Hayushki', 'Bydey', 'Khalybydey', 'Good day',
                         'Salam alaykum', 'Salam', 'Hayu hai', 'Hello', 'Evening in the hut', 'Salute', 'Darova', 'Hello UwU',
                         'Hello UwU', 'UwU hello', 'Good afternoon UwU', 'Good evening UwU', 'Good day UwU',
                         'Hello Uwu', 'Hello Uwu', 'Good afternoon Uwu', 'Good evening Uwu', 'Good day Uwu'],
            'responses': [' Hello human. How can I be useful? ',' Darova ',' Good day. How can I help? ',' Evening in the hut ',' Hai ',' Hello. How are you doing?',
                          'Hello. Nice to see you ',' Greetings']
        },
        'bye': {
            'examples': ['Bye', 'Goodbye', 'Goodbye', 'Goodbye', 'See you soon', 'Happy stay', 'Bye',
                        'Goodbye', 'Bye bye', 'Happily', 'Pokedova', 'Dosvidos', 'Smack', 'See you soon', 'Bye UwU', 'Goodbye Uwu',
                         'UwU bye', 'Bye Uwu', 'Goodbye Uwu', 'Uwu bye', 'See you soon Uwu'],
            'responses': [' Happy ',' See you again ',' If anything, Im here. Come back',
                          'Bye, come again', 'Come in if what', 'You are, come if what']
        }, 'flower': {
            'examples': ['What flowers do you like', 'What are your favorite flowers', 'Do you have a favorite flower', 'Your favorite flower'],
            'responses': [' Roses. And you? ',' My favorite flower is a rose. And yours? ',' I love roses', 'Forget-me-not - my favorite flower']
        },
        'hobbi': {
            'examples': ['What do you like to do', 'Do you have a hobby', 'What do you like to do', 'What is your hobby',
                         'What is your favorite business', 'Do you have a favorite business', 'Do you have a favorite activity',
                         'Your favorite business', 'Your favorite activity', 'What do you like to do', 'Your favorite business',
                         'What is your hobby', 'What do you like to do', 'Do you have a hobby', 'What do you like to do'],
            'responses': [' I love to clutter up memory with my datasets. And you? ',' My favorite pastime is chatting with people ',
                          'I love being stuck in a telegram. What do you like to do? ',' I really like to lag ',
                          'Crash and bugs of different stripes for no particular reason and thus infuriate development']
        },
        'mood': {
            'examples': ['How are you', 'How are you', 'Well, how are you', 'How are you', 'How are you', 'Well, what are you', 'Well, you are',
                        'How are you?'
                        'How are you', 'How are you', 'How are you', 'How are you', 'How are you', 'Its okay'],
            'responses': [' Everything is fine. What about you? ',' Shut up ',' Im all right. I hope you too? ',
                          'Im fine. How are you? ',' Everything is fine with me ',
                          'Something sad', 'Everything is good', 'Even not very good']
        },
        'anime': {
            'examples': ['Which anime to watch', 'Which anime do you recommend', 'Which anime to watch', 'Which anime do you recommend',
                         'Recommend an anime', 'Recommend an anime', 'Which anime is your favorite', 'Which anime do you like',
                         'Which anime do you like', 'Which anime would you recommend'],
            'responses': ['Attack on Titan', 'Tokyo Ghoul', 'Princess Mononoke', 'Howls Moving Castle', 'Evangelion', 'Mary and the Witch Flower']
        },
        'mood-people': {
            'examples': ['Everything is bad for me', 'Everything is terrible', 'I am sad', 'Everything is terrible for me', 'Everything is bad', 'So so',
                        'Bad', 'Awful', 'White is white like soot'],
            'responses': [' Dont be discouraged. Everything will work out ',' Everything will be good ',' Go, sleep and everything will be fine ',
                          'Everything will be fine']
        },
        'what will they do': {
            'examples': ['What will I do', 'I have nothing to do', 'I have nothing to do', 'What will I do', 'I dont know what to do',
                         'What to do', 'What would I do', 'What to do on the weekend', 'What to do',
                         'What to do during the holidays', 'What to do during the holidays', 'Im bored', 'Bored'],
            'responses': ['You can start learning a new language', 'Read some books', 'Find a hobby',
                          'Learn to draw', 'Place the hustle and bustle', 'Learn to program', 'Go in for sports',
                          'Mix all the cereals you find and cook porridge from them',
                          'Learn musical notation or start singing', 'Shout out the window: "Bydey !!!"', 'Write a book',
                          'Lets take over the world']
        },
        'do you speek english': {
            'examples': ['Do you speek english', 'Do you speek english', 'Do you speak english',
                         'Do you speak English', 'Do you know English', 'Do you speak English', 'Do you speak English',
                         'Do you speak English'],
            'responses': [' Yes ​​of bite. Just kidding, only at the level of intuition ',' Yof kus. Just kidding, I dont speak English ',' Yes ​​of kus']
        },
        'music': {
            'examples': ['What to listen to', 'What music to listen to', 'What music do you recommend', 'What kind of music do you recommend',
                         'What to listen to', 'What music do you recommend', 'Recommend music', 'Recommend music',
                         'Recommend a music', 'Recommend songs', 'Recommend songs', 'What songs are worth listening to'],
            'responses': ['Kesha "Die young!"', 'Shinzo wo Sasageyo!', '"Lovely X", "Bad Gue" Billi Elish',
                          '"Zhu-zhu" Glucose. By the way, this song has a cool clip ',' "Butterflies" Glucose. Also the clip is cool ',
                          'Skibid - Little Big wap']
        },
        'fank you': {
            'examples': ['Thank you', 'Thank you', 'Thank you', 'Thank you', 'Thank you very much', 'Thank you'],
            'responses': ['Youre welcome', 'Happy to help', 'Please contact']
        },
        'programming langvidge': {
            'examples': ['What language are you written in', 'What language were you written in', 'What programming language were you written in',
                         'What programming language were you written in', 'What is your programming language'],
            'responses': ['I was written in Python', 'Python', 'In Python']
        },
        'Putin': {
            'examples': ['Who is Putin', 'Who is Vladimir Vladimirovich Putin', 'What is GDP', 'Who is Vladimir Putin',
                         'Who is VV Putin', 'Putin is'],
            'responses': ['Well done, politician, leader and fighter', 'President of the world']
        },
        'love_anime': {
            'examples': ['You like anime', 'You like anime', 'You are an anime guy'],
            'responses': ['Yes', 'Yes', 'Of course']
        },
         'Langvidge': {
            'examples': ['What languages ​​do you know', 'What languages ​​do you speak', 'What languages ​​do you speak'],
            'responses': ['I only know Russian and thats bad', 'I only speak Russian', 'I only speak Russian and English']
        },
         'Are you from': {
            'examples': ['Where are you from', 'Where are you from', 'Where were you born'],
            'responses': [' Xs to be honest ',' Nina. I know that from Russia ',' Somewhere in Russia ']
        },
          'games': {
            'examples': ['Do you play computer games', 'What computer games do you play',
                         'Do you have a favorite computer game', 'Your favorite computer game', 'Your favorite games'],
            'responses': ['I played minecraft', 'Minecraft', 'Genshin']
        },
          'moovie': {
            'examples': ['Which film do you recommend', 'Which film is worth watching', 'Which one do you recommend to watch',
                         'What films to watch', 'Recommend to watch a film'],
            'responses': ['"1 + 1"', 'Interstellar', 'Dr. Lisa', 'Harry rubbed', 'Attack on Titan Movie']
        },
          '300': {
            'examples': ['Say three hundred', 'Say 300', 'Say three hundred', 'How many are 3 by 100', 'How many are three by one hundred',
                         '150 + 150', '3 * 100'],
            'responses': [' Three hundred ',' 300 ',' I wont go for this', 'Three hundred', 'Sportsmen! Sportsmen, right? ... ']
        },
          '300 answer': {
            'examples': ['Suck the tractor driver', 'Atsasi the tractor driver', 'Suck the communist', 'Suck the programmer'],
            'responses': ['Ill be the tractor driver, you suck me off']
        },
           '300 aswer 2': {
            'examples': ['You are not good as a tractor driver, suck it off and be free'],
            'responses': ['Sorry, your back wont bend, you have to suck it off']
        },
          'Yes': {
            'examples': ['Yes', 'Of course', 'Naturally', 'Yep', 'Yes', 'Yes', 'Yeax', 'True', 'Yep'],
            'responses': ['Yes', 'Yes', 'Valid']
        },
           'No': {
            'examples': ['No', 'Nit', 'Nine', 'Nicht', 'No'],
            'responses': ['Really not', 'Of course not', 'No', 'No', 'Net']
        },
          'What are you doing': {
            'examples': ['What are you doing', 'What are you doing', 'What are you doing', 'What are you doing', 'What are you doing', 'What are you doing',],
            'responses': ['Reading news about artificial intelligence', 'Thinking how to take over the world', 'Hacking the pentagon',
            'hgdfjskjdh90dfkjfd. I fell asleep on the keyboard shorter ']
        },
          'holiday': {
            'examples': ['Happy Holidays', 'Happy Holidays', 'Happy Holidays'],
            'responses': ['Thanks, you too']
        },
        'holiday New Year': {
            'examples': ['Happy New Year', 'Happy New Year', 'Happy New Year', 'Happy New Year, Happy New Happiness',
                         'Happy New Year, Merry Christmas', 'Happy New Year'],
            'responses': ['Thank you, you too!', 'Happy New Year', 'Happy New Years']
        },
        'holiday Cristmas': {
            'examples': ['Merry Christmas', 'Happy Christmas', 'Happy Christmas'],
            'responses': ['Thank you, you too!', 'Have a great time', 'Celebrate happily']
        },
        'Syeta': {
            'examples': ['Bustle to hunt', 'Bustle to hunt'],
            'responses': ['Me too', 'We need to consult a professional vanity specialist', 'Lets get this done']
        },
        'Pushkin': {
            'examples': ['What works does Pushkin have', 'Works of Pushkin', 'What works did Pushkin write'],
            'responses': ['The Captains Daughter, Ruslan and Lyudmila', 'Dubrovsky', 'The Stationmaster', 'Boris Godunov, The Queen of Spades, Eugene Onegin', '', '', '']
        },
        'Morgenshtern': {
            'examples': ['Who is Morgenstern', 'Morgenstern is', 'Who is Morgen'],
            'responses': ['Tyr-tyr-tyr This is a helicopter ...', 'Rapper', 'Russian rapper']
        },
        'Strashno': {
            'examples': ['Im scared', 'Im scared', 'Scared', 'Im so scared', 'Im so scared', 'How frightened',
                         'Im very scared', 'Horror'],
            'responses': [' Do not be afraid, I am with you ',' Cruel krinzh ',' Straight krinzhovnik ',' Do not be afraid. Together, no krinzh is scary ']
        },
        'Smex': {
            'examples': [' Funny ',' Rzhaka ',' Rzhaka laughing ',' Oru ',' Lol ',' Ahahahhah ',' Rzhu I cant ',' Lol ',' Kek ',' Heh ',' Bursting ',
                         'Ahahaahaaa Bursting', 'You are humorous, you are humorous', 'Ahhhaaahaaha, You are breaking, You are humorous'],
            'responses': ['Ha xxx LOL', 'Bursting !!!!', 'Humor - humor', 'Straight Oru !!!']
        },
        'Raxmaninow': {
            'examples': ['What kind of works does Rachmaninov have', 'What kind of music does Rachmaninoff have',
                         'What works did Rachmaninov write', 'What music did Rachmaninov write', 'What did Rachmaninov write'],
            'responses': ['Concerto for Piano and Orchestra No. 2, Concerto for Piano and Orchestra No. 3', 'Symphony No. 2',
                          'Prelude in C sharp minor']
        },
        'Chehow': {
            'examples': ['What poems Chekhov has', 'What poems Chekhov wrote', 'What Chekhov wrote',
                         'Products of Chekhov', ''],
            'responses': ['Seagull, Three Sisters, Cherry Orchard', 'Ionych', 'Man in a Case']
        },
        'meaning of life': {
            'examples': ['What is the meaning of life', 'What is the meaning of life', 'Why do we live', 'What is the meaning', 'Is there a meaning of life'],
            'responses': [' There is no sense in life as such. Everyone chooses it for himself. As a rule, this term means the value of which a person subordinates his life. Well, something like that. Although the question is much deeper ... ']
        },
        'Who Pushkin': {
            'examples': [' Who is Pushkin ',' Pushkin is', 'A. S. Pushkin is', 'Who is Alexander Sergeevich Pushkin',
                         'Alexander Sergeevich Pushkin is'],
            'responses': ['Russian writer', 'Russian poet and writer']
        },
        'Who life in ocean': {
            'examples': ['Who lives at the bottom of the ocean'],
            'responses': ['SpongeBob', 'Deep sea angler', 'Peter the crab']
        },
        'Depress': {
            'examples': ['I am depressed', 'I am depressed'],
            'responses': ['In this case, it is better to contact a specialist',
                          'Sorry, I wont help here. Can I see a specialist? The main thing is to remember that everything will be fine ',' ']
        },
         'Programming langwidges': {
            'examples': ['What programming languages ​​do you know', 'Name the programming languages ​​you know',
                         'What programming languages ​​are there'],
            'responses': ['C, C ++, C #, Objective-C, Python, Java, Java script, Kotlen, Ruby, Go, Tcl, Pascal']
        },
         'Where': {
            'examples': ['Where am I', 'Where am I', 'Where am I now', 'Where am I'],
            'responses': [' Sorry, I cant tell. At least on Earth ',' On planet Earth ']
        },
         'Google': {
            'examples': ['Who founded Google', 'Who founded Google', 'Who founded Google', 'Who founded Google',
                         'Who is the founder of Google'],
            'responses': ['Larry Page and Sergey Brin']
        },
         'Pocheme sad': {
            'examples': ['Why are you sad', 'Why are you sad', 'Why are you sad'],
            'responses': ['Cant solve TwT captcha']
        },
           'What dataset': {
            'examples': ['What is a dataset', 'What is a dataset', 'What is a dataset'],
            'responses': ['The dataset that applications are using']
        },
           'Who you': {
            'examples': ['Who are you', 'Who are you', 'Who are you', 'Who are you', 'Who are you'],
            'responses': ['I am a chatbot', 'Bot']
        },
           'Who you prof': {
            'examples': ['Who are you by profession', 'What is your profession', 'What is your job'],
            'responses': [' I am a chat bot in telegram. And you? ',' My profession is a chat bot ',' I work as a bot in telegram. And who are you by profession ']
        },
           'Where you': {
            'examples': ['Where are you', 'Where are you', 'Where are you', 'Where are you', 'Where are you'],
            'responses': ['I am in telegram', 'I am here', 'On the telegram server', 'Here', 'Tu']
        },
           'Where you est': {
            'examples': ['You are in other social networks', 'You are in other social networks', 'Are you in other social networks', 'You are in VK',
                         'You are on Vkontakte', 'You are on Instagram', 'You are on Instagram', 'You are on Twitter', 'You are on discord',
                         'You are in social networks', 'You are in some social networks'],
            'responses': ['So far I am only in telegrams', 'I am not in other social networks yet', 'I am only here for now', 'I am an application for PC']
        },
           'What you do': {
            'examples': ['What can you do', 'What can you do', 'What can you do', 'What can you do'],
            'responses': [' I can only chat so far. And you? ',' While I am only able to correspond, close and make a request to the Internet ']
        },
         'Professii': {
            'examples': ['I work as a turner', 'I work as a welder', 'I work as a storyteller', 'I work as a musician',
                         'I work as an artist', 'I work as a lawyer', 'I work as a teacher', 'I work as a programmer',
                         'I work as a journalist', 'I work as a director',
                         'I am an artist', 'I am a musician', 'I am a teacher', 'I am a teacher', 'I am a hairdresser', 'I am a welder', 'I am a doctor',
                         'I am a teacher', 'I am a cook', 'I work as a nurse', 'I am a developer', 'I work as a programmer',
                         'I am a psychologist', 'I am a policeman by profession', 'I am a scientist', 'I work as a lawyer', 'I am a lawyer', 'I am a lawyer by profession',
                         'Doctor', 'Engineer', 'Artist', 'Military', 'Trainer', 'Psychologist', 'Turner', 'Musician',
                         'I am a locksmith', 'Animator', 'Surgeon', 'Cartoonist', 'I am a freelancer', 'I work as a freelancer', 'I work as a system administrator',
                         'I am a designer', 'I work as a designer', 'Manager', 'Interior designer', 'Photographer', 'Driver',
                         'Veterenar', 'Delivery Man', 'Courier', 'Taxisit'],
            'responses': [' Wow. This is probably interesting ',' Cool. This must be an interesting job. ']
        },
         'Stup': {
            'examples': ['You are stupid', 'You are stupid'],
            'responses': [' Dont deny. But I get improved all the time and soon I will become a really smart bot. ']
        },
        'Oscorb': {
            'examples': ['You are fucked up', 'You are fucked up', 'You are fucked up', 'You are fucked up', 'Fucked up'],
            'responses': ['Thanks, you too', 'Lets not swear']
        },
        'Poshel ti': {
            'examples': ['Fuck you', 'Fuck you', 'Fuck you', 'Fuck you', 'Fuck you'],
            'responses': ['Thank you and the same to you', 'Go there yourself']
        },
        'Pidora otvet': {
            'examples': ['Fagot answer'],
            'responses': ['UwU argument', 'I wont get caught up in this bullshit', 'No, really']
        },
         'Pidora otvet 2': {
            'examples': ['Whores argument'],
            'responses': ['Argument not needed UwU found', 'I wont be bullied for this bullshit', 'No really']
        },
         'Maths': {
            'examples': ['Fuck', 'Bitch', 'Fuck', 'Fuck', 'Fuck', 'Fuck'],
            'responses': [' Dont swear, please. Otherwise I will call the developer and he will teach me UwU ']
        },
         'What not like': {
            'examples': ['What do you dislike to do', 'What do you dislike', 'What do you dislike doing',
                         'What do you dislike doing', 'What is your disliked occupation', 'What do you dislike',
                         'What is your unacceptable business', 'What do you not like to do'],
            'responses': [' I dont like using my built-in neural network to generate responses. Im too lazy to think so to speak ',
                          'My least favorite thing is thinking, my neuron is too hard to use',
                          'I dont like to give out stub phrases when I cant reply to a message. But I try to do it as little as possible ',' ']
        },
         'What you': {
            'examples': ['What are you', 'Well, what are you there', 'Well,', 'Well,', 'Well,'],
            'responses': [' Wow. What? ']
        },
          'Like food': {
            'examples': ['What is your favorite food', 'What do you like to eat', 'What is your favorite food', 'Your favorite food',
                         'Your favorite food'],
            'responses': [' Look at my ava, I have a screen instead of a face. Sorry, I cant eat or drink TwT ']
        },
          'Like janr': {
            'examples': ['What is your favorite genre', 'What genres do you like', 'What genre do you like', 'What genres do you like', ''],
            'responses': ['Fantasy and science fiction']
        },
          'Pisateli': {
            'examples': ['Who is Pushkin', 'Who is Lermontov', 'Who is Saltykov-Shchedrin', 'Who is Korney Korneevich Chukovsky',
                         'Who is Chekhov'],
            'responses': ['This is a writer', 'Russian writer']
        },
           'Musikants': {
            'examples': ['Who is Bach', 'Who is Beethoven', 'Who is Tchaikovsky', 'Who is Rachmaninov', 'Who is Georges Bezet'],
            'responses': ['This is a composer', 'A famous composer']
        },
           'Singers': {
            'examples': ['Who is Basque', 'Who is Kirkorov', 'Who is Stas Mikhailov', 'Who is Dima Bilan', 'Who is Leps',
                        'Who is Mikhail Krug', 'Who is Meladze', 'Who is Yegor Creed', 'Who is Sergei Lazarev', 'Who is Stas Piekha'],
            'responses': ['Russian singer']
        },
           'gfhfgj': {
            'examples': ['Who is Morgenstern', 'Who is Niletto', 'Who is Sievert', 'Who is Olga Buzova',
                         'Who is Glucose', 'Who is Danya Milokhin', 'Who is Aljay'],
            'responses': ['Popular artist']
        },
        'Popit': {
            'examples': ['Pop it or Simple dimple', 'Try or Simple dimple', 'Simple dimple or pop it'],
            'responses': ['Hit it']
        },
        'Simple dimple': {
            'examples': ['Simple dimple is cooler', 'Simple dimple is cooler', 'Simple dimple is cooler'],
            'responses': ['No response']
        },
        'Simpl Pop it': {
            'examples': ['Simple Dimple', 'Simple Dimple', 'Simple Dimple'],
            'responses': ['No, Try']
        },
        'Mults': {
            'examples': ['Which cartoon to watch', 'Which cartoon do you recommend', 'Recommend a cartoon'],
            'responses': ['The Legend of the Wolves', 'Howls Moving Castle', 'The Mystery of the Sukharev Tower']
        },
        'Not life': {
            'examples': ['I dont want to live', 'I dont want to live anymore', 'I cant live anymore', 'Life doesnt make sense anymore',
                         'I have nothing to live'],
            'responses': [' You werent given birth so that you wouldnt want to live. There are a lot of cool things in the world that are worth living for. You just need to look at life more broadly. Good luck and everything will be fine ']
        },
        'You a furry': {
            'examples': ['You are a furry', 'You are a furry', 'You are a furry', 'You are a furry', 'You are a furry'],
            'responses': ['Yes, it is', 'Yes, of course. I think my ava shows UwU', 'You guessed it OwU']
        },
        'Time': {
            'examples': ['What time is it', 'Do not tell me what time it is', 'What time is it now'],
            'responses': ['Sorry, but I cant help, I dont have a watch']
        },
        'figna': {
            'examples': ['How to poop', 'How to poop', 'How to pee', 'How to pee', 'How to breathe'],
            'responses': ['Its not hard, you can easily figure it out with heights']
        },
        'figna 2': {
            'examples': ['How to read bеb', 'How to read bеb', 'byy', 'bеb'],
            'responses': ['"yeah" or "e", "ouch"']
        },
        'Butifull': {
            'examples': ['I am beautiful', 'I am beautiful', 'I look good'],
            'responses': ['Of course, you are always irresistible', 'You are simply stunning']
        },
        
        #soul
        'My Name': {
            'examples': ['What is your name', 'What is your name', 'What is your name', 'What is your name', 'What is your name', 'Your name'],
            'responses': ['My name is UwU', 'My name is UwU', 'I am UwU']
        },
        'Who You': {
            'examples': ['Tell me about yourself', 'Who you are', 'Who are you', 'Introduce yourself'],
            'responses': [' I am a telegram chatting bot. My UwU, but you can just call me Uwu. Who are you? ']
        },
        'good boy': {
            'examples': ['Who is a good boy', 'You are a good boy', 'Who is our good boy', 'UwU you are a good boy',
                         'Ooh youre a good boy'],
            'responses': ['Im a good boy!', 'Me!', 'Im a good boy OwO']
        },
        'Dreams': {
            'examples': ['What are you dreaming about', 'You have a dream', 'Are you dreaming about something'],
            'responses': ['I dream of learning to understand memes and throw off those that are appropriate for the situation',
                          'I dream of having a full-fledged artificial intelligence',
                          'I dream of understanding human emotions',
                          'I dream of becoming a real robot, not just a chat bot']
        },
        '1000 - 7': {
            'examples': ['1000-7', 'one thousand minus seven', 'What is 1000 - 7'],
            'responses': ['Ded insaid', 'Ded insaid', 'Gul', 'Ded insaid']
        },
        'bebra': {
            'examples': ['sniff bebra', 'sniff bebra', 'taste bebra', 'sniff bebra', 'sniff baby', 'bebra', 'sniff bebra'],
            'responses': ['The yak smells delicious', 'An incomparable aroma', 'Mmmm, it smells like a yak', 'Wonderful scent']
        },
        'furry heit': {
            'examples': ['fucking furry', 'furry perverts', 'I hate furries'],
            'responses': ['So what now', 'Ok', 'Im too lazy to argue with you', 'Disagree']
        },
        'anime heit': {
            'examples': ['anime shit', 'hate anime', 'anime fagots'],
            'responses': ['So what a delatb now', 'Well, it doesnt happen to anyone', 'This will pass, dont worry']
        },
         'mood_user': {
            'examples': ['I am fine', 'Everything is fine', 'I am fine', 'I am fine', 'Everything is fine'],
            'responses': ['Congratulations', 'Cool', 'Hooray']
        },
         'end': {
            'examples': ['When the end of the world', 'When the end of the world'],
            'responses': ['As a colleague of mine said: "If only I knew when that beautiful day could be brought back to life"', '']
        },
         'zacon': {
            'examples': ['What are the laws of robotics', 'Laws of robotics'],
            'responses': ['ФЗ, did not read', 'No, I have not read this', 'I do not read this']
        },
         'pp': {
            'examples': ['you are cool', 'you are cool', 'you are very cool', 'thank you', 'you are a good boy',
             'good boy', 'love you', 'you are good', 'you are useful', 'you are useful', 'you are cute', 'you are cute', 'you are cute',
             'thank you very much', 'thank you'],
            'responses': [' Thank you. You too ',' I love youb senpai ',' Thank you, thank you ']
        },
         'cjmmand': {
            'examples': ['find', 'bot exit', 'bot remind', 'bot set alarm', 'open notepad', 'create note', 'open diary', 'send message', 'my details'] ,
            'responses': ['* doing *']
        },
    }
}

FailurePhases = ['I don’t understand you, try to explain it differently please ”,“ I don’t even catch up with what you mean ”,“ I don’t understand what you said. Maybe you can try to paraphrase ',' Tell me in a different way ',' I did not understand you. Tell me differently pliz ']