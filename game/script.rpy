# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("test", color="#fdfefe")

define nar = Character("")
define i = Character("???", color= "#fdfefe")

define manic = Character("Manic", color="#2e4053")
define jay = Character("Jay", callback = talking_callback, cb_image_talking = "jay", color="#2ecc71")
define kit = Character("Kit", color="#3498db")
define andrea = Character("Andrea", color="#8e44ad")
define vida = Character("Vida", color="#f1c40f")

define neda = Character("Neda", color= "#fdfefe")

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
   
    # These display lines of dialogue.

    # prologue here

    stop music fadeout 4
    scene bg blank
    show jay animation_talk at right
    nar "I woke up with a start." 
    nar "It was that damn dream again."
    nar "I couldn't even describe what it was about. In my mind it was nothing but a gray blur."
    nar "I scratched my head, my hand passing through my long black hair. I turned over only for my eyes to meet my alarm clock."
    jay "Shit..."
    jay "I'm gonna be late for school."

    scene bg streetcorner
    show jay animation_talk at right
    play music "audio/background music 1.mp3" volume 0.5 fadein 2.0 

    nar "Soon, I was dashing down the street, the wind brushing against my white dress shirt and black pants. my shoes clopped on the ground as I ran over the crosswalk, I dodged out of the way of an incoming car that missed me by about an inch."
    nar "I couldn't care less, however, my one and only focus was getting to high school on time. If I got caught by any of the teachers for being late, I would most certainly be sent to detention after school, and that would be catastrophic. Not for the reason most people would think however." 
    nar "I couldn't care less about detention; all I care about is my club."
    nar "I am part of the newspaper club, where me and my only friends would go around and write about anything notable we encountered. I don't actually care about reporting or writing, I just like to slack off with my friends." 
    nar "Though I do like reading, or more accurately, love reading. Too much for my own good it turned out as reading all night long had thrown off my sleep schedule causing me to wake up later than usual."
    
    call char_jay_update

    scene bg schoolexterior
    show jay animation_talk at right
    nar "I arrived just in time at the front gates of the school. With a sigh of relief I walked through the door of Leadville high."
    
    scene bg classroom
    show jay animation_talk at right   
    nar "Even though I was almost late, I still had time to relax. My teacher for my first class was always a little late, so I wasn't worried when I walked into class."

    play music "audio/Chaos Head OST Uneven Dance.mp3" volume 0.5 fadeout 1.5 fadein 3.0

    nar "I slumped into my chair. my classmates appeared to be mingling and chatting as usual... but something was off about the atmosphere of the room, and I can't seem to place what it is."

    i "Hey!" 
    nar "I turned my head towards the cheerful voice."
    show kit armscrossed at right
    nar "It was Kit, one of my friends from the newspaper club." 

    call char_screen_update
    call char_kit_update

    kit "..."
    show kit explaining 2 right at right
    kit "I saw you run by through the window... almost late it seems." 
    nar "Kit teased me."
    jay "Yeah, yeah"
    nar "I groaned as I slumped my face between my arms, which I had crossed on my desk." 
    jay "I spent all night reading."
    show kit armscrossed at right
    kit "You sure do love your books, huh?" 
    nar "Kit sighed."
    nar "Before I could respond the door creaked open. Our teacher had just arrived to class earlier than she usually did." 
    show kit sigh
    kit "Oh shit."
    nar "he turned back towards his own desk not wanting to get caught away from it. But before he got even a foot away from me he froze and turned his head back to me." 
    kit "By the way... I got some big info to share with everyone in the club tonight, be ready." 
    nar "He smirked and continued to his desk before the teacher started to take attendance."
    hide kit
    nar "Kit always had interesting things to bring up during club, but this time he said this in a more uneasy tone than that was his usual voice." 
    nar "I assumed he was adding more intrigue to really get me riled up. Knowing Kit, he had probably already riled up the others in their club as well. One thing I was expecting was that they weren't getting any work done for the newspaper today."
    nar "I was almost too lost in thought that I almost missed my cue when my name was called for attendance. After my name was called I relaxed back in my chair and continued to observe my classmates." 
    nar "Kit was twirling his pencil, not paying attention to the teacher."
    nar "Nothing new there, but it wasn't just Kit; it was almost everyone in class."
    nar "Of course, there were a few overattentive students still focusing, but most others were whispering and passing notes to each other."
    nar "They couldn't seem to shut up about something, and they weren't hiding it either." 
    nar "Our teacher started out annoyed at all the chatter, throwing a few 'Quiet down' or 'stop that's at the troublemaking students but gradually gave up on trying to make the class listen to her with less and less objections as the class went on." 
    nar "When I had noticed that the only authority in the room had abandoned all attempts at regulation I started to feel left out on whatever this was."
    nar "I whispered to the girl seated to the left of me, I think her name was Neda if I remembered correctly."
    show neda armhug at left

    call char_neda_update

    jay "Hey, what's everyone talking about?" 
    nar "She leaned towards me and cupped her hand around the side of her mouth."
    neda "You haven't heard? Did you not watch the news this morning or something?"
    jay "No, I woke up late, what happened?"

    stop music fadeout 1.0

    neda "..."
    neda "Well..." 
    nar "she whispered cautiously."
    neda "They're calling it the Human Kebab."

    hide neda
    scene bg blank

    $ renpy.movie_cutscene("images/videos/animation v03.webm", delay=None, loops=0, stop_music=True)
   
    scene bg cafiteria 
    show jay animation_talk at right
    play music "audio/Chaos Head OST Beginning Of Attachment.mp3" volume 0.5 fadein 2.0

    nar "I sat staring out the window during lunch as my nachos got cold." 
    nar "I shivered again as he had done many times since his first class. The human kebab is what was on my mind." 
    nar "I hadn't seen any pictures so he could only use his imagination. I reviewed what had been told to him by different people he talked to over the course of the mourning."
    nar "I tried to compile all the information in my mind." 
    nar "In short it was a murder case: a very disturbing one. Last night a body had been found in an alley, with its limbs severed and all the pieces impaled onto a piece of rebar in a fashion that resembled a kebab, as the name implies." 
    nar "It was a truly gruesome sight with blood splattered everywhere. Suicide was ruled out almost immediately and it was determined that the murder clearly happened on location." 
    nar "The body was so disfigured that the police hadn't been able to identify it. Apparently there was no evidence left behind either, or at least none has been found left behind." 
    i "The killer is said to still be on the loose... and no one knows why they did it"
    nar "I heard from one classmate nearby"
    i "Who knows if or when they could strike again"
    nar "I heard from another"
    nar "On another note, an announcement had been given during my second class that tomorrow there would be an assembly to discuss how to keep yourself safe and what to do if you see someone suspicious. They also said not to go in public alone, especially at night."
    nar "When I left lunch for my next class, I was hoping that the murderer was caught before I had to waste any time at an assembly." 

    scene bg classroom
    show jay animation_talk at right

    nar "When I sat down at my desk, I checked my watch, only to realize I had left it during my rush in the morning." 
    jay "Dammit"
    nar "I took out my flip phone to check the time instead." 
    nar "1:03."
    nar "Only 2 more classes until I was free form this torture and could forget all of today's absurdity." 
    nar "I let his mind wander to his friends, Kit, Vida, Andrea, and James, all laughing at some stupid joke together." 
    nar "It had only been a weekend since they had been together, but I felt like I hadn't seen them in forever." 
    nar "I also think that I need them more than ever, after all it was only the start of the week and so much had happened already."

    scene bg hallway
    show jay animation_talk at right

    nar "I walked through the hallways after my last class of the day..."
    nar "I looked around at the walls, which were covered with signage for different school clubs."
    nar "The walls were painted white and maroon red, supposedly the colors of the school mascot. Although Leadville high had infamously failed in sports so they hadn't used a mascot in many years. I couldn't even remember what the mascot was supposed to be."
    nar "I climbed the stairs, passed a group of gossiping girls and continued to the second floor."
    nar "That was where the newspaper club was located. I stopped at the top of the stairs to look at a billboard filled with more posters."
    nar "I often found myself looking at the board in my free time. This one had everything: all the clubs, student jobs, class openings, anything a student could ask for." 
    nar "Well, almost anything, as there sat an empty spot where the newspaper club was supposed to post their contribution to the school."
    nar "It was barren, and had been for a while. Me and my friends didn't really put in the work for the newspaper so we haven't actually produced anything in a long while."
    nar "Although no one seemed to care that it was absent so I thought 'why bother?'" 
    nar "I continued to scan the board until he saw the words 'Human Kebab'."
    
    play  music "audio/Chaos Head OST Qualm.mp3" volume 0.25 fadeout 2.0 fadein 3.0

    nar "I lowered my head to the ground and turned down the rest of the hallway. I couldn't deal with whatever else it said, I just couldn't handle it right now." 
    nar "I marched onwards toward the door with the hanging sign that read 'Newspaper Club'."

    scene bg classroom 2
    show jay animation_talk at right
    play music "audio/background music 1.mp3" volume 0.5 fadeout 0.5 fadein 1.0 

    nar "When I walked into the club room, most of the other members were already there." 
    show vida behindback at left
    nar "Vida leaned against the wall next to a rollable whiteboard."

    call char_vida_update

    show andrea peacesign at center
    nar "Andrea was sitting in a chair at the rectangular table in the center of the room."
    show andrea onearmonhip at center

    call char_andrea_update

    show kit armscrossed at right
    nar "Kit sitting atop the same table." 
    nar "While I entered the cluttered room, he looked around and noticed that someone was missing." 
    jay "Where's James?"
    nar "James was the unofficial leader of the group and the president of the club." 
    nar "I recalled the first time I and James met, James was incredibly helpful when no one else noticed me struggling to carry... carry what? I can't remember exactly..."
    nar "I decided to ignore it, what matters is that James was friends with everyone here individually first then he introduced everyone to each other. Therefore having a meet up without him felt a little awkward for me."
    andrea "He hasn't come in yet." 
    nar "She was tapping away at her phone. She leaned back in her chair with her legs on the table in the center of the room."
    vida "No one's seen him all day."
    show kit shrug at right
    kit "He might be sick."
    nar "Kit said while smiling at me, though to me the smile looked more like a frown. As Kit was lying on his back with his head hanging over the edge of the table."
    nar "Kit continued to smile at me, then when he got no feedback on his quirky position he tried again with Andrea and Vida."
    show kit sigh at right
    kit "Y'all are no fun..."
    show kit hurt at right
    show andrea smug at center
    nar "He turned over onto his stomach, only to be kicked on the head by Andrea, who showed her full appreciation to Kits stunt with a smug grin of her own."
    show kit angry at right
    nar "While the two friends bickered in the background, Vida turned to me."
    vida "I hope it isn't bad."
    jay "Huh? Oh right, James..."
    nar "I was briefly distracted by the argument happening beside us."
    jay "Knowing him, it won't keep him down for lon-"
    show kit explaining right at right
    show andrea onearmonhip at center
    kit "Alrighty then!" 
    nar "Kit shouted, cutting me off." 
    nar "He turned around, seemingly mid conversation with Andrea, and climbed atop the table he had once been lying on. He turned, once again, to address his audience of three newspaper club members." 
    kit "Since James isn't here, we'll have to start without him!"
    jay "Start what?" 
    nar "Kit crouched down and leaned towards me." 
    kit "Our venture to make the newspaper club relevant again!"
    jay "No one cares about the school newspaper anymore..."
    vida "No one has ever cared about it."
    nar "Kit ignored her and continued talking."
    kit "That's a problem because I heard that the school is gonna start closing clubs that they deem unnecessary, so we have to make sure we're not on that list."
    andrea "Wait, so the club could be disbanded!?"
    kit "It's not..."
    kit "Because I have a plan, all we have to do is make people read a paper we put out and the school will automatically accept us."
    jay "Ok..."
    jay "That makes sense..."
    jay "But what could we write about to ever make people read the paper?" 
    andrea "That would require us to do work though..."
    vida "What is there even to write about in this school?"
    nar "The group continued to question each other for a little while as Kit watched with an eager grin on his face."
    kit "Silence!" 
    kit "I have everything laid out already!"
    andrea "Where?" 
    nar "Vida sarcastically asked." 
    kit "In my head."
    nar "He acknowledged her for the first time in a while. The room was silent for a moment with everyone staring at Kit." 
    kit "I have the perfect topic that will make everyone read our paper..."
    show kit explaining 2 right at right 
    nar "He jumped off the table he was still atop and landed in front of a crowd eager for him to get to the point."
    kit "It will keep our club alive and well, while being relatively low effort!" 
    nar "He said turning toward Vida for the last part."
    jay "Well what is the topic?" 
    nar "I asked, annoyed with Kit's shenanigans."

    play  music "audio/Chaos Head OST Qualm.mp3" volume 0.25 fadeout 2.0 fadein 5.0

    nar "Kit leaned in the direction of Jay and slowly turned his head to also face him."
    nar "He whispered..."
    kit "The Human Kebab..."
    show andrea nervous at center
    show vida nervous at left
    jay "What!!"
    vida "..."
    andrea "..."
    jay "Can't we just do an article about the status of the school's water fountains?"
    nar "I asked half jokingly."
    nar "It was clear the three of us had worries about covering the topic. Though Kit waved his hands as if to calm them down."
    kit "Just think about it... it's the talk of the town... so everyone will read the paper!"
    kit "Also we can't get in trouble for covering it because we can force an outcry from the students if the teachers try to take it down..."
    kit "It's almost guaranteed to garner attention to the club!"
    show kit armscrossed at right
    nar "We all thought about it for a minute."
    andrea "I hate to admit it but you might have come up with a good idea..."
    nar "Vida nodded."
    nar "I was still concerned  while I tried to think of a way out of this."
    jay "B-But since it's so popular... Everyone already knows everything about it from the news... so there's no use in us covering it... right?" 
    nar "I watched my friends' faces and saw Vida and Andrea seem to reconsider the idea..."
    nar "but all hopes of getting out of this were shattered when Kit uttered the words"
    show kit smug at right
    kit "I haven't yet shared what I told you all about this morning..."

    menu:
        "I feel uneasy, so I decide to..."
        
        "Hear what Kit has to say.":
            jump hear_what_kit_has_to_say

        "Walk out of the room.":
            jump walk_out_of_the_room

