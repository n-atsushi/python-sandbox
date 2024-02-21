from logging import getLogger, Formatter, FileHandler, DEBUG, INFO
import logger
import os

# どのような形式でログを出力するかを設定する
formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# ログの保存先(ファイル名をしているす)
file_handler = FileHandler("sample.log")
file_handler.setFormatter(formatter)

#  ログを記録
main_logger = getLogger(__name__)
main_logger.addHandler(file_handler)
main_logger.setLevel(DEBUG)

main_logger.info(f"Runnging {os.path.basename(__file__)}")


# logger側のlogを呼び出す
sample_logger = getLogger("logger")
sample_logger.addHandler(file_handler)
sample_logger.setLevel(INFO)

logger.do_something()

