class Animation():
    def __init__(self):  
        self.anim_field = {
            "email_login": {"new_y": 0, "new_x": 0, "new_height": 0, "new_width": 0, "text_size": 0},
            "password_login": { "new_y": 0, "new_x": 0, "new_height": 0, "new_width": 0, "text_size": 0},
            "email": {"new_y": 0, "new_x": 0, "new_height": 0, "new_width": 0, "text_size": 0},
            "password": { "new_y": 0, "new_x": 0, "new_height": 0, "new_width": 0, "text_size": 0},
            "name": { "new_y": 0, "new_x": 0, "new_height": 0, "new_width": 0, "text_size": 0},
            "surname": { "new_y": 0, "new_x": 0, "new_height": 0, "new_width": 0, "text_size": 0},
            "username": { "new_y": 0, "new_x": 0, "new_height": 0, "new_width": 0, "text_size": 0}
        }

    def text_input(self, rect, input, text, x, y, width, height, id):
        if self.is_mouse_over_button(rect) or input != "":
            if self.anim_field[id]["new_y"] < height / 2:
                self.anim_field[id]["new_x"] += width / 6
                self.anim_field[id]["new_y"] += height / 2
                self.anim_field[id]["new_width"] += width / 2
                self.anim_field[id]["new_height"] += height / 2
                self.anim_field[id]["text_size"] += 1
            self.rect_full(self.green2, (x - self.anim_field[id]["new_x"]), y - self.anim_field[id]["new_y"], width - self.anim_field[id]["new_width"], height - self.anim_field[id]["new_height"], 5)
            self.rect_border(self.white, (x - self.anim_field[id]["new_x"]), y - self.anim_field[id]["new_y"], width - self.anim_field[id]["new_width"], height - self.anim_field[id]["new_height"], 2, 5)
            self.text_center(self.font4, 13 - self.anim_field[id]["text_size"], text, self.white, (x - self.anim_field[id]["new_x"]), y - self.anim_field[id]["new_y"])

        else:
            if self.anim_field[id]["new_y"] > 0:
                self.anim_field[id]["new_x"] -= width / 6
                self.anim_field[id]["new_y"] -= height / 2
                self.anim_field[id]["new_width"] -= width / 2
                self.anim_field[id]["new_height"] -= height / 2
                self.anim_field[id]["text_size"] -= 1
                self.rect_border(self.black, (x - self.anim_field[id]["new_x"]), y - self.anim_field[id]["new_y"], width - self.anim_field[id]["new_width"], height - self.anim_field[id]["new_height"], 2, 5)
            self.rect_full(self.green2,(x - self.anim_field[id]["new_x"]), y - self.anim_field[id]["new_y"], width - self.anim_field[id]["new_width"], height - self.anim_field[id]["new_height"], 5)
            self.text_center(self.font4, 15 - self.anim_field[id]["text_size"], text, self.white,(x - self.anim_field[id]["new_x"]), y - self.anim_field[id]["new_y"])
