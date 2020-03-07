from src.imagemeasure import initial_form, measurement_picker
from src.monsters import monstercomparison
from src.statgen import statGenerator

name = initial_form.survey()
front_path = initial_form.select_front_image()
side_path = initial_form.select_side_image()

measurement_picker.make_measurements(front_path, side_path, name)


stats = statGenerator.genStats()
monstercomparison.makeMonster(stats[0], stats[1], stats[2], stats[3], stats[4], stats[5])
initial_form.complete()