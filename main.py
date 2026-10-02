
# 1. IMPORTS


import pygame

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASSETS = BASE_DIR / "assets"




# 2.pygame init


pygame.init()
pygame.mixer.init()

SCREEN= pygame.display.set_mode((800,600),pygame.FULLSCREEN| pygame.SCALED)
pygame.display.set_caption("ONE PIECE GAME BY KUNJAN")
clock=pygame.time.Clock()


# 3.audio and sound effects



pygame.mixer.music.load(str(ASSETS / "audio" / "music" / "Loading_Sound.mp3"))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)

luffy_start_sound=pygame.mixer.Sound(str(ASSETS / "audio" / "sfx" / "luffy_start.mp3"))
luffy_start_sound.set_volume(1)

luffy_arm_stretch=pygame.mixer.Sound(str(ASSETS / "audio" / "sfx" / "luffy-arm-stretch.mp3"))
luffy_arm_stretch.set_volume(0.7)

gatling_sound=pygame.mixer.Sound(str(ASSETS / "audio" / "sfx" / "gatlings.mp3"))
gatling_sound.set_volume(1)


luffy_jump=pygame.mixer.Sound(str(ASSETS / "audio" / "sfx" / "luffy_jump.mp3"))
luffy_jump.set_volume(0.5)

luffy_orewa=pygame.mixer.Sound(str(ASSETS / "audio" / "sfx" / "luffy-orewa.mp3"))
luffy_orewa.set_volume(1)

one_piece_sad=pygame.mixer.Sound(str(ASSETS / "audio" / "music" / "one-piece-sad.mp3"))
one_piece_sad.set_volume(1)


# 4. IMAGES

# ----for Luffy


luffy_idle =pygame.image.load(str(ASSETS / "characters" / "luffy" / "Left (Normal - Playable)" / "Split Sprites" / "idoling__idoling_01.png")).convert_alpha()
luffy_idle=pygame.transform.scale(luffy_idle, (120, 120))

luffy_left =pygame.image.load(str(ASSETS / "characters" / "luffy" / "Left (Normal - Playable)" / "Split Sprites" / "back.png")).convert_alpha()
luffy_left=pygame.transform.scale(luffy_left, (120, 120))

luffy_right =pygame.image.load(str(ASSETS / "characters" / "luffy" / "Right (Reversed - Enemy)" / "Split Sprites" / "go.png")).convert_alpha()
luffy_right=pygame.transform.scale(luffy_right, (120, 120))

luffy_attack11 =pygame.image.load(str(ASSETS / "characters" / "luffy" / "Left (Normal - Playable)" / "Split Sprites" / "attack_01.png")).convert_alpha()
luffy_attack11=pygame.transform.scale(luffy_attack11, (120, 120))
luffy_attack12 =pygame.image.load(str(ASSETS / "characters" / "luffy" / "Left (Normal - Playable)" / "Split Sprites" / "attack_02__finish__ready.png")).convert_alpha()
luffy_attack12=pygame.transform.scale(luffy_attack12, (120, 120))
luffy_attack13 =pygame.image.load(str(ASSETS / "characters" / "luffy" / "Left (Normal - Playable)" / "Split Sprites" / "attack_03.png")).convert_alpha()
luffy_attack13=pygame.transform.scale(luffy_attack13, (120, 120))


# ---- for Alvida

alvida1 = pygame.image.load(str(ASSETS / "characters" / "alvida" / "idle" / "alvida1.png")).convert_alpha()
alvida1 = pygame.transform.scale(alvida1, ((150, 150)))

alvida2 = pygame.image.load(str(ASSETS / "characters" / "alvida" / "idle" / "alvida2.png")).convert_alpha()
alvida2 = pygame.transform.scale(alvida2, ((150, 150)))

alvida3 = pygame.image.load(str(ASSETS / "characters" / "alvida" / "idle" / "alvida3.png")).convert_alpha()
alvida3 = pygame.transform.scale(alvida3, ((150, 150)))

