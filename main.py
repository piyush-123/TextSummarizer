from TextSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} finished <<<<")
except Exception as e:
    logger.ecxeption(e)
    raise e


