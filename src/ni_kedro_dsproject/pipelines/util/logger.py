import logging
    
def logging_node(result):
    # ロガーを取得
    logger = logging.getLogger('kedro.pipeline.node')

    # 結果をログに出力
    logger.info(f'Result: {result}')