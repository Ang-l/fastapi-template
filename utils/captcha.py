
import random
import os
import base64

from PIL import Image, ImageDraw, ImageFont


current_directory = os.getcwd()

init_config = {
    "bg_paths": [
        os.path.join(current_directory, "static/images/captcha/click/bgs/1.png"),
        os.path.join(current_directory, "static/images/captcha/click/bgs/2.png"),
        os.path.join(current_directory, "static/images/captcha/click/bgs/3.png")
    ],
    "font_paths": [
        os.path.join(current_directory, "static/fonts/zhttfs/SourceHanSansCN-Normal.ttf"),
    ],
    "icon_dict": {
        'aeroplane': '飞机',
        'apple': '苹果',
        'banana': '香蕉',
        'bell': '铃铛',
        'bicycle': '自行车',
        'bird': '小鸟',
        'bomb': '炸弹',
        'butterfly': '蝴蝶',
        'candy': '糖果',
        'crab': '螃蟹',
        'cup': '杯子',
        'dolphin': '海豚',
        'fire': '火',
        'guitar': '吉他',
        'hexagon': '六角形',
        'pear': '梨',
        'rocket': '火箭',
        'sailboat': '帆船',
        'snowflake': '雪花',
        'wolf head': '狼头',
    },
    "length": 4,
    "arr_len": 2,
    "zhSet": "这里显示的是中文哈啊我就饿得我看到拿到"
}


class Captcha:
    def __init__(self, config=init_config, expire=300):
        self.config = config
        self.expire = expire
        self.bg_paths = self.config['bg_paths']
        self.font_paths = self.config['font_paths']
        self.icon_dict = self.config['icon_dict']

    def create(self, id: str):
        bg_path = random.choice(self.bg_paths)
        font_path = random.choice(self.font_paths)
        image = Image.open(bg_path)
        draw = ImageDraw.Draw(image)
        num_text = self.config['length']
        num_icons = min(len(self.icon_dict), num_text)
        num_text_chars = num_text - num_icons

        # ####### Select the text information, if necessary, it can be adjusted to any type of text such as Chinese, etc.
        text = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=num_text_chars))
        icons = random.sample(list(self.icon_dict.keys()), num_icons) if num_icons > 0 else []

        rand_points = list(text) + icons
        random.shuffle(rand_points)

        text_arr = []

        icon_base_path = os.path.join(current_directory, 'static/images/captcha/click/icons/')

        occupied = []

        for v in rand_points:
            tmp = {}
            tmp['size'] = random.randint(15, 30)

            if v in self.icon_dict:
                # #### Draw Icon
                icon_path = os.path.join(icon_base_path, f"{v}.png")
                if os.path.exists(icon_path):
                    icon = Image.open(icon_path)
                    icon_width, icon_height = icon.size

                    placed = False
                    while not placed:
                        x = random.randint(0, image.width - icon_width)
                        y = random.randint(0, image.height - icon_height)
                        if all(not self._is_overlapping(x, y, icon_width, icon_height, ox, oy, ow, oh) for (ox, oy, ow, oh) in occupied):
                            image.paste(icon, (x, y), icon.convert('RGBA'))
                            tmp['icon'] = True
                            tmp['name'] = v
                            tmp['text'] = f"<{self.icon_dict[v]}>"
                            tmp['width'] = icon_width
                            tmp['height'] = icon_height
                            tmp['x'] = x
                            tmp['y'] = y
                            occupied.append((x, y, icon_width, icon_height))
                            placed = True
                else:
                    tmp['icon'] = False
                    tmp['text'] = v
                    tmp['width'] = 0
                    tmp['height'] = 0
                    tmp['x'] = 0
                    tmp['y'] = 0
            else:
                # ###### Drawing Text
                font = ImageFont.truetype(font_path, tmp['size'])
                text_width, text_height = draw.textsize(v, font=font)

                placed = False
                while not placed:
                    x = random.randint(0, image.width - text_width)
                    y = random.randint(0, image.height - text_height)
                    if all(not self._is_overlapping(x, y, text_width, text_height, ox, oy, ow, oh) for (ox, oy, ow, oh) in occupied):
                        draw.text((x, y), v, font=font, fill=(239, 239, 234))
                        tmp['icon'] = False
                        tmp['text'] = v
                        tmp['width'] = text_width
                        tmp['height'] = text_height
                        tmp['x'] = x
                        tmp['y'] = y
                        occupied.append((x, y, text_width, text_height))
                        placed = True

            text_arr.append(tmp)

        # ####### Split the first two into select answers
        text_arr = text_arr[:self.config['arr_len']]
        text = [item['text'] for item in text_arr]

        # ###### Save the image locally and delete it if necessary
        image_filename = os.path.join(os.path.join(current_directory, "static/images/temporary/"), f"{id}.png")
        image.save(image_filename, format="PNG")

        with open(image_filename, "rb") as img_file:
            base64_image = base64.b64encode(img_file.read()).decode()

        os.remove(image_filename)

        return {
            'id': id,
            'text': text,
            'base64': 'data:image/png;base64,' + base64_image,
            'width': image.width,
            'height': image.height,
            'text_arr': text_arr
        }

    # ########### Collision detection to avoid icon overlap
    @classmethod
    def _is_overlapping(cls, x1, y1, w1, h1, x2, y2, w2, h2):
        return not (x1 > x2 + w2 or x1 + w1 < x2 or y1 > y2 + h2 or y1 + h1 < y2)

    @classmethod
    def parse_user_clicks(cls, user_click_data_str):
        parts = user_click_data_str.split(';')

        coords_str = parts[0]
        image_width = int(parts[1])
        image_height = int(parts[2])
        click_coords = coords_str.split('-')
        click1_x, click1_y = map(int, click_coords[0].split(','))
        click2_x, click2_y = map(int, click_coords[1].split(','))

        return [(click1_x, click1_y), (click2_x, click2_y)], (image_width, image_height)

    @classmethod
    def is_within_tolerance(cls, user_coord, correct_coord):
        # 容错范围为图标的宽度和高度
        tolerance_x = correct_coord['width']
        tolerance_y = correct_coord['height']

        return (abs(user_coord[0] - correct_coord['x']) <= tolerance_x and
                abs(user_coord[1] - correct_coord['y']) <= tolerance_y)

    @classmethod
    def validate_click(cls, user_click_data_str, correct_coords):
        try:
            user_clicks, _ = cls.parse_user_clicks(user_click_data_str)
        except ValueError as e:
            return False

        # 确保用户点击数量与正确坐标数量一致
        if len(user_clicks) != len(correct_coords):
            return False

        # 确保每个用户点击坐标都与对应的正确坐标匹配
        for i, user_click in enumerate(user_clicks):
            correct_coord = correct_coords[i]
            if not cls.is_within_tolerance(user_click, correct_coord):
                return False

        return True
