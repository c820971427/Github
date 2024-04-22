import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s- %(name)s - %(levelname)s - %(message)s')
loggerMCU = logging.getLogger('MCU')
loggerRun = logging.getLogger('Run')

loggerMCU.info('start print log')
loggerMCU.debug('debug something')
loggerMCU.warning('something may be wrong')
loggerMCU.info('finish')
loggerRun.info('start print log')
loggerRun.debug('debug something')
loggerRun.warning('something may be wrong')
loggerRun.info('finish')

loggerNew = logging.getLogger('SWMU')
loggerNew.setLevel(level=logging.INFO)
handler = logging.FileHandler("SWMUlog.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(filename)s- %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
loggerNew.addHandler(handler)


loggerNew.info("Start print log")
loggerNew.debug("Do something")
loggerNew.warning("Something maybe fail.")
loggerNew.info("Finish")
