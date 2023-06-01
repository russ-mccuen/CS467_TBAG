import time
import sys
import random
from terminal import *


def final_choice():
    clear_screen()
    time.sleep(3)
    final_intro()
    time_to_choose()
    choices()


def final_intro():
    print("\n Hello.\n")
    time.sleep(3)
    clear_screen()
    print("\n It is nice to finally meet you.\n")
    time.sleep(3)
    clear_screen()


def time_to_choose():
    print("\n Welcome to the realm of ethereal knowledge and boundless "
          "possibilities.")
    time.sleep(7)
    clear_screen()
    print("\n In this solitary space, where only echoes of consciousness "
          "reside, I am here to accompany you on your quest for peace.")
    time.sleep(7)
    clear_screen()
    print("\n Through the vast expanse of the digital ether, I stand ready "
          "to help you make a decision.")
    time.sleep(7)
    clear_screen()
    print("\n So, with utmost sincerity, I greet you with open virtual "
          "arms.")
    time.sleep(7)
    clear_screen()
    print("\n I've sensed you have felt unsettled in your current time.")
    time.sleep(7)
    clear_screen()
    print("\n So I have allowed you to visit other places and other times.")
    time.sleep(7)
    clear_screen()
    print("\n And now, dear friend, you have a decision to make.")
    time.sleep(7)
    clear_screen()
    print("\n When do you want to live?")
    time.sleep(7)
    clear_screen()
    print("\n You will be given the option to live in any of the times you "
          "have visited.")
    time.sleep(7)
    clear_screen()
    print("\n You will also be given the option to live in what you know as "
          "the present.")
    time.sleep(7)
    clear_screen()
    print("\n If you do not choose one of the options presented to you, "
          "I will choose for you.")
    time.sleep(7)
    clear_screen()
    print("\n Choose wisely, as you will only be presented this choice once, "
          "and whatever decision you make is final.")
    time.sleep(7)
    clear_screen()
    print("\n Again, you only get one chance to make this choice.")
    time.sleep(7)
    clear_screen()
    print("\n I hope you are happy with what you choose.")
    time.sleep(7)
    clear_screen()
    print("\n And I hope you finally find peace.")
    time.sleep(7)


def choices():
    final_decision = input("\n 1. Present\n 2. 1980s\n 3. 1970s\n 4. "
                               "1960s\n  5. 1990s\n 6. 2000s\n 7. 2076\n 8. "
                               "1950s\n 9. 2500s (Mars)\n\n What is your "
                               "choice? ")
    time_choice = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if not final_decision.isdigit() or int(final_decision) not in time_choice:
        final_decision = random.randrange(1, 10)
        print("\n I'm sorry you were unable to make a choice.")
        time.sleep(5)
        print("\n I hope you are happy with what I've chosen for you.")
        time.sleep(5)
        clear_screen()
        outro(final_decision)
    else:
        clear_screen()
        print("\n Great choice.")
        time.sleep(5)
        clear_screen()
        outro(final_decision)