label walk_out_of_the_room:

    hide vida
    hide andrea
    hide kit
    scene bg hallway
    show jay animation_talk at right

    nar "I left the club room..."
    nar "I couldn't handle this anymore..."
    nar "My friends whom I had usually found comfort in had started to make me uncomfortable."
    vida "Jay!"
    vida "Wait up!"

    menu:
        jay "..."

        "Wait for Vida":
            jump wait_for_vida

        "Leave":
            jump walk_out_of_school

label walk_out_of_school:

    jay "I'm sorry vida... but I need some fresh air right now."
    vida "Ok then. Well I'll see you later, maybe tomorrow."
    vida "Bye for now... and stay safe."




    e "Not done yet."

    return 

##
define wait_for_vida = False
##
label wait_for_vida:

    $ wait_for_vida = True

    nar "I stand still and turn to face Vida."
    show vida nervous at center
    vida "Are you ok Jay?"
    vida "You walked out all of a sudden..."
    jay "Y-yeah... I'm alright, just needed a second to think."
    vida "Is it about the murder?"
    jay "Yes. I'm just a little concerned about covering it."
    show vida explaining at center
    vida "Well I am too, but I think whatever Kit knows will help keep the club afloat."
    vida "How about we go back to the club room and at least listen to what he has to say."
    vida "Ok?" 

    menu:
        nar "I think about it and decide to..."

        "Walk back to the club room":
            jump hear_what_kit_has_to_say

        "Leave":
            jump walk_out_of_school


