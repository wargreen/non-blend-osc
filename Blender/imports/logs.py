from sys import stdout
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO

logger = getLogger()

logger.setLevel(DEBUG)

handler = StreamHandler(stdout)

formatter = Formatter(
	"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

handler.setFormatter(formatter)

logger.addHandler(handler)


class Logged:
	def __init__(self, _logger=logger):
		self.logger = _logger.getChild(self.__class__.__name__)
		
	def debug(self, *args, **kwargs):
		self.logger.debug(*args, **kwargs)
		
	def info(self, *args, **kwargs):
		self.logger.info(*args, **kwargs)
