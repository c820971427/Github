import logging
import subModule

logger = logging.getLogger("mainModule")
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(console)

logger.info("creating an instance of subModule.subModuleClass")
a = subModule.SubModuleClass()
logger.info("calling subModule.subModuleClass.doSomething")
a.doSomething()
logger.info("done with  subModule.subModuleClass.doSomething")
logger.info("calling subModule.some_function")
subModule.som_function()
logger.info("done with subModule.some_function")

# import logging
# 
# 
# logger = logging.getLogger(__name__)
# logger.setLevel(level=logging.INFO)
# handler = logging.FileHandler("log.txt")
# handler.setLevel(logging.INFO)
# 
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# 
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# 
# logger.addHandler(handler)
# logger.addHandler(console)
# 
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# try:
#     open("sklearn.txt", "rb")
# except (SystemExit, KeyboardInterrupt):
#     raise
# except Exception:
#     logger.error("Faild to open sklearn.txt from logger.error", exc_info=True)
# 
# logger.info("Finish")