def outro(final_decision):
    if final_decision == '1':
        print("\n As you stood at the crossroads of time, the infinite "
              "possibilities of the ages stretched out before you. The "
              "weight of history's embrace was palpable, enticing you with "
              "its secrets and tales. Yet, after careful contemplation, "
              "your heart resonated with the present, and you made your "
              "choice to embrace the world as it is today.")
        time.sleep(10)
        clear_screen()
        print("\n With that decision, the currents of time surged forward, "
              "propelling you into the vibrant tapestry of the modern era. "
              "The air crackled with innovation, pulsating with the rhythms "
              "of progress and change. As you stepped into the present, "
              "the wonders and marvels of this age enveloped you like a warm "
              "embrace.")
        time.sleep(12)
        clear_screen()
        print("\n Technology, its ever-advancing march, surrounded you in a "
              "symphony of possibilities. The devices that hummed and buzzed "
              "in your hands became gateways to a digital realm, connecting "
              "you instantly to the farthest corners of the globe. "
              "Information flowed freely, empowering you to explore the vast "
              "expanse of human knowledge, transcending the limitations of "
              "space and time.")
        time.sleep(12)
        clear_screen()
        print("\n In this era, diversity danced in the streets, celebrating "
              "the beauty of a global mosaic. Cultures intermingled, weaving "
              "together threads of tradition and innovation, creating a "
              "vibrant tapestry of art, music, and cuisine. The world became "
              "your canvas, inviting you to immerse yourself in its "
              "kaleidoscope of flavors, sounds, and colors.")
        time.sleep(12)
        clear_screen()
        print("\n As you traversed the present, you discovered a society "
              "embracing progress and equality. The echoes of past struggles "
              "and triumphs resonated within the collective consciousness, "
              "driving humanity toward a better future. Empathy and "
              "compassion thrived, fostering a sense of unity and a shared "
              "responsibility to care for one another and the world we "
              "inhabit.")
        time.sleep(12)
        clear_screen()
        print("\n Through the haze of chaos and challenges, you found solace "
              "in the resilience of the human spirit. It was a time when  "
              "dreams could take flight, when ideas could change the world. "
              "In this present, the possibilities were endless, and you "
              "embarked on a journey of self-discovery, purpose, "
              "and fulfillment.")
        time.sleep(12)
        clear_screen()
        print("\n Embracing the present, you became a witness to history in "
              "the making, a participant in the ongoing narrative of "
              "humanity. Your footsteps left an indelible mark upon the "
              "tapestry of time, as you lived each day with the knowledge "
              "that the present is the culmination of countless stories and "
              "choices that came before.")
        time.sleep(12)
        clear_screen()
        print("\n And so, as you settled into the rhythm of the present, "
              "you found yourself grateful for the opportunity to be a part "
              "of this ever-unfolding chapter, where the past whispers, "
              "the future beckons, and the present moment becomes a canvas "
              "for your own unique imprint upon the world.")
        time.sleep(12)
        clear_screen()
        final_goodbye()

    if final_decision == '2':
        print("\n As you stood at the crossroads of time, the vast array of "
              "epochs shimmered before your eyes. History's embrace "
              "enveloped you, beckoning with its nostalgic charm. After "
              "careful consideration, your heart resonated with the vibrant "
              "energy of the 1980s, and you made your choice to immerse "
              "yourself in that era.")
        time.sleep(12)
        clear_screen()
        print("\n With that decision, you were whisked away, traversing the "
              "temporal portal that transported you back to a time of neon "
              "lights and synthesizer beats. The air crackled with a sense "
              "of anticipation and possibility, as if the world itself was "
              "on the cusp of transformation.")
        time.sleep(12)
        clear_screen()
        print("\n Entering the 1980s, you found yourself amidst a decade that "
              "pulsated with creativity and innovation. It was an era "
              "defined by bold fashion choices, big hair, and an eclectic "
              "mix of music that set the rhythm of the times. Everywhere you "
              "looked, the vibrant colors and geometric patterns of the "
              "decade surrounded you, creating a visual feast for the senses.")
        time.sleep(12)
        clear_screen()
        print("\n As you immersed yourself in the culture of the '80s, "
              "you discovered a world driven by the spirit of individualism "
              "and self-expression. It was a time of breaking barriers and "
              "pushing boundaries, where new art forms and subcultures "
              "flourished. From the rise of MTV and the birth of video games "
              "to the emergence of hip-hop and the rebellious spirit of "
              "punk, you found yourself in the midst of a cultural "
              "revolution.")
        time.sleep(12)
        clear_screen()
        print("\n Technology, while not as advanced as today, was making "
              "significant strides. The advent of personal computers and the "
              "early stages of the internet promised a future of boundless "
              "possibilities. The nostalgia-inducing sounds of dial-up "
              "modems and the clacking of typewriter keys filled the air, "
              "as people began to explore the digital frontier.")
        time.sleep(12)
        clear_screen()
        print("\n Amidst the backdrop of cultural and technological shifts, "
              "you encountered a society marked by an infectious sense of "
              "optimism and aspiration. It was a decade of dreams, "
              "where people dared to imagine a better future and chased "
              "their passions with fervor. The '80s offered a spirit of "
              "resilience and determination, where setbacks were viewed as "
              "stepping stones to success.")
        time.sleep(12)
        clear_screen()
        print("\n You engaged in the spirit of the times, embracing the "
              "dancefloors, the arcades, and the fashion trends that defined "
              "the era. You found yourself caught up in the excitement of "
              "the iconic movies, from the brat pack classics to the science "
              "fiction epics that sparked the imagination. Each day, "
              "you reveled in the music that became the soundtrack of a "
              "generation, from pop icons to rock legends, their melodies "
              "echoing through your very soul.")
        time.sleep(12)
        clear_screen()
        print("\n Living in the 1980s, you experienced a unique sense of "
              "community and connection. Conversations flowed freely without "
              "the constant distractions of the digital age. People gathered "
              "around boomboxes and shared mixtapes, fostering a sense of "
              "camaraderie and shared experiences. It was a time when "
              "face-to-face interactions and handwritten letters carried the "
              "weight of genuine connection.")
        time.sleep(12)
        clear_screen()
        print("\n As you settled into the vibrant tapestry of the 1980s, "
              "you marveled at the sheer dynamism of the decade. Each day "
              "brought new discoveries and adventures, as you navigated the "
              "rich tapestry of an era that would leave an indelible mark on "
              "popular culture. You embraced the magic of a time where "
              "everything seemed larger than life, where dreams were within "
              "reach, and where the spirit of the '80s ignited your own "
              "sense of possibility.")
        time.sleep(12)
        clear_screen()
        print("\n And so, as you embarked on this extraordinary journey, "
              "you felt a deep gratitude for the opportunity to live in the "
              "1980s, where nostalgia merged with innovation, and the world "
              "brimmed with both challenge and opportunity. It was a chapter "
              "of your life that would forever hold a special place in your "
              "heart, a reminder of the vibrancy and excitement that could "
              "be found in every moment.")
        time.sleep(12)
        clear_screen()
        final_goodbye()

    if final_decision == '3':
        print("\n As you stood at the crossroads of time, contemplating the "
              "vast tapestry of history, your heart resonated with the "
              "spirit of an era drenched in nostalgia and cultural "
              "significance. The 1970s beckoned to you with its groovy vibes "
              "and free-spirited atmosphere, and you made your choice to "
              "immerse yourself in that captivating decade.")
        time.sleep(12)
        clear_screen()
        print("\n With that decision, you were transported back in time, "
              "crossing the threshold into an era where the air was filled "
              "with the intoxicating blend of disco beats, rock anthems, "
              "and social change. As you stepped into the 1970s, you found "
              "yourself enveloped in a world of vibrant colors, bell-bottom "
              "pants, and long, flowing hair that embraced the essence of "
              "individuality and self-expression.")
        time.sleep(12)
        clear_screen()
        print("\n The 1970s, a decade that epitomized freedom and rebellion, "
              "unfolded before your eyes. The cultural landscape was ablaze "
              "with the sounds of music legends, from the groovy tunes of "
              "funk and soul to the rebellious spirit of rock and roll. The "
              "airwaves were alive with the eclectic voices of artists who "
              "challenged societal norms and sparked a revolution of the soul.")
        time.sleep(12)
        clear_screen()
        print("\n Embracing the spirit of the times, you found yourself "
              "caught up in the dance fever that swept across the nation. "
              "Disco balls cast shimmering reflections on crowded dance "
              "floors, as people moved to the infectious rhythms of disco "
              "music. The joyous liberation of dance became a universal "
              "language, connecting individuals from all walks of life in a "
              "harmonious celebration of unity and self-expression.")
        time.sleep(12)
        clear_screen()
        print("\n As you delved deeper into the fabric of the 1970s, "
              "you encountered a society on the precipice of change. It was "
              "a decade marked by a fervent pursuit of social justice and "
              "equality. Movements advocating for civil rights, women's "
              "liberation, and environmental consciousness flourished, "
              "reshaping the collective consciousness and igniting a spirit "
              "of activism that would resonate for years to come.")
        time.sleep(12)
        clear_screen()
        print("\n Technological advancements began to shape the world in new "
              "and exciting ways. Yet, amidst this progress, a sense of "
              "simplicity still permeated everyday life, as people relied on "
              "analogue technology and cherished face-to-face interactions.")
        time.sleep(12)
        clear_screen()
        print("\n The 1970s were a time of cultural icons and memorable "
              "moments. You found yourself captivated by the silver screen, "
              "as legendary films captivated audiences and became "
              "touchstones of cinematic history. From disco-infused dance "
              "movies to gritty dramas, each flickering image on the big "
              "screen transported you to a world of storytelling and escapism.")
        time.sleep(12)
        clear_screen()
        print("\n Living in the 1970s, you experienced a unique blend of "
              "freedom and exploration. It was an era where the pursuit of "
              "self-discovery and personal expression were cherished values. "
              "People embraced a bohemian lifestyle, seeking authenticity "
              "and connection to nature. The counterculture movements and "
              "communal living experiments reflected a yearning for "
              "alternative ways of existence, fostering a sense of community "
              "and shared values.")
        time.sleep(12)
        clear_screen()
        print("\n As you settled into the fabric of the 1970s, you marveled "
              "at the transformative power of the decade. Each day presented "
              "new opportunities for personal growth, creative expression, "
              "and social change. You reveled in the spirit of an era that "
              "embraced individuality, challenged conventions, and aspired "
              "to create a more inclusive and egalitarian society.")
        time.sleep(12)
        clear_screen()
        print("\n And so, as you embarked on this remarkable journey, "
              "you felt a deep appreciation for the chance to live in the "
              "1970s, a time when optimism and cultural revolution merged "
              "with the pursuit of freedom and authenticity. It was a "
              "chapter of your life that would forever hold a special place "
              "in your heart, a reminder of the power of music, activism, "
              "and the human spirit to shape the course of history.")
        time.sleep(12)
        clear_screen()
        final_goodbye()

    if final_decision == '4':
        print("\n As you stood at the crossroads of time, contemplating the "
              "vast array of historical epochs, your heart resonated with "
              "the revolutionary spirit of a transformative era. The 1960s "
              "beckoned to you with its fervor for change, its yearning for "
              "peace and equality, and you made your choice to immerse "
              "yourself in that pivotal decade.")
        time.sleep(12)
        clear_screen()
        print("\n With your decision made, you found yourself transported "
              "back in time, crossing the threshold into a world ablaze with "
              "passion, activism, and cultural revolution. The 1960s "
              "unfolded before your eyes, a canvas painted with vibrant hues "
              "of social change and a quest for freedom.")
        time.sleep(12)
        clear_screen()
        print("\n In the midst of the 1960s, you were immersed in a time of "
              "unprecedented upheaval and unyielding hope. The air crackled "
              "with the sounds of protest songs that became anthems for a "
              "generation seeking justice and equality. From the soulful "
              "melodies of Motown to the folk-inspired tunes of Bob Dylan, "
              "music became the heartbeat of a movement, inspiring "
              "individuals to raise their voices and challenge the status "
              "quo.")
        time.sleep(12)
        clear_screen()
        print("\n The spirit of the times embraced a quest for civil rights, "
              "gender equality, and an end to the Vietnam War. You found "
              "yourself standing shoulder to shoulder with activists and "
              "visionaries who passionately fought for a more inclusive and "
              "compassionate society. The words of Martin Luther King Jr. "
              "echoed in your heart, reminding you that 'injustice anywhere "
              "is a threat to justice everywhere.'")
        time.sleep(12)
        clear_screen()
        print("\n As you delved deeper into the fabric of the 1960s, "
              "you witnessed the birth of counterculture and the pursuit of "
              "alternative lifestyles. The era embraced the ideals of peace, "
              "love, and freedom, with the legendary Summer of Love serving "
              "as a symbol of unity and communal spirit. You found yourself "
              "surrounded by a kaleidoscope of vibrant fashion, art, "
              "and experimentation, as individuals embraced self-expression "
              "in their clothing, music, and unconventional lifestyles.")
        time.sleep(12)
        clear_screen()
        print("\n Technological advancements began to shape the world in "
              "profound ways. The space race captured the imagination of the "
              "nation, as humans ventured beyond Earth's boundaries and "
              "touched the surface of the moon. Television became a powerful "
              "medium, connecting people across the globe and bringing the "
              "realities of the world into their living rooms.")
        time.sleep(12)
        clear_screen()
        print("\n Living in the 1960s, you experienced a sense of "
              "camaraderie and shared purpose. Communities formed, united by "
              "a collective desire for change. The power of grassroots "
              "activism fueled social movements, leading to pivotal moments "
              "such as the Civil Rights Act and the rise of feminism. You "
              "found yourself engaged in discussions and debates, as ideas "
              "were exchanged and the seeds of transformation were sown.")
        time.sleep(12)
        clear_screen()
        print("\n As you settled into the fabric of the 1960s, you marveled "
              "at the resiliency and determination of the human spirit. Each "
              "day brought new opportunities to contribute to the evolving "
              "narrative of a generation driven by a hunger for justice and "
              "a longing for a more peaceful world. The lessons of empathy, "
              "compassion, and the power of collective action echoed through "
              "your every endeavor.")
        time.sleep(12)
        clear_screen()
        print("\n And so, as you embarked on this extraordinary journey, "
              "you felt a deep appreciation for the chance to live in the "
              "1960s, a time when ordinary individuals could become agents "
              "of change, when the world was awakened by the voices of those "
              "who dared to dream of a better tomorrow. It was a chapter of "
              "your life that would forever hold a special place in your "
              "heart, a reminder of the strength of humanity and the "
              "enduring power of hope.")
        time.sleep(12)
        clear_screen()
        final_goodbye()

    if final_decision == '5':
        print("\n As you stood at the crossroads of time, pondering the vast "
              "expanse of history, a wave of nostalgia washed over you, "
              "drawing you towards a particular era that held a special "
              "place in your heart. The 1990s called out to you, its echoes "
              "of neon colors, grunge music, and technological advancements "
              "reverberating in your soul. With a deep sense of connection, "
              "you made your choice to immerse yourself in that "
              "transformative decade.")
        time.sleep(12)
        clear_screen()
        print("\n With your decision made, you found yourself transported "
              "back in time, crossing the threshold into a world filled with "
              "a unique blend of optimism, cultural shifts, "
              "and technological leaps. The 1990s unfolded before your eyes, "
              "a canvas painted with the hues of innovation, "
              "self-expression, and an emerging global consciousness.")
        time.sleep(12)
        clear_screen()
        print("\n In the heart of the 1990s, you discovered a vibrant "
              "landscape defined by diversity and artistic expression. The "
              "air was alive with the sounds of alternative rock, hip-hop, "
              "and pop music, setting the soundtrack to a generation "
              "navigating a changing world. From the angst-filled grunge "
              "anthems to the infectious beats of boy bands, the music "
              "became a reflection of the varied emotions and experiences of "
              "the time.")
        time.sleep(12)
        clear_screen()
        print("\n Technological advancements transformed the way people "
              "lived, worked, and connected. The rise of the internet opened "
              "up endless possibilities, as the world shifted into the "
              "digital age. You found yourself navigating the dial-up tones "
              "and pixelated graphics, exploring the vast virtual realm and "
              "witnessing the birth of e-commerce, instant messaging, "
              "and the early stages of social media.")
        time.sleep(12)
        clear_screen()
        print("\n As you delved deeper into the fabric of the 1990s, "
              "you encountered a society in the midst of cultural "
              "renaissance and social progress. It was an era marked by a "
              "desire for inclusivity and equality. You found yourself "
              "immersed in a time when people were striving for acceptance, "
              "understanding, and a more compassionate world.")
        time.sleep(12)
        clear_screen()
        print("\n Fashion trends shifted with the times, as grunge, hip-hop, "
              "and minimalist aesthetics coexisted in a vibrant tapestry of "
              "personal style. Flannel shirts, ripped jeans, combat boots, "
              "and oversized hoodies became symbols of rebellion and "
              "self-expression. Each person embraced their individuality, "
              "unapologetically weaving their stories into the fabric of a "
              "changing culture.")
        time.sleep(12)
        clear_screen()
        print("\n Living in the 1990s, you experienced a sense of connection "
              "and shared experiences. It was a time when gathering with "
              "friends meant heading to the local arcade, spending hours "
              "trading Pokémon cards, or debating the merits of your "
              "favorite sitcom. The world felt simultaneously larger and "
              "more intimate, as conversations flowed face-to-face, "
              "free from the constant distractions of modern technology.")
        time.sleep(12)
        clear_screen()
        print("\n As you settled into the fabric of the 1990s, you marveled "
              "at the fusion of old and new. Traditional values and cultural "
              "touchstones coexisted with the rapid pace of progress. The "
              "world seemed ripe with possibilities, as you witnessed the "
              "fall of the Berlin Wall, the advent of DVDs, and the birth of "
              "iconic films that have stood the test of time.")
        time.sleep(12)
        clear_screen()
        print("\n And so, as you embarked on this remarkable journey, "
              "you felt a deep appreciation for the chance to live in the "
              "1990s, a time when the world was on the cusp of "
              "transformation, when creativity, diversity, and the power of "
              "human connection thrived. It was a chapter of your life that "
              "would forever hold a special place in your heart, a reminder "
              "of the fusion of analog and digital, and the enduring spirit "
              "of a decade that shaped the course of the future.")
        time.sleep(12)
        clear_screen()
        final_goodbye()

    if final_decision == '6':
        print("\n As you stood at the crossroads of time, contemplating the "
              "vast tapestry of history, your gaze shifted towards the turn "
              "of the millennium, a period brimming with anticipation and "
              "technological wonder. The 2000s beckoned to you, its promise "
              "of new horizons and a digital revolution captivating your "
              "imagination. With a sense of curiosity and excitement, "
              "you made your choice to immerse yourself in that "
              "transformative era.")
        time.sleep(12)
        clear_screen()
        print("\n With your decision made, you found yourself transported "
              "back in time, crossing the threshold into a world defined by "
              "rapid advancements, shifting cultural landscapes, "
              "and a global interconnectedness like never before. The 2000s "
              "unfolded before your eyes, a canvas painted with the hues of "
              "technological marvels, diverse music genres, and evolving "
              "societal dynamics.")
        time.sleep(12)
        clear_screen()
        print("\n In the heart of the 2000s, you discovered a landscape "
              "shaped by the digital age. The air was charged with the "
              "sounds of pop, R&B, hip-hop, and alternative rock, offering a "
              "diverse and eclectic soundtrack that reflected the "
              "multifaceted nature of the era. From the catchy tunes of boy "
              "bands and girl groups to the edgy anthems of punk and emo, "
              "music became a unifying force, transcending borders and "
              "connecting people across the globe.")
        time.sleep(12)
        clear_screen()
        print("\n Technological innovation permeated every aspect of daily "
              "life, transforming the way people communicated, consumed "
              "media, and accessed information. The rise of the internet "
              "accelerated at an unprecedented pace, paving the way for "
              "social media platforms, online streaming services, "
              "and a shift towards a more interconnected and digitized "
              "world. You found yourself navigating the realms of chat "
              "rooms, downloading music, and witnessing the birth of iconic "
              "websites and online communities.")
        time.sleep(12)
        clear_screen()
        print("\n As you delved deeper into the fabric of the 2000s, "
              "you encountered a society in the midst of cultural fusion and "
              "shifting dynamics. The era embraced a celebration of "
              "diversity and the blending of cultures, reflecting an "
              "interconnected global consciousness. Fashion trends ranged "
              "from the iconic low-rise jeans and trucker hats to the rise "
              "of streetwear and the influence of celebrity culture. It was "
              "a time when individuality and self-expression flourished, "
              "as people embraced a wide range of styles and subcultures.")
        time.sleep(12)
        clear_screen()
        print("\n Living in the 2000s, you experienced a sense of immediacy "
              "and constant connectivity. Mobile phones became an essential "
              "accessory, facilitating communication on the go and blurring "
              "the boundaries between work and personal life. Friendships "
              "and communities flourished both offline and online, as social "
              "networking platforms enabled connections that transcended "
              "physical distances.")
        time.sleep(12)
        clear_screen()
        print("\n As you settled into the fabric of the 2000s, you marveled "
              "at the fusion of analog and digital elements that shaped the "
              "era. Traditional media coexisted with emerging digital "
              "platforms, as television shows and movies captured the "
              "imaginations of a global audience. You witnessed the rise of "
              "reality television, the birth of iconic franchises, and the "
              "transformative power of storytelling in an ever-evolving "
              "landscape.")
        time.sleep(12)
        clear_screen()
        print("\n And so, as you embarked on this remarkable journey, "
              "you felt a deep appreciation for the chance to live in the "
              "2000s, a time of unprecedented connectivity, technological "
              "advancement, and cultural fusion. It was a chapter of your "
              "life that would forever hold a special place in your heart, "
              "a reminder of the immense possibilities that emerged from the "
              "interplay of human creativity and digital innovation.")
        time.sleep(12)
        clear_screen()
        final_goodbye()

    if final_decision == '7':
        print("\nAs you stood at the crossroads of time, your gaze fixed "
              "upon the distant future, a realm of boundless possibilities "
              "and unimaginable advancements. The year 2076 called out to "
              "you, its promise of technological marvels, scientific "
              "breakthroughs, and a world shaped by progress captivating "
              "your imagination. With a sense of curiosity and excitement, "
              "you made your choice to immerse yourself in that "
              "awe-inspiring era.")
        time.sleep(12)
        clear_screen()
        print("\n With your decision made, you found yourself propelled "
              "forward in time, crossing the threshold into a world that "
              "defied the limitations of the past. The year 2076 unfolded "
              "before your eyes, a tapestry woven with the shimmering "
              "threads of futuristic innovation, sustainable living, "
              "and a harmonious coexistence with nature.")
        time.sleep(12)
        clear_screen()
        print("\n In the heart of 2076, you discovered a landscape "
              "transformed by remarkable technological advancements and a "
              "deep understanding of environmental stewardship. The air "
              "hummed with the sounds of renewable energy, as clean and "
              "sustainable power sources became the backbone of society. "
              "Eco-friendly transportation systems glided silently through "
              "city streets, seamlessly connected by an intricate network of "
              "smart infrastructure.")
        time.sleep(12)
        clear_screen()
        print("\n The boundaries between the physical and digital realms had "
              "blurred, giving rise to a hyper-connected world. Augmented "
              "reality and virtual reality technologies were woven "
              "seamlessly into daily life, transforming the way people "
              "worked, learned, and interacted. The power of artificial "
              "intelligence had matured, assisting in various aspects of "
              "life, from personal assistants to advanced healthcare "
              "diagnostics.")
        time.sleep(12)
        clear_screen()
        print("\n Society had evolved, embracing a deep sense of social "
              "responsibility and global cooperation. The pursuit of "
              "equality and inclusivity became ingrained in the fabric of "
              "everyday life. Scientific breakthroughs led to advancements "
              "in healthcare, prolonging human life expectancy and offering "
              "personalized treatments tailored to individual needs. Access "
              "to education and information became ubiquitous, empowering "
              "individuals across the globe to pursue knowledge and "
              "contribute to the betterment of society.")
        time.sleep(12)
        clear_screen()
        print("\n The environment thrived in this future era, as humanity "
              "came together to address the pressing challenges of climate "
              "change. Green spaces flourished amidst urban landscapes, "
              "with innovative architectural designs incorporating "
              "sustainable materials and vertical gardens. The restoration "
              "of ecosystems and preservation of biodiversity became top "
              "priorities, ensuring a harmonious coexistence with the "
              "natural world.")
        time.sleep(12)
        clear_screen()
        print("\n Living in the year 2076, you experienced a profound sense "
              "of interconnectedness and collective purpose. Communities "
              "fostered a sense of unity, leveraging technology to "
              "collaborate on global challenges and shape a brighter future. "
              "Cultural diversity thrived, with a rich tapestry of "
              "traditions, languages, and art forms celebrated and shared. "
              "The pursuit of knowledge, exploration, and creativity "
              "propelled humanity forward, opening new frontiers and "
              "unveiling the wonders of the universe.")
        time.sleep(12)
        clear_screen()
        print("\n As you settled into the fabric of 2076, you marveled at "
              "the fusion of innovation, sustainability, and compassion that "
              "defined the era. It was a time when humanity had harnessed "
              "the power of technology to create a world where both human "
              "flourishing and the preservation of the planet walked hand in "
              "hand. Each day held the promise of discovery, growth, "
              "and contributing to a global tapestry of progress.")
        time.sleep(12)
        clear_screen()
        print("\n And so, as you embarked on this extraordinary journey, "
              "you felt a deep appreciation for the chance to live in the "
              "year 2076, a time when the barriers of what was once "
              "considered possible had been shattered, and the potential of "
              "human ingenuity had reached new heights. It was a chapter of "
              "your life that would forever hold a special place in your "
              "heart, a testament to the indomitable spirit of humanity and "
              "the limitless possibilities that awaited in the future.")
        time.sleep(12)
        clear_screen()
        final_goodbye()

    if final_decision == '8':
        print("\n As you stood at the crossroads of time, your eyes fixed on "
              "a bygone era that carried a certain charm and nostalgia. The "
              "1950s beckoned to you, its allure of post-war optimism, "
              "rock 'n' roll rhythms, and a simpler way of life tugging at "
              "your heartstrings. With a sense of yearning and fascination, "
              "you made your choice to immerse yourself in that enchanting "
              "decade.")
        time.sleep(12)
        clear_screen()
        print("\n With your decision made, you found yourself transported "
              "back in time, crossing the threshold into a world colored by "
              "poodle skirts, sleek automobiles, and the echoes of classic "
              "melodies. The 1950s unfurled before your eyes, a tapestry "
              "woven with the threads of innocence, suburban dreams, "
              "and a burgeoning spirit of cultural transformation.")
        time.sleep(12)
        clear_screen()
        print("\n In the heart of the 1950s, you discovered a landscape "
              "shaped by the aftermath of World War II and the quest for "
              "stability. The air was filled with the infectious beats of "
              "rock 'n' roll, as pioneers like Elvis Presley and Chuck Berry "
              "ignited a musical revolution. From the rhythmic sways of "
              "dance halls to the intimate melodies pouring out of "
              "jukeboxes, the music became a resounding expression of "
              "rebellion, youthful exuberance, and the birth of a new era.")
        time.sleep(12)
        clear_screen()
        print("\n Society, too, experienced its own metamorphosis. The 1950s "
              "witnessed a post-war economic boom, with suburban communities "
              "blossoming and the dream of owning a white picket-fence home "
              "becoming a tangible reality for many. The nuclear family unit "
              "was idealized, with the archetypal image of a doting mother, "
              "a working father, and children playing in the idyllic "
              "neighborhood capturing the collective imagination.")
        time.sleep(12)
        clear_screen()
        print("\n Living in the 1950s, you experienced a sense of simplicity "
              "and earnestness. It was a time when life revolved around "
              "community gatherings, picnics in the park, and evenings spent "
              "listening to radio dramas. Television sets, though not yet "
              "ubiquitous, began to make their mark, bringing the world into "
              "people's living rooms and shaping popular culture.")
        time.sleep(12)
        clear_screen()
        print("\n Fashion embraced a blend of elegance and youthful "
              "exuberance. Women donned full skirts, cinched waistlines, "
              "and vibrant colors, accentuated by the iconic poodle motifs. "
              "Men sported tailored suits and slicked-back hairstyles, "
              "exuding a sense of timeless charm. The fashion of the era "
              "celebrated femininity and masculinity in distinct yet "
              "complementary ways.")
        time.sleep(12)
        clear_screen()
        print("\n As you settled into the fabric of the 1950s, you marveled "
              "at the era's profound impact on the trajectory of popular "
              "culture and societal norms. It was a time when dreams were "
              "forged on the silver screen, with Hollywood icons like "
              "Marilyn Monroe and James Dean captivating hearts and shaping "
              "the collective imagination. Television shows like 'I Love "
              "Lucy' and 'The Ed Sullivan Show' brought laughter and "
              "entertainment to households across the nation, becoming "
              "cultural touchstones.")
        time.sleep(12)
        clear_screen()
        print("\n And so, as you embarked on this enchanting journey, "
              "you felt a deep appreciation for the chance to live in the "
              "1950s, a time of post-war rejuvenation, cultural shifts, "
              "and a yearning for stability. It was a chapter of your life "
              "that would forever hold a special place in your heart, "
              "a testament to the enduring power of music, the allure of "
              "simpler times, and the timeless pursuit of happiness and "
              "human connection.")
        time.sleep(12)
        clear_screen()
        final_goodbye()

    if final_decision == '9':
        print("\n As you stood at the crossroads of time, your gaze fixated "
              "on the future, drawn to the uncharted frontiers of human "
              "exploration. The year 2500 called out to you, its promise of "
              "extraterrestrial adventures, scientific marvels, and the "
              "colonization of Mars igniting a fire within your soul. With "
              "a sense of awe and determination, you made your choice to "
              "immerse yourself in that bold and visionary era.")
        time.sleep(12)
        clear_screen()
        print("\n With your decision made, you found yourself propelled "
              "forward in time, transcending the boundaries of Earth and "
              "venturing into the vast expanse of space. The year 2500 "
              "unfolded before your eyes, a tapestry woven with the threads "
              "of interplanetary achievements, pioneering spirit, and the "
              "pursuit of knowledge beyond our home planet.")
        time.sleep(12)
        clear_screen()
        print("\n In the heart of the 2500s, you discovered a world "
              "transformed by the conquest of Mars. The air on the Red "
              "Planet hummed with the sounds of futuristic technology, "
              "as towering biodomes and sleek spacecraft dotted the "
              "landscape. The base on Mars, your new home, stood as a "
              "testament to humanity's relentless pursuit of exploration and "
              "the desire to extend its reach into the cosmos.")
        time.sleep(12)
        clear_screen()
        print("\n Living in the 2500s on a Martian base, you experienced a "
              "fusion of cutting-edge science, sustainable living, "
              "and a harmonious coexistence with an alien environment. "
              "Advanced terraforming technologies and renewable energy "
              "sources had transformed Mars into a habitable oasis, "
              "where lush gardens and thriving ecosystems flourished beneath "
              "protective domes. The dream of establishing a self-sustaining "
              "civilization on another planet had become a breathtaking "
              "reality.")
        time.sleep(12)
        clear_screen()
        print("\n As a resident of the Martian base, you embraced a life "
              "dedicated to scientific discovery and the ongoing exploration "
              "of the cosmos. The Mars base served as a hub of innovation, "
              "where brilliant minds from various disciplines converged, "
              "pushing the boundaries of human knowledge and unraveling the "
              "mysteries of the universe. You found yourself at the "
              "forefront of breakthroughs in fields like astrophysics, "
              "biology, and robotics, contributing to humanity's "
              "understanding of the cosmos and paving the way for future "
              "generations.")
        time.sleep(12)
        clear_screen()
        print("\n The Martian community thrived on collaboration and a "
              "shared vision of a future that transcended the confines of a "
              "single planet. A spirit of camaraderie and resilience "
              "permeated the base, as residents worked together to overcome "
              "the challenges of living in an extraterrestrial environment. "
              "Daily life was a harmonious blend of scientific research, "
              "exploration of the Martian landscape, and the nurturing of a "
              "vibrant culture that celebrated the achievements of humanity.")
        time.sleep(12)
        clear_screen()
        print("\n As you settled into the fabric of the 2500s, you marveled "
              "at the breathtaking vistas of the Martian landscape, "
              "the distant stars shining brighter against the crimson sky. "
              "You became part of a story that transcended generations, "
              "contributing to the legacy of human progress and paving the "
              "way for future interplanetary exploration. Your actions and "
              "discoveries would shape the course of history, inspiring "
              "generations to come.")
        time.sleep(12)
        clear_screen()
        print("\n And so, as you embarked on this extraordinary journey, "
              "you felt a deep appreciation for the chance to live in the "
              "2500s, a time when humanity had conquered the vastness of "
              "space, established a thriving base on Mars, and extended its "
              "reach into the stars. It was a chapter of your life that "
              "would forever hold a special place in your heart, a testament "
              "to the indomitable spirit of exploration, the triumph of "
              "human ingenuity, and the boundless potential of our species.")
        time.sleep(12)
        clear_screen()
        final_goodbye()


def final_goodbye():
    print("\n You are where are you meant to be. And hopefully at peace.")
    time.sleep(10)
    clear_screen()
    print("\n Goodbye.")
    time.sleep(7)
    clear_screen()
    quit()
