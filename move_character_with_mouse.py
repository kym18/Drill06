from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

def handle_events():
    global running, click_positions #클릭한 마우스 좌표
    global arrow_x, arrow_y #이동하는 마우스 좌표

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:      #안누름, 계속 그려.
            arrow_x, arrow_y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:  #그 자리에 그려. (리스트에 저장)-> 나중에 배열로 접근 ㅋ
                click_positions.append((event.x, TUK_HEIGHT - 1 - event.y))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def mouse_point():
    global arrow_x, arrow_y
    global click_positions

    arrow.draw(arrow_x, arrow_y)
    for pos in click_positions:
        arrow.draw(pos[0],pos[1])


def character_follow():
    global x, y
    global click_positions
    speed = 30

    if len(click_positions)> 0: #만약에 클릭한 마우스가 있다면
        target_x, target_y = click_positions[0]
    else:
        target_x, target_y = x, y

    # 캐릭터 이동시키기
    t = 0.1  # 보간 계수 (0.0에서 1.0 사이의 값)
    x = (1 - t) * x + t * target_x
    y = (1 - t) * y + t * target_y

    #캐릭터 좌우방향 변경 ㅋ.ㅋ
    if (target_x >= x): #right
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif (target_x < x):
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

    # 화살표 제거
    dis = math.sqrt((target_x - x) ** 2 + (target_y - y) ** 2)
    if dis < 10:
        if len(click_positions) > 0:
            click_positions.pop(0)  # 첫 번째 클릭 지점

#초기화
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
running = True
arrow_x, arrow_y = 0, 0
click_positions = []

frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character_follow()
    mouse_point()
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
    delay(0.05)

close_canvas()