alvida4 = pygame.image.load(str(ASSETS / "characters" / "alvida" / "idle" / "alvida4.png")).convert_alpha()
alvida4 = pygame.transform.scale(alvida4, ((150, 150)))

alvida5 = pygame.image.load(str(ASSETS / "characters" / "alvida" / "idle" / "alvida5.png")).convert_alpha()
alvida5 = pygame.transform.scale(alvida5, ((150, 150)))

alvida6 = pygame.image.load(str(ASSETS / "characters" / "alvida" / "idle" / "alvida6.png")).convert_alpha()
alvida6 = pygame.transform.scale(alvida6, ((150, 150)))

alvida7 = pygame.image.load(str(ASSETS / "characters" / "alvida" / "idle" / "alvida7.png")).convert_alpha()
alvida7 = pygame.transform.scale(alvida7, ((150, 150)))


# ---- for Backgrounds

bg_image = pygame.image.load(str(ASSETS / "backgrounds" / "loading.png")).convert_alpha()
bg_image = pygame.transform.scale(bg_image, ((800, 600)))

alvida_image = pygame.image.load(str(ASSETS / "characters" / "alvida" / "idle" / "alvida-ship.png")).convert_alpha()
alvida_image = pygame.transform.scale(alvida_image, ((800, 600)))




# 5. animation

# Luffy Gatling
luffy_attack2_frames = []
gatling_path =ASSETS/"characters"/"luffy"/"Left (Normal - Playable)"/"Assembled Sprites"/"motion_0002_attack"

for i in range(1, 46):
    full_path=gatling_path/f"{i}.png"
    frame_img =pygame.image.load(str(full_path)).convert_alpha()
    frame_img=pygame.transform.scale(frame_img, (400, 130))
    luffy_attack2_frames.append(frame_img)

# Alvida defeat
alvida_fall_frames = []
for i in range(1, 12):
    full_path2=ASSETS/"characters"/"alvida"/"fall"/f"alvida-fall-{i}.png"
    frame_img2= pygame.image.load(str(full_path2)).convert_alpha()
    frame_img2=pygame.transform.scale(frame_img2, (200, 100))
    alvida_fall_frames.append(frame_img2)

# Alvida attack
alvida_attack_frames = []
for i in range(1, 16):
    full_path3=ASSETS/"characters"/"alvida"/"attack"/f"alvida-attack-{i}.png"
    frame_img3 = pygame.image.load(str(full_path3)).convert_alpha()
    frame_img3 = pygame.transform.scale(frame_img3, (145, 150))
    alvida_attack_frames.append(frame_img3)


# 6. GAME VARIABLES


# Physics
vel_x=0
vel_y=0
speed=5
jump_force=-14
gravity=0.8
on_ground=False
fall_timer=0

# Player
luffy_x = 50
luffy_y = 210
luffy_rect = pygame.Rect(luffy_x, luffy_y, 120, 120)
luffy_hp = 100
luffy_resized = luffy_idle


# Combat
attack1 = False
attack2 = False
attack_frame = 0
attack_timer = 0
attack_frame2 = 0
attack_timer2 = 0


# Enemy
alvida_rect = pygame.Rect(600, 300, 150, 150)
alvida_hp = 500
alvida_frame = 0
alvida_timer = 0
alvida_fall_frame = 0
alvida_fall_timer = 0
alvida_attack_frame = 0
alvida_attack_timer = 0
healthbar = alvida_hp
alvida_attack=False

ending2_sound=True

# Game State
running = True
state = "loading"
orewa = False
pressed_keys = pygame.key.get_pressed()


# UI
font = pygame.font.SysFont("Arial", 24, bold=True)


# 7. MAIN GAME LOOP



while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
     if event.type==pygame.QUIT or keys[pygame.K_ESCAPE]:
        running=False

     if keys[pygame.K_F11] or keys[pygame.K_f]:
                pygame.display.toggle_fullscreen() 



# 8. GAME STATES

