from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

def handle_events():
    global running, click_positions
    global arrow_x, arrow_y
    global check

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            #안누름, 계속 그려.
            arrow_x, arrow_y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                #그 자리에 그려. (리스트에 저장)-> 나중에 배열로 접근 ㅋ
                click_positions.append((event.x, TUK_HEIGHT - 1 - event.y))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def follow_hand():
    global arrow_x, arrow_y
    global check, click_positions

    arrow.draw(arrow_x, arrow_y)
    for pos in click_positions:
        arrow.draw(pos[0],pos[1])



running = True
arrow_x, arrow_y = 0, 0
click_positions = []
check = 1

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    follow_hand()
    update_canvas()
    handle_events()
    delay(0.05)

close_canvas()