label hear_what_kit_has_to_say:

    if wait_for_vida:
        
        scene bg classroom 2
        show kit armscrossed at right
        show andrea neutral at center
        show vida behindback at left

        kit "You good Jay?"
        andrea "Yeah is everything alright?"
        jay "Yeah yeah I'm fine..."
        jay "Can we just continue from where we left off?"
        kit "Of course! Let me tell you all what I know!"
        kit "It's something that will definitely save our club!"
        nar "He leaned in and smiled." 

    show kit smug at right
    kit "I know where the human kebab murder happened..."
    show vida nervous at left
    show andrea nervous at center
    nar "Kit whispered."
    nar "The rest of us in the club room couldn't even speak."
    vida "H-how?"
    kit "I was hoping you would have asked where... To answer your question..."
    kit "I was watching the news about it when I noticed something in the alley that looked familiar." 
    jay "What was it?" 
    kit "I saw a sign in the background that had a sticker on it."
    show kit handing sticker
    nar "Kit reached into his pocket and pulled out a sticker with a bird emblem on it."
    kit "This sticker." 
    nar "The three of us stood there shocked, before we could say anything Kit explained."
    kit "This is from the same pack of stickers I had as a kid. I used to take a shortcut to school through some alleyways and placed these stickers along the way in case I got lost."
    kit "So years ago I must have placed that sticker next to where the murder recently took place."
    show kit raised arms at right
    nar "He leaned back in his chair and pumped both his hands in the air."
    kit "Which means! I know where it happened..."

    stop music
    hide kit
    hide andrea
    hide vida
    scene bg blank

    nar "The next day, all four of us were standing on the rooftop of a building during sunset."

    scene bg rooftop 1
    play  music "audio/rooftop wind sound.mp3" volume 0.5 fadeout 2.0 fadein 2.0

    jay "I can't believe you convinced me to do this..." 
    show kit armscrossed at center
    kit "You don't want the club to be disbanded, do you?" 
    hide kit
    nar "Kit made the jump from one rooftop to the next."
    jay "So what's the plan again?"
    show andrea armsonhips at left
    andrea "Find murder site, find new info, write paper, profit." 
    nar "Andrea said as she was jumping in place in order to prepare herself for the jump. The jump itself was only around two feet but still felt massive when they were so high up." 
    show vida wave at right
    vida "How many of these jumps do we have to do?"
    nar "She said already on the other side of the gap."
    show kit raised arms at center
    kit "I don't know!"
    nar "Kit shouted cheerfully. This was not what Jay expected to be doing instead of today's assembly."
    jay "You sure we should be doing this, it's technically still school hours?"
    show kit sigh at center
    kit "Stop worrying, you didn't want to go to it anyways, and we have to strike the iron while it's hot." 

    menu:
        "I thought about it, standing on the roof across from my friends."

        "Take the Jump.":
            jump jump_along_rooftops 

        "Leave now.":
            jump walk_away_from_rooftops

   