# Loading
    if state == 'loading':
     SCREEN.blit(bg_image, (0, 0))
     if keys[pygame.K_RETURN]:   
      state="menu"
      pygame.mixer.music.stop()

# Menu
    elif state == "menu":
        state="arc_select"

# Arc Select
    elif state == "arc_select":
        state="level"
        luffy_start_sound.play()
# Level
    elif state == "level":
        
            vel_x=0
            if  keys[pygame.K_LEFT] or keys[pygame.K_a]:
                vel_x=-speed
            if  keys[pygame.K_RIGHT] or keys[pygame.K_d]:
             vel_x=speed

            if  (keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]) and on_ground:
             vel_y=jump_force
             on_ground=False
             luffy_jump.play()

            if keys[pygame.K_j] and attack1==False:
             luffy_arm_stretch.play()
             attack1=True
             attack_frame = 0
             attack_timer=0
             if alvida_rect.x-luffy_rect.x<100:
                alvida_hp-=20

            elif keys[pygame.K_k] and attack2==False:
             gatling_sound.play() 
             attack2=True
             attack_frame2 = 0
             attack_timer2=0
             if alvida_rect.x-luffy_rect.x<275:
                alvida_hp-=50

            vel_y+=gravity
            if vel_x < 0:
             luffy_resized = luffy_left   
            elif vel_x > 0:
             luffy_resized = luffy_right  
            else:
             luffy_resized = luffy_idle

            luffy_rect.x +=vel_x
            luffy_rect.y +=vel_y

            if luffy_rect.left <0:
             luffy_rect.left=0
            if luffy_rect.right >640:
             luffy_rect.right=640
            if luffy_rect.bottom>=460:
             luffy_rect.bottom=460
             vel_y=0
             on_ground=True

            healthbar=alvida_hp
            SCREEN.blit(alvida_image, (0, 0))
            pygame.draw.rect(SCREEN,(80,20,20),(150,35,500,20))
            pygame.draw.rect(SCREEN,(255,30,30),(150,35,healthbar,20))
            pygame.draw.rect(SCREEN,(200,200,200),(150,35,500,20),2)
            pygame.draw.rect(SCREEN,(0,0,0),(355,530,90,26))
            hp_text = font.render(f"HP: {luffy_hp}", True, (0, 255, 0))
            hp_text2 = font.render("ALVIDA - CAPTAIN OF ALVIDA PIRATES", True,(255, 105, 180))
            hp_text2_black = font.render("ALVIDA - CAPTAIN OF ALVIDA PIRATES", True, (0, 0, 0))
            SCREEN.blit(hp_text2_black, (238, 10))
            SCREEN.blit(hp_text2_black, (242, 10))
            SCREEN.blit(hp_text2_black, (240, 8))
            SCREEN.blit(hp_text2_black, (240, 12))
            SCREEN.blit(hp_text2,(240,10))
            SCREEN.blit(hp_text,(355,530))

            if alvida_hp > 0:
             if abs(alvida_rect.x - luffy_rect.x) <= 100:
              alvida_attack = True
            
            
        

            if alvida_hp <= 0:
                alvida_fall_timer+=1
                SCREEN.blit(alvida_fall_frames[alvida_fall_frame], (alvida_rect.x, alvida_rect.y + 55))
                if orewa==False:
                  luffy_orewa.play()
                  orewa=True
                if alvida_fall_timer >=16:
                 alvida_fall_frame +=1
                 alvida_fall_timer=0
                if alvida_fall_frame >=len(alvida_fall_frames):
                  state="ending"

            elif luffy_hp<=0:
               state="ending2"
               if ending2_sound==True:
                one_piece_sad.play()
                ending2_sound=False

            elif alvida_attack==True:
                alvida_attack_timer+=1
                SCREEN.blit(alvida_attack_frames[alvida_attack_frame], (alvida_rect.x, alvida_rect.y+5))
                if alvida_attack_timer >=3:
                 alvida_attack_frame +=1
                 alvida_attack_timer=0
                if alvida_attack_frame >= 6<7:
                 if  abs(alvida_rect.x - luffy_rect.x) <= 100:
                  luffy_hp-=1
                if alvida_attack_frame >= len(alvida_attack_frames):
                 alvida_attack_frame = 0
                 alvida_attack = False

            else:               
                alvida_timer += 1
                if alvida_frame == 0:
                    SCREEN.blit(alvida1, alvida_rect)
                elif alvida_frame == 1:
                    SCREEN.blit(alvida2, alvida_rect)
                elif alvida_frame == 2:
                    SCREEN.blit(alvida3, alvida_rect)
                elif alvida_frame == 3:
                    SCREEN.blit(alvida4, alvida_rect)
                elif alvida_frame == 4:
                    SCREEN.blit(alvida5, alvida_rect)
                elif alvida_frame == 5:
                    SCREEN.blit(alvida6, alvida_rect)
                elif alvida_frame == 6:
                    SCREEN.blit(alvida7, alvida_rect) 
                if alvida_timer >= 14:
                    alvida_frame += 1
                    alvida_timer = 0
                if alvida_frame > 6:
                    alvida_frame=0


            
            if attack1 == True:
                attack_timer += 1
                if attack_frame == 0:
                    SCREEN.blit(luffy_attack11, luffy_rect)
                elif attack_frame == 1:
                    SCREEN.blit(luffy_attack12, luffy_rect)
                elif attack_frame == 2:
                    SCREEN.blit(luffy_attack13, luffy_rect)
                if attack_timer >= 6:
                    attack_frame += 1
                    attack_timer = 0
                if attack_frame > 2:
                    attack1 = False
            
            elif attack2 == True:
                attack_timer2 += 1
                SCREEN.blit(luffy_attack2_frames[attack_frame2], luffy_rect)
                if attack_timer2 >=2:
                 attack_frame2 +=1
                 attack_timer2 =0
                if attack_frame2 >=len(luffy_attack2_frames):
                    attack2 = False
                    attack_frame2 = 0


            else:
                SCREEN.blit(luffy_resized, luffy_rect)



