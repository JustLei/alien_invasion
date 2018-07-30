class GameStats():
	"""跟踪游戏的统计信息"""

	def __init__(self,ai_settings):
		"""初始化统计信息"""
		self.ai_settings = ai_settings

		#存储最高分的文件
		self.save_high_score_file = "high_score.txt"

		self.reset_stats()
		
		#游戏刚启动时处于非活动状态
		self.game_active = False

		#在任何情况下都不应该重置最高分
		self.read_high_score()

	def  reset_stats(self):
		"""初始化在游戏运行期间可能变化的统计信息"""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 0

	def save_high_score(self):
		"""在退出游戏前将最高分保存到文件中"""
		with open(self.save_high_score_file,'w') as file_object:
			file_object.write(str(self.high_score))

	def read_high_score(self):
		"""在游戏开始时将最高分从文件中读入"""
		with open(self.save_high_score_file) as file_object:
			self.high_score = int(file_object.read())