label jump_along_rooftops:

    vida "Just come on already, it will be fine!"
    nar "I took a set back, hesitated, and launched myself forward over the gap."

    hide andrea
    hide kit
    hide vida

    nar "The four of us walked across rooftops and jumped over a few more gaps of various sizes."
    nar "I noticed on my watch that we had been traveling for about fifteen minutes."
    jay "Hey, Kit. Are we almost there?"
    show kit smug at center
    nar "Kit took a few more steps, turned around and smiled."
    kit "We're here."

    play  music "audio/Chaos Head OST Qualm.mp3" volume 0.5 fadeout 2.0 fadein 3.0

    nar "We stood at the edge of a rooftop with an alleyway down below behind us. Kit and Andrea crouched down and peered over the edge looking into the darkness below." 
    hide kit
    scene bg blank
    kit "Damn I can't see anything."
    nar "Suddenly they all heard footsteps down below." 
    jay "Quiet..."
    nar "I whispered as I examined the alleyway below."
    vida "That is why we're up here, I guess."
    nar "She whispered to Kit." 
    nar "We looked down below as two figures walked around the corner talking to each other. We couldn't make out what they were saying but they seemed to be the authorities as one man wore a police cap."
    scene bg alleyway 2
    nar "The two men held flashlights and scanned them over the alley; it featured garbage and debris, all of which was covered in dried blood."
    nar "It was definitely the murder site. From what he could see from the flashlights, he didn't know how they would have seen without them, in the alley there was no corpse so the victim must have already been removed."
    nar "Even without it the whole scene sent shivers down my spine."
    nar "Kit leaned his head sideways attempting to hear what the men were saying deep below them. To avoid the disgusting scene below me and my friends I looked towards his left at the crossroad of the alley, and there was the sign Kit had mentioned."
    nar "Supposedly it had a sticker on it, though it was so dark out he couldn't tell."
    andrea "I think I can still smell it from here..."
    nar "I sniffled subtly and almost threw up. It smelled so bad."
    nar "I couldn't help but look down into the alley in search of the source of the smell, refusing to believe such a smell could come from such a cause."
    nar "As I tried to focus on the scene down below me I started to feel more sick and slowly everything became blurry as I stumbled backward before tripping causing me to fall onto my back."
    scene bg blank
    vida "Jay... Jay!" 
    nar "Everyone huddled around me as I was passing out."
    scene bg sky
    nar "The men in the alley shined their flashlights up towards the rooftop to the sound of Jay falling over. This let me see... something... in the sky, illuminated by the flashlights, before my eyes fully closed."


    e "Not done yet."

    return

label walk_away_from_rooftops:

    e "Not done yet."


    # This ends the game.

    return