# Ending
    elif state =="ending":
     SCREEN.fill((30,30,30))
     end_title = font.render("VICTORY!", True, (0, 255, 0))
     end_below = font.render("You defeated Captain Alvida! Press ENTER to restart.", True, (255, 255, 255))
     SCREEN.blit(end_title, (310,200))
     SCREEN.blit(end_below, (140,250))
     if keys[pygame.K_RETURN]:
            pygame.mixer.music.stop()    
            state="loading"
            alvida_hp = 500
            alvida_fall_frame = 0
            alvida_fall_timer = 0
            alvida_frame = 0
            alvida_timer = 0
            attack1 = False
            attack2 = False
            attack_frame = 0
            attack_frame2 = 0
            attack_timer = 0
            attack_timer2 = 0
            orewa = False
            luffy_rect.x,luffy_rect.y=100,100
 

    elif state =="ending2":
     SCREEN.fill((30,30,30))
     end_title = font.render("LOSTTTT!", True, (255, 0, 0))
     end_below = font.render("You lost from Captain Alvida! Press ENTER to restart.", True, (255, 255, 255))
     SCREEN.blit(end_title, (310,200))
     SCREEN.blit(end_below, (140,250))
     if keys[pygame.K_RETURN]: 
        pygame.mixer.music.stop()  
        one_piece_sad.stop()
        state="loading"
        luffy_hp=100
        alvida_hp = 500
        alvida_fall_frame = 0
        alvida_fall_timer = 0
        alvida_frame = 0
        alvida_timer = 0
        attack1 = False
        attack2 = False
        attack_frame = 0
        attack_frame2 = 0
        attack_timer = 0
        attack_timer2 = 0
        orewa = False
        ending2_sound = True
        luffy_rect.x,luffy_rect.y=100,100
   



# 9. DISPLAY UPDATE AND QUIT


    pygame.display.flip()
    clock.tick(60)
pygame.quit()